"""Course 5 -- So-Called Primitive Accumulation: Volume I, Part VIII, Chapters 26-33.

Split across two lesson modules: part_a is Chapters 26 to 29 (the secret, the
land, the laws, the farmer); part_b is Chapters 30 to 33 (the home market, the
industrial capitalist, the historical tendency, the colonies). One lesson per
chapter.
"""

from . import part_a, part_b

COURSE = {
    "slug": "capital-primitive-accumulation",
    "title": "So-Called Primitive Accumulation",
    "level": "Intermediate",
    "summary": (
        "Volume I, Part VIII, The So-Called Primitive Accumulation: Chapters 26 to 33. "
        "“So-called” is Marx's own, in the German and in the Kerr text. Where the "
        "first capital and the first propertyless workers came from: the legend of thrift "
        "and Marx's answer, the expropriation of the English peasantry, the laws that "
        "disciplined the expropriated and held their wages down, the rise of the farmer and "
        "the industrial capitalist, where Marx thinks the process leads, and what the "
        "colonies revealed about it."
    ),
    "blurb": (
        "Read the history at the end of Volume I with the mechanism of each chapter "
        "computed beside it. Time a capital saved out of a wage, turn a smallholder's day "
        "into a day with a surplus in it, price a claim on the state, and count the workers "
        "a colonist can hire when land is free. Where historians dispute Marx, each lesson "
        "says who and why."
    ),
    "key": [
        "days to save = target / daily saving",
        "surplus = day − necessary; 0 on own land",
        "s/v = (value made − wage) / wage",
        "real rent = money rent / price index",
        "home market = households × part bought",
        "price of a claim = yearly income / rate",
        "largest's share = largest / total",
        "years to land = land price / share saved",
    ],
    "assumes_short": "Wages and Accumulation",
    "assumes_long": (
        "the arithmetic of Volume I up to and including Wages and Accumulation: the working "
        "day, the rate of surplus value, wages, and simple and expanded reproduction"
    ),
    "outcomes_intro": (
        "By the end you can compute the mechanism each chapter of Part VIII describes, say "
        "what the figure shows, and say where the history behind it is disputed."
    ),
    "outcomes": [
        ("Time a saved capital",
         "Compute the working days a wage-earner would need to save a stated capital, and "
         "the years in which simple reproduction consumes a capital, and name the two "
         "senses in which Marx's labourer is free."),
        ("Compute the surplus separation creates",
         "Given a working day and its necessary labour, compute the surplus labour for an "
         "employer before and after producers lose their land, for one household and for "
         "an estate."),
        ("Compute what a wage statute enforces",
         "Compute the gap between a statutory wage and the value of labour-power, and the "
         "rate of surplus value the statute enforces."),
        ("Follow a fixed rent and a new market",
         "Compute the real value of a rent fixed while prices rise and what the farmer "
         "keeps when wages lag, and the market created when households must buy their "
         "subsistence."),
        ("Price a claim on the state",
         "Name the four levers of Chapter 31 and compute the price of a claim from its "
         "yearly income and the rate of interest, before and after the rate changes."),
        ("Compute centralisation and a colony's labour",
         "Compute the largest capital's share under growth and under merging, and the "
         "years of wage-labour a colonial land price imposes before a worker can leave."),
    ],
    "syllabus_intro": (
        "One lesson for each of the eight chapters of Part VIII, in Marx's order: the "
        "question and the legend, four chapters of English history, the industrial "
        "capitalist's levers, Marx's summary of where it leads, and the colonies."
    ),
    "how_to": [
        "Read the passage before the explanation. Every lesson opens with Marx's words "
        "and then goes back through them a phrase at a time. Quotations are from the Kerr "
        "editions in the Online Library of Liberty, hosted by Liberty Fund, Inc.",
        "Expect history, and expect it to be argued over. Part VIII is the most disputed "
        "part of Volume I: enclosure, the clearances, the vagrancy laws, the price "
        "revolution, the colonial system and the national debt all have historians who "
        "read the evidence differently from Marx. Each lesson states the strongest "
        "objection and names who holds it. The lessons present Marx's account; they do "
        "not ask you to accept it.",
        "Read the labs as mechanisms, not records. Each lab computes the mechanism its "
        "chapter describes, a day with a surplus in it, a rent fixed while prices rise, a "
        "debt priced as capital, with illustrative figures except where a preset says it "
        "uses Marx's. Change one figure at a time and watch what moves.",
        "Mind the chapter numbers. This course follows the English edition, as Penguin "
        "does. In the German, Chapters 26 to 32 here are the seven sections of Chapter 24, "
        "and Chapter 33 is Chapter 25, both inside Part Seven. The German Chapter 24 is "
        "titled die sogenannte ursprüngliche Akkumulation, the so-called primitive "
        "accumulation, the title the Kerr text gives to Part VIII.",
    ],
    "not_covered": [
        "The economic history itself. No lab here computes historical series: enclosure "
        "acreages, wage and price indices, slave-trade profits, the size of the national "
        "debt. Presets use Marx's figures where a label says so and illustrative ones "
        "otherwise, and the data that would settle the disputes is not carried.",
        "Adjudicating the historians. Chambers and Allen on enclosure, Davies on the "
        "vagrancy laws, Kerridge on Tudor rents, Williams, Engerman, O'Brien and Inikori on "
        "slavery and industrialisation, North and Weingast on public credit: each is named "
        "at full strength where the chapter meets them, and none is declared the winner.",
        "Primitive accumulation beyond England, and its later theorists. Marx takes "
        "England as the classic case. Rosa Luxemburg's argument that capital goes on "
        "accumulating by expropriation at its margins, and later versions of it, belong "
        "to the history of Marxism this Subject leaves out.",
        "The transition debate. Historians in and outside the Marxist tradition have argued "
        "for seventy years about how feudalism gave way to capitalism, in the exchanges "
        "associated with Maurice Dobb and Paul Sweezy and later with Robert Brenner. The "
        "lessons read Marx's chapters, not the debate they started.",
        "Marx's sources. Eden, Price, Bacon, Steuart, Somers, Fielden, Howitt and the "
        "others appear where Marx quotes them; their own reliability is a question for "
        "historians and is touched on only where a lesson's dispute turns on it.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from the quantities a "
        "lesson states, in exact arithmetic, on Marx's definitions. The figures are "
        "illustrative except where a preset says it uses Marx's, and no lab can tell you "
        "whether Marx's history is right: that is argued with evidence these pages do not "
        "carry."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
