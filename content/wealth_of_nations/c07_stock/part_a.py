"""Stock, Money and Banks, lessons 1-5 -- Book II, the Introduction and Chapters 1-2.

Every quotation is copied from /mnt/project-files/wealth-texts/wealth-of-nations-psu.txt
(the Electronic Classics Series edition, Pennsylvania State University, 2005);
the line numbers in the comments are that file's. Chapter 2 is long and is read in
three lessons: gross and net revenue, paper money, and drawing and redrawing.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # PSU text l. 8834-8905 (Book II, Introduction). l. 8836-8844 (the rude
    # state); l. 8851-8859 (the weaver); l. 8860-8876 (division needs stock);
    # l. 8877-8889 (stock leads to division); l. 8892-8905 (the plan of the Book).
    {
        "slug": "stock-must-be-accumulated-first",
        "title": "Stock Must Be Accumulated First",
        "module": "Book II, Introduction · Of the Nature, Accumulation, and Employment of Stock",
        "one_line": "A weaver cannot give himself to weaving until a stock of food, yarn and tools is laid up to carry him until his web is sold, and the more labour is divided, the more stock that takes.",
        "summary": (
            "Book II begins with a short Introduction that turns the first book round. "
            "Division of labour, Smith says, needs a stock stored up beforehand, and "
            "the stock needed grows as the labour is divided. Sort a weaver's stock into "
            "what he lives on, what he works with and what he works up, and watch which "
            "part must grow when the same workmen divide their work further."
        ),
        "key": [
            "first the stock, then the division of labour",
            "a weaver needs food, yarn and a loom first",
            "stock = consumption + fixed + circulating",
            "division: same food, more materials and tools",
            "stock employed leads to division",
        ],
        "key_label": "The Introduction in five lines",
        "concepts_intro": (
            "The Introduction is two pages long and has three moves: an order of events, "
            "a proportion, and a motive."
        ),
        "concepts": [
            ("Stock",
             "In Smith's word, stock is goods laid up, not money: food, clothes, "
             "materials, tools, anything stored beforehand. A person with stock enough "
             "for a few weeks lives on it; a person with stock enough for years can "
             "set part of it to work."),
            ("Accumulation before division",
             "When people live by exchanging the products of divided labour, no one can "
             "wait for the pay for his own work, because that pay comes only when the "
             "work is finished and sold. Someone must hold a stock to carry him over. "
             "That accumulation, Smith says, is previous to the division of labour."),
            ("Division draws on stock, and stock draws on division",
             "As labour is divided, the same workmen need the same provisions but more "
             "materials and tools. And whoever lays out a stock to employ labour wants "
             "the most work from it, so he divides the work and buys machines, in "
             "proportion to the stock he has."),
        ],
        "read_title": "The weaver first, then the plan of the Book",
        "read_intro": (
            "The Introduction opens on a world with no division of labour, where no stock "
            "is needed, and takes it away from the weaver one sentence at a time."
        ),
        "body": [
            ("p", "<strong>Book II, Introduction.</strong> In that rude state of "
                  "society, Smith begins, &ldquo;in which there is no "
                  "division of labour, in which exchanges are seldom made, and in which "
                  "every man provides every thing for himself, it is not necessary that "
                  "any stock should be accumulated, or stored up beforehand, in order to "
                  "carry on the business of the society.&rdquo;"),
            ("p", "That is the opening, and the first page of Book II is an argument about "
                  "what changes when it stops being true. In the rude state each man meets "
                  "each want as it comes: &ldquo;When he is hungry, he goes to the forest "
                  "to hunt; when his coat is worn out, he clothes himself with the skin of "
                  "the first large animal he kills&rdquo;. Nothing is stored because "
                  "nothing needs to be. His labour and his supper are the same event."),
            ("p", "Now divide the labour, which is where Book I left you. A man makes one "
                  "thing and lives by the things other men make. But he can buy theirs only "
                  "with his own, and his own is not worth anything to anyone until it is "
                  "made and sold. Smith puts it as a problem of waiting: &ldquo;A stock of "
                  "goods of different kinds, therefore, must be stored up somewhere, "
                  "sufficient to maintain him, and to supply him with the materials and "
                  "tools of his work, till such time at least as both these events can be "
                  "brought about.&rdquo; The two events are the finishing of the work and "
                  "its sale."),
            ("p", "He gives the case a trade. &ldquo;A weaver cannot apply himself entirely "
                  "to his peculiar business, unless there is before-hand stored up "
                  "somewhere, either in his own possession, or in that of some other "
                  "person, a stock sufficient to maintain him, and to supply him with the "
                  "materials and tools of his work, till he has not only completed, but "
                  "sold his web.&rdquo; Three things are in that stock, and the lab sorts "
                  "them as Chapter 1 will. The yarn is circulating, because it goes from "
                  "him in the web and comes back in its price. The loom stays with him "
                  "and earns by staying, so it is fixed. The food that keeps him until "
                  "the web is sold earns him nothing: it is what a man reserves, in "
                  "Chapter 1's words, for &ldquo;his immediate consumption&rdquo;, and "
                  "his clothes and household goods sit with it in a third portion. (Had "
                  "a master advanced the same food to him as wages, it would be "
                  "circulating capital to the master, as a farmer's servants' wages are "
                  "in Chapter 1: the sorting is always from the owner's side.) The next "
                  "lesson gives the three portions their names and their reasons; here "
                  "you are only counting them. In the weaver preset, written for this "
                  "lesson, the weaver holds a loom and tools worth £20, yarn worth £30, "
                  "food for the weeks until the web is sold worth £40, and clothes and "
                  "furniture worth £10. That is £100 in all, of which £50, the loom and "
                  "the yarn, is the capital he works with, and £50 is what he lives on "
                  "while he waits."),
            ("p", "Smith's conclusion is about order: &ldquo;This accumulation must "
                  "evidently be previous to his applying his industry for so long a time "
                  "to such a peculiar business.&rdquo; He does not say that the stock must "
                  "be the weaver's own. It may be &ldquo;in that of some other "
                  "person&rdquo;, a master who advances yarn and keep, or a lender. What "
                  "he says is that someone must hold it first."),
            ("p", "Then the proportion. &ldquo;As the accumulation of stock must, in the "
                  "nature of things, be previous to the division of labour, so labour can "
                  "be more and more subdivided in proportion only as stock is previously "
                  "more and more accumulated.&rdquo; The reason is in the pins and the "
                  "pin-makers of Book I. A divided trade works up far more material with "
                  "the same hands, and invents machines for each simple operation, so the "
                  "same workmen need an &ldquo;equal stock of provisions&rdquo; but, in "
                  "Smith's words, &ldquo;a greater stock of materials and tools than what "
                  "would have been necessary in a ruder state of things&rdquo;. Take the "
                  "same weaver's workshop after the work is divided and the same number of "
                  "people are still to be fed. The divided preset keeps the food at £40 "
                  "and the clothes at £10, and triples the tools to £60 and the yarn to "
                  "£90. The stock is now £200, and the part of it that is capital has "
                  "gone from a half to three quarters. The long-wait preset changes "
                  "something else: the first weaver waits twice as long for his sale, "
                  "so his food doubles to £80, his stock is £140, and the capital he "
                  "works with is still £50, now only about 36% of it. A longer wait "
                  "asks for more stock without adding any capital."),
            ("p", "Then the motive, which turns the argument round. &ldquo;The person who "
                  "employs his stock in maintaining labour, necessarily wishes to employ it "
                  "in such a manner as to produce as great a quantity of work as "
                  "possible.&rdquo; So he divides the work and buys the best machines "
                  "he can afford, and his means of doing both are &ldquo;generally in "
                  "proportion to the extent of his stock, or to the number of people whom "
                  "it can employ&rdquo;. Stock makes division possible, and having stock "
                  "to employ makes division worth trying. Smith's summary is that the "
                  "quantity of industry increases with the stock, and that the same "
                  "industry then produces &ldquo;a much greater quantity of work&rdquo;."),
            ("def", ("Stock",
                     "Smith's word for goods laid up beforehand: what a person or a "
                     "society holds to eat, wear and live in, to work with, and to work "
                     "up. It is goods, not money, and Book II is about how it divides, "
                     "how it grows and how it is put to work.")),
            ("p", "The Introduction ends on a plan, and the plan is this course and the "
                  "next. The first chapter shows the parts &ldquo;into which the stock, "
                  "either of an individual, or of a great society, naturally divides "
                  "itself&rdquo;. The second explains money as one branch of that stock. "
                  "The third and fourth ask what happens when a capital is employed by its "
                  "owner and when it is lent. The fifth asks what the different employments "
                  "do to the industry of the country."),
            ("p", "Two things need saying about the argument. First, it is a claim about "
                  "what a divided trade requires, not about history. It says someone must "
                  "hold the stock before a specialist can work; it does not say where the "
                  "stock first came from. Marx took what he called Smith's <em>previous "
                  "accumulation</em> as the name of a legend about origins, and "
                  "Capital's lesson <em>The Secret of Primitive Accumulation</em> "
                  "reads what he made of it, which this lesson does not repeat. Second, "
                  "historians of trade point out that many specialists did their work on "
                  "credit, or on materials a merchant advanced, without owning the stock "
                  "themselves. Smith allows for that when he says the stock may be in "
                  "&ldquo;that of some other person&rdquo;; the question the critics ask is "
                  "how much of the economy worked that way."),
            ("p", "The next lesson, <em>Fixed and Circulating Capital</em>, opens "
                  "Chapter 1 and gives the three portions of the weaver's stock the names "
                  "they keep for the rest of the book."),
        ],
        "lab": ("wonkit", {
            "mode": "stock",
            "view": "division",
            "money_unit": "£",
            "preset": "weaver",
            "presets": [
                {"id": "weaver", "label": "A weaver's stock, written for this lesson",
                 "parts": [{"part": "loom-and-tools", "amount": 20, "kind": "fixed"},
                           {"part": "yarn", "amount": 30, "kind": "circulating"},
                           {"part": "food-until-the-web-is-sold", "amount": 40, "kind": "consumption"},
                           {"part": "clothes-and-furniture", "amount": 10, "kind": "consumption"}],
                 "expect": {"wstWhole": "£100", "wstConsumption": "£50 (50%)", "wstFixed": "£20 (20%)", "wstCirculating": "£30 (30%)", "wstCapital": "£50 of £100 (50%)"}},
                {"id": "divided", "label": "The same workmen after more division, written for this lesson",
                 "parts": [{"part": "looms-and-tools", "amount": 60, "kind": "fixed"},
                           {"part": "yarn", "amount": 90, "kind": "circulating"},
                           {"part": "food-until-the-web-is-sold", "amount": 40, "kind": "consumption"},
                           {"part": "clothes-and-furniture", "amount": 10, "kind": "consumption"}],
                 "expect": {"wstWhole": "£200", "wstConsumption": "£50 (25%)", "wstFixed": "£60 (30%)", "wstCirculating": "£90 (45%)", "wstCapital": "£150 of £200 (75%)"}},
                {"id": "long-wait", "label": "The first weaver, waiting twice as long for his sale, written for this lesson",
                 "parts": [{"part": "loom-and-tools", "amount": 20, "kind": "fixed"},
                           {"part": "yarn", "amount": 30, "kind": "circulating"},
                           {"part": "food-until-the-web-is-sold", "amount": 80, "kind": "consumption"},
                           {"part": "clothes-and-furniture", "amount": 10, "kind": "consumption"}],
                 "expect": {"wstWhole": "£140", "wstConsumption": "£90 (≈ 64.29%)", "wstFixed": "£20 (≈ 14.29%)", "wstCirculating": "£30 (≈ 21.43%)", "wstCapital": "£50 of £140 (≈ 35.71%)"}},
            ],
            "panel_title": "A weaver's stock before the web is sold",
            "panel_intro": (
                "Each holding is a name, a sum in pounds and one of three kinds. The lab "
                "adds each kind and gives its share of the whole stock. Compare the first "
                "preset with the second to see what division adds, and with the third to "
                "see what a longer wait for a sale adds."
            ),
        }),
        "steps_title": "Reading a stock off a list",
        "steps_intro": "Four steps, the same for a weaver, a farmer or a whole country.",
        "steps": [
            ("List what is held before the first sale",
             "Write down what the specialist must have in hand: what keeps him until he "
             "is paid, what he works up, what he works with, and what he owns for his "
             "own use. Anything he will receive later is not yet stock."),
            ("Put a sum against each and name its kind",
             "Value each holding in the same money. Call it fixed if it stays with him "
             "and earns by being used, circulating if it earns by going from him, and "
             "consumption if it is kept for his own use and earns nothing."),
            ("Add by kind and find the shares",
             "Total each kind, then divide by the whole stock. Capital is fixed plus "
             "circulating, and its share is what is left after the stock for his own "
             "use."),
            ("Change one thing and compare",
             "Lengthen the wait, or divide the work further, and say which part moved. "
             "Smith's claim is that division adds to materials and tools while the "
             "provisions for the same workmen stay where they were."),
        ],
        "worked": {
            "title": "The weaver, before and after division",
            "intro": [
                "Take the first two presets. The weaver holds a loom and tools worth £20, "
                "yarn worth £30, food worth £40 and clothes and furniture worth £10. After "
                "the work is divided he holds £60 of tools and £90 of yarn, with the "
                "same food and clothes.",
            ],
            "lines": [
                "before:  20 + 30 + 40 + 10 = 100",
                "capital before:  20 + 30 = 50, and 50 / 100 = 1/2",
                "after:  60 + 90 + 40 + 10 = 200",
                "capital after:  60 + 90 = 150, and 150 / 200 = 3/4",
                "food and clothes:  40 and 10, unchanged",
            ],
            "after": [
                "The stock doubled and the food did not move: the whole increase is in "
                "tools and materials, which is Smith's &ldquo;equal stock of "
                "provisions&rdquo; and &ldquo;a greater stock of materials and "
                "tools&rdquo;. In the third preset only the wait has changed: the "
                "food rises to £80 while the tools and yarn stay put, and the capital "
                "share falls to 50/140, about 36%.",
            ],
        },
        "quiz_title": "What a weaver must have first",
        "quiz": [
            {"q": "Why, on Smith's account, must a stock be stored up before the labour "
                  "of a weaver can be divided from that of other trades?",
             "a": ["Because weaving cannot begin until a law gives him the right to work",
                   "Because a weaver is paid in advance by the government",
                   "Because he buys what he needs with the price of his own work, and that "
                   "price comes only once the work is finished and sold",
                   "Because gold and silver must be in circulation before any trade can begin"],
             "c": 2,
             "why": "Smith says the purchase &ldquo;cannot be made till such time as "
                    "the produce of his own labour has not only been completed, but "
                    "sold&rdquo;. Until "
                    "then a stock must maintain him and supply the materials and tools. "
                    "Smith names no law, government pay or money stock in the argument."},
            {"q": "When the same workmen divide their work further, which stock does Smith "
                  "say must grow?",
             "a": ["The provisions that keep each workman",
                   "The materials and tools",
                   "Both, in proportion to the number of operations",
                   "Neither, because the workmen's skill makes up the difference"],
             "c": 1,
             "why": "He says an &ldquo;equal stock of provisions&rdquo; and &ldquo;a "
                    "greater stock of materials and tools&rdquo; must be accumulated, for "
                    "the same number of workmen. The number of workmen generally grows "
                    "too, but that is a separate effect."},
            {"q": "A weaver holds a loom worth £15, yarn worth £30, food for his own "
                  "table worth £30 and furniture worth £25. What share of the whole is "
                  "capital, on the lab's sorting?",
             "a": ["Three fifths",
                   "Nine twentieths",
                   "One quarter",
                   "Three quarters"],
             "c": 1,
             "why": "The whole is `15 + 30 + 30 + 25 = 100`. His food and furniture are "
                    "kept for his own use and are not capital. The loom and yarn are "
                    "`15 + 30 = 45`, so capital is `45/100`, nine twentieths. Three "
                    "quarters counts his food as capital, three fifths is the yarn and "
                    "food together, and one quarter is the furniture alone."},
            {"q": "What does Smith say about the connection running the other way, from "
                  "stock to the division of labour?",
             "a": ["Whoever lays out a stock to employ labour wants as much work from it "
                   "as possible, so he divides the work and buys machines, as far as his "
                   "stock allows",
                   "A large stock makes the owner idle, so he divides the work to rest",
                   "Stock has no connection with the division of labour once it is begun",
                   "Only a government can accumulate enough stock to divide labour"],
             "c": 0,
             "why": "&ldquo;The person who employs his stock in maintaining labour, "
                    "necessarily wishes to employ it in such a manner as to produce as "
                    "great a quantity of work as possible.&rdquo; His abilities to do so "
                    "are &ldquo;generally in proportion to the extent of his stock&rdquo;."},
        ],
        "mistakes": [
            ("Taking the weaver's stock to be money",
             "Smith's stock is &ldquo;A stock of goods of different kinds&rdquo;: food, "
             "yarn, a loom. Money is one of the goods that may be held, and Chapter 2 "
             "treats it as one branch of the stock, but the weaver's problem is waiting "
             "for his pay, not shortage of coin. In the lab every part is a good with a "
             "money value put against it."),
            ("Reading the argument as saying the weaver must own it all",
             "The stock must be stored &ldquo;either in his own possession, or in that of "
             "some other person&rdquo;. A master who advances yarn and keep holds the "
             "weaver's stock for him. What Smith insists on is that it exists beforehand, "
             "not that it belongs to the specialist."),
            ("Counting everything the weaver owns as capital",
             "Only the part he expects to give him a revenue is capital. His food until "
             "the sale, his clothes and his furniture are kept for his own use and are "
             "part of the whole stock without being capital. In the first preset £50 of "
             "the £100 is of that kind, which is why the capital share is a half and not "
             "the whole."),
        ],
        "standard": (
            "Finish when you can sort a stock and say what division adds to it.",
            "Given a list of holdings with sums, sort each as consumption, fixed or "
            "circulating, compute the shares and the capital share, and say which part "
            "Smith expects to grow when the same workmen divide their work further."
        ),
        "note": (
            "The lab sorts a list that the lesson writes. It cannot say how much stock a "
            "given division needs: Smith asserts the proportion without measuring it. It "
            "cannot say which came first in history, either, and every figure in the "
            "three presets is written for this lesson; Smith gives none."
        ),
    },
    # ---------------------------------------------------------------- 02
    # PSU text l. 8909-9162 (Book II, Chapter 1). l. 8915-8926 (capital and
    # immediate consumption); l. 8927-8940 (circulating and fixed); l. 8963-8984
    # (the farmer; seed); l. 8985-9022 (consumption portion; houses); l. 9023-9051
    # (four fixed); l. 9052-9078 (four circulating); l. 9086-9096 (one depends on
    # the other); l. 9134-9143 ("perfectly crazy"); l. 9144-9162 (hoarding).
    {
        "slug": "fixed-and-circulating-capital",
        "title": "Fixed and Circulating Capital",
        "module": "Book II, Chapter 1 · Of the Division of Stock",
        "one_line": "A stock divides into what is kept for use, what earns by staying with its owner, and what earns by going from him and coming back.",
        "summary": (
            "Chapter 1 sorts every stock, a man's or a nation's, by one test: does it "
            "yield a revenue, and if so does it do it by staying or by going? Sort a "
            "parish, a farm and an iron-work into Smith's three portions, compute the "
            "shares, and see why a farmer's seed is fixed and his cattle's keep is "
            "circulating."
        ),
        "key": [
            "kept for use: no revenue",
            "fixed: revenue by staying",
            "circulating: revenue by going and returning",
            "capital = fixed + circulating",
            "fixed needs circulating to yield",
        ],
        "key_label": "The three portions in five lines",
        "concepts_intro": (
            "The chapter is a classification with a reason behind each class. The reason "
            "is the whole of it."
        ),
        "concepts": [
            ("Stock reserved for immediate consumption",
             "The part of a stock kept to be used up, not to earn: food in the larder, "
             "clothes, furniture and, to its owner, his dwelling-house. It yields no "
             "revenue; it is spent, however slowly."),
            ("Fixed capital",
             "What yields a revenue without changing masters: machines and tools, "
             "profitable buildings, improvements of land, and the acquired abilities of "
             "the people. Its owner profits by keeping it."),
            ("Circulating capital",
             "What yields a revenue only by circulating, by going from its owner and "
             "coming back with a profit: money, provisions, materials and finished work in "
             "dealers' hands. Its owner profits by parting with it."),
        ],
        "read_title": "The test, then the farmer's cattle, then the society",
        "read_intro": (
            "Smith divides first a single man's stock and then a country's. The test is "
            "stated once and applied to the farmer, whose case is the hardest."
        ),
        "body": [
            ("p", "<strong>Book II, Chapter 1.</strong> &ldquo;But when he possesses stock "
                  "sufficient to maintain him for months or years, he naturally endeavours "
                  "to derive a revenue from the greater part of it, reserving only so much "
                  "for his immediate consumption as may maintain him till this revenue "
                  "begins to come in. His whole stock, therefore, is distinguished into two "
                  "parts. That part which he expects is to afford him this revenue is "
                  "called his capital.&rdquo;"),
            ("p", "That is the first cut, and everything later in the chapter is the second "
                  "cut made inside capital. A person with a week's food has no capital: "
                  "he eats it. A person with a year's food can set some of it to work, "
                  "and the part set to work is what Smith calls capital. The remainder "
                  "supplies immediate consumption, whether it is what he first reserved, "
                  "the revenue as it comes in, or &ldquo;such things as had been "
                  "purchased by either of these in former years, and which are not yet "
                  "entirely consumed&rdquo;."),
            ("p", "Now the test that splits capital. A capital may be employed &ldquo;in "
                  "raising, manufacturing, or purchasing goods, and selling them again "
                  "with a profit&rdquo;. The merchant's goods earn nothing while they sit. "
                  "&ldquo;His capital is continually going from him in one shape, and "
                  "returning to him in another; and it is only by means of such "
                  "circulation, or successive changes, that it can yield him any "
                  "profit.&rdquo; That is circulating capital. The other way is to lay it "
                  "out on &ldquo;such like things as yield a revenue or profit without "
                  "changing masters, or circulating any further&rdquo;, which Smith calls "
                  "fixed capital. A merchant's capital is almost all circulating. A "
                  "tailor's fixed capital is a parcel of needles. An iron-work's is a "
                  "furnace, a forge and a slit-mill, which &ldquo;cannot be erected "
                  "without a very great expense&rdquo;."),
            ("p", "The farmer is where the test earns its keep, and Smith is careful with "
                  "him. &ldquo;He makes a profit of the one by keeping it in his own "
                  "possession, and of the other by parting with it.&rdquo; His labouring "
                  "cattle are fixed capital, like his plough, but their keep is "
                  "circulating, like the wages of his servants. Cattle bought and fattened "
                  "to sell are circulating throughout. A breeding flock that he keeps for "
                  "wool and increase is fixed, and its keep circulating. Then the "
                  "surprise: &ldquo;The whole value of the seed, too, is properly a "
                  "fixed capital. Though it goes backwards and forwards between the "
                  "ground and the granary, it never changes masters, and therefore does "
                  "not properly circulate.&rdquo; The test asks about owners and sales, "
                  "not about whether the thing moves. The farmer preset sorts a farm "
                  "this way, with kinds from Smith and sums written for the lesson, and "
                  "the farmer's capital comes to £340 of a £400 stock."),
            ("p", "Then the society. &ldquo;The general stock of any country or society "
                  "is the same with that of all its inhabitants or members&rdquo;, so it "
                  "divides into the same three portions. The first, for immediate "
                  "consumption, includes the whole stock of dwelling-houses. A house lived "
                  "in by its owner is no capital to him: &ldquo;A dwelling-house, as such, "
                  "contributes nothing to the revenue of its inhabitant&rdquo;. Let it to "
                  "a tenant and it yields its owner a rent, but the tenant pays that from "
                  "some other revenue, so it yields none to the public. Smith lists "
                  "masquerade dresses let for the night and funeral furniture let by the "
                  "day to show the same point at the smallest scale."),
            ("p", "The second portion, fixed capital, has four parts. Machines and "
                  "instruments of trade; the profitable buildings, shops, warehouses and "
                  "farmhouses, which are &ldquo;very different from mere "
                  "dwelling-houses&rdquo;; the improvements of land, such as clearing, "
                  "draining and manuring; and a fourth that is easy to read past: "
                  "&ldquo;the acquired and useful abilities of all the inhabitants and "
                  "members of the society&rdquo;. The maintenance of a person while he "
                  "learns, Smith says, &ldquo;always costs a real expense, which is a "
                  "capital fixed and realized, as it were, in his person&rdquo;. Later "
                  "writers gave this idea its own name, human capital, and it is in the "
                  "book already."),
            ("p", "The third portion, circulating capital, also has four: the money by "
                  "which the others are circulated; the provisions in the hands of "
                  "butchers, farmers and brewers; the materials not yet made up; and the "
                  "finished work still in the shops of the smith and the cabinet-maker. "
                  "The parish preset puts all ten of these holdings into one parish, with "
                  "sums written for this lesson: £400 for immediate consumption, £600 "
                  "fixed and £250 circulating, which makes the capital £850 of a £1,250 "
                  "stock."),
            ("p", "The two capitals lean on one another. &ldquo;No fixed capital can "
                  "yield any revenue but by means of a circulating capital&rdquo;: the "
                  "best machine produces nothing without materials to work on and "
                  "maintenance for the workmen, and land, however improved, yields no "
                  "revenue without a circulating capital to keep its labourers. And "
                  "both exist for the first portion: to maintain and augment the stock "
                  "for immediate consumption is, Smith says, &ldquo;the sole end and "
                  "purpose both of the fixed and circulating capitals&rdquo;, and "
                  "&ldquo;It is this stock which feeds, clothes, and lodges the "
                  "people.&rdquo; Hold the three presets next to each other and you see "
                  "the proportions vary by trade. The iron-work preset, with "
                  "figures written for the lesson, is £600 fixed of £1,000, and the "
                  "farmer's is under half."),
            ("p", "The chapter ends with a remark whose first half is plain Smith. "
                  "&ldquo;A man must be perfectly crazy, who, where there is a tolerable "
                  "security, does not employ all the stock which he commands&rdquo; in one "
                  "of the three ways. The second half is a warning about where security is "
                  "missing, where men &ldquo;bury or conceal a great part of their "
                  "stock&rdquo; to have it ready to carry off. The stock exists in either "
                  "case; what differs is whether it works."),
            ("p", "Two later arguments about the test are worth knowing. Smith's rule sorts "
                  "by what the owner does with a thing, so a farmer's seed is fixed, and "
                  "Ricardo sorted by how long a capital lasts, which puts seed with the "
                  "circulating capital that is used up in a year; Capital's lessons "
                  "<em>Ricardo on Fixed and Circulating Capital</em> and <em>The "
                  "Physiocrats and Adam Smith on Fixed Capital</em> take up the "
                  "objections, which this lesson does not repeat. The point for now is that "
                  "the classes are drawn from the owner's side. A capital that is fixed "
                  "to one person may be circulating for another: the loom is fixed to the "
                  "weaver and circulating to the maker who sells it."),
            ("p", "Chapter 2 asks what part of all this is money. It is the first of the "
                  "circulating capitals, and it turns out to be the odd one out, which is "
                  "the subject of the next lesson, <em>Gross and Net Revenue</em>."),
        ],
        "lab": ("wonkit", {
            "mode": "stock",
            "view": "division",
            "money_unit": "£",
            "preset": "parish",
            "presets": [
                {"id": "parish", "label": "A parish's stock, written for this lesson",
                 "parts": [{"part": "dwelling-houses", "amount": 300, "kind": "consumption"},
                           {"part": "clothes-and-furniture", "amount": 100, "kind": "consumption"},
                           {"part": "machines-and-tools", "amount": 150, "kind": "fixed"},
                           {"part": "farmhouses-shops-and-warehouses", "amount": 100, "kind": "fixed"},
                           {"part": "improvements-of-land", "amount": 250, "kind": "fixed"},
                           {"part": "acquired-abilities", "amount": 100, "kind": "fixed"},
                           {"part": "money", "amount": 50, "kind": "circulating"},
                           {"part": "provisions-in-dealers-hands", "amount": 80, "kind": "circulating"},
                           {"part": "materials", "amount": 60, "kind": "circulating"},
                           {"part": "finished-work-in-the-shops", "amount": 60, "kind": "circulating"}],
                 "expect": {"wstWhole": "£1,250", "wstConsumption": "£400 (32%)", "wstFixed": "£600 (48%)", "wstCirculating": "£250 (20%)", "wstCapital": "£850 of £1,250 (68%)"}},
                {"id": "farmer", "label": "A farmer's stock sorted as Smith sorts it (his kinds, sums written for this lesson)",
                 "parts": [{"part": "plough-and-farm-tools", "amount": 40, "kind": "fixed"},
                           {"part": "price-of-the-labouring-cattle", "amount": 60, "kind": "fixed"},
                           {"part": "keep-of-the-labouring-cattle", "amount": 30, "kind": "circulating"},
                           {"part": "cattle-bought-to-fatten-for-sale", "amount": 60, "kind": "circulating"},
                           {"part": "breeding-flock", "amount": 60, "kind": "fixed"},
                           {"part": "keep-of-the-flock", "amount": 30, "kind": "circulating"},
                           {"part": "seed", "amount": 20, "kind": "fixed"},
                           {"part": "wages-of-labouring-servants", "amount": 40, "kind": "circulating"},
                           {"part": "household-clothes-and-furniture", "amount": 60, "kind": "consumption"}],
                 "expect": {"wstWhole": "£400", "wstConsumption": "£60 (15%)", "wstFixed": "£180 (45%)", "wstCirculating": "£160 (40%)", "wstCapital": "£340 of £400 (85%)"}},
                {"id": "iron-work", "label": "An iron-work, written for this lesson",
                 "parts": [{"part": "furnace-forge-and-slit-mill", "amount": 600, "kind": "fixed"},
                           {"part": "ore-coal-and-other-materials", "amount": 200, "kind": "circulating"},
                           {"part": "wages-of-the-workmen", "amount": 150, "kind": "circulating"},
                           {"part": "the-ironmasters-household-goods", "amount": 50, "kind": "consumption"}],
                 "expect": {"wstWhole": "£1,000", "wstConsumption": "£50 (5%)", "wstFixed": "£600 (60%)", "wstCirculating": "£350 (35%)", "wstCapital": "£950 of £1,000 (95%)"}},
            ],
            "panel_title": "Three portions of a stock",
            "panel_intro": (
                "Each holding is a name, a sum in pounds and a kind. The lab totals each "
                "kind, gives its share and the capital share, and names the largest part "
                "of each kind. The farm's kinds are Smith's; every sum is written for this "
                "lesson."
            ),
        }),
        "steps_title": "Sorting a holding by Smith's test",
        "steps_intro": "Four steps, and the second is the only one that needs thought.",
        "steps": [
            ("Ask whether it is meant to earn",
             "If it is kept for its owner's own use and spent in using, it belongs to "
             "the stock reserved for immediate consumption, whatever it is made of."),
            ("Ask whether it earns by staying or by going",
             "If the owner profits by keeping it, as with a loom, a drained field or a "
             "breeding flock, it is fixed. If he profits by selling it on and getting "
             "back more, as with a merchant's goods or a servant's wages, it is "
             "circulating."),
            ("Add the sums by kind",
             "Total consumption, fixed and circulating separately. Capital is the sum of "
             "the last two, and the whole stock is all three."),
            ("Check the dependence",
             "A fixed capital yields only with a circulating one beside it. If a list "
             "has machines and no materials or maintenance, something was left out."),
        ],
        "worked": {
            "title": "A farmer's stock, sorted",
            "intro": [
                "Take the second preset. The kinds are Smith's: plough, cattle and flock "
                "fixed, their keep and the servants' wages circulating, cattle bought to "
                "fatten circulating, seed fixed. The sums are written for the lesson.",
            ],
            "lines": [
                "fixed:  40 + 60 + 60 + 20 = 180",
                "circulating:  30 + 60 + 30 + 40 = 160",
                "consumption:  60",
                "whole stock:  180 + 160 + 60 = 400",
                "capital:  180 + 160 = 340, and 340 / 400 = 17/20",
            ],
            "after": [
                "The farmer's fixed capital is under half the whole, and his seed, a small "
                "part, is on the fixed side, which Smith insists on although the seed "
                "goes back and forth between ground and granary. In the iron-work the "
                "fixed share is three fifths, which is the difference Smith meant when he "
                "set a tailor's needles beside a furnace.",
            ],
        },
        "quiz_title": "Fixed, circulating or kept for use",
        "quiz": [
            {"q": "Which of a farmer's holdings does Smith call a fixed capital?",
             "a": ["The keep of his labouring cattle",
                   "The wages of his labouring servants",
                   "The seed he sows",
                   "Cattle he has bought to fatten for sale"],
             "c": 2,
             "why": "&ldquo;The whole value of the seed, too, is properly a fixed "
                    "capital&rdquo;, because it &ldquo;never changes masters&rdquo;. The "
                    "keep of the cattle and the servants' wages are circulating capital; "
                    "cattle bought for sale are circulating throughout, because the farmer "
                    "makes his profit by parting with them."},
            {"q": "A man lives in a house he owns. In Smith's sorting, what is it to him?",
             "a": ["Fixed capital, because it stays with him",
                   "Part of his stock reserved for immediate consumption",
                   "Circulating capital, because it can be sold",
                   "Capital, but only after a tenant moves in"],
             "c": 1,
             "why": "&ldquo;A dwelling-house, as such, contributes nothing to the revenue "
                    "of its inhabitant&rdquo;. It stays with him, but it earns him nothing, "
                    "so it is kept for use. Let to a tenant it would yield its owner a "
                    "rent, though not the public, since the tenant pays it from some other "
                    "revenue."},
            {"q": "A stock is made of £200 kept for use, £300 in fixed capital and £100 in "
                  "circulating capital. What fraction of the whole stock is capital?",
             "a": ["One half",
                   "One third",
                   "Five sixths",
                   "Two thirds"],
             "c": 3,
             "why": "The whole is `200 + 300 + 100 = 600`. Capital is the fixed and "
                    "circulating parts, `300 + 100 = 400`, and `400/600` is two thirds. "
                    "One half is the fixed share alone."},
            {"q": "What does Smith say a fixed capital needs before it will yield any "
                  "revenue?",
             "a": ["A circulating capital that supplies materials and the maintenance of "
                   "the workmen",
                   "A dwelling-house for the workmen to live in",
                   "A loan of money at interest",
                   "A division of labour among the owners"],
             "c": 0,
             "why": "&ldquo;No fixed capital can yield any revenue but by means of a "
                    "circulating capital.&rdquo; The best machines &ldquo;will produce "
                    "nothing, without the circulating capital, which affords the "
                    "materials they are employed upon, and the maintenance of the "
                    "workmen who employ them&rdquo;."},
        ],
        "mistakes": [
            ("Sorting by what a thing is made of, not by what it does for its owner",
             "Smith's test is the owner's: does he profit by keeping it or by parting with "
             "it? A farmer's seed moves between ground and granary and is fixed. His "
             "cattle are fixed if kept for labour or increase and circulating if bought "
             "to sell. In the farm preset the same herd appears on both sides for this "
             "reason: the price of the labouring cattle is fixed, and their keep "
             "circulating."),
            ("Counting an owner's dwelling-house as capital",
             "It is the largest single item in the parish preset and it is not capital. "
             "Smith puts it with clothes and furniture, only longer-lived: a stock of "
             "houses &ldquo;may last many centuries&rdquo; but is &ldquo;still as really "
             "a stock reserved for immediate consumption&rdquo;. A rented house is capital "
             "to its landlord only."),
            ("Thinking fixed capital means machinery",
             "Smith names four kinds: machines, profitable buildings, improvements of land, "
             "and acquired abilities. In the parish preset £250 of improved land and £100 "
             "of acquired abilities are fixed capital, and neither is a machine. An "
             "apprentice's years of keep are, in Smith's words, a capital &ldquo;fixed "
             "and realized, as it were, in his person&rdquo;."),
        ],
        "standard": (
            "Finish when you can sort a list of holdings by Smith's test.",
            "Given a list of holdings, classify each as kept for immediate consumption, "
            "fixed capital or circulating capital by whether it yields a revenue and, if "
            "so, by staying or by going, and compute the share of each kind and the "
            "capital share."
        ),
        "note": (
            "The classification depends on the owner's point of view, and that is a "
            "strength and a limit of it. The lab applies the test to kinds that the "
            "lesson assigns, so it cannot show whether Smith's classes cut an economy at "
            "its joints, which later writers disputed. The sums in all three presets are "
            "written for this lesson; Smith lists the kinds and gives no amounts."
        ),
    },
    # ---------------------------------------------------------------- 03
    # PSU text l. 9163-9500 (Book II, Chapter 2, first part). l. 9167-9193 (the
    # three parts; gross and neat rent); l. 9201-9204 (gross and neat revenue);
    # l. 9205-9267 (fixed capital's upkeep; circulating capital); l. 9278-9280
    # (money the only part); l. 9303-9309 (the great wheel); l. 9310-9381
    # (the guinea); l. 9382-9398 (savings); l. 9399-9405 (paper replaces gold).
    {
        "slug": "gross-and-net-revenue",
        "title": "Gross and Net Revenue",
        "module": "Book II, Chapter 2, first part · Of Money, considered as a particular Branch of the general Stock of the Society",
        "one_line": "A nation's real wealth is its net revenue, what is left of the gross after the upkeep of its machines and its money, and money, though a valuable part of its capital, is no part of its revenue.",
        "summary": (
            "Smith carries the gross and the neat rent of a private estate up to a whole "
            "country, deducts the upkeep of fixed capital and of money, and says that the "
            "money that circulates the goods is not itself any part of the revenue. "
            "Compute a country's net revenue from a gross and two upkeeps, then watch "
            "what a saving on either one adds."
        ),
        "key": [
            "gross = the whole annual produce",
            "net = gross − fixed upkeep − money upkeep",
            "the other circulating capital stays in net",
            "money is the wheel, not the goods",
            "savings in upkeep add to net revenue",
        ],
        "key_label": "Gross and net in five lines",
        "concepts_intro": (
            "Chapter 2 begins from Book I's three parts of price and builds a measure "
            "of national wealth in three steps."
        ),
        "concepts": [
            ("Gross and net revenue",
             "The gross revenue of a country is the whole annual produce of its land and "
             "labour. The net revenue is what is left after maintaining its fixed and "
             "circulating capitals: what the people can spend on living without "
             "encroaching on capital. Real wealth, Smith says, is in proportion to the "
             "net."),
            ("The upkeep that comes off",
             "All of the upkeep of fixed capital comes off. Of the circulating capital, "
             "provisions, materials and finished work are withdrawn into consumption and "
             "stay in the net revenue. Money alone is a circulating capital whose upkeep "
             "is a deduction."),
            ("Money is not revenue",
             "A guinea paid weekly is worth what it buys. The same coin pays one man today "
             "and another tomorrow, so the coins in a country are worth far less than the "
             "payments made with them, and the revenue is the goods, not the coins."),
        ],
        "read_title": "From an estate's rent to a nation's, then the guinea",
        "read_intro": (
            "The chapter opens by borrowing Book I's result and putting it to work. "
            "Smith then makes two arguments, one about machines and one about money, "
            "and says they are alike."
        ),
        "body": [
            ("p", "<strong>Book II, Chapter 2.</strong> &ldquo;The gross rent of a private "
                  "estate comprehends whatever is paid by the farmer; the neat rent, what "
                  "remains free to the landlord, after deducting the expense of management, "
                  "of repairs, and all other necessary charges&rdquo;. And Smith's point "
                  "about it: &ldquo;His real wealth is in proportion, not to his gross, but "
                  "to his neat rent.&rdquo;"),
            ("p", "The chapter begins by reminding you of Book I, where &ldquo;the price "
                  "of the greater part of commodities resolves itself into three "
                  "parts&rdquo;, wages, profit and rent. What was true of each commodity "
                  "is then said of all of them together: the whole annual produce of a "
                  "country is divided among its people as wages, profits and rents. That "
                  "step, from one commodity to the whole annual produce, is the one Marx "
                  "contests in Capital's lesson <em>Former Discussions: Quesnay and "
                  "Smith</em>, and this lesson does not repeat that argument. Here it "
                  "is only the starting point."),
            ("p", "From there Smith does for a country what he did for an estate. "
                  "&ldquo;The gross revenue of all the inhabitants of a great country "
                  "comprehends the whole annual produce of their land and labour; the neat "
                  "revenue, what remains free to them, after deducting the expense of "
                  "maintaining first, their fixed, and, secondly, their circulating "
                  "capital&rdquo;. The test is whether the people can spend it on living "
                  "&ldquo;without encroaching upon their capital&rdquo;."),
            ("p", "The first deduction is the whole upkeep of fixed capital. Smith's reason "
                  "is not that machines are a waste. &ldquo;The expense which is properly "
                  "laid out upon a fixed capital of any kind, is always repaid with great "
                  "profit.&rdquo; It is that the upkeep needs materials and workmen who "
                  "might otherwise have been making food, clothes and lodging, so it "
                  "counts in the gross and not in the net. It resembles the repairs on "
                  "an estate: &ldquo;The expense of maintaining the fixed capital in a "
                  "great country, may very properly be compared to that of repairs in a "
                  "private estate.&rdquo; Cheaper upkeep that costs no productive power is "
                  "a gain. &ldquo;The undertaker of some great manufactory, who employs a "
                  "thousand a-year in the maintenance of his machinery, if he can reduce "
                  "this expense to five hundred, will naturally employ the other five "
                  "hundred in purchasing an additional quantity of materials, to be wrought "
                  "up by an additional number of workmen.&rdquo; The thousand and the five "
                  "hundred are Smith's; the works' yearly produce of £10,000 in the "
                  "lab's undertaker and cheaper-machinery presets is written for the lesson. The net revenue "
                  "rises from £9,000 to £9,500, and the five hundred is back at work."),
            ("p", "The second deduction is subtler, because a society's circulating "
                  "capital is not like a man's. A man's circulating capital is wholly "
                  "excluded from his net revenue, which consists of his profits. But the "
                  "goods in a merchant's shop, though no part of his own stock for "
                  "consumption, may go into the stock of other people, who, in Smith's "
                  "words, &ldquo;from a revenue derived from other funds, may regularly "
                  "replace their value to him, together with its profits&rdquo;: "
                  "they are withdrawn into other people's consumption and stay in the "
                  "society's net revenue. So, &ldquo;Money, therefore, is the only part "
                  "of the circulating capital of a society, of which the maintenance can "
                  "occasion any diminution in their neat revenue.&rdquo;"),
            ("p", "Smith then draws the likeness between machines and money. Both cost "
                  "something to make and to keep up. A quantity of gold and silver and "
                  "&ldquo;of very curious labour&rdquo; is spent maintaining the "
                  "&ldquo;great but expensive instrument of commerce&rdquo; instead of "
                  "adding to the stock for consumption. Neither is a part of the revenue "
                  "it helps to distribute. &ldquo;The great wheel of circulation is "
                  "altogether different from the goods which are circulated by means of "
                  "it. The revenue of the society consists altogether in those goods, and "
                  "not in the wheel which circulates them.&rdquo; In the lab's country "
                  "preset a country has a gross of £10,000,000, a fixed capital whose "
                  "upkeep is £2,000,000 and a stock of money whose yearly upkeep is "
                  "£500,000, all written for the lesson. The net revenue is £7,500,000, "
                  "three quarters of the gross."),
            ("p", "Smith expects an objection, since incomes are paid in money, and "
                  "answers it by distinguishing two things the word covers. &ldquo;when we "
                  "say that the circulating money of England has been computed at eighteen "
                  "millions, we mean only to express the amount of the metal pieces&rdquo;. "
                  "But when we say a man is worth a hundred pounds a year we mean the goods "
                  "his money buys, so his weekly revenue is &ldquo;to the guinea's worth "
                  "rather than to the guinea&rdquo;. A guinea that could be exchanged for "
                  "nothing would be, like a bill upon a bankrupt, worth no more than "
                  "waste paper. Smith thinks the whole difficulty a verbal one: "
                  "&ldquo;It is the ambiguity of language only which can make this "
                  "proposition appear either doubtful or paradoxical.&rdquo;"),
            ("p", "Then the argument for a society. &ldquo;As the same guinea which pays "
                  "the weekly pension of one man to-day, may pay that of another "
                  "to-morrow, and that of a third the day thereafter, the amount of the "
                  "metal pieces which annually circulate in any country, must always be of "
                  "much less value than the whole money pensions annually paid with "
                  "them.&rdquo; The payments made in a year are a multiple of the coins "
                  "that make them. What is paid is a power of purchasing, and the "
                  "revenue is the goods it buys."),
            ("p", "The third likeness is the one that leads to the next lesson. Any saving in "
                  "the upkeep of the fixed capital that does not reduce the productive "
                  "power of labour raises the net revenue; so does any such saving in "
                  "&ldquo;collecting and supporting that part of the circulating capital "
                  "which consists in money&rdquo;. If upkeep is the whole of the money's "
                  "claim on the net revenue, then replacing gold by something cheaper "
                  "that circulates as well would be an improvement of exactly the same "
                  "kind. In the paper preset a country does it: the upkeep of its money "
                  "falls from £500,000 to £100,000, a saving of £400,000, and the net "
                  "revenue rises to £7,900,000. Smith's own name for that something "
                  "cheaper is paper money, and it is the subject of the next lesson."),
            ("p", "Two cautions on the argument. The yearly upkeep of a country's money is "
                  "not a number Smith gives or one anyone could read off the national "
                  "accounts, and the lab's £500,000 is a placeholder written for the "
                  "lesson. And the claim that money is no part of revenue is a claim about "
                  "what to count in a country's wealth. It is consistent with money "
                  "being very useful, as Smith says, in the way a wheel is. The next "
                  "lesson is <em>Paper Money and the Scottish Banks</em>."),
        ],
        "lab": ("wonkit", {
            "mode": "stock",
            "view": "revenue",
            "money_unit": "£",
            "preset": "undertaker",
            "presets": [
                {"id": "undertaker", "label": "Smith's undertaker: a thousand a year on machinery (the thousand is Smith's, the works' produce is written for this lesson)",
                 "gross": 10000, "fixed": 1000, "money": 0, "expect": {"wstKeep": "£1,000 (10% of the gross)", "wstNet": "£9,000", "wstNetShare": "90%", "wstNew": "no saving given", "wstGain": "no saving given"}},
                {"id": "cheaper-machinery", "label": "The same works with the upkeep cut to five hundred (Smith's figure)",
                 "gross": 10000, "fixed": 500, "money": 0, "expect": {"wstKeep": "£500 (5% of the gross)", "wstNet": "£9,500", "wstNetShare": "95%", "wstNew": "no saving given", "wstGain": "no saving given"}},
                {"id": "country", "label": "A country's gross and two upkeeps, written for this lesson",
                 "gross": 10000000, "fixed": 2000000, "money": 500000, "expect": {"wstKeep": "£2,500,000 (25% of the gross)", "wstNet": "£7,500,000", "wstNetShare": "75%", "wstNew": "no saving given", "wstGain": "no saving given"}},
                {"id": "paper", "label": "The same country with a saving of £400,000 on the money, written for this lesson",
                 "gross": 10000000, "fixed": 2000000, "money": 500000, "saving": 400000, "expect": {"wstKeep": "£2,500,000 (25% of the gross)", "wstNet": "£7,500,000", "wstNetShare": "75%", "wstNew": "£7,900,000 (79% of the gross)", "wstGain": "+£400,000 (≈ +5.33% on the net revenue)"}},
            ],
            "panel_title": "What is left of the gross",
            "panel_intro": (
                "Enter a gross revenue, the yearly upkeep of the fixed capital and the "
                "yearly upkeep of the money. The lab subtracts and gives the net revenue "
                "and its share of the gross; with a saving it gives the new net and the "
                "gain. The thousand-and-five-hundred presets are Smith's figures on "
                "written produce; the country's are all written for this lesson."
            ),
        }),
        "steps_title": "From a gross to a net revenue",
        "steps_intro": "Four steps, in Smith's order.",
        "steps": [
            ("Start from the whole annual produce",
             "The gross revenue is everything the land and labour of the country "
             "produce in the year, in the same money as the other figures."),
            ("Take off the upkeep of fixed capital",
             "Subtract everything it costs each year to keep machines, buildings and "
             "improvements as they are. All of it comes off."),
            ("Take off the upkeep of the money, and nothing else of the circulating capital",
             "Subtract what it costs to collect and keep up the stock of money. The "
             "provisions, materials and finished work in dealers' hands are withdrawn "
             "into consumption and stay in the net."),
            ("Price a saving",
             "Reduce either upkeep by the amount saved, keeping productive power as it "
             "was. The gain in net revenue is the saving, and Smith expects it to go "
             "to employing more labour."),
        ],
        "worked": {
            "title": "A country's net revenue, before and after paper",
            "intro": [
                "Take the third and fourth presets. The figures are written for the "
                "lesson. A country's annual produce is £10,000,000; the yearly upkeep "
                "of its fixed capital is £2,000,000 and of its money £500,000. Then paper "
                "replaces gold and the money's upkeep falls by £400,000.",
            ],
            "lines": [
                "net:  10,000,000 − 2,000,000 − 500,000 = 7,500,000",
                "share of gross:  7,500,000 / 10,000,000 = 3/4",
                "money's upkeep after:  500,000 − 400,000 = 100,000",
                "net after:  10,000,000 − 2,000,000 − 100,000 = 7,900,000",
                "gain:  7,900,000 − 7,500,000 = 400,000",
            ],
            "after": [
                "The gross did not move: it is the same land and the same labour. What "
                "changed is how much of it is spent keeping a wheel turning. Smith's "
                "claim is that the whole saving is an addition to the stock that can "
                "go to consumption or to employing more labour, and the lab's "
                "undertaker preset is the same arithmetic on a single works.",
            ],
        },
        "quiz_title": "What comes off a gross revenue",
        "quiz": [
            {"q": "Which part of a society's circulating capital does Smith say reduces its "
                  "net revenue when it is maintained?",
             "a": ["Money, provisions, materials and finished work together",
                   "Provisions and materials, but not money",
                   "Money alone",
                   "None of it: only fixed capital reduces net revenue"],
             "c": 2,
             "why": "&ldquo;Money, therefore, is the only part of the circulating capital "
                    "of a society, of which the maintenance can occasion any diminution "
                    "in their neat revenue.&rdquo; The other three parts are regularly "
                    "withdrawn into the fixed capital or into consumption. The upkeep of "
                    "fixed capital reduces the net as well, so money is not the only "
                    "deduction; the last option is wrong because money reduces the net "
                    "revenue too."},
            {"q": "A country's annual produce is 5,000, the yearly upkeep of its fixed "
                  "capital is 800 and of its money is 200. What is its net revenue on "
                  "Smith's definition?",
             "a": ["4,200",
                   "4,000",
                   "4,800",
                   "5,000"],
             "c": 1,
             "why": "Net revenue is `5,000 − 800 − 200 = 4,000`. Subtracting only the "
                    "fixed capital's upkeep gives 4,200, only the money's gives 4,800, and "
                    "5,000 is the gross."},
            {"q": "Smith says the weekly revenue of a man paid a guinea consists in:",
             "a": ["The guinea itself, because it is gold",
                   "Both the guinea and what it buys, added together",
                   "The interest the guinea would earn if it were lent",
                   "What the guinea will buy"],
             "c": 3,
             "why": "His revenue is &ldquo;not equal both to the guinea and to what can be "
                    "purchased with it, but only to one or other of those two equal "
                    "values, and to the latter more properly than to the former&rdquo;. "
                    "Counting both would count the same value twice."},
            {"q": "An undertaker employs a thousand a year in maintaining his machinery and "
                  "finds he can do it for five hundred. What does Smith say he will "
                  "naturally do with the other five hundred?",
             "a": ["Employ it in buying more materials, to be worked up by more workmen",
                   "Keep it as additional profit and spend it on his own household",
                   "Lend it to government at interest",
                   "Reduce the wages of his workmen to match"],
             "c": 0,
             "why": "&ldquo;will naturally employ the other five hundred in purchasing "
                    "an additional quantity of materials, to be wrought up by an "
                    "additional number of workmen.&rdquo; The saving puts more labour to "
                    "work; Smith says nothing of his pocketing it or cutting wages."},
        ],
        "mistakes": [
            ("Counting money as part of a nation's revenue because incomes are paid in it",
             "Smith's answer is that a sum of money has two meanings, the metal pieces "
             "and what they buy, and revenue is the second. The coins are far fewer "
             "than the payments made with them, because the same guinea pays one man "
             "today and another tomorrow. In the country preset the money's upkeep is "
             "subtracted, because it is a cost of the wheel, not part of what the wheel "
             "carries."),
            ("Subtracting all the circulating capital from the gross, as if it were all "
             "like money",
             "Only money comes off. Provisions, materials and finished work are "
             "&ldquo;regularly withdrawn&rdquo; into fixed capital or consumption, so "
             "they stay in the net revenue; a society's circulating capital differs "
             "from a single man's in this respect. In the lab the circulating capital "
             "has no entry of its own: only the money's upkeep is subtracted."),
            ("Taking Smith to say that machines should be cut because they are deducted",
             "The upkeep of fixed capital is deducted because it uses up labour and "
             "materials, but it &ldquo;is always repaid with great profit&rdquo;. The "
             "saving he praises is one that keeps the productive power, and the point "
             "of his own example is that the five hundred saved is put back to work. "
             "In the cheaper-machinery preset the net rises by £500 and the output does "
             "not fall."),
        ],
        "standard": (
            "Finish when you can get from a gross to a net revenue and price a saving.",
            "Given a gross revenue and the yearly upkeep of fixed capital and of money, "
            "compute the net revenue and its share of the gross, compute the effect of a "
            "stated saving on either upkeep, and say why money is not itself revenue."
        ),
        "note": (
            "The upkeep figures are written for this lesson; Smith gives only the "
            "thousand and the five hundred. He says himself that the proportion of money "
            "to the whole annual produce is &ldquo;perhaps impossible to determine&rdquo;, "
            "and that writers had put it at a fifth, a tenth, a twentieth and a "
            "thirtieth. The lab can subtract; it cannot say what a country's money "
            "costs, and it takes Smith's definition of net revenue as given."
        ),
    },
    # ---------------------------------------------------------------- 04
    # PSU text l. 9399-9990 (Book II, Chapter 2, second part). l. 9406-9434
    # (the banker's notes; a fifth); l. 9435-9492 (the million); l. 9493-9510
    # (where the gold goes); l. 9531-9559 (paper added to the wheel; a fifth);
    # l. 9560-9607 (Scotland; Glasgow); l. 9612-9683 (cash accounts; London and Edinburgh);
    # l. 9684-9708 (paper cannot exceed the gold); l. 9740-9754 (forty and forty-four
    # thousand); l. 10454-10472 (highway and waggon-way); l. 10580-10586 (note
    # equal in value to gold); l. 10533-10579 (small notes; party walls).
    {
        "slug": "paper-money-and-the-scottish-banks",
        "title": "Paper Money and the Scottish Banks",
        "module": "Book II, Chapter 2, second part · Of Money, considered as a particular Branch of the general Stock of the Society",
        "one_line": "Bank notes take the place of gold in circulation, setting the gold free to buy goods abroad, but only as many notes as the circulation can absorb will stay out of the bank.",
        "summary": (
            "Smith's argument that paper money improves a country by replacing an "
            "expensive wheel with a cheap one, worked in his own million of gold and "
            "silver and in a bank of forty thousand pounds. Compute the gold a note "
            "issue sets free from a circulation, a note total and a reserve, and what "
            "happens when a bank issues four thousand more notes than the country needs."
        ),
        "key": [
            "notes in, gold out: the channel stays full",
            "coin kept = reserve share × notes",
            "gold free = circulation − coin kept",
            "notes beyond the circulation return",
            "excess notes raise the reserve needed",
        ],
        "key_label": "Paper money in five lines",
        "concepts_intro": (
            "The argument goes in three steps. Paper replaces gold, the gold is spent "
            "abroad, and there is a limit that the bank cannot pass."
        ),
        "concepts": [
            ("Paper replaces gold",
             "A banker whose notes are trusted can lend them as readily as coin, and "
             "needs only a small reserve of coin for those that come back. The rest of "
             "the circulation, which gold and silver used to fill, the notes now fill."),
            ("The gold goes abroad and comes back as goods",
             "Notes cannot go abroad, because they cannot be demanded there, so the gold "
             "that is not needed at home goes. It buys goods, and Smith thinks most of "
             "them will be materials, tools and provisions that employ more industry."),
            ("The limit",
             "The whole paper that can circulate cannot exceed the gold and silver it "
             "replaces. Notes beyond that come straight back to the bank for coin, and "
             "the bank pays for every one it must collect again."),
        ],
        "read_title": "The million, then the forty thousand pounds",
        "read_intro": (
            "Smith works the argument twice in pounds, once for the whole country and "
            "once for a bank, and the two examples are the arithmetic of the lab."
        ),
        "body": [
            ("p", "<strong>Book II, Chapter 2.</strong> &ldquo;A particular banker lends "
                  "among his customers his own promissory notes, to the extent, we shall "
                  "suppose, of a hundred thousand&rdquo; pounds. His debtors pay him the "
                  "interest they would have paid on coin; that is where his gain comes "
                  "from. And though some notes come back, &ldquo;twenty thousand pounds "
                  "in gold and silver may, frequently, be a sufficient provision for "
                  "answering occasional demands&rdquo;. The result, in Smith's words: "
                  "&ldquo;twenty thousand pounds in gold and silver perform all the "
                  "functions which a hundred thousand could otherwise have "
                  "performed&rdquo;, and so &ldquo;Eighty thousand pounds of gold and "
                  "silver, therefore, can in this manner be spared from the circulation "
                  "of the country&rdquo;. If many banks do the same, the whole circulation "
                  "may be carried on with a fifth of the gold and silver it needed."),
            ("p", "That is the banker preset, with a reserve of one fifth. Take it slowly, "
                  "because the rest of the chapter follows from it. The banker's notes "
                  "carry a hundred thousand pounds of payments. A reserve of twenty "
                  "thousand in coin sits in his coffers, and it is the one thing that "
                  "makes the notes as good as gold: each one, Smith says, is trusted "
                  "because the holder can have coin for it &ldquo;at any time&rdquo;. The "
                  "eighty thousand in coin that used to carry those payments is no longer "
                  "wanted for them."),
            ("p", "Now the whole country. &ldquo;Let us suppose, for example, that the "
                  "whole circulating money of some particular country amounted, at a "
                  "particular time, to one million sterling, that sum being then "
                  "sufficient for circulating the whole annual produce of their land and "
                  "labour; let us suppose, too, that some time thereafter, different "
                  "banks and bankers issued promissory notes payable to the bearer, to "
                  "the extent of one million, reserving in their different coffers two "
                  "hundred thousand pounds for answering occasional demands&rdquo;. So "
                  "800,000 of coin and a million of notes, 1,800,000 in all, are poured "
                  "in to fill a channel that held a million, and they cannot all stay. "
                  "&ldquo;The channel of circulation, if I may be allowed such an "
                  "expression, will remain precisely the same as before.&rdquo; Eight "
                  "hundred thousand pounds must overflow."),
            ("p", "Where does it go? &ldquo;But the paper cannot go abroad; because at a "
                  "distance from the banks which issue it, and from the country in which "
                  "payment of it can be exacted by law, it will not be received in common "
                  "payments. Gold and silver, therefore, to the amount of eight hundred "
                  "thousand pounds, will be sent abroad&rdquo;. The million preset runs "
                  "this: a circulation of 1,000,000, notes of 1,000,000, a reserve of one "
                  "fifth. The coin kept is 200,000 and the coin set free is 800,000. "
                  "Smith adds that it does not go &ldquo;for nothing&rdquo;: its owners "
                  "will exchange it for foreign goods."),
            ("p", "What goods matter to Smith, and he gives two cases. If they are goods "
                  "for idle people, foreign wines and silks, the gold promotes "
                  "prodigality &ldquo;and is in every respect hurtful to the society&rdquo;. "
                  "If they are materials, tools and provisions to employ more industrious "
                  "people, it &ldquo;promotes industry&rdquo;, and the gross revenue and the "
                  "net rise by what those workmen add. He then argues that most of it will "
                  "go the second way, since the revenue of idle people is not raised by "
                  "banking and a class does not suddenly spend more than it has. That is "
                  "an inference from prudence, not a measurement, and it is the weakest "
                  "link in the chain; a reader who doubts it is doubting something "
                  "Smith says himself is only &ldquo;probable&rdquo;."),
            ("p", "Smith puts the gain in the terms of the last lesson. When a dealer's "
                  "ready money is replaced by credit, the gold in the till can become "
                  "stock to work on. His comparison is two merchants of equal stock, one "
                  "in London, one in Edinburgh. The London merchant &ldquo;must always "
                  "keep by him a considerable sum of money, either in his own coffers, or "
                  "in those of his banker, who gives him no interest for it&rdquo;, say five "
                  "hundred pounds, so his warehouse holds five hundred pounds less goods "
                  "and his trade is smaller by what that would have employed. The "
                  "Edinburgh merchant &ldquo;keeps no money unemployed for answering such "
                  "occasional demands&rdquo;: he draws on his cash account with the bank "
                  "and repays it piecemeal from his sales. Cash accounts, credits of "
                  "two or three thousand pounds to anyone who could find two sureties of "
                  "good landed estate, were granted, Smith believed, by banks in all "
                  "parts of the world; what was peculiar to the Scottish banks was the "
                  "easy repayment, in small sums with the interest discounted on each, "
                  "and he thought it had perhaps been the principal cause both of their "
                  "trade and of the benefit the country drew from it. He is careful about "
                  "the evidence: he says he has heard that the trade of Glasgow doubled in "
                  "fifteen years of banking, but &ldquo;I do not pretend to know&rdquo;, "
                  "and that if so it would be &ldquo;an effect too great to be accounted "
                  "for by the sole operation of this cause&rdquo;."),
            ("p", "Now the limit, and a bank's own sums. &ldquo;The whole paper money of "
                  "every kind which can easily circulate in any country, never can exceed "
                  "the value of the gold and silver, of which it supplies the place&rdquo;. "
                  "&ldquo;Should the circulating paper at any time exceed that sum, as "
                  "the excess could neither be sent abroad nor be employed in the "
                  "circulation of the country, it must immediately return upon the banks, "
                  "to be exchanged for gold and silver.&rdquo; Then comes the case the lab "
                  "was built for. Suppose, he says, that all the paper of a particular "
                  "bank which the &ldquo;circulation of the country can easily absorb and "
                  "employ, amounts exactly to forty thousand pounds, and that, for "
                  "answering occasional demands, this bank is obliged to keep at all times "
                  "in its coffers ten thousand pounds in gold and silver.&rdquo; That is "
                  "the forty preset: notes of 40,000, a reserve of a quarter, coin kept "
                  "of 10,000."),
            ("p", "Now let the bank issue four thousand more. &ldquo;Should this bank "
                  "attempt to circulate forty-four thousand pounds, the four thousand "
                  "pounds which are over and above what the circulation can easily absorb "
                  "and employ, will return upon it almost as fast as they are issued. For "
                  "answering occasional demands, therefore, this bank ought to keep at all "
                  "times in its coffers, not eleven thousand pounds only, but fourteen "
                  "thousand pounds.&rdquo; The forty-four preset enters 44,000 of notes on the "
                  "same circulation of 40,000: the quarter that Smith's bank held "
                  "against its notes is eleven thousand, and the four thousand of excess "
                  "has to be held in coin as well, since those notes go straight back "
                  "to be paid. The bank earns no interest on the excess and bears the "
                  "whole expense of collecting the coin again."),
            ("p", "Smith adds a comparison that still reads well: a highway carries all "
                  "the corn and grass to market and grows none. &ldquo;The judicious "
                  "operations of banking, by providing, if I may be allowed so violent a "
                  "metaphor, a sort of waggon-way through the air, enable the country to "
                  "convert, as it were, a great part of its highways into good pastures, "
                  "and corn fields, and thereby to increase, very considerably, the annual "
                  "produce of its land and labour.&rdquo; He does not stop there. The "
                  "country that runs on paper is &ldquo;suspended upon the Daedalian wings "
                  "of paper money&rdquo;, and is less secure than one that travels on "
                  "&ldquo;the solid ground of gold and silver&rdquo;."),
            ("p", "He therefore recommends rules, and they are worth setting beside his "
                  "praise of liberty. Banks should be restrained from issuing notes under "
                  "a certain sum: &ldquo;It were better, perhaps, that no bank notes were "
                  "issued in any part of the kingdom for a smaller sum than £5&rdquo;, so "
                  "that paper stays in the trade between dealers, and bound to pay on demand without conditions. "
                  "The objection is that this violates natural liberty, and Smith's "
                  "answer is that liberty has always been restrained where its use "
                  "&ldquo;might endanger the security of the whole society&rdquo;: "
                  "&ldquo;The obligation of building party walls, in order to prevent the "
                  "communication of fire, is a violation of natural liberty, exactly of "
                  "the same kind with the regulations of the banking trade which are here "
                  "proposed.&rdquo; Within those rules the trade may be &ldquo;perfectly "
                  "free&rdquo;, and competition among many banks makes each more careful."),
            ("p", "Three things happened after he wrote, and each bears on a step. The "
                  "argument that excess notes must return depends on the notes being "
                  "convertible; in 1797, seven years after Smith's death, the Bank of "
                  "England stopped paying coin for its notes and did not resume until "
                  "1821, and in those years the check Smith relies on did not operate. "
                  "Henry Thornton, writing in 1802, argued that a rule of lending only on "
                  "good bills does not limit the quantity of notes when prices are rising "
                  "and bills are growing. Capital's lesson <em>Medium of Circulation "
                  "and Capital: Tooke and Fullarton</em> reads a later form of the "
                  "return of notes and what Marx made of it. Whether Smith's own "
                  "conditions were enough is left to them."),
            ("p", "The next lesson, <em>Drawing and Redrawing</em>, is about what "
                  "happened in Scotland when some traders found a way to take more "
                  "from the banks than the chapter's rule allows."),
        ],
        "lab": ("wonkit", {
            "mode": "bank",
            "view": "paper",
            "money_unit": "£",
            "preset": "million",
            "presets": [
                {"id": "banker", "label": "Smith's banker: notes of £100,000, a reserve of a fifth (Smith's figures)",
                 "circulation": 100000, "notes": 100000, "reserve": 20, "expect": {"wbkKept": "£20,000", "wbkBefore": "£180,000 (£100,000 of notes, £80,000 of coin)", "wbkAbroad": "£80,000", "wbkCoin": "£0", "wbkExcess": "none: the notes do not exceed the circulation", "wbkNeeded": "£20,000 (the reserve kept)"}},
                {"id": "million", "label": "Smith's million of gold and silver and a reserve of two hundred thousand (Smith's figures)",
                 "circulation": 1000000, "notes": 1000000, "reserve": 20, "expect": {"wbkKept": "£200,000", "wbkBefore": "£1,800,000 (£1,000,000 of notes, £800,000 of coin)", "wbkAbroad": "£800,000", "wbkCoin": "£0", "wbkExcess": "none: the notes do not exceed the circulation", "wbkNeeded": "£200,000 (the reserve kept)"}},
                {"id": "forty", "label": "Smith's bank of forty thousand pounds of notes, with ten thousand in coin (Smith's figures)",
                 "circulation": 40000, "notes": 40000, "reserve": 25, "expect": {"wbkKept": "£10,000", "wbkBefore": "£70,000 (£40,000 of notes, £30,000 of coin)", "wbkAbroad": "£30,000", "wbkCoin": "£0", "wbkExcess": "none: the notes do not exceed the circulation", "wbkNeeded": "£10,000 (the reserve kept)"}},
                {"id": "forty-four", "label": "The same bank issuing forty-four thousand (Smith's figures)",
                 "circulation": 40000, "notes": 44000, "reserve": 25, "expect": {"wbkKept": "£11,000", "wbkBefore": "£73,000 (£44,000 of notes, £29,000 of coin)", "wbkAbroad": "not determined: the notes exceed the circulation", "wbkCoin": "none", "wbkExcess": "£4,000", "wbkNeeded": "£14,000 (£3,000 more than the reserve kept)"}},
            ],
            "panel_title": "What a note issue sets free",
            "panel_intro": (
                "Enter the gold and silver the circulation needs, the paper issued and "
                "the share of the notes kept in coin. The lab gives the coin kept, the "
                "coin set free, the notes beyond the circulation that come back, and the "
                "reserve needed. All four presets are Smith's own figures."
            ),
        }),
        "steps_title": "What a note issue does to the circulation",
        "steps_intro": "Four steps, with the same circulation throughout.",
        "steps": [
            ("Fix the circulation",
             "Find the gold and silver the country's trade needs to circulate. Smith says "
             "the quantity of goods to be circulated is fixed, so the quantity of "
             "money needed is fixed too."),
            ("Find the coin the bank keeps",
             "Multiply the notes issued by the share the bank keeps in coin. That is the "
             "coin that stays behind for occasional demands."),
            ("Find the gold set free",
             "When the notes fill the circulation, the rest of the circulation's gold "
             "is set free: circulation less the coin kept. It goes abroad for goods."),
            ("Test the limit",
             "If notes exceed what the circulation can absorb, the excess comes back at "
             "once for coin. The bank must hold coin against those notes too, and "
             "bears the cost of replacing it."),
        ],
        "worked": {
            "title": "Smith's million, and his bank of forty thousand",
            "intro": [
                "Take the million, forty and forty-four presets. Smith supposes a "
                "country whose circulation takes a million in gold and silver, notes of "
                "a million and a fifth of them held in coin. Then a bank whose notes of "
                "40,000 take a quarter in coin and then issue 4,000 too many.",
            ],
            "lines": [
                "coin kept:  1,000,000 · 1/5 = 200,000",
                "gold set free:  1,000,000 − 200,000 = 800,000",
                "bank's coin:  40,000 · 1/4 = 10,000",
                "excess notes:  44,000 − 40,000 = 4,000",
                "reserve Smith asks:  10,000 + 4,000 = 14,000, not 11,000",
            ],
            "after": [
                "In the first case the same exchanges are made with a fifth of the gold. In "
                "the second Smith's point is that the extra notes bring no extra business "
                "and do bring extra costs, because they come straight back and the coin "
                "that goes out to meet them has to be collected again. The lab's tile for "
                "the coin the bank needs prints his fourteen thousand for the forty-four "
                "preset, £3,000 more than the quarter it keeps.",
            ],
        },
        "quiz_title": "What paper does to a circulation",
        "quiz": [
            {"q": "A banker's notes of £50,000 take the place of coin in circulation, and "
                  "he keeps a fifth of them in coin. How much gold and silver is spared "
                  "from the circulation?",
             "a": ["£10,000",
                   "£50,000",
                   "£40,000",
                   "£60,000"],
             "c": 2,
             "why": "The coin he keeps is `50,000 · 1/5 = 10,000`, so the coin set free is "
                    "`50,000 − 10,000 = 40,000`. The ten thousand is the part that stays in "
                    "his coffers; fifty thousand would be spared only with no reserve, "
                    "which no banker could do."},
            {"q": "Why does Smith say that notes issued beyond what the circulation can "
                  "easily absorb will return to the bank?",
             "a": ["Because the law requires every note to be cancelled after a year",
                   "The excess can neither be sent abroad nor used at home, so its holders "
                   "will ask for gold and silver, which can be",
                   "Because notes are worth less than gold and nobody wants them",
                   "Because the other banks refuse to accept them"],
             "c": 1,
             "why": "&ldquo;as the excess could neither be sent abroad nor be employed in "
                    "the circulation of the country, it must immediately return upon the "
                    "banks, to be exchanged for gold and silver.&rdquo; Notes of a trusted "
                    "bank are, in the chapter, &ldquo;in every respect, equal in value to "
                    "gold and silver money&rdquo;; they come back because the extra supply "
                    "has no use, not because they are worth less."},
            {"q": "On Smith's argument, what will most of the gold and silver that paper "
                  "sets free be exchanged for?",
             "a": ["Foreign wines, silks and other goods for idle people",
                   "Nothing; it will be hoarded at home until needed",
                   "Paper money printed abroad",
                   "Materials, tools and provisions that employ more industrious people"],
             "c": 3,
             "why": "He grants that if it bought goods for idle consumers it would be "
                    "&ldquo;hurtful to the society&rdquo;, but argues that the greater "
                    "part &ldquo;will naturally be destined for the employment of "
                    "industry&rdquo;, because the revenue of idle people is not raised by "
                    "banking. He calls this probable, not certain."},
            {"q": "Why could an Edinburgh merchant carry on a greater trade than a London "
                  "merchant of equal stock, according to Smith?",
             "a": ["He kept no money idle for occasional demands, because his cash account "
                   "with the bank covered them",
                   "Scottish bank notes were worth more than English ones",
                   "Edinburgh merchants could discount bills of exchange and London merchants could not",
                   "Interest was lower in Scotland by law"],
             "c": 0,
             "why": "The London merchant must keep, say, five hundred pounds unemployed, "
                    "so his stock of goods is smaller by that sum. The Edinburgh merchant "
                    "&ldquo;keeps no money unemployed&rdquo;. Smith says expressly that "
                    "the English merchants can discount bills as easily, so the "
                    "third answer is the opposite of what he says."},
        ],
        "mistakes": [
            ("Thinking the notes add to the country's money",
             "Smith's reply is that &ldquo;the quantity of gold and silver, which is taken "
             "from the currency, is always equal to the quantity of paper which is added "
             "to it&rdquo;, so paper money &ldquo;does not necessarily increase the "
             "quantity of the whole currency&rdquo;. In the million preset the circulation "
             "is a million before and after: eight hundred thousand of coin goes out as "
             "a million of notes comes in."),
            ("Thinking the gold set free is a present to foreigners",
             "&ldquo;we must not imagine that it is sent abroad for nothing, or that its "
             "proprietors make a present of it to foreign nations.&rdquo; It buys goods, "
             "and what matters, for Smith, is what goods. That is the step in his "
             "argument most open to doubt, since it is an inference about how people "
             "spend."),
            ("Thinking a bank can issue as much as it likes, because notes cost only "
             "paper",
             "This was the view of the traders who complained that banks could extend "
             "credit &ldquo;without incurring any other expense besides that of a few "
             "reams of paper&rdquo;. The forty-four thousand preset is the answer: the "
             "excess earns nothing, returns at once, and has to be paid in coin that the "
             "bank must collect again at its own cost."),
        ],
        "standard": (
            "Finish when you can compute the gold a note issue sets free and the limit "
            "on it.",
            "Given a circulation, a note issue and a reserve share, compute the coin "
            "kept, the gold and silver set free and the notes beyond the circulation, "
            "and say why Smith expects the excess to come back."
        ),
        "note": (
            "Smith's notes are promises to pay coin on demand, and his limit works because "
            "they can be presented. The lab models that and nothing else: no deposits, no "
            "central bank, no inconvertible money. It also takes the circulation as given, "
            "when Smith himself says the proportion of money to produce, a fifth, a tenth, "
            "a twentieth or a thirtieth, cannot be determined. Whether banks in practice "
            "kept to his rule is what the next lesson is about."
        ),
    },
    # ---------------------------------------------------------------- 05
    # PSU text l. 9990-10767 (Book II, Chapter 2, last part). l. 9990-10021
    # (over-trading; the shift); l. 10022-10076 (A and B; interest and commission);
    # l. 10077-10088 (profits of six to ten per cent); l. 10089-10124 (note);
    # l. 10125-10202 (circulating bills; the banks and the projectors); l. 10203-10284
    # (the new bank, six hundred thousand, eight per cent); l. 10036-10053 (the
    # privileges of a bill; the weary traveller); l. 9829-9877
    # (real bills; the water-pond); l. 9936-9981 (what a bank can advance; fixed
    # capital); l. 10747-10764 (free trade in banking).
    {
        "slug": "drawing-and-redrawing",
        "title": "Drawing and Redrawing",
        "module": "Book II, Chapter 2, last part · Of Money, considered as a particular Branch of the general Stock of the Society",
        "one_line": "Raising money by drawing bills on a friend who redraws them back costs a trader eight per cent or more a year, and the banks that discount the bills advance a capital that never returns to them.",
        "summary": (
            "Smith explains the trick of drawing and redrawing, shows how it pulled "
            "capital out of the Scottish banks, and says what a bank may with propriety "
            "lend. Compute what a year of renewals costs from the interest, the "
            "commission and the term of each bill, and set it beside the profits a "
            "merchant can hope to earn."
        ),
        "key": [
            "draws a year = 12 / months a bill runs",
            "yearly cost = interest + commission × draws",
            "5% interest and ½% six times: 8%",
            "with interest on interest: a little more",
            "a real bill replaces what it advanced",
        ],
        "key_label": "Drawing and redrawing in five lines",
        "concepts_intro": (
            "The last third of the chapter is a warning, and it is told as a case. "
            "Three ideas carry it."
        ),
        "concepts": [
            ("A bill drawn to be redrawn",
             "A in Edinburgh draws on B in London for a bill with no debt behind it. B "
             "accepts on condition that he may redraw on A, before it falls due, for the "
             "same sum with interest and commission. The renewal repeats, and each bill "
             "is discounted at a bank."),
            ("Real bills and circulating bills",
             "A bank that discounts a real bill, drawn by a real creditor on a real "
             "debtor, is repaid when it falls due and its coffers refill. A circulating "
             "bill is never really paid: another is always drawn to pay the last, and "
             "the value advanced never returns to the bank."),
            ("What a bank may advance",
             "A bank can properly lend only the part of a trader's capital that he would "
             "otherwise keep idle in ready money. It cannot lend his whole capital, and "
             "least of all his fixed capital, which returns too slowly for a bank."),
        ],
        "read_title": "A in Edinburgh and B in London, then the new bank",
        "read_intro": (
            "Smith explains the practice for readers who are not men of business, and "
            "then tells what it did to the banks. He is not neutral about it."
        ),
        "body": [
            ("p", "<strong>Book II, Chapter 2.</strong> &ldquo;The practice of drawing "
                  "and redrawing is so well known to all men of business, that it may, "
                  "perhaps, be thought unnecessary to give any account of it. But as this "
                  "book may come into the hands of many people who are not men of "
                  "business, and as the effects of this practice upon the banking trade "
                  "are not, perhaps, generally understood, even by men of business "
                  "themselves, I shall endeavour to explain it as distinctly as I "
                  "can.&rdquo;"),
            ("p", "He first says when it began. Traders who had over-traded, after the "
                  "banks would not lend them as much as they wished, turned to &ldquo;the "
                  "well known shift of drawing and redrawing; the shift to which "
                  "unfortunate traders have sometimes recourse, when they are upon the "
                  "brink of bankruptcy&rdquo;. A bill of exchange, he explains, has "
                  "privileges: money is advanced on it more readily than on any other "
                  "obligation, and if the acceptor does not pay when it is presented he is "
                  "&ldquo;from that moment a bankrupt&rdquo;. Short dates add security. "
                  "His image is of a weary traveller who thinks the house he has come "
                  "to is crazy and will not stand very long, &ldquo;but it is a chance "
                  "if it falls to-night&rdquo;."),
            ("p", "Now A and B. A in Edinburgh draws a bill on B in London, payable in two "
                  "months. &ldquo;In reality B in London owes nothing to A in "
                  "Edinburgh&rdquo;. B accepts on condition that before it falls due he "
                  "shall redraw on A &ldquo;for the same sum, together with the interest "
                  "and a commission, another bill, payable likewise two months after "
                  "date&rdquo;. A does the same again before that one falls due, and B "
                  "again. It &ldquo;has sometimes gone on, not only for several months, but "
                  "for several years together&rdquo;. A discounts the bills he draws with "
                  "a bank in Edinburgh, and B discounts the ones he redraws in London, "
                  "so the money A raises is, in every round, advanced by a bank."),
            ("p", "What did it cost? &ldquo;The interest was five per cent. in the "
                  "year, and the commission was never less than one half per cent. on each "
                  "draught.&rdquo; Two-month bills are drawn six times a year, so: "
                  "&ldquo;This commission being repeated more than six times in the year, "
                  "whatever money A might raise by this expedient might necessarily have "
                  "cost him something more than eight per cent. in the year and sometimes "
                  "a great deal more, when either the price of the commission happened to "
                  "rise, or when he was obliged to pay compound interest&rdquo; upon the "
                  "interest and commission of former bills. The lab's two-months preset "
                  "is this: £10,000 raised on two-month bills at five per cent interest "
                  "and a half per cent commission. Interest five, commission six halves "
                  "makes three, and the simple cost is eight per cent, £800 a year. Counted "
                  "with interest on each round's interest and commission, it comes a "
                  "little above, as Smith says. The name for it was &ldquo;raising money "
                  "by circulation&rdquo;."),
            ("p", "Smith then asks what a project would need to earn to pay for this. "
                  "&ldquo;In a country where the ordinary profits of stock, in the greater "
                  "part of mercantile projects, are supposed to run between six and ten "
                  "per cent. it must have been a very fortunate speculation, of which the "
                  "returns could not only repay the enormous expense at which the money "
                  "was thus borrowed for carrying it on, but afford, besides, a good "
                  "surplus profit to the projector.&rdquo; The projectors, he adds, had "
                  "&ldquo;in their golden dreams the most distinct vision of this great "
                  "profit&rdquo; and, on waking, very seldom found it. Eight per cent "
                  "would take most or all of an ordinary profit of six to ten per cent "
                  "before a project had earned its projector a penny."),
            ("p", "The harm to the banks is the point of the passage. The bank that "
                  "discounted such a bill advanced, in its notes, a value that never came "
                  "back. &ldquo;This payment, therefore, was altogether fictitious. The "
                  "stream which, by means of those circulating bills of exchange, had once "
                  "been made to run out from the coffers of the banks, was never replaced "
                  "by any stream which really ran into them.&rdquo; The notes so issued "
                  "were, on many occasions, &ldquo;the whole fund destined for carrying on "
                  "some vast and extensive project&rdquo; and so far over what a "
                  "circulation could absorb that they returned to the banks for gold. It "
                  "was a capital, Smith says, that the projectors had drawn out of the "
                  "banks &ldquo;not only without their knowledge or deliberate consent, "
                  "but for some time, perhaps, without their having the most distant "
                  "suspicion that they had really advanced it&rdquo;."),
            ("p", "Compare it with a real bill. &ldquo;When a bank discounts to a merchant "
                  "a real bill of exchange, drawn by a real creditor upon a real debtor, "
                  "and which, as soon as it becomes due, is really paid by that debtor; it "
                  "only advances to him a part of the value which he would otherwise be "
                  "obliged to keep by him unemployed and in ready money, for answering "
                  "occasional demands.&rdquo; Then the bank's coffers &ldquo;resemble a "
                  "water-pond, from which, though a stream is continually running out, yet "
                  "another is continually running in, fully equal to that which runs "
                  "out&rdquo;. Little or no expense is needed to replenish them. Draw and "
                  "redraw, and the stream out runs on and the stream in never comes."),
            ("p", "When the bankers noticed and refused more, the projectors blamed them. "
                  "Smith says they called their own distress &ldquo;the distress of the "
                  "country&rdquo;, and complained of the banks' &ldquo;ignorance, "
                  "pusillanimity, and bad conduct&rdquo;. Then &ldquo;a new bank was "
                  "established in Scotland&rdquo; to relieve it. Smith does not name it; "
                  "historians identify it with the Ayr bank, which opened in 1769 and "
                  "stopped in 1772. It would, he says, advance &ldquo;the whole "
                  "capital&rdquo; for improvements of the slowest return, such as the "
                  "improvement of land, and made &ldquo;scarce any distinction between "
                  "real and circulating bills&rdquo;. It stopped with about two hundred "
                  "thousand pounds of notes outstanding and had been drawing bills on "
                  "London, &ldquo;upwards of six hundred thousand pounds&rdquo;, to "
                  "support them."),
            ("p", "Then Smith does the sum for the bank. &ldquo;Upon the two hundred "
                  "thousand pounds which it circulated in bank notes, this five per cent. "
                  "might perhaps be considered as a clear gain&rdquo;. But on "
                  "&ldquo;upwards of six hundred thousand pounds, for which it was "
                  "continually drawing bills of exchange upon London, it was paying, in "
                  "the way of interest and commission, upwards of eight per cent. and was "
                  "consequently losing more than three per cent. upon more than three "
                  "fourths of all its dealings.&rdquo; The ayr-bank preset enters his round "
                  "figures: 600,000 on two-month bills at five per cent and a half "
                  "per cent. The yearly cost is eight per cent, £48,000. Against the five "
                  "per cent the bank was earning, that is a loss of three per cent, "
                  "£18,000. Smith's conclusion about the bank's effect is hard: it "
                  "&ldquo;thereby only enabled them to get so much deeper into "
                  "debt&rdquo; and, in the long run, &ldquo;increased the real distress of "
                  "the country, which it meant to relieve&rdquo;."),
            ("p", "What should a bank lend? &ldquo;What a bank can with propriety advance "
                  "to a merchant or undertaker of any kind, is not either the whole "
                  "capital with which he trades, or even any considerable part of that "
                  "capital; but that part of it only which he would otherwise be obliged "
                  "to keep by him unemployed and in ready money, for answering occasional "
                  "demands.&rdquo; The test is in the repayments: if over four, six or "
                  "eight months they equal the advances, the bank is safe; if they fall "
                  "short, it is feeding a trader's capital with its own. Fixed capital "
                  "comes back too slowly: &ldquo;The returns of the fixed capital are, in "
                  "almost all cases, much slower than those of the circulating "
                  "capital&rdquo;, and long loans &ldquo;ought not to be borrowed of a "
                  "bank, but ought to be borrowed upon bond or mortgage, of such private "
                  "people as propose to live upon the interest of their money&rdquo;. A "
                  "bank would be &ldquo;a very convenient creditor&rdquo; to such traders, "
                  "and they &ldquo;most inconvenient debtors to such a bank&rdquo;. The "
                  "three-months preset is a mild case, written for this lesson: three-month "
                  "bills, so four draws a year, which cost seven per cent."),
            ("p", "Three points for the other side of the ledger. Later writers, Thornton "
                  "among them, doubted that discounting only real bills limits issue, "
                  "since bills grow when prices rise; the lesson on paper money has the "
                  "reference. The Ayr bank's defenders have said it was brought down by a "
                  "failure of credit in London in 1772 that hit sound banks as well as "
                  "unsound; Smith's account, written within four years, is of a bank "
                  "that never had the coin to meet its notes. And Marx took the "
                  "practice up as a case of credit that outruns the real sale of goods; "
                  "Capital's lesson <em>Credit and Fictitious Capital</em> has "
                  "its own three-bill example and reads it in his terms."),
            ("p", "That ends Book II's two chapters on the nature of stock and money. The "
                  "next course, <em>Accumulation and the Employments of Capital</em>, "
                  "starts from a different question: which labour adds to a nation's "
                  "stock, and which does not."),
        ],
        "lab": ("wonkit", {
            "mode": "bank",
            "view": "redraw",
            "money_unit": "£",
            "preset": "two-months",
            "presets": [
                {"id": "two-months", "label": "A in Edinburgh: £10,000 on two-month bills, interest five per cent, commission a half (Smith's rates)",
                 "sum": 10000, "interest": 5, "commission": "1/2", "months": 2, "years": 1,
                 "expect": {"wbkDraws": "6 draws a year", "wbkSimple": "8% a year, £800", "wbkCompound": "≈ 8.27% a year, ≈ £827.15", "wbkTotal": "simple £800, compound ≈ £827.15 over 1 year", "wbkExcess": "simple +3 points, compound ≈ +3.27 points"}},
                {"id": "ayr-bank", "label": "The new bank's £600,000 of drafts on London, at the same rates (Smith's round figures)",
                 "sum": 600000, "interest": 5, "commission": "1/2", "months": 2, "years": 1,
                 "expect": {"wbkDraws": "6 draws a year", "wbkSimple": "8% a year, £48,000", "wbkCompound": "≈ 8.27% a year, ≈ £49,628.73", "wbkTotal": "simple £48,000, compound ≈ £49,628.73 over 1 year", "wbkExcess": "simple +3 points, compound ≈ +3.27 points"}},
                {"id": "three-months", "label": "Three-month bills, written for this lesson",
                 "sum": 10000, "interest": 5, "commission": "1/2", "months": 3, "years": 1,
                 "expect": {"wbkDraws": "4 draws a year", "wbkSimple": "7% a year, £700", "wbkCompound": "≈ 7.19% a year, ≈ £718.59", "wbkTotal": "simple £700, compound ≈ £718.59 over 1 year", "wbkExcess": "simple +2 points, compound ≈ +2.19 points"}},
            ],
            "panel_title": "What a year of renewals costs",
            "panel_intro": (
                "Enter the sum raised, the yearly interest, the commission each time a "
                "bill is drawn, the term of each bill in months and the years it goes on. "
                "The lab gives the draws in a year, the yearly cost simply and with "
                "interest on interest, and the excess over the stated interest. The "
                "two-month rates are Smith's; the three-month preset is written for "
                "the lesson."
            ),
        }),
        "steps_title": "Pricing a year of renewals",
        "steps_intro": "Four steps, the first being the one people skip.",
        "steps": [
            ("Count the draws",
             "Divide twelve months by the term of each bill. Two-month bills are drawn "
             "six times a year, three-month bills four times."),
            ("Take the interest once",
             "Interest is a yearly rate, so it is paid once over the year in this "
             "simple count. Smith's five per cent is the legal rate."),
            ("Add the commission for every draw",
             "Multiply the commission by the draws. A half per cent six times is three "
             "per cent, and it is the part that makes the practice dear."),
            ("Set it beside profit",
             "The total is the yearly cost of the money. Compare it with the six to ten "
             "per cent Smith says a merchant may expect, and with the interest the "
             "bank earns on its advance."),
        ],
        "worked": {
            "title": "Eight per cent, and three per cent lost",
            "intro": [
                "Take the first two presets. Smith's rates: bills of two months, five "
                "per cent interest and a half per cent commission on each draught, "
                "first on a sum of £10,000, then on the new bank's £600,000.",
            ],
            "lines": [
                "draws a year:  12 / 2 = 6",
                "interest:  5",
                "commission:  6 · 1/2 = 3",
                "yearly cost:  5 + 3 = 8 per cent, so 800 on 10,000",
                "the bank's loss:  8 − 5 = 3 per cent, so 18,000 on 600,000",
            ],
            "after": [
                "Those are Smith's own words in figures: &ldquo;upwards of eight per "
                "cent&rdquo; paid, five received, &ldquo;losing more than three per "
                "cent&rdquo;. With a month longer on every bill, in the three-months preset, the "
                "draws fall to four and the cost to seven per cent, since the interest is "
                "still the same five and the commission is paid two fewer times.",
            ],
        },
        "quiz_title": "The cost of a bill that never dies",
        "quiz": [
            {"q": "A trader raises money on bills that run for two months, paying interest "
                  "of 6 per cent a year and a commission of 1 per cent each time a bill "
                  "is drawn. By the simple count, what does the money cost him in a year?",
             "a": ["7 per cent",
                   "6 per cent",
                   "12 per cent",
                   "42 per cent"],
             "c": 2,
             "why": "There are `12/2 = 6` draws, so commission is `6 · 1 = 6` per cent, and "
                    "with interest of 6 per cent the cost is `6 + 6 = 12` per cent. Seven "
                    "counts the commission once, six leaves it out, and forty-two charges "
                    "the whole year's interest again at every draw."},
            {"q": "Why does Smith call the payment of a redrawn bill fictitious?",
             "a": ["Because the signatures on the bills were forged",
                   "Because before each bill fell due another was drawn, and its "
                   "discounting was needed to pay the first, so the value advanced "
                   "was never really returned to the bank",
                   "Because the bills were paid in paper and not in gold",
                   "Because the bank charged commission on each bill"],
             "c": 1,
             "why": "&ldquo;The stream which, by means of those circulating bills of "
                    "exchange, had once been made to run out from the coffers of the "
                    "banks, was never replaced by any stream which really ran into "
                    "them.&rdquo; Smith does not say the signatures were forged or that "
                    "paper payment was the fault."},
            {"q": "On Smith's account, what may a bank with propriety advance to a "
                  "merchant?",
             "a": ["The whole capital he trades with",
                   "The money for his warehouse, forge or improvements, so long as the "
                   "security is good",
                   "Whatever he asks, since a note costs only paper",
                   "The part of his capital that he would otherwise keep idle in ready "
                   "money for occasional demands"],
             "c": 3,
             "why": "&ldquo;that part of it only which he would otherwise be obliged to "
                    "keep by him unemployed and in ready money, for answering occasional "
                    "demands.&rdquo; Fixed capital returns too slowly for a bank, and "
                    "&ldquo;a few reams of paper&rdquo; is what the over-trading "
                    "projectors thought a loan cost; Smith says otherwise."},
            {"q": "What kind of bill leaves a bank's coffers refilled when it falls due?",
             "a": ["A real bill, drawn by a real creditor on a real debtor",
                   "A bill drawn by A on B and redrawn by B on A",
                   "A bill discounted at several banks at once",
                   "A bill longer than six months"],
             "c": 0,
             "why": "A real bill, &ldquo;as soon as it becomes due, is really paid by that "
                    "debtor&rdquo;, so the payment replaces the advance with its interest "
                    "and the coffers are like a pond with an equal stream running in "
                    "and out. A circulating bill is paid by drawing another."},
        ],
        "mistakes": [
            ("Counting only the interest and forgetting the commission",
             "The interest on A's bills was the legal five per cent a year, like any "
             "loan. The commission was paid each time a bill was drawn, and in six "
             "draws it added three per cent. In the first preset the whole cost is "
             "eight per cent, of which the commission is three eighths."),
            ("Thinking the bills were harmless because each was paid on time",
             "Each bill was paid, by the next. The payment was &ldquo;altogether "
             "fictitious&rdquo;, because the discounting of the new bill was needed to "
             "pay the old, and the bank never got back the value it first advanced. "
             "The test Smith gives is whether repayments equal advances within a few "
             "months; here they could not."),
            ("Reading Smith as saying banks should lend only to rich men",
             "His rule is about what is lent, not to whom. Real bills and cash "
             "accounts are good business; the whole capital of a trader, and above all "
             "fixed capital, is not, whatever the borrower's fortune. Money for fixed "
             "capital, he says, ought to be borrowed &ldquo;upon bond or mortgage, of "
             "such private people as propose to live upon the interest of their "
             "money&rdquo;, who can wait for slow returns."),
        ],
        "standard": (
            "Finish when you can price a year of renewals and say why the bank loses.",
            "Given an interest rate, a commission per draw and the term of each bill, "
            "compute the draws a year and the simple yearly cost, compare it with a "
            "rate the bank earns, and say why the payment of a redrawn bill returns "
            "nothing to the bank."
        ),
        "note": (
            "The lab prices renewals, and the price is the least of what Smith says. It "
            "cannot show which bills were real and which were not, or whether a banker "
            "could tell; Smith himself says the difficulty of telling was the practice's "
            "protection. The first two presets are his rates and round figures, but he "
            "says his eight per cent is a floor, and later accounts of the bank disagree "
            "about how far the distress it met was of its own making. The lab can "
            "work the arithmetic of his reading and not decide between readings."
        ),
    },
]
