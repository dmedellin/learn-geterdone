"""Wages and Accumulation, lessons 1-5 -- Volume I, Chapters 19 to 23.

Every quotation is copied from /mnt/project-files/capital-texts/volume-1-kerr.txt
(the Kerr edition of Volume I); the comment beside each lesson gives its line
numbers. Footnote numerals in the text are left out of the quotations, a
drop capital ("ON", "WAGES") is printed as an ordinary capital, and the
translator's double quotation marks inside a quotation are printed as single
curly quotes. Nothing else is changed.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Kerr vol. 1, l. 3944 (the opening sentences); l. 3957 (labour has no
    # value); l. 3972 (6s. and 3s.); l. 3974 (unpaid labour appears as paid).
    {
        "slug": "value-of-labour-power-into-wages",
        "title": "The Value of Labour-Power Becomes Wages",
        "module": "Chapter 19 · The Transformation of the Value (and Respectively the Price) of Labour-Power into Wages",
        "one_line": "A wage looks like the price of the work done; it is the value of a day's labour-power divided over the hours, and the hours create more than that.",
        "summary": (
            "Chapter 19 asks why the wage presents itself as a price paid for labour when "
            "what the worker sells is labour-power. Compute the apparent price of an hour "
            "from the daily value of labour-power and the length of the day, set it beside "
            "the value the hours create, and see the unpaid part disappear inside the "
            "form of the wage."
        ),
        "key": [
            "the wage appears as the price of labour",
            "what is sold is labour-power",
            "price of an hour = day's value / hours",
            "3s / 12 hours = 3d an hour",
            "the 12 hours create 6s: 6d an hour",
            "the wage form shows all labour as paid",
        ],
        "key_label": "Chapter 19 in six lines",
        "concepts_intro": (
            "Part VI of Volume I is short, four chapters, and it is about one appearance: "
            "the wage. The first chapter sets out the appearance and the thing behind it."
        ),
        "concepts": [
            ("The price of labour",
             "In everyday speech, and in the economists before Marx, a wage is the price "
             "of so much labour: so many shillings for so many hours. Smith called its "
             "average the &ldquo;natural price&rdquo; of labour."),
            ("The value of labour-power",
             "What the worker sells is the capacity to work for a stated time. Its daily "
             "value is the value of what it takes to maintain the worker for a day, and in "
             "Marx's example that is 3s, the product of 6 hours."),
            ("The wage form",
             "Paying the value of labour-power as if it were the price of all the hours "
             "worked makes the whole day look paid. Marx calls this a phenomenal form that "
             "&ldquo;makes the actual relation invisible&rdquo;."),
        ],
        "read_title": "The surface first, then what lies under it",
        "read_intro": (
            "The chapter opens with the way wages are spoken of, and spends the rest of "
            "its length showing that the phrase cannot mean what it says."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 19.</strong> &ldquo;On the surface of "
                  "bourgeois society the wage of the labourer appears as the price of "
                  "labour, a certain quantity of money that is paid for a certain quantity of "
                  "labour. Thus people speak of the value of labour and call its expression "
                  "in money its necessary or natural price.&rdquo;"),
            ("p", "If you have ever been paid by the hour, you know this sentence from the "
                  "inside. The payslip says so many hours at so much an hour, and it is hard "
                  "to read it as anything but a price for the work you did. Marx does not "
                  "say the payslip lies. He says it shows a surface, and that the phrase "
                  "&ldquo;value of labour&rdquo; on that surface is one the economists "
                  "borrowed from everyday life without asking what it could mean."),
            ("p", "His first objection is that it means nothing. The value of a commodity is "
                  "measured by the labour it contains. So the value of a twelve-hour day "
                  "would be the twelve hours a twelve-hour day contains, which he calls "
                  "&ldquo;an absurd tautology&rdquo;. His second is sharper. Suppose a "
                  "twelve-hour day is embodied in 6s. If the worker is paid 6s, equivalents "
                  "are exchanged and nothing is left over, so the money never becomes "
                  "capital. If he is paid less than 6s, twelve hours of labour are exchanged "
                  "for fewer, and the law that equal values exchange is broken in the very "
                  "act it was meant to govern. Either way the phrase defeats itself."),
            ("p", "<strong>Volume I, Chapter 19.</strong> &ldquo;That which comes directly "
                  "face to face with the possessor of money on the market, is in fact not "
                  "labour, but the labourer. What the latter sells is his labour-power. As "
                  "soon as his labour actually begins, it has already ceased to belong to "
                  "him; it can therefore no longer be sold by him. Labour is the substance, "
                  "and the immanent measure of value, but has itself no value.&rdquo;"),
            ("p", "Read the middle sentence twice. Labour, the activity, does not exist yet "
                  "when the bargain is struck, and once it begins it belongs to the buyer. "
                  "What exists at the moment of sale is the worker's capacity. Marx then "
                  "tells how the classical economists half found this out. They asked what "
                  "regulates the price of labour around which market prices swing, called "
                  "it the &ldquo;natural price&rdquo;, and looked for it in the cost of "
                  "production. But the cost of producing labour is a circle, so without "
                  "noticing they asked instead what it costs to produce the labourer. That "
                  "is the value of labour-power, &ldquo;as different from its function, "
                  "labour, as a machine is from the work it performs&rdquo;. They reached "
                  "the right category and kept the wrong name for it."),
            ("p", "Now Marx's figures, which the lab reproduces. The working day is 12 hours. "
                  "The daily value of labour-power is 3s, the money form of 6 hours of "
                  "labour. Write that as a price of labour and you get the formula he gives: "
                  "twelve hours' labour has a value of 3s, so an hour costs `3s/12`, which "
                  "is 3d. But the labour-power works for 12 hours, and an hour of labour "
                  "creates 6d of new value in this example, so the day creates 6s. Marx "
                  "calls it &ldquo;a result absurd at first sight&mdash;that labour which "
                  "creates a value of 6s. possesses a value of 3s.&rdquo; The lab prints the "
                  "two numbers side by side in the marx preset: 3d an hour paid, 6d an hour "
                  "created. The equivalents preset pays the full 6s, and the price of an "
                  "hour rises to the 6d it creates."),
            ("p", "The difference is not hidden in any one hour. The 3s pays for 6 hours, "
                  "and it appears as the price of all 12. Marx compares three ways of "
                  "dividing a day. Under the corvée the serf works for himself on some days "
                  "and for the lord on others, in plain sight. Under slavery even the hours "
                  "in which the slave replaces his own keep appear as labour for the master. "
                  "&ldquo;In wage-labour, on the contrary, even surplus labour, or unpaid "
                  "labour, appears as paid.&rdquo; The money relation does for the wage "
                  "worker what the property relation does for the slave, in the opposite "
                  "direction."),
            ("p", "Why would anyone see it otherwise? Marx gives the appearance its due. "
                  "Money is handed over for something that is not money, as in every sale. "
                  "The worker is paid after the work is done, the way a debt is paid after "
                  "the goods are delivered. And what the buyer actually receives is "
                  "tailoring or spinning, a definite useful labour. From the worker's side, "
                  "he always gives 12 hours, and if the value of his labour-power moves from "
                  "3s to 4s or down to 2s, he sees the price of his twelve hours move. That "
                  "misled Adam Smith, Marx says, into treating the value of labour as "
                  "constant and the money as what varies. The dearer and cheaper presets "
                  "make the change: labour-power worth 4s gives 4d an hour, worth 2s gives "
                  "2d, and the twelve hours create 6s throughout. The capitalist, for his part, "
                  "explains his profit by buying cheap and selling dear, and never asks "
                  "where it would come from if labour really were paid its value."),
            ("p", "Two everyday facts seem to prove that labour, not labour-power, is paid. "
                  "Wages rise when the day is longer: but it also costs more to hire a "
                  "machine for a week than for a day, and nobody concludes that the machine's "
                  "work rather than the machine is being hired. And workers doing the same "
                  "job are paid differently: but the same differences existed under slavery, "
                  "where labour-power was sold openly, and there they fell on the owner "
                  "instead of the worker."),
            ("p", "The strongest objection comes from the economics that followed. John Bates "
                  "Clark, the American economist, argued in 1899 that under competition the "
                  "wage equals the value of what the last worker hired adds to the product, "
                  "the marginal product of labour. On that account the worker is paid for "
                  "what his labour contributes, and nothing is unpaid: the rest of the "
                  "product is what capital contributes and is paid for in turn. Marx's 6s "
                  "against 3s depends on counting the whole new value as labour's creation, "
                  "which is the labour theory of value from Commodities and Money. The lab "
                  "computes on Marx's definition and cannot decide between the two."),
            ("p", "With the wage named for what it is, the two forms it takes come next. "
                  "“Time-Wages” asks how the price of an hour is computed, and what happens "
                  "to it and to the day's wage when the day gets longer or shorter."),
        ],
        "lab": ("capkit", {
            "mode": "wages",
            "view": "form",
            "money_unit": "s",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's figures: 3s for a 12-hour day, an hour creates 6d",
                 "lp_value": 3, "normal_hours": 12, "value_per_hour": "1/2", "expect": {"waHourPrice": "3d", "waValueCreated": "6s in 12 h (6d an hour)"}},
                {"id": "equivalents", "label": "Equivalents exchanged: 6s for the 12 hours",
                 "lp_value": 6, "normal_hours": 12, "value_per_hour": "1/2", "expect": {"waHourPrice": "6d", "waValueCreated": "6s in 12 h (6d an hour)"}},
                {"id": "dearer", "label": "Subsistence dearer: labour-power worth 4s a day",
                 "lp_value": 4, "normal_hours": 12, "value_per_hour": "1/2", "expect": {"waHourPrice": "4d"}},
                {"id": "cheaper", "label": "Subsistence cheaper: labour-power worth 2s a day",
                 "lp_value": 2, "normal_hours": 12, "value_per_hour": "1/2", "expect": {"waHourPrice": "2d"}},
            ],
            "panel_title": "What an hour seems to cost, and what it creates",
            "panel_intro": (
                "Money is in shillings and pence, 12d to the shilling, so 6d is entered as "
                "1/2. The lab divides the daily value of labour-power by the hours and sets "
                "the result beside the value the hours create. Step through the presets: the "
                "twelve hours and the 6s they create never move, while the apparent price "
                "of an hour does."
            ),
        }),
        "steps_title": "Reading a wage as Marx reads it",
        "steps_intro": "Four steps, for any day's wage paid by time.",
        "steps": [
            ("Find the daily value of labour-power",
             "It is the value of the worker's daily means of subsistence, here 3s, the "
             "money form of 6 hours of labour."),
            ("Divide by the hours of the day",
             "The wage form presents that value as the price of every hour worked: 3s over "
             "12 hours is 3d an hour."),
            ("Compute the value the hours create",
             "Multiply the hours by the value an hour creates. Twelve hours at 6d create "
             "6s, whatever the wage."),
            ("Compare the two",
             "The difference, 3s, is surplus value. It does not appear on the payslip, "
             "because the wage form shows every hour as paid."),
        ],
        "worked": {
            "title": "Twelve hours for three shillings",
            "intro": [
                "Take Marx's figures. A day's labour-power is worth 3s, the product of 6 "
                "hours. It is set to work for 12 hours, and each hour creates 6d. You want "
                "the apparent price of an hour and what the day leaves unpaid.",
            ],
            "lines": [
                "wage for the day:  3s = 36d",
                "apparent price of an hour:  36d / 12 = 3d",
                "value created in an hour:  6d",
                "value created in the day:  12 · 6d = 72d = 6s",
                "unpaid:  6s − 3s = 3s, or 3d in every hour",
            ],
            "after": [
                "Half of each hour is paid and half is not, or the first 6 hours are paid and "
                "the last 6 are not; Marx says the two ways of putting it come to the same. "
                "In the equivalents preset the worker receives the full 6s, the price of an "
                "hour equals the value it creates, and there is no surplus value for the 6s "
                "to become capital with.",
            ],
        },
        "quiz_title": "The wage and what it hides",
        "quiz": [
            {"q": "A day's labour-power is worth 4s and the working day is 12 hours. Each "
                  "hour creates 6d. What is the apparent price of an hour?",
             "a": ["4d", "6d", "3d", "8d"],
             "c": 0,
             "why": "The wage form divides the day's value of labour-power by the hours: "
                    "48d over 12 is 4d. Sixpence is what an hour creates, not what it is "
                    "paid. Threepence is the figure when labour-power is worth 3s, and 8d "
                    "would need a wage of 8s."},
            {"q": "On Marx's account, what does the worker sell to the capitalist?",
             "a": ["Labour, at so much an hour",
                   "Labour-power, for a stated period",
                   "The finished product, at its value",
                   "A share of the product, paid in advance"],
             "c": 1,
             "why": "Labour does not exist when the bargain is struck and belongs to the "
                    "buyer once it starts, so it cannot be what is sold. The product belongs "
                    "to the capitalist from the outset. Wages are paid after the work, not in "
                    "advance, and they are the price of the capacity to work."},
            {"q": "Suppose the worker were paid 6s for the twelve hours, the whole value they "
                  "create. What follows on the chapter's argument?",
             "a": ["The rate of surplus value is 100%",
                   "The capitalist makes 3s",
                   "There is no surplus value, so the 6s does not become capital",
                   "The worker is paid less than the value of labour-power"],
             "c": 2,
             "why": "If equivalents are exchanged hour for hour, the price of the labour "
                    "equals the price of its product and nothing is left over. Marx says "
                    "the basis of capitalist production then vanishes. The 3s and the 100% "
                    "belong to the 3s wage, and 6s is more than the 3s value of labour-power, "
                    "not less."},
            {"q": "Under which arrangement does the worker's labour for himself stand "
                  "visibly apart, in time and place, from his labour for another?",
             "a": ["Slavery", "The corvée", "Wage-labour by time", "Wage-labour by the piece"],
             "c": 1,
             "why": "Under the corvée the serf works his own land on some days and the "
                    "lord's on others. Under slavery all labour appears unpaid; under "
                    "wage-labour, whether by time or by the piece, all of it appears paid."},
        ],
        "mistakes": [
            ("Taking the wage as the price of the work done",
             "The wage form invites it, and Marx's tiles refute it. At 3s for 12 hours the "
             "apparent price of an hour is 3d while the hour creates 6d. If the wage really "
             "were the price of the work, the worker would receive the 6s, as in the "
             "equivalents preset, and there would be no surplus value and no capital. What "
             "is bought is labour-power, for 3s, and its use for 12 hours creates 6s."),
            ("Thinking the value of labour is fixed and the money varies",
             "This is the error Marx finds in Adam Smith. The worker always gives 12 hours, "
             "so when his wage moves from 3s to 4s it looks as if the price of a constant "
             "thing changed. In the dearer and cheaper presets the hours and the 6s they "
             "create stay put; what moves is the value of labour-power, and the apparent "
             "price of an hour moves with it, from 2d to 4d."),
            ("Reading higher pay for a longer day as proof that labour is paid",
             "A longer day is paid more, but it also costs more to hire a machine for a "
             "week than for a day. That shows the hire is for a period of use, not that the "
             "machine's work is being bought at its value. The same holds of labour-power."),
        ],
        "standard": (
            "Finish when you can separate the price of an hour from the value it creates.",
            "Given the daily value of labour-power, the hours of the day and the value an "
            "hour creates, compute the apparent price of an hour and the value the day "
            "creates, and state the difference as the unpaid part of the day."
        ),
        "note": (
            "The figures are Marx's, and the 6d an hour creates is an input: the lab takes it "
            "from the chapter and does not derive it. That an hour of labour creates value "
            "in proportion to its length is the labour theory of value, which marginal "
            "productivity theory replaces with the claim that each factor is paid what it "
            "adds. The lab computes the unpaid part on Marx's definitions; whether those "
            "definitions are right is what the two theories dispute."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Kerr vol. 1, l. 4011 (10, 12 and 15 hours); l. 4019 (short time);
    # l. 4043 (the full-priced bakers).
    {
        "slug": "time-wages",
        "title": "Time-Wages",
        "module": "Chapter 20 · Time-Wages",
        "one_line": "The price of an hour is the day's value of labour-power over the hours of the normal day, so the same daily wage can hide a falling price of labour.",
        "summary": (
            "A time-wage is the value of labour-power paid by the day or the week, and its "
            "unit is the price of an hour. Compute that price from Marx's 3s and the length "
            "of the normal day, then the day's wage when the hours worked differ from the "
            "normal day, longer in overtime and shorter in short time."
        ),
        "key": [
            "price of an hour = day's value / normal hours",
            "3s over 10 hours: 3 3/5 d an hour",
            "3s over 12 hours: 3d;  over 15: 2 2/5 d",
            "day's wage = price of an hour × hours worked",
            "short time: 6 hours at 3d = 1s 6d",
        ],
        "key_label": "Time-wages in five lines",
        "concepts_intro": (
            "Marx says the laws of Chapter 17 pass over into laws of wages by a change of "
            "form, so he limits himself to what is peculiar to time-wages. Three ideas carry "
            "it."
        ),
        "concepts": [
            ("Nominal wage and price of labour",
             "The nominal wage is the sum received for a day or a week. The price of labour "
             "is that sum divided by the hours. The same daily wage can stand for very "
             "different prices of labour."),
            ("The unit measure",
             "The price of an hour is the daily value of labour-power divided by the hours "
             "of the normal working day. It is computed from the normal day, not from the "
             "hours this worker happens to work."),
            ("Overtime and short time",
             "Paid at that hourly price, a longer day raises the daily wage and a shorter "
             "one cuts it below the value of labour-power. Both sources of suffering, "
             "over-work and under-employment, come from the same quotient."),
        ],
        "read_title": "Marx's three working days",
        "read_intro": (
            "The passage works one fraction three times with the same numerator, which is "
            "the whole argument of the chapter in miniature."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 20.</strong> &ldquo;If, e.g., the habitual "
                  "working-day is 10 hours and the daily value of the labour-power 3s., the "
                  "price of the working hour is 3 3/5d. It falls to 3d. as soon as the "
                  "working-day rises to 12 hours, to 2 2/5 d. as soon as it rises to 15 "
                  "hours. Daily or weekly wages remain, despite all this, unchanged.&rdquo;"),
            ("p", "Suppose two jobs are offered at the same weekly wage. Before you choose, "
                  "you want to know the hours, because the same money for more hours is "
                  "less money for each one. That is the distinction Marx draws first: the "
                  "nominal wage, the sum received, against the price of labour, the sum for "
                  "a given quantity of labour. To find the second you divide the first by "
                  "the hours. More exactly, the unit measure is the daily value of "
                  "labour-power divided by the number of hours in the normal working day."),
            ("p", "Now the passage. The numerator is 3s, which is 36d, and it does not move. "
                  "Over 10 hours it gives `36/10` pence, which is 3 3/5d an hour. Over 12 "
                  "hours it gives 3d, and over 15 hours 2 2/5d. Every day pays 3s. A "
                  "worker whose employer lengthens the habitual day from 10 hours to 15 "
                  "takes home the same money, and the price of his labour has fallen by a "
                  "third. Nothing on the payslip records it. The lab's normal preset is the "
                  "12-hour day, 3d an hour and 3s a day; the ten-hour preset is the 10-hour "
                  "day, 3 3/5d an hour and the same 3s."),
            ("p", "The same fraction works the other way. Keep the price at 3 3/5d and let "
                  "the worker put in 12 hours because trade is brisk: the daily wage rises "
                  "to 3s 7 1/5d, the overtime preset, and the price of labour has not "
                  "changed at all. A higher "
                  "intensity of work would do the same, and so would the wife and children "
                  "going to work beside the head of the family. Marx states the general law "
                  "plainly: given the hours, the wage depends on the price of labour; given "
                  "the price of labour, the wage depends on the hours."),
            ("p", "Then short time. Take a 12-hour normal day at 3s, so 3d an hour, of which "
                  "each hour creates 6d. If the worker is employed only 6 or 8 hours, he "
                  "receives &ldquo;with this price of labour, only 2s. or 1s. 6d. a "
                  "day.&rdquo; He works half of every hour for himself and half for the "
                  "capitalist, so to earn the value of 6 hours he must be employed 12. The "
                  "short-time preset prints his 1s 6d for 6 hours. In "
                  "earlier chapters the damage came from over-work; here, Marx says, we find "
                  "&ldquo;the sources of the sufferings that result to the labourer from his "
                  "insufficient employment.&rdquo;"),
            ("p", "This is why the hour-wage mattered so much in practice. If the employer "
                  "promises only so much an hour for the hours he chooses, the fraction loses "
                  "its denominator: there is no longer a definite normal day, and the link "
                  "between paid and unpaid labour is cut. He can alternate over-work with "
                  "idleness at his convenience. Marx calls the 1860 revolt of the London "
                  "building workers against the hour system &ldquo;perfectly "
                  "rational&rdquo;, and says the legal limitation of the day put an end to "
                  "that particular mischief."),
            ("p", "Overtime is the reverse case. In trades with no legal limit a custom grew "
                  "up of a normal day of, say, ten hours, with the hours beyond it paid "
                  "better. Marx takes the employer at his word and computes. If an hour of "
                  "the normal day is paid 3d and creates 6d, the employer keeps half of it. "
                  "If an overtime hour is paid 4d, the extra pay still leaves him a third "
                  "of the 6d. Better-paid overtime is still partly unpaid labour, and where "
                  "the normal hour is paid low enough, the worker cannot live without the "
                  "overtime."),
            ("p", "Competition finishes the movement. A low price of labour pushes the day "
                  "longer, a longer day lowers the price of labour, and an employer who gets "
                  "unpaid hours beyond the average can pass some of them on to his customers "
                  "as a lower price. Marx's witnesses are the London master bakers who sold "
                  "at the full price, complaining to a parliamentary inquiry about the "
                  "undersellers, who in their words were &ldquo;getting 18 hours' work out "
                  "of their men for 12 hours' wages.&rdquo;"),
            ("p", "Marx calls their complaint a jeremiad and enjoys it. The full-priced "
                  "bakers think the normal day is fully paid and only the extra hours are "
                  "stolen. Surplus labour inside the normal day does not exist for them, "
                  "because they believe the day's wage paid for it."),
            ("p", "The objection worth stating comes from later labour economics, which "
                  "treats the hourly wage as a price and the hours as the worker's own "
                  "choice between income and leisure. Lionel Robbins showed in 1930 that a "
                  "rise in the hourly wage can lead a worker to choose more hours or fewer, "
                  "depending on how much he values the extra income. On that view the "
                  "length of the day reflects preferences. Marx's chapter assumes the "
                  "opposite, that the normal day is fixed by the employer, by custom and by "
                  "law, and that the worker takes it or leaves the job."),
            ("p", "Time-wages measure labour by its duration. The next lesson, "
                  "“Piece-Wages”, asks what changes when labour is measured instead by the "
                  "pieces it turns out."),
        ],
        "lab": ("capkit", {
            "mode": "wages",
            "view": "time",
            "money_unit": "s",
            "preset": "normal",
            "presets": [
                {"id": "normal", "label": "Marx's figures: 3s for a normal day of 12 hours, 12 worked",
                 "lp_value": 3, "normal_hours": 12, "hours_worked": 12, "expect": {"waHourPrice": "3d", "waDaily": "3s"}},
                {"id": "ten-hour", "label": "Marx's figures: 3s for a normal day of 10 hours, 10 worked",
                 "lp_value": 3, "normal_hours": 10, "hours_worked": 10, "expect": {"waHourPrice": "3 3/5 d", "waDaily": "3s"}},
                {"id": "overtime", "label": "Marx's figures: a 10-hour normal day, 12 hours worked at the same price",
                 "lp_value": 3, "normal_hours": 10, "hours_worked": 12, "expect": {"waHourPrice": "3 3/5 d", "waDaily": "3s 7 1/5 d"}},
                {"id": "short-time", "label": "Marx's figures: a 12-hour normal day, only 6 hours worked",
                 "lp_value": 3, "normal_hours": 12, "hours_worked": 6, "expect": {"waHourPrice": "3d", "waDaily": "1s 6d"}},
            ],
            "panel_title": "The price of an hour and the day's wage",
            "panel_intro": (
                "Money is in shillings: the daily value of labour-power is 3s. The lab "
                "divides it by the hours of the normal day to get the price of an hour, then "
                "multiplies by the hours actually worked. Compare normal with ten-hour, and "
                "then overtime and short time with the day they depart from."
            ),
        }),
        "steps_title": "Computing a time-wage",
        "steps_intro": "Four steps, using the normal day as the denominator.",
        "steps": [
            ("Fix the daily value of labour-power",
             "It is the numerator throughout. Convert it to pence if the answer will be in "
             "pence: 3s is 36d."),
            ("Divide by the normal day",
             "The price of an hour is the daily value over the hours of the normal working "
             "day: 36d over 10 hours is 3 3/5d."),
            ("Multiply by the hours worked",
             "The day's wage is the price of an hour times the hours actually worked, "
             "longer than the normal day in overtime and shorter in short time."),
            ("Compare with the daily value",
             "A day's wage below the daily value of labour-power means the worker is not "
             "paid enough to reproduce his labour-power; above it means more hours or a "
             "higher price, and the steps say which."),
        ],
        "worked": {
            "title": "The same 3s over three working days",
            "intro": [
                "Marx keeps the daily value of labour-power at 3s and lengthens the habitual "
                "day from 10 hours to 12 and then to 15. You want the price of an hour each "
                "time, and the wage of a man paid the 10-hour price for 12 hours.",
            ],
            "lines": [
                "10 hours:  36d / 10 = 3 3/5 d an hour",
                "12 hours:  36d / 12 = 3d an hour",
                "15 hours:  36d / 15 = 2 2/5 d an hour",
                "12 hours at 3 3/5 d:  43 1/5 d = 3s 7 1/5 d",
            ],
            "after": [
                "Each habitual day pays 3s while the price of labour falls by a third. The "
                "last line runs the other way: the daily wage rises by 7 1/5d with no change "
                "in the price of labour, because the hours rose.",
            ],
        },
        "quiz_title": "Price of labour and day's wage",
        "quiz": [
            {"q": "The daily value of labour-power is 3s and the habitual working day is 15 "
                  "hours. What is the price of an hour?",
             "a": ["2 2/5d", "3d", "3 3/5d", "2½d"],
             "c": 0,
             "why": "Thirty-six pence over 15 hours is `36/15 = 12/5` pence, which is "
                    "2 2/5d. Threepence belongs to the 12-hour day and 3 3/5d to the 10-hour "
                    "day. Twopence halfpenny is 2.5d, a little more than the true 2.4d."},
            {"q": "A normal day of 12 hours is paid 3s, so 3d an hour. The worker is employed "
                  "only 8 hours. What is his day's wage?",
             "a": ["3s", "2s", "1s 6d", "2s 8d"],
             "c": 1,
             "why": "Eight hours at 3d is 24d, which is 2s, a shilling below the daily value "
                    "of labour-power. Three shillings would need the full 12 hours, 1s 6d is "
                    "the 6-hour case, and 2s 8d would need 4d an hour."},
            {"q": "A worker on a 10-hour normal day at 3s works 12 hours at the same price "
                  "per hour. Which statement is true?",
             "a": ["The price of labour rises to 3 3/5d from 3d",
                   "The daily wage rises to 3s 7 1/5d and the price of labour is unchanged",
                   "The daily wage stays at 3s",
                   "The price of labour falls to 3d"],
             "c": 1,
             "why": "The price of an hour stays at 3 3/5d, and 12 of them make 43 1/5d, which "
                    "is 3s 7 1/5d. The price falls to 3d only if 3s is spread over a 12-hour "
                    "habitual day, which is the other case in Marx's passage, and then the "
                    "wage stays at 3s."},
            {"q": "In Marx's overtime example a normal hour is paid 3d, an overtime hour 4d, "
                  "and every hour creates 6d. What share of an overtime hour is unpaid?",
             "a": ["None of it", "One half", "One third", "Two thirds"],
             "c": 2,
             "why": "Fourpence of the 6d is paid, so 2d, a third, is not. A half is unpaid in "
                    "the normal hour at 3d. Two thirds paid is the 4d, which is the paid "
                    "share, not the unpaid one."},
        ],
        "mistakes": [
            ("Taking a higher hourly rate for a better-paid worker",
             "The hourly rate is a quotient, and the day's wage depends on the hours too. "
             "The ten-hour preset pays 3 3/5d an hour, more than the normal preset's 3d, and "
             "its day's wage is the same 3s. In short time the rate stays at 3d and the day "
             "pays 1s 6d. A worker on 3 3/5d employed 6 hours would take home 1s 9 3/5d, "
             "less than the worker on 3d employed 12."),
            ("Thinking better-paid overtime is fully paid labour",
             "Overtime at 4d looks generous against a normal 3d, but an hour creates 6d. "
             "The employer keeps a third of the overtime hour instead of half of the normal "
             "one. Extra pay reduces the unpaid share; it does not remove it."),
            ("Computing the price of an hour from the hours worked",
             "The unit measure divides by the normal day, not by this week's hours. That is "
             "why short time at 3d an hour leaves the worker below the value of his "
             "labour-power: had the denominator been the 6 hours worked, the day would have "
             "paid 3s. The hour system broke exactly this link."),
        ],
        "standard": (
            "Finish when you can compute an hourly price and a day's wage from a time-wage.",
            "Given the daily value of labour-power, the hours of the normal day and the "
            "hours worked, compute the price of an hour and the day's wage, and state "
            "whether the wage is below, at or above the daily value of labour-power."
        ),
        "note": (
            "Every preset uses Marx's own figures. The lab pays every hour at the normal "
            "hourly price; it does not model a separate overtime rate, which is why the 4d "
            "overtime hour is worked in the prose. It also takes the daily value of "
            "labour-power as fixed, while Marx notes that it rises with the wear of a longer "
            "day, so a lengthened day at a constant price is a further fall in the price of "
            "labour that no tile shows."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Kerr vol. 1, l. 4053 (piece-wages a converted form of time-wages);
    # l. 4065 (24 pieces); l. 4097 (48 pieces, 1½d. to ¾d.); l. 4097
    # (the operatives watch prices).
    {
        "slug": "piece-wages",
        "title": "Piece-Wages",
        "module": "Chapter 21 · Piece-Wages",
        "one_line": "A piece-rate is the time-wage divided by the pieces a normal day yields, so when the normal output rises the rate falls and the day pays the same.",
        "summary": (
            "Piece-wages look like payment for what the worker produced, but the rate is set "
            "from the daily value of labour-power and the normal output of a day. Compute "
            "Marx's piece-rate of 1½d from 24 pieces and 3s, see what doubled output does to "
            "the day's wage at the old rate and at the new one, and find the speed-up hidden "
            "in a cut rate."
        ),
        "key": [
            "piece-rate = day's value / normal pieces",
            "3s / 24 pieces = 1½d a piece",
            "a piece creates 3d and is paid 1½d",
            "48 pieces: the rate falls to ¾d",
            "48 · ¾d = 24 · 1½d = 3s",
        ],
        "key_label": "Piece-wages in five lines",
        "concepts_intro": (
            "Marx's claim is that nothing essential changes from time-wages; what changes is "
            "how the measure works on the worker. Three ideas carry the chapter."
        ),
        "concepts": [
            ("A converted form of time-wages",
             "The piece-rate is fixed so that a worker of average skill and intensity earns "
             "the daily value of labour-power in a normal day. It is the time-wage divided "
             "by the normal output."),
            ("The measure of intensity",
             "Only the time embodied in a quantity fixed beforehand by experience counts as "
             "socially necessary and is paid. The form of the wage controls quality and "
             "intensity, so much supervision becomes superfluous."),
            ("The rate follows productivity",
             "A piece-rate is the money form of a definite working time. When productivity "
             "doubles, a piece holds half the time and the rate halves, so the day's wage is "
             "unchanged."),
        ],
        "read_title": "One sentence of definition, then 24 pieces and 48",
        "read_intro": (
            "The chapter opens by denying that piece-wages are a new thing, and ends its "
            "arithmetic with the case that shows why."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 21.</strong> &ldquo;Wages by the piece are "
                  "nothing else than a converted form of wages by time, just as wages by time "
                  "are a converted form of the value or price of labour-power.&rdquo;"),
            ("p", "If you have been paid per delivery, per item packed or per article "
                  "written, you know the feeling this form gives: that you are being paid "
                  "for what you made, and that working harder pays more. Marx grants that "
                  "the appearance is strong. It looks as if what is bought is labour already "
                  "realised in a product, priced by the capacity of the producer, and not "
                  "labour-power priced by its daily value."),
            ("p", "His first shock to that confidence is simple. Both forms exist side by "
                  "side in the same trade. London compositors worked by the piece and "
                  "country ones by the day; in the same London saddlery shops the French "
                  "were paid by the piece and the English by time, often for the same work. "
                  "A difference in the form of payment that can be switched from one worker "
                  "to the next does not change what is being paid for."),
            ("p", "Then his figures. The ordinary day is 12 hours, 6 of them paid; it creates "
                  "6s of new value, so 6d an hour. A worker of average intensity and skill "
                  "turns out 24 pieces in the day. After the value of the means of "
                  "production is taken out, the 24 pieces are worth 6s, so a piece is worth "
                  "3d. The worker is paid 1½d a piece and earns 3s in 12 hours. Each piece is "
                  "half paid and half unpaid, exactly as each hour was in the time-wage. "
                  "The marx preset prints the 1½d and the 3s."),
            ("p", "So the piece-rate is the daily value of labour-power divided by the "
                  "pieces of a normal day: `36d/24 = 1½d`. Marx says the form is as "
                  "irrational as the time-wage. Two pieces are the product of an hour and "
                  "worth 6d, and the worker receives 3d for them. The piece-rate does not "
                  "measure the value of a piece by the time in it. It measures the time the "
                  "worker spent by the pieces he turned out."),
            ("p", "What piece-wages do is put the measure inside the wage. A piece below "
                  "average quality is not paid in full. In the large London tailoring shops "
                  "a waistcoat was called an hour or half an hour, at 6d the hour, and "
                  "master and worker argued over whether a new fashion was an hour's work "
                  "until experience settled it. A worker who could not reach the minimum was "
                  "dismissed. Supervision becomes largely unnecessary, and the form lends "
                  "itself to middlemen, in what England called the &ldquo;Sweating "
                  "system&rdquo;, where a "
                  "sub-contractor lives on the difference between the rate the capitalist "
                  "pays and the part he lets reach the worker."),
            ("p", "It is also the worker's own interest, now, to work harder and longer, "
                  "because his day's wage rises with his output. Individual earnings spread "
                  "out with skill, strength and stamina. Marx does not think this changes "
                  "the relation between wages and surplus value, because the surplus labour "
                  "each worker supplies rises with his wage. But the competition it sets up "
                  "among the workers tends, he says, to raise individual wages above the "
                  "average while lowering the average itself. The speed-up preset shows how "
                  "the rate can follow: a worker pushes his output from 24 pieces to 30, the "
                  "rate is cut from 1½d to 1 1/5d, and the day pays 3s as before."),
            ("p", "<strong>Volume I, Chapter 21.</strong> &ldquo;If the same working day now "
                  "supplies, in consequence of the doubled productiveness of labour, 48 "
                  "pieces instead of 24, and all other circumstances remain unchanged, then "
                  "the piece-wage falls from 1½d. to ¾d., as every piece now only represents "
                  "¼, instead of ½ of a working hour.&rdquo;"),
            ("p", "This is where the appearance and the reality part. The lab's faster preset "
                  "is the worker's reading: 48 pieces at the old 1½d make 6s, and he expects "
                  "to be paid for his product. The cut preset is the capitalist's: the normal "
                  "day now yields 48, so the rate is 3s over 48, ¾d, and the day pays 3s "
                  "again. `24 · 1½d = 48 · ¾d = 3s`. Marx calls the change &ldquo;so far "
                  "purely nominal&rdquo;, and notes that it is where the fights start, since "
                  "employers use it as a pretext for real cuts, or the higher productivity "
                  "comes with more intensity."),
            ("p", "Some workers did take the appearance seriously. Marx quotes operatives who "
                  "&ldquo;carefully watch the price of the raw material and the price of "
                  "manufactured goods&rdquo; and so could estimate their master's profits. "
                  "He adds, dryly, that the capitalist rightly knocks such pretensions on "
                  "the head as gross errors about the nature of wage-labour, and declares "
                  "that the productivity of labour is none of the labourer's concern."),
            ("p", "Modern labour economics reads piece-rates more kindly. Edward Lazear's "
                  "study of a firm that installed car windscreens, published in 2000, found "
                  "that moving from hourly pay to piece-rates raised output per worker "
                  "substantially, partly through effort and partly by attracting faster "
                  "workers, and that pay rose with it. The same literature knows Marx's "
                  "problem under another name, the ratchet effect: workers hold back output "
                  "when they expect the rate to be cut once they show what they can do. "
                  "Whether rates are cut after output rises is a question about particular "
                  "firms that this chapter's arithmetic cannot answer."),
            ("p", "The last two lessons compared wages inside one country. The next, "
                  "“National Differences of Wages”, asks what the same reasoning says when "
                  "the wages of two countries are set side by side."),
        ],
        "lab": ("capkit", {
            "mode": "wages",
            "view": "piece",
            "money_unit": "s",
            "qty_unit": "pieces",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's figures: 3s a day, 24 pieces in a normal day of 12 hours",
                 "lp_value": 3, "normal_hours": 12, "pieces_normal": 24, "pieces_actual": 24,
                 "rate_cut_to": "", "expect": {"waPieceRate": "1½d", "waDaily": "3s"}},
                {"id": "faster", "label": "Marx's figures: 48 pieces made, the old rate still paid",
                 "lp_value": 3, "normal_hours": 12, "pieces_normal": 24, "pieces_actual": 48,
                 "rate_cut_to": "", "expect": {"waPieceRate": "1½d", "waDaily": "6s"}},
                {"id": "cut", "label": "Marx's figures: 48 pieces is the new normal day",
                 "lp_value": 3, "normal_hours": 12, "pieces_normal": 48, "pieces_actual": 48,
                 "rate_cut_to": "", "expect": {"waPieceRate": "¾d", "waDaily": "3s"}},
                {"id": "speed-up", "label": "Speed-up: 30 pieces made, the rate cut to 1 1/5d",
                 "lp_value": 3, "normal_hours": 12, "pieces_normal": 24, "pieces_actual": 30,
                 "rate_cut_to": "1/10", "expect": {"waPieceRate": "1 1/5 d", "waDaily": "3s"}},
            ],
            "panel_title": "The piece-rate and the day's wage",
            "panel_intro": (
                "Money is in shillings, so a rate cut to 1 1/5d is entered as 1/10 of a "
                "shilling; leave the cut empty for none. The lab divides the daily value of "
                "labour-power by the pieces of a normal day and pays the pieces actually "
                "made at that rate, or at the cut rate. Compare faster with cut: the same 48 "
                "pieces, two readings of what they should earn."
            ),
        }),
        "steps_title": "Computing a piece-rate",
        "steps_intro": "Four steps, starting from the time-wage the piece-rate converts.",
        "steps": [
            ("Fix the daily value of labour-power",
             "It is the same numerator as in the time-wage: 3s, or 36d."),
            ("Find the normal output",
             "The pieces a worker of average skill and intensity turns out in the normal day, "
             "fixed beforehand by experience: 24 in Marx's example."),
            ("Divide for the rate",
             "The piece-rate is the daily value over the normal output: 36d over 24 is 1½d."),
            ("Pay the pieces made",
             "The day's wage is the rate times the pieces actually made, at the rate in "
             "force. If the normal output changes, recompute the rate first."),
        ],
        "worked": {
            "title": "Twenty-four pieces, then forty-eight",
            "intro": [
                "Marx's worker makes 24 pieces in a 12-hour day on a time-wage of 3s. "
                "Productivity then doubles. You want the rate before and after, and the day's "
                "wage each way.",
            ],
            "lines": [
                "rate:  36d / 24 = 1½d a piece",
                "value of a piece:  6s / 24 = 3d",
                "day's wage:  24 · 1½d = 36d = 3s",
                "doubled:  36d / 48 = ¾d a piece",
                "day's wage:  48 · ¾d = 36d = 3s",
            ],
            "after": [
                "Paid at the old rate, the 48 pieces would bring 6s, which is what the worker "
                "expects. The rate falls in the same proportion as the output rises, because "
                "a piece now holds a quarter of an hour of labour instead of half.",
            ],
        },
        "quiz_title": "Rates, pieces and days",
        "quiz": [
            {"q": "The daily value of labour-power is 3s and a normal day yields 36 pieces. "
                  "What is the piece-rate?",
             "a": ["1d", "1½d", "¾d", "2d"],
             "c": 0,
             "why": "Thirty-six pence over 36 pieces is 1d. One and a half pence is the rate "
                    "for 24 pieces and ¾d for 48. Twopence would need 18 pieces."},
            {"q": "In Marx's example, what is a piece worth after the means of production are "
                  "taken out, and what is the worker paid for it?",
             "a": ["Worth 1½d, paid 1½d",
                   "Worth 3d, paid 1½d",
                   "Worth 6d, paid 3d",
                   "Worth 3d, paid 3d"],
             "c": 1,
             "why": "The day's 6s of new value over 24 pieces is 3d a piece, and the rate is "
                    "1½d, so each piece is half paid. Sixpence and threepence are the value "
                    "and the pay of the two pieces made in one hour, not of one piece."},
            {"q": "Productivity doubles and the normal day now yields 48 pieces. What does the "
                  "day pay at the new rate?",
             "a": ["6s", "3s", "1s 6d", "4s 6d"],
             "c": 1,
             "why": "The rate falls to 3s over 48, ¾d, and 48 pieces at ¾d make 3s. Six "
                    "shillings is 48 pieces at the old 1½d, which the worker expects and does "
                    "not get. The other two match no rate in the example."},
            {"q": "Which of these does Marx count among the peculiarities of piece-wages?",
             "a": ["They abolish the unpaid part of the day",
                   "They give the capitalist an exact measure of the intensity of labour",
                   "They pay for labour already realised in the product",
                   "They always raise the average wage of a trade"],
             "c": 1,
             "why": "Only time embodied in an output fixed beforehand counts and is paid, so "
                    "the wage itself measures intensity. Each piece is still half unpaid. "
                    "Payment for realised labour is the appearance Marx denies, and he says "
                    "piece-work tends to lower the average wage, not raise it."},
        ],
        "mistakes": [
            ("Believing piece-wages pay for the worker's actual effort",
             "The cut preset answers it: the worker makes twice as many pieces and the day "
             "pays 3s, exactly as before, because the rate fell from 1½d to ¾d. The rate was "
             "set from the daily value of labour-power and the normal output, and it follows "
             "them, not the effort. In the speed-up preset 30 pieces at a rate cut to 1 1/5d "
             "also pay 3s: more effort, the same day's wage."),
            ("Reading the piece-rate as the value of a piece",
             "A piece is worth 3d of new value and is paid 1½d. Piece-wages, Marx says, do "
             "not express any relation of value directly; they measure the worker's time by "
             "his output."),
            ("Thinking a fast worker's higher pay changes the rate of exploitation",
             "A worker above the average earns more, and supplies proportionally more "
             "surplus labour, since each of his pieces is half paid like anyone's. The "
             "proportion between wages and surplus value is unchanged; what changes is the "
             "competition between workers."),
        ],
        "standard": (
            "Finish when you can compute a piece-rate and the day's wage it pays.",
            "Given the daily value of labour-power, the normal output and the pieces made, "
            "compute the piece-rate and the day's wage, and recompute both when the normal "
            "output changes or the rate is cut."
        ),
        "note": (
            "The marx, faster and cut presets use Marx's figures; the speed-up is "
            "illustrative. The lab takes the daily value of labour-power as fixed when "
            "output rises. Marx's own example assumes that too, and he notes that higher "
            "productivity in practice often came with higher intensity, which would raise "
            "the wear on labour-power and, on his definitions, its value."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Kerr vol. 1, l. 4111 (the scale of national intensities); l. 4117
    # (nominal and real wages); l. 4119 (the relative price of labour);
    # l. 4121 (Cowell).
    {
        "slug": "national-differences-of-wages",
        "title": "National Differences of Wages",
        "module": "Chapter 22 · National Differences of Wages",
        "one_line": "A country can pay higher wages and still pay less per unit of output, so the higher money wage may come with the higher rate of surplus value.",
        "summary": (
            "Chapter 22 compares wages across countries and finds that the comparison has to "
            "be made per unit of product. Compute two countries' wages per unit of output "
            "from their hourly wages and outputs, and their rates of surplus value from the "
            "world-market value of a unit."
        ),
        "key": [
            "compare per unit of output, not per day",
            "wage per unit = hourly wage / output",
            "relative wage = per unit here / per unit there",
            "s′ = (output × unit value − wage) / wage",
            "dearer by the day, cheaper by the piece",
        ],
        "key_label": "Comparing two countries",
        "concepts_intro": (
            "The chapter is six pages long, and most of it is evidence. The argument it "
            "supports has three parts."
        ),
        "concepts": [
            ("Reduce to the same terms",
             "A fair comparison first brings day-wages to a uniform working day, then turns "
             "time-wages into piece-wages, because only output measures the productivity and "
             "intensity of labour."),
            ("National labour on the world market",
             "Within a country, labour of average intensity counts as average. Between "
             "countries the national averages form a scale, and more intense or more "
             "productive national labour produces more value in the same time."),
            ("The relative price of labour",
             "The price of labour compared with the value of the product and with surplus "
             "value. A country can pay a higher day's wage and a lower relative price, which "
             "is what Marx says the English evidence shows."),
        ],
        "read_title": "The scale of national labours",
        "read_intro": (
            "The passage that carries the argument comes after Marx's list of everything a "
            "comparison of wages has to take into account."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 22.</strong> &ldquo;The average intensity of "
                  "labour changes from country to country; here it is greater, there less. "
                  "These national averages form a scale, whose unit of measure is the "
                  "average unit of universal labour. The more intense national labour, "
                  "therefore, as compared with the less intense, produces in the same time "
                  "more value, which expresses itself in more money.&rdquo;"),
            ("p", "You have probably heard wages compared across countries, usually by the "
                  "day or the hour, and usually to make a point about who is better off or "
                  "whose industry can compete. Marx's first move is to say that such "
                  "comparisons are not yet comparisons. Everything that determines the value "
                  "of labour-power differs between countries: the necessaries of life and "
                  "their prices, the cost of training, the part played by women's and "
                  "children's labour, productivity, the length and intensity of the day. "
                  "So the day-wages must first be brought to a uniform working day, and then "
                  "the time-wage turned into a piece-wage, since only output measures how "
                  "productive and how intense the labour is."),
            ("p", "Then the passage. Within one country, labour below the national average "
                  "intensity simply does not count as normal labour, and only intensity "
                  "above the average raises the value an hour creates. On the world market "
                  "the national averages themselves differ, and they form a scale. An hour "
                  "of more intense national labour creates more value than an hour of less "
                  "intense labour. Marx adds that on the world market the more productive "
                  "national labour also counts as more intense, so long as competition does "
                  "not force that nation to sell its goods down to their value."),
            ("p", "Two consequences follow. Money has a lower relative value in the country "
                  "with the more developed capitalist production, so its nominal wages are "
                  "higher, which proves nothing about real wages, the necessaries the money "
                  "buys. And even apart from that, the day's wage can be higher in the first "
                  "country while the price of labour measured against its product is lower:"),
            ("p", "<strong>Volume I, Chapter 22.</strong> &ldquo;&hellip; the relative price "
                  "of labour, i.e., the price of labour as compared both with surplus-value "
                  "and with the value of the product, stands higher in the second than in "
                  "the first.&rdquo;"),
            ("p", "Marx's evidence is English. J. W. Cowell of the Factory Commission of 1833 "
                  "concluded that &ldquo;in England wages are virtually lower to the "
                  "capitalist, though higher to the operative than on the Continent of "
                  "Europe.&rdquo; The factory inspector Alexander Redgrave reported in 1866 "
                  "that Continental labour, despite lower wages and much longer hours, was "
                  "dearer in proportion to its product. Redgrave's table counts spindles per "
                  "person: 14 in France, 37 in Prussia, 74 in Great Britain."),
            ("p", "The lab sets two countries side by side for one hour. England pays 6d an "
                  "hour and its spinner turns out 2 lb of yarn; the Continent pays 4d and "
                  "turns out 1 lb. The figures are illustrative. A pound of yarn is worth 8d "
                  "on the world market. Per pound, England pays 3d and the Continent 4d, so "
                  "England's relative wage is `3/4` of the Continent's. England's hour "
                  "creates 16d against a wage of 6d, a rate of surplus value of `10/6`, or "
                  "166.67%; the Continent's creates 8d against 4d, 100%. The country with the "
                  "higher money wage has the higher rate of surplus value. That is the "
                  "england-continent preset. In the same-intensity preset England's hour "
                  "turns out only 1 lb, its relative wage becomes `3/2` and its rate falls "
                  "to 33.33%. In the cheaper-goods preset competition forces the world value "
                  "of a pound down to 6d: the relative wage stays `3/4`, and the rates fall "
                  "to 100% for England and 50% for the Continent."),
            ("p", "English contractors building railways in Eastern Europe and Asia learned "
                  "this in practice, Marx says. They employed English navvies beside local "
                  "labourers, found that the higher English wages roughly matched the higher "
                  "intensity of their work, and lost nothing by it: the relative price of "
                  "labour generally moves in the opposite direction to the money wage."),
            ("p", "The chapter ends with the American economist Henry Carey, whose 1835 "
                  "<em>Essay on the Rate of Wages</em> argued that "
                  "the wages of different nations are proportional to the productivity of "
                  "their working days, and concluded that wages everywhere rise and fall "
                  "with productivity. Marx answers that the whole analysis of surplus value "
                  "shows the conclusion is absurd even if the premises were proved, and "
                  "accuses Carey of &ldquo;shuffling to and fro a confused mass of "
                  "statistical materials.&rdquo; Carey's premise has a long life, though. "
                  "Economists today compare countries by unit labour cost, the same wage "
                  "per unit of output Marx computes, and many argue, as Carey did, that real "
                  "wages track productivity across countries over the long run. The "
                  "disagreement is over the second tile, the rate of surplus value, which "
                  "only exists on Marx's definitions."),
            ("p", "That completes Part VI on wages. Part VII turns from the single exchange "
                  "of labour-power to its repetition, and the first lesson, “Simple "
                  "Reproduction”, asks what changes when the same process is simply run "
                  "again, year after year."),
        ],
        "lab": ("capkit", {
            "mode": "wages",
            "view": "national",
            "money_unit": "s",
            "qty_unit": "lb",
            "preset": "england-continent",
            "presets": [
                {"id": "england-continent",
                 "label": "England pays 1½ times the wage for twice the output",
                 "countries": [{"name": "England", "wage": "1/2", "output_per_hour": 2},
                               {"name": "Continent", "wage": "1/3", "output_per_hour": 1}],
                 "unit_value": "2/3", "expect": {"waRelative": "3/4", "waRate": "England 5/3 = 166.67%, Continent 1 = 100%"}},
                {"id": "same-intensity",
                 "label": "The same output an hour in both countries",
                 "countries": [{"name": "England", "wage": "1/2", "output_per_hour": 1},
                               {"name": "Continent", "wage": "1/3", "output_per_hour": 1}],
                 "unit_value": "2/3", "expect": {"waRelative": "3/2", "waRate": "England 1/3 = 33.33%, Continent 1 = 100%"}},
                {"id": "cheaper-goods",
                 "label": "Competition lowers the world value of a pound of yarn to 6d",
                 "countries": [{"name": "England", "wage": "1/2", "output_per_hour": 2},
                               {"name": "Continent", "wage": "1/3", "output_per_hour": 1}],
                 "unit_value": "1/2", "expect": {"waRelative": "3/4", "waRate": "England 1 = 100%, Continent 1/2 = 50%"}},
            ],
            "panel_title": "Two countries, one hour of spinning",
            "panel_intro": (
                "Each country is a name, an hourly wage in shillings (6d is 1/2) and the "
                "pounds of yarn an hour turns out; the last field is the value of a pound on "
                "the world market. The figures are illustrative. Compare the first two "
                "presets: the same wages, and only the output changes."
            ),
        }),
        "steps_title": "Comparing two countries' wages",
        "steps_intro": "Four steps, in the order Marx says the comparison must be made.",
        "steps": [
            ("Bring the wages to the same period",
             "Express both wages for the same unit of time, an hour or a uniform working "
             "day, so that a longer day does not pass for a higher wage."),
            ("Divide by output",
             "Wage per unit is the hourly wage over the units an hour turns out. This turns "
             "the time-wage into a piece-wage."),
            ("Compare per unit",
             "The relative wage is the first country's wage per unit over the second's. "
             "Below 1, the first country's labour is cheaper per unit, whatever its money "
             "wage."),
            ("Compute each rate of surplus value",
             "Value an hour's output at the world-market value of a unit, subtract the "
             "hourly wage, and divide by the wage."),
        ],
        "worked": {
            "title": "Sixpence against fourpence",
            "intro": [
                "England pays 6d an hour for 2 lb of yarn; the Continent pays 4d for 1 lb. A "
                "pound is worth 8d on the world market. You want the wage per pound, the "
                "relative wage and each rate of surplus value.",
            ],
            "lines": [
                "per lb:  England 6d / 2 = 3d;  Continent 4d / 1 = 4d",
                "relative wage:  3d / 4d = 3/4",
                "England:  (2 · 8d − 6d) / 6d = 10/6 = 166.67%",
                "Continent:  (8d − 4d) / 4d = 1 = 100%",
            ],
            "after": [
                "England's money wage is half as high again, its labour three quarters as "
                "dear per pound, and its rate of surplus value two thirds higher. Give "
                "England the Continent's output of 1 lb an hour and its rate falls to "
                "`(8 − 6)/6 = 1/3`: the higher wage alone means a lower rate only when "
                "output is the same.",
            ],
        },
        "quiz_title": "Wages per day and per piece",
        "quiz": [
            {"q": "Country A pays 9d an hour and an hour turns out 3 lb; country B pays 4d an "
                  "hour for 1 lb. What is A's relative wage, its wage per pound over B's?",
             "a": ["3/4", "9/4", "4/3", "3"],
             "c": 0,
             "why": "A pays 9d over 3 lb, 3d a pound; B pays 4d a pound; 3d over 4d is 3/4. "
                    "Nine fourths compares the hourly wages without the outputs, 4/3 is B "
                    "over A, and 3 is A's output over B's."},
            {"q": "In the england-continent preset, which country has the higher rate of "
                  "surplus value?",
             "a": ["England, at 166.67%",
                   "The Continent, at 166.67%",
                   "Both are 100%",
                   "The Continent, because its wage is lower"],
             "c": 0,
             "why": "England's hour creates 16d for a 6d wage, a rate of 10/6; the "
                    "Continent's creates 8d for 4d, a rate of 1. A lower money wage does not "
                    "mean a higher rate when the output an hour is lower too."},
            {"q": "Marx says nominal wages are higher in the nation with more developed "
                  "capitalist production. What does he say this does not prove?",
             "a": ["That its money has a lower relative value",
                   "That its real wages are higher",
                   "That its labour is more productive",
                   "That its day-wage is higher"],
             "c": 1,
             "why": "He says higher nominal wages do not prove that the means of subsistence "
                    "at the worker's disposal are greater. The lower relative value of money "
                    "is his explanation of the higher nominal wage, and the higher "
                    "productivity is its cause; the higher day-wage is the fact itself."},
            {"q": "Why must time-wages be turned into piece-wages before two countries' wages "
                  "are compared?",
             "a": ["Because piece-wages are always higher",
                   "Because only the piece-wage measures productivity and intensity",
                   "Because the Factory Acts required it",
                   "Because piece-wages contain no unpaid labour"],
             "c": 1,
             "why": "Marx says the piece-wage alone can measure both the productivity and the "
                    "intensity of labour, which is what differs between countries. Piece-wages "
                    "are not always higher, the Factory Acts have nothing to do with the "
                    "comparison, and a piece is half unpaid in Marx's example."},
        ],
        "mistakes": [
            ("Assuming a country with higher money wages has a lower rate of surplus value",
             "It holds only when output is the same, as in the same-intensity preset, where "
             "England's rate drops to 33.33%. In the england-continent preset England pays "
             "1½ times the wage for twice the output, its relative wage is 3/4, and its rate "
             "of surplus value is 166.67% against the Continent's 100%. The tile that "
             "decides is the wage per unit of output."),
            ("Comparing day-wages without a common working day",
             "A Continental day of fourteen hours and an English day of ten are not the same "
             "quantity of labour, so their wages are not the same kind of figure. Marx's "
             "first step is to reduce both to a uniform working day."),
            ("Taking a higher nominal wage for a higher real wage",
             "Money has a lower relative value where capitalist production is more "
             "developed. A higher money wage there may buy no more necessaries, and Marx "
             "says the nominal figure proves nothing about real wages."),
        ],
        "standard": (
            "Finish when you can compare two countries' wages per unit of output.",
            "Given two countries' hourly wages and outputs and the world-market value of a "
            "unit, compute each country's wage per unit, the relative wage, and each rate of "
            "surplus value, and state which country's labour is cheaper per unit."
        ),
        "note": (
            "The wages, outputs and unit values are illustrative; Marx gives evidence, not a "
            "worked example. The lab values both countries' output at one world-market price "
            "per unit, which is Marx's claim that more productive national labour counts as "
            "more intense on the world market. That claim is what makes England's rate "
            "higher, and it is the step a trade economist who explains wages by productivity "
            "would contest."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Kerr vol. 1, l. 4256 (the passage); l. 4244 (last week's labour);
    # l. 4254 (£1000 and £200); l. 4256 (not a single atom); l. 4278
    # (invisible threads); l. 4303 (reproduces the capitalist relation).
    {
        "slug": "simple-reproduction",
        "title": "Simple Reproduction",
        "module": "Chapter 23 · Simple Reproduction",
        "one_line": "Run the same capital again and again with the surplus value consumed, and after capital ÷ consumption years the capitalist has eaten a sum equal to what he advanced.",
        "summary": (
            "Chapter 23 repeats one year of production without growth and asks what the "
            "repetition alone changes. Compute how many years of consumed surplus value "
            "equal the capital advanced, see why Marx then calls the whole capital "
            "capitalised surplus value, and follow the same repetition as it reproduces the "
            "worker as a worker."
        ),
        "key": [
            "simple reproduction: all of s consumed",
            "years = capital / yearly surplus consumed",
            "£1,000 / £200 = 5 years",
            "the worker is paid from his past labour",
            "it reproduces capitalist and wage-worker",
        ],
        "key_label": "Chapter 23 in five lines",
        "concepts_intro": (
            "Part VII opens by doing nothing new: the capitalist spends all his surplus "
            "value and starts again on the same scale. Repetition turns out to change three "
            "things."
        ),
        "concepts": [
            ("Reproduction",
             "No society can stop producing, so every process of production is also one of "
             "reproduction. Under capitalism the value advanced is reproduced as capital and "
             "the surplus value becomes a regular revenue."),
            ("The worker's own labour pays him",
             "The worker is paid after he works. Viewed as a repeated process, his wages are "
             "a portion of the product he made in the previous period, flowing back to him "
             "in money."),
            ("The capital becomes capitalised surplus value",
             "Divide the capital by the surplus value consumed each year. After that many "
             "years the capitalist has consumed a sum equal to his original capital, and "
             "the capital he still holds equals the surplus value he appropriated."),
        ],
        "read_title": "The capitalist's reckoning, and Marx's",
        "read_intro": (
            "The passage sits in the middle of the chapter, right after the arithmetic. It "
            "is the step that makes the arithmetic matter."
        ),
        "body": [
            ("p", "<strong>Volume I, Chapter 23.</strong> &ldquo;The capitalist thinks, that "
                  "he is consuming the produce of the unpaid labour of others, i.e., the "
                  "surplus-value, and is keeping intact his original capital; but what he "
                  "thinks cannot alter facts. After the lapse of a certain number of years "
                  "the capital value he then possesses is equal to the sum total of the "
                  "surplus-value appropriated by him during those years, and the total value "
                  "he has consumed is equal to that of his original capital.&rdquo;"),
            ("p", "Marx starts further back. A society can no more stop producing than stop "
                  "consuming, so it must turn part of each year's product back into means of "
                  "production. That is reproduction, and if production is capitalist, so is "
                  "reproduction. If £100 is advanced and brings in £20 of surplus value, it "
                  "must do the same next year and the year after, and the surplus value takes "
                  "the form of a revenue flowing from capital. When that revenue is all "
                  "spent on the capitalist's consumption, the scale stays the same: simple "
                  "reproduction."),
            ("p", "The first thing repetition changes is the look of wages. The worker is not "
                  "paid until he has worked, so before his wage reaches him he has already "
                  "produced the fund it comes from. &ldquo;It is his labour of last week, or "
                  "of last year, that pays for his labour-power this week or this "
                  "year.&rdquo; Look at the classes instead of one employer and one worker, "
                  "and the money is only an order-note: the capitalists hand the workers "
                  "notes on part of what the workers produced, and the workers hand them "
                  "back for goods."),
            ("p", "Marx makes the point with a serf. A peasant works 3 days a week on his own "
                  "land with his own tools and 3 days on the lord's. He produces his own "
                  "means of subsistence, and nobody advances it to him. Now suppose the lord "
                  "takes the land, the cattle and the seed one fine morning. The peasant "
                  "still works 6 days, 3 for himself and 3 for the lord, but from that "
                  "morning the 3 days he works for himself come back to him as wages, a "
                  "capital apparently advanced by the lord."),
            ("p", "The second change concerns the whole capital, and it is the passage the "
                  "lesson opened with. Marx's arithmetic is a single division. A capital of "
                  "£1,000 brings in £200 of surplus value a year, all of it consumed. After "
                  "5 years the capitalist has consumed `5 · £200 = £1,000`, the sum he "
                  "advanced. If he consumed only half, £100 a year, the same point comes "
                  "after 10 years. The general rule: the capital advanced divided by the "
                  "surplus value consumed each year gives the number of years after which "
                  "the original capital has been consumed. The marx preset prints 5 years, "
                  "the slower preset, Marx's half, 10, and the faster preset, at £250 a "
                  "year, 4."),
            ("p", "He makes it vivid with a debtor. A man who runs through his whole property "
                  "by borrowing against it still has the property in his hands, but its "
                  "value now represents only his debts. In the same way, the capitalist who "
                  "has consumed the equivalent of his original capital still holds a capital "
                  "of the same size, buildings and machines included, but its value "
                  "represents only the surplus value he took without payment. &ldquo;Not a "
                  "single atom of the value of his old capital continues to exist.&rdquo;"),
            ("p", "This is a way of reckoning, and the obvious objection deserves its full "
                  "weight. Money has no label on it. An accountant would say just as "
                  "truthfully that the capitalist spent his profits each year and kept his "
                  "capital intact, and nothing in the ledger can choose between the two "
                  "descriptions. Marx's reply is that he is not tracing coins but asking "
                  "what the present value of the capital is equivalent to, and that the "
                  "repeated process makes the question unavoidable whatever the capital's "
                  "first origin. Even a capital first earned by its owner's own labour, he "
                  "says, becomes unpaid labour of others after enough repetitions. Readers "
                  "who find the accountant's description equally good are not making an "
                  "arithmetic mistake."),
            ("p", "The third change is in the worker. He consumes twice: productively, using "
                  "up means of production at work, and individually, turning his wages into "
                  "food and shelter. Seen as a class, even his individual consumption is "
                  "the reproduction of labour-power for capital, like oiling a machine, "
                  "which is why economists counted as productive only the part of it the "
                  "class needs to survive. &ldquo;The Roman slave was held by fetters: the "
                  "wage-labourer is bound to his owner by invisible threads.&rdquo;"),
            ("p", "Marx's example is the cotton famine of the 1860s. When the American Civil "
                  "War cut off the cotton and Lancashire's spinners were thrown out of work, "
                  "there were calls for public money to help them emigrate. Edmund Potter, a "
                  "former president of the Manchester Chamber of Commerce, wrote to the "
                  "<em>Times</em> in March 1863 against it: the workers were the trade's "
                  "trained power, and could not be replaced for a generation. Marx reads the "
                  "letter as a manufacturer counting his workers among his machinery. The "
                  "emigration was not paid for, and the workers stayed in what the "
                  "<em>Times</em> had called a &ldquo;moral workhouse&rdquo;."),
            ("p", "So the repetition reproduces more than products and surplus value. It "
                  "keeps the worker without means of production and returns him to the "
                  "market to sell his labour-power again. Capitalist production, Marx "
                  "concludes, &ldquo;produces and reproduces the capitalist relation; on the "
                  "one side the capitalist, on the other the wage-labourer.&rdquo;"),
            ("p", "Simple reproduction consumes every penny of surplus value. The next "
                  "lesson, “Surplus Value into Capital”, asks what happens when the "
                  "capitalist does not."),
        ],
        "lab": ("capkit", {
            "mode": "accumulate",
            "view": "simple",
            "money_unit": "£",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's figures: £1,000 capital, £200 of surplus value consumed a year",
                 "capital": 1000, "consumed_per_year": 200, "expect": {"acYears": "5 years"}},
                {"id": "faster", "label": "£250 consumed a year",
                 "capital": 1000, "consumed_per_year": 250, "expect": {"acYears": "4 years"}},
                {"id": "slower", "label": "Marx's figures: only half consumed, £100 a year",
                 "capital": 1000, "consumed_per_year": 100, "expect": {"acYears": "10 years"}},
            ],
            "panel_title": "When the capitalist has eaten his capital",
            "panel_intro": (
                "The lab divides the capital advanced by the surplus value consumed each "
                "year. Try a capital of your own: the answer is always the number of years "
                "after which a sum equal to the capital has been consumed."
            ),
        }),
        "steps_title": "Marx's reckoning in four steps",
        "steps_intro": "The general rule of the chapter, applied to any capital.",
        "steps": [
            ("State the capital advanced",
             "The value first laid out in means of production and labour-power: £1,000 in "
             "Marx's example."),
            ("State the surplus value consumed each year",
             "Under simple reproduction all of it is consumed; if only part is, use that "
             "part."),
            ("Divide",
             "Capital advanced over surplus value consumed a year gives the years, or "
             "reproduction periods: £1,000 over £200 is 5."),
            ("Read the result",
             "After that many years the capitalist has consumed a value equal to his "
             "original capital, and on Marx's reckoning the capital he holds is "
             "capitalised surplus value."),
        ],
        "worked": {
            "title": "A thousand pounds in five years",
            "intro": [
                "A capital of £1,000 produces £200 of surplus value a year and the capitalist "
                "spends it all. You want the year in which he has consumed a sum equal to his "
                "capital, and the year if he spent only half.",
            ],
            "lines": [
                "years:  £1,000 / £200 = 5",
                "consumed in 5 years:  5 · £200 = £1,000",
                "half consumed:  £1,000 / £100 = 10 years",
            ],
            "after": [
                "At the end of the fifth year he still holds a capital of £1,000. On Marx's "
                "reckoning it is now the equivalent of the £1,000 of surplus value he "
                "appropriated, and the original £1,000 has been consumed.",
            ],
        },
        "quiz_title": "Repetition and its results",
        "quiz": [
            {"q": "A capital of £1,500 yields £300 of surplus value a year, all of it "
                  "consumed. After how many years has the capitalist consumed a sum equal to "
                  "his capital?",
             "a": ["3", "5", "10", "6"],
             "c": 1,
             "why": "Capital over surplus value consumed is `1500/300 = 5`. Ten is the answer "
                    "if only half the surplus value, £150, were consumed a year; 6 divides "
                    "£1,800, the capital with one year's surplus added, by £300; 3 comes from "
                    "no division of these two figures."},
            {"q": "In Marx's example of the peasant whose land is taken, who produces the "
                  "fund from which the peasant is paid after the change?",
             "a": ["The lord, out of his own wealth",
                   "The peasant himself, in the days he works for himself",
                   "The other peasants of the village",
                   "Nobody: the wage is advanced from capital saved earlier"],
             "c": 1,
             "why": "The peasant goes on working 3 days for himself and 3 for the lord. The "
                    "3 days for himself now come back to him as wages, a capital apparently "
                    "advanced by the lord, but he produced it, as he did before the change."},
            {"q": "After the 5 years of Marx's example, what does he say the value of the "
                  "capitalist's present capital represents?",
             "a": ["His original £1,000, kept intact",
                   "The sum of the surplus value he appropriated",
                   "Nothing, since the capital has been consumed",
                   "His own labour and that of his forefathers"],
             "c": 1,
             "why": "Marx says the capital he holds equals the surplus value appropriated in "
                    "those years, while what he consumed equals the original capital. Kept "
                    "intact is the capitalist's own view. The capital has not vanished; it "
                    "is still £1,000. The forefathers are the economists' answer, which Marx "
                    "takes up in the next chapter."},
            {"q": "What does Marx call the worker's individual consumption, seen from the "
                  "standpoint of the classes?",
             "a": ["Unproductive and of no interest to capital",
                   "The reproduction of labour-power for capital",
                   "A deduction from surplus value",
                   "Saving out of revenue"],
             "c": 1,
             "why": "Within the limits of what is necessary, the worker's consumption "
                    "reproduces his labour-power and new workers, a factor of the "
                    "reproduction of capital like the cleaning of machinery. It is paid from "
                    "variable capital, not from surplus value, and it is consumption, not "
                    "saving."},
        ],
        "mistakes": [
            ("Thinking the capital stays the capitalist's original property however long it runs",
             "The tile counts the years until consumption equals the capital: 5 at Marx's "
             "figures. From then on, on Marx's reckoning, the value the capitalist holds "
             "equals the surplus value he took, and his original capital is the value he "
             "has consumed. The thing in his hands is the same; what it is the equivalent of "
             "has changed. The reckoning is disputable, as the note says, but the figure is "
             "not."),
            ("Thinking wages are advanced from the capitalist's own funds",
             "In one isolated transaction they seem to be. Repeated, the worker is paid "
             "after he works, out of the product of the previous period, and his own labour "
             "produced the fund. Marx's peasant shows the change is one of form: the same 3 "
             "days now return to him as wages."),
            ("Treating the worker's private life as outside production",
             "Marx's point is that the worker's eating and sleeping reproduce the "
             "labour-power capital needs, and that the process returns him to the market "
             "with nothing to sell but that labour-power. It keeps reproducing him as a "
             "wage-labourer."),
        ],
        "standard": (
            "Finish when you can compute the years in which a capital is consumed.",
            "Given a capital and the surplus value consumed each year, compute the years "
            "after which a sum equal to the capital has been consumed, and state what Marx "
            "says the remaining capital then represents."
        ),
        "note": (
            "The figures are Marx's. The years are a way of reckoning, not a fact the ledger "
            "records: one could as well say that the capitalist consumed only the surplus "
            "each year and kept his capital whole. The lab computes the division, which "
            "both descriptions accept; which of them names the capital correctly is the "
            "point Marx and his critics dispute."
        ),
    },
]
