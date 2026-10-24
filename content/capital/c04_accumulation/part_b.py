"""Wages and Accumulation, lessons 6-9 -- Volume I, Chapters 24 and 25.

Every quotation is copied from /mnt/project-files/capital-texts/volume-1-kerr.txt
(the Kerr edition of Volume I); the comment beside each lesson gives its line
numbers. Footnote numerals are left out, a drop capital is printed as an
ordinary capital, and the translator's double quotation marks inside a
quotation are printed as single curly quotes. Nothing else is changed.
"""

LESSONS = [
    # ---------------------------------------------------------------- 06
    # Kerr vol. 1, l. 4445 (Moses and the prophets); l. 4315 (£2000 is
    # £2000); l. 4335 (Abraham begat Isaac); l. 4341 (not one single atom);
    # l. 4347 (the more he has accumulated); l. 4451 (Senior's abstinence).
    {
        "slug": "surplus-value-into-capital",
        "title": "Surplus Value into Capital",
        "module": "Chapter 24 · Conversion of Surplus-Value into Capital",
        "one_line": "Capitalise surplus value year after year and the original capital shrinks to a vanishing share of a capital made of surplus value.",
        "summary": (
            "Chapter 24 lets the capitalist add surplus value to his capital. Run Marx's "
            "spinner, £10,000 at four parts constant to one variable and a rate of surplus "
            "value of 100%, period by period, compute what share of the capital the original "
            "advance still is, and set the result against Senior's claim that capital is the "
            "reward of abstinence."
        ),
        "key": [
            "accumulation: s turned back into capital",
            "added capital splits into c and v",
            "£10,000 → £12,000: a sixth is capitalised s",
            "next capital = capital + share · s",
            "original share = first capital / present",
        ],
        "key_label": "Chapter 24 in five lines",
        "concepts_intro": (
            "Chapter 24 has five sections. The lesson follows the first and the third most "
            "closely, and the other three in the prose."
        ),
        "concepts": [
            ("Accumulation",
             "Employing surplus value as capital. The surplus value is sold for money and "
             "laid out again, in the same proportions as the original capital, in means of "
             "production and labour-power."),
            ("Capital out of capital",
             "The first additional capital presupposes the original advance. Every later one "
             "presupposes only earlier surplus value. &ldquo;The more the capitalist has "
             "accumulated, the more is he able to accumulate.&rdquo;"),
            ("Capital and revenue",
             "Surplus value is split between the capitalist's consumption and accumulation. "
             "Given its mass, the larger one share, the smaller the other, and the split is "
             "the capitalist's own act."),
        ],
        "read_title": "Marx at his most sardonic",
        "read_intro": (
            "The passage comes from the third section, after the story of the Manchester "
            "manufacturers. It is the chapter's summary in one line, and a joke at the "
            "expense of the economists who preached it."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 24, §3.</strong> &ldquo;Accumulate, "
                  "accumulate! That is Moses and the prophets! &lsquo;Industry furnishes the "
                  "material which saving accumulates.&rsquo; Therefore, save, save, i.e., "
                  "reconvert the greatest possible portion of surplus-value, or "
                  "surplus-product into capital! Accumulation for accumulation's sake, "
                  "production for production's sake: by this formula classical economy "
                  "expressed the historical mission of the bourgeoisie, and did not for a "
                  "single instant deceive itself over the birth-throes of wealth.&rdquo;"),
            ("p", "&ldquo;Moses and the prophets&rdquo; is scripture: the whole of the law. "
                  "Marx is mocking the economists who made accumulation a commandment, and "
                  "the line he quotes inside his own comes from Adam Smith. To see what the "
                  "commandment asks, go back to the start of the chapter, where Marx sets up "
                  "a spinner. He advances £10,000, four fifths of it, £8,000, in cotton and "
                  "machinery and one fifth, £2,000, in wages. At a rate of surplus value of "
                  "100% his yarn is worth £12,000, and £2,000 of it is surplus value. "
                  "&ldquo;£2000 is £2000. We can neither see nor smell in this sum of money "
                  "a trace of surplus-value.&rdquo;"),
            ("p", "To capitalise it, the spinner lays it out exactly as he laid out the "
                  "original: £1,600 in cotton and the like, £400 in more spinners. That "
                  "needs two things the market must already hold. The year's surplus product "
                  "must contain additional means of production and subsistence, and there "
                  "must be additional workers, which the working class supplies because its "
                  "wages keep it and let it increase. The circle of simple reproduction, in "
                  "Sismondi's word, becomes a spiral."),
            ("p", "<strong>Volume I, Chapter 24, §1.</strong> &ldquo;It is the old story: "
                  "Abraham begat Isaac, Isaac begat Jacob, and so on. The original capital "
                  "of £10,000 brings in a surplus-value of £2000, which is capitalised. The "
                  "new capital of £2000 brings in a surplus-value of £400, and this, too, is "
                  "capitalised, converted into a second additional capital, which, in its "
                  "turn, produces a further surplus-value of £80. And so the ball rolls "
                  "on.&rdquo;"),
            ("p", "The lab rolls the ball. Each period it lays out the whole capital at four "
                  "parts to one, takes a surplus value equal to the variable capital, and "
                  "adds the share of it you choose. In the marx preset, with all of it added, "
                  "the capital is £12,000 after the first year, and the original £10,000 is "
                  "`5/6` of it; the other sixth is capitalised surplus value. After five "
                  "years the capital is £24,883 4s and the original advance is about 40% of "
                  "it. Marx says that as production goes on the capital first advanced "
                  "becomes a vanishing quantity, <em>magnitudo evanescens</em>, beside the "
                  "capital accumulated. The half preset capitalises half and ends at £16,105 "
                  "2s, of which the original is 62.09%; the consume-all preset is simple "
                  "reproduction again, and the capital stays at £10,000."),
            ("p", "Where did the first £10,000 come from? &ldquo;By his own labour and that "
                  "of his forefathers,&rdquo; the economists answer, and Marx lets it stand "
                  "for now. The additional £2,000 is another matter: &ldquo;There is not one "
                  "single atom of its value that does not owe its existence to unpaid "
                  "labour.&rdquo; Every exchange along the way can be of equal values, the "
                  "workers paid in full for their labour-power, and still, Marx argues, the "
                  "laws of property based on one's own labour turn into their opposite: the "
                  "right to appropriate the unpaid labour of others."),
            ("p", "The second section corrects Smith and Ricardo, who held that the part of "
                  "revenue added to capital is consumed by productive labourers, so that "
                  "all accumulated surplus value becomes wages. Marx's spinner shows the "
                  "error in one line: of the £2,000, £1,600 goes into cotton and machinery. "
                  "Capitalised surplus value divides into constant and variable capital like "
                  "any other, and Smith's &ldquo;and so on&rdquo;, by which every purchase "
                  "of yarn and machinery eventually resolves into wages, is where Marx says "
                  "Smith broke off just as the difficulty began."),
            ("p", "The third section is about character. As personified capital, the "
                  "capitalist is driven to accumulate by competition, and his own "
                  "consumption is a robbery from accumulation. As a man, he wants to enjoy "
                  "himself, and Marx gives him Faust's two souls. His witness is Dr Aikin's "
                  "history of Manchester from 1795: manufacturers who once lived like misers, "
                  "then got rich, then began to build brick houses, and by 1758 one of them "
                  "was seen with a carriage of his own."),
            ("p", "Then comes Nassau Senior, the Oxford professor of the last hour, who a "
                  "year before that discovery had announced another. &ldquo;I "
                  "substitute,&rdquo; Marx quotes him, &ldquo;for the word capital, "
                  "considered as an instrument of production, the word abstinence.&rdquo; "
                  "Marx's ridicule runs for a page. If the corn is not all eaten but some is "
                  "sown, that is the capitalist's abstinence; if the wine is left to mature, "
                  "that too is the capitalist's abstinence."),
            ("p", "The idea outlived the ridicule, and it deserves its strongest form. Alfred "
                  "Marshall kept it under a better name, &lsquo;waiting&rsquo;, and Eugen "
                  "von Böhm-Bawerk and Irving Fisher built theories of interest on the "
                  "observation that people value present goods above future ones. On that "
                  "view, a capitalist who invests instead of spending gives up something "
                  "real, present consumption, and interest is the price of getting him to "
                  "do it. Marx's reply works at the level of the class: the means of "
                  "production must be used, not eaten, if production is to go on at all, "
                  "and the capitalist's consumption grows with his accumulation rather than "
                  "being sacrificed to it. The two accounts do not disagree about the "
                  "arithmetic below; they disagree about what it rewards."),
            ("p", "The fourth section lists what determines the amount accumulated besides "
                  "the split. If 80 per cent is capitalised, the accumulation is £2,400 or "
                  "£1,200 as the surplus value is £3,000 or £1,500, so everything that "
                  "raises surplus value raises accumulation: wages pushed below the value of "
                  "labour-power, a longer day worked with the same machines, cheaper means "
                  "of production. The fifth dismisses the &lsquo;labour fund&rsquo;, the "
                  "doctrine of Bentham and his followers that the part of wealth available "
                  "for wages is a fixed quantity."),
            ("p", "So far the variable capital has grown in step with the rest. The next "
                  "lesson, “Accumulation with Constant Composition”, asks what that growth "
                  "does to the demand for workers, and to their wages."),
        ],
        "lab": ("capkit", {
            "mode": "accumulate",
            "view": "expand",
            "money_unit": "£",
            "periods": 5,
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's figures: £10,000 at 4:1, s/v 100%, all of s capitalised",
                 "capital": 10000, "c_v": 4, "s_rate": 1, "accumulate_share": 1,
                 "invest_threshold": 0, "expect": {"acCapital": "£124,416/5", "acShareOriginal": "3,125/7,776 = 40.19%"}},
                {"id": "half", "label": "Half of s capitalised, half consumed",
                 "capital": 10000, "c_v": 4, "s_rate": 1, "accumulate_share": "1/2",
                 "invest_threshold": 0, "expect": {"acCapital": "£161,051/10", "acShareOriginal": "100,000/161,051 = 62.09%"}},
                {"id": "consume-all", "label": "None capitalised: simple reproduction",
                 "capital": 10000, "c_v": 4, "s_rate": 1, "accumulate_share": 0,
                 "invest_threshold": 0, "expect": {"acCapital": "£10,000", "acShareOriginal": "1 = 100%"}},
            ],
            "panel_title": "The ball rolls on",
            "panel_intro": (
                "Each period the lab lays out the whole capital at the composition c/v, takes "
                "s = s/v · v, and adds the chosen share of s to capital. The table shows every "
                "period; the tiles show the end of the last. Slide the periods back to 1 to "
                "see Marx's first year, £12,000 of which the original is 5/6."
            ),
        }),
        "steps_title": "Running accumulation period by period",
        "steps_intro": "Four steps, repeated for each period.",
        "steps": [
            ("Split the capital",
             "With c/v = 4, the variable capital is a fifth of the whole: v = capital / "
             "(1 + c/v). At £10,000 that is £2,000."),
            ("Compute the surplus value",
             "s = s/v · v. At a rate of 100%, s equals v: £2,000."),
            ("Add the accumulated share",
             "The next period's capital is this period's plus the share of s capitalised. "
             "All of it gives £12,000; half gives £11,000; none leaves £10,000."),
            ("Compare with the original",
             "Divide the first capital by the present one. The rest of the present capital "
             "is capitalised surplus value."),
        ],
        "worked": {
            "title": "Marx's spinner, year one and year five",
            "intro": [
                "The spinner advances £10,000 at four parts constant to one variable, with "
                "a rate of surplus value of 100%, and capitalises all of it. You want the "
                "capital after one year and after five, and the original's share of each.",
            ],
            "lines": [
                "v = £10,000 / 5 = £2,000;  s = £2,000",
                "year 1:  £10,000 + £2,000 = £12,000",
                "original share:  10,000 / 12,000 = 5/6",
                "each year:  capital × 6/5",
                "year 5:  £10,000 · (6/5)⁵ = £24,883 4s",
                "original share:  about 40.19%",
            ],
            "after": [
                "The second year's surplus value is £2,400: £2,000 from the original "
                "capital, which goes on producing, and Marx's £400 from the first £2,000 "
                "added. With half of s consumed the capital grows by a tenth a year instead "
                "of a fifth, and the original is still about 62% of it after five years.",
            ],
        },
        "quiz_title": "Capitalised surplus value",
        "quiz": [
            {"q": "After one year at Marx's figures, what share of the £12,000 capital is "
                  "capitalised surplus value?",
             "a": ["1/5", "1/6", "5/6", "1/2"],
             "c": 1,
             "why": "The £2,000 added is a sixth of £12,000. Five sixths is the original "
                    "£10,000's share, and a fifth is the variable capital's share of the "
                    "original. Half matches nothing in the example."},
            {"q": "How does Marx's spinner lay out the £2,000 of surplus value he "
                  "capitalises?",
             "a": ["All £2,000 in wages for more spinners",
                   "£1,600 in cotton and machinery and £400 in wages",
                   "£1,000 each in means of production and wages",
                   "All £2,000 in a hoard until it can be invested"],
             "c": 1,
             "why": "He lays it out in the proportions of the original capital, four fifths "
                    "constant and one fifth variable. All of it in wages is the Smith and "
                    "Ricardo error the second section corrects. The other two are not what "
                    "the spinner does."},
            {"q": "A capitalist capitalises 80% of his surplus value. How much does he "
                  "accumulate if the surplus value is £3,000?",
             "a": ["£600", "£2,400", "£3,000", "£1,200"],
             "c": 1,
             "why": "Eighty per cent of £3,000 is £2,400, Marx's own figure. £600 is the part "
                    "he consumes, and £1,200 is the accumulation when the surplus value is "
                    "£1,500."},
            {"q": "In the half preset, roughly what share of the capital after five periods "
                  "is the original £10,000?",
             "a": ["About 40%", "About 62%", "100%", "About 83%"],
             "c": 1,
             "why": "With half of s capitalised the capital grows by a tenth a year, to "
                    "£16,105 after five, and £10,000 is about 62% of that. About 40% is the "
                    "marx preset, 100% is consume-all, and about 83% is the first year at "
                    "Marx's figures."},
        ],
        "mistakes": [
            ("Calling accumulation the capitalist's abstinence from consumption",
             "The half preset consumes £1,000 of the first year's surplus value and still "
             "adds £1,000 to capital; in the consume-all preset the capitalist eats £2,000 a "
             "year and keeps a £10,000 capital. What is added is in either case surplus "
             "value, and after five periods of the marx preset five ninths of the capital "
             "was never anybody's to abstain from: it is capitalised unpaid labour, on "
             "Marx's definitions. Waiting may be a real cost to a person, as Marshall said; "
             "it is not what the capital consists of."),
            ("Treating all capitalised surplus value as wages",
             "Smith and Ricardo held that what is added to capital is consumed by "
             "productive labourers. Marx's spinner lays out £1,600 of the £2,000 in means "
             "of production and £400 in wages, in the same proportions as the original "
             "capital."),
            ("Thinking the original capital remains the bulk of a growing capital",
             "At Marx's figures the original is 5/6 after one year and about 40% after five. "
             "The more periods, the smaller its share, which is Marx's "
             "<em>magnitudo evanescens</em>."),
        ],
        "standard": (
            "Finish when you can run accumulation for several periods by hand.",
            "Given a capital, its composition, the rate of surplus value and the share "
            "capitalised, compute the capital after each period and the original capital's "
            "share of the final one."
        ),
        "note": (
            "The marx preset is the spinner of §1; the half and consume-all presets vary "
            "only the share capitalised. The lab lays out each period's whole capital at the "
            "same composition and rate, as Marx's illustration does, and assumes the extra "
            "means of production and workers are always there to be bought. Whether capital "
            "is capitalised unpaid labour or the reward of waiting is a dispute about "
            "definitions that the arithmetic leaves exactly where it found it."
        ),
    },
    # ---------------------------------------------------------------- 07
    # Kerr vol. 1, l. 4547 (increase of the proletariat); l. 4539 (value,
    # technical and organic composition); l. 4549 (Bellers); l. 4558 (the
    # golden chain); l. 4564 (to put it mathematically).
    {
        "slug": "accumulation-with-constant-composition",
        "title": "Accumulation with Constant Composition",
        "module": "Chapter 25 · The General Law of Capitalist Accumulation",
        "one_line": "With the composition of capital fixed, the demand for workers grows as fast as capital, and when it outruns the supply wages rise until accumulation slows.",
        "summary": (
            "The first section of Chapter 25 holds the composition of capital constant and "
            "lets it accumulate. Compute the workers a growing variable capital employs, "
            "find the period in which demand overtakes the supply, and see the rise in "
            "wages eat into surplus value until the growth of capital slackens."
        ),
        "key": [
            "value composition: c / v",
            "constant c/v: v grows with capital",
            "workers employed = v / wage",
            "demand > supply: the wage rises",
            "higher wages: less s, slower growth",
        ],
        "key_label": "The first section in five lines",
        "concepts_intro": (
            "Chapter 25 is about &ldquo;the influence of the growth of capital on the lot of "
            "the labouring class&rdquo;. Its first section needs three terms."
        ),
        "concepts": [
            ("The composition of capital",
             "In value, the ratio of constant to variable capital. In material, the ratio of "
             "the means of production to the labour needed to work them. Marx calls the "
             "value composition, so far as it mirrors the technical one, the organic "
             "composition."),
            ("Demand for labour",
             "Labour is employed by the variable capital alone. With the composition fixed, "
             "the variable capital and the demand for workers grow in the same proportion "
             "as the whole capital."),
            ("The rate of accumulation decides",
             "When demand outruns the supply, wages rise and the unpaid part of labour "
             "shrinks. If accumulation slackens as a result, the excess of capital that "
             "raised wages disappears. The rate of wages follows; it does not lead."),
        ],
        "read_title": "Accumulation is increase of the proletariat",
        "read_intro": (
            "The passage closes the first half of §1, after the composition of capital has "
            "been defined and held fixed."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 25, §1.</strong> &ldquo;As simple "
                  "reproduction constantly reproduces the capital-relation itself, i.e., the "
                  "relation of capitalists on the one hand, and wage-workers on the other, "
                  "so reproduction on a progressive scale, i.e., accumulation, reproduces "
                  "the capital-relation on a progressive scale, more capitalists or larger "
                  "capitalists at this pole, more wage-workers at that. &hellip; "
                  "Accumulation of capital is, therefore, increase of the proletariat.&rdquo;"),
            ("p", "The chapter's subject is stated in its first line: the influence of the "
                  "growth of capital on the lot of the working class. And the most important "
                  "factor, Marx says, is the composition of capital. He defines it twice. "
                  "On the side of value, it is the proportion of constant to variable "
                  "capital, c to v. On the side of material, it is the mass of means of "
                  "production against the mass of labour needed to work them. The first, so "
                  "far as it reflects the second, he calls the organic composition, and "
                  "that is what he means whenever he writes &ldquo;composition&rdquo; "
                  "without a qualifier."),
            ("p", "Hold the composition fixed and the rest follows. Part of each year's "
                  "surplus value becomes additional capital, and part of that additional "
                  "capital is variable, so the demand for labour grows in the same "
                  "proportion as capital, and faster the faster capital grows. Sooner or "
                  "later, Marx says, accumulation must reach the point where it outruns the "
                  "customary supply of labour, and wages rise. The complaint was heard in "
                  "England through the fifteenth century and the first half of the "
                  "eighteenth."),
            ("p", "The lab starts from the composition Marx uses as his own starting point "
                  "in the next section, half constant and half variable, so c/v = 1. A "
                  "capital of £5,120 employs £2,560 of variable capital, 256 workers at £10 "
                  "a period. The rate of surplus value is 100% and half of each period's "
                  "surplus value is capitalised, so capital grows by a quarter each period "
                  "and so does the demand for workers: 256, 320, 400, 500, 625. The figures "
                  "are illustrative. In the steady preset the workers available grow by 100 "
                  "a period, always ahead of demand."),
            ("p", "The earlier economists saw the connection between more capital and more "
                  "workers clearly, and Marx lets them say it. John Bellers wrote in 1696 "
                  "of &ldquo;the labour of the poor being the mines of the rich&rdquo;. "
                  "Bernard de Mandeville, early in the next century, thought the poor should "
                  "be kept from starving but receive nothing worth saving. Sir Frederic Eden, "
                  "whom Marx calls the only disciple of Adam Smith in the eighteenth century "
                  "to produce a work of importance, "
                  "described the ideal relation as an &ldquo;easy and liberal&rdquo; "
                  "dependence. What none of them saw, Marx says, is that the mechanism of "
                  "accumulation itself produces the &lsquo;labouring poor&rsquo; along with "
                  "the capital."),
            ("p", "Under these conditions, the most favourable to the worker, the dependence "
                  "becomes wider rather than tighter. Workers can buy a little more, put "
                  "something by. Marx grants it and gives it an image: a rise in wages "
                  "means only that &ldquo;the length and weight of the golden chain the "
                  "wage-worker has already forged for himself, allow of a relaxation of the "
                  "tension of it.&rdquo; Wages always imply some unpaid labour, and a rise "
                  "can only reduce its quantity, never to the point that would threaten "
                  "the system."),
            ("p", "Why not? Because of an alternative Marx states precisely. Either wages go "
                  "on rising because the rise does not interfere with accumulation, and "
                  "Smith himself observed that a great stock with small profits generally "
                  "grows faster than a small stock with great profits. Or accumulation "
                  "slackens because the rise blunts the stimulus of gain, and with it the "
                  "disproportion between capital and available labour-power disappears, "
                  "and wages fall back."),
            ("p", "<strong>Volume I, Chapter 25, §1.</strong> &ldquo;To put it "
                  "mathematically: the rate of accumulation is the independent not the "
                  "dependent, variable; the rate of wages, the dependent, not the "
                  "independent, variable.&rdquo;"),
            ("p", "The tight and wage-rise presets show the mechanism in the lab's own model. "
                  "In tight the supply grows by only 40 a period, and in period 3 the 400 "
                  "workers capital wants are more than the 380 available. The lab then "
                  "employs all 380, spreads the variable capital over them as a higher wage, "
                  "and takes the extra wages out of surplus value: s is £3,600 instead of "
                  "£4,000, and capital grows more slowly. In wage-rise the supply stops "
                  "growing at 300, the wage climbs every period, and surplus value falls "
                  "from £2,800 in period 2 to about £1,181 in period 5. The rise in wages "
                  "eats its own cause."),
            ("p", "So the movement of wages reflects the movement of capital, not the other "
                  "way round. Marx's target is the economists who read it backwards, as a "
                  "natural law of population: too few workers, so wages rise, so the poor "
                  "multiply until there are too many. The correlation between capital and "
                  "wages, he says, is really a relation between the unpaid and the paid "
                  "labour of the same working population."),
            ("p", "The view he opposed is not foolish, and a modern version of it is "
                  "standard. In the growth model Robert Solow published in 1956, capital "
                  "accumulating faster than the labour force raises capital per worker, and "
                  "with it the real wage, as far as you like, with no reaction that pushes "
                  "wages back: rising wages and continuing accumulation go together. Marx's "
                  "second case, the reaction, depends on his claim that the rise comes out "
                  "of unpaid labour. The lab builds that claim in, so it cannot test it."),
            ("p", "This section held the composition fixed, and Marx immediately drops the "
                  "assumption. The next lesson, “The Reserve Army of Labour”, asks what "
                  "becomes of the demand for workers when constant capital grows faster "
                  "than variable."),
        ],
        "lab": ("capkit", {
            "mode": "accumulate",
            "view": "labour",
            "money_unit": "£",
            "periods": 5,
            "preset": "steady",
            "presets": [
                {"id": "steady", "label": "Supply grows by 100 workers a period, ahead of demand",
                 "capital": 5120, "c_v": 1, "s_rate": 1, "accumulate_share": "1/2",
                 "labour_supply": 300, "supply_growth": 100, "wage_per_worker": 10, "expect": {"acDemand": "625", "acReserve": "75", "acCapital": "£15,625"}},
                {"id": "tight", "label": "Supply grows by 40 a period: demand overtakes it in period 3",
                 "capital": 5120, "c_v": 1, "s_rate": 1, "accumulate_share": "1/2",
                 "labour_supply": 300, "supply_growth": 40, "wage_per_worker": 10, "expect": {"acDemand": "460", "acReserve": "0", "acCapital": "£26,525/2"}},
                {"id": "wage-rise", "label": "Supply stops at 300: the wage rises every period",
                 "capital": 5120, "c_v": 1, "s_rate": 1, "accumulate_share": "1/2",
                 "labour_supply": 300, "supply_growth": 0, "wage_per_worker": 10, "expect": {"acDemand": "300", "acReserve": "0", "acCapital": "£81,825/8"}},
            ],
            "panel_title": "Capital grows; how many workers does it want?",
            "panel_intro": (
                "The composition is fixed at c/v = 1 and the rate of surplus value at 100%, "
                "and half of s is capitalised. Each period the lab divides the variable "
                "capital by the wage to get the workers wanted. When that exceeds the "
                "supply, it employs the supply at a higher wage. Watch the wage and s "
                "columns in the tight preset from period 3."
            ),
        }),
        "steps_title": "Following demand for labour at constant composition",
        "steps_intro": "Four steps for each period.",
        "steps": [
            ("Split the capital",
             "v = capital / (1 + c/v). At c/v = 1 the variable capital is half: £2,560 of "
             "£5,120."),
            ("Divide by the wage",
             "Workers wanted = v / wage. At £10 a worker, £2,560 wants 256."),
            ("Compare with the supply",
             "If the workers wanted are no more than those available, the difference is a "
             "reserve. If they are more, all available are employed, the wage becomes v / "
             "supply, and surplus value is reduced by the extra wages."),
            ("Accumulate and repeat",
             "Add the capitalised share of s and start the next period from the larger "
             "capital, at the same composition."),
        ],
        "worked": {
            "title": "The steady preset, five periods",
            "intro": [
                "Capital £5,120 at c/v = 1, s/v = 100%, half of s capitalised, a wage of £10. "
                "The supply starts at 300 and grows by 100 a period. You want the workers "
                "wanted and the reserve each period.",
            ],
            "lines": [
                "growth a period:  1/2 · 100% · 1/2 = 1/4",
                "capital:  5,120  6,400  8,000  10,000  12,500",
                "workers wanted:  256  320  400  500  625",
                "supply:  300  400  500  600  700",
                "reserve in period 5:  700 − 625 = 75",
            ],
            "after": [
                "Demand grows by a quarter a period and the supply by 100, so the reserve "
                "first widens and then narrows. In the tight preset the supply grows by 40 "
                "and demand passes it in period 3; from then on the wage rises and the "
                "capital grows more slowly than a quarter a period.",
            ],
        },
        "quiz_title": "Composition, demand and wages",
        "quiz": [
            {"q": "A capital of £8,000 has c/v = 1 and pays £10 a worker. How many workers "
                  "does it employ?",
             "a": ["800", "400", "200", "80"],
             "c": 1,
             "why": "The variable capital is £8,000 / 2 = £4,000, and £4,000 / £10 is 400. "
                    "Eight hundred divides the whole capital by the wage; 200 would need c/v "
                    "= 3; 80 has the decimal point in the wrong place."},
            {"q": "In the tight preset, in which period does the demand for workers first "
                  "exceed the supply?",
             "a": ["Period 2", "Period 3", "Period 4", "Never"],
             "c": 1,
             "why": "Demand is 256, 320 and 400 in the first three periods; supply is 300, "
                    "340 and 380. In period 2, 320 is still below 340; in period 3, 400 is "
                    "above 380."},
            {"q": "Marx says that &ldquo;to put it mathematically&rdquo; one of the two "
                  "rates is the independent variable. Which?",
             "a": ["The rate of wages",
                   "The rate of accumulation",
                   "The rate of population growth",
                   "The rate of interest"],
             "c": 1,
             "why": "The rate of accumulation is independent and the rate of wages "
                    "dependent. The economists he opposes make the working population the "
                    "independent quantity; interest does not enter the argument."},
            {"q": "What does Marx call the value composition of capital, so far as it is "
                  "determined by and mirrors the technical composition?",
             "a": ["The organic composition",
                   "The rate of surplus value",
                   "The labour fund",
                   "The technical composition"],
             "c": 0,
             "why": "That is his definition of the organic composition. The rate of "
                    "surplus value is s/v, the labour fund is the economists' fixed quantity "
                    "of wages, and the technical composition is the material ratio itself."},
        ],
        "mistakes": [
            ("Taking rising wages as proof that accumulation benefits the worker without limit",
             "In the wage-rise preset the wage climbs every period, and surplus value falls "
             "with it, from £2,800 in period 2 to about £1,181 in period 5, while capital "
             "grows ever more slowly. On Marx's account a rise in wages can only reduce the "
             "unpaid labour, and once that touches the point where accumulation slackens "
             "the rise is checked. The chain is relaxed, not removed."),
            ("Making the working population the independent variable",
             "The economists Marx answers explain wages by population: high wages make the "
             "poor multiply until wages fall. Marx reverses the arrow. In the lab the "
             "supply is the same in all three presets until it is changed by hand, and the "
             "wage rises only when accumulation outruns it."),
            ("Confusing the value composition with the technical composition",
             "The technical composition is a ratio of masses, means of production to "
             "labour; the value composition is a ratio of values, c to v. They move "
             "together but not equally, because means of production get cheaper as they "
             "multiply. The lab works with the value ratio only."),
        ],
        "standard": (
            "Finish when you can follow demand for labour as capital accumulates.",
            "Given a capital, a fixed composition, the rate of surplus value, the share "
            "capitalised, the wage and the labour supply, compute the workers wanted each "
            "period and identify the period in which demand first exceeds the supply."
        ),
        "note": (
            "The figures are illustrative. The rule by which the lab raises wages, spreading "
            "the variable capital over the workers available, is the lab's model of Marx's "
            "&ldquo;wages may rise&rdquo;; the chapter states the direction and the limit, "
            "not a formula. The lab also never lets the wage fall back, so it shows "
            "accumulation slackening but not the reaction Marx says follows."
        ),
    },
    # ---------------------------------------------------------------- 08
    # Kerr vol. 1, l. 4631 (a surplus-population); l. 4588 (£6,000 to
    # £18,000); l. 4599 (centralisation); l. 4615 (railroads); l. 4629
    # (1:1 to 7:1); l. 4639 (reserve army); l. 4670 (28 4/7 per cent);
    # l. 4680 (both sides).
    {
        "slug": "the-reserve-army",
        "title": "The Reserve Army of Labour",
        "module": "Chapter 25 · The General Law of Capitalist Accumulation",
        "one_line": "When constant capital grows faster than variable, capital can triple while it employs no more workers, and the workers it does not take on form a reserve.",
        "summary": (
            "Sections 2 and 3 of Chapter 25 let the composition of capital rise as "
            "accumulation proceeds. Compute employment period by period when the ratio of "
            "constant to variable capital climbs through Marx's 1:1, 2:1, 3:1, and the "
            "relative surplus population that results; then see what a faster rate of "
            "accumulation or a constant composition does instead."
        ),
        "key": [
            "productivity raises c/v as capital grows",
            "v = capital / (1 + c/v)",
            "c/v 1 → 5: capital ×3, v unchanged",
            "reserve = supply − workers employed",
            "centralisation speeds the rise in c/v",
        ],
        "key_label": "Sections 2 and 3 in five lines",
        "concepts_intro": (
            "The constant composition of §1 is dropped at once. Three ideas replace it."
        ),
        "concepts": [
            ("The rising composition",
             "As productivity grows, each worker sets more means of production in motion, "
             "and constant capital grows faster than variable. Demand for labour is set by "
             "the variable part alone, so it falls relative to the whole capital."),
            ("Concentration and centralisation",
             "Concentration is the growth of individual capitals by accumulation. "
             "Centralisation is the merging of capitals already formed, by competition and "
             "credit, and it is not limited by the growth of social wealth."),
            ("The industrial reserve army",
             "A population of workers in excess of what capital needs on average. Marx says "
             "accumulation produces it, and that it is in turn a condition of capitalist "
             "production, which needs workers ready for sudden expansions."),
        ],
        "read_title": "A surplus population, produced",
        "read_intro": (
            "The passage is the turn of §3, where the arithmetic of a rising composition is "
            "said to produce, not merely to find, a surplus of workers."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 25, §3.</strong> &ldquo;But in fact, it is "
                  "capitalistic accumulation itself that constantly produces, and produces "
                  "in the direct ratio of its own energy and extent, a relatively redundant "
                  "population of labourers, i.e., a population of greater extent than "
                  "suffices for the average needs of the self-expansion of capital, and "
                  "therefore a surplus-population.&rdquo;"),
            ("p", "Begin with §2, which supplies the cause. As the productivity of labour "
                  "grows, one worker turns more raw material into product in the same time, "
                  "using more machinery, more buildings, more power. The mass of the means "
                  "of production grows relative to the labour that works them, and that "
                  "shows in value as constant capital growing faster than variable: half and "
                  "half at first, then four fifths and one fifth, and so on. Marx's "
                  "illustration is spinning: if its capital is seven eighths constant today "
                  "against half at the start of the eighteenth century, the mass of material "
                  "a spinner works up has grown many hundred times. The value ratio rises "
                  "less than the material one, because the means of production cheapen as "
                  "they multiply."),
            ("p", "<strong>Volume I, Chapter 25, §2.</strong> &ldquo;If in the meantime the "
                  "original capital, say £6,000, has increased to £18,000, its variable "
                  "constituent has also increased. It was £3,000, it is now £3,600. But "
                  "whereas formerly an increase of capital by 20 per cent. would have "
                  "sufficed to raise the demand for labour 20 per cent., now this latter rise "
                  "requires a tripling of the original capital.&rdquo;"),
            ("p", "Read it as a sum. At half and half, £6,000 has £3,000 variable. At four "
                  "fifths to one fifth, £18,000 has `18,000/5 = 3,600`. The capital tripled "
                  "and the variable part, which is what employs workers, rose by a fifth. "
                  "That is Marx's whole point in two numbers, and the lab carries it a step "
                  "further."),
            ("p", "First, though, §2's other subject. Individual capitals grow by "
                  "accumulation, which Marx calls concentration, and new ones split off, so "
                  "growth is spread across many hands. Against that runs centralisation, the "
                  "attraction of capital by capital: the larger capitals beat the smaller in "
                  "competition by cheapening their goods, and credit gathers scattered money "
                  "into a few hands. &ldquo;Capital grows in one place to a huge mass in a "
                  "single hand, because it has in another place been lost by many.&rdquo; "
                  "Its speed is the point. &ldquo;The world would still be without "
                  "railroads, if it had been obliged to wait until accumulation should have "
                  "enabled a few individual capitals to undertake the construction of a "
                  "railroad.&rdquo; Joint-stock companies did it at a stroke, and every "
                  "centralised capital renews its equipment in the latest form, so "
                  "centralisation hastens the rise in the composition."),
            ("p", "Then §3 gives the ratios. As capital accumulates, constant to variable "
                  "goes from 1:1 to 2:1, 3:1, 4:1, 5:1, 7:1, so that of the total value "
                  "first a half, then a third, a quarter, a fifth, a sixth, an eighth goes "
                  "into labour-power. The rising preset runs those ratios one per period, "
                  "starting from Marx's £6,000. With a rate of surplus value of 100% and all "
                  "of it capitalised, the capital laid out goes £6,000, £9,000, £12,000, "
                  "£15,000, £18,000, and the variable capital stays at £3,000 every period. "
                  "Capital triples and employs 300 workers throughout. The labour supply "
                  "grows by 30 a period, and by period 5 there are 120 workers capital does "
                  "not want. In the fast-growth preset the same ratios run at a rate of "
                  "surplus value of 200%, capital grows fast enough to take on 100 more "
                  "workers each period, 700 by period 5, and with the supply also growing "
                  "by 100 no reserve forms. In the constant preset the composition stays at "
                  "1:1 and demand outruns the 420 available."),
            ("p", "This reserve, Marx says, is not a misfortune of capitalist production but a "
                  "condition of it. &ldquo;It forms a disposable industrial reserve army, "
                  "that belongs to capital quite as absolutely as if the latter had bred it "
                  "at its own cost.&rdquo; Capital expands by fits and starts, into railways "
                  "or a suddenly opened market, and needs masses of workers it can throw at "
                  "the decisive point without stripping other branches. The modern cycle of "
                  "about ten years, through average activity, high pressure, crisis and "
                  "stagnation, depends on the reserve being formed, absorbed and formed "
                  "again. Herman Merivale, the Oxford professor who moved to the Colonial "
                  "Office, said as much: manufacturers &ldquo;must have hands ready by "
                  "them&rdquo;."),
            ("p", "The reserve grows faster even than the composition rises, because capital "
                  "can also get more labour out of the same workers. A larger variable "
                  "capital can buy more labour without more labourers, by lengthening or "
                  "intensifying the day; the same variable capital can buy cheaper labour, "
                  "women's and children's for men's. The over-work of the employed swells "
                  "the reserve, and the reserve's competition forces over-work on the "
                  "employed."),
            ("p", "Marx then attacks the economists' theory of wages, in which high wages "
                  "make the workers multiply until wages fall. Before that could happen, he "
                  "replies, the industrial campaign would have been fought and won many "
                  "times; wages move with the expansion and contraction of the reserve, "
                  "inside the decennial cycle. His example is English agriculture between "
                  "1849 and 1859, when wages in Wiltshire rose from 7s to 8s a week. The "
                  "farmers did not wait for the labourers to multiply. They brought in "
                  "machinery, and the labourers were redundant again. A rise from 7s to 9s, "
                  "he notes drily, is 28 4/7 per cent, &ldquo;which sounds very fine&rdquo;."),
            ("p", "Last, the compensation theory of Chapter 15, that machinery which displaces "
                  "workers sets free capital to employ them. Marx's answer now is that the "
                  "supply of labour and the demand for it are not two independent forces. "
                  "&ldquo;Capital works on both sides at the same time.&rdquo; Its "
                  "accumulation raises the demand for workers, and its rising composition "
                  "raises the supply by setting them free. When workers organise the "
                  "employed and the unemployed together, he adds, the economists cry out "
                  "against the violation of the sacred law of supply and demand."),
            ("p", "The record since has been the strongest objection. Over the twentieth "
                  "century employment in the industrial countries grew a great deal along "
                  "with their capital, and Nicholas Kaldor's stylised facts of economic "
                  "growth, set out in 1961, include a ratio of capital to output roughly "
                  "constant over long periods, which is hard to square with a value "
                  "composition always rising. Marx's own qualification, that the means of "
                  "production cheapen as they multiply, is what defenders appeal to and "
                  "critics say empties the law. The lab assumes the rise you give it and "
                  "computes the consequence."),
            ("p", "A reserve army has been produced; Marx now asks who is in it and what its "
                  "existence means for the whole class. That is the last lesson of the "
                  "course, “The General Law of Capitalist Accumulation”."),
        ],
        "lab": ("capkit", {
            "mode": "accumulate",
            "view": "composition",
            "money_unit": "£",
            "periods": 5,
            "preset": "rising",
            "presets": [
                {"id": "rising", "label": "Marx's ratios: c/v rises 1:1, 2:1, 3:1, 4:1, 5:1 from £6,000",
                 "capital": 6000, "c_v": 1, "s_rate": 1, "accumulate_share": 1,
                 "composition_rise": 1, "labour_supply": 300, "supply_growth": 30,
                 "wage_per_worker": 10, "expect": {"acDemand": "300", "acReserve": "120"}},
                {"id": "fast-growth", "label": "The same ratios at s/v 200%: capital outruns the composition",
                 "capital": 6000, "c_v": 1, "s_rate": 2, "accumulate_share": 1,
                 "composition_rise": 1, "labour_supply": 300, "supply_growth": 100,
                 "wage_per_worker": 10, "expect": {"acDemand": "700", "acReserve": "0"}},
                {"id": "constant", "label": "The composition stays at 1:1",
                 "capital": 6000, "c_v": 1, "s_rate": 1, "accumulate_share": 1,
                 "composition_rise": 0, "labour_supply": 300, "supply_growth": 30,
                 "wage_per_worker": 10, "expect": {"acDemand": "420", "acReserve": "0"}},
            ],
            "panel_title": "More capital, the same workers",
            "panel_intro": (
                "The lab adds the rise you give to c/v each period, lays out the whole "
                "capital at that composition, and divides the variable capital by the wage. "
                "Read the capital and v columns of the rising preset together: one triples, "
                "the other does not move. The figures besides Marx's ratios are "
                "illustrative."
            ),
        }),
        "steps_title": "Employment under a rising composition",
        "steps_intro": "Four steps for each period.",
        "steps": [
            ("Find this period's composition",
             "Add the period's rise to c/v. Marx's ratios rise by 1 a period: 1, 2, 3, 4, "
             "5."),
            ("Split the capital",
             "v = capital / (1 + c/v). At £9,000 and c/v = 2, v is £3,000."),
            ("Count the workers",
             "Workers employed = v / wage, up to the supply; the rest of the supply is the "
             "reserve."),
            ("Accumulate",
             "Add the capitalised surplus value and repeat. Compare the growth of capital "
             "with the growth of v: employment follows v."),
        ],
        "worked": {
            "title": "Capital triples, employment stands still",
            "intro": [
                "Start from Marx's £6,000 at 1:1. The rate of surplus value is 100% and all "
                "of it is capitalised; c/v rises by 1 each period. A worker costs £10, and "
                "300 are available at first, 30 more each period.",
            ],
            "lines": [
                "period 1:  6,000 / 2 = 3,000 v;  300 workers",
                "period 2:  9,000 / 3 = 3,000 v;  300 workers",
                "period 3:  12,000 / 4 = 3,000 v;  300 workers",
                "period 5:  18,000 / 6 = 3,000 v;  300 workers",
                "reserve in period 5:  420 − 300 = 120",
            ],
            "after": [
                "Each period adds s = v = £3,000 to capital, and the rise in composition "
                "takes the whole of it into constant capital. Marx's own sum in §2 is less "
                "stark: his £18,000 at four to one still has a variable part of £3,600, a "
                "fifth more than before. Either way the demand for labour grows far more "
                "slowly than capital.",
            ],
        },
        "quiz_title": "Composition and employment",
        "quiz": [
            {"q": "A capital of £12,000 has c/v = 3 and pays £10 a worker. How many workers "
                  "does it employ?",
             "a": ["1,200", "400", "300", "600"],
             "c": 2,
             "why": "The variable capital is £12,000 / 4 = £3,000, which employs 300. Divide "
                    "by 3 instead of 4 and you get 400; 600 is the variable capital at 1:1, "
                    "and 1,200 divides the whole capital by the wage."},
            {"q": "In Marx's §2 example, £6,000 at half and half grows to £18,000 at four "
                  "fifths and one fifth. What is the variable capital now?",
             "a": ["£3,000", "£3,600", "£9,000", "£4,500"],
             "c": 1,
             "why": "One fifth of £18,000 is £3,600, up from £3,000. £9,000 keeps the old "
                    "half-and-half split, and £4,500 would be a quarter."},
            {"q": "How does centralisation differ from concentration, in Marx's terms?",
             "a": ["Centralisation is growth by accumulation; concentration is merging",
                   "Centralisation redistributes capitals already formed and is not limited "
                   "by the growth of social wealth",
                   "Centralisation happens only through the state",
                   "There is no difference; the words are synonyms"],
             "c": 1,
             "why": "Concentration is the growth of capitals by accumulation and is limited "
                    "by the growth of social wealth. Centralisation is the merging of existing "
                    "capitals, through competition, credit or stock companies. The first "
                    "option swaps the two."},
            {"q": "In the rising preset the capital laid out goes from £6,000 to £18,000. "
                  "What happens to the number of workers employed?",
             "a": ["It triples, to 900",
                   "It stays at 300",
                   "It falls to 100",
                   "It rises to 420, the whole supply"],
             "c": 1,
             "why": "The variable capital is £3,000 in every period, so employment stays at "
                    "300. Tripling would need a constant composition; 420 is the supply in "
                    "period 5, of which 120 are in reserve."},
        ],
        "mistakes": [
            ("Assuming accumulation always increases employment",
             "In the rising preset capital triples and employs 300 workers from first period "
             "to last, because the rise in composition takes every pound of new capital into "
             "constant capital. Employment rises only where accumulation outpaces the "
             "composition, as in the fast-growth preset at 200%, or where the composition "
             "does not rise, as in the constant preset."),
            ("Explaining the reserve army by population growth",
             "The economists Marx answers blame the number of workers. The lab holds the "
             "supply's growth at 30 a period in both the rising and the constant presets; "
             "one produces a reserve of 120 and the other none. On Marx's account the "
             "difference is made by capital's composition, not by births."),
            ("Confusing centralisation with concentration",
             "Concentration is accumulation in individual hands and is limited by the "
             "growth of social wealth. Centralisation is the merging of capitals already "
             "formed, can happen with no growth at all, and is much faster."),
        ],
        "standard": (
            "Finish when you can compute employment and the reserve under a rising composition.",
            "Given a capital, a starting composition and its rise per period, the rate of "
            "surplus value, the share capitalised, the wage and the labour supply, compute "
            "the workers employed and the reserve in each period."
        ),
        "note": (
            "The ratios in the rising preset are Marx's, from §3, and the starting capital "
            "is his £6,000 from §2; the wage and the labour supply are illustrative. The lab "
            "takes the rise in composition as an input. Whether the value composition of "
            "capital does in fact rise over time is disputed, because the cheapening of "
            "means of production can offset the growth in their mass, and the lab cannot "
            "settle that."
        ),
    },
    # ---------------------------------------------------------------- 09
    # Kerr vol. 1, l. 4715-4717 (the lot of the labourer, two poles); l. 4686
    # (three forms); l. 4698 (latent); l. 4702 (stagnant); l. 4704 and l. 4706
    # (pauperism); l. 4708 (the absolute general law); l. 4815 and l. 4817
    # (Gladstone).
    {
        "slug": "the-general-law-of-accumulation",
        "title": "The General Law of Capitalist Accumulation",
        "module": "Chapter 25 · The General Law of Capitalist Accumulation",
        "one_line": "The reserve army grows with the energy of accumulation, so the ratio of reserve to employed can rise while the employed are paid more.",
        "summary": (
            "Section 4 of Chapter 25 names the forms of the relative surplus population and "
            "states the general law. Compute the ratio of the reserve army to the active "
            "army period by period, in a boom with rising wages, in a slump and in the long "
            "run, and keep apart what the law says about the ratio from what it is often "
            "read as saying about wages."
        ),
        "key": [
            "floating, latent, stagnant; then paupers",
            "ratio = reserve / workers employed",
            "boom: wages rise and the ratio can rise too",
            "wealth at one pole, misery at the other",
            "a tendency, modified by circumstances",
        ],
        "key_label": "The general law in five lines",
        "concepts_intro": (
            "Section 4 is the shortest of the chapter's five and carries its most famous "
            "sentence. It turns on three ideas."
        ),
        "concepts": [
            ("The three forms",
             "The floating surplus population moves in and out of modern industry; the "
             "latent waits in agriculture to move to the towns; the stagnant is employed, "
             "but irregularly, with the longest hours and the lowest wages."),
            ("Pauperism",
             "The lowest layer: paupers able to work, orphans and pauper children, and those "
             "unable to work. Marx calls it the hospital of the active army and the dead "
             "weight of the reserve."),
            ("The general law",
             "The greater the social wealth and the energy of its growth, the greater the "
             "reserve army relative to the active army, and the greater the misery of the "
             "layers that bear it. Marx calls it absolute and adds at once that "
             "circumstances modify it."),
        ],
        "read_title": "The law in its strongest words",
        "read_intro": (
            "The passage comes near the end of §4, after the forms of the surplus "
            "population have been described and the law stated. It is the sentence most "
            "quoted from the whole of Volume I, and most argued over."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 25, §4.</strong> &ldquo;It follows therefore "
                  "that in proportion as capital accumulates, the lot of the labourer, be his "
                  "payment high or low, must grow worse. &hellip; It establishes an "
                  "accumulation of misery, corresponding with accumulation of capital. "
                  "Accumulation of wealth at one pole is, therefore, at the same time "
                  "accumulation of misery, agony of toil, slavery, ignorance, brutality, "
                  "mental degradation, at the opposite pole, i.e., on the side of the class "
                  "that produces its own product in the form of capital.&rdquo;"),
            ("p", "Before reading the passage closely, look at who Marx says is in the "
                  "reserve. Every worker belongs to it while partly or wholly unemployed, and "
                  "besides the acute form it takes in a crisis and the chronic form in dull "
                  "times, &ldquo;it has always three forms, the floating, the latent, the "
                  "stagnant.&rdquo;"),
            ("p", "The floating form lives in the centres of modern industry, where workers "
                  "are repelled and attracted again and the number employed grows, but more "
                  "slowly than production. Boys are taken on in great numbers and discharged "
                  "when they come of age. Labour-power is used up so fast that a worker is "
                  "worn out half-way through life; Marx cites a Manchester medical officer "
                  "who put the average age at death among the labouring class at 17, against "
                  "38 for the upper middle class. The latent form is in agriculture, where "
                  "capital reduces the demand for labourers absolutely and a part of the "
                  "rural population is always on the point of moving to the towns. The "
                  "agricultural labourer, Marx writes, &ldquo;always stands with one foot "
                  "already in the swamp of pauperism.&rdquo;"),
            ("p", "The stagnant form is part of the active army, but irregularly employed, "
                  "and it is characterised &ldquo;by maximum of working time, and minimum "
                  "of wages.&rdquo; It is the domestic industry of Chapter 15, recruited from "
                  "trades where handicraft is giving way to manufacture and manufacture to "
                  "machinery. Below all three lies pauperism, &ldquo;the lowest sediment of "
                  "the relative surplus-population&rdquo;: those able to work, whose numbers "
                  "rise with every crisis; orphans and pauper children, enrolled in the "
                  "active army in good years like 1860; and the demoralised, the old, the "
                  "maimed and the widowed. &ldquo;Pauperism is the hospital of the active "
                  "labour-army and the dead weight of the industrial reserve-army.&rdquo;"),
            ("p", "<strong>Volume I, Chapter 25, §4.</strong> &ldquo;This is the absolute "
                  "general law of capitalist accumulation. Like all other laws it is modified "
                  "in its working by many circumstances, the analysis of which does not "
                  "concern us here.&rdquo;"),
            ("p", "The law in the sentences just before is a chain of proportions. The "
                  "greater the social wealth, the capital in use and the energy of its "
                  "growth, the greater the reserve army; the greater the reserve relative to "
                  "the active army, the greater the consolidated surplus population; the "
                  "larger that layer and the reserve, the greater official pauperism. The lab "
                  "can compute the middle term, the reserve as a ratio of those employed, and "
                  "that is all it computes."),
            ("p", "Its presets run the law view for five periods from £6,000 at a "
                  "composition of 1:1 and a wage of £10. In the boom the rate of surplus "
                  "value is 200%, all of it is capitalised, the composition rises by 1 a "
                  "period, and the wage rises by 10s a period, from £10 to £12. Employment "
                  "grows from 300 to 475, and still the supply, growing by 50 a period, "
                  "outruns it: the ratio of reserve to employed goes from 0 to `1/19`. Wages "
                  "and the reserve rise together. In the slump nothing is capitalised and "
                  "the composition creeps up by a half each period, so the same capital "
                  "employs 150 by the fifth period, and the ratio is `9/5`. In the long run "
                  "Marx's ratios carry employment flat at 300 while the reserve reaches 120, "
                  "a ratio of `2/5`; slide the periods to 10 and it reaches `9/10`."),
            ("p", "Now the passage. &ldquo;Be his payment high or low&rdquo; is the phrase to "
                  "hold on to: Marx is not saying the worker's pay must fall. He is saying "
                  "the worker's position worsens in proportion as capital accumulates, "
                  "whatever happens to pay, because the methods of raising productivity "
                  "turn into means of domination: they mutilate the labourer into a fragment "
                  "of a man, he says, and drag his wife and child under the wheels of "
                  "capital. The two poles are the image. Wealth accumulates on the side that "
                  "owns the product, misery on the side that produces it."),
            ("p", "Section 5 illustrates the law with England from 1846 to 1866 over many "
                  "pages: the income tax returns, the official count of paupers, Dr "
                  "Smith's measurements of the diets of the worst-fed workers in grains of "
                  "carbon and nitrogen, Dr Hunter's reports on housing, the cotton famine, "
                  "the crisis of 1866 in the East End, the gang system in Lincolnshire, and "
                  "Ireland, whose population fell from over 8 million in 1841 to about 5½ "
                  "million in 1866 while rents rose. One exchange states the interpretive "
                  "question exactly. Gladstone, presenting his budget in 1863, said: "
                  "&ldquo;While the rich have been growing richer, the poor have been "
                  "growing less poor.&rdquo; Marx answers that if the working class has only "
                  "become less poor while producing an intoxicating growth of wealth for "
                  "others, &ldquo;then it has remained relatively just as poor.&rdquo;"),
            ("p", "That reply is where the long argument over the law begins. Read as a "
                  "prediction that the real wages of employed workers must fall, it was "
                  "contradicted by British wages from the later nineteenth century on, and "
                  "Eduard Bernstein, a leading German socialist, said so in 1899 in the book "
                  "that began the revisionist controversy. Read as a claim about relative "
                  "position, the worker's share of what he produces and his dependence on "
                  "capital, it is harder to refute and harder to test. Defenders also point "
                  "to the global reserve of rural and informal workers, which is outside "
                  "any one country's statistics. This course leaves the question open; the "
                  "boom preset shows only that a rising reserve ratio and rising wages are "
                  "compatible on the chapter's own arithmetic."),
            ("p", "Marx ends §4 with the economists who saw the same antagonism and called it "
                  "nature: the Venetian monk Giammaria Ortes, for whom the abundance of some "
                  "always equals the want of others; the parson Joseph Townsend, who thought "
                  "hunger a better spur to labour than law. His own claim is the opposite. "
                  "The law is peculiar to capitalist production, as he said in §3: an "
                  "abstract law of population exists only for plants and animals."),
            ("p", "Volume I has now asked where surplus value comes from, how it becomes "
                  "capital, and what that does to the workers. One question was put off: "
                  "where the first capital came from, which the economists answered with the "
                  "labour of the capitalist's forefathers. The next course, “So-Called "
                  "Primitive Accumulation”, reads Marx's answer."),
        ],
        "lab": ("capkit", {
            "mode": "accumulate",
            "view": "law",
            "money_unit": "£",
            "periods": 5,
            "preset": "boom",
            "presets": [
                {"id": "boom", "label": "Boom: s/v 200%, wages rise 10s a period, c/v rises by 1",
                 "capital": 6000, "c_v": 1, "s_rate": 2, "accumulate_share": 1,
                 "composition_rise": 1, "labour_supply": 300, "supply_growth": 50,
                 "wage_per_worker": 10, "wage_growth": "1/2", "expect": {"acRatio": "1/19 = 5.26%", "acReserve": "25", "acDemand": "475"}},
                {"id": "slump", "label": "Slump: nothing capitalised, c/v creeps up by 1/2",
                 "capital": 6000, "c_v": 1, "s_rate": 1, "accumulate_share": 0,
                 "composition_rise": "1/2", "labour_supply": 300, "supply_growth": 30,
                 "wage_per_worker": 10, "wage_growth": 0, "expect": {"acRatio": "9/5 = 180%", "acReserve": "270", "acDemand": "150"}},
                {"id": "long-run", "label": "Long run: Marx's ratios, 1:1 rising by 1 a period",
                 "capital": 6000, "c_v": 1, "s_rate": 1, "accumulate_share": 1,
                 "composition_rise": 1, "labour_supply": 300, "supply_growth": 30,
                 "wage_per_worker": 10, "wage_growth": 0, "expect": {"acRatio": "2/5 = 40%", "acReserve": "120", "acDemand": "300"}},
            ],
            "panel_title": "The reserve against the active army",
            "panel_intro": (
                "The lab runs accumulation period by period with the composition, the wage "
                "and the supply moving as the inputs say, and divides the reserve by the "
                "workers employed. In the boom read the wage and reserve columns together. "
                "The figures are illustrative; slide the periods to 10 for a longer run."
            ),
        }),
        "steps_title": "Computing the reserve ratio",
        "steps_intro": "Four steps for each period.",
        "steps": [
            ("Find the period's composition and wage",
             "Add the period's rise to c/v and the period's rise to the wage."),
            ("Find the workers wanted",
             "v = capital / (1 + c/v), and the workers wanted are v divided by the "
             "period's wage, up to the supply."),
            ("Find the reserve",
             "Reserve = supply − workers employed, never below zero."),
            ("Divide",
             "Ratio = reserve / workers employed. Compare it period by period with the "
             "wage, which can move the other way."),
        ],
        "worked": {
            "title": "The boom, period 5",
            "intro": [
                "In the boom the capital laid out in period 5 is £34,200 at c/v = 5, the wage "
                "has risen to £12, and 500 workers are available. You want employment, the "
                "reserve and the ratio.",
            ],
            "lines": [
                "v:  34,200 / 6 = 5,700",
                "workers wanted:  5,700 / 12 = 475",
                "reserve:  500 − 475 = 25",
                "ratio:  25 / 475 = 1/19 ≈ 5.26%",
            ],
            "after": [
                "In period 1 all 300 available were employed at £10 and the ratio was 0. By "
                "period 5 the wage is a fifth higher, employment is up by more than half, and "
                "a reserve has formed. Higher wages and a growing reserve are not "
                "contradictory on the chapter's arithmetic.",
            ],
        },
        "quiz_title": "Reading the general law",
        "quiz": [
            {"q": "In some period 400 workers are employed and 100 more are available but not "
                  "employed. What is the ratio of reserve to employed?",
             "a": ["1/5", "1/4", "4", "4/5"],
             "c": 1,
             "why": "Reserve over employed is 100 / 400 = 1/4. One fifth divides the reserve "
                    "by the whole supply of 500, 4 is the ratio upside down, and 4/5 is the "
                    "employed share of the supply."},
            {"q": "Which form of the relative surplus population is the part of the rural "
                  "population always on the point of moving to the towns?",
             "a": ["The floating", "The latent", "The stagnant", "Pauperism"],
             "c": 1,
             "why": "Marx calls it latent, because its extent shows only when the channels to "
                    "the towns open wide. The floating moves in and out of modern industry; "
                    "the stagnant is irregularly employed; pauperism is the layer below "
                    "all three."},
            {"q": "In the boom preset, what happens between period 1 and period 5?",
             "a": ["Wages fall and the reserve grows",
                   "Wages rise and the ratio of reserve to employed rises",
                   "Wages rise and the reserve disappears",
                   "Employment falls and wages stay at £10"],
             "c": 1,
             "why": "The wage goes from £10 to £12 and the ratio from 0 to 1/19. Falling "
                    "wages are the slump's reading of the law, not the boom's; employment "
                    "rises from 300 to 475."},
            {"q": "Marx says the lot of the labourer must grow worse &ldquo;be his payment "
                  "high or low&rdquo;. Which of these does the lab compute?",
             "a": ["The worker's real wage over time",
                   "The ratio of the reserve army to the employed",
                   "The degree of misery at the opposite pole",
                   "Whether the law holds in fact"],
             "c": 1,
             "why": "The lab computes employment, the reserve and their ratio on the inputs "
                    "you give. It does not compute real wages, it cannot measure misery, and "
                    "whether the law holds is an empirical question its arithmetic cannot "
                    "answer."},
        ],
        "mistakes": [
            ("Reading the law as predicting that real wages must always fall",
             "Marx's own words are &ldquo;be his payment high or low&rdquo;. In the boom "
             "preset the wage rises from £10 to £12 while the ratio of reserve to employed "
             "rises from 0 to 1/19. What the law ties to accumulation is the relative size "
             "of the reserve and the condition of the class, not the level of the wage, and "
             "whether that condition is relative or absolute is the disputed part."),
            ("Taking official pauperism for the whole reserve army",
             "Paupers are the lowest layer. The floating, latent and stagnant forms are "
             "workers who are partly or irregularly employed, and Marx says the official "
             "statistics understate even pauperism, since workers avoided the workhouse "
             "as long as they could."),
            ("Treating the law as a law of nature",
             "Ortes and Townsend made the antagonism natural. Marx calls it a law peculiar to "
             "capitalist production, and in the same breath says it is modified by many "
             "circumstances. It is a tendency stated from the definitions, not a "
             "prediction for every year."),
        ],
        "standard": (
            "Finish when you can compute the reserve ratio and say what it does and does not show.",
            "Given the inputs of a period of accumulation, compute the workers employed, the "
            "reserve and the ratio of reserve to employed, and state whether the wage and "
            "the ratio moved in the same direction."
        ),
        "note": (
            "The figures are illustrative, and the wage rise in the boom is an input, not "
            "the result of the reserve's absorption that Marx describes. The lab computes a "
            "ratio; it does not measure misery, and it holds no data on real wages or "
            "unemployment. Whether the general law describes the history since 1867, and in "
            "which reading, is argued with evidence this course does not carry."
        ),
    },
]
