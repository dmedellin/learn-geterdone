"""So-Called Primitive Accumulation, lessons 1-4 -- Volume I, Chapters 26 to 29.

Every quotation is copied from /mnt/project-files/capital-texts/volume-1-kerr.txt
(the Kerr edition of Volume I); the comment beside each lesson gives its line
numbers. Footnote numerals in the text are left out of the quotations, a
drop capital is printed as an ordinary capital, and the translator's double
quotation marks inside a quotation are printed as single curly quotes. Nothing
else is changed.

Part Eight is history, and the most disputed part of the book. The labs compute
the mechanism each chapter describes, with illustrative figures except where a
preset says it uses Marx's; where historians dispute Marx's account the lesson
names who holds each side.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Kerr vol. 1, l. 5255 (the vicious circle); l. 5257 (original sin; the
    # frugal elite); l. 5259 (insipid
    # childishness; force in actual history); l. 5261 (free in a double
    # sense); l. 5263 (the definition); l. 5267 (blood and fire).
    {
        "slug": "the-secret-of-primitive-accumulation",
        "title": "The Secret of Primitive Accumulation",
        "module": "Chapter 26 · The Secret of Primitive Accumulation",
        "one_line": "The economists told the origin of capital as a tale of thrift, and Marx answers that it is the history of separating producers from their means of production.",
        "summary": (
            "Accumulation presupposes surplus value, surplus value presupposes capitalist "
            "production, and that presupposes capital and propertyless workers already "
            "there. Compute how long a worker saving from a wage would take to assemble a "
            "factory's capital, compare it with the years in which simple reproduction "
            "consumes any capital, and see why Marx says the secret is not saving but the "
            "divorce of the producer from the means of production."
        ),
        "key": [
            "the legend: a frugal elite saved",
            "days = target / (wage × share saved)",
            "a tenth of 3s a day: £3,000 in 200,000 days",
            "capital needs labourers free twice over",
            "the secret: producers parted from the means",
        ],
        "key_label": "Chapter 26 in five lines",
        "concepts_intro": (
            "Chapter 26 is short and sets up the whole of Part Eight: the question it "
            "answers, the answer it rejects, and the answer it gives."
        ),
        "concepts": [
            ("The previous accumulation",
             "Capital makes surplus value and surplus value makes more capital, so the "
             "movement seems to need a first capital that was not made this way. Adam Smith "
             "called it a previous accumulation; Marx translates it as primitive "
             "accumulation and asks where it came from."),
            ("Free in a double sense",
             "Money and means of production become capital only when they meet workers "
             "who are free twice over: free to sell their labour-power, not being slaves or "
             "serfs, and free of any means of production of their own, unlike a "
             "peasant-proprietor."),
            ("Separation as the secret",
             "Marx's answer is that the so-called primitive accumulation is the "
             "historical process that divorced the producers from the means of production, "
             "and so made the second kind of freedom general."),
        ],
        "read_title": "The legend first, then the history",
        "read_intro": (
            "Marx opens Part Eight with a parable he does not believe, and then says what "
            "he thinks it hides."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 26.</strong> &ldquo;This primitive accumulation "
                  "plays in Political Economy about the same part as original sin in theology. "
                  "Adam bit the apple, and thereupon sin fell on the human race. Its origin is "
                  "supposed to be explained when it is told as an anecdote of the past. In "
                  "times long gone by there were two sorts of people; one, the diligent, "
                  "intelligent, and, above all, frugal élite; the other, lazy rascals, "
                  "spending their substance, and more, in riotous living.&rdquo;"),
            ("p", "The chapter starts from a circle. You have watched, over the last "
                  "courses, money become capital, capital make surplus value and surplus "
                  "value become more capital. But each step presupposes the one before it, and "
                  "the first presupposes &ldquo;considerable masses of capital and of "
                  "labour-power&rdquo; already in the hands of producers of commodities. Adam "
                  "Smith had met the same circle and answered it with a stock that must be "
                  "accumulated before the division of labour can begin, his previous "
                  "accumulation. Marx keeps the question and translates the name: primitive, "
                  "in the sense of first."),
            ("p", "Then the joke. The economists tell the origin of capital the way theology "
                  "tells the origin of sin, as a story about two kinds of people long ago. "
                  "Theology's story at least explains why people must work; the economic "
                  "version explains why some people need not. &ldquo;Never mind!&rdquo;, Marx "
                  "writes, and names Adolphe Thiers, the French statesman who defended property "
                  "against the socialists of 1848 with this very tale. &ldquo;Such insipid "
                  "childishness is every day preached to us in the defence of property.&rdquo; "
                  "His counter-claim is blunt: &ldquo;In actual history it is notorious that "
                  "conquest, enslavement, robbery, murder, briefly force, play the great "
                  "part.&rdquo;"),
            ("p", "The legend deserves a fairer hearing than Marx gives it, because it has "
                  "serious holders. Max Weber argued in 1905 that a disciplined, saving, "
                  "Protestant asceticism shaped the spirit of early capitalism. François "
                  "Crouzet's studies of the first English industrialists found that most "
                  "founders came from the middling ranks, merchants, master craftsmen and "
                  "farmers, started small, and grew by ploughing their profits back. Neither "
                  "claims that capital was saved out of wages. Both claim that thrift and "
                  "reinvestment, not plunder, built most firms. Marx's reply, which the next "
                  "paragraphs compute, is that profits to plough back already presuppose "
                  "people who work for wages."),
            ("p", "First the legend in its plainest form, which the lab computes. A labourer "
                  "earns 3s a day and saves a tenth of it, 3.6 pence. The target is £3,000, the "
                  "yearly wage bill of the carpet factory in “Machinery and the Displaced "
                  "Worker”, 100 workers at £30 a year. That is 720,000 pence, so the saving "
                  "takes 200,000 working days, the figure in the carpet preset. At about 300 working days a year it is more than "
                  "six and a half centuries. Save the whole wage and eat nothing, the whole-wage "
                  "preset, and it is still 20,000 days, some 67 years. The mill preset sets the "
                  "same saving against a smaller capital of £600: 40,000 days, over 130 years. Thrift out of a wage does not make a "
                  "factory's capital in a working life."),
            ("p", "Now set that beside the result of “Simple Reproduction”. There Marx took a "
                  "capital of £1,000 that yields £200 of surplus value a year, all of it "
                  "consumed by its owner. After 5 years he has consumed a sum equal to his "
                  "capital, and on Marx's reckoning what he still holds is capitalised surplus "
                  "value, other people's unpaid labour. So even a capital that really was saved "
                  "loses its origin in a computable number of years. Two hundred thousand days "
                  "to build it by thrift; five years for reproduction to replace it with "
                  "surplus value."),
            ("p", "But the sum is not the chapter's main point. Money and commodities, Marx "
                  "says, are no more capital in themselves than are the means of production. "
                  "They become capital only when two kinds of commodity-owner meet: on one side "
                  "the owners of money and means of production, on the other free labourers. "
                  "And free in a particular way:"),
            ("p", "<strong>Volume I, Chapter 26.</strong> &ldquo;Free labourers, in the double "
                  "sense that neither they themselves form part and parcel of the means of "
                  "production, as in the case of slaves, &hellip; nor do the means of "
                  "production belong to them, as in the case of peasant-proprietors&rdquo;. "
                  "&ldquo;The so-called primitive accumulation, therefore, is nothing else than "
                  "the historical process of divorcing the producer from the means of "
                  "production.&rdquo;"),
            ("def", ("Primitive accumulation",
                     "On Marx's definition, the historical process that separated the "
                     "immediate producers from their means of production, turning the means "
                     "of production and subsistence into capital and the producers into "
                     "wage-labourers. It is primitive because it comes before capital's own "
                     "accumulation, as its starting point.")),
            ("p", "Read the two freedoms against each other. A slave is not free in the "
                  "first sense; a peasant who owns her land is not free in the second, because "
                  "she can live by working her own means of production and need not sell her "
                  "labour-power to anyone. A capital of £3,000 saved by any means at all would "
                  "still need people of the second kind before it could employ them. That is "
                  "why Marx calls the separation the secret: it is the condition the thrift "
                  "story leaves out."),
            ("p", "Marx grants that the history has two faces. Seen from one side it is the "
                  "workers' emancipation from serfdom and from the guilds, &ldquo;and this side "
                  "alone exists for our bourgeois historians&rdquo;. Seen from the other, the "
                  "new freedmen became sellers of themselves only after they were robbed of "
                  "their own means of production, and &ldquo;the history of this, their "
                  "expropriation, is written in the annals of mankind in letters of blood and "
                  "fire&rdquo;. How much of the history was robbery and how much was slow "
                  "economic change is exactly what historians still argue about, and the next "
                  "lessons give both sides."),
            ("p", "Marx takes England as his example, because there alone, he says, the "
                  "process has its classic form. The next lesson, “Expropriation of the "
                  "Agricultural Population”, follows how the English peasants were separated "
                  "from the land, from the fifteenth century to the clearing of the "
                  "Highlands."),
        ],
        "lab": ("capkit", {
            "mode": "accumulate",
            "view": "thrift",
            "money_unit": "s",
            "preset": "carpet",
            "presets": [
                {"id": "carpet", "label": "3s a day, a tenth saved, against the carpet factory's £3,000",
                 "wage": 3, "saving_share": "1/10", "target": 60000,
                 "expect": {"acDaysToTarget": "200,000 working days"}},
                {"id": "mill", "label": "The same saving against a smaller capital of £600",
                 "wage": 3, "saving_share": "1/10", "target": 12000,
                 "expect": {"acDaysToTarget": "40,000 working days"}},
                {"id": "whole-wage", "label": "The whole wage saved, against £3,000",
                 "wage": 3, "saving_share": 1, "target": 60000,
                 "expect": {"acDaysToTarget": "20,000 working days"}},
            ],
            "panel_title": "Saving a capital out of a wage",
            "panel_intro": (
                "The wage and the target are in shillings: £3,000 is 60,000s and £600 is "
                "12,000s. The tile divides the target by the part of the wage saved each "
                "working day. Compare the first and last presets: saving every penny of the "
                "wage only divides the time by ten."
            ),
        }),
        "steps_title": "Timing the saving of a capital",
        "steps_intro": "Four steps, from a daily wage to the days needed and what they leave out.",
        "steps": [
            ("Put both sums in one unit",
             "Express the wage and the target capital in the same money: £1 is 20s and 1s "
             "is 12d, so £3,000 is 60,000s."),
            ("Find the daily saving",
             "Multiply the wage by the share saved. A tenth of 3s is 3/10 s, which is "
             "3.6d."),
            ("Divide",
             "Working days needed = target / daily saving. At about 300 working days a "
             "year, divide again by 300 for years."),
            ("Set it beside reproduction",
             "Divide the capital by the surplus value consumed each year for the years in "
             "which simple reproduction consumes a sum equal to it. Then name what neither "
             "figure supplies: workers with no means of production of their own."),
        ],
        "worked": {
            "title": "A labourer and a carpet factory",
            "intro": [
                "A labourer earns 3s a day and saves a tenth. You want the working days "
                "needed to save the £3,000 a carpet factory pays in wages in a year, and "
                "the years in which a capital of £1,000 yielding £200 a year is consumed.",
            ],
            "lines": [
                "target:  £3,000 = 60,000s",
                "saved a day:  3s × 1/10 = 3.6d",
                "days:  60,000 / (3/10) = 200,000",
                "years at 300 days:  200,000 / 300 = 666 2/3",
                "reproduction:  £1,000 / £200 = 5 years",
            ],
            "after": [
                "Six and two-thirds centuries of thrift against five years of consumed "
                "surplus value. Marx's point lies past both numbers: whatever the sum and "
                "however it was gathered, it becomes capital only when it meets people who "
                "have nothing to sell but their labour-power.",
            ],
        },
        "quiz_title": "Thrift and separation",
        "quiz": [
            {"q": "A labourer earns 2s a day and saves a quarter of it. How many working days "
                  "does it take to save £500?",
             "a": ["20,000", "1,000", "5,000", "250"],
             "c": 0,
             "why": "£500 is 10,000s and a quarter of 2s is 1/2 s a day, so "
                    "10,000 / (1/2) = 20,000 days. Five thousand saves the whole wage; 1,000 "
                    "divides pounds by half a shilling; 250 divides pounds by the wage."},
            {"q": "On Marx's definition in Chapter 26, which person is a free labourer in the "
                  "double sense?",
             "a": ["A serf who owes the lord three days a week",
                   "A peasant who owns the land she works",
                   "A former weaver with no loom, who may work for whoever hires her",
                   "A slave hired out by his owner for wages"],
             "c": 2,
             "why": "The weaver is free in both senses: she is no one's property, and she owns "
                    "no means of production. The serf and the slave are not free in the first "
                    "sense; the peasant-proprietor is not free in the second, since she can "
                    "live from her own land."},
            {"q": "A capital of £2,000 yields £400 of surplus value a year, all consumed by "
                  "its owner. On the reckoning of “Simple Reproduction”, after how many years "
                  "has he consumed a sum equal to his capital?",
             "a": ["5", "4", "10", "20"],
             "c": 0,
             "why": "£2,000 / £400 = 5 years. Ten years would be right if he consumed half the "
                    "surplus value, 20 if he consumed a quarter of it, and 4 if he consumed "
                    "£500 a year."},
            {"q": "What does Marx say the so-called primitive accumulation is?",
             "a": ["The saving that a frugal minority did before capitalism began",
                   "The historical process of divorcing the producer from the means of "
                   "production",
                   "The first surplus value a capitalist makes and reinvests",
                   "The gold and silver Europe gathered before the sixteenth century"],
             "c": 1,
             "why": "Marx's definition is the divorce of the producer from the means of "
                    "production. The frugal minority is the legend he rejects; reinvested "
                    "surplus value is capitalist accumulation itself, which presupposes the "
                    "separation; and treasure is one of the levers of Chapter 31, not the "
                    "definition."},
        ],
        "mistakes": [
            ("Thinking the first capitalists became so by saving",
             "In its plain form, saving out of wages, the tile refutes it: 3.6d a day "
             "takes 200,000 working days to reach £3,000, and even the whole wage takes "
             "20,000. The stronger form, held by Weber and supported by Crouzet's founders, "
             "is that capital grew by thrift and reinvested profit. Marx's reply is that "
             "profit to reinvest presupposes workers who own nothing, so the saving explains "
             "the size of a capital, not the separation that lets it be capital."),
            ("Treating money or means of production as capital in themselves",
             "Marx says they &ldquo;want transforming into capital&rdquo;, and that this "
             "happens only when they meet labourers free in both senses. A sum saved by a "
             "labourer in a world of peasant-proprietors would find no one to employ."),
            ("Reading the emancipation and the expropriation as two different events",
             "Marx's claim is that they are one process seen from two sides: the producers "
             "were freed from serfdom and the guilds, and in the same history they lost "
             "their own means of production. A history that tells only the first, he says, "
             "is the one the economists tell."),
        ],
        "standard": (
            "Finish when you can time a saved capital and state what it presupposes.",
            "Given a wage, the share saved and a target capital, compute the working days "
            "needed; given a capital and the surplus value consumed each year, compute the "
            "years in which it is consumed; and name the two senses in which Marx's "
            "labourer is free."
        ),
        "note": (
            "The lab times a saving and nothing more. It shows that thrift out of a wage "
            "cannot assemble a factory's capital; it cannot show where the first capitals "
            "actually came from, which is a question of evidence that historians from Weber "
            "to Crouzet answer differently from Marx. The 3s wage and the 300-day year are "
            "illustrative; the £3,000 is the carpet factory's wage bill and the £1,000 and "
            "£200 are Marx's, from Chapter 23."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Kerr vol. 1, l. 5338 (the Sutherland clearing); l. 5283 and l. 5285 (the
    # fifteenth-century peasantry); l. 5303 (the economic
    # causes set aside); l. 5293 (Bacon); l. 5313 (the law as the instrument);
    # l. 5348 (idyllic methods).
    {
        "slug": "expropriation-from-the-land",
        "title": "Expropriation of the Agricultural Population",
        "module": "Chapter 27 · Expropriation of the Agricultural Population from the Land",
        "one_line": "Over three centuries the English and Scottish peasantry was separated from the land, and the same working day became a day with a surplus in it for someone else.",
        "summary": (
            "Marx follows the separation from the free peasantry of the fifteenth century, "
            "through enclosures, the Reformation and the parliamentary enclosure of commons, "
            "to the clearing of the Highlands. Compute a smallholder's working day before "
            "and after expropriation, and the surplus labour that separation makes available "
            "to an employer, for one household and for the 3,000 families of the Sutherland "
            "clearing."
        ),
        "key": [
            "own land: the whole day for the household",
            "surplus = day − necessary labour",
            "estate: surplus × households",
            "same day, same work, a new owner",
            "the chapter sets the economic causes aside",
        ],
        "key_label": "Chapter 27 in five lines",
        "concepts_intro": (
            "The chapter is a history in stages, and the lab reduces each stage to the "
            "same change in the working day."
        ),
        "concepts": [
            ("The free peasantry",
             "By the fifteenth century, Marx says, serfdom had gone in England and most "
             "people were free peasant proprietors. Even wage-labourers had cottages, four "
             "or more acres and the use of the common, so they could live partly from their "
             "own land."),
            ("Stages of expropriation",
             "Feudal retainers disbanded; peasants evicted for sheep-walks; church lands "
             "seized at the Reformation; state lands taken after 1688; commons enclosed by Act "
             "of Parliament; and last the clearing of estates, of which the Highlands are "
             "Marx's example."),
            ("A day with a surplus in it",
             "Working one's own land, every hour of the day is worked for the household. "
             "Separated from it and hired, the same person works a day of which only the "
             "necessary part replaces the wage, and the rest is surplus labour for the "
             "employer."),
        ],
        "read_title": "The clearing of an estate",
        "read_intro": (
            "The chapter's last and most systematic case comes first: the Duchess of "
            "Sutherland's estate between 1814 and 1820, as Marx reports it."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 27.</strong> &ldquo;From 1814 to 1820 these "
                  "15,000 inhabitants, about 3000 families, were systematically hunted and "
                  "rooted out. All their villages were destroyed and burnt, all their fields "
                  "turned into pasturage. British soldiers enforced this eviction, and came to "
                  "blows with the inhabitants. One old woman was burnt to death in the flames "
                  "of the hut, which she refused to leave. Thus this fine lady appropriated "
                  "794,000 acres of land that had from time immemorial belonged to the "
                  "clan.&rdquo;"),
            ("p", "The chapter gets there by a long road, and it starts with people who were "
                  "not poor. In the fifteenth century, Marx writes, serfdom had practically "
                  "disappeared in England and the immense majority were free peasant "
                  "proprietors. Even the agricultural wage-labourers had cottages and four or "
                  "more acres, and shared the common land, which gave &ldquo;pasture to their "
                  "cattle, furnished them with timber, fire-wood, turf&rdquo;. That world "
                  "allowed a wealth of the people, he says, but &ldquo;it excluded the "
                  "possibility of capitalistic wealth&rdquo;."),
            ("p", "Then the stages. At the end of the fifteenth century the great lords "
                  "disbanded their retainers and drove peasants from the land to turn arable "
                  "into sheep-walks, because Flemish wool had raised the price of English wool. "
                  "Parliament legislated against it for a hundred and fifty years, in vain. "
                  "Francis Bacon praised Henry VII's law for keeping farms large enough "
                  "&ldquo;to keep the plough in the hands of the owners and not mere "
                  "hirelings&rdquo;, and Marx reads the phrase as an unwitting statement of "
                  "what capital needed the opposite of. The Reformation threw the church's "
                  "lands to royal favourites and speculators; after 1688 state lands were "
                  "given away or sold for almost nothing."),
            ("p", "In the eighteenth century the means changed. Where the earlier thefts were "
                  "individual acts of violence that the law opposed, now &ldquo;the law itself "
                  "becomes now the instrument of the theft of the people's land&rdquo;: Acts "
                  "for the enclosure of commons, by which, in Marx's phrase, the landlords grant "
                  "themselves the people's land. He counts 3,511,770 acres of common land "
                  "enclosed between 1801 and 1831. The last stage is the clearing of estates, "
                  "and its classic place is the Highlands, where the clan's land, held by the "
                  "chief only as titular owner, was turned into his private property."),
            ("p", "Sutherland is the example. The 15,000 people were given about 6,000 acres "
                  "of waste on the shore, two acres a family, at a rent; the clan land became "
                  "29 sheep farms; by 1835, Marx reports, 131,000 sheep had replaced the "
                  "15,000 Gaels. The Duchess, &ldquo;well instructed in "
                  "economy&rdquo;, let the shore land to the clansmen &ldquo;in the nobility "
                  "of her heart&rdquo;: Marx's sarcasm is doing the arguing here. And then the "
                  "sheep-walks became deer forests."),
            ("p", "In the middle of this history Marx stops to say what he is not "
                  "claiming:"),
            ("p", "<strong>Volume I, Chapter 27.</strong> &ldquo;We leave on one side here the "
                  "purely economic causes of the agricultural revolution. We deal only with "
                  "the forcible means employed.&rdquo;"),
            ("p", "That sentence is where the chapter's critics begin. J. D. Chambers argued in "
                  "1953 that parliamentary enclosure raised the demand for farm labour, and "
                  "that the industrial workforce came from a growing population rather than "
                  "from people driven off the land. Robert Allen argued in 1992 that enclosure "
                  "added little to output and mainly moved income from farmers and cottagers to "
                  "landlords, a finding closer to Marx's. Eric Richards, the historian of the "
                  "Highland Clearances, does not dispute the evictions but questions some of "
                  "the figures Marx took from his sources and reads the Sutherland plan as a "
                  "resettlement scheme that failed. The lab cannot decide between them."),
            ("p", "What the lab can do is compute the mechanism the chapter is about. Take a "
                  "smallholder's 12-hour day. On her own land every hour is worked for her "
                  "household, so the surplus labour performed for anyone else is 0 hours: the smallholder "
                  "preset. Now "
                  "separate her from the land and hire her for the same 12 hours, at a wage "
                  "whose value takes 6 hours to produce. Nothing about the work has changed: "
                  "the same hours, the same skill. The day now holds 6 hours of surplus labour "
                  "for her employer, a rate of surplus value of 100%, as the labourer preset "
                  "shows. Make it the 3,000 "
                  "families of Sutherland, one wage-worker each, and the separation makes "
                  "18,000 hours a day of surplus labour available to whoever employs them: the "
                  "clearing preset."),
            ("def", ("Expropriation",
                     "In this chapter, the separation of the immediate producers from the land "
                     "and the other means by which they worked for themselves. On the lab's "
                     "model it changes no hour of the working day; it changes who the hours "
                     "beyond the necessary ones are worked for.")),
            ("p", "That last clause says available, not delivered. The Sutherland families "
                  "mostly did not become the Duchess's wage-workers: they were sent to the "
                  "shore to fish, or emigrated, or went to Glasgow. The lab computes what "
                  "separation makes possible for capital in general. Marx's summary is in his "
                  "most ironic register: church property, state domains and common lands were "
                  "taken by &ldquo;just so many idyllic methods of primitive "
                  "accumulation&rdquo;."),
            ("p", "The people turned off the land could not all be employed as fast as they "
                  "were turned off. The next lesson, “Bloody Legislation and the Forcing Down of "
                  "Wages”, asks what the law did with them, and with the wages of those who "
                  "were hired."),
        ],
        "lab": ("capkit", {
            "mode": "workday",
            "view": "separate",
            "money_unit": "hours",
            "preset": "smallholder",
            "presets": [
                {"id": "smallholder", "label": "A smallholder's 12-hour day on her own land",
                 "day": 12, "necessary": 6, "own_land": True, "count": 1,
                 "expect": {"wdSurplus": "0 h", "wdRate": "0 = 0%"}},
                {"id": "labourer", "label": "The same 12 hours as a wage-labourer, 6 necessary",
                 "day": 12, "necessary": 6, "own_land": False, "count": 1,
                 "expect": {"wdSurplus": "6 h", "wdRate": "1 = 100%"}},
                {"id": "clearing", "label": "Marx's 3,000 Sutherland families, each a wage-labourer (the day is illustrative)",
                 "day": 12, "necessary": 6, "own_land": False, "count": 3000,
                 "expect": {"wdSurplus": "18,000 h", "wdRate": "1 = 100%"}},
            ],
            "panel_title": "One working day, before and after the land is gone",
            "panel_intro": (
                "The day and the necessary labour-time stay the same in every preset; only "
                "whether the worker holds her own land, and how many households are counted, "
                "change. The bar shows the necessary and surplus parts of one day."
            ),
        }),
        "steps_title": "From a smallholding to a day with a surplus",
        "steps_intro": "Four steps, the same for one household or for an estate.",
        "steps": [
            ("Fix the day and the necessary labour",
             "Take the length of the working day and the hours needed to produce the value "
             "of a day's subsistence. Both are the same before and after the separation."),
            ("On one's own land",
             "Every hour is worked for the producer's household. The surplus labour "
             "performed for anyone else is 0 hours, and the rate is 0%."),
            ("As a wage-labourer",
             "Surplus labour = day − necessary labour, and the rate of surplus value = "
             "surplus / necessary."),
            ("Scale to an estate",
             "Multiply the surplus labour of one day by the number of households "
             "separated, one wage-worker each. The figure is what separation makes "
             "available to employers, not a count of who was actually hired."),
        ],
        "worked": {
            "title": "Sutherland, as a sum",
            "intro": [
                "Each of 3,000 households works a 12-hour day, and the value of a day's "
                "subsistence takes 6 hours to produce. You want the surplus labour before and "
                "after the households lose their land.",
            ],
            "lines": [
                "on own land:  0 h of surplus for anyone else",
                "as wage-labour:  12 − 6 = 6 h a day; 6/6 = 100%",
                "3,000 households:  3,000 × 6 = 18,000 h a day",
            ],
            "after": [
                "The work did not change; the owner of the surplus did. The 3,000 families "
                "are Marx's figure. The 12 and 6 hours are illustrative, and the chapter's "
                "point is the zero becoming six, not the size of either.",
            ],
        },
        "quiz_title": "The day before and after",
        "quiz": [
            {"q": "A cottager works 10 hours a day on her own land. Separated from it, she is "
                  "hired for the same 10 hours at a wage whose value takes 4 hours to produce. "
                  "How much surplus labour does her day hold for an employer?",
             "a": ["6 hours", "4 hours", "10 hours", "0 hours"],
             "c": 0,
             "why": "Surplus labour is the day less the necessary labour: 10 − 4 = 6 hours. "
                    "Four hours is the necessary part; 10 is the whole day; 0 is her surplus "
                    "for anyone else while she still had her land."},
            {"q": "In that example, what is the rate of surplus value after the separation?",
             "a": ["2/3 = 66.67%", "3/2 = 150%", "3/5 = 60%", "5/2 = 250%"],
             "c": 1,
             "why": "The rate is surplus over necessary labour, 6/4 = 3/2 = 150%. Sixty per "
                    "cent divides the surplus by the whole day; 2/3 divides necessary by "
                    "surplus labour; 250% divides the whole day by the necessary part."},
            {"q": "Two hundred households are separated from their land, each supplying one "
                  "wage-worker for a 12-hour day with 7 hours necessary. How much surplus "
                  "labour a day does the separation make available?",
             "a": ["1,000 hours", "1,400 hours", "2,400 hours", "5 hours"],
             "c": 0,
             "why": "Each day holds 12 − 7 = 5 hours of surplus, and 200 × 5 = 1,000. The "
                    "1,400 hours are the necessary labour of all 200; 2,400 is every hour "
                    "worked; 5 is one household's figure."},
            {"q": "Marx writes, &ldquo;We leave on one side here the purely economic causes of the "
                  "agricultural revolution.&rdquo; What does that sentence commit the chapter to?",
             "a": ["Denying that enclosure raised agricultural output",
                   "Treating only the forcible means of expropriation, not whether farming "
                   "methods improved",
                   "Showing that every enclosure was illegal",
                   "Proving that the industrial workforce came only from evicted peasants"],
             "c": 1,
             "why": "He says he deals &ldquo;only with the forcible means employed&rdquo;. He "
                    "does not deny higher output; Chapter 30 says the soil yielded as much or "
                    "more. He describes legal enclosure by Act of Parliament, and the source of "
                    "the industrial workforce is the question Chambers and others dispute, not "
                    "one this sentence settles."},
        ],
        "mistakes": [
            ("Thinking that what changed at the clearing was the work, not who it was done for",
             "This reads the chapter as a story of farming technique. In the lab the day "
             "stays 12 hours and the necessary labour 6 in every preset, so nothing about "
             "the work moves; yet the surplus labour for someone else goes from 0 hours on "
             "her own land to 6 hours as a wage-labourer, and to 18,000 hours a day for the "
             "3,000 Sutherland families. Whether enclosure also raised yields is a separate "
             "question, which Marx sets aside and historians such as Chambers and Allen "
             "still argue."),
            ("Reading 0 hours as a claim that smallholders had no surplus at all",
             "The lab's zero is surplus labour for anyone else. A smallholder might work "
             "beyond her household's needs and keep or sell the product, and real "
             "smallholders often paid rent and tithes. The model isolates what separation "
             "adds: a part of the day worked for an employer."),
            ("Reading the estate figure as people actually hired",
             "Eighteen thousand hours a day is what 3,000 separated households make "
             "available. Many of the Sutherland families fished, emigrated or went to the "
             "towns. The lab computes the mechanism, not the census."),
        ],
        "standard": (
            "Finish when you can compute the surplus labour that separation creates.",
            "Given the length of the day, the necessary labour-time and a number of "
            "households, compute the surplus labour for an employer before and after the "
            "producers lose their land, the rate of surplus value after it, and the total "
            "for the households together."
        ),
        "note": (
            "The lab's smallholder owes no rent, tithe or labour service, so her surplus for "
            "anyone else is exactly zero; real peasants owed some of all three, which is why "
            "the zero is a model of what separation changes and not a description of "
            "fifteenth-century life. The 12 and 6 hours are illustrative; the 3,000 families "
            "and the other Sutherland figures are Marx's, from his sources, and historians "
            "have revised several of them."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Kerr vol. 1, l. 5386 (the Statute of Labourers); l. 5388 (a maximum, no
    # minimum); l. 5360 (grim irony); l. 5378 (dull compulsion); l. 5392
    # (Pitt); l. 5394 (a permanent Trades' Union of the capitalists).
    {
        "slug": "bloody-legislation",
        "title": "Bloody Legislation and the Forcing Down of Wages",
        "module": "Chapter 28 · Bloody Legislation against the Expropriated",
        "one_line": "The expropriated were whipped into wage-labour by vagrancy laws, and their wages were held down by statutes that fixed a maximum and never a minimum.",
        "summary": (
            "Chapter 28 has two halves: the laws against vagabonds that disciplined the "
            "people turned off the land, and the labour statutes, from 1349 to 1813, that "
            "fixed the most a worker could be paid. Compute the gap between a statutory wage "
            "and the value of labour-power, and the rate of surplus value the statute "
            "enforces, with illustrative figures."
        ),
        "key": [
            "the statute fixed a maximum, never a minimum",
            "value made = day × daily value / necessary",
            "the gap: labour-power's value − the wage",
            "s/v = (value made − wage) / wage",
            "force at the start; dull compulsion later",
        ],
        "key_label": "Chapter 28 in five lines",
        "concepts_intro": (
            "The chapter's claim is that at its birth capitalism needed the state to do "
            "what, once established, the labour market does by itself."
        ),
        "concepts": [
            ("The laws against vagabonds",
             "From Henry VIII to James I, people without work were whipped, branded, "
             "enslaved or executed for being without work. Marx reads the laws as treating "
             "the expropriated as &ldquo;voluntary&rdquo; criminals who could have gone on "
             "working under conditions that no longer existed."),
            ("The statutory maximum",
             "The Statute of Labourers of 1349 and its successors fixed wages by law, made "
             "it a crime to pay more and a greater crime to take more, and voided "
             "workers' combinations. They set a ceiling and no floor."),
            ("Force and dull compulsion",
             "Once capitalist production stands on its own feet, Marx says, the reserve army "
             "keeps wages in their rut and direct force is used only exceptionally. At its "
             "genesis the state had to regulate wages directly."),
        ],
        "read_title": "A tariff of wages, fixed by law",
        "read_intro": (
            "The second half of the chapter, on wages, comes first, because it is the half "
            "the lab computes."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 28.</strong> &ldquo;The Statute of Labourers was "
                  "passed at the urgent instance of the House of Commons. &hellip; A tariff of "
                  "wages was fixed by law for town and country, for piece-work and day-work. "
                  "The agricultural labourers were to hire themselves out by the year, the "
                  "town ones &lsquo;in open market.&rsquo; It was forbidden, under pain of "
                  "imprisonment, to pay higher wages than those fixed by the statute, but the "
                  "taking of higher wages was more severely punished than the giving "
                  "them.&rdquo;"),
            ("p", "The chapter opens not with wages but with the people the last lesson "
                  "left on the road. The proletariat created by expropriation, Marx says, could "
                  "not be absorbed by the new manufactures as fast as it was made, and could not "
                  "at once adapt to the discipline of the new condition. So, across Western "
                  "Europe, came laws against vagabondage. Under Henry VIII in 1530 sturdy "
                  "vagabonds were to be whipped and sent home to &ldquo;put themselves to "
                  "labour&rdquo;. &ldquo;What grim irony!&rdquo;, Marx writes. Under Edward VI in "
                  "1547 a man who refused to work could be condemned as a slave to whoever "
                  "denounced him. Elizabeth and James I kept the whipping and added "
                  "branding."),
            ("p", "Historians have tested the list. C. S. L. Davies showed in 1966 that the "
                  "slavery statute of 1547 was repealed within about two years and seems hardly "
                  "to have been enforced, and later work on vagrancy, A. L. Beier's among it, "
                  "treats the statutes as evidence of what lawmakers feared as much as of what "
                  "magistrates did. Marx's catalogue is of the law's text. Its force as history "
                  "depends on enforcement, which he does not measure."),
            ("p", "Then the turn the chapter's argument rests on. Once capitalist production "
                  "is fully developed, the constant relative surplus population keeps wages "
                  "where capital needs them. &ldquo;The dull compulsion of economic relations "
                  "completes the subjection of the labourer to the capitalist.&rdquo; Direct "
                  "force is used only exceptionally. At the genesis it was otherwise: the rising "
                  "bourgeoisie used the state to &ldquo;regulate&rdquo; wages, to lengthen the "
                  "day and to keep the labourer dependent, and Marx calls this an essential "
                  "element of primitive accumulation."),
            ("p", "The Statute of Labourers of 1349 is where the wage laws start. Marx's "
                  "context is that wage-labourers were then few and well placed, with demand "
                  "for labour outrunning supply. Historians add the event behind the date: the "
                  "Black Death of 1348 and 1349 killed perhaps a third or more of England's "
                  "people, labour became scarce, wages rose, and the statute tried to hold them "
                  "to their old level. It was enforced hard for a time, and yet, on James "
                  "Thorold Rogers's wage series and later ones, real wages in the century "
                  "after it were among the highest of the whole pre-industrial era. The law's "
                  "aim and the law's effect are two different questions."),
            ("p", "<strong>Volume I, Chapter 28.</strong> &ldquo;The spirit of the Statute of "
                  "Labourers of 1349 and of its offshoots, comes out clearly in the fact, that "
                  "indeed a maximum of wages is dictated by the State, but on no account a "
                  "minimum.&rdquo;"),
            ("p", "The lab computes what a maximum of that kind does, with illustrative "
                  "figures. A labourer works a 12-hour day, and the value of a day's "
                  "labour-power, 3s, takes 6 hours to produce, so the day creates 6s of value. "
                  "Paid at the value, 3s, he yields 3s of surplus value, a rate of 100%: the market "
                  "preset. In the statute preset the law fixes 2s, one third below the value. The day still creates 6s; now 4s "
                  "of it is surplus value, and the rate is 200%. Now suppose masons combine to "
                  "demand 4s, a shilling above the value, as labour was scarce: the combination "
                  "preset. The rate falls to 50%, and that combination is exactly what the statutes declared void and "
                  "punished."),
            ("def", ("Statutory maximum wage",
                     "A wage fixed by law as the most an employer may pay and a worker may "
                     "take. Where it lies below the value of labour-power it raises the rate "
                     "of surplus value by law; it gives the worker no protection from a wage "
                     "below it.")),
            ("p", "The statutes lasted. In the sixteenth century money wages rose less than "
                  "prices, so real wages fell, and the Statute of Apprentices of 1563 let "
                  "justices fix wages by the season and the price of goods. In 1796 Samuel "
                  "Whitbread proposed a legal minimum wage for farm labourers, the first such "
                  "proposal in the House; &ldquo;Pitt opposed this&rdquo;, though he confessed "
                  "that the condition of the poor was cruel. The wage laws went in 1813, the laws "
                  "against combinations in 1825. Marx's verdict on five centuries is that "
                  "Parliament had held &ldquo;the position of a permanent Trades' Union of the "
                  "capitalists against the labourers&rdquo;."),
            ("p", "Wage laws you may know are the reverse: a minimum wage is a floor. The "
                  "chapter's point is about these statutes, whose wage was a ceiling, and the "
                  "lab's statute preset shows the direction of the effect. Whether a floor helps "
                  "or harms low-paid workers is argued in another literature, which this "
                  "Subject does not compute."),
            ("p", "Expropriation made the workers; the law disciplined them and held their "
                  "wages down. But where did the capitalists come from? The next lesson, "
                  "“Genesis of the Capitalist Farmer”, starts with the farmer, whose rise Marx "
                  "says you can almost put your hand on."),
        ],
        "lab": ("capkit", {
            "mode": "wages",
            "view": "statute",
            "money_unit": "s",
            "preset": "statute",
            "presets": [
                {"id": "statute", "label": "A statutory maximum of 2s, a third below the value",
                 "statutory_wage": 2, "lp_value": 3, "day": 12, "necessary": 6,
                 "expect": {"waGap": "1s below the value", "waRate": "2 = 200%"}},
                {"id": "market", "label": "The wage at the value of labour-power, 3s",
                 "statutory_wage": 3, "lp_value": 3, "day": 12, "necessary": 6,
                 "expect": {"waGap": "at the value", "waRate": "1 = 100%"}},
                {"id": "combination", "label": "Masons combine for 4s, which the statutes forbade",
                 "statutory_wage": 4, "lp_value": 3, "day": 12, "necessary": 6,
                 "expect": {"waGap": "1s above the value", "waRate": "1/2 = 50%"}},
            ],
            "panel_title": "What a wage fixed by law does to the rate",
            "panel_intro": (
                "All figures are illustrative. The day, the value of labour-power and the "
                "necessary hours stay the same; only the wage paid changes. The first tile "
                "compares the wage with the value of labour-power, the second gives the rate "
                "of surplus value at that wage."
            ),
        }),
        "steps_title": "The rate a wage statute enforces",
        "steps_intro": "Four steps, from the working day to the rate of surplus value.",
        "steps": [
            ("Value the day's product",
             "Value created in a day = day × value of labour-power / necessary hours. Twelve "
             "hours, with 3s produced in 6, create 6s."),
            ("Compare the wage with the value",
             "Gap = value of labour-power − wage paid. A positive gap is a wage below the "
             "value; a negative gap is a wage above it."),
            ("Compute the surplus value",
             "Surplus value = value created − wage paid."),
            ("Compute the rate",
             "Rate of surplus value = surplus value / wage paid. Compare it with the rate at "
             "a wage equal to the value."),
        ],
        "worked": {
            "title": "A shilling below the value",
            "intro": [
                "A labourer's day is 12 hours, and his labour-power, worth 3s a day, is "
                "reproduced in 6 of them. You want the rate of surplus value at the value and "
                "under a statutory maximum of 2s.",
            ],
            "lines": [
                "value created:  12 × 3s / 6 = 6s",
                "at the value:  (6s − 3s) / 3s = 1 = 100%",
                "statute:  3s − 2s = 1s below the value",
                "under the statute:  (6s − 2s) / 2s = 2 = 200%",
            ],
            "after": [
                "A third off the wage doubles the rate, because the shilling taken from the "
                "wage is added to a surplus value that was only 3s. The figures are "
                "illustrative; the direction of the effect is the statute's.",
            ],
        },
        "quiz_title": "Wages fixed by law",
        "quiz": [
            {"q": "A day of 10 hours creates value at 1s an hour, and labour-power is worth "
                  "5s a day. A statute fixes the wage at 4s. What rate of surplus value does "
                  "the statute enforce?",
             "a": ["3/2 = 150%", "1 = 100%", "3/5 = 60%", "5/4 = 125%"],
             "c": 0,
             "why": "The day creates 10s; at a 4s wage the surplus value is 6s, and "
                    "6s / 4s = 150%. One hundred per cent is the rate at the value, 5s; 60% "
                    "divides by the whole day's value; 125% divides 5s by 4s."},
            {"q": "In the same example, what is the gap between the statutory wage and the "
                  "value of labour-power?",
             "a": ["1s below the value", "1s above the value", "6s below the value",
                   "at the value"],
             "c": 0,
             "why": "The value of labour-power is 5s and the statute pays 4s, so the wage is "
                    "1s below it. Six shillings is the surplus value, not the gap."},
            {"q": "What, on Marx's account, does the Statute of Labourers of 1349 fix?",
             "a": ["A minimum wage below which no worker may be paid",
                   "A maximum wage, with heavier penalties for taking more than for paying "
                   "more",
                   "A wage equal to the value of labour-power",
                   "A legal working day of ten hours"],
             "c": 1,
             "why": "Marx's point is that the State dictated &ldquo;a maximum of wages&rdquo; "
                    "and &ldquo;on no account a minimum&rdquo;, and that taking higher wages was "
                    "punished more severely than paying them. Nothing in the statute ties the "
                    "wage to the value, and the ten-hour day is a Factory Act of 1847."},
            {"q": "What distinction does Marx draw between the genesis of capitalist "
                  "production and its developed state?",
             "a": ["At the genesis wages were set by the market; later by the state",
                   "At the genesis the state regulated wages by force; later the dull "
                   "compulsion of economic relations does it",
                   "At the genesis there was no wage-labour at all",
                   "Later, force is no longer used in any circumstances"],
             "c": 1,
             "why": "Once developed, the relative surplus population keeps wages in their rut "
                    "and direct force is used &ldquo;only exceptionally&rdquo;; at the genesis "
                    "the state had to &ldquo;regulate&rdquo; wages. The first choice reverses "
                    "this; wage-labour existed from the fourteenth century; and Marx says force "
                    "is still used, exceptionally."},
        ],
        "mistakes": [
            ("Thinking a wage law protects the worker by setting a floor",
             "That is true of modern minimum-wage laws, and it is the reverse of these. The "
             "Statute of Labourers fixed a ceiling: in the statute preset the first tile reads "
             "1s below the value, and the rate of surplus value rises from 100% "
             "to 200%. The only floor ever proposed in the period, Whitbread's in 1796, was "
             "rejected."),
            ("Thinking a law that lowers wages lowers the value of labour-power",
             "In the lab the value of labour-power stays 3s whatever the statute says; what "
             "moves is the gap between it and the wage, and with it the rate. A wage held "
             "below the value is a transfer to the employer, not a cheaper worker."),
            ("Reading the statutes' text as a record of what happened",
             "A law shows what its makers intended. Davies found the 1547 slavery statute "
             "barely enforced, and wages rose after 1349 despite the statute. The lab "
             "computes the effect the law aimed at, not its enforcement."),
        ],
        "standard": (
            "Finish when you can compute the rate a wage statute enforces.",
            "Given the working day, the necessary hours, the value of labour-power and a "
            "statutory wage, compute the value the day creates, the gap between the wage and "
            "the value of labour-power, and the rate of surplus value at the statutory wage."
        ),
        "note": (
            "Every figure in this lab is illustrative: the chapter gives no day, value or "
            "statutory rate to compute with, apart from details such as 2s 7½d for London "
            "tailors. The lab shows the direction in which a maximum below the value moves "
            "the rate. Whether the statutes held wages down in fact is a question of "
            "enforcement, and the wage histories since Thorold Rogers suggest that after "
            "1349 they often did not."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Kerr vol. 1, l. 5408 (golden fruit; rent diminished in reality), the
    # quotation running on to l. 5410 (rich, considering the circumstances);
    # l. 5404 and l. 5406 (from bailiff to farmer).
    {
        "slug": "the-capitalist-farmer",
        "title": "Genesis of the Capitalist Farmer",
        "module": "Chapter 29 · Genesis of the Capitalist Farmer",
        "one_line": "The farmer grew rich in the sixteenth century because his money rent was fixed by long lease while prices rose and wages lagged behind them.",
        "summary": (
            "The shortest chapter of Part Eight follows the farmer from serf bailiff to "
            "capitalist tenant, and finds the source of his fortune in the price revolution "
            "of the sixteenth century. Compute the real value of a money rent fixed while "
            "prices double, and what the farmer keeps when money wages rise by less than "
            "prices."
        ),
        "key": [
            "real rent = money rent / price index",
            "keeps = product·p − wages·w − rent",
            "fixed rent, rising prices: landlord loses",
            "wages lagging prices: labourer loses",
            "the farmer gains from both",
        ],
        "key_label": "Chapter 29 in five lines",
        "concepts_intro": (
            "Chapter 29 is two pages long. It answers the first half of the question the "
            "last two chapters left: whence came the capitalists?"
        ),
        "concepts": [
            ("From bailiff to farmer",
             "The first English farmer was a bailiff and a serf; then a farmer supplied with "
             "stock by the landlord; then a métayer who shared stock and product with him; "
             "then the farmer proper, who employs wage-labour with his own capital and pays "
             "the landlord rent."),
            ("The price revolution",
             "In the sixteenth century the value of the precious metals fell, and with it "
             "the value of money: prices of corn, wool and meat rose, and kept rising, for "
             "decades."),
            ("A rent fixed in money",
             "Farm leases ran long, often for 99 years, at a money rent fixed when they "
             "were signed. As prices rose the rent fell in real terms, while money wages "
             "rose more slowly than prices."),
        ],
        "read_title": "Golden fruit",
        "read_intro": (
            "The whole mechanism is in a few sentences, and the last of them names both "
            "losers. Leases at the time, Marx notes just before, often ran for 99 years."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 29.</strong> &ldquo;The progressive fall in "
                  "the value of the precious metals, and therefore of money, brought the "
                  "farmers golden fruit. Apart from all the other circumstances discussed "
                  "above, it lowered wages. A portion of the latter was now added to the "
                  "profits of the farm. The continuous rise in the price of corn, wool, meat, "
                  "in a word of all agricultural produce, swelled the money capital of the "
                  "farmer without any action on his part, whilst the rent he paid, (being "
                  "calculated on the old value of money) diminished in reality. Thus they grew "
                  "rich at the expense both of their labourers and their landlords.&rdquo;"),
            ("p", "If you have ever paid a fixed rent or a fixed-rate loan through a few years "
                  "of rising prices, you know the mechanism. The payment stays the same number "
                  "of pounds; everything else costs more; so the payment is lighter in real "
                  "terms each year, and the person receiving it is the loser. Chapter 29 says "
                  "this happened to English landlords on a grand scale in the sixteenth "
                  "century, and that it helped make a class of capitalist farmers."),
            ("p", "Marx begins by asking where the capitalists came from. Expropriation "
                  "creates directly only great landowners, so the farmer has to be traced "
                  "separately, and because his rise is slow, over centuries, &ldquo;we can, so to "
                  "say, put our hand on it&rdquo;. The bailiff, himself a serf, gives way in the "
                  "fourteenth century to a farmer whom the landlord stocks with seed, cattle "
                  "and implements; he becomes a métayer, a half-farmer who advances part of the "
                  "stock and shares the product; and he becomes the farmer proper, who "
                  "&ldquo;makes his own capital breed by employing wage-labourers&rdquo; and pays "
                  "rent."),
            ("p", "Two things then enriched him. The usurped commons let him keep more cattle "
                  "almost without cost. And the price revolution did the rest. On Marx's theory "
                  "of money, prices rose because the value of gold and silver fell: the American "
                  "mines, Potosí above all, produced silver with far less labour than Europe's, "
                  "so each ounce held less value and every price in silver rose."),
            ("def", ("Real rent",
                     "A money rent divided by the index of prices, so that it is measured in "
                     "the goods it buys at the prices of the time the lease was signed. A "
                     "rent of £20 when prices have doubled is £10 of real rent.")),
            ("p", "The lab keeps one farm's account. At the old prices the farm's product is "
                  "worth £100, the wage bill is £40 and the rent £20, so the farmer keeps £40: the stable "
                  "preset. In the price-revolution preset every price doubles, money wages included. The product sells for £200, the "
                  "wages cost £80, the rent is still £20, and the farmer keeps £100, which is "
                  "£50 at the old prices. The rent, meanwhile, is worth £10. Not everyone is "
                  "where he was: £10 of real value has passed from landlord to farmer."),
            ("p", "In the wages-lag preset money wages rise by half while prices double, which is Marx's "
                  "&ldquo;it lowered wages&rdquo;. The wage bill is £60, and the farmer keeps "
                  "£120, which is £60 at the old prices. Against the stable account that is £20 "
                  "of real gain: £10 from the landlord, whose rent is worth half what it was, "
                  "and £10 from the labourers, whose £60 buys what £30 bought before. The "
                  "arithmetic splits the gain exactly as Marx's last sentence does, between "
                  "&ldquo;their labourers and their landlords&rdquo;."),
            ("p", "Both halves of the story are disputed. On the cause of the price "
                  "revolution, Jean Bodin argued in 1568 that the flood of American treasure "
                  "raised prices because there was more money, the first statement of the "
                  "quantity theory, and Earl Hamilton's figures on Spanish treasure in 1934 "
                  "seemed to bear it out. Later historians, R. B. Outhwaite and Jack Goldstone "
                  "among them, pointed out that English prices began to rise before much "
                  "American silver arrived and argued that a growing population pressing on "
                  "land and food drove them. Marx's own account is the fall in the metals' "
                  "value. The lab takes the price index as given and does not choose."),
            ("p", "On the effect, Eric Kerridge's study of estate rents from 1540 to 1640 "
                  "found that rents, through entry fines and new leases, rose faster than "
                  "prices, so that many landlords were not losers at all. The farmer's golden "
                  "fruit, on that evidence, ripened only where a lease really was long and its "
                  "rent really was fixed. Where it was, the arithmetic is as Marx says; how "
                  "often it was is a question for the estate records."),
            ("p", "By the end of the sixteenth century, Marx concludes, England had a class of "
                  "capitalist farmers, &ldquo;rich, considering the circumstances of the "
                  "time&rdquo;. The next lesson, “The Home Market for Industrial Capital”, asks "
                  "what the agricultural revolution did for industry: where its workers, its "
                  "materials and its customers came from."),
        ],
        "lab": ("capkit", {
            "mode": "money",
            "view": "fixed-rent",
            "money_unit": "£",
            "preset": "price-revolution",
            "presets": [
                {"id": "price-revolution", "label": "Prices and money wages both double; the rent is fixed",
                 "rent": 20, "price_index": 2, "wage_index": 2, "product": 100, "wages": 40,
                 "expect": {"moRealRent": "£10", "moFarmerGain": "£100"}},
                {"id": "stable", "label": "Prices and wages as when the lease was signed",
                 "rent": 20, "price_index": 1, "wage_index": 1, "product": 100, "wages": 40,
                 "expect": {"moRealRent": "£20", "moFarmerGain": "£40"}},
                {"id": "wages-lag", "label": "Prices double; money wages rise by half",
                 "rent": 20, "price_index": 2, "wage_index": "3/2", "product": 100, "wages": 40,
                 "expect": {"moRealRent": "£10", "moFarmerGain": "£120"}},
            ],
            "panel_title": "A rent fixed by lease while prices rise",
            "panel_intro": (
                "The farm's product and wage bill are entered at the prices of the year the "
                "lease was signed, and the rent is fixed in money. The first tile is the rent "
                "at those old prices; the second is what the farmer keeps in money at the new "
                "prices. Divide the second by the price index to compare it with the stable "
                "preset. All figures are illustrative."
            ),
        }),
        "steps_title": "A farm's account through a price revolution",
        "steps_intro": "Four steps, from the lease to who gained and who lost.",
        "steps": [
            ("Deflate the rent",
             "Real rent = money rent / price index. The rent is fixed in money, so the "
             "landlord's loss is the money rent less the real rent."),
            ("Inflate the product and the wages",
             "Product at new prices = product × price index; wages at new prices = wage bill "
             "× wage index."),
            ("Compute what the farmer keeps",
             "Farmer keeps = product × price index − wages × wage index − rent, in money at "
             "the new prices."),
            ("Compare in real terms",
             "Divide what the farmer keeps by the price index and compare it with the stable "
             "case. Split the difference into the rent's fall and the wages' fall, each "
             "measured at old prices."),
        ],
        "worked": {
            "title": "Golden fruit, in pounds",
            "intro": [
                "At the old prices a farm's product is worth £100, its wages £40 and its rent "
                "£20. Prices double and money wages rise by half. You want the real rent, "
                "what the farmer keeps, and where his gain came from.",
            ],
            "lines": [
                "real rent:  £20 / 2 = £10",
                "keeps:  £200 − £60 − £20 = £120",
                "at old prices:  £120 / 2 = £60, against £40",
                "from the landlord:  £20 − £10 = £10",
                "from the labourers:  £40 − £60 / 2 = £10",
            ],
            "after": [
                "The farmer's real gain of £20 is £10 of rent and £10 of wages. The figures "
                "are illustrative; Marx gives no farm's accounts, only the direction.",
            ],
        },
        "quiz_title": "Rent, prices and wages",
        "quiz": [
            {"q": "A lease fixes a rent of £30. Prices rise to three times what they were. "
                  "What is the rent worth at the old prices?",
             "a": ["£10", "£90", "£30", "£27"],
             "c": 0,
             "why": "Real rent is the money rent divided by the price index: £30 / 3 = £10. "
                    "Ninety pounds multiplies instead of dividing; £30 is the money rent; £27 "
                    "subtracts the index."},
            {"q": "At old prices a farm's product is £60, its wages £20 and its rent £10. "
                  "Prices double and money wages double too. What does the farmer keep, in "
                  "money?",
             "a": ["£70", "£60", "£30", "£80"],
             "c": 0,
             "why": "£60 × 2 − £20 × 2 − £10 = £70. Sixty pounds doubles the rent as well, "
                    "which the lease forbids; £30 is the old figure; £80 forgets the rent."},
            {"q": "Prices double and every money payment doubles except a rent fixed by a "
                  "lease. Who is worse off in real terms?",
             "a": ["Nobody, since all prices doubled",
                   "The landlord",
                   "The farmer",
                   "The labourers"],
             "c": 1,
             "why": "The rent alone stayed fixed in money, so it alone fell in real terms; the "
                    "landlord loses and the farmer gains the same amount. Wages doubled with "
                    "prices, so the labourers are where they were, and not every payment "
                    "doubled."},
            {"q": "On Marx's account in Chapter 29, why did prices rise in the sixteenth "
                  "century?",
             "a": ["Because the population grew faster than food",
                   "Because the value of the precious metals, and so of money, fell",
                   "Because farmers raised their prices to pay higher rents",
                   "Because the state issued paper money"],
             "c": 1,
             "why": "Marx names the &ldquo;progressive fall in the value of the precious "
                    "metals, and therefore of money&rdquo;. Population pressure is the "
                    "explanation later historians such as Goldstone give, not Marx's; rents "
                    "were fixed, not raised; and there was no state paper money in Tudor "
                    "England."},
        ],
        "mistakes": [
            ("Thinking that when all prices double, every party is where it was",
             "That holds only if every payment doubles. A rent fixed by a 99-year lease does "
             "not. In the price-revolution preset prices and money wages double and the rent "
             "stays £20: the rent tile shows £10 at the old prices, and the farmer keeps £100, "
             "which is £50 at the old prices against £40 before. The landlord has lost £10 of "
             "real value and the farmer has gained it."),
            ("Thinking the farmer grew rich by his own exertion",
             "Marx's phrase is that rising prices swelled the farmer's capital &ldquo;without "
             "any action on his part&rdquo;. In the lab nothing about the farm's output "
             "changes between presets; only prices, wages and a fixed rent do."),
            ("Taking the price revolution's cause as settled",
             "Marx says the metals' value fell, Bodin and the quantity theorists that their "
             "quantity rose, and historians such as Goldstone that population drove prices. "
             "The lab takes the price index as an input and is silent between them."),
        ],
        "standard": (
            "Finish when you can trace a fixed rent through rising prices.",
            "Given a money rent, a price index, a money-wage index and a farm's product and "
            "wage bill at old prices, compute the real rent, what the farmer keeps in money "
            "and at old prices, and how much of his gain came from the landlord and how "
            "much from the labourers."
        ),
        "note": (
            "Every figure here is illustrative. The lab takes the price index as given and "
            "cannot say why prices rose, which Marx, the quantity theorists and the "
            "demographic historians explain differently. Nor can it say how many leases "
            "were long and fixed: Kerridge's estate studies suggest many rents kept pace "
            "with prices, so the mechanism is Marx's and its reach is disputed."
        ),
    },
]
