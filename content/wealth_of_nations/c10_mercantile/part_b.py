"""The Mercantile System, lessons 4-6 -- Book IV, Chapters 4 to 6.

Every quotation is copied from /mnt/project-files/wealth-texts/wealth-of-nations-psu.txt
(the Electronic Classics Series edition, Pennsylvania State University, 2005); the
comment beside each lesson gives its line numbers. A quotation that would cross a
page break in the extraction stops before the break, and nothing else is changed.
Smith's own figures are marked as his in each lab preset; the rest were written
for the lesson.
"""

LESSONS = [
    # ---------------------------------------------------------------- 04
    # PSU text l. 15946-16118 (Book IV, Chapter 4). Opening l. 15948-15966; the old subsidy
    # l. 15967-15979; tobacco l. 15980-15986; sugar l. 15987-15993; French goods l. 15994-16009;
    # the colonies l. 16033-16070; the carrying trade l. 16071-16091; the colonial
    # drawback l. 16092-16109; fraud l. 16110-16115. The bounty that is a drawback l. 16731-16740.
    {
        "slug": "drawbacks",
        "title": "Drawbacks",
        "module": "Book IV, Chapter 4 · Of Drawbacks",
        "one_line": "A drawback repays a duty on goods exported again, and Smith counts it the most reasonable of the encouragements to exportation because it adds nothing the duty did not take away.",
        "summary": (
            "Merchants cannot ask for a monopoly in foreign markets, so they ask for help "
            "in selling there. The shortest chapter in Book IV takes the first kind: a "
            "refund of the duty on goods exported again. Compute the duty paid, drawn back "
            "and kept on Smith's tobacco, and see why he approves of it and where he stops."
        ),
        "key": [
            "duty paid = quantity × duty a unit",
            "drawn back = exported × duty × share",
            "duty kept = duty paid − duty drawn back",
            "full refund leaves the home duty only",
            "a refund beyond the duty is a bounty",
        ],
        "key_label": "The fourth chapter in five lines",
        "concepts_intro": (
            "The chapter is short and its argument is a single comparison. Three ideas "
            "carry it: what a drawback is, why it passes Smith's test, and where the "
            "test fails."
        ),
        "concepts": [
            ("What a drawback is",
             "A refund, on exportation, of the whole or a part of a duty. There are two "
             "kinds: of an excise or inland duty laid on home goods, and of the duty paid on "
             "foreign goods that were imported only to be exported again. The second makes "
             "by far the largest part of the drawbacks in Great Britain, Smith says."),
            ("Why Smith counts it reasonable",
             "A drawback cannot make the country export more than it would have exported "
             "had no duty been laid. It does not turn more of the country's capital to "
             "any trade than would go there of its own accord, and only stops the duty "
             "from driving some of it elsewhere."),
            ("Where the reason fails",
             "In trade with a country where the exporting merchants already hold a monopoly, "
             "the same exports would go whether or not the duty was repaid, and the refund "
             "is a pure loss to the revenue. It also fails if the goods are not really "
             "exported but landed again at home, as tobacco frequently was."),
        ],
        "read_title": "The passage first, then the chapter in its order",
        "read_intro": (
            "Smith's case for drawbacks is made in the first two paragraphs. The rest of "
            "the chapter is the history of how the rule was bent."
        ),
        "body": [
            ("p", "<strong>Book IV, Chapter 4.</strong> Smith begins with what merchants and "
                  "manufacturers want. They are not contented with the monopoly of the home "
                  "market but &ldquo;desire likewise the most extensive foreign sale for their "
                  "goods&rdquo;. Their country has no jurisdiction abroad and can seldom give "
                  "them a monopoly there, so they petition for the encouragements the next "
                  "four chapters take in turn: drawbacks, bounties, treaties and, in Chapter 7, "
                  "colonies. Of the first he says: &ldquo;Of these encouragements, what are "
                  "called drawbacks seem to be the most reasonable.&rdquo;"),
            ("p", "A man who makes cloth pays an excise on it at home, and a man who "
                  "imports sugar pays a duty at the port. If either sells abroad, the duty "
                  "he paid is added to what he must charge, and he is at a disadvantage "
                  "against foreign sellers who paid none. A drawback gives it back. Smith's "
                  "reason for approving is exact: &ldquo;To allow the merchant to draw back "
                  "upon exportation, either the whole, or a part of whatever excise or inland "
                  "duty is imposed upon domestic industry, can never occasion the exportation "
                  "of a greater quantity of goods than what would have been exported had no "
                  "duty been imposed.&rdquo;"),
            ("def", ("Drawback",
                     "A refund, when goods are exported, of the whole or a part of a duty "
                     "paid on them or on what they were made from. The goods are exported "
                     "in the same form in which they were imported, or, for an excise, as "
                     "home goods. A refund of more than the duty paid is not a drawback "
                     "but a bounty.")),
            ("p", "Think of it as a ledger. Without the duty, so much would have been "
                  "exported. With the duty and no drawback, less would. With the drawback, "
                  "the same as without. Smith puts it as a statement about the balance of "
                  "employments: &ldquo;They tend not to overturn that balance which naturally "
                  "establishes itself among all the various employments of the society, but "
                  "to hinder it from being overturned by the duty.&rdquo; The comparison "
                  "that matters is with the world with no duty, and a drawback restores "
                  "the situation in that world. He says the same of the revenue: it "
                  "&ldquo;profits from such drawbacks, by that part of the duty which is "
                  "retained&rdquo;. If the whole duty had been kept, he says, the foreign "
                  "goods could seldom have been exported, nor consequently imported, and "
                  "the duty would never have been paid."),
            ("p", "The rest of the chapter is the history of the rule. When the old subsidy "
                  "was laid, a merchant could draw back half of it on exportation, an "
                  "Englishman if he exported within twelve months, an alien within nine, "
                  "and the term was later extended to three years. Later duties were mostly "
                  "repaid in full. Special cases grew. Smith's example is tobacco: before the "
                  "revolt of the colonies Britain had the monopoly of the tobacco of "
                  "Maryland and Virginia, and &ldquo;We imported about ninety-six thousand "
                  "hogsheads, and the home consumption was not supposed to exceed fourteen "
                  "thousand.&rdquo; To make the export of the other 82,000 possible, `96,000 − "
                  "14,000 = 82,000`, the whole duties were drawn back when the export took "
                  "place within three years. He takes his figures to mean that the "
                  "hogsheads not used at home went abroad, and that is the lab's assumption."),
            ("p", "The lab computes what is paid, returned and kept. Smith gives no duty "
                  "a hogshead, so the lab's figure is written for the lesson, at £5. "
                  "In the preset <em>tobacco-whole</em>, with the whole duty drawn back on "
                  "the 82,000 exported, the duty paid is `96,000 × 5 = 480,000`, the drawback "
                  "is `82,000 × 5 = 410,000`, and the duty kept is `480,000 − 410,000 = "
                  "70,000`, which is the duty on the 14,000 hogsheads that stayed at home. "
                  "The preset <em>tobacco-half</em> draws back half of it, as under the old "
                  "subsidy, which gives `410,000 × 1/2 = 205,000` and leaves 275,000, and "
                  "<em>tobacco-none</em> draws nothing back and keeps all 480,000. Only the "
                  "share changes between them."),
            ("p", "Smith then lists where the rule was bent. French goods were treated "
                  "worst: &ldquo;Not only half the old subsidy, but the second twenty-five "
                  "per cent. is retained upon the exportation of all French goods&rdquo;, since "
                  "&ldquo;We are unwilling even to be the carriers of French goods, and "
                  "choose rather to forego a profit to ourselves than to suffer those whom "
                  "we consider as our enemies to make any profit by our means.&rdquo; Goods "
                  "the home manufacturers feared could be imported to be warehoused for "
                  "export on payment of duty, and then got nothing back. Wine had "
                  "special allowances, and after 1763 duties on wine sent to the colonies "
                  "were drawn back down to £3 10s, except for French wine."),
            ("p", "The reason he gives for the original drawbacks is not a compliment: they "
                  "were, he says, &ldquo;perhaps, originally granted for the encouragement "
                  "of the carrying trade&rdquo;, which was thought good for bringing in gold, "
                  "since freight is often paid by foreigners in money. He then separates the "
                  "motive from the institution: &ldquo;though the motive of the institution "
                  "was, perhaps, abundantly foolish, the institution itself seems reasonable "
                  "enough.&rdquo; And he adds that &ldquo;The carrying trade, though it "
                  "deserves no preference, ought not to be precluded, but to be left free, "
                  "like all other trades.&rdquo; It is a resource for capital that cannot "
                  "find work at home. Note the style of the argument: Smith does not need the "
                  "mercantile reason to be right. He asks what the institution does."),
            ("p", "There are two limits. The first concerns the colonies. His reasons "
                  "&ldquo;will justify drawbacks only upon exporting goods to those "
                  "countries which are altogether foreign and independent, not to those in "
                  "which our merchants and manufacturers enjoy a monopoly&rdquo;, because "
                  "where the monopoly holds the same quantity might go if the whole duties "
                  "were kept, and the refund is then &ldquo;pure loss to the revenue&rdquo;. "
                  "The second is fraud. Drawbacks &ldquo;are useful only in those cases in "
                  "which the goods, for the exportation of which they are given, are really "
                  "exported to some foreign country, and not clandestinely re-imported into "
                  "our own&rdquo;, and tobacco, he says, has frequently been abused in that way, "
                  "to the harm of the revenue and the fair trader. A drawback is a payment "
                  "to the man who can show his goods went abroad, and a paper trail can be "
                  "made without the voyage."),
            ("p", "Smith's account is not without opponents. In the mercantile view the "
                  "carrying trade deserved a drawback for itself, since it brought in "
                  "freight and silver, and Smith's reply is that it should be left free and "
                  "not encouraged. Alexander Hamilton, in his Report on Manufactures of "
                  "1791, counted among the means by which a government could encourage a new "
                  "manufacture both drawbacks of the duties on its materials and bounties, "
                  "which Smith condemns, and he argued that bounties had some advantages "
                  "over protecting duties. Smith had died the year before and could not "
                  "have answered. Modern trade agreements keep Smith's line: they "
                  "allow the refund of import duties on goods exported again and treat a "
                  "refund of more than the duty as an export subsidy. The next lesson takes "
                  "up what Smith calls a bounty, and how it differs from a drawback: &ldquo;What "
                  "is called a bounty, is sometimes no more than a drawback&rdquo;, as when "
                  "the bounty on exported refined sugar repays the duties on the brown sugar "
                  "it is made from."),
        ],
        "lab": ("wonkit", {
            "mode": "trade",
            "view": "drawback",
            "qty_unit": "hogsheads",
            "money_unit": "£",
            "preset": "tobacco-whole",
            "presets": [
                {"id": "tobacco-whole",
                 "label": "Smith's tobacco, the whole duty drawn back (the duty is written for this lesson)",
                 "quantity": 96000, "duty": 5, "exported": 82000, "share": 100,
                 "expect": {
                    "wtrPaid": "£480,000",
                    "wtrDrawn": "£410,000",
                    "wtrNet": "£70,000",
                    "wtrKept": "£5 a hogshead on 14,000 hogsheads",
                 }},
                {"id": "tobacco-half",
                 "label": "The same tobacco, half the duty drawn back",
                 "quantity": 96000, "duty": 5, "exported": 82000, "share": 50,
                 "expect": {
                    "wtrPaid": "£480,000",
                    "wtrDrawn": "£205,000",
                    "wtrNet": "£275,000",
                    "wtrKept": "£275/14 ≈ £19.64 a hogshead on 14,000 hogsheads",
                 }},
                {"id": "tobacco-none",
                 "label": "The same tobacco, nothing drawn back",
                 "quantity": 96000, "duty": 5, "exported": 82000, "share": 0,
                 "expect": {
                    "wtrPaid": "£480,000",
                    "wtrDrawn": "£0",
                    "wtrNet": "£480,000",
                    "wtrKept": "£240/7 ≈ £34.29 a hogshead on 14,000 hogsheads",
                 }},
            ],
            "panel_title": "The duty paid, drawn back and kept",
            "panel_intro": (
                "The quantity imported, the duty a unit, the quantity exported again and "
                "the share of the duty drawn back go in. The lab prints the duty paid, the "
                "duty drawn back and the duty kept. Only the share changes between the "
                "presets, so the whole difference is the drawback."
            ),
        }),
        "steps_title": "Working out a drawback",
        "steps_intro": "Four steps, the same for any duty and any share.",
        "steps": [
            ("Duty paid",
             "Multiply the quantity imported by the duty a unit. The duty is paid on all of "
             "it when it lands, whether or not it is later exported."),
            ("Duty drawn back",
             "Multiply the quantity exported again by the duty a unit and by the share "
             "drawn back. Goods that stay at home get nothing back."),
            ("Duty kept",
             "Subtract the second from the first. With the whole duty drawn back it "
             "equals the duty on the goods consumed at home."),
            ("Ask whether the goods really left",
             "A drawback is justified only on goods really exported to a foreign and "
             "independent country. If they were landed again, or were bound for a "
             "market where the exporter already had a monopoly, the refund is a loss "
             "with no export gained."),
        ],
        "worked": {
            "title": "Smith's tobacco, with a duty written for the lesson",
            "intro": [
                "Britain imports 96,000 hogsheads, 14,000 stay at home and 82,000 are "
                "exported. The duty is £5 a hogshead, and the whole of it is drawn back on "
                "what is exported.",
            ],
            "lines": [
                "duty paid:  96,000 · 5 = 480,000",
                "drawn back:  82,000 · 5 · 100% = 410,000",
                "kept:  480,000 − 410,000 = 70,000",
                "consumed at home:  96,000 − 82,000 = 14,000",
                "kept a hogshead at home:  70,000 / 14,000 = 5",
            ],
            "after": [
                "With the whole duty drawn back, the revenue keeps exactly the duty on "
                "what is consumed at home and nothing on what is exported. With half drawn "
                "back it keeps 275,000, and with none, 480,000, which at £5 a hogshead "
                "puts the full duty on tobacco that was never consumed here and would "
                "probably not have been imported."
            ],
        },
        "quiz_title": "Duty paid, drawn back and kept",
        "quiz": [
            {"q": "In the preset tobacco-whole, how much duty does the revenue keep?",
             "a": ["£410,000", "£480,000", "£14,000", "£70,000"],
             "c": 3,
             "why": "`96,000 × 5 = 480,000` is paid and `82,000 × 5 = 410,000` is drawn back, "
                    "so `480,000 − 410,000 = 70,000` is kept, the duty on the 14,000 "
                    "hogsheads that stayed. £410,000 is the refund, £480,000 the gross duty, "
                    "and 14,000 is a count of hogsheads."},
            {"q": "In the preset tobacco-half, how much is drawn back?",
             "a": ["£410,000", "£205,000", "£240,000", "£102,500"],
             "c": 1,
             "why": "Half of the duty on the exported hogsheads: `82,000 × 5 × 1/2 = 205,000`. "
                    "£240,000 would be half of all the duty paid, which includes the "
                    "hogsheads that stayed home and got no refund."},
            {"q": "Why does Smith count a drawback among the reasonable encouragements?",
             "a": ["It turns more of the country's capital to the export trade than would "
                   "otherwise go there",
                   "It cannot make the country export more than it would have exported "
                   "had no duty been laid, and only stops the duty driving capital away",
                   "It brings gold into the country by way of the freight",
                   "It raises the revenue of the customs by the whole of the duty"],
             "c": 1,
             "why": "His reason is that a drawback leaves things as they would be without "
                    "the duty. The first option is the objection he raises against bounties. "
                    "The gold is the mercantile reason he calls &ldquo;abundantly "
                    "foolish&rdquo;, and the revenue keeps only the part retained."},
            {"q": "On which drawbacks does Smith say the loss to the revenue may be pure "
                  "loss, without making the trade larger?",
             "a": ["On goods sent to the American colonies, where British merchants held "
                   "a monopoly",
                   "On goods exported to Holland, the great carrier of Europe",
                   "On any drawback of the whole duty",
                   "On French goods, which kept half the old subsidy"],
             "c": 0,
             "why": "&ldquo;A drawback, for example, upon the exportation of European goods to "
                    "our American colonies, will not always occasion a greater exportation "
                    "than what would have taken place without it.&rdquo; Where the "
                    "monopoly already holds, the same goods would go if the whole duty "
                    "were kept. The other three are not the cases he names."},
        ],
        "mistakes": [
            ("Calling a drawback a bounty",
             "A drawback repays a duty and no more, and a bounty pays something beyond "
             "it. Smith says the names overlap in the language of the customs: what is "
             "called a bounty is sometimes no more than a drawback, as on exported refined "
             "sugar. The test is what the payment does to the quantity exported, "
             "not what it is called."),
            ("Thinking a drawback costs the revenue the whole refund",
             "Without the drawback the goods would often not be imported at all, and the "
             "duty on them would not be paid. In the lab the revenue keeps 70,000 with a "
             "full drawback and would have kept nothing if the goods had not come, so "
             "the refund is paid out of a duty that was only collected because of it."),
            ("Thinking Smith defends every drawback in the book",
             "He excludes drawbacks on exports to the colonies, on goods landed again in "
             "fraud, and, by implication, any refund beyond the duty. His case is "
             "for one rule, and the chapter is a list of the exceptions that had grown up."),
        ],
        "standard": (
            "Finish when you can compute the duty kept and say when a drawback is reasonable.",
            "Given a quantity, a duty, the quantity exported and the share drawn back, "
            "compute the duty paid, drawn back and kept, and say in one sentence why a "
            "drawback passes Smith's test and a refund to a monopoly market does not."
        ),
        "note": (
            "The lab computes a refund from the figures it is given. It cannot say whether "
            "the goods really left the country, which Smith says was the chief abuse, or "
            "whether a drawback preserves the natural balance of employments or only the "
            "interests of exporting merchants. The 96,000 and 14,000 hogsheads are Smith's, "
            "the 82,000 exported is the lesson's reading of them, and the £5 duty is "
            "written for the lesson, since Smith gives none."
        ),
    },
    # ---------------------------------------------------------------- 05
    # PSU text l. 16119-17454 (Book IV, Chapter 5, with the Digression concerning the
    # Corn Trade and Corn Laws l. 16757-17454). Opening l. 16121-16165; the Tracts l. 16166-16185;
    # the two taxes l. 16229-16262; nominal and real price l. 16263-16336; Spain and
    # Portugal l. 16337-16421; the corn merchants l. 16448-16459; real value of corn
    # l. 16481-16503; production bounty l. 16520-16551; herring l. 16566-16730; the four trades
    # l. 16763-16767; the inland dealer l. 16768-16922; witchcraft l. 17151-17157; the
    # proportions l. 17169-17186; the exporter l. 17289-17297; the laws of Solon l. 17449-17454.
    {
        "slug": "bounties-and-the-corn-trade",
        "title": "Bounties and the Corn Trade",
        "module": "Book IV, Chapter 5 · Of Bounties, with the Digression concerning the Corn Trade and Corn Laws",
        "one_line": "A bounty on exported corn is a tax that the public pays twice, once to the treasury and once in the price at home, and Smith adds that it does not raise corn's real value.",
        "summary": (
            "Chapter 5 takes the encouragement that pays foreigners to buy, and spends "
            "most of its length on the bounty on corn. Compute what a bounty of five "
            "shillings the quarter costs the treasury and home buyers on Smith's own "
            "supposition, then read the Digression on the Corn Trade for its four "
            "trades, its two ratios and its claim about famine."
        ),
        "key": [
            "treasury pays bounty × quantity exported",
            "home buyers pay rise × quantity bought here",
            "two taxes together, per unit exported",
            "the money price rises, the real price does not",
            "four trades in corn, one interest opposed",
        ],
        "key_label": "The fifth chapter in five lines",
        "concepts_intro": (
            "The chapter first states the bounty in general and then turns to corn, "
            "where a digression takes up more than half of it. Three ideas do the work."
        ),
        "concepts": [
            ("A bounty pays foreigners to buy",
             "A country cannot force foreigners to buy its goods as it forces its own "
             "people, so &ldquo;The next best expedient, it has been thought, therefore, is "
             "to pay them for buying.&rdquo; Smith says bounties ought to be given only to "
             "trades that cannot be carried on without them, and such a trade must "
             "sell for less than it cost, so it is a losing trade."),
            ("The two taxes",
             "An export bounty imposes two taxes on the people. The first is what they "
             "contribute to pay the bounty. The second is the rise in the price of the "
             "same goods at home, caused by sending more abroad. For corn the second is "
             "the heavier by far, since everyone buys corn."),
            ("Nominal price and real price",
             "A bounty raises the money price of corn at home but not its real value, "
             "which is the labour it will maintain. Since the money price of corn sets the "
             "money price of labour and of home goods, the effect is to lower the real "
             "value of silver in that country, and not to enrich the grower."),
        ],
        "read_title": "The passage first, then the bounty, the corn trade and the laws",
        "read_intro": (
            "Smith states the bounty in general terms, takes the corn bounty as his "
            "example, and then, in the Digression, examines the corn trade itself."
        ),
        "body": [
            ("p", "<strong>Book IV, Chapter 5.</strong> Smith begins with what a bounty "
                  "is for. &ldquo;We cannot give our workmen a monopoly in the foreign, as we "
                  "have done in the home market. We cannot force foreigners to buy their "
                  "goods, as we have done our own countrymen. The next best expedient, it "
                  "has been thought, therefore, is to pay them for buying.&rdquo; It is "
                  "the system's way, he says, of putting money into all our pockets by the "
                  "balance of trade."),
            ("p", "His first argument is about what a bounty must be. &ldquo;Those trades "
                  "only require bounties, in which the merchant is obliged to sell his goods "
                  "for a price which does not replace to him his capital, together with the "
                  "ordinary profit, or in which he is obliged to sell them for less than it "
                  "really cost him to send them to market.&rdquo; A trade that paid would not "
                  "need one. So a bounty always props up a trade that loses, and the effect "
                  "of bounties, &ldquo;like that of all the other expedients of the mercantile "
                  "system, can only be to force the trade of a country into a channel much "
                  "less advantageous than that in which it would naturally run of its own "
                  "accord&rdquo;."),
            ("p", "The best defence of the corn bounty in his own day was in the <em>Tracts "
                  "upon the Corn Trade</em>, whose author showed that since the bounty "
                  "began, the value of the corn exported had exceeded that of the corn "
                  "imported by far more than the bounties paid. That, on the system's "
                  "principles, proved the trade beneficial. Smith's reply is that the "
                  "author &ldquo;does not consider that this extraordinary expense, or the "
                  "bounty, is the smallest part of the expense which the exportation of "
                  "corn really costs the society&rdquo;. The farmer's capital must be "
                  "replaced as well, with the ordinary profit, and the very reason a bounty "
                  "was thought needed is that the price abroad did not do it."),
            ("p", "Then the two taxes. &ldquo;The corn bounty, it is to be observed, as well "
                  "as every other bounty upon exportation, imposes two different taxes upon "
                  "the people; first, the tax which they are obliged to contribute, in order "
                  "to pay the bounty; and, secondly, the tax which arises from the advanced "
                  "price of the commodity in the home market.&rdquo; Smith gives a "
                  "supposition, with figures: &ldquo;Let us suppose that, taking one year with "
                  "another, the bounty of 5s. upon the exportation of the quarter of wheat "
                  "raises the price of that commodity in the home market only 6d. the "
                  "bushel, or 4s. the quarter higher than it otherwise would have been in "
                  "the actual state of the crop.&rdquo; A quarter is eight bushels, so 6d. "
                  "a bushel is `8 × 6 = 48` pence, which is 4s. He takes from the Tracts that "
                  "the corn exported was not more than one part in thirty-one of the corn "
                  "consumed at home. So for each quarter exported there were 31 consumed "
                  "here, and `31 × 4 = 124` shillings of second tax for each 5 shillings of "
                  "the first. In his words: &ldquo;For every 5s. therefore, which they "
                  "contribute to the payment of the first tax, they must contribute £6:4s. "
                  "to the payment of the second.&rdquo; 124 shillings is £6 4s."),
            ("p", "The lab computes the two taxes. To keep the arithmetic in whole "
                  "numbers it scales Smith's ratio: 1,000 quarters exported and 31,000 "
                  "consumed at home, which is the one to thirty-one, with a bounty of 5s. and "
                  "a rise of 4s. In the preset <em>smith-corn-bounty</em>, in shillings, the "
                  "treasury pays `5 × 1,000 = 5,000`, home buyers pay `4 × 31,000 = "
                  "124,000`, and the two together are `5,000 + 124,000 = 129,000`, or 129 "
                  "shillings for each quarter exported. The preset <em>a-smaller-rise</em> "
                  "lets the rise be 1s. and gives `1 × 31,000 = 31,000` and a total of "
                  "36,000. The preset <em>no-rise</em> lets nothing rise and leaves only the "
                  "first tax of 5,000. The rise is Smith's supposition, and not a "
                  "measurement he made, and the first preset says so."),
            ("p", "Smith's next point is that this rise is nominal. Defenders of the bounty "
                  "said that a better money price for corn would encourage its growing. "
                  "He answers that it would, if it raised the real price, but nothing can: "
                  "&ldquo;The real effect of the bounty is not so much to raise the real "
                  "value of corn, as to degrade the real value of silver.&rdquo; The reason "
                  "is that the money price of corn regulates the money price of labour, "
                  "which must be enough to buy the labourer's corn, and through labour "
                  "and the rude produce it regulates the price of nearly every home-made "
                  "good, so the farmer who gets 4s. for his bushel instead of 3s. 6d. finds "
                  "that 4s. buys no more of what he needs. &ldquo;The nature of things has "
                  "stamped upon corn a real value, which cannot be altered by merely altering "
                  "its money price.&rdquo; And &ldquo;Woollen or linen cloth are not the "
                  "regulating commodities by which the real value of all other commodities "
                  "must be finally measured and determined; corn is.&rdquo; A bounty on "
                  "cloth does raise the real price of cloth, he says, which is the difference."),
            ("p", "Smith then offers a picture, drawn from Spain and Portugal, who taxed or "
                  "forbade the export of gold and silver. &ldquo;When you dam up a stream of "
                  "water, as soon as the dam is full, as much water must run over the "
                  "dam-head as if there was no dam at all.&rdquo; The metal is deeper "
                  "behind the dam and so cheaper there, and everything priced in it dearer, "
                  "and foreigners can undersell the Spaniards at home. The corn bounty, he "
                  "says, operates exactly in the same way, lowering the value of silver "
                  "at home and raising it a little abroad, to the advantage of the Dutch."),
            ("p", "Who gains? &ldquo;There is, perhaps, but one set of men in the whole "
                  "commonwealth to whom the bounty either was or could be essentially "
                  "serviceable. These were the corn merchants, the exporters and importers "
                  "of corn.&rdquo; It was in them, he says, that he had observed the greatest "
                  "zeal for keeping the bounty. He adds "
                  "that a bounty on production would operate more directly than one on "
                  "exportation, and would impose only one tax, and says it has rarely "
                  "been given because the system teaches that wealth comes from export. "
                  "His comment on one bounty paid on tonnage is a good sample of his "
                  "temper: the herring-buss bounty, paid by the ton of the ship and not by "
                  "its catch, had led vessels, he was afraid, to fit out &ldquo;for the sole purpose of catching, not "
                  "the fish but the bounty&rdquo;. In 1759, he says, at fifty shillings a ton "
                  "the whole Scottish buss fishery brought in four barrels. The accounts "
                  "are given at the end of Book IV and are not worked here."),
            ("p", "Objections to him come from two sides. David Ricardo argued in 1815 "
                  "that restrictions on importing corn raise rents and lower profits, so "
                  "that the price of corn does change who gets what, and Smith's claim that "
                  "corn's real value cannot be altered needs that distinction. Malthus "
                  "defended the restriction in the same year, on the ground that a country "
                  "which depends on foreign corn is exposed in a war and that agriculture "
                  "and manufactures should be kept in balance. And Alexander Hamilton, in "
                  "1791, argued that pecuniary bounties are among the most effective means "
                  "of encouraging a new manufacture, the case Smith's rule against bounties "
                  "has to meet. Smith had died the year before, and the argument was "
                  "carried on without him."),
            ("p", "The Digression concerning the Corn Trade takes the rest of the chapter. "
                  "Smith says that praise of the bounty law and of the system of laws joined "
                  "to it is &ldquo;altogether unmerited&rdquo;, and that the corn trade is "
                  "four trades, which may be carried on by one man but are in nature "
                  "separate: the inland dealer, the importer for home consumption, the "
                  "exporter, and the carrier who imports in order to export again. The first, "
                  "he says, has an interest that is, even in the years of greatest scarcity, "
                  "&ldquo;exactly the same&rdquo; as that of the people. By raising his price "
                  "as high as the scarcity requires, he makes them thrifty, and if he raises "
                  "it too high he is left with corn at the end of the season, and if too low "
                  "he starves them before the next crop. &ldquo;Without intending the "
                  "interest of the people, he is necessarily led, by a regard to his own "
                  "interest, to treat them, even in years of scarcity, pretty much in the "
                  "same manner as the prudent master of a vessel is sometimes obliged to treat "
                  "his crew.&rdquo; It is the idea of Chapter 2, "
                  "the second lesson of this course, put without the words "
                  "&ldquo;invisible hand&rdquo;."),
            ("p", "Smith's argument against fearing a combination of dealers is about "
                  "numbers. Corn is the commodity of greatest annual consumption, divided "
                  "among more owners than any other, scattered everywhere, so the dealers "
                  "are more numerous than in any other trade, and a dealer who found himself "
                  "with too much would lower his price and not hold it up for his rivals' "
                  "benefit. He grants one case: if one great company could hold a whole crop "
                  "it might destroy part of it to keep up the price, as the Dutch are said "
                  "to do with the spices of the Moluccas, but he thinks that scarcely "
                  "possible with corn. His summary of history is strong: &ldquo;a dearth never "
                  "has arisen from any combination among the inland dealers in corn, nor from "
                  "any other cause but a real scarcity&rdquo;, and a famine from nothing "
                  "but government&rsquo;s attempts to remedy a dearth by improper means. "
                  "Of the fear of engrossing and forestalling, he says it &ldquo;may be "
                  "compared to the popular terrors and suspicions of witchcraft&rdquo;."),
            ("p", "Two later arguments press on this. E. P. Thompson argued in 1971 that "
                  "the crowds who seized grain and fixed prices were acting on a coherent "
                  "moral economy, with older rules of fair dealing which they expected "
                  "magistrates to enforce, and that the political economy of Smith's day "
                  "was a replacement of it, not a plain correction. Amartya Sen argued "
                  "in 1981 that famines can occur when the food supply is not unusually "
                  "short, because some groups lose the means to buy food, so that "
                  "the supply in the market does not settle the matter. Smith's own "
                  "example is the drought in Bengal &ldquo;a few years ago&rdquo;, turned into "
                  "a famine, he thinks, by restraints on the rice trade, and Sen's chief "
                  "case is a different Bengal, in 1943. Smith does not "
                  "claim that markets cure scarcity, only that the dealers are not "
                  "its cause and that restraints make it worse."),
            ("p", "On the other three trades Smith is shorter. The importer for home "
                  "consumption benefits the people at once and lowers the money price but "
                  "not the real value of corn. The exporter does not supply the home "
                  "market directly, though a free export lets the farmer grow a surplus. "
                  "But &ldquo;The interest of the inland dealer, however, it has already been "
                  "shown, can never be opposite to that of the great body of the people. "
                  "That of the merchant-exporter may, and in fact sometimes is.&rdquo; The "
                  "carrier, who imports in order to export, helps the home market too, "
                  "since he will sell part at home to save the cost of reshipping. He gives "
                  "two ratios from the Tracts: grain imported is one part in 570 of the "
                  "grain consumed, and grain exported one part in thirty-one of the annual "
                  "produce, from which he puts the importance of the inland trade at 570 to "
                  "one against the import trade and thirty to one against the export trade. "
                  "Then he disarms them: &ldquo;I have no great faith in political "
                  "arithmetic, and I mean not to warrant the exactness of either of these "
                  "computations.&rdquo;"),
            ("p", "Smith closes with candour. &ldquo;The laws concerning corn may "
                  "everywhere be compared to the laws concerning religion.&rdquo; People "
                  "care so much about their subsistence that government must yield to "
                  "their prejudices. He credits the statute of the thirteenth year of George "
                  "III with improving the old system in some respects and worsening it in others, "
                  "and says of it what was said of the laws of Solon: &ldquo;though not the "
                  "best in itself, it is the best which the interest, prejudices, and temper "
                  "of the times, would admit of&rdquo;. The history of the corn statutes "
                  "and the table of duties are in the book. The next lesson takes the "
                  "third encouragement, treaties of commerce, and the treaty with "
                  "Portugal that was thought a masterpiece."),
        ],
        "lab": ("wonkit", {
            "mode": "trade",
            "view": "bounty",
            "qty_unit": "quarters",
            "money_unit": "s",
            "preset": "smith-corn-bounty",
            "presets": [
                {"id": "smith-corn-bounty",
                 "label": "Smith's supposition: 5s. bounty, 4s. rise, one in thirty-one exported (scaled)",
                 "exported": 1000, "bounty": 5, "home": 31000, "rise": 4,
                 "expect": {
                    "wtrTreasury": "5,000 s",
                    "wtrConsumers": "124,000 s",
                    "wtrTotal": "129,000 s",
                    "wtrPerUnit": "129 s a quarter exported",
                    "wtrRatio": "24.8 paid by home buyers for each 1 paid to the bounty",
                 }},
                {"id": "a-smaller-rise",
                 "label": "The same bounty with a rise of 1s., written for this lesson",
                 "exported": 1000, "bounty": 5, "home": 31000, "rise": 1,
                 "expect": {
                    "wtrTreasury": "5,000 s",
                    "wtrConsumers": "31,000 s",
                    "wtrTotal": "36,000 s",
                    "wtrPerUnit": "36 s a quarter exported",
                    "wtrRatio": "6.2 paid by home buyers for each 1 paid to the bounty",
                 }},
                {"id": "no-rise",
                 "label": "The same bounty with no rise, written for this lesson",
                 "exported": 1000, "bounty": 5, "home": 31000, "rise": 0,
                 "expect": {
                    "wtrTreasury": "5,000 s",
                    "wtrConsumers": "0 s",
                    "wtrTotal": "5,000 s",
                    "wtrPerUnit": "5 s a quarter exported",
                    "wtrRatio": "0 paid by home buyers for each 1 paid to the bounty",
                 }},
            ],
            "panel_title": "The two taxes of a bounty",
            "panel_intro": (
                "The quantity exported, the bounty on each, the quantity sold at home and "
                "the rise in the home price go in, all in shillings a quarter. The lab "
                "prints the cost to the treasury, the cost to home buyers and the total, "
                "and the total for each unit exported. The rise is an input you "
                "choose and not something the lab estimates."
            ),
        }),
        "steps_title": "Counting the two taxes",
        "steps_intro": "Four steps, the same for any bounty on any exported good.",
        "steps": [
            ("The first tax",
             "Multiply the bounty on each unit by the units exported. This is what the "
             "treasury pays, and what the public contributes to it."),
            ("The second tax",
             "Multiply the rise in the home price of a unit by the units sold at "
             "home. Every home buyer pays it, since the price is one price."),
            ("Add and divide",
             "Add the two taxes, and divide by the units exported to see what each "
             "exported unit cost the public altogether."),
            ("Ask whether the rise is real",
             "A rise in the money price of corn is a rise in the real price only if it "
             "buys more labour. Smith says it does not for corn, and the lab takes the "
             "rise as given and cannot say."),
        ],
        "worked": {
            "title": "Smith's corn bounty",
            "intro": [
                "Take Smith's supposition: a bounty of 5s. a quarter raises the home price "
                "by 4s., and one quarter is exported for 31 eaten at home. Scaled to "
                "1,000 quarters exported and 31,000 eaten at home, in shillings.",
            ],
            "lines": [
                "first tax:  5 · 1,000 = 5,000",
                "second tax:  4 · 31,000 = 124,000",
                "together:  5,000 + 124,000 = 129,000",
                "a quarter exported:  129,000 / 1,000 = 129",
                "for each 5:  124,000 / 1,000 = 124 = £6 4s",
            ],
            "after": [
                "The public pays 129 shillings for each quarter exported, and the second "
                "tax is `124/5` times the first. That is Smith's £6 4s against 5s. If "
                "the rise were 1s. instead, the total would be 36,000 and the second tax "
                "would still exceed the first, `31,000 > 5,000`, because so much more corn "
                "is eaten than sold abroad.",
            ],
        },
        "quiz_title": "Bounties and the corn trade",
        "quiz": [
            {"q": "On Smith's supposition, for every 5s. contributed to pay the corn bounty, "
                  "how much do the people pay in the higher price of corn at home?",
             "a": ["4s.", "31s.", "£7 15s.", "£6 4s."],
             "c": 3,
             "why": "The rise of 4s. a quarter is paid on 31 quarters eaten at home for "
                    "each one exported: `31 × 4 = 124` shillings, which is £6 4s. 4s. is "
                    "the rise on one quarter, 31s. forgets to multiply by the rise, and "
                    "£7 15s. is `31 × 5` shillings, multiplying by the bounty."},
            {"q": "In the preset smith-corn-bounty, what is the total cost of the "
                  "bounty to treasury and home buyers together?",
             "a": ["129,000 shillings", "124,000 shillings", "5,000 shillings",
                   "36,000 shillings"],
             "c": 0,
             "why": "`5,000 + 124,000 = 129,000`. 124,000 is the second tax alone, 5,000 "
                    "the first alone, and 36,000 is the total in the preset "
                    "a-smaller-rise."},
            {"q": "Why does Smith say the corn bounty cannot raise the real value of corn?",
             "a": ["Because exports are too small a share of the crop",
                   "Because corn is sold abroad at a loss",
                   "Because the money price of corn sets the money price of labour and of "
                   "home goods, so a higher price buys no more of them",
                   "Because the bounty is paid to merchants and not to farmers"],
             "c": 2,
             "why": "&ldquo;The nature of things has stamped upon corn a real value, which "
                    "cannot be altered by merely altering its money price.&rdquo; The "
                    "money price of corn regulates the money price of labour and of "
                    "other home-made goods, so the farmer's 4s. buys no more than 3s. 6d. "
                    "did. The other reasons are true or false but are not his argument "
                    "for this point."},
            {"q": "Of the four trades in corn, which does Smith say may have an interest "
                  "opposed to that of the great body of the people?",
             "a": ["The inland dealer", "The importer for home consumption",
                   "The carrier who imports to export again", "The merchant-exporter"],
             "c": 3,
             "why": "&ldquo;That of the merchant-exporter may, and in fact sometimes is.&rdquo; "
                    "If his own country has a dearth and a neighbour a famine, it may pay him "
                    "to carry corn to the neighbour. The inland dealer's interest he calls "
                    "&ldquo;exactly the same&rdquo; as the people's."},
        ],
        "mistakes": [
            ("Taking the 4s. rise as a measurement",
             "It is a supposition, in Smith's words &ldquo;Let us suppose&rdquo;, and the "
             "one-in-thirty-one ratio is from the Tracts, whose computations he says he "
             "does not warrant. "
             "The lab shows what the reasoning implies for those figures and not what the "
             "bounty did."),
            ("Treating the money price of corn as its real price",
             "Smith's point is that a bounty can raise the first and not the second. A "
             "farmer who sells at 4s. where he sold at 3s. 6d. is not better off if 4s. "
             "now buys what 3s. 6d. did. Ricardo's later argument is that restrictions "
             "on importing corn do shift income to landlords, so the question of whose "
             "real income is affected is not closed by Smith's sentence."),
            ("Hearing in the Digression a claim that dealers are good men",
             "The argument is about interest and numbers, not character. Smith says that "
             "a single company holding the whole crop might destroy part of it, and that the "
             "exporter's interest may be opposed to the people's. What he denies is "
             "that the inland dealers, being many and scattered, can combine to raise "
             "the price beyond what the scarcity requires."),
        ],
        "standard": (
            "Finish when you can count the two taxes of a bounty and say what Smith adds about corn.",
            "Given a bounty, the quantity exported, the quantity sold at home and the rise "
            "in the home price, compute the cost to the treasury and to home buyers and "
            "the total for each unit exported, and say in one sentence why Smith "
            "calls the rise in corn's money price nominal."
        ),
        "note": (
            "The lab adds two products and cannot say whether the bounty raised the home "
            "price, by how much, or whether the farmer's real income changed. Smith "
            "supposes a rise of 4s. and takes the one-in-thirty-one ratio from the author of "
            "the Tracts, whose figures he says he does not warrant. Ricardo and Malthus "
            "disagreed with each other and with parts of this chapter on what restrictions "
            "do, and Sen and Thompson disagree with its account of dearths. The ratio of "
            "1,000 to 31,000 is the lesson's scale, and the preset with a rise of 1s. and "
            "the one with no rise were written for it."
        ),
    },
    # ---------------------------------------------------------------- 06
    # PSU text l. 17455-17849 (Book IV, Chapter 6). The favoured and the favouring country
    # l. 17457-17491; the Methuen treaty l. 17492-17530; the masterpiece and the gold
    # l. 17531-17615; the round-about trade l. 17616-17639; coinage and seignorage
    # l. 17640-17849.
    {
        "slug": "treaties-of-commerce",
        "title": "Treaties of Commerce",
        "module": "Book IV, Chapter 6 · Of Treaties of Commerce",
        "one_line": "A treaty that gives one country's goods a lower duty favours its merchants and costs the other's buyers, and Smith reads the Methuen treaty with Portugal that way.",
        "summary": (
            "Chapter 6 takes the third encouragement to exportation: a treaty that gives "
            "one country's goods a favour in another's market. Smith reads it as a "
            "monopoly granted against the home buyers, and applies the reading to the "
            "Methuen treaty. Compute a preferential duty on wine, and read the digression "
            "on coinage, where the word seignorage is explained."
        ),
        "key": [
            "price to buyers = foreign price + duty",
            "a preference lowers one seller's duty only",
            "favoured sellers can raise price under cover",
            "seignorage: a duty on coinage",
            "gold sent for goods is a trade like any other",
        ],
        "key_label": "The sixth chapter in five lines",
        "concepts_intro": (
            "The chapter argues from monopoly, applies it to one famous treaty, and "
            "then, in a long digression, turns to the coin."
        ),
        "concepts": [
            ("A preference as a monopoly",
             "When a country admits one nation's goods on better terms than others', the "
             "favoured merchants enjoy a sort of monopoly there and may sell for a better "
             "price. Smith says the treaty is advantageous to them and disadvantageous "
             "to the merchants of the favouring country, who must buy dearer."),
            ("Still a gain, a smaller one",
             "Smith adds that the favouring country is not made a loser outright, since "
             "it will not sell its goods for less than they cost, or the trade could not "
             "go on. It gains less than it would under free competition."),
            ("Seignorage",
             "A duty taken on coinage, over and above what it costs. Smith says a moderate "
             "one is paid by nobody in the end, because every holder of the coin gets it "
             "back in the advanced value of the coin, and that it stops the melting down and "
             "export of good coin when money passes by tale."),
        ],
        "read_title": "The passage first, then the treaty and the coin",
        "read_intro": (
            "The chapter's first paragraph is its argument, and the Methuen treaty "
            "is the example Smith picks to test it."
        ),
        "body": [
            ("p", "<strong>Book IV, Chapter 6.</strong> When a nation binds itself by treaty "
                  "to let in some foreign country's goods on terms it refuses to others, the "
                  "merchants of the favoured country, Smith says, enjoy a sort of monopoly, "
                  "and the market is more extensive for them and more advantageous. "
                  "&ldquo;Such treaties, however, though they may be advantageous to the "
                  "merchants and manufacturers of the favoured, are necessarily "
                  "disadvantageous to those of the favouring country.&rdquo; A monopoly is "
                  "granted against them to a foreign nation, and they must often buy dearer."),
            ("p", "Think of a shop that tells you it will only buy its wine from one "
                  "wholesaler. The wholesaler no longer needs to be the cheapest, and the "
                  "shop's customers pay for the arrangement. Smith's own balancing sentence "
                  "comes next: the favouring country will not sell below cost, so it "
                  "loses a part of its gain and not all of it. &ldquo;Even the favouring "
                  "country, therefore, may still gain by the trade, though less than if there "
                  "was a free competition.&rdquo;"),
            ("p", "He then turns to those who thought treaties good for a different "
                  "reason, because a country might bind itself against its own interest in "
                  "some goods in the hope that gold and silver would be returned to it. "
                  "The Methuen treaty of 1703 between England and Portugal was praised on "
                  "that ground. It has three articles. Portugal promises to admit English "
                  "woollens as before, on condition that Britain admits Portuguese wines "
                  "paying no more than French wine, less a third part of the customs. Smith "
                  "reads the first as no favour, since Portugal did not bind itself to admit "
                  "English woollens on better terms than anyone's, and the second as "
                  "binding Britain to admit Portuguese wine &ldquo;upon paying only "
                  "two-thirds of the duty which is paid for those of France, the wines most "
                  "likely to come into competition with them&rdquo;. His verdict follows: "
                  "&ldquo;So far this treaty, therefore, is evidently advantageous to "
                  "Portugal, and disadvantageous to Great Britain.&rdquo; &ldquo;It has been "
                  "celebrated, however, as a masterpiece of the commercial policy of "
                  "England.&rdquo;"),
            ("p", "The lab works out what a preferential duty does to a buyer's cost, with "
                  "figures written for the lesson. Only the two-thirds is Smith's. A tun of "
                  "wine from France costs £20 delivered and pays a duty of £30, and a tun "
                  "from Portugal costs £22 and, without a preference, pays the same. In "
                  "<em>french-equal-duty</em>, the buyer pays `20 + 30 = 50` a tun. In "
                  "<em>portuguese-two-thirds</em>, the duty on Portuguese wine falls to "
                  "two-thirds of £30, which is £20, so the buyer pays `22 + 20 = 42` a tun. "
                  "Portuguese wine is cheaper to the buyer by £8 though it costs £2 more to "
                  "bring, and the preference has decided which wine is bought."),
            ("p", "Smith's point, though, is about what happens next. The favoured "
                  "merchants &ldquo;will often sell their goods for a better price than if "
                  "exposed to the free competition of all other nations&rdquo;. The third "
                  "preset, <em>portuguese-dearer</em>, has the Portuguese price rise to £29 "
                  "with the duty at £20, so the buyer pays `29 + 20 = 49`, still under "
                  "France's 50. Compare it with the first preset on 1,000 tuns. The buyers "
                  "pay 49,000 instead of 50,000. The treasury takes `20 × 1,000 = 20,000` "
                  "where it took 30,000. And what goes abroad rises from 20,000 to 29,000, "
                  "which is 9,000 more of the country's produce sent out for the same wine. "
                  "The buyers saved 1,000 and the treasury lost 10,000, so the country's loss "
                  "is `10,000 − 1,000 = 9,000`, which is the extra price paid to Portugal. "
                  "That is Smith's reading in numbers: the cheapness of one thing is the "
                  "dearness of another."),
            ("p", "The lab also prices the alternative of Chapter 2, making the wine at "
                  "home. Each preset gives a tun made in Britain a cost of £600, thirty "
                  "times the French price, which is the ratio Smith gives for wine from "
                  "Scottish hot-walls; the pounds are written for the lesson. The tile for "
                  "the cost of making all at home reads £580,000 a year in "
                  "<em>french-equal-duty</em>, `1,000 × (600 − 20) = 580,000`, £578,000 in "
                  "<em>portuguese-two-thirds</em> and £571,000 in "
                  "<em>portuguese-dearer</em>. Set beside the 9,000, it shows the line "
                  "Smith draws in the chapter's first paragraph, that a preference's cost "
                  "&ldquo;can scarce amount to any positive loss, but only to a lessening of "
                  "the gain which it might otherwise make&rdquo;, where a prohibition is a "
                  "loss outright. In every preset the buyer pays the whole duty on wine "
                  "bought abroad, so the tile for what buyers pay above the cheaper price "
                  "equals the duty collected, £30,000 or £20,000, and the tile for what is "
                  "paid and not collected as duty reads £0. That £0 in "
                  "<em>portuguese-dearer</em> deserves a second look: the extra £7 a tun "
                  "to the favoured merchants is inside the foreign price, where a tile "
                  "that watches the duty cannot see it, and the 9,000 appears only when "
                  "you compare two presets."),
            ("p", "The case for the treaty was gold. Portugal gets from Brazil more gold "
                  "than it can use, and a large share of it comes to England. &ldquo;Mr "
                  "Barretti was informed, that the weekly packet-boat from Lisbon brings, "
                  "one week with another, more than £50,000 in gold to England.&rdquo; "
                  "Smith thinks the sum exaggerated: `50,000 × 52 = 2,600,000` a year "
                  "&ldquo;which is more than the Brazils are supposed to afford&rdquo;. "
                  "Then he supposes it true. The trade &ldquo;would not, upon that account, be "
                  "more advantageous than any other, in which, for the same value sent out, we "
                  "received an equal value of consumable goods in return&rdquo;. Most of "
                  "the gold must be sent out again for goods, and buying the goods directly "
                  "with English produce would be better than buying gold with it and goods "
                  "with the gold. If Britain were shut out of the Portugal trade, gold, "
                  "like every other commodity, would be got somewhere else. He does "
                  "allow the trade one advantage: gold is the most convenient thing to "
                  "carry on the round-about trades, and in that, he says, consists "
                  "&ldquo;the principal advantage of the Portugal trade; and though it is "
                  "not a capital advantage, it is, no doubt, a considerable one&rdquo;."),
            ("p", "He adds a point that returns to Chapter 3: the more gold we import from "
                  "one country, the less we need from others, so that &ldquo;the balance of "
                  "trade, appears to be in our favour with some particular countries, the more "
                  "it must necessarily appear to be against us with many others&rdquo;. And "
                  "he adds an episode. Our merchants had lately been out of humour with "
                  "Portugal, and the people most interested in praising the Portugal trade "
                  "were then inclined to belittle it, saying the gold was mostly for other "
                  "nations. Towards the end of the late war, France and Spain required the "
                  "king of Portugal to shut his ports to British ships, on the notion that "
                  "England could not live without the Portugal trade. Smith's remark is that "
                  "Britain would have lost little and been freed of defending a weak ally."),
            ("p", "The long end of the chapter is about coin, which he says belongs to "
                  "Book I but was kept for this chapter because the law that makes "
                  "coinage free comes from the system's prejudice: &ldquo;Nothing could be more "
                  "agreeable to the spirit of that system than a sort of bounty upon the "
                  "production of money, the very thing which, it supposes, constitutes the "
                  "wealth of every nation.&rdquo; In England coinage was paid by the government. "
                  "When the gold coin was worn to two per cent below its standard weight, "
                  "new coin was melted and sold as bullion at a profit, which Smith "
                  "compares to the web of Penelope: &ldquo;the work that was done in the day was "
                  "undone in the night&rdquo;. A seignorage, a charge on coinage, takes the "
                  "profit away."),
            ("def", ("Seignorage",
                     "A charge on coinage above its cost, kept by the sovereign. In "
                     "France it was eight per cent, and in England coinage was free. "
                     "Smith's rule: the profit of melting down coin is the shortfall of "
                     "its weight below standard minus the seignorage.")),
            ("p", "The rule is exact, and he gives the cases. With a gold coin two per cent "
                  "below standard, a seignorage of five per cent turns a profit into a loss, "
                  "`2 − 5 = −3`, three per cent. A seignorage of two per cent gives "
                  "`2 − 2 = 0`, &ldquo;neither profit nor loss&rdquo;, and one per cent leaves "
                  "a profit of `2 − 1 = 1` instead of two. Smith's conclusion is that "
                  "&ldquo;Wherever money is received by tale, therefore, and not by "
                  "weight, a seignorage is the most effectual preventive of the melting down of "
                  "the coin, and, for the same reason, of its exportation.&rdquo; And a "
                  "moderate one costs nobody anything: &ldquo;though every body advances the "
                  "tax, nobody finally pays it&rdquo;, because money is a commodity "
                  "in which everyone is a merchant and there is no last consumer, and "
                  "everyone gets it back in the advanced value of the coin."),
            ("p", "Later readers have three things to add. Ricardo's 1817 chapter on foreign "
                  "trade uses the very case of English cloth and Portuguese wine, and his "
                  "figures are these: in England a unit of cloth costs the labour of 100 men "
                  "for a year and a unit of wine 120, and in Portugal cloth costs 90 and "
                  "wine 80. Portugal makes both cheaper, yet wine is relatively cheaper "
                  "there, `80/90 = 8/9` of a cloth against `120/100 = 6/5`. If England puts "
                  "its 220 men on cloth and Portugal its 170 on wine, England makes "
                  "`220/100 = 11/5` of cloth and Portugal `170/80 = 17/8` of wine, where "
                  "before each made one of each, so both are better supplied from the "
                  "same labour. Smith could not have answered this, since he died in 1790, "
                  "and it does not decide whether the particular treaty, at the particular "
                  "duties, was good. List argued in 1841 that the Methuen treaty held Portugal "
                  "to wine and left it without manufactures. And Jacob Viner, in 1950, gave "
                  "the effect of a preference two names: trade diversion, in which purchases "
                  "move from the cheaper source to the favoured one, as in the lab's first "
                  "two presets, and trade creation, in which a lower duty brings in trade "
                  "that would not have taken place. A preference can do both, and whether a "
                  "given one does more good than harm depends on which is larger. The next "
                  "course, Colonies and the Agricultural Systems, takes up the fourth "
                  "encouragement Smith lists, the colony."),
        ],
        "lab": ("wonkit", {
            "mode": "trade",
            "view": "make",
            "qty_unit": "tuns",
            "money_unit": "£",
            "preset": "french-equal-duty",
            "presets": [
                {"id": "french-equal-duty",
                 "label": "French wine at £20 with a £30 duty, written for this lesson",
                 "goods": [{"good": "wine", "quantity": 1000, "home": 600, "foreign": 20, "duty": 30}],
                 "expect": {
                    "wtrAbroad": "wine £50",
                    "wtrCheaper": "wine abroad",
                    "wtrProhibit": "£580,000 a year",
                    "wtrDuty": "£30,000 a year",
                    "wtrBuyers": "£30,000 a year",
                    "wtrLoss": "£0 a year",
                 }},
                {"id": "portuguese-two-thirds",
                 "label": "Portuguese wine at £22 with two-thirds of the duty (the ratio is Smith's)",
                 "goods": [{"good": "wine", "quantity": 1000, "home": 600, "foreign": 22, "duty": 20}],
                 "expect": {
                    "wtrAbroad": "wine £42",
                    "wtrCheaper": "wine abroad",
                    "wtrProhibit": "£578,000 a year",
                    "wtrDuty": "£20,000 a year",
                    "wtrBuyers": "£20,000 a year",
                    "wtrLoss": "£0 a year",
                 }},
                {"id": "portuguese-dearer",
                 "label": "The favoured merchants raise their price to £29, written for this lesson",
                 "goods": [{"good": "wine", "quantity": 1000, "home": 600, "foreign": 29, "duty": 20}],
                 "expect": {
                    "wtrAbroad": "wine £49",
                    "wtrCheaper": "wine abroad",
                    "wtrProhibit": "£571,000 a year",
                    "wtrDuty": "£20,000 a year",
                    "wtrBuyers": "£20,000 a year",
                    "wtrLoss": "£0 a year",
                 }},
            ],
            "panel_title": "What a preferential duty does to the price of wine",
            "panel_intro": (
                "Each preset prices one source of wine to the British buyer: its price "
                "delivered, the duty, and the cost of a tun made in Britain, set at £600, "
                "thirty times the French price, which is the ratio Smith gives for Scottish "
                "wine in Chapter 2. The lab prints what the wine costs the buyer, what the "
                "treasury collects, and what a prohibition would cost the country. Compare "
                "the three: the preference changes "
                "who is cheapest to the buyer, and the third shows what the favoured "
                "merchants' monopoly can do to the price."
            ),
        }),
        "steps_title": "Reading a preferential duty",
        "steps_intro": "Four steps, the same for any pair of sources and any preference.",
        "steps": [
            ("Price each source to the buyer",
             "Add the duty to the foreign price. A buyer chooses the source with the "
             "smaller sum, not the smaller price."),
            ("Apply the preference",
             "Lower the duty on the favoured source only, and price both again. If the "
             "favoured source is now the cheaper, the trade has moved."),
            ("Split the buyer's price",
             "What the buyer pays is the foreign price, which goes abroad, plus the duty, "
             "which goes to the treasury. A preference changes the split as well as "
             "the sum."),
            ("Compare what goes abroad",
             "The country as a whole gains or loses by the change in what it sends out. "
             "If the favoured price rose, the extra went to the favoured merchants "
             "and not to the treasury."),
        ],
        "worked": {
            "title": "French wine and favoured Portuguese wine",
            "intro": [
                "Take the presets, with figures written for the lesson. The two-thirds is "
                "Smith's. The country buys 1,000 tuns.",
            ],
            "lines": [
                "French, equal duty:  20 + 30 = 50",
                "Portuguese, two-thirds duty:  22 + (2/3) · 30 = 22 + 20 = 42",
                "Portuguese, price raised:  29 + 20 = 49",
                "treasury:  30,000 against 20,000",
                "sent abroad:  20,000 against 29,000",
                "country's loss:  (30,000 − 20,000) − (50,000 − 49,000) = 9,000",
                "a prohibition instead:  1,000 · (600 − 20) = 580,000",
            ],
            "after": [
                "Buyers pay 1,000 less, the treasury takes 10,000 less, and 9,000 more "
                "goes to Portugal for the same wine. The favoured merchants gain what "
                "the country loses, which is Smith's account of a preference. A "
                "prohibition, at Smith's thirtyfold home cost, would cost the country "
                "£580,000: a preference lessens the gain, and a prohibition removes it.",
            ],
        },
        "quiz_title": "Preferences and coin",
        "quiz": [
            {"q": "On Smith's reading of the Methuen treaty, who gains and who loses?",
             "a": ["Portugal's merchants gain and Britain's buyers of wine lose",
                   "Britain's merchants gain and Portugal's buyers lose",
                   "Both countries gain equally, since each opens its market",
                   "Neither gains, since gold is the only thing exchanged"],
             "c": 0,
             "why": "&ldquo;So far this treaty, therefore, is evidently advantageous to "
                    "Portugal, and disadvantageous to Great Britain.&rdquo; Portugal bound "
                    "itself only to admit woollens on the old terms. He adds that even Britain "
                    "may still gain a little by the trade, but less than under free "
                    "competition."},
            {"q": "In the preset portuguese-dearer the duty revenue on 1,000 tuns "
                  "is £20,000. By how much does it differ from the preset "
                  "french-equal-duty?",
             "a": ["It rises by £9,000", "It is unchanged", "It falls by £1,000",
                   "It falls by £10,000"],
             "c": 3,
             "why": "The duty falls from £30 to £20 a tun, so the revenue falls from "
                    "`30 × 1,000 = 30,000` to `20 × 1,000 = 20,000`, a fall of £10,000. "
                    "£9,000 is the rise in what is sent abroad and £1,000 the buyers' "
                    "saving, and neither is the treasury's figure."},
            {"q": "On Ricardo's figures (England: cloth 100, wine 120; Portugal: cloth 90, "
                  "wine 80, in men for a year), how much cloth does England make if all 220 "
                  "of its men make cloth?",
             "a": ["2 units", "1 unit", "11/5 units", "220 units"],
             "c": 2,
             "why": "`220/100 = 11/5`. Before, England's 220 men made one unit of cloth "
                    "and one of wine, so it now makes more cloth than the one it gave up "
                    "(and Portugal makes `170/80 = 17/8` of wine), though Portugal "
                    "makes both cheaper. These are Ricardo's figures, not Smith's."},
            {"q": "Smith's gold coin is two per cent below its standard weight. What is the "
                  "result of melting new coin if there is a seignorage of five per cent?",
             "a": ["A profit of three per cent", "A loss of three per cent",
                   "Neither profit nor loss", "A profit of two per cent"],
             "c": 1,
             "why": "Profit from melting is the shortfall minus the seignorage, "
                    "`2 − 5 = −3`, so there is a loss of three per cent. A profit of two per "
                    "cent is what there would be with no seignorage, and neither would be "
                    "the case at a seignorage of two."},
        ],
        "mistakes": [
            ("Taking Smith to say a treaty with a customer is always a loss",
             "He says the favouring country may still gain, though less than under free "
             "competition. His objection is to the claim that a preference is a "
             "masterpiece, and to its effect on what buyers pay."),
            ("Counting the gold from Portugal as a gain on its own",
             "&ldquo;this trade would not, upon that account, be more advantageous than "
             "any other&rdquo; in which an equal value of consumable goods came back. "
             "Gold is one of the things a country buys, and most of what is imported "
             "must be sent out again for goods."),
            ("Thinking a seignorage is a tax that someone must bear",
             "Smith says a moderate one is paid by nobody in the end, since everyone who "
             "advances it gets it back in the advanced value of the coin. If it is "
             "large enough to encourage false coining, the argument no longer holds, and "
             "he says so."),
        ],
        "standard": (
            "Finish when you can price a preference and say who gains and who pays.",
            "Given the foreign price and duty of two sources and a preferential duty on "
            "one, compute what the buyer pays for each, what the treasury takes, and "
            "what goes abroad, and say in one sentence how Smith reads the Methuen "
            "treaty."
        ),
        "note": (
            "The lab prices one source of wine at a time and holds the quantity fixed, "
            "so it cannot say how much trade a preference moves, how favoured merchants "
            "set their price, or whether a larger market compensates the buyers. The "
            "two-thirds is Smith's and every pound in the presets was written for the "
            "lesson, with the £600 home cost borrowing Smith's thirtyfold ratio from "
            "Chapter 2, so the 9,000 is what the arithmetic implies for them. Ricardo's "
            "figures are his and not Smith's. Whether the Methuen treaty did Portugal good "
            "or harm in the long run is argued over by historians of both countries, "
            "and no figure here decides it."
        ),
    },
]
