"""Ground Rent, lessons 1-6 -- Volume III, Chapters 37-42.

Every quotation is copied from /mnt/project-files/capital-texts/volume-3-kerr.txt
(Untermann's translation of Volume III, Kerr edition); the comment beside each
lesson gives its line numbers. Footnote numerals in the text are left out of
the quotations, a drop capital is printed as an ordinary capital, and the
translator's double quotation marks inside a quotation are printed as single
curly quotes. Nothing else is changed.

The plain-text Kerr edition does not print the tables of Chapters 39 to 44;
they are images, read from /mnt/project-files/capital-texts/tables/volume-3/
(Kerr pp. 764-826 for these lessons). Every "Marx's figures" preset below was
checked against the printed table and against the sentences around it. Chapter 39 is reckoned in shillings and Chapters 40 to 44 in
pounds at 60s to the pound sterling's three: £2½ of capital is 50s and a price
of £3 a quarter is 60s. The labs keep shillings throughout, so that one table
can be compared with the next, and each lesson says so where Marx changes unit.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Kerr vol. 3, l. 5379 (capitalised rent, the irrational form; rent is not
    # derived from its own capitalisation); l. 5383 (the rate falls to 4%).
    # Inline: l. 5357 (three classes), l. 5359 (land-capital), l. 5363
    # (fruges consumere nati; Anderson), l. 5375 (Carey; North, Locke, Turgot),
    # l. 5389 (justify its existence by its existence), l. 5393 (capitalised
    # income from the lease), l. 5401 (Palmerston), l. 5473 (the third error).
    {
        "slug": "introductory-remarks-on-rent",
        "title": "Introductory Remarks on Ground Rent",
        "module": "Chapter 37 · Preliminaries",
        "one_line": "Ground rent is what a farmer pays for leave to put capital on a piece of the earth, and the price of land is that rent capitalised at the rate of interest, not the value of anything.",
        "summary": (
            "Part VI begins by setting the stage: capitalist farmers, wage-labourers on the "
            "land, and landowners who are paid for leave to farm it. Compute the price of a "
            "piece of land from its rent and the rate of interest, separate the true rent from "
            "the interest on drains and buildings that a lease payment may contain, and see "
            "the price rise when the rate of interest falls and the rent does not move."
        ),
        "key": [
            "rent: paid for leave to invest in land",
            "price of land = rent / rate of interest",
            "£200 at 5% = £4,000; at 4% = £5,000",
            "true rent = payment − interest on land-capital",
            "rent is not derived from its price",
        ],
        "key_label": "The preliminaries in five lines",
        "concepts_intro": (
            "Chapter 37 clears the ground before any rent is explained. It says whose rent "
            "this is, what part of a lease payment is not rent at all, and why land has a "
            "price though it has no value."
        ),
        "concepts": [
            ("Ground rent proper",
             "The sum a capitalist farmer pays the landowner, at fixed dates and by "
             "contract, for permission to invest capital in this piece of land. Marx calls "
             "it the form in which property in land &ldquo;realizes itself economically&rdquo;."),
            ("Land-capital",
             "Capital fixed in the soil: manure, drains, irrigation, levelling, farm "
             "buildings. The interest on it may be paid inside the lease money, but it is "
             "interest on capital, not rent for the soil as such."),
            ("The price of land",
             "A yearly rent capitalised at the ordinary rate of interest: the sum that, "
             "lent at that rate, would bring in the same income. It is the price of the "
             "rent, not of the land, which as no product of labour has no value."),
        ],
        "read_title": "The passage first, then the chapter's warnings",
        "read_intro": (
            "The passage is Marx's account of the price of land. It comes in the middle of "
            "the chapter, after he has separated rent from the interest it is mixed with."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 37.</strong> &ldquo;Ground-rent so capitalised "
                  "forms the purchase price or value of the land, a category which is on its face "
                  "irrational, just as the price of labor is, since the earth is not the product "
                  "of labor and therefore has no value. But on the other hand a real relation in "
                  "production is concealed behind this irrational form.&rdquo;"),
            ("p", "If you rent a flat, or know someone who farms rented land, you already know "
                  "the thing this Part is about: a payment made every year to someone for the "
                  "use of a piece of the earth they own and you do not. Marx puts that payment "
                  "into the setting the whole of Volume III assumes. The tillers of the soil are "
                  "wage-labourers, employed by a capitalist farmer who treats farming as one more "
                  "field for his capital, and who pays the landowner a sum fixed by contract "
                  "&ldquo;for the permission to invest his capital in this particular sphere of "
                  "production&rdquo;. That sum is ground rent. With it all three classes are on "
                  "stage at once, &ldquo;wage-laborers, industrial capitalists, land "
                  "owners&rdquo;, each with an income of its own."),
            ("p", "The first warning is that a lease payment is not all rent. A farmer may "
                  "drain a field, put up buildings, manure it for years. That is "
                  "&ldquo;land-capital&rdquo;, and the interest on it may be part of what the "
                  "landowner collects; but it is interest on capital, not rent for the soil as "
                  "such. When the lease ends the improvements stay with the land, and the next "
                  "lease charges for them. Marx's dry Latin for the landowners is "
                  "&ldquo;fruges consumere nati&rdquo;, born to consume the fruits of the earth, "
                  "and he notes that the obstacle this puts in the way of improvement was "
                  "denounced by James Anderson, a Scottish farmer who worked "
                  "out the modern theory of rent in the 1770s and whom Marx calls its "
                  "&ldquo;actual discoverer&rdquo;. The lab's improvements preset runs the "
                  "separation: of a payment of £200, £50 is interest on drains and buildings, so "
                  "the true rent is £150."),
            ("p", "The second warning is about the price. Marx's figures: a rent of £200 a year, "
                  "an average rate of interest of 5%. Someone who pays £4,000 for that land gets "
                  "5% on his money, exactly as if he had lent it out. In England this is reckoned "
                  "in &ldquo;years' purchase&rdquo;: £4,000 is twenty years of the rent. The "
                  "marx preset prints £4,000 for the price and £200 for the true rent."),
            ("p", "<strong>Volume III, Chapter 37.</strong> &ldquo;It is in fact the purchase "
                  "price, not of the land, but of the ground-rent yielded by it, calculated on the "
                  "ordinary rate of interest. But this capitalisation of rent has for its premise "
                  "the existence of rent, for rent cannot be explained and derived from its own "
                  "capitalisation.&rdquo;"),
            ("p", "Read that phrase by phrase. The price is the price &ldquo;of the "
                  "ground-rent&rdquo;, a title to an income. It is calculated &ldquo;on the "
                  "ordinary rate of interest&rdquo;, so it moves when that rate moves. And the "
                  "order of explanation runs one way: rent first, price after. Marx's own "
                  "example shows the direction. Let the rate of interest fall from 5% to 4% and "
                  "the same £200 is the income of £5,000; the land's price rises from twenty to "
                  "twenty-five years' purchase, and nothing on the farm has changed. That is the "
                  "rate-falls preset: £5,000, with the true rent still £200."),
            ("def", ("The price of land",
                     "The yearly rent divided by the rate of interest: the capital that, lent at "
                     "that rate, would yield the same income. It is a price of the rent, and it "
                     "rises when the rate of interest falls even if the rent stays the same.")),
            ("p", "Two older views Marx sets aside here are worth hearing at their best. One "
                  "says rent simply is interest: the landowner's land is a capital like any "
                  "other, he paid for it, and the rent is the return on what he paid. Henry "
                  "Carey, the American economist who saw harmony where Marx saw antagonism, "
                  "argued that rent is interest on all the labour ever spent improving the soil. "
                  "In the seventeenth century the argument ran the other way: Dudley North and "
                  "Locke defended interest by likening it to rent, and Turgot justified interest "
                  "&ldquo;from the existence of ground-rent&rdquo;. Marx's reply is that rent can "
                  "exist without any capital sunk in the land, and that a purchase only transfers "
                  "a title. If paying for land justified rent, he says, paying for a slave would "
                  "justify slavery; it is &ldquo;to justify its existence by its "
                  "existence&rdquo;."),
            ("p", "He adds a sharper point about practice. Whatever a tenant pays for leave to "
                  "farm shares one feature with real rent: it fixes the price of land, which "
                  "&ldquo;is nothing but the capitalised income from the lease of the "
                  "land&rdquo;. So lease money can contain a deduction from the farmer's normal "
                  "profit, or from his labourers' wages, and still be capitalised into the price "
                  "of land as if it were rent. Marx's examples are the Irish smallholder, whose "
                  "rent ate into his own wages and whose improvements went to the landlord, and "
                  "the English farm labourers whose depressed wages swelled rents during the wars "
                  "with France. When tenants asked Parliament for compensation for improvements, "
                  "Palmerston answered, Marx reports, that &ldquo;The House of Commons is a house "
                  "of landlords.&rdquo;"),
            ("p", "The chapter ends with three errors to avoid, and they set the plan for the "
                  "Part. Do not confuse the rent of different historical stages (Chapter 47 "
                  "traces them). Do not think that explaining surplus value explains rent: under "
                  "capitalism rent is a surplus &ldquo;over and above profit&rdquo;, and that "
                  "extra is what needs explaining. And do not mistake what is true of every "
                  "commodity for something peculiar to land. What is peculiar, Marx says, is that "
                  "the rent's amount is fixed &ldquo;by the independent development of social "
                  "labor, in which he does not take part&rdquo;."),
            ("p", "The standard objection to the chapter is not to its arithmetic, which every "
                  "school accepts: the price of an asset is its income capitalised. It is to the "
                  "word &ldquo;irrational&rdquo;. On the marginal-productivity account that "
                  "economists built after the 1870s, land is a factor of production like any "
                  "other, its rent is what an extra acre adds to output, and its price is a "
                  "rational valuation of a scarce input. Marx's position is that the earth has a "
                  "price without a value, and the course follows his definitions without "
                  "deciding which account is right."),
            ("p", "So the price of land rests on rent, and rent is still unexplained. The next "
                  "lesson, “Differential Rent: General Remarks”, explains the first kind of rent "
                  "with a factory that has a waterfall and its neighbours that burn coal."),
        ],
        "lab": ("capkit", {
            "mode": "rent",
            "view": "price",
            "money_unit": "£",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's figures: a rent of £200 at 5%",
                 "rent": 200, "interest_rate": "1/20", "expect": {"rtPrice": "£4,000", "rtTrueRent": "£200"}},
                {"id": "rate-falls", "label": "Marx's figures: the same £200 when the rate falls to 4%",
                 "rent": 200, "interest_rate": "1/25", "expect": {"rtPrice": "£5,000", "rtTrueRent": "£200"}},
                {"id": "improvements", "label": "£200 a year, of which £50 is interest on drains and buildings",
                 "rent": 200, "interest_rate": "1/20", "improvement_interest": 50, "expect": {"rtPrice": "£4,000", "rtTrueRent": "£150"}},
            ],
            "panel_title": "What a rent is worth as a price",
            "panel_intro": (
                "The yearly payment and the rate of interest go in; the lab divides one by the "
                "other. If part of the payment is interest on capital sunk in the land, give it, "
                "and the second tile shows the rent left for the soil as such. Compare the first "
                "two presets: the rent is the same and the price is not."
            ),
        }),
        "steps_title": "Pricing a piece of land",
        "steps_intro": "Four steps, for any lease payment and rate of interest.",
        "steps": [
            ("Split the payment",
             "Separate the interest on capital sunk in the land, such as drains, buildings and "
             "lasting manuring, from the payment for the soil as such. What is left is the true "
             "ground rent."),
            ("Take the rate of interest",
             "Use the ordinary rate at which money is lent, written as a fraction: 5% is 1/20."),
            ("Capitalise",
             "Divide the yearly payment by the rate of interest. The result is the price of the "
             "land; divided by the payment it is the number of years' purchase."),
            ("Read the direction",
             "Hold the rent fixed and change the rate: the price moves against the rate. The "
             "price follows from the rent and the rate; neither the rent nor its cause follows "
             "from the price."),
        ],
        "worked": {
            "title": "Marx's £200 a year",
            "intro": [
                "A piece of land brings in £200 a year and money lends at 5%. You want its "
                "price, and its price when the rate of interest falls to 4%.",
            ],
            "lines": [
                "price at 5%:  £200 / (1/20) = £4,000",
                "years' purchase:  £4,000 / £200 = 20",
                "price at 4%:  £200 / (1/25) = £5,000",
                "years' purchase:  £5,000 / £200 = 25",
            ],
            "after": [
                "The rent never moved; the price rose by a quarter because money became cheaper "
                "to borrow. Marx draws the consequence: since the rate of interest tends to fall "
                "over time, the price of land tends to rise even when rents and grain prices do "
                "not.",
            ],
        },
        "quiz_title": "Rent, interest and the price of land",
        "quiz": [
            {"q": "Land brings in a rent of £300 a year and the rate of interest is 5%. What is "
                  "its price?",
             "a": ["£6,000", "£1,500", "£315", "£3,000"],
             "c": 0,
             "why": "The price is the rent capitalised: `300 / (1/20) = 6,000`, or twenty "
                    "years' purchase. £1,500 is five years of rent, £315 adds 5% to the rent, "
                    "and £3,000 capitalises at 10%."},
            {"q": "The rent on a farm stays at £200 while the rate of interest falls from 5% to "
                  "4%. What happens to the price of the land?",
             "a": ["It falls from £4,000 to £3,200",
                   "It rises from £4,000 to £5,000",
                   "It stays at £4,000, because the rent has not changed",
                   "It rises from £4,000 to £4,200"],
             "c": 1,
             "why": "At 4% the same £200 is the income of £5,000, so the price moves against the "
                    "rate. £3,200 multiplies instead of dividing; £4,000 ignores the rate; £4,200 "
                    "adds a year's rent."},
            {"q": "A tenant pays £200 a year, of which £50 is interest on drains the landowner "
                  "inherited with the land. On Marx's definitions, what is the ground rent "
                  "proper?",
             "a": ["£200", "£250", "£150", "£50"],
             "c": 2,
             "why": "Interest on capital incorporated in the soil may be paid inside the lease "
                    "money but &ldquo;does not constitute that ground-rent, strictly "
                    "speaking&rdquo;. The rent for the soil as such is `200 − 50 = 150`. £50 is "
                    "the interest, and £200 the whole payment."},
            {"q": "Why does Marx call the price of land an irrational category?",
             "a": ["Because land is sold below its value",
                   "Because the earth is not a product of labour and so has no value, yet it has a price",
                   "Because land prices are set by speculation alone",
                   "Because the rate of interest cannot be known in advance"],
             "c": 1,
             "why": "On his definitions value is labour, and the earth is no product of labour, "
                    "so a price of land is a price without a value. Land cannot be sold below a "
                    "value it does not have, and the chapter derives the price from rent and the "
                    "rate of interest, not from speculation."},
        ],
        "mistakes": [
            ("Thinking rent is the return on the land's value",
             "A landowner who bought his estate sees his rent as interest on the price he paid. "
             "Marx reverses the order: the price is the rent capitalised, so it cannot explain "
             "the rent. The rate-falls preset shows it: the rent stays £200 while the price "
             "goes from £4,000 to £5,000, and nothing on the land changed. Rent, he writes, "
             "&ldquo;cannot be explained and derived from its own capitalisation&rdquo;."),
            ("Counting the whole lease payment as rent",
             "Part of what a tenant pays may be interest on drains, buildings or past "
             "manuring, and part may even be taken from his own profit or his labourers' "
             "wages. All of it is capitalised into the price of land, but only the payment for "
             "the soil as such is ground rent proper: £150 of the £200 in the improvements "
             "preset."),
            ("Thinking a purchase justifies the rent",
             "The buyer did pay an equivalent, but to the seller, for a title that already "
             "existed. Marx's comparison is the slave bought for money, whose labour then looks "
             "like interest on the purchase price; to justify rent by its sale is to justify "
             "its existence by its existence."),
        ],
        "standard": (
            "Finish when you can price land from its rent and say what part is rent.",
            "Given a yearly payment, the interest on capital sunk in the land and the rate of "
            "interest, compute the true ground rent and the price of the land, and the price "
            "after a stated change in the rate of interest."
        ),
        "note": (
            "The lab capitalises a perpetual rent at a single rate of interest, which is "
            "Marx's assumption in this chapter. Real land prices also carry expectations, "
            "taxes, risk and the premium Marx himself mentions, that land is bought at a "
            "lower rate because it is thought safe. The £50 of interest in the improvements "
            "preset is illustrative; Marx gives no figure."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Kerr vol. 3, l. 5549 (private property does not create the surplus
    # profit); l. 5545 (natural basis, not source). Inline: l. 5505 (90 and
    # 115), l. 5511 (103½; coal cheaper), l. 5535 (monopolised natural power),
    # l. 5539 (10 pounds annually), l. 5543 (greater relative fertility),
    # l. 5553 (capitalised at 5%: 200 pounds; would disappear).
    {
        "slug": "differential-rent-general",
        "title": "Differential Rent: General Remarks",
        "module": "Chapter 38 · Differential Rent. General Remarks",
        "one_line": "A factory with a waterfall sells at the price set by factories on steam and pockets the difference; whoever owns the waterfall can take that difference as rent.",
        "summary": (
            "Before he turns to farming, Marx explains differential rent with a factory driven "
            "by a natural waterfall, competing with factories driven by steam. Compute the "
            "water-driven factory's surplus profit both ways Marx does, against the steam "
            "user's profit and against its own price of production, and see why the surplus "
            "becomes the owner's rent and vanishes when steam cheapens."
        ),
        "key": [
            "price set by the steam users: cost + profit",
            "surplus profit = price − cost − profit",
            "Marx: 115 − 90 − 15 = 10",
            "against own price: 115 − 103½ = 11½",
            "a waterfall is the basis, not the source",
        ],
        "key_label": "The waterfall in five lines",
        "concepts_intro": (
            "The chapter has one example and three claims about it: where the surplus profit "
            "comes from, why it lasts, and why it goes to the owner of the land."
        ),
        "concepts": [
            ("Surplus profit",
             "Profit above the average, made by a capital that produces more cheaply than the "
             "conditions that regulate the price. Every industry has it; normally competition "
             "wears it away as the better method spreads."),
            ("A monopolisable natural power",
             "A force of nature, like a waterfall, that raises the productivity of labour, is "
             "attached to particular pieces of land, and cannot be made by capital. Steam, by "
             "contrast, is at the command of any capital that buys an engine."),
            ("Differential rent",
             "The surplus profit that such a natural advantage makes lasting, transferred to "
             "the owner of the land that holds it. It is differential because it arises from a "
             "difference between individual and general prices of production."),
        ],
        "read_title": "The passage first, then the waterfall step by step",
        "read_intro": (
            "The passage is Marx's verdict on the waterfall's owner. The chapter reaches it by "
            "way of the factory owner's books."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 38.</strong> &ldquo;Hence private property in "
                  "land does not create that portion of value, which is transformed into surplus "
                  "profit, but it merely enables the landowner, who has possession of the "
                  "waterfall, to coax this surplus profit out of the pocket of the industrial "
                  "capitalist into his own.&rdquo;"),
            ("p", "Marx starts the theory of rent away from the farm, on purpose. Most of a "
                  "country's factories run on steam, a few on natural waterfalls. On steam, a "
                  "capital of 100 makes goods that sell at 115, the cost plus the average profit "
                  "of 15%, and that 115 is the regulating price for the whole branch. The "
                  "factory on the waterfall has a cost price of only 90, because the water costs "
                  "less materialised labour and less living labour: "
                  "&ldquo;the water wheel need not be heated&rdquo;. It still sells at 115. Its profit is 25 against the steam user's 15: a surplus "
                  "profit of 10. The marx preset prints £115 for the price and both of Marx's "
                  "measures in the surplus tile."),
            ("p", "Why two measures? Marx gives both. His first is the one above, 10, the water "
                  "user's profit less the steam user's. His second is the difference between the "
                  "general price and the water user's own individual price of production: if 100 "
                  "becomes 115, then 90 becomes 103½, and 115 less 103½ is 11½. The first "
                  "measure treats the water user as entitled to 15, the steam user's profit in "
                  "money; the second gives him 15% on his own smaller cost. The lab prints both, "
                  "and the lessons that follow use the first, which is the one Marx carries "
                  "forward."),
            ("p", "So far this is ordinary. Any capitalist with a better machine or a bigger "
                  "plant makes a surplus profit, and Marx has analysed it already in the "
                  "chapters on prices of production. What is different here? An ordinary "
                  "surplus profit comes from the capital itself, from its size or its method, "
                  "and competition removes it as the method spreads. The waterfall's comes from "
                  "a natural power that capital cannot make: water power &ldquo;is found only "
                  "locally in nature, and wherever it does not exist, it cannot be created by "
                  "any investment of capital&rdquo;. It is &ldquo;a monopolised natural "
                  "power&rdquo;, attached to particular pieces of the globe."),
            ("p", "Now let someone own those pieces. The industrial capitalist pays the owner "
                  "of the waterfall 10 pounds a year, keeps 15 on his 100 like everyone else, and "
                  "the surplus profit has become ground rent. It would make no difference if the "
                  "manufacturer owned the waterfall himself; he would collect the 10 &ldquo;in "
                  "his capacity as a landowner&rdquo;."),
            ("p", "<strong>Volume III, Chapter 38.</strong> &ldquo;The natural power is not the "
                  "source of the surplus profit, but only its natural basis, because this natural "
                  "basis permits an increase in the productive power of labor.&rdquo;"),
            ("p", "This is the claim the rest of the Part leans on, so take it phrase by phrase. "
                  "First, it is &ldquo;not the source&rdquo;: the water adds no value, for on Marx's "
                  "definitions nothing that is not labour does; the goods made with it contain "
                  "less labour and so less value. It is &ldquo;only its natural basis&rdquo;: "
                  "the water lets the same labour make more. The surplus profit exists because the "
                  "goods sell at the general price of production set by steam, not at their own "
                  "lower one. Marx's test is the steam-cheapens preset. If some new method cuts "
                  "the steam users' cost from 100 to 90, the price falls to 103½ and the "
                  "waterfall's surplus is nothing by either measure. The waterfall has not "
                  "changed; the rent is gone."),
            ("p", "The two-falls preset puts the water user's cost at 80 instead of 90. At the "
                  "same 115 the surplus profit is 20 against the steam user's profit and 23 "
                  "against its own price of production of 92. A better natural advantage makes "
                  "a larger difference, which is what &ldquo;differential&rdquo; means: the rent "
                  "is measured by a difference in productivity, &ldquo;the greater relative "
                  "fertility&rdquo; of one capital against the others in its branch."),
            ("p", "The waterfall even has a price, and you can compute it with the last lesson's "
                  "rule. The 10 a year at 5% interest is the income of a capital of 200 pounds, "
                  "and 200 pounds &ldquo;appears then as the capital-value of the waterfall "
                  "itself&rdquo;. It is a strange price, Marx notes: the owner collects the 10 "
                  "for as long as the conditions last, not for twenty years."),
            ("p", "The objection is the one that runs through the whole Part. An economist "
                  "after the 1870s would agree with every number here and still say the "
                  "waterfall is productive: remove it and output falls, so it earns its rent as "
                  "machines earn theirs. What the chapter says bears on that claim: the natural "
                  "power raises the productivity of labour, value on Marx's definitions is "
                  "labour, and the rent is a share of a surplus that exists only because the "
                  "price is set elsewhere. Which description is the better one is the question the "
                  "Subject leaves open."),
            ("p", "The waterfall is the model; the field is the case Marx cares about. The next "
                  "lesson, “Differential Rent I”, applies the same rule to four soils of unequal "
                  "fertility, and to Ricardo, who had done so first."),
        ],
        "lab": ("capkit", {
            "mode": "rent",
            "view": "waterfall",
            "money_unit": "£",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's figures: cost 100 on steam, 90 on water, profit 15%",
                 "cost_steam": 100, "cost_water": 90, "profit_rate": "3/20", "expect": {"rtPrice": "£115", "rtSurplusProfit": "£10 against the steam user's profit; £11½ against its own price of production"}},
                {"id": "two-falls", "label": "A better fall: cost 80 on water",
                 "cost_steam": 100, "cost_water": 80, "profit_rate": "3/20", "expect": {"rtPrice": "£115", "rtSurplusProfit": "£20 against the steam user's profit; £23 against its own price of production"}},
                {"id": "steam-cheapens", "label": "Marx's case: steam's cost falls from 100 to 90",
                 "cost_steam": 90, "cost_water": 90, "profit_rate": "3/20", "expect": {"rtPrice": "£207/2", "rtSurplusProfit": "£0 against the steam user's profit; £0 against its own price of production"}},
            ],
            "panel_title": "The factory on the waterfall",
            "panel_intro": (
                "The steam users' cost, the water user's cost and the average rate of profit go "
                "in. The steam users set the price; the second tile gives the water user's "
                "surplus profit by Marx's two measures. Choose steam-cheapens and watch the "
                "surplus go while the waterfall stays."
            ),
        }),
        "steps_title": "Computing a surplus profit and its rent",
        "steps_intro": "Four steps, for any natural advantage inside one branch of production.",
        "steps": [
            ("Find the regulating price",
             "Take the cost price under the conditions that supply most of the market, here "
             "steam, and add the average profit on it."),
            ("Compute Marx's measure",
             "Subtract the favoured producer's cost and the regulating producer's profit from "
             "the price: what is left is the surplus profit Marx carries forward."),
            ("Compute the second measure",
             "Raise the favoured cost by the average rate of profit for its own price of "
             "production, and subtract that from the regulating price."),
            ("Turn it into rent",
             "If the advantage is a natural power attached to land that others own, the "
             "surplus profit is paid to the owner as rent; capitalised at the rate of interest "
             "it becomes the price of the waterfall."),
        ],
        "worked": {
            "title": "Steam and water",
            "intro": [
                "Steam-driven factories have a cost price of 100, the one on the waterfall 90, "
                "and the average rate of profit is 15%. You want the water user's surplus "
                "profit by both measures, and the waterfall's price at 5% interest.",
            ],
            "lines": [
                "price:  100 + 15% of 100 = 115",
                "water user's profit:  115 − 90 = 25",
                "against the steam user:  25 − 15 = 10",
                "water user's own price:  90 + 15% of 90 = 103½",
                "against its own price:  115 − 103½ = 11½",
                "price of the waterfall:  10 / (1/20) = 200",
            ],
            "after": [
                "The owner of the fall collects the 10 as rent. Cut the steam users' cost to 90 "
                "and the price falls to 103½; the 10 and the 11½ both become 0, and so does the "
                "price of the waterfall.",
            ],
        },
        "quiz_title": "The waterfall and its rent",
        "quiz": [
            {"q": "Steam-driven mills have a cost price of 200 and the average rate of profit is "
                  "10%. A mill on a waterfall has a cost price of 180. What is its surplus profit "
                  "by Marx's first measure?",
             "a": ["20", "22", "18", "38"],
             "c": 0,
             "why": "The price is `200 + 20 = 220`; the water user's profit is `220 − 180 = 40` "
                    "against the steam user's 20, so 20. Twenty-two is the second measure, "
                    "`220 − 198`; 18 is 10% of 180; 38 subtracts only the water user's own "
                    "profit."},
            {"q": "On Marx's account, what is the source of the water user's surplus profit?",
             "a": ["The value the waterfall adds to the product",
                   "The landowner's title to the waterfall",
                   "The sale of its goods at the general price of production, above its own lower one",
                   "The sale of its goods above their price of production"],
             "c": 2,
             "why": "The waterfall is the &ldquo;natural basis&rdquo; and adds no value; the "
                    "title transfers the surplus but does not create it; and the goods sell at "
                    "the regulating price, not above it. The surplus is the gap between the "
                    "general and the individual price of production."},
            {"q": "In the steam-cheapens preset, the steam users' cost falls to 90. What happens "
                  "to the waterfall's rent?",
             "a": ["It rises, because the water user's goods are now relatively dearer",
                   "It stays at 10, because the waterfall is unchanged",
                   "It disappears",
                   "It falls to 5"],
             "c": 2,
             "why": "The regulating price is now `90 + 13½ = 103½`, the water user's own price "
                    "of production, so there is no difference left to pay as rent. Marx says "
                    "the surplus profit, the rent and the price of the waterfall "
                    "&ldquo;would disappear&rdquo;."},
        ],
        "mistakes": [
            ("Thinking the waterfall creates the surplus profit",
             "The water is free and powerful, so it is natural to credit it with the extra 10. "
             "Marx's answer is in the steam-cheapens preset: the same waterfall makes nothing "
             "extra once steam's cost falls to 90, because the surplus is a difference between "
             "two prices of production. The fall lets labour produce more; the surplus exists "
             "because the goods sell at a price set by steam."),
            ("Thinking the landowner's title creates the rent's substance",
             "Marx says the reverse: the surplus profit &ldquo;would also exist, if private "
             "property did not prevail&rdquo;. Ownership decides who gets it, not whether it "
             "exists."),
            ("Mixing up the two measures",
             "Ten and 11½ are both Marx's. Ten measures against the steam user's profit, 11½ "
             "against the water user's own price of production. Say which one a figure is; "
             "the later lessons use the first."),
        ],
        "standard": (
            "Finish when you can compute a natural advantage's surplus profit both ways.",
            "Given the regulating cost price, the favoured producer's cost price and the "
            "average rate of profit, compute the regulating price of production and the "
            "surplus profit against the regulating producer's profit and against the favoured "
            "producer's own price of production."
        ),
        "note": (
            "The figures 100, 90 and 15% are Marx's, and he says &ldquo;definite figures are "
            "immaterial&rdquo;; the two-falls preset's 80 is illustrative. The lab assumes the "
            "steam users regulate the price because they supply most of the market, as the "
            "chapter does; if the waterfalls supplied most of it, the regulating price would "
            "be theirs and there would be no surplus to pay."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Kerr vol. 3, l. 5564 (Ricardo quoted); l. 5669 (the primitive
    # misconception). Inline: l. 5592-5604 (Table I), l. 5610 (descending
    # succession: 15s, 20s, 30s, 60s), l. 5627-5635 (A' at 1 1/3 quarters,
    # 45s), l. 5639 and l. 5651 (Table III; "to 22, a growth of 22 1/9%"),
    # l. 5667 (eight times thirty), l. 5689-5691 (240s sold at 600s; a false
    # social value).
    {
        "slug": "differential-rent-i",
        "title": "Differential Rent I",
        "module": "Chapter 39 · The First Form of Differential Rent",
        "one_line": "Equal capitals on soils of unequal fertility make unequal products; the worst soil in use sets the price, and every better soil pays its surplus as rent.",
        "summary": (
            "Marx's four soils, A to D, take the same capital and yield 1, 2, 3 and 4 "
            "quarters of wheat. Compute the price the worst soil sets, the rent each better "
            "soil pays and the total, then change the order in which the soils were taken up, "
            "replace the worst soil with a better one and improve them all, and see why Marx "
            "says rent does not need a descent to ever worse land, as Ricardo thought."
        ),
        "key": [
            "price = worst soil's capital + profit / output",
            "A–D: 1, 2, 3, 4 quarters on 50s, 20%",
            "price 60s; rents 0, 60, 120, 180s",
            "total rent 360s = £18",
            "rent needs unequal soils, not worse ones",
        ],
        "key_label": "Differential Rent I in five lines",
        "concepts_intro": (
            "Chapter 39 is the first of six chapters of tables, and the one the others lean "
            "on. It turns the waterfall into a field, and then argues with Ricardo."
        ),
        "concepts": [
            ("The regulating soil",
             "The least fertile soil that must be farmed to supply the market. Its price of "
             "production per quarter, capital plus average profit divided by its output, is "
             "the market price of all the wheat."),
            ("Differential rent I",
             "The surplus profit of equal capitals on soils of unequal fertility or location, "
             "paid to the landowners. Each soil pays its extra product, valued at the "
             "regulating price."),
            ("False social value",
             "Marx's name for what the market price makes of the whole harvest: every quarter "
             "sells at the worst soil's price, so the crop sells for more than its total price "
             "of production, and the excess is the rent."),
        ],
        "read_title": "Ricardo first, then the four soils",
        "read_intro": (
            "The chapter opens by agreeing with Ricardo. Its argument with him comes after the "
            "tables, where Marx says what the tables do not need."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 39.</strong> &ldquo;Rent is always the "
                  "difference between the produce obtained by the employment of two equal "
                  "quantities of capital and labor&rdquo;, Marx quotes from Ricardo, and "
                  "comments: &ldquo;He should have added &lsquo;On the same quantities of "
                  "land,&rsquo; so far as ground-rent and not surplus profit in general is "
                  "concerned.&rdquo;"),
            ("p", "David Ricardo was a London stockbroker who made a fortune in the Napoleonic "
                  "wars and then wrote the most rigorous economics of his age. In 1815 he and "
                  "three others, Edward West, Thomas Malthus and Robert Torrens, published the "
                  "same idea within weeks: as population grows, farming is pushed onto poorer "
                  "land; the price of corn must rise until the poorest land in use pays its "
                  "costs and the ordinary profit; and every better field then earns more than "
                  "it needs, which its owner takes as rent. Rent on this account is no gift of "
                  "nature's generosity but a sign of its stinginess, and it rises as society "
                  "grows, while profits are squeezed. Ricardo used it to argue against the Corn "
                  "Laws, which kept foreign grain out and rents up. Marx takes over the "
                  "mechanism and calls Ricardo &ldquo;quite right&rdquo;."),
            ("p", "Here are Marx's soils, A, B, C and D, each taking 50 shillings of capital "
                  "with an average profit of 20%, so 60s of cost and profit per field. A yields "
                  "1 quarter of wheat, B 2, C 3, D 4. A is the worst soil the market needs, so "
                  "its 60s a quarter is the price of all the wheat. At 60s, B's 2 quarters sell "
                  "for 120s against its 60s: a surplus of 60s. C's surplus is 120s, D's 180s, "
                  "and the total is 360 shillings, &ldquo;equal to the sum of the differences "
                  "between D and A, C and A, B and A&rdquo;. The marx preset prints a price of "
                  "60s a quarter, rents of 0s, 60s, 120s and 180s, and a total of 360s, as "
                  "Marx's Table I on page 764 of the Kerr edition does."),
            ("p", "Now the history the table hides. Marx tells it two ways. Suppose D was "
                  "farmed first, when wheat was cheap. As demand grew the price rose until C "
                  "could be farmed, at 20s; then B, at 30s; then A, at 60s. At each step D's "
                  "rent grew: &ldquo;first of 5 shillings per quarter, or 20 shillings for the "
                  "4 quarters&rdquo;, then 60s, then 180s. The descending preset stops at the "
                  "middle step, with D, C and B in use: the price is 30s, and the rents are 0s, "
                  "30s and 60s, with D's 60s just as Marx says. Or suppose A was farmed first "
                  "and the better soils were found later, as settlers might find them: then the "
                  "price never rose above 60s, and the same table forms with the price "
                  "constant."),
            ("p", "That is the first half of Marx's quarrel with Ricardo, and he states it as a "
                  "conclusion of the tables:"),
            ("p", "<strong>Volume III, Chapter 39.</strong> &ldquo;This does away with the "
                  "primitive misconception of differential rent still found among men like West, "
                  "Malthus, Ricardo, to the effect that it necessarily requires a progress "
                  "toward worse and worse soil, or an ever decreasing productivity of "
                  "agriculture.&rdquo;"),
            ("p", "The better-added preset runs one of his cases. The worst soil is replaced by "
                  "one that yields 1⅓ quarters for the same 60s, or the old A is improved to "
                  "that yield, &ldquo;by the introduction of clover, etc.&rdquo;. The price falls "
                  "&ldquo;from 60 shillings to 45 shillings, or by 25%&rdquo;, and with B, C and "
                  "D unchanged the rents fall to 30s, 75s and 120s, 225s on these four soils. "
                  "Marx's Table II, on page 768, also brings in three soils between A and C, "
                  "yielding 1⅔, 2⅓ and 2⅔ quarters, with rents of 15s, 45s and 60s, for a total "
                  "of 345s. That is seven soils, and the lab holds six, so the preset keeps the "
                  "four that Table I had. (The table calls the 1⅓-quarter soil A and the "
                  "1⅔-quarter soil A′, though the sentence before it says A′ for the first.)"),
            ("p", "The improved preset is his Table III, on page 768: "
                  "every soil improves, but the better ones more, so A yields 2 quarters, B 4, C "
                  "7 and D 10. The price falls to 30s, half what it was, and yet total rent "
                  "rises: B's 60s is unchanged, C's goes to 150s, D's to 240s, &ldquo;eight "
                  "times thirty&rdquo;, as Marx says. The total is 450s, as the "
                  "table prints it, which is £22 10s and a rise of 25% on £18. The Kerr text prints the total as &ldquo;from 18 pounds "
                  "sterling to 22, a growth of 22 1/9%&rdquo;, and that is a slip: neither "
                  "figure follows from the yields or from the table, and even £22 would be a rise of 22 "
                  "2/9%. It also says the rent is &ldquo;doubled upon C&rdquo;, which the "
                  "yields do not give either, in money or in grain."),
            ("p", "What the tables show is the rule the rest of the Part builds on. Rent "
                  "needs unequal soils, not worsening ones. Its premise, in Marx's words, "
                  "&ldquo;is merely the inequality of the different kinds of soil&rdquo;; it can "
                  "grow with cultivation moving to better land, with the worst land improved, "
                  "with agriculture getting more productive. Ricardo's argument is about a "
                  "growing country with a given technique, where the next acre is the worse "
                  "one; Marx's tables treat that as one case among several."),
            ("p", "One more consequence, and Marx puts it sharply. The ten quarters of Table I "
                  "cost 240s to produce in all: 60s on each of four fields. They sell for 600s, "
                  "because every quarter fetches the worst soil's 60s. The 360s difference is "
                  "the rent. Marx calls this &ldquo;a false social value&rdquo;: the market, "
                  "which prices like goods alike, makes society pay for the whole harvest as if "
                  "all of it were grown on the worst land. A society that planned its farming, "
                  "he says, would not pay two and a half times the labour the crop contains. An "
                  "economist would reply that the price at the margin is what rations the "
                  "scarce good land, and that a single price is how a market tells farmers "
                  "which land to plough; the dispute is about what that price measures."),
            ("p", "Every soil here takes a single capital of 50s. The next lesson, "
                  "“Differential Rent II”, puts several capitals on the same field one after "
                  "another, and asks whether that makes a different kind of rent."),
        ],
        "lab": ("capkit", {
            "mode": "rent",
            "view": "dr1",
            "money_unit": "s",
            "qty_unit": "quarter",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's Table I: A, B, C, D yield 1, 2, 3, 4 quarters on 50s",
                 "soils": [{"name": "A", "capital": 50, "outputs": [1]},
                           {"name": "B", "capital": 50, "outputs": [2]},
                           {"name": "C", "capital": 50, "outputs": [3]},
                           {"name": "D", "capital": 50, "outputs": [4]}],
                 "profit_rate": "1/5", "regulating": "auto", "expect": {"rtPrice": "60s a quarter", "rtRents": "0s, 60s, 120s, 180s", "rtTotal": "360s"}},
                {"id": "descending", "label": "Marx's descending order: D, C and B in use, before A",
                 "soils": [{"name": "B", "capital": 50, "outputs": [2]},
                           {"name": "C", "capital": 50, "outputs": [3]},
                           {"name": "D", "capital": 50, "outputs": [4]}],
                 "profit_rate": "1/5", "regulating": "auto", "expect": {"rtPrice": "30s a quarter", "rtRents": "0s, 30s, 60s", "rtTotal": "90s"}},
                {"id": "better-added", "label": "Marx's Table II, four of its soils: A at 1⅓ quarters, B, C, D",
                 "soils": [{"name": "A", "capital": 50, "outputs": ["4/3"]},
                           {"name": "B", "capital": 50, "outputs": [2]},
                           {"name": "C", "capital": 50, "outputs": [3]},
                           {"name": "D", "capital": 50, "outputs": [4]}],
                 "profit_rate": "1/5", "regulating": "auto", "expect": {"rtPrice": "45s a quarter", "rtRents": "0s, 30s, 75s, 120s", "rtTotal": "225s"}},
                {"id": "improved", "label": "Marx's Table III: A, B, C, D improved to 2, 4, 7, 10 quarters",
                 "soils": [{"name": "A", "capital": 50, "outputs": [2]},
                           {"name": "B", "capital": 50, "outputs": [4]},
                           {"name": "C", "capital": 50, "outputs": [7]},
                           {"name": "D", "capital": 50, "outputs": [10]}],
                 "profit_rate": "1/5", "regulating": "auto", "expect": {"rtPrice": "30s a quarter", "rtRents": "0s, 60s, 150s, 240s", "rtTotal": "450s"}},
            ],
            "panel_title": "Four soils, one price",
            "panel_intro": (
                "Each soil's capital and output go in, with the average rate of profit. The "
                "least productive soil in use sets the price per quarter; each soil's rent is "
                "its output at that price less its capital and profit. Compare marx with "
                "improved: the price halves and the total rent rises."
            ),
        }),
        "steps_title": "Computing differential rent I",
        "steps_intro": "Four steps, for any set of soils each taking one equal capital.",
        "steps": [
            ("Cost each soil",
             "Add the average profit to each soil's capital: 50s at 20% is 60s. This is the "
             "sum each soil's product must fetch for its farmer to stay."),
            ("Find the regulating price",
             "Divide each soil's cost and profit by its output. The highest result among the "
             "soils the market needs is the price of every quarter."),
            ("Value each soil's product",
             "Multiply each soil's output by the regulating price and subtract its cost and "
             "profit. The remainder is its surplus profit, paid as rent; the regulating soil's "
             "is zero."),
            ("Add the rents",
             "The total rent is the sum. It equals the extra quarters of the better soils over "
             "the worst, valued at the regulating price."),
        ],
        "worked": {
            "title": "Marx's Table I",
            "intro": [
                "Soils A to D each take 50 shillings of capital at a 20% profit and yield 1, 2, "
                "3 and 4 quarters. You want the price, each soil's rent and the total.",
            ],
            "lines": [
                "cost and profit:  50 + 10 = 60 shillings a field",
                "price:  60 / 1 = 60 shillings a quarter (A)",
                "B:  2 · 60 − 60 = 60",
                "C:  3 · 60 − 60 = 120",
                "D:  4 · 60 − 60 = 180",
                "total:  0 + 60 + 120 + 180 = 360 shillings",
            ],
            "after": [
                "The 360 shillings are 6 quarters at 60s: B's one extra quarter over A, C's two "
                "and D's three. Improve every soil to 2, 4, 7 and 10 quarters and the price "
                "halves to 30s, while the total rises to 450s.",
            ],
        },
        "quiz_title": "Four soils and their rents",
        "quiz": [
            {"q": "Three soils each take a capital of 100s at a 20% profit and yield 2, 3 and 5 "
                  "quarters. All three are needed. What is the rent of the best soil?",
             "a": ["180s", "240s", "120s", "300s"],
             "c": 0,
             "why": "The worst soil sets the price: `120 / 2 = 60`s a quarter. The best soil's "
                    "5 quarters fetch 300s against its 120s, a rent of 180s. 240s forgets the "
                    "profit; 120s is the middle soil's figure at 60s plus nothing for it; 300s "
                    "is its whole product."},
            {"q": "In the improved preset the price falls from 60s to 30s. What happens to the "
                  "total rent?",
             "a": ["It halves, to 180s",
                   "It rises, to 450s",
                   "It stays at 360s",
                   "It falls to nothing, because A now pays its way"],
             "c": 1,
             "why": "The better soils improved more than A, so their surplus quarters grew "
                    "faster than the price fell: B 2, C 5, D 8 extra quarters at 30s make 450s. "
                    "A paid no rent before either; halving assumes the extra quarters are "
                    "unchanged."},
            {"q": "On Marx's account, what is the premise of differential rent?",
             "a": ["A progress from better to ever worse soil",
                   "A falling productivity of agriculture",
                   "The inequality of the soils in use",
                   "A rising price of corn"],
             "c": 2,
             "why": "Marx says its premise &ldquo;is merely the inequality of the different "
                    "kinds of soil&rdquo;. The first two are what he calls the &ldquo;primitive "
                    "misconception&rdquo; of West, Malthus and Ricardo, and the improved preset "
                    "has rent rising while the price of corn falls."},
            {"q": "In Table I, ten quarters that cost 240s to produce sell for 600s. Where do "
                  "the other 360s go?",
             "a": ["To the farmers on the better soils as extra profit",
                   "To the landowners of B, C and D as rent",
                   "To the farmer on A, who regulates the price",
                   "Nowhere; the 600s is a nominal figure"],
             "c": 1,
             "why": "Competition among farmers for the better land turns their surplus profit "
                    "into rent, which is the chapter's whole assumption. The farmer on A gets "
                    "only his 60s, and the 600s is what the crop actually fetches."},
        ],
        "mistakes": [
            ("Thinking rent arises because cultivation must move to ever worse land",
             "This is the reading of West, Malthus and Ricardo, and it fits the case of a "
             "growing country with given methods. Marx's tables show it is not required. In "
             "the improved preset every soil gets better, the price halves from 60s to 30s, and "
             "total rent still rises from 360s to 450s. What rent needs is that the soils in "
             "use are unequal."),
            ("Thinking the worst soil's farmer pays rent too",
             "In this chapter A's farmer just covers his capital and the average profit, and "
             "has nothing over. Whether the worst soil pays anything at all is the question of "
             "absolute rent, which Marx takes up in Chapter 45 and shows does not change any "
             "of these differences."),
            ("Confusing rent per acre with total rent",
             "Marx's later tables in the chapter double or triple the acres of each soil. Total "
             "rent grows with the area, but the average rent per acre can fall if the new "
             "acres are mostly on A and B. The rent of each soil, per acre, is what these "
             "presets compute."),
        ],
        "standard": (
            "Finish when you can compute the rents on a set of soils of unequal fertility.",
            "Given soils with equal capitals, their outputs and the average rate of profit, "
            "compute the regulating price per quarter, the rent on each soil and the total "
            "rent, and say how they change when the worst soil is replaced or every soil "
            "improves."
        ),
        "note": (
            "The lab assumes the market needs every soil listed, so the least productive sets "
            "the price; Marx assumes the same. His 20% profit, 50s capitals and yields are "
            "his own, and he says they are &ldquo;arbitrarily chosen, but the assumptions are "
            "quite rational&rdquo;. Location, which he says can outweigh fertility, is left "
            "out here as he leaves it out; and the lab takes the Kerr text's yields as the "
            "authority where the text's totals disagree with them."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Kerr vol. 3, l. 5823 (DR II a different expression of DR I). Inline:
    # l. 5795 (the same result on one acre), l. 5799 (long leases),
    # l. 5801 (intensive cultivation), l. 5825 (4, 3, 2, 1 on one acre D),
    # l. 5833 (10-2 = 8 quarters, 12 pounds), l. 5835 (Ricardo onesided),
    # l. 5851 (Ricardo's only case).
    {
        "slug": "differential-rent-ii",
        "title": "Differential Rent II",
        "module": "Chapter 40 · The Second Form of Differential Rent",
        "one_line": "Capitals laid one after another on the same field, with unequal results, make surplus profits by the same rule as equal capitals on different fields.",
        "summary": (
            "Differential rent II comes from successive investments of capital on the same "
            "land. Compute the rent on one acre that takes four doses of capital yielding 4, "
            "3, 2 and 1 quarters, and compare it with Marx's four soils side by side: the "
            "same surplus profits, the same 360 shillings. Then see what is different, which "
            "is not the rule but how the surplus becomes rent."
        ),
        "key": [
            "DR II: successive capitals on one field",
            "price set by the least productive dose",
            "D: 4, 3, 2, 1 quarters on 50s: rent 360s",
            "same 360s as A–D side by side",
            "harder to fix in a lease than DR I",
        ],
        "key_label": "The second form in five lines",
        "concepts_intro": (
            "Chapter 40 asks whether it matters that capitals are laid on the same acre rather "
            "than on different acres, and answers twice: not for the surplus profit, a great "
            "deal for the rent."
        ),
        "concepts": [
            ("Differential rent II",
             "Surplus profit from successive investments of capital on the same land with "
             "unequal results, measured against the least productive investment the market "
             "needs. Marx's name for concentrating capital on one piece of land is intensive "
             "cultivation."),
            ("The same rule",
             "Each dose of capital earns, at the regulating price, its output less its capital "
             "and profit. Whether the doses lie side by side or on top of one another does not "
             "change the sums."),
            ("The lease",
             "A rent is fixed when the lease is signed. Surplus profits from capital the "
             "tenant adds afterwards stay with him until the lease ends, which is why tenants "
             "fought for long leases and landlords for short ones."),
        ],
        "read_title": "The passage first, then the one acre",
        "read_intro": (
            "The passage is Marx's verdict on the two forms. He reaches it by laying Table I's "
            "four capitals on a single acre."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 40.</strong> &ldquo;It is evident, in that case, "
                  "that differential rent No. II is but a different expression of differential "
                  "rent No. I, but that it coincides with it in substance.&rdquo;"),
            ("p", "Think of the difference between farming more land and farming the same land "
                  "harder. A farmer with more money can rent the next field, or he can put more "
                  "manure, labour and machinery on the field he has. The first is how the last "
                  "lesson's rent arose; the second is this chapter's, and Marx says it is the "
                  "one that grows as capitalist agriculture develops. He defines intensive "
                  "cultivation, &ldquo;economically&rdquo;, as &ldquo;the concentration of "
                  "capital upon the same piece of land, instead of its distribution over "
                  "adjoining pieces of land&rdquo;."),
            ("p", "His test is direct. Take Table I's capital of £10, in four portions of £2½, "
                  "and instead of spreading it over one acre each of A, B, C and D, lay it "
                  "successively on one acre of D, so that the first portion yields 4 quarters, "
                  "the second 3, the third 2 and the fourth 1. (Marx reckons this chapter in "
                  "pounds: £2½ is 50 shillings and a price of £3 a quarter is 60s. The lab keeps "
                  "shillings so the tables line up.) The last portion, yielding 1 quarter, "
                  "regulates the price at 60s, as A did. The others earn surplus profits of "
                  "180s, 120s and 60s. That is the same-acre preset: a price of 60s a quarter and "
                  "a rent of 360s on the one acre, the very total of the side-by-side preset, "
                  "which is Table I again. &ldquo;The formation of the surplus profits would be "
                  "the same as in Table I.&rdquo;"),
            ("p", "The second-on-d preset is the case in between. All four soils are farmed "
                  "with one capital each, and D takes a second 50s that yields 3 quarters. A "
                  "still regulates at 60s; D's first dose pays 180s and its second 120s, and the "
                  "total rent rises from 360s to 480s with no change of price. Marx also lets D's "
                  "second dose yield only 1 quarter, like A: then it is &ldquo;a rentless "
                  "investment&rdquo;, it earns the average profit and no more, and nothing "
                  "changes for anyone."),
            ("def", ("Differential rent II",
                     "The rent that arises from successive investments of capital on the same "
                     "land with unequal productivity. Its surplus profits follow the same rule "
                     "as differential rent I, measured against the least productive investment "
                     "the market needs.")),
            ("p", "If the sums are the same, what is different? The conversion into rent. On "
                  "separate fields a landowner can see what each acre yields and set the rent "
                  "by it. On one field, capital added during a lease earns its surplus for the "
                  "tenant: &ldquo;the rent is fixed when the lease for the land is made "
                  "out&rdquo;, and only at renewal can the landlord claim it. Hence, Marx says, "
                  "English tenants resisted official farm statistics, fought for long leases, "
                  "and landlords preferred tenancies that could be ended every year. The "
                  "valuer who assesses rents becomes, under intensive cultivation, "
                  "&ldquo;a very important, complicated and difficult profession&rdquo;."),
            ("p", "Then Marx turns the combination round, and here the manuscript stumbles. "
                  "Suppose D's four doses yield 4, 1, 3 and 2 quarters and their product throws "
                  "A out of use, so that B regulates at £1½, 30s a quarter. Marx reckons D's "
                  "rent as &ldquo;10-2 = 8 quarters, at 1½ pounds sterling per quarter, or 12 "
                  "pounds sterling&rdquo;. But that sets D's ten quarters from four doses against "
                  "B's two quarters from one. Valued dose by dose at 30s, D's ten quarters fetch "
                  "300s against four doses' 240s of cost and profit: a rent of 60s, or £3, and "
                  "the dose that yields 1 quarter does not even cover its costs. The point Marx "
                  "wanted, that the regulating price can fall while rent on the better land "
                  "rises, is sound, and the next two lessons compute it properly."),
            ("p", "The chapter's quarrel is again with Ricardo, who made differential rent II "
                  "one case only: additional capital on land already farmed, with diminishing "
                  "returns, so that the price of corn rises, wages rise with it, profits fall "
                  "and rents climb. That is a real case, and Marx keeps it, but he says it "
                  "&ldquo;has been stamped by Ricardo as the only case, the normal case&rdquo;. "
                  "With the price constant, extra capital at a falling but still positive "
                  "surplus raises rent without touching price or profit; with more productive "
                  "doses, the price can fall. The chapter sorts these into the three cases the "
                  "next three lessons read."),
            ("p", "Ricardo's case has a defender in every later textbook, under the name of "
                  "diminishing returns: add more of one input to a fixed amount of land and each "
                  "addition yields less. What the chapter says bears on it directly: most of Marx's own doses "
                  "diminish, and the price still does not move, because it is set by the least "
                  "productive investment the market needs, not by the last one made on the best "
                  "field."),
            ("p", "The doses here all leave the price where it was. The next lesson, "
                  "“Differential Rent II at a Constant Price of Production”, keeps it there on "
                  "purpose and asks what happens to the rent per acre."),
        ],
        "lab": ("capkit", {
            "mode": "rent",
            "view": "dr2",
            "money_unit": "s",
            "qty_unit": "quarter",
            "preset": "side-by-side",
            "presets": [
                {"id": "side-by-side", "label": "Marx's Table I: one 50s capital on each of A, B, C, D",
                 "soils": [{"name": "A", "capital": 50, "outputs": [1]},
                           {"name": "B", "capital": 50, "outputs": [2]},
                           {"name": "C", "capital": 50, "outputs": [3]},
                           {"name": "D", "capital": 50, "outputs": [4]}],
                 "profit_rate": "1/5", "regulating": "auto", "expect": {"rtPrice": "60s a quarter", "rtRents": "0s, 60s, 120s, 180s", "rtTotal": "360s"}},
                {"id": "same-acre", "label": "Marx's figures: four 50s doses on one acre of D, yielding 4, 3, 2, 1",
                 "soils": [{"name": "D", "capital": 50, "outputs": [4, 3, 2, 1]}],
                 "profit_rate": "1/5", "regulating": "auto", "former_price": 60, "expect": {"rtPrice": "60s a quarter", "rtRents": "360s", "rtTotal": "360s"}},
                {"id": "second-on-d", "label": "A, B, C, D, with a second 50s on D yielding 3 quarters",
                 "soils": [{"name": "A", "capital": 50, "outputs": [1]},
                           {"name": "B", "capital": 50, "outputs": [2]},
                           {"name": "C", "capital": 50, "outputs": [3]},
                           {"name": "D", "capital": 50, "outputs": [4, 3]}],
                 "profit_rate": "1/5", "regulating": "auto", "expect": {"rtPrice": "60s a quarter", "rtRents": "0s, 60s, 120s, 300s", "rtTotal": "480s"}},
            ],
            "panel_title": "Doses of capital on one field",
            "panel_intro": (
                "Each soil's capital per dose and the output of each dose go in. The least "
                "productive dose in use sets the price; each soil's rent sums its doses' "
                "surplus profits. Compare side-by-side with same-acre: four fields or one, the "
                "rent is 360s."
            ),
        }),
        "steps_title": "Computing rent from successive doses",
        "steps_intro": "Four steps, for any field that takes several equal doses of capital.",
        "steps": [
            ("List the doses",
             "Write each dose of capital on each soil with its own output. A soil with three "
             "doses is three rows."),
            ("Price each dose",
             "Divide each dose's capital plus the average profit by its output. The highest "
             "figure among the doses the market needs is the regulating price."),
            ("Compute each dose's surplus",
             "Value each dose's output at the regulating price and subtract its capital and "
             "profit. A dose that only covers them has no surplus; one that cannot cover them "
             "is not worth making at that price."),
            ("Add per soil",
             "The rent of a field is the sum of its doses' surpluses, to be claimed by the "
             "landowner when the lease is renewed."),
        ],
        "worked": {
            "title": "One acre of D, four doses",
            "intro": [
                "One acre of D takes four doses of 50 shillings at a 20% profit, yielding 4, 3, "
                "2 and 1 quarters. You want the price and the acre's rent.",
            ],
            "lines": [
                "cost and profit:  60 shillings a dose",
                "price:  60 / 1 = 60 shillings (the 4th dose)",
                "doses 1 to 3:  (4 + 3 + 2) · 60 − 3 · 60 = 360",
                "dose 4:  1 · 60 − 60 = 0",
                "rent of the acre:  360 shillings",
            ],
            "after": [
                "The same 360s as one capital each on A, B, C and D. Marx's conclusion: the "
                "second form is &ldquo;a different expression&rdquo; of the first, and differs "
                "in how the surplus is turned into rent.",
            ],
        },
        "quiz_title": "One field, several capitals",
        "quiz": [
            {"q": "A field takes three doses of 50s at a 20% profit, yielding 3, 2 and 1 "
                  "quarters, and the last dose regulates the price. What is the field's rent?",
             "a": ["180s", "360s", "120s", "240s"],
             "c": 0,
             "why": "The price is `60 / 1 = 60`s. The doses fetch `6 · 60 = 360`s against "
                    "`3 · 60 = 180`s of cost and profit, leaving 180s. 360s is the whole "
                    "product; 120s counts only the first dose's surplus; 240s forgets the "
                    "profit on the capital."},
            {"q": "In the second-on-d preset, D's second dose yields 3 quarters and A still "
                  "regulates the price. What happens to the price and the total rent?",
             "a": ["The price falls and the rent falls",
                   "The price stays at 60s and the total rent rises to 480s",
                   "The price rises, because D's second dose is less productive than its first",
                   "Nothing changes, because the second dose is less productive"],
             "c": 1,
             "why": "The second dose yields 3 quarters for 60s of cost and profit, so at 60s it "
                    "makes 120s of surplus and the total goes from 360s to 480s. It is less "
                    "productive than D's first dose but more productive than A, which still "
                    "sets the price."},
            {"q": "On Marx's account, what is different about differential rent II?",
             "a": ["Its surplus profits follow a different law",
                   "It needs a rising price of corn",
                   "The surplus is harder for the landowner to fix as rent during a lease",
                   "It arises only on the worst soil"],
             "c": 2,
             "why": "Marx says it is &ldquo;immaterial for the law forming the surplus "
                    "profit&rdquo; but makes &ldquo;a considerable difference for the conversion "
                    "of surplus profit into ground-rent&rdquo;. A rising price is Ricardo's one "
                    "case, which Marx refuses to make the rule, and doses on better soils pay "
                    "rent too."},
        ],
        "mistakes": [
            ("Thinking DR II is a different source of rent from DR I",
             "Laying capital on the same field sounds like a different thing from farming more "
             "fields. Marx's test is the same-acre preset: Table I's four capitals laid on one "
             "acre of D with yields of 4, 3, 2 and 1 make exactly the surpluses of A, B, C and "
             "D side by side, 360s in all. The rule is one; what differs is how the landowner "
             "gets hold of the surplus."),
            ("Thinking diminishing returns must raise the price",
             "D's doses yield less and less, and the price does not move, because it is set by "
             "the least productive investment the market needs. Only when added capital is "
             "less productive than that, and needed, does the price rise; Ricardo made this one "
             "case the rule."),
            ("Reading Marx's 12 pounds as a correct rent",
             "In the case where B regulates at £1½, the text sets D's ten quarters from four "
             "doses against B's two from one. Dose by dose the rent is £3, and one of the doses "
             "cannot cover its costs at that price. The manuscript's point survives; the "
             "figure does not."),
        ],
        "standard": (
            "Finish when you can compute rent from successive doses on one field.",
            "Given the doses of capital on each soil, their outputs and the average rate of "
            "profit, compute the regulating price, each soil's rent and the total, and show "
            "that the same capitals spread over separate soils give the same surplus profits."
        ),
        "note": (
            "The lab values every dose separately at the regulating price, as Marx does in "
            "this chapter. A farmer knows only the yield of the whole acre, and Chapter 43 "
            "says the separate doses must first be &ldquo;reconverted&rdquo; by averaging "
            "before a landlord can set a rent; the lab does not average. The second-on-d "
            "preset's 3 quarters are illustrative; the other figures are Marx's."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Kerr vol. 3, l. 5917 (the law: rent increases absolutely). Inline:
    # l. 5878 (Table II: doubled capital, £6, £12, £18; total 36),
    # l. 5884-5888 (Table III: 3½, 5, 6 quarters; D from three quarters to
    # five, £9 to £15), l. 5919 (90% against 120%), l. 5938 (two countries).
    # Tables: Kerr p. 800 (Ch. 40's second investments: rents £1½, £3, £6),
    # p. 802 (Table II), p. 803 (Table III: D 4 + 3½ = 7½, rent £16½, total £30).
    {
        "slug": "dr-ii-constant-price",
        "title": "Differential Rent II at a Constant Price of Production",
        "module": "Chapter 41 · Differential Rent II—First Case: Constant Price of Production",
        "one_line": "While the worst soil still sets the price, every extra dose of capital on a better soil that beats the worst soil's yield raises the rent per acre, even when it yields less than the dose before.",
        "summary": (
            "The first case of differential rent II keeps the regulating price fixed: soil A "
            "still sets it. Compute the rents when every soil takes a second capital as "
            "productive as the first, a less productive one and a more productive one, and see "
            "that the rent per acre rises in all three while the rent per pound of capital may "
            "fall."
        ),
        "key": [
            "A still regulates: the price stays 60s",
            "proportional doses: rent doubles per acre",
            "less productive doses: rent still rises",
            "rate of rent can fall as rent per acre rises",
            "concentrated capital, dearer land",
        ],
        "key_label": "The first case in five lines",
        "concepts_intro": (
            "Chapter 41 is short and has one law. It distinguishes three things that move "
            "differently: rent per acre, rent per pound of capital, and total rent."
        ),
        "concepts": [
            ("Rent per acre",
             "The rent a fixed piece of land pays. Under differential rent II it rises with the "
             "capital laid on the land, as long as each new dose beats the regulating soil's "
             "yield."),
            ("Rate of rent",
             "Rent divided by the capital invested. It can stay the same or fall while the "
             "rent per acre rises, because the capital per acre is growing."),
            ("The constant-price case",
             "The worst soil A goes on supplying part of the market and so goes on regulating "
             "the price. Added capital on the better soils changes the rents but not the "
             "price."),
        ],
        "read_title": "The law first, then three ways of adding capital",
        "read_intro": (
            "The passage is the law the chapter states after its third case. The first case, "
            "doses that do no better than A, takes a sentence: nothing changes."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 41.</strong> &ldquo;But this is the law: That "
                  "the rent increases absolutely upon all these classes of soil, although not in "
                  "proportion to the additional capital invested.&rdquo;"),
            ("p", "When a farmer adds capital to his field and the price of corn does not move, "
                  "who gains? The chapter's answer is the landowner, at the next lease, and it "
                  "takes Marx four cases to show how much. If the added capital on B, C or D "
                  "yields only what the same capital yields on A, it earns the average profit and "
                  "nothing more: &ldquo;Everything remains as it is.&rdquo; It is as if more acres "
                  "of A had been ploughed. The other cases are the lab's three presets. All are "
                  "reckoned, as before, at 50s a dose (Marx's £2½) and 60s a quarter (his £3)."),
            ("p", "First, the proportional preset, Marx's Table II. Every soil takes a second "
                  "capital exactly as productive as its first: A yields 1 and 1, B 2 and 2, C 3 "
                  "and 3, D 4 and 4. A still regulates at 60s. The rents double: B pays 120s, C "
                  "240s, D 360s, and the total is 720s, Marx's &ldquo;total rental of 36&rdquo; "
                  "pounds. The rent per acre has doubled, and so has the price of the land, "
                  "&ldquo;in which this rent is capitalised&rdquo;. The rate of rent has not "
                  "moved: 720s on 400s of capital is the same 180% as 360s on 200s."),
            ("p", "Second, the slower preset, Marx's Table III on page 803, where the second "
                  "doses are less productive than the first but still beat A. B's second dose "
                  "yields 1½ quarters, C's 2, D's 3½. At 60s, B's rent goes from 60s to 90s, C's "
                  "from 120s to 180s, D's from 180s to 330s, and the total is 600s, the table's "
                  "£30. The rate of rent has "
                  "fallen; on B, Marx says, the surplus is now 90% of the capital where it was "
                  "120% on the first dose alone. But the rent per acre is higher on every soil. "
                  "That is the law in the passage: rent rises &ldquo;absolutely&rdquo;, though "
                  "&ldquo;not in proportion to the additional capital invested&rdquo;."),
            ("p", "A word on D, because the text gives it three different yields. Chapter 40, "
                  "which first sketches this case, lists the doubled yields as &ldquo;B would "
                  "raise only 3½ quarters, C, 5 quarters, and D, 6 quarters&rdquo;, but goes on "
                  "to say that D's second dose pays &ldquo;two quarters instead of three&rdquo; "
                  "and that D's rent rises &ldquo;from three quarters to five (from 9 pounds "
                  "sterling to 15 pounds sterling)&rdquo;, and its table on page 800 gives that "
                  "dose a rent of £6. A second dose that pays 2 quarters of rent must yield 3, "
                  "so Chapter 40's D has 7 quarters, not 6. Chapter 41's Table III then gives "
                  "D's second dose 3½ quarters, a total of 7½ and a rent of £16½. The lab "
                  "follows Table III, the table this chapter computes with."),
            ("p", "Third, the faster preset: the second doses yield more than the first, 3 on "
                  "B, 4 on C, 5 on D. Marx gives no figures for this case, so these are "
                  "illustrative, and he says it &ldquo;requires no further analysis&rdquo;: the "
                  "rent per acre rises faster than the capital. Here it is 180s, 300s and 420s, "
                  "900s in all. He adds a distinction that matters later. Producing twice the "
                  "product with the same capital is not the same as producing it with twice the "
                  "capital: the first releases capital, the second has to find it."),
            ("def", ("Rent per acre and rate of rent",
                     "Rent per acre is rent divided by the land; the rate of rent is rent "
                     "divided by the capital invested in it. Under differential rent II at a "
                     "constant price the first rises with every dose that beats the regulating "
                     "soil, while the second may stay level or fall.")),
            ("p", "The consequence Marx draws is about countries. Take two with the same "
                  "prices, the same soils and the same capital in farming, but in one the "
                  "capital is concentrated on a smaller area and in the other spread over a "
                  "wider one. The total rent can be the same in both, yet the rent per acre, and "
                  "with it the price of land, is higher in the first. The difference "
                  "&ldquo;could not be explained&rdquo; by the soil, he says, &ldquo;but solely "
                  "out of the different ways in which the capital is invested&rdquo;. As "
                  "capitalist farming concentrates capital, rents per acre and land prices "
                  "rise."),
            ("p", "This is where a reader who knows diminishing returns will push back. Each "
                  "added dose on B yields less; surely the farmer stops adding at some point? "
                  "He does, and the chapter puts the limit in the same place: he stops where a dose would yield no more than the "
                  "same capital on A, because beyond that it no longer pays the average profit at "
                  "the regulating price. Up to that point every dose, however much smaller its "
                  "yield, raises the rent per acre. The stopping point is "
                  "the same on both accounts; what the surplus before it is, is where they "
                  "part."),
            ("p", "Here the price never moved because A stayed in use. The next lesson, "
                  "“Differential Rent II at a Falling Price of Production”, lets the added "
                  "capital supply so much that A is no longer needed."),
        ],
        "lab": ("capkit", {
            "mode": "rent",
            "view": "dr2",
            "money_unit": "s",
            "qty_unit": "quarter",
            "price_case": "constant",
            "preset": "proportional",
            "presets": [
                {"id": "proportional", "label": "Marx's Table II: every soil's capital doubled at the same yield",
                 "soils": [{"name": "A", "capital": 50, "outputs": [1, 1]},
                           {"name": "B", "capital": 50, "outputs": [2, 2]},
                           {"name": "C", "capital": 50, "outputs": [3, 3]},
                           {"name": "D", "capital": 50, "outputs": [4, 4]}],
                 "profit_rate": "1/5", "regulating": "auto", "expect": {"rtPrice": "60s a quarter", "rtRents": "0s, 120s, 240s, 360s", "rtTotal": "720s"}},
                {"id": "slower", "label": "Marx's Table III: second doses yield 1½, 2 and 3½ quarters on B, C, D",
                 "soils": [{"name": "A", "capital": 50, "outputs": [1]},
                           {"name": "B", "capital": 50, "outputs": [2, "3/2"]},
                           {"name": "C", "capital": 50, "outputs": [3, 2]},
                           {"name": "D", "capital": 50, "outputs": [4, "7/2"]}],
                 "profit_rate": "1/5", "regulating": "auto", "expect": {"rtPrice": "60s a quarter", "rtRents": "0s, 90s, 180s, 330s", "rtTotal": "600s"}},
                {"id": "faster", "label": "Second doses yield more: 3, 4 and 5 quarters on B, C, D",
                 "soils": [{"name": "A", "capital": 50, "outputs": [1]},
                           {"name": "B", "capital": 50, "outputs": [2, 3]},
                           {"name": "C", "capital": 50, "outputs": [3, 4]},
                           {"name": "D", "capital": 50, "outputs": [4, 5]}],
                 "profit_rate": "1/5", "regulating": "auto", "expect": {"rtPrice": "60s a quarter", "rtRents": "0s, 180s, 300s, 420s", "rtTotal": "900s"}},
            ],
            "panel_title": "A second capital on every soil",
            "panel_intro": (
                "Each soil's doses and their outputs go in; soil A, with the least productive "
                "dose, keeps the price at 60s. Compare proportional with slower: the second "
                "doses yield less, and every soil's rent still rises above Table I's."
            ),
        }),
        "steps_title": "Adding capital at a constant price",
        "steps_intro": "Four steps, while the regulating soil stays in use.",
        "steps": [
            ("Check the regulator",
             "Confirm that the least productive dose in use is still the worst soil's, so the "
             "price is unchanged."),
            ("Value each new dose",
             "At the unchanged price, each added dose earns its output less its capital and "
             "profit. A dose that yields no more than the regulating soil earns nothing extra."),
            ("Add per acre",
             "Each soil's rent is the sum over its doses. Compare it with the rent before the "
             "doses were added."),
            ("Compare with the capital",
             "Divide the rent by the capital on the soil for the rate of rent, and set it "
             "beside the rent per acre. The first may fall while the second rises."),
        ],
        "worked": {
            "title": "Marx's soil B, two doses",
            "intro": [
                "Soil B takes a first dose of 50 shillings yielding 2 quarters and a second "
                "yielding 1½, while A keeps the price at 60s a quarter. You want B's rent before "
                "and after, and its rate of rent.",
            ],
            "lines": [
                "first dose:  2 · 60 − 60 = 60 shillings",
                "second dose:  (3/2) · 60 − 60 = 30 shillings",
                "rent per acre:  60 → 90 shillings",
                "rate of rent:  60/50 = 120% → 90/100 = 90%",
            ],
            "after": [
                "The rent per acre rose by half while the rate of rent fell by a quarter: "
                "Marx's 120% and 90%, and his £3 and £4½.",
            ],
        },
        "quiz_title": "Rent per acre at a constant price",
        "quiz": [
            {"q": "At a price of 60s a quarter, a soil's first dose of 50s at 20% yields 3 "
                  "quarters and its second 2. What is the soil's rent?",
             "a": ["120s", "180s", "240s", "60s"],
             "c": 1,
             "why": "The first dose makes `3 · 60 − 60 = 120`s and the second `2 · 60 − 60 = "
                    "60`s, so 180s. 120s is the first dose alone, 60s the second alone, and "
                    "240s leaves out one dose's cost."},
            {"q": "In the slower preset, the second doses yield less than the first. What "
                  "happens to the rent per acre on B, C and D compared with Table I?",
             "a": ["It falls on every soil",
                   "It rises on every soil",
                   "It stays the same, because the price has not changed",
                   "It rises on D and falls on B"],
             "c": 1,
             "why": "Each second dose still beats A's 1 quarter, so it adds a surplus: B goes "
                    "from 60s to 90s, C from 120s to 180s, D from 180s to 330s. That is Marx's "
                    "law, rent rising &ldquo;absolutely&rdquo;."},
            {"q": "In Marx's Table II every soil's capital is doubled at the same productivity. "
                  "What happens to the rate of rent, rent divided by capital?",
             "a": ["It doubles", "It halves", "It stays the same", "It falls to zero"],
             "c": 2,
             "why": "Rent and capital both double: 720s on 400s is the same 180% as 360s on "
                    "200s. It is the rent per acre that doubles, because the acre is a fixed "
                    "measure."},
            {"q": "A second dose on soil C yields exactly 1 quarter, the same as A's dose. What "
                  "does it add to C's rent?",
             "a": ["60s", "Nothing", "One quarter", "It lowers C's rent by 60s"],
             "c": 1,
             "why": "At 60s its quarter just pays its 50s and the 10s of profit. Marx: "
                    "&ldquo;the effect upon the rent is nil&rdquo;, as if another acre of A had "
                    "been ploughed. It neither adds nor subtracts."},
        ],
        "mistakes": [
            ("Thinking more output always lowers rent per acre",
             "More corn, one expects, means cheaper corn and lower rents. At a constant price "
             "it does not: in the slower preset every second dose yields less than the first, "
             "and B's rent still goes from 60s to 90s, D's from 180s to 330s, because each dose "
             "beats the regulating soil. More output lowers rents only when it lowers the "
             "price, which is the next lesson's case."),
            ("Confusing rent per acre with the rate of rent",
             "In Table II the rent per acre doubles and the rate of rent does not change; in "
             "Table III the rent per acre rises and the rate falls. Say which one a figure "
             "is: land prices follow the first."),
            ("Taking Chapter 40's 6 quarters for D at face value",
             "Chapter 40 gives D a total of 6 quarters but a second-dose rent of 2 quarters and "
             "a total rent of 5, which need 7 quarters; with 6, D's rent would be 240s, not the "
             "£15 the text states twice. Chapter 41's Table III gives 7½. Say which table a "
             "figure for D comes from."),
        ],
        "standard": (
            "Finish when you can compute the rents after adding capital at a constant price.",
            "Given each soil's doses of capital, their outputs and an unchanged regulating "
            "soil, compute each soil's rent and the total, and compare the rent per acre and "
            "the rate of rent with the rents before the capital was added."
        ),
        "note": (
            "The constant price is an assumption the lab checks: if a preset's doses changed "
            "the regulating investment, the banner would say the figures have left this "
            "case. The faster preset's yields are illustrative; the other two are Marx's "
            "Tables II and III, checked against the printed tables on pages 802 and 803."
        ),
    },
    # ---------------------------------------------------------------- 06
    # Kerr vol. 3, l. 5990 (rental the same, price halved). Inline: l. 5956
    # (18 quarters; "D and its price of production of 30 shillings"),
    # l. 5958 (36 to 9 pounds), l. 5966-5978 (IV a, IV b), l. 5992-5994
    # (IV c, IV d), l. 6006-6008 (44 quarters on D; 36 pounds again),
    # l. 6016 (grain rent a tradition), l. 6271 (Engels: prairies).
    {
        "slug": "dr-ii-falling-price",
        "title": "Differential Rent II at a Falling Price of Production",
        "module": "Chapter 42 · Differential Rent II—Second Case: Falling Price of Production",
        "one_line": "When added capital on the better soils supplies enough to make the worst soil unnecessary, the price falls, and total rent can fall, hold or rise depending on how much capital goes where.",
        "summary": (
            "In the second case the added capital is so productive in total that soil A drops "
            "out and B sets a lower price. Compute Marx's tables in which A drops out and rent "
            "falls by three-quarters, in which the total rent of Table I returns at half the "
            "price, and in which it doubles at half the price, and see why a falling price "
            "decides nothing on its own."
        ),
        "key": [
            "A drops out: B regulates at 30s",
            "Table IV: rent 180s, a quarter of 720s",
            "IV d: 360s again at half the price",
            "44 quarters on D: 720s at half the price",
            "price falls; rent may fall, hold or rise",
        ],
        "key_label": "The second case in five lines",
        "concepts_intro": (
            "Chapter 42 is the longest run of tables in the Part. Its argument is short: a "
            "falling price does not settle what happens to rent, and it shows why with "
            "Marx's own soils."
        ),
        "concepts": [
            ("A new regulator",
             "When the better soils' added doses supply the market without A, A's capital is "
             "withdrawn and B, the next soil up, sets the price. B now pays no rent, as A did "
             "before."),
            ("Two opposing movements",
             "The regulating price falls, which lowers each surplus quarter's money value; the "
             "surplus quarters multiply, which raises it. Total rent moves with whichever is "
             "larger."),
            ("Grain rent and money rent",
             "Rent counted in quarters of wheat and rent counted in money. With the price "
             "halved, a grain rent must double for the money rent to hold, and Marx's tables "
             "track both."),
        ],
        "read_title": "Marx's comparison first, then the tables behind it",
        "read_intro": (
            "The passage is Marx's summary of the two tables he says matter most. The rest of "
            "the lesson builds them, and one that goes further."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 42.</strong> &ldquo;We find that the total money "
                  "rental has remained the same, namely 18 pounds sterling, while the price of "
                  "production has fallen by one-half, from 60 shillings to 30 shillings per "
                  "quarter, and that the grain rent has been correspondingly duplicated, from 6 "
                  "quarters to 12.&rdquo;"),
            ("p", "Begin from the last lesson's Table II: every soil with two equal doses, A "
                  "yielding 1 and 1, B 2 and 2, C 3 and 3, D 4 and 4, twenty quarters at 60s and "
                  "a rent of 720s. Now suppose the market wants only 18 quarters. The two "
                  "quarters A supplies are not needed; its capital is withdrawn, and the "
                  "least productive dose still in use is one of B's, at 60s for 2 quarters, or "
                  "30s a quarter. B pays no rent; C and D pay their extra quarters at 30s. The "
                  "a-drops-out preset, Marx's Table IV, gives the lab exactly that: all four soils "
                  "and a market of 18 quarters. It prints 30s a quarter, rents of 0s, 0s, 60s and "
                  "120s, and a total of 180s, Marx's fall &ldquo;from 36 pounds sterling to 9 "
                  "pounds sterling&rdquo;. A misprint on the way: the Kerr text says that "
                  "&ldquo;D and its price of production of 30 shillings&rdquo; would regulate. "
                  "It is B: D's price of production is 15s, and B's is the 30s the rest of the "
                  "chapter uses."),
            ("p", "So the price halved and the rent fell by three-quarters. But that is because "
                  "nothing was added to make up for A. Marx now lays more capital on the best "
                  "soils, at the same productivity per dose. A third dose on D, his Table IV b, "
                  "lifts the total to 240s. Two more on D, Table IV d, give D five doses and 20 "
                  "quarters: D's rent is 300s, C's 60s, and the total is 360s, the "
                  "&ldquo;18 pounds sterling&rdquo; of Table I, now at half the price and twice "
                  "the grain. That is the iv-d preset, and the passage above is about it."),
            ("p", "Marx does not stop there. If D took eleven doses, producing 44 quarters, "
                  "&ldquo;the total rental would once more reach the level of Table II&rdquo;: "
                  "54 quarters in all, a money rent of 720s, at 30s a quarter. The rent-rises "
                  "preset runs it; the lab takes six doses a soil at most, so D's eleven doses of 50s "
                  "go in as one capital of 550s yielding 44 quarters, the same 15s a quarter. "
                  "Marx's table on page 817 prints the money rents the lab does, £3 on C and "
                  "£33 on D; it gives C a grain rent of 3 quarters and a grain total of 25, where "
                  "£3 at 30s is 2 quarters and the total 24. "
                  "Compared with Table I, the price has halved and the money rent "
                  "has doubled; compared with Table II, the price has halved and the money rent "
                  "is the same."),
            ("p", "Why does this work? Because each dose on D yields 4 quarters where B's yields "
                  "2, so each D dose makes 2 surplus quarters, worth 60s at the new price. Halve "
                  "the price and you need twice the surplus quarters to keep the money rent; "
                  "Marx puts it in two clauses: &ldquo;The price of grain falls by 50%, the "
                  "surplus product increases by 100%.&rdquo; And the capital this takes is less, "
                  "the more of it goes to the best soil: Table IV c reaches the same 360s by "
                  "putting more of the extra capital on C, and needs 550s of capital where IV d "
                  "needs 450s."),
            ("def", ("The falling-price case",
                     "Added capital on the better soils supplies the market without the worst "
                     "soil, which drops out; the next soil sets a lower price. Total rent then "
                     "depends on how many surplus quarters the added capital creates against "
                     "how far the price falls.")),
            ("p", "Marx is ironic about the habit of counting rent in grain, &ldquo;merely due "
                  "to tradition&rdquo;: one might as well show that a manufacturer buys more of "
                  "his own yarn with £5 of profit than he used to with £10. The tables keep both "
                  "counts, and the lab prints money, because money is what the lease is written "
                  "in. The chapter goes on to the cases where the added doses diminish and where "
                  "they improve. With diminishing doses, his Table V on page 820 drops A and "
                  "gives B 2 and 1½ quarters, C 3 and 2, D 4 and 3½. It prices every quarter at "
                  "B's average, £6 for 3½ quarters or 1 5/7 pounds, and reaches a rent of 9 3/7 "
                  "pounds. The lab values each dose by itself, so it would let B's weaker second "
                  "dose, at £2 a quarter, set the price instead; it does not reproduce Table V."),
            ("p", "Engels, editing the volume in the 1890s, added a note to the next chapter "
                  "that reads like this one come true. American prairie, Argentine pampas and "
                  "the grain of Russian and Indian peasants forced to sell for their taxes "
                  "reached Europe by steamship and railway; a portion of Europe's soil "
                  "&ldquo;fell definitely out of the competition for the raising of "
                  "grain&rdquo;, and rents fell everywhere. That is the a-drops-out preset on a "
                  "continent: a falling price, with nothing added on the better land to make up "
                  "for it."),
            ("p", "The standard objection to these tables is that they are arithmetic, and Marx "
                  "says as much: his yields of 1, 2, 3 and 4 are chosen to make the sums easy, "
                  "and Engels complains they are so far apart that they &ldquo;lead to utterly "
                  "forced results&rdquo;. What the tables establish is a possibility, that the "
                  "same falling price is compatible with rent falling, holding or rising. Which "
                  "happened in a given country is a question of where the capital went, and the "
                  "tables cannot answer it."),
            ("p", "Here the price fell because the added doses were productive enough. The "
                  "next lesson, “Differential Rent II at a Rising Price of Production”, takes "
                  "doses so unproductive that the price must rise to call them forth."),
        ],
        "lab": ("capkit", {
            "mode": "rent",
            "view": "dr2",
            "money_unit": "s",
            "qty_unit": "quarter",
            "price_case": "falling",
            "preset": "a-drops-out",
            "presets": [
                {"id": "a-drops-out", "label": "Marx's Table IV: Table II's soils, a market of 18 quarters",
                 "soils": [{"name": "A", "capital": 50, "outputs": [1, 1]},
                           {"name": "B", "capital": 50, "outputs": [2, 2]},
                           {"name": "C", "capital": 50, "outputs": [3, 3]},
                           {"name": "D", "capital": 50, "outputs": [4, 4]}],
                 "profit_rate": "1/5", "regulating": "auto", "market_limit": 18, "expect": {"rtPrice": "30s a quarter", "rtRents": "0s, 0s, 60s, 120s", "rtTotal": "180s"}},
                {"id": "iv-d", "label": "Marx's Table IV d: five doses on D, a market of 30 quarters",
                 "soils": [{"name": "A", "capital": 50, "outputs": [1, 1]},
                           {"name": "B", "capital": 50, "outputs": [2, 2]},
                           {"name": "C", "capital": 50, "outputs": [3, 3]},
                           {"name": "D", "capital": 50, "outputs": [4, 4, 4, 4, 4]}],
                 "profit_rate": "1/5", "regulating": "auto", "market_limit": 30, "expect": {"rtPrice": "30s a quarter", "rtRents": "0s, 0s, 60s, 300s", "rtTotal": "360s"}},
                {"id": "rent-rises", "label": "Marx's figures: 44 quarters on D from 550s (his £27½), a market of 54",
                 "soils": [{"name": "A", "capital": 50, "outputs": [1, 1]},
                           {"name": "B", "capital": 50, "outputs": [2, 2]},
                           {"name": "C", "capital": 50, "outputs": [3, 3]},
                           {"name": "D", "capital": 550, "outputs": [44]}],
                 "profit_rate": "1/5", "regulating": "auto", "market_limit": 54, "expect": {"rtPrice": "30s a quarter", "rtRents": "0s, 0s, 60s, 660s", "rtTotal": "720s"}},
            ],
            "panel_title": "When the worst soil drops out",
            "panel_intro": (
                "Each soil's doses go in with the quantity the market takes. The lab supplies "
                "the market from the most productive doses first; the last one needed sets the "
                "price, and A's doses, not needed, earn nothing. Compare a-drops-out with "
                "rent-rises: the same 30s price, a quarter of the rent and then all of it."
            ),
        }),
        "steps_title": "Computing rent when the price falls",
        "steps_intro": "Four steps, when added capital makes the worst soil unnecessary.",
        "steps": [
            ("Rank the doses",
             "Price every dose: capital and profit divided by its output. Order them from "
             "cheapest to dearest."),
            ("Supply the market",
             "Take doses in that order until the market's quantity is reached. The last dose "
             "taken sets the new, lower price; doses not needed drop out."),
            ("Revalue every surplus",
             "Value each dose in use at the new price, less its capital and profit. Soils that "
             "paid rent before may now pay none."),
            ("Compare the totals",
             "Set the new total rent beside the old in money and in quarters: the price fell by "
             "a known proportion, and the surplus quarters changed by another."),
        ],
        "worked": {
            "title": "Marx's Table IV d",
            "intro": [
                "A is out of use; B takes two doses yielding 2 each, C two yielding 3 each, D "
                "five yielding 4 each, all at 50 shillings and 20%. You want the price and the "
                "total rent.",
            ],
            "lines": [
                "price:  60 / 2 = 30 shillings a quarter (B)",
                "C:  6 · 30 − 2 · 60 = 60",
                "D:  20 · 30 − 5 · 60 = 300",
                "total:  0 + 60 + 300 = 360 shillings",
                "in grain:  360 / 30 = 12 quarters",
            ],
            "after": [
                "Table I's money rent of 360s, or £18, at half its price and with twice its "
                "grain. Without the extra doses on D, Table IV, the same price gives only 180s.",
            ],
        },
        "quiz_title": "A falling price and the rent",
        "quiz": [
            {"q": "Soil A drops out and B, yielding 2 quarters for 60s of cost and profit, now "
                  "regulates. Soil D has three doses of 50s yielding 4 quarters each. What is D's "
                  "rent?",
             "a": ["180s", "360s", "540s", "120s"],
             "c": 0,
             "why": "The price is 30s. D's 12 quarters fetch 360s against `3 · 60 = 180`s of "
                    "cost and profit, leaving 180s. 360s is the whole product; 540s values it at "
                    "45s; 120s is two doses' surplus."},
            {"q": "In which preset does the total rent rise above Table I's 360s while the price "
                  "falls from 60s to 30s?",
             "a": ["a-drops-out", "iv-d", "rent-rises", "None of them"],
             "c": 2,
             "why": "With 44 quarters on D the total is 720s. In a-drops-out it falls to 180s, "
                    "and in iv-d it is exactly 360s again, held, not risen."},
            {"q": "The regulating price halves. What must happen to the surplus quarters for "
                  "the money rent to stay the same?",
             "a": ["They must halve", "They must stay the same", "They must double",
                   "They must rise by half"],
             "c": 2,
             "why": "Money rent is surplus quarters times price, so halving the price needs "
                    "twice the quarters: Marx's 6 quarters becoming 12."},
        ],
        "mistakes": [
            ("Thinking a falling price must lower total rent",
             "It is the natural inference: cheaper corn, smaller surpluses in money. Marx's "
             "tables show the price falling from 60s to 30s with the total rent falling to "
             "180s, holding at 360s and doubling to 720s, according to how much capital the "
             "better soils take. A falling price lowers what each surplus quarter is worth; the "
             "number of surplus quarters decides the rest."),
            ("Reading the Kerr text's &ldquo;D&rdquo; as the new regulator",
             "The text says D's price of production of 30s would regulate. D's is 15s; it is "
             "B, the worst soil left, whose 2 quarters for 60s give 30s. Everything that "
             "follows in the chapter uses B."),
            ("Thinking the soil dropped is lost to rent for good",
             "A pays no rent here because it is not needed, not because it cannot be farmed. "
             "Let demand rise past what the better soils supply and A comes back as the "
             "regulator at 60s, with every rent revalued at that price."),
        ],
        "standard": (
            "Finish when you can compute rents when the worst soil drops out.",
            "Given each soil's doses and outputs and the quantity the market takes, compute "
            "the new regulating price, each soil's rent and the total, and compare the total "
            "with the rent before the price fell."
        ),
        "note": (
            "The lab lets the market quantity decide which doses are used, cheapest first; "
            "Marx simply assumes A drops out. The presets are checked against his printed "
            "Tables IV, IV b and IV d and the table on page 817. Engels "
            "warned that yields of 1, 2, 3 and 4 exaggerate the differences between soils, so "
            "treat the size of the swings as illustrative and the direction as the point."
        ),
    },
]
