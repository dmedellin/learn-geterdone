"""The Division of Labour, lessons 1-4 -- the Introduction and Book I, Chapters 1-3.

Every quotation is copied from /mnt/project-files/wealth-texts/wealth-of-nations-psu.txt
(the Electronic Classics Series edition, Pennsylvania State University, 2005);
the comment beside each lesson gives its line numbers. Smith's spelling is kept
inside quotations, and a drop-capital opening ("THE ANNUAL LABOUR") is quoted
from the first lower-case word.

Figures of Smith's own, used as preset data: the pin factory (l. 231-248), the
nailers (l. 316-329), the Highland nailer (l. 632-637) and the wagon and the ship
(l. 643-651). The nations, the hunters, the producers and the places are written
for the lessons and the presets say so.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # PSU text l. 107-115 (the first sentence), l. 116-122 (two circumstances),
    # l. 123-142 (savage and civilized), l. 143-183 (the plan of the five Books).
    {
        "slug": "the-annual-labour-of-every-nation",
        "title": "The Annual Labour of Every Nation",
        "module": "Introduction and Plan of the Work",
        "one_line": "A nation is well supplied by what its labour produces for each head, and that depends on skill first and on how many work second.",
        "summary": (
            "Smith opens the book with a sum before he has a figure: the produce of a "
            "nation's labour, divided by the number who consume it, is what the nation "
            "has to live on. Compute that produce per head from a population, the share "
            "at work and the output of each worker, and see why a nation in which many do "
            "no work can still supply its poorest better than one in which nearly all do."
        ),
        "key": [
            "produce per head = share at work × output",
            "produce = workers × output per worker",
            "per head = produce / population",
            "supply turns on skill and share at work",
            "Smith: skill seems to matter the more",
        ],
        "key_label": "The opening sum in five lines",
        "concepts_intro": (
            "The Introduction is two pages, and it does three things: it says what a "
            "nation's wealth is, it names the two things that decide how much there is, and "
            "it tells you where in the book each one is dealt with."
        ),
        "concepts": [
            ("Wealth is a yearly flow of necessaries",
             "Smith does not begin with gold, land or a treasury. The wealth of a nation is "
             "the yearly produce of its labour, together with whatever that produce buys "
             "from other nations: the &ldquo;necessaries and conveniencies of life&rdquo; "
             "that the people consume in a year."),
            ("Produce per head, not produce",
             "A large produce shared among a great many people can leave each short, and a "
             "small one shared among few can leave each well supplied. What matters is the "
             "proportion the produce bears to the number who are to consume it."),
            ("Two circumstances regulate the proportion",
             "First the skill, dexterity and judgment with which labour is applied; "
             "second the proportion between those employed in useful labour and those who "
             "are not. Smith says the first seems to matter more, and the whole of Book I "
             "is spent on it."),
        ],
        "read_title": "The opening sentence, then the contrast between nations",
        "read_intro": (
            "Read the first paragraph slowly, because the rest of the book hangs from it. "
            "Then read Smith's two portraits of a nation, which are the nearest thing the "
            "Introduction has to an argument."
        ),
        "body": [
            ("p", "<strong>Introduction and Plan of the Work.</strong> The first sentence "
                  "says that the annual labour &ldquo;of every nation is the fund which "
                  "originally supplies it with all the necessaries and conveniencies of life "
                  "which it annually consumes, and which consist always either in the "
                  "immediate produce of that labour, or in what is purchased with that "
                  "produce from other nations.&rdquo;"),
            ("p", "Take it a phrase at a time. A <em>fund</em> is a store you draw on, and "
                  "Smith means a store that is refilled every year: nothing here is a "
                  "treasure laid up once. <em>Necessaries and conveniencies</em> is his "
                  "plain phrase for what we would call goods: what you need to live and what "
                  "makes living easier. And the last clause matters for later books: a "
                  "nation can have its supply from its own labour or from what that labour "
                  "buys abroad. Smith is already saying that foreign trade is a way of "
                  "turning the nation's own work into things it wants, a thesis that Book IV "
                  "argues at length."),
            ("p", "The next sentence turns the fund into a quotient. The nation will be "
                  "better or worse supplied according as this produce &ldquo;bears a greater "
                  "or smaller proportion to the number of those who are to consume it&rdquo;. "
                  "Write that as a sum and you have the lab for this lesson: "
                  "`produce per head = produce / population`. A rich country is one in which "
                  "that quotient is large, and a poor country is one in which it is small, "
                  "whatever the country's size."),
            ("p", "Then Smith names what regulates the quotient: &ldquo;first, by the skill, "
                  "dexterity, and judgment with which its labour is generally applied; and, "
                  "secondly, by the proportion between the number of those who are employed "
                  "in useful labour, and that of those who are not so employed.&rdquo; "
                  "Those two are the two factors on the right-hand side of "
                  "`produce per head = share at work × output per worker`, which you get by "
                  "writing the produce as workers times output and dividing by the whole "
                  "population. The first factor is the fraction of the people at useful "
                  "work. The second is how much each of them turns out in the year."),
            ("def", ("Useful labour",
                     "The Introduction's word for work that supplies the nation's necessaries "
                     "and conveniencies, set against the work of those who &ldquo;are not so "
                     "employed&rdquo;. Book II, Chapter 3 draws a sharper line between "
                     "productive and unproductive labour, and the course on accumulation "
                     "reads it; here the word means only what it says: labour whose result "
                     "is something the people consume.")),
            ("p", "Now the portraits. &ldquo;Among the savage nations of hunters and "
                  "fishers, every individual who is able to work is more or less employed in "
                  "useful labour&rdquo;, and yet Smith says such nations are so poor that they "
                  "are sometimes driven to abandon their infants and their old people. "
                  "&ldquo;Among civilized and thriving nations, on the contrary, though a "
                  "great number of people do not labour at all, many of whom consume the "
                  "produce of ten times, frequently of a hundred times, more labour than the "
                  "greater part of those who work; yet the produce of the whole labour of the "
                  "society is so great, that all are often abundantly supplied.&rdquo;"),
            ("p", "The lab puts numbers on the contrast, with figures written for this lesson "
                  "because Smith gives none. In the first preset, <code>contrast</code>, a "
                  "hunters' nation has 100 people, 60 of them at work, each turning out 2 "
                  "units a year; a civilized nation has 100 people, only 40 at work, each "
                  "turning out 12. The hunters' produce is 120 units, `6/5` a head. The "
                  "civilized nation's is 480, `24/5` a head: four times as much for each "
                  "person, with a third fewer at work. Take the second preset, "
                  "<code>few-at-work</code>, and let only 20 of the 100 work: the produce "
                  "falls to 240 and `12/5` a head, and the civilized people are still "
                  "twice as well supplied as the hunters. That is Smith's claim in "
                  "arithmetic, and it is why he says the first circumstance seems to matter "
                  "more than the second."),
            ("p", "The third preset, <code>same-skill</code>, shows the other half, and "
                  "Smith does not deny it. Give both nations the same output of 2 a worker "
                  "and the nation with more at work wins: the hunters' 120 units against "
                  "the other's 80. The share at work does matter. It is only that a "
                  "difference in skill can be of any size, while the share at work is a "
                  "fraction and cannot exceed one."),
            ("p", "The portrait of the &ldquo;savage&rdquo; deserves a second look, because it "
                  "is the weakest part of the passage and Smith's readers have said so. It is "
                  "a conjecture built from travellers' reports, one stage in a story he "
                  "tells of societies passing from hunting to herding, farming and commerce. "
                  "The anthropologist Marshall Sahlins argued in 1972, from field studies of "
                  "present-day hunting peoples, that they often worked few hours and wanted "
                  "little, so that poverty is not the right word for how they lived. Others "
                  "answered that small present-day groups cannot stand for all the past. The "
                  "lab does not decide between them. It takes Smith's contrast as a stated "
                  "pair of nations and computes what the opening sentence implies for them."),
            ("p", "Last, the plan. The first book is to explain the &ldquo;causes of this "
                  "improvement in the productive powers of labour&rdquo; and how the produce "
                  "is shared among the ranks of the people. The second, on capital stock, "
                  "explains why the number of useful labourers depends on how much stock sets "
                  "them to work. The third explains how the policy of Europe came to favour "
                  "towns over the country, and the fourth examines the theories that grew up "
                  "round that policy. The fifth is about the revenue of the sovereign. This "
                  "Subject follows him through all five."),
            ("def", ("Money and measures, once",
                     "Smith's sums are in the money of his day. Twelve pence (written d, "
                     "from the Latin denarius) make a shilling (s), and twenty shillings make "
                     "a pound (£), so a pound is two hundred and forty pence. A farthing is a "
                     "quarter of a penny. Corn is sold by the quarter, which is eight "
                     "bushels. Ounces and pounds of silver are weights. The lessons repeat a "
                     "unit where a figure needs it, and the labs say which unit they use.")),
            ("p", "That is the whole Introduction: one sentence that says what to measure, "
                  "one that says what moves it, and a map of the road. The next lesson goes "
                  "straight to Smith's own answer to the second factor, with the most famous "
                  "factory in economics, a workshop of ten men making pins."),
        ],
        "lab": ("wonkit", {
            "mode": "division",
            "view": "supply",
            "qty_unit": "units",
            "preset": "contrast",
            "presets": [
                {"id": "contrast",
                 "label": "A hunters' nation and a civilized one, written for this lesson",
                 "nations": "hunters, 100, 60, 2; civilized, 100, 40, 12",
                 "expect": {
                          "wdvShare": "hunters 3/5 = 60%; civilized 2/5 = 40%",
                          "wdvProduce": "hunters 120 units; civilized 480 units",
                          "wdvPerHead": "hunters 6/5 = 1.20 units; civilized 24/5 = 4.80 units",
                          "wdvBest": "civilized, 24/5 = 4.80 units a head",
                          "wdvRatio": "4× (civilized over hunters)",
                         }},
                {"id": "few-at-work",
                 "label": "Only 20 in 100 at work in the civilized nation, written for this lesson",
                 "nations": "hunters, 100, 60, 2; civilized, 100, 20, 12",
                 "expect": {
                          "wdvShare": "hunters 3/5 = 60%; civilized 1/5 = 20%",
                          "wdvProduce": "hunters 120 units; civilized 240 units",
                          "wdvPerHead": "hunters 6/5 = 1.20 units; civilized 12/5 = 2.40 units",
                          "wdvBest": "civilized, 12/5 = 2.40 units a head",
                          "wdvRatio": "2× (civilized over hunters)",
                         }},
                {"id": "same-skill",
                 "label": "The same output a worker in both, written for this lesson",
                 "nations": "hunters, 100, 60, 2; civilized, 100, 40, 2",
                 "expect": {
                          "wdvShare": "hunters 3/5 = 60%; civilized 2/5 = 40%",
                          "wdvProduce": "hunters 120 units; civilized 80 units",
                          "wdvPerHead": "hunters 6/5 = 1.20 units; civilized 4/5 = 0.80 units",
                          "wdvBest": "hunters, 6/5 = 1.20 units a head",
                          "wdvRatio": "3/2 = 1.50× (hunters over civilized)",
                         }},
            ],
            "panel_title": "What a nation has for each head",
            "panel_intro": (
                "Each nation's population, the number at useful work and the output of each "
                "go in; the lab multiplies, divides and compares. Try the three presets in "
                "turn and watch which factor moves the produce per head."
            ),
        }),
        "steps_title": "Computing a nation's supply per head",
        "steps_intro": "Four steps, the same for any nation whose three figures you know.",
        "steps": [
            ("Find the share at work",
             "Divide the number at useful labour by the whole population. Everyone is in the "
             "denominator, the old, the young and the idle, because they all consume."),
            ("Fix the output of a worker",
             "State what one worker turns out in a year, in some one unit. Smith's first "
             "circumstance, skill, lives here: a more skilful or better-equipped worker "
             "has a larger number."),
            ("Multiply, then divide",
             "The produce is the workers times the output of each. Divide it by the "
             "population and you have the produce per head, which equals the share at work "
             "times the output."),
            ("Compare, one change at a time",
             "Set two nations side by side, or one nation before and after, and change "
             "either the share at work or the output, not both. Whichever moves the produce "
             "per head more is the one that matters more in that case."),
        ],
        "worked": {
            "title": "Four times as well supplied with a third fewer at work",
            "intro": [
                "Take the first preset. The hunters' nation has 100 people, 60 at work, each "
                "making 2 units a year; the civilized nation has 100 people, 40 at work, "
                "each making 12. You want the produce per head of each and how they compare.",
            ],
            "lines": [
                "hunters:  60 · 2 = 120 units",
                "hunters per head:  120 / 100 = 6/5",
                "civilized:  40 · 12 = 480 units",
                "civilized per head:  480 / 100 = 24/5",
                "ratio:  (24/5) / (6/5) = 4",
            ],
            "after": [
                "The civilized nation has 40 at work against the hunters' 60 and is four "
                "times better supplied, because each of its workers makes six times as "
                "much. Cut its workers to 20 and the ratio halves to 2, which is still "
                "better than one. The figures are the lesson's, and the next lessons ask "
                "where the factor of six comes from.",
            ],
        },
        "quiz_title": "Supply per head",
        "quiz": [
            {"q": "In the Introduction, which of the two circumstances does Smith say the "
                  "abundance or scantiness of a nation's supply seems to depend on more?",
             "a": ["The proportion of the people employed in useful labour",
                   "The skill, dexterity and judgment with which labour is applied",
                   "The soil, climate and extent of the territory",
                   "The share of the produce bought from other nations"],
             "c": 1,
             "why": "Smith writes that the supply &ldquo;seems to depend more upon the "
                    "former of those two circumstances than upon the latter&rdquo;, and the "
                    "former is skill, dexterity and judgment. The proportion employed is "
                    "the second circumstance. He says that whatever the soil, climate or "
                    "territory, the supply depends on those two, so they are not a third "
                    "circumstance, and trade appears only as a way of getting the produce."},
            {"q": "A nation has 200 people, 50 of them at useful work, each producing 12 "
                  "units a year. What is its produce per head?",
             "a": ["3 units", "12 units", "600 units", "1/4 of a unit"],
             "c": 0,
             "why": "The produce is `50 · 12 = 600`, and shared among 200 people it is "
                    "`600/200 = 3` a head. Twelve is the output of one worker, 600 is the "
                    "produce of the whole nation, and one quarter is the share of the "
                    "population at work."},
            {"q": "Why does Smith say a civilized nation can supply even its poorest "
                  "workman abundantly, though many of its people do no labour?",
             "a": ["Those who do not labour consume very little",
                   "Its land is more fertile than the hunters' land",
                   "The produce of the whole labour of the society is so great",
                   "It buys its supplies from savage nations"],
             "c": 2,
             "why": "Smith's words are that &ldquo;the produce of the whole labour of the "
                    "society is so great, that all are often abundantly supplied&rdquo;. "
                    "He says the idle consume ten or a hundred times as much as a worker, "
                    "so the first answer is the reverse of his, and he sets the soil aside "
                    "at the start. Foreign trade is a way to spend the produce, and nothing "
                    "in the passage makes the savage nations a source of supply."},
            {"q": "Which Book does the Introduction say treats of the nature of capital "
                  "stock and the manner in which it is accumulated?",
             "a": ["The first", "The second", "The third", "The fifth"],
             "c": 1,
             "why": "The second book. The first treats of the causes of improvement in the "
                    "productive powers of labour and of how the produce is distributed. The "
                    "third explains the course Europe's policy took, and the fifth is "
                    "about the revenue of the sovereign."},
        ],
        "mistakes": [
            ("Thinking more people at work always means more wealth",
             "The share at work is one of two factors, and the other can dominate it. In "
             "the <code>contrast</code> preset the nation with fewer at work has four "
             "times the supply per head. Counting heads at work tells you about one factor "
             "and nothing about the other."),
            ("Reading the produce as the wealth, not the produce per head",
             "A nation of 1,000 people with a produce of 3,000 units is worse supplied than "
             "one of 100 with a produce of 600, though its produce is five times larger. "
             "Smith's test is the proportion the produce bears to those who consume it."),
            ("Treating the lesson's nations as Smith's figures",
             "Smith gives no numbers in the Introduction. The populations, the workers and "
             "the outputs are written for the lesson so that the factor Smith names can be "
             "seen to move, and nothing in them is a measurement of any real people."),
        ],
        "standard": (
            "Finish when you can compute a nation's supply per head and say which factor "
            "moved it.",
            "Given a population, the number at useful work and the output of each, compute "
            "the produce and the produce per head, and state which of Smith's two "
            "circumstances accounts for a difference between two nations."
        ),
        "note": (
            "The lab computes what Smith's opening sentence implies for the figures it is "
            "given. It cannot say how many people in a real country are at useful work, "
            "because that depends on what counts as useful, and Book II, Chapter 3 is a "
            "dispute about exactly that. It cannot measure the output of a worker either, "
            "since the units are the lesson's, and the picture of the hunters is a "
            "conjecture that later observers have challenged. What the arithmetic does "
            "show is the shape of the claim: skill is a multiplier of any size and the "
            "share at work is a fraction."
        ),
    },
    # ---------------------------------------------------------------- 02
    # PSU text l. 193-248 (the pin-maker), l. 255-306 (separation of trades and
    # agriculture), l. 307-411 (three causes, nails, the boy and the valve),
    # l. 412-470 (the woollen coat).
    {
        "slug": "the-pin-factory",
        "title": "The Pin Factory",
        "module": "Book I, Chapter 1 · Of the Division of Labour",
        "one_line": "Ten men making pins, each at a part of the work, make some four thousand eight hundred a day apiece, where one alone might make twenty or none.",
        "summary": (
            "Smith explains the first circumstance, skill, by looking at a trade so small "
            "that all of it can be seen at once. Work through his pin-maker's figures: "
            "ten men, eighteen operations, upwards of forty-eight thousand pins a day "
            "between them, and the multiple by which dividing the work raised the output of "
            "each man. Then read his three causes, and the coat that took a multitude to "
            "make."
        ),
        "key": [
            "each man's share = team output / workers",
            "multiple = divided output / output alone",
            "Smith: 4800 each, against 20 or fewer alone",
            "multiple of at least 240, perhaps 4800",
            "three causes: skill, time saved, machines",
        ],
        "key_label": "The pin factory in five lines",
        "concepts_intro": (
            "Chapter 1 does one thing at length: it shows the division of labour in a "
            "small trade, then asks why it makes so large a difference, then widens the "
            "view to a whole society."
        ),
        "concepts": [
            ("The division of the work",
             "Smith counts about eighteen distinct operations in making a pin, from "
             "drawing the wire to putting the pins into paper. In the small factory he "
             "describes, ten men shared them, so that some did two or three of the "
             "operations and no one did all eighteen."),
            ("The multiple",
             "Ten men together made upwards of 48,000 pins a day, so each might be "
             "considered as making 4,800. Working apart and untrained, Smith says each "
             "could certainly not make twenty and perhaps not one. The multiple is what "
             "the division of the work adds."),
            ("Three causes",
             "Smith gives three reasons: the increase of dexterity in each workman, the "
             "saving of the time commonly lost in passing from one kind of work to "
             "another, and the invention of machines that abridge labour. He ends the "
             "chapter with a woollen coat to show how many hands even the plainest thing "
             "takes."),
        ],
        "read_title": "A trifling manufacture first, then the three causes",
        "read_intro": (
            "Smith says he chooses a trifling trade because the division in a great one is "
            "spread over too many workshops to see. Read the pin passage for its figures, "
            "and then the three causes, which are the explanation."
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 1.</strong> Smith's untrained pin-maker, "
                  "without the trade or its machinery, &ldquo;could scarce, perhaps, with "
                  "his utmost industry, make one pin in a day, and certainly could not make "
                  "twenty.&rdquo; Then he describes the trade as it is carried on: "
                  "&ldquo;One man draws out the wire; another straights it; a third cuts "
                  "it; a fourth points it; a fifth grinds it at the top for receiving the "
                  "head; to make the head requires two or three distinct operations; to put "
                  "it on is a peculiar business; to whiten the pins is another; it is even a "
                  "trade by itself to put them into the paper.&rdquo;"),
            ("p", "Then come the figures. He has &ldquo;seen a small manufactory of this "
                  "kind, where ten men only were employed, and where some of them "
                  "consequently performed two or three distinct operations&rdquo;. They were "
                  "poor and poorly equipped, yet &ldquo;they could, when they exerted "
                  "themselves, make among them about twelve pounds of pins in a day. There "
                  "are in a pound upwards of four thousand pins of a middling "
                  "size.&rdquo; Twelve times four thousand is `48000`, and Smith writes "
                  "&ldquo;upwards of forty-eight thousand&rdquo;, so that is a floor, not a "
                  "count. Ten men share it, so each might be &ldquo;considered as making "
                  "four thousand eight hundred pins in a day&rdquo;."),
            ("def", ("The multiple",
                     "How many times as much each man makes when the work is divided as he "
                     "could make alone: the divided output per worker, divided by the output "
                     "a worker would have working alone. Smith gives the bounds himself: working "
                     "apart, his men &ldquo;certainly could not each of them have made twenty, perhaps not one pin in a day&rdquo;, so the multiple "
                     "has a smallest value, 240, and may be as large as 4,800 or "
                     "more.")),
            ("p", "Put them in the lab. The preset <code>smith</code>, labelled "
                  "Smith's pin factory, has ten workers, eighteen operations, 48,000 pins a "
                  "day together and 20 pins a day alone. Each man makes 4,800 in the team. "
                  "If all ten worked alone at 20, the lot would make 200, so the division "
                  "adds 47,800 pins a day and the multiple is 240. That is Smith's "
                  "&ldquo;two hundred and fortieth part&rdquo;. Change the 20 to 1 in "
                  "<code>smith-one</code> and the multiple is 4,800, which is his "
                  "&ldquo;four thousand eight hundredth&rdquo;. And in "
                  "<code>nobody-alone</code> the output alone is 0, and the lab prints no "
                  "finite multiple, because you cannot divide by nothing; the ten men have "
                  "gone from no pins to 48,000, and no multiple describes that."),
            ("p", "Spread the eighteen operations over ten men and each does `18/10`, "
                  "which is one and four-fifths, operations on average. This is why "
                  "Smith says some of them &ldquo;performed two or three&rdquo;: eighteen "
                  "jobs cannot be shared evenly among ten, and the factory's division is "
                  "coarser than the eighteen operations suggest."),
            ("p", "Smith then says why. &ldquo;This great increase in the quantity of work, "
                  "which, in consequence of the division of labour, the same number of "
                  "people are capable of performing, is owing to three different "
                  "circumstances; first, to the increase of dexterity in every particular "
                  "workman; secondly, to the saving of the time which is commonly lost in "
                  "passing from one species of work to another; and, lastly, to the "
                  "invention of a great number of machines which facilitate and abridge "
                  "labour.&rdquo;"),
            ("p", "He illustrates the first with nails. A common smith will scarce, he "
                  "is assured, &ldquo;be able to make above two or three hundred nails in a "
                  "day&rdquo;, and bad ones; a smith used to nails, but not a nailer by "
                  "trade, seldom more than eight hundred or a thousand; and he has "
                  "&ldquo;seen several boys, under twenty years of age, who had never "
                  "exercised any other trade but that of making nails&rdquo;, making "
                  "&ldquo;upwards of two thousand three hundred&rdquo; each. Against the "
                  "common smith's three hundred that is more than seven times as many. For "
                  "the second cause he describes the country weaver going from his loom to "
                  "his field, and the man who &ldquo;saunters a little in turning his "
                  "hand from one sort of employment to another&rdquo;: his mind, as they "
                  "say, does not go to it. For the third, he tells of a boy employed to "
                  "open and shut a valve on an early steam engine, who tied a string from "
                  "the handle of the valve to another part of the machine so that he could "
                  "go and play. Smith calls it one of the greatest improvements made on the "
                  "engine, the discovery of a boy who wanted to save his own labour."),
            ("p", "The chapter then widens. A woollen coat on a day-labourer's back is, he "
                  "says, the produce of the joint labour of a great multitude: the shepherd, "
                  "the wool-sorter, the carder, the dyer, the spinner, the weaver, the "
                  "fuller, and behind them the merchants, the carriers, the shipbuilders "
                  "who bring the dyers' drugs from far away, and the miners and smiths who "
                  "make the shepherd's shears. The number of people whose industry has "
                  "helped to supply a common artificer, he says, &ldquo;exceeds all "
                  "computation&rdquo;. And he closes with a comparison that has lasted: the "
                  "accommodation of a European prince does not always so much exceed that "
                  "of an industrious and frugal peasant &ldquo;as the accommodation of the "
                  "latter exceeds that of many an African king&rdquo;. The comparison "
                  "rests on what travellers reported, and it is as much a rhetorical turn "
                  "as a measurement."),
            ("p", "Three things are worth saying about the example. First, Smith says he "
                  "saw this factory, and the figures are his; scholars have also noticed "
                  "that the article on pins in Diderot's <em>Encyclopédie</em>, printed "
                  "some twenty years earlier, counts the same eighteen operations, so the "
                  "example may owe something to a book as well as to a visit. Second, he "
                  "limits the claim: agriculture, he says, does not admit of so many "
                  "subdivisions, because the ploughman, the sower and the reaper are often "
                  "the same, the seasons bringing round their tasks one at a time, and that "
                  "is why the rich country's advantage is greater in manufactures than in "
                  "corn. Third, he says nothing yet about what the division does to the "
                  "man. He returns to that in Book V, where the worker whose whole life is "
                  "spent on a few simple operations loses the habit of exerting his "
                  "understanding, and the lesson on the instruction of people of all ages "
                  "reads that passage. Marx's reading of the pin factory, and of what "
                  "division in a workshop does to the labourer, is in the Capital lesson "
                  "&lsquo;Division of Labour and Manufacture&rsquo;, and it is not "
                  "repeated here."),
            ("p", "So the pin factory gives you a multiple and three causes. Smith has not "
                  "yet said why people divide their work at all, since no one planned it, "
                  "and the next lesson asks what makes them do it."),
        ],
        "lab": ("wonkit", {
            "mode": "division",
            "view": "pins",
            "qty_unit": "pins",
            "preset": "smith",
            "presets": [
                {"id": "smith",
                 "label": "Smith's pin factory: ten men, eighteen operations, 48,000 a day, at most 20 alone",
                 "workers": 10, "operations": 18, "together": 48000, "alone": 20,
                 "expect": {
                          "wdvPerWorker": "4,800 pins a day",
                          "wdvAloneTeam": "200 pins a day",
                          "wdvMultiple": "240×",
                          "wdvExtra": "+47,800 pins a day",
                          "wdvOpsEach": "9/5 = 1.80 operations a worker",
                         }},
                {"id": "smith-one",
                 "label": "Smith's pin factory, if alone one pin a day",
                 "workers": 10, "operations": 18, "together": 48000, "alone": 1,
                 "expect": {
                          "wdvPerWorker": "4,800 pins a day",
                          "wdvAloneTeam": "10 pins a day",
                          "wdvMultiple": "4,800×",
                          "wdvExtra": "+47,990 pins a day",
                          "wdvOpsEach": "9/5 = 1.80 operations a worker",
                         }},
                {"id": "nobody-alone",
                 "label": "Smith's pin factory, if alone no pin at all (the lab's reading of his perhaps not one)",
                 "workers": 10, "operations": 18, "together": 48000, "alone": 0,
                 "expect": {
                          "wdvPerWorker": "4,800 pins a day",
                          "wdvAloneTeam": "0 pins a day",
                          "wdvMultiple": "no finite multiple: alone, a worker makes none",
                          "wdvExtra": "+48,000 pins a day",
                          "wdvOpsEach": "9/5 = 1.80 operations a worker",
                         }},
            ],
            "panel_title": "What the division of the work added",
            "panel_intro": (
                "The number of workers and operations, the team's output a day, and what one "
                "of them would make alone go in. The lab divides, multiplies and compares. "
                "Smith's own presets all use his 48,000; change only the figure for working "
                "alone."
            ),
        }),
        "steps_title": "Computing the multiple",
        "steps_intro": "Four steps; the order is the order Smith gives the figures in.",
        "steps": [
            ("Find the team's output",
             "Multiply the pounds of pins by the pins in a pound: 12 pounds at upwards of "
             "4,000 a pound. If the figure is stated as &ldquo;upwards of&rdquo;, it is a "
             "floor."),
            ("Divide among the workers",
             "Divide the team's output by the number of workers. This is the output of "
             "each when the work is divided, 4,800 a day for Smith's ten."),
            ("State what one would make alone",
             "Take Smith's bounds: at most 20, perhaps as few as 1. Each gives a "
             "different multiple, and 0 gives none."),
            ("Divide the two",
             "The multiple is the divided output of one worker over his output alone. Say "
             "what it covers, and what it does not: three causes, one small factory, and "
             "a floor."),
        ],
        "worked": {
            "title": "From twelve pounds of pins to a multiple of 240",
            "intro": [
                "Take the first preset. Ten men make twelve pounds of pins a day, with upwards "
                "of four thousand pins to the pound. At most, working alone, each could make "
                "twenty. You want the output of each in the team and the multiple.",
            ],
            "lines": [
                "team:  12 · 4000 = 48000 pins a day",
                "each in the team:  48000 / 10 = 4800",
                "ten working alone, at most:  10 · 20 = 200",
                "multiple:  4800 / 20 = 240",
                "if alone one pin:  4800 / 1 = 4800",
            ],
            "after": [
                "On Smith's own figures the division of the work made each man at least 240 "
                "times as productive as the best he could do alone, and perhaps 4,800 times "
                "as productive, and that is before the question of whether anyone could have "
                "made even a single pin without the trade and the tools it created.",
            ],
        },
        "quiz_title": "Pins, men and multiples",
        "quiz": [
            {"q": "Smith's ten men make about twelve pounds of pins a day, with upwards of "
                  "four thousand pins in a pound. What is each man's share of the day's output?",
             "a": ["Upwards of 480", "Upwards of 4,800", "Upwards of 48,000", "Exactly 4,000"],
             "c": 1,
             "why": "Twelve pounds at four thousand a pound is 48,000 pins, and ten men "
                    "share it: 4,800 each. The figure 48,000 is the whole team's output, "
                    "480 is a tenth of the team's per man, and four thousand is the number "
                    "of pins in a pound."},
            {"q": "Which of these is one of Smith's three causes of the increase in the "
                  "quantity of work?",
             "a": ["The saving of the time lost in passing from one sort of work to another",
                   "A longer working day",
                   "Lower wages for the workmen",
                   "A better grade of wire"],
             "c": 0,
             "why": "His three are the increase of dexterity, the saving of the time lost "
                    "in passing from one species of work to another, and the invention of "
                    "machines. Nothing in the passage says the workmen worked longer, were "
                    "paid less or had better wire; they were, he says, poor and poorly "
                    "equipped."},
            {"q": "A workman alone could certainly not make twenty pins a day, and in the "
                  "team of ten he makes 4,800. What is the least multiple by which the "
                  "division of the work raised his output?",
             "a": ["24", "200", "240", "4,800"],
             "c": 2,
             "why": "At most 20 alone against 4,800 in the team is `4800/20 = 240`, which "
                    "is Smith's &ldquo;two hundred and fortieth part&rdquo;. Four thousand "
                    "eight hundred would be the multiple if he could make only one; 200 is "
                    "what ten men could make alone together, and 24 is a slip of a factor "
                    "of ten."},
            {"q": "Why does Smith say the improvement of labour in agriculture does not keep "
                  "pace with its improvement in manufactures?",
             "a": ["Farmers are less skilful than manufacturers",
                   "Land cannot be improved by labour and expense",
                   "The tasks of the farm come round with the seasons, so one man cannot be "
                   "constantly employed in any one of them",
                   "Machines cannot be used in the fields"],
             "c": 2,
             "why": "Smith says the occasions for the different sorts of labour return with "
                    "the different seasons, so it is impossible that one man should be "
                    "constantly employed in any one of them. He says the land of a rich "
                    "country is better cultivated, so improvement is possible, and he does "
                    "not say farmers are less skilful or that machines are impossible."},
        ],
        "mistakes": [
            ("Reading 48,000 as a measured day's output",
             "Smith writes &ldquo;upwards of forty-eight thousand&rdquo; from twelve pounds "
             "&ldquo;when they exerted themselves&rdquo; and &ldquo;upwards of four "
             "thousand&rdquo; pins to the pound. It is a floor taken from one small factory "
             "on a good day, and the lab uses it as stated."),
            ("Using the multiple as the gain of every trade",
             "Smith says the effects are similar in every art and manufacture, but that "
             "in many the labour can &ldquo;neither be so much subdivided, nor reduced to "
             "so great a simplicity of operation&rdquo;. The pin is the most favourable "
             "case he could choose, and he chose it for that reason."),
            ("Taking the three causes for the whole story",
             "They explain why output per worker rises, and nothing here says what the "
             "worker gives up for it. Smith raises that cost himself in Book V, and "
             "Capital makes it central. The chapter is an account of productive power and "
             "stops there."),
        ],
        "standard": (
            "Finish when you can compute the multiple from the output of the team and the "
            "output alone.",
            "Given the number of workers, the team's daily output and a bound on what one "
            "could make alone, compute each worker's share and the multiple, and name "
            "Smith's three causes."
        ),
        "note": (
            "The lab divides Smith's total by his ten and compares the quotient with the "
            "bound he gives. It cannot say whether the factory was typical, whether a day's "
            "output was measured or estimated, or how much of the multiple is dexterity, "
            "how much saved time and how much machinery, which Smith does not apportion. "
            "The figure 20 is an upper bound he states, and the figure 1 is his "
            "&ldquo;perhaps&rdquo;."
        ),
    },
    # ---------------------------------------------------------------- 03
    # PSU text l. 476-480 (the propensity), l. 485-514 (no dog exchanges bones),
    # l. 515-533 (butcher, brewer, baker), l. 534-556 (bows and arrows),
    # l. 557-603 (philosopher and porter, mastiff and greyhound).
    {
        "slug": "the-propensity-to-truck-and-barter",
        "title": "The Propensity to Truck, Barter and Exchange",
        "module": "Book I, Chapter 2 · Of the Principle Which Gives Occasion to the Division of Labour",
        "one_line": "People divide their work because they can exchange its surplus, and what they will exchange it for is the other's interest.",
        "summary": (
            "Chapter 2 asks where the division of labour came from, and answers that no one "
            "planned it: it is the slow consequence of a propensity to exchange. Compute "
            "what two producers have when each makes everything for himself and when each "
            "keeps to the trade he does at the lower cost, and see why Smith thinks the "
            "difference between a philosopher and a porter is more the effect of the "
            "division than its cause."
        ),
        "key": [
            "self-sufficient: q = hours / (a + b)",
            "specialised: hours / hours per unit",
            "gain = specialised total − self-sufficient",
            "dinner comes from interest, not kindness",
            "talents: more effect than cause",
        ],
        "key_label": "The principle in five lines",
        "concepts_intro": (
            "The chapter is short and does three jobs: it says what the division of labour "
            "rests on, it says why we can rely on it, and it says what it does to the "
            "differences between people."
        ),
        "concepts": [
            ("A propensity, not a plan",
             "The division of labour is &ldquo;not originally the effect of any human "
             "wisdom&rdquo; that foresaw the general opulence it brings. It is the "
             "consequence of a propensity in human nature, to truck, barter and exchange "
             "one thing for another, which Smith says is found in no other animal."),
            ("Self-love, not benevolence",
             "A man has constant need of the help of great multitudes and cannot get it "
             "from their benevolence only. He will prevail if he can show them that it is "
             "for their own advantage to do what he asks, and this is the meaning of every "
             "bargain."),
            ("Talents as an effect",
             "The difference between the most dissimilar characters, he says, seems to arise "
             "not so much from nature as from habit, custom and education. The division of "
             "labour makes the difference of talents, and exchange makes it useful by "
             "bringing every talent into a common stock."),
        ],
        "read_title": "The propensity, the butcher and the bow-maker",
        "read_intro": (
            "Chapter 2 is the place the book is most often quoted from, and the passage "
            "about the butcher, brewer and baker is usually quoted without what comes "
            "before and after it. Read all of it."
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 2.</strong> Smith starts by denying that the "
                  "division of labour came from foresight. It is &ldquo;the necessary, "
                  "though very slow and gradual, consequence of a certain propensity in "
                  "human nature, which has in view no such extensive utility; the "
                  "propensity to truck, barter, and exchange one thing for another.&rdquo; "
                  "Whether this propensity is an original principle or the consequence of "
                  "reason and speech, he says, it does not belong to the present subject "
                  "to inquire, and he moves on to what is plain: it is found in men and in "
                  "no other animal. &ldquo;Nobody ever saw a dog make a fair and deliberate "
                  "exchange of one bone for another with another dog.&rdquo;"),
            ("p", "Then the reason it matters. An animal grown up is independent, but man "
                  "&ldquo;has almost constant occasion for the help of his brethren, and it "
                  "is in vain for him to expect it from their benevolence only.&rdquo; He "
                  "points out how little of a lifetime there is to spare for it: &ldquo;In "
                  "civilized society he stands at all times in need of the co-operation and "
                  "assistance of great multitudes, while his whole life is scarce sufficient "
                  "to gain the friendship of a few persons.&rdquo; So he must interest their "
                  "self-love, and every offer of a bargain says the same thing: "
                  "&ldquo;Give me that which I want, and you shall have this which you "
                  "want&rdquo;."),
            ("p", "And then the sentence that everyone knows: &ldquo;It is not from the "
                  "benevolence of the butcher the brewer, or the baker that we expect our "
                  "dinner, but from their regard to their own interest.&rdquo; Read it with "
                  "the sentence before it and the claim is narrower than the slogan. It is "
                  "about the multitudes of strangers a person depends on, not about "
                  "friends or family, and it does not say benevolence is absent from life, "
                  "only that it cannot be relied on to supply a dinner. Even the beggar, "
                  "Smith adds, does not depend on charity entirely: what he is given he "
                  "turns into what he needs by barter and purchase. Later readers have "
                  "asked whether the author of this passage can be the author of his "
                  "earlier <em>Theory of Moral Sentiments</em>, which opens with how we feel "
                  "for one another. The chapter does not ask that question, and it is "
                  "no part of this lesson's arithmetic."),
            ("p", "From the propensity Smith derives the division of labour, with an example "
                  "from a tribe of hunters or shepherds. One man makes bows and arrows "
                  "more readily than the rest. He exchanges them for cattle or venison, and "
                  "&ldquo;he finds at last that he can, in this manner, get more cattle and "
                  "venison, than if he himself went to the field to catch them.&rdquo; So "
                  "making bows and arrows becomes his chief business and he becomes a sort of "
                  "armourer. Another becomes a house-carpenter, a third a smith, a fourth a "
                  "tanner."),
            ("p", "That is a sum, and the lab computes it with figures written for the "
                  "lesson, because Smith gives none. Two producers each have 80 hours. The "
                  "armourer takes 2 hours to make a bow and 8 to bring in a unit of "
                  "venison; the hunter takes 8 hours for a bow and 2 for the venison. If "
                  "each makes the same quantity of both for himself, each gets "
                  "`80/(2+8) = 8` of each, 16 bows and 16 units of venison between them. If "
                  "each keeps to what he does at the lower cost, the armourer makes 40 bows "
                  "and the hunter 40 units of venison, and the gain is 24 of each. The "
                  "preset is <code>armourer-and-hunter</code>. The lab's baseline, the equal "
                  "quantities of both, is a choice made for the sum; Smith says only that "
                  "the specialist gets more than he would catching for himself."),
            ("p", "The second preset, <code>unequal-hours</code>, gives the armourer 80 "
                  "hours at 2 and 8, and the hunter 70 hours at 5 and 2. Alone, they get 8 "
                  "and 10 of each, 18 between them; specialised, 40 bows and 35 units of "
                  "venison, a gain of 22 bows and 17 of venison. And in "
                  "<code>slight-difference</code>, where the armourer takes 4 and 5 hours "
                  "and the hunter 5 and 4, each with 90 hours, the gain is only 2.5 of each "
                  "(20 become 22.5). That is the point of Smith's next paragraph: the "
                  "smaller the natural difference between people, the smaller the gain "
                  "from sorting them, so a division of labour that grows large must have "
                  "grown its own differences."),
            ("p", "He says exactly that. &ldquo;The difference between the most dissimilar "
                  "characters, between a philosopher and a common street porter, for "
                  "example, seems to arise not so much from nature, as from habit, custom, "
                  "and education.&rdquo; At six or eight years old they were, perhaps, "
                  "very much alike; then they are put to different employments, the "
                  "difference of talents is noticed, and it widens by degrees. The very "
                  "different genius of men of different professions &ldquo;is not upon "
                  "many occasions so much the cause, as the effect of the division of "
                  "labour&rdquo;. He compares it with the breeds of dogs, which differ more "
                  "by nature than philosopher and porter, yet cannot help one another: the "
                  "mastiff's strength is not supported by the greyhound's swiftness. "
                  "Among men, by contrast, the different talents &ldquo;being brought, as "
                  "it were, into a common stock&rdquo;, every man may buy what part of "
                  "the produce of the others' talents he needs."),
            ("def", ("The rule the lab uses",
                     "Each producer makes the good in which his cost relative to the "
                     "other's is lower: hours for a bow, divided by hours for a unit of "
                     "venison. This is the rule David Ricardo stated in 1817, in chapter 7 "
                     "of his <em>Principles</em> (Robert Torrens had a version two years "
                     "earlier), and it is the lab's rule, not Smith's. It agrees with "
                     "Smith's case when each producer is better at one thing. Where one is "
                     "better at both, it is Ricardo's rule that still finds a gain, and "
                     "Smith's chapter does not discuss that case.")),
            ("p", "What the chapter does not say is also worth a sentence. Smith assumes "
                  "a person's surplus will find a taker: he speaks of the &ldquo;certainty "
                  "of being able to exchange all that surplus part of the produce of his "
                  "own labour&rdquo;. If it will not, the specialist starves, and that is "
                  "the subject of the very next chapter, which says the division of "
                  "labour is limited by the extent of the market."),
        ],
        "lab": ("wonkit", {
            "mode": "division",
            "view": "exchange",
            "goods": "bows venison",
            "preset": "armourer-and-hunter",
            "presets": [
                {"id": "armourer-and-hunter",
                 "label": "An armourer and a hunter, 80 hours each, written for this lesson",
                 "producers": "armourer, 80, 2, 8; hunter, 80, 8, 2",
                 "expect": {
                          "wdvSelfEach": "armourer 8 of each; hunter 8 of each",
                          "wdvSelfTotal": "bows 16; venison 16",
                          "wdvWho": "armourer makes bows (relative cost 1/4 = 0.25 against 4); hunter makes venison",
                          "wdvSpecTotal": "bows 40; venison 40",
                          "wdvGain": "bows +24; venison +24",
                          "wdvCase": "each is better at one good: armourer at bows, hunter at venison (Smith’s case)",
                         }},
                {"id": "unequal-hours",
                 "label": "The hunter has 70 hours and slower bows, written for this lesson",
                 "producers": "armourer, 80, 2, 8; hunter, 70, 5, 2",
                 "expect": {
                          "wdvSelfEach": "armourer 8 of each; hunter 10 of each",
                          "wdvSelfTotal": "bows 18; venison 18",
                          "wdvWho": "armourer makes bows (relative cost 1/4 = 0.25 against 5/2 = 2.50); hunter makes venison",
                          "wdvSpecTotal": "bows 40; venison 35",
                          "wdvGain": "bows +22; venison +17",
                          "wdvCase": "each is better at one good: armourer at bows, hunter at venison (Smith’s case)",
                         }},
                {"id": "slight-difference",
                 "label": "Little difference between them, written for this lesson",
                 "producers": "armourer, 90, 4, 5; hunter, 90, 5, 4",
                 "expect": {
                          "wdvSelfEach": "armourer 10 of each; hunter 10 of each",
                          "wdvSelfTotal": "bows 20; venison 20",
                          "wdvWho": "armourer makes bows (relative cost 4/5 = 0.80 against 5/4 = 1.25); hunter makes venison",
                          "wdvSpecTotal": "bows 45/2 = 22.50; venison 45/2 = 22.50",
                          "wdvGain": "bows +5/2 = 2.50; venison +5/2 = 2.50",
                          "wdvCase": "each is better at one good: armourer at bows, hunter at venison (Smith’s case)",
                         }},
            ],
            "panel_title": "What keeping to one trade gains",
            "panel_intro": (
                "Each producer's hours and the hours a bow and a unit of venison cost him go "
                "in. The lab compares making equal quantities of both with making only the "
                "good he does at the lower relative cost, and says who makes what."
            ),
        }),
        "steps_title": "Computing the gain from a trade",
        "steps_intro": "Four steps, for two producers and two goods.",
        "steps": [
            ("Make each do it all",
             "A producer who makes equal quantities of both goods spends hours a unit for "
             "the first and b a unit for the second, so he makes `hours/(a+b)` of each."),
            ("Total each good",
             "Add the two producers' quantities of each good. This is the baseline the "
             "lab chooses, not one Smith states."),
            ("Let each keep to one good",
             "Give each producer the good in which his hours per unit, compared with the "
             "other's, are lower, and let him use all his hours on it: hours divided by "
             "hours per unit."),
            ("Subtract",
             "The gain in each good is the specialised total less the baseline. If a "
             "difference between producers is small, the gain is small."),
        ],
        "worked": {
            "title": "Sixteen bows and sixteen units of venison become forty of each",
            "intro": [
                "Take the first preset. The armourer and the hunter have 80 hours each. The "
                "armourer takes 2 hours a bow and 8 a unit of venison, and the hunter 8 and 2.",
            ],
            "lines": [
                "each alone:  80 / (2 + 8) = 8 of each",
                "both together, alone:  2 · 8 = 16 of each",
                "armourer keeps to bows:  80 / 2 = 40",
                "hunter keeps to venison:  80 / 2 = 40",
                "gain:  40 − 16 = 24 of each",
            ],
            "after": [
                "Each has the same hours, and between them they have 24 more bows and 24 "
                "more units of venison. Make the two nearly equal at both jobs, as in the "
                "third preset, and 20 of each becomes only 22.5 of each: the gain depends on "
                "a difference, and Smith's argument is that the difference follows the "
                "division, not the other way.",
            ],
        },
        "quiz_title": "Interest and exchange",
        "quiz": [
            {"q": "On what, according to Smith, do we rely to get our dinner from the butcher, "
                  "the brewer and the baker?",
             "a": ["Their benevolence",
                   "The law, which obliges them to supply us",
                   "Their friendship, once we have earned it",
                   "Their regard to their own interest"],
             "c": 3,
             "why": "Smith says we address ourselves &ldquo;not to their humanity, but to "
                    "their self-love&rdquo;. He says benevolence cannot be relied on from "
                    "great multitudes of strangers, and that a lifetime is scarce "
                    "sufficient to gain the friendship of a few. The law plays no part in "
                    "the passage."},
            {"q": "Two producers each have 60 hours. A takes 1 hour a bow and 5 a unit of "
                  "venison; B takes 5 hours a bow and 1 a unit of venison. How many bows "
                  "and units of venison do they have between them if each makes equal "
                  "quantities of both for himself?",
             "a": ["10 of each", "20 of each", "60 of each", "120 of each"],
             "c": 1,
             "why": "Each makes `60/(1+5) = 10` of each, so 20 of each between them. "
                    "Sixty is what one of them would make of his own good by keeping to it, "
                    "and 120 is the two together doing so. Ten is only one producer's share."},
            {"q": "What does Smith say about the difference between a philosopher and a "
                  "common street porter?",
             "a": ["It is the cause of their different employments",
                   "It is far greater than between a mastiff and a greyhound",
                   "It seems to arise more from habit, custom and education than from nature",
                   "It cannot be explained"],
             "c": 2,
             "why": "He says the difference &ldquo;seems to arise not so much from nature, "
                    "as from habit, custom, and education&rdquo;, and is more the effect "
                    "of the division of labour than its cause. He says that by nature the "
                    "philosopher is not half so different from the porter as the mastiff is "
                    "from the greyhound, so the second answer reverses him."},
            {"q": "Who later stated the rule that producers should keep to the good in which "
                  "their relative cost is lower, even when one is better at both?",
             "a": ["Adam Smith, in the same chapter",
                   "David Ricardo, in 1817",
                   "Karl Marx, in Capital",
                   "Bernard Mandeville, in the Fable of the Bees"],
             "c": 1,
             "why": "Ricardo set it out in his <em>Principles</em> of 1817 (with an earlier "
                    "version by Robert Torrens). Smith's chapter, 41 years before, "
                    "concerns the case in which each producer is better at one thing, "
                    "and Marx and Mandeville did not state this rule."},
        ],
        "mistakes": [
            ("Reading the butcher passage as praise of selfishness",
             "Smith says what we may expect of strangers in the mass: that their own "
             "interest will serve us if we show them it does. He does not say people have "
             "no other motives, and his book on the moral sentiments says a good deal "
             "about them. The passage gives a reason why exchange works, and it is silent "
             "on what a good life is."),
            ("Reading the philosopher and porter as proof that people start alike",
             "Smith says the difference is &ldquo;much less than we are aware of&rdquo; and "
             "that at six or eight years old the two were &ldquo;perhaps&rdquo; very much "
             "alike. He is making a claim about degree, and he qualifies it. The lab's "
             "<code>slight-difference</code> preset is the claim in arithmetic: a small "
             "difference gives a small gain."),
            ("Taking the lab's gain as Smith's calculation",
             "Smith gives no hours and no quantities. The producers, the hours and the "
             "baseline of equal quantities are written for the lesson, and the rule that "
             "decides who makes what is Ricardo's, not Smith's."),
        ],
        "standard": (
            "Finish when you can compute what two producers gain by specialising and say "
            "what the chapter does and does not claim.",
            "Given each producer's hours and his hours per unit of two goods, compute the "
            "two goods' totals when each is self-sufficient and when each keeps to the "
            "good of lower relative cost, and state the gain."
        ),
        "note": (
            "The lab shows that specialising by relative cost yields more of both goods "
            "than making them in equal quantities, for the hours it is given. It cannot "
            "show that people exchange because they are disposed to, which is Smith's "
            "thesis and is a claim about human nature, or that a market will take the "
            "surplus. Smith's examples are a tribe of hunters and a village; the "
            "chapter's hours and rates are not his, and the choice of equal quantities "
            "as the baseline flatters the gain."
        ),
    },
    # ---------------------------------------------------------------- 04
    # PSU text l. 606-611 (the thesis), l. 612-637 (the porter, the Highlands,
    # the nailer), l. 637-675 (the wagon and the ship), l. 676-686 (coasts and
    # rivers), l. 687-753 (Egypt, Bengal, China, Africa, Tartary, the Danube).
    {
        "slug": "the-extent-of-the-market",
        "title": "The Extent of the Market",
        "module": "Book I, Chapter 3 · That the Division of Labour Is Limited by the Extent of the Market",
        "one_line": "A trade can exist only where there is enough demand to keep one man at it, and water carriage widens the market more than any road.",
        "summary": (
            "Chapter 3 gives the division of labour its limit. Take Smith's nailer, who "
            "could make three hundred thousand nails a year but could sell a thousand in "
            "the Highlands, and compute how many specialists a place's demand can keep. "
            "Then weigh the wagon against the ship, in Smith's own figures, and see why he "
            "thought industry began on the coasts."
        ),
        "key": [
            "specialists = whole units of demand/output",
            "share of a year = demand / one's output",
            "a trade lives where demand fills a year",
            "ship: 200 tons for 8 men at most",
            "wagon: about 4 tons for 2 men",
        ],
        "key_label": "The limit in five lines",
        "concepts_intro": (
            "The chapter is built on a single sentence, and then it spends most of its "
            "length on geography to show the sentence at work."
        ),
        "concepts": [
            ("The limit",
             "The extent of the division of labour must be limited by the extent of the "
             "power of exchanging, or in other words by the extent of the market. When the "
             "market is very small, no one has encouragement to give himself to one "
             "employment, for want of the power to exchange his surplus."),
            ("How many a place can keep",
             "A trade needs enough demand to keep a man at it all year. Where it does not, "
             "his work is added to someone else's: the country carpenter is also joiner, "
             "cabinet-maker and cart-maker, the Highland farmer his own butcher, baker "
             "and brewer."),
            ("Water carriage",
             "A ship carrying two hundred tons with six or eight men does what fifty "
             "wagons, a hundred men and four hundred horses do by land. So the first "
             "improvements of art and industry begin on the sea-coast and along "
             "navigable rivers, and reach the inland parts much later."),
        ],
        "read_title": "A limit stated, then shown on the map",
        "read_intro": (
            "Read the first paragraph and the Highland nailer for the argument. Read the "
            "wagon and the ship for its figures. The tour of the world that follows is the "
            "same argument on a larger map."
        ),
        "body": [
            ("p", "<strong>Book I, Chapter 3.</strong> The chapter's first sentence is its "
                  "thesis. The power of exchanging gives occasion to the division of "
                  "labour, so the extent of this division &ldquo;must always be limited by "
                  "the extent of that power, or, in other words, by the extent of the "
                  "market.&rdquo; Smith opens with the thing the previous chapter left "
                  "open: if exchange makes the division of labour, then the division can "
                  "go only as far as exchange can."),
            ("p", "Then the reason. When the market is very small, &ldquo;no person can have "
                  "any encouragement to dedicate himself entirely to one employment, for "
                  "want of the power to exchange all that surplus part of the produce of "
                  "his own labour, which is over and above his own consumption, for such "
                  "parts of the produce of other men's labour as he has occasion "
                  "for.&rdquo; Some trades, even of the lowest kind, can be carried on "
                  "nowhere but in a great town. A porter can find employment and "
                  "subsistence in no other place; a village is by much too narrow a sphere "
                  "for him. The scattered Highland houses have the opposite case: "
                  "&ldquo;every farmer must be butcher, baker, and brewer, for his own "
                  "family&rdquo;."),
            ("p", "Then Smith gives the figure that makes it arithmetic. A nailer at the "
                  "rate of a thousand nails a day, and three hundred working days in a year, "
                  "will make three hundred thousand nails. But in a remote Highland "
                  "district, &ldquo;it would be impossible to dispose of one thousand, that "
                  "is, of one day's work in the year.&rdquo; The lab's first preset, "
                  "<code>highlands</code>, is exactly this: a demand of 1,000 nails a year "
                  "and a nailer who makes 300,000. The place keeps no whole nailer, "
                  "`1000/300000 = 1/300` of one man's year, and a nailer who tried to live "
                  "there would be idle on all but a day in three hundred."),
            ("def", ("Specialists a demand keeps",
                     "The number of whole men a place's yearly demand for a good can keep "
                     "at it, taking each man's yearly output as given: the demand divided "
                     "by one man's output, rounded down. A place that keeps none can still "
                     "have the trade done, by a man who does it in a few days of the year "
                     "alongside other work.")),
            ("p", "Now let the demand grow. In the preset <code>ladder</code> the "
                  "Highlands keep 1,000; a village, with figures written for the lesson, "
                  "30,000; a market town 150,000; a port 900,000; a city 3,000,000. With a "
                  "nailer making 300,000 nails a year, the village takes a tenth of a "
                  "nailer, the market town a half, the port three nailers, the city ten. "
                  "Only in the port does the trade first stand on its own. Smith's "
                  "remark that a country smith's trade is &ldquo;still more various&rdquo; "
                  "than the carpenter's is what the first four places look like in "
                  "practice: the man who cannot live by nails alone makes everything "
                  "iron."),
            ("p", "The third preset, <code>by-water</code>, written for the lesson, is the "
                  "same sum with a river. An inland village that can reach only its "
                  "neighbours takes 20,000 nails a year, a fifteenth of one nailer's year "
                  "and no living for him. A village on a navigable river, whose trade can "
                  "travel as far as the water does, takes 600,000, and keeps two nailers. "
                  "Nothing about the villagers has changed except how far their trade "
                  "can go."),
            ("p", "Then he turns to what widens a market. &ldquo;A broad-wheeled waggon, "
                  "attended by two men, and drawn by eight horses, in about six weeks time, "
                  "carries and brings back between London and Edinburgh near four ton "
                  "weight of goods. In about the same time a ship navigated by six or eight "
                  "men, and sailing between the ports of London and Leith, frequently "
                  "carries and brings back two hundred ton weight of goods.&rdquo; The ratio "
                  "is easy to work. Two hundred tons is fifty wagon-loads of four, and "
                  "fifty wagons mean a hundred men and four hundred horses, which are "
                  "Smith's figures. By land that is two tons a man; by sea it is between "
                  "twenty-five and thirty-three, so a man on the ship does roughly the "
                  "work of twelve to seventeen on the road. The goods that bear a price in "
                  "proportion to their weight are the only ones the wagons can move, and "
                  "Smith asks what goods could bear the expense of land carriage between "
                  "London and Calcutta."),
            ("p", "Hence his geography. Because water carriage opens a wider market, "
                  "&ldquo;it is upon the sea-coast, and along the banks of navigable "
                  "rivers, that industry of every kind naturally begins to subdivide and "
                  "improve itself&rdquo;, and only much later in the inland parts. The "
                  "nations that were first civilized dwelt round the Mediterranean, a "
                  "sea without tides and with many islands, so that sailors who dared not "
                  "lose sight of the coast could still cross it. Egypt was the first "
                  "country improved because the Nile and its canals gave water carriage "
                  "to nearly every village, and Smith says the same of Bengal and the "
                  "eastern provinces of China, though he says their antiquity is "
                  "&ldquo;not authenticated by any histories of whose authority we, in this "
                  "part of the world, are well assured&rdquo;. And where there is no water "
                  "carriage, in the interior of Africa and in what he calls Tartary and "
                  "Siberia, he finds none of the improvement."),
            ("p", "That last sweep is the weakest part of the chapter, and Smith's "
                  "readers have said so. It rests on what a European knew in 1776, it "
                  "passes over the caravan routes that historians of Asia and Africa have "
                  "since described, and it "
                  "takes the coast as the cause of the civilisation when the coast might "
                  "be a consequence of it. The core of the chapter does not stand or fall "
                  "with it. The economist Allyn Young added a point in 1928 that Smith's "
                  "sentence does not contain: the division of labour does not only wait for "
                  "the market but widens it, because each new specialist is a customer "
                  "for others, so that the limit and the thing limited feed on one "
                  "another. Smith's own first chapter says that every "
                  "workman has a great quantity of his own work to dispose of, and "
                  "exchanges it for a great quantity of theirs, which is half of "
                  "Young's point."),
            ("p", "This is the end of Smith's first account of the division of labour: "
                  "what it does, why it arises and what limits it. In the next course the "
                  "exchange it depends on gets its instrument. Chapter 4 asks what happens "
                  "when the butcher has more meat than he can eat and the baker has no "
                  "need for any, and why every society has ended by choosing a metal."),
        ],
        "lab": ("wonkit", {
            "mode": "division",
            "view": "market",
            "qty_unit": "nails",
            "output": 300000,
            "days": 300,
            "preset": "highlands",
            "presets": [
                {"id": "highlands",
                 "label": "Smith's Highland nailer: 1,000 nails a year against 300,000",
                 "places": "highlands, 1000",
                 "expect": {
                          "wdvKeeps": "highlands 0",
                          "wdvYearShare": "highlands 1/300 ≈ 0.3%",
                          "wdvLive": "none of 1 place",
                          "wdvPerDay": "1,000 nails a day",
                         }},
                {"id": "ladder",
                 "label": "The Highlands, then larger places, written for this lesson (the Highlands are Smith's)",
                 "places": "highlands, 1000; village, 30000; market-town, 150000; port, 900000; city, 3000000",
                 "expect": {
                          "wdvKeeps": "highlands 0; village 0; market-town 0; port 3; city 10",
                          "wdvYearShare": "highlands 1/300 ≈ 0.3%; village 1/10 = 10%; market-town 1/2 = 50%; port 3 = 300%; city 10 = 1,000%",
                          "wdvLive": "2 of 5 places: port, city",
                          "wdvPerDay": "1,000 nails a day",
                         }},
                {"id": "by-water",
                 "label": "An inland village and the same village on a navigable river, written for this lesson",
                 "places": "inland-village, 20000; river-village, 600000",
                 "expect": {
                          "wdvKeeps": "inland-village 0; river-village 2",
                          "wdvYearShare": "inland-village 1/15 ≈ 6.7%; river-village 2 = 200%",
                          "wdvLive": "1 of 2 places: river-village",
                          "wdvPerDay": "1,000 nails a day",
                         }},
            ],
            "panel_title": "How many nailers a place can keep",
            "panel_intro": (
                "Each place's yearly demand and what one specialist makes in a year go in. "
                "The lab divides, floors, and says whether a full-time trade can live "
                "there. Smith's own figures are the 1,000, the 1,000 a day and the 300 days."
            ),
        }),
        "steps_title": "Counting the specialists a place can keep",
        "steps_intro": "Four steps, the same for any trade and any place.",
        "steps": [
            ("Find one specialist's year",
             "Multiply what he makes in a day by the days he works: 1,000 nails a day and "
             "300 days make 300,000 nails a year."),
            ("State the place's demand",
             "How many of the same good the place will take in a year, from every customer "
             "within reach. Smith's Highland figure is a thousand."),
            ("Divide",
             "The demand over one man's yearly output is the share of a man's year the "
             "place takes. Anything under one is a part-time trade; the whole number "
             "below it is how many men the place can keep."),
            ("Change the market, not the man",
             "Widen the place's reach and repeat the division. The difference is the effect "
             "of the extent of the market and nothing else."),
        ],
        "worked": {
            "title": "A Highland nailer, and a port that keeps three",
            "intro": [
                "Smith's nailer makes a thousand nails a day for three hundred days. You want "
                "to know how much of his year a Highland district, and then a port, would "
                "give him.",
            ],
            "lines": [
                "one man's year:  1000 · 300 = 300000 nails",
                "Highlands:  1000 / 300000 = 1/300 of a year",
                "village:  30000 / 300000 = 1/10 of a year",
                "port:  900000 / 300000 = 3 nailers",
                "ship against wagon:  200 / 4 = 50 wagons",
            ],
            "after": [
                "Smith's one day in three hundred is `1/300` of a year. The nailer's trade "
                "is impossible in the Highlands and takes three men in the port, and in "
                "neither place is the nailer any different. The ship against the wagon is "
                "the reason a port can be a market for places that cannot reach each other "
                "by road.",
            ],
        },
        "quiz_title": "The reach of a market",
        "quiz": [
            {"q": "A nailer makes 300,000 nails a year and a Highland district would take "
                  "1,000. What share of his year's work would the district give him?",
             "a": ["1/3 of it", "1/30 of it", "1/300 of it", "1/3000 of it"],
             "c": 2,
             "why": "`1000/300000 = 1/300`, which is Smith's one day's work in the year, "
                    "since there are 300 working days. The other fractions are factors of "
                    "ten off."},
            {"q": "Smith says a waggon carries about four tons between London and Edinburgh "
                  "and a ship about two hundred. How many waggons does a ship's cargo "
                  "replace?",
             "a": ["20", "50", "100", "400"],
             "c": 1,
             "why": "`200/4 = 50` waggons. A hundred is the number of men they need, and "
                    "four hundred the number of horses. Smith's own sentence says "
                    "&ldquo;fifty broad-wheeled waggons, attended by a hundred men, and drawn "
                    "by four hundred horses&rdquo;."},
            {"q": "A place takes 900,000 nails a year and a nailer makes 300,000. How many "
                  "nailers can it keep?",
             "a": ["3", "30", "300", "None"],
             "c": 0,
             "why": "`900000/300000 = 3`. Three hundred is the number of working days in "
                    "Smith's year, and a place that takes less than one nailer's year keeps "
                    "none."},
            {"q": "According to Smith, why does industry begin to subdivide and improve "
                  "itself first on the sea-coast and along navigable rivers?",
             "a": ["Because the soil is better near the sea",
                   "Because sailors are more skilful than carters",
                   "Because water carriage opens a wider market to every sort of industry",
                   "Because governments protect the coast"],
             "c": 2,
             "why": "Smith's reason is that water carriage &ldquo;opens the whole world for "
                    "a market to the produce of every sort of labour&rdquo;. He says nothing "
                    "about better soil near the sea or about government protection, and "
                    "skilful sailors are not the point; the point is the cost of carrying "
                    "goods."},
        ],
        "mistakes": [
            ("Thinking a trade needs a big town because its goods are special",
             "Smith's nailer is no different in the Highlands and in a port. What differs "
             "is how many nails a year are wanted. A trade fails where demand is below a "
             "man's year of work, whatever the goods."),
            ("Reading the limit as a ceiling the market simply sets",
             "Smith says the market limits the division, which is a claim that it cannot "
             "go further. Later economists, Allyn Young among them, added that the division "
             "also enlarges the market, so that one does not simply wait for the other."),
            ("Taking the geography for a proof",
             "The cases of Egypt, Bengal, China and Africa are illustrations with the "
             "evidence of 1776, and Smith himself calls the antiquity of Bengal and China "
             "unauthenticated. The nailer and the wagon are arithmetic, the coasts and "
             "rivers are history, and they differ in how much can be checked."),
        ],
        "standard": (
            "Finish when you can say how many specialists a place can keep from its demand "
            "and one man's output.",
            "Given a place's yearly demand for a good and one specialist's yearly output, "
            "compute the share of a year and the number of whole specialists, and use "
            "Smith's wagon and ship figures to say why water carriage widens a market."
        ),
        "note": (
            "The lab divides demand by output, and the figure that matters is the demand, "
            "which Smith does not measure: the 1,000 nails is a reasoned guess, and the "
            "villages and towns of the <code>ladder</code> preset are the lesson's. The "
            "arithmetic cannot say whether the Highlands really lacked a nailer, whether "
            "demand grows with the market or the market with demand, or whether the "
            "carriage figures of 1776 hold for any other century. What it does show is the "
            "form of the claim: a division of labour that works at one scale fails below "
            "it."
        ),
    },
]
