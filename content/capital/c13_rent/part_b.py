"""Ground Rent, lessons 7-11 -- Volume III, Chapters 43-47.

Every quotation is copied from /mnt/project-files/capital-texts/volume-3-kerr.txt
(Untermann's translation of Volume III, Kerr edition); the comment beside each
lesson gives its line numbers. Footnote numerals in the text are left out of
the quotations, a drop capital is printed as an ordinary capital, and the
translator's double quotation marks inside a quotation are printed as single
curly quotes. Nothing else is changed.

Chapter 43 is in two hands: its first part, in square brackets signed F. E.,
is Engels' (the manuscript had only the title), and the rest is Marx's; the
lesson says which is which. Chapter 44 has a bracketed correction by Engels,
which the lesson states beside Marx's figures. As in part_a, the labs reckon
in shillings: Marx's £2½ is 50s and his £3 a quarter is 60s.
"""

LESSONS = [
    # ---------------------------------------------------------------- 07
    # Kerr vol. 3, l. 6398-6400 (rent a reason for the earlier rise of
    # price). Inline: l. 6094 and l. 6123 (Engels' brackets), l. 5849-5851
    # (Ricardo's case, in Ch. 40), l. 6267-6271 (Engels: 1846, prairies),
    # l. 6302 and l. 6311-6316 (B's doses; the individual average price),
    # l. 6338-6346 (rent absorbed), l. 6352 (A-1 and A-2; 21 pounds, 15
    # pounds, 3 pounds), l. 6396 (rise to 4 pounds; a rent formed on A).
    {
        "slug": "dr-ii-rising-price",
        "title": "Differential Rent II at a Rising Price of Production",
        "module": "Chapter 43 · Differential Rent No. II—Third Case: Rising Price of Production",
        "one_line": "When the extra corn the market needs can only come from a dose less productive than the worst soil's, the price rises to that dose's cost, and every rent rises with it, the worst soil's included.",
        "summary": (
            "The third case is the one Ricardo thought was the rule: more corn is needed, and "
            "it can only be had from less productive capital, so the regulating price rises. "
            "Compute the rents when the extra quarters come from weaker doses on soil B, from "
            "two soils worse than A, and from a weak dose on the best soil, and see why rent "
            "follows the price, and where Marx says landed property hastens the rise."
        ),
        "key": [
            "least productive dose needed sets the price",
            "B's weak doses: price 60s → 80s",
            "A−1, A−2 brought in: price 120s",
            "worst soil A then pays rent too",
            "rent follows price; leases hasten it",
        ],
        "key_label": "The third case in five lines",
        "concepts_intro": (
            "Chapter 43 has two authors. Engels wrote the opening, because Marx left only the "
            "title, and Marx's own text that follows draws the conclusions of the whole run of "
            "tables."
        ),
        "concepts": [
            ("The rising-price case",
             "The extra product the market needs costs more per quarter than the old "
             "regulating soil's, whether it comes from a weak dose on land already farmed or "
             "from a worse soil. That dearer quarter now sets the price of all."),
            ("Rent follows the price",
             "Every investment that produces more cheaply than the new regulator now has a "
             "surplus, so every rent rises, and soil A, which paid none, pays one."),
            ("The individual average price",
             "A tenant sells his whole acre's product, not doses. Marx shows that weak doses "
             "raise the acre's average cost toward the regulating price and eat into the "
             "rent, unless a fixed rent stops them."),
        ],
        "read_title": "Marx's conclusion first, then the cases",
        "read_intro": (
            "The passage comes near the end of the chapter, in Marx's hand. It qualifies the "
            "rule the lesson otherwise teaches, so it is worth reading before the arithmetic."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 43.</strong> &ldquo;The rise of the general price "
                  "of production, which becomes necessary when the limit is narrowed beyond the "
                  "ordinary, is in this case not merely the cause of a rise of the differential "
                  "rent, but the existence of differential rent as rent is at the same time a "
                  "reason for the earlier and more rapid rise of the general price of production, "
                  "in order to insure by this means the supply of the needed larger "
                  "product.&rdquo;"),
            ("p", "Bread gets dearer and landlords get richer: anyone in England in 1815 could "
                  "see the two go together, and the obvious conclusion was that the landlords' "
                  "rents made the bread dear. Ricardo's reply, at its strongest, was that this "
                  "had cause and effect backwards. Corn is dear because the last land the "
                  "country needs is poor and costly to farm; rent is only what the better land "
                  "earns at that price; abolish every rent and the price of corn would not fall "
                  "a penny. Marx agrees with the first half and, in the passage, adds a "
                  "qualification to the second."),
            ("p", "The chapter's opening is Engels', and he says so: the manuscript had "
                  "&ldquo;only its title&rdquo;. A rising price, he begins, means the least "
                  "productive investment has become less productive than before, or that soil "
                  "worse than A is needed. He then sets out twenty-one tables, Tables VII to X a in "
                  "pounds and XI to XXIV in bushels and shillings (pages 829 to 839 of the Kerr "
                  "edition). Most of them price each soil's whole product at its average over "
                  "both doses, a rule the lab does not apply, so the lab takes its cases from "
                  "Marx's own pages instead, in shillings as before."),
            ("p", "First, the worse-investment preset. Marx's soil B yields 2 quarters on its "
                  "first 50s and 1½ on its second, A yields 1, and the price is 60s. Now the "
                  "market needs 1½ quarters more, and the only way to get them is a further 100s "
                  "on B at 80s a quarter, his &ldquo;4 pounds sterling&rdquo;. (The lab takes "
                  "equal doses, so the 100s goes in as two doses of 50s yielding ¾ quarter "
                  "each.) If the market demands them, &ldquo;then the regulating market price would have to rise to 4 pounds "
                  "sterling per quarter. In consequence of this rise in the regulating market "
                  "price the rent upon B would rise for the first and second investment, and a "
                  "rent would be formed upon A.&rdquo; The lab prints a price of 80s, rents of "
                  "20s on A and 160s on B, against 0s and 90s before."),
            ("p", "Second, the new-soil preset, Marx's other route. The extra quarters come from "
                  "soils worse than A, which he calls A−1 and A−2: 1½ quarters on A−1 at 80s a "
                  "quarter, and the last quarter on A−2 at 120s, his £6. Now 120s regulates. "
                  "&ldquo;The 3½ quarters of B would then be sold at 21 pounds sterling instead "
                  "of 10½ pounds sterling, and this would leave a rent of 15 pounds "
                  "sterling&rdquo;; A's quarter leaves &ldquo;a rent of 3 pounds "
                  "sterling&rdquo;. The lab agrees: 300s on B, 60s on A, 60s on A−1 and nothing "
                  "on A−2, 420s in all."),
            ("p", "Third, the ricardo-case preset, which is the case Marx says Ricardo made the "
                  "only one. All four soils are farmed, and the extra corn comes from a second "
                  "dose on the best soil, D, yielding only ¾ quarter. The price rises to 80s, and "
                  "every rent rises with it: A 20s, B 100s, C 180s, D 260s, 560s against Table I's "
                  "360s. In Chapter 40 Marx describes exactly this: rent rising &ldquo;upon all "
                  "classes of soil just as though inferior soil than A were regulating the "
                  "market&rdquo;, and wages rising with the price of bread. His summary: "
                  "&ldquo;Differential rent would then rise in connection with a falling rate "
                  "of profit.&rdquo;"),
            ("def", ("The rising-price case",
                     "The added product the market needs can be had only at a higher price of "
                     "production per quarter than the old regulator's. The new, dearer dose "
                     "regulates, and every rent is recomputed at the higher price.")),
            ("p", "Now the passage. Marx works through what happens on one acre of B when the "
                  "tenant adds weak doses at an unchanged price. If he sells the acre's whole "
                  "product, the strong doses' surplus can cover the weak doses' shortfall: add "
                  "doses that lose 30s and 60s at the regulating price, and the 90s of rent is "
                  "absorbed into the average profit, &ldquo;the rent disappears&rdquo;, and the "
                  "price need not rise at all. But the tenant has signed a lease. &ldquo;If the "
                  "capitalist renter once pays 4½ pounds sterling of rent for the first two "
                  "investments of capital, he must continue to pay them&rdquo;, and every weak "
                  "dose is then a straight loss to him. He stops adding capital sooner, so the "
                  "extra corn has to come from somewhere dearer, sooner. That is the "
                  "&ldquo;earlier and more rapid rise&rdquo;: rent does not set the price, but "
                  "the fixed rent narrows the cheaper routes to more corn."),
            ("p", "Engels closes his half of the chapter with history. When the English corn "
                  "duties were repealed in 1846, manufacturers expected the landowners to be "
                  "ruined; instead tenants were bound to invest more per acre, landlords voted "
                  "themselves drainage subsidies, and rents rose with the capital laid on the "
                  "land, as the constant-price lesson computes. Ruin came later, he writes, from "
                  "the prairies and the pampas: &ldquo;Our second case Variant II (falling prices "
                  "and falling productivity of the additional investment of capital) became the "
                  "rule for Europe.&rdquo;"),
            ("p", "The objection from later economics is mostly agreement. On the marginal "
                  "account the price of corn is set at the margin and rent is the surplus "
                  "inside it, which is Ricardo's mechanism generalised to every input. Where "
                  "economists part from this chapter is over what the surplus is: the earnings "
                  "of a scarce factor on their account, a share of surplus value on Marx's. What "
                  "the chapter adds that a pure margin account leaves out is the lease, a "
                  "contract that fixes the rent and so changes where the margin falls."),
            ("p", "In the new-soil preset A pays rent because something worse came in below it. "
                  "The next lesson, “Differential Rent Also on the Worst Cultivated Soil”, finds "
                  "a way for A to pay rent with nothing worse in use at all."),
        ],
        "lab": ("capkit", {
            "mode": "rent",
            "view": "dr2",
            "money_unit": "s",
            "qty_unit": "quarter",
            "price_case": "rising",
            "preset": "worse-investment",
            "presets": [
                {"id": "worse-investment", "label": "Marx's figures: B's further 100s yields 1½ quarters at 80s (his £4)",
                 "soils": [{"name": "A", "capital": 50, "outputs": [1]},
                           {"name": "B", "capital": 50, "outputs": [2, "3/2", "3/4", "3/4"]}],
                 "profit_rate": "1/5", "regulating": "auto", "former_price": 60, "expect": {"rtPrice": "80s a quarter", "rtRents": "20s, 160s", "rtTotal": "180s"}},
                {"id": "new-soil", "label": "Marx's figures: soils A−1 at 80s and A−2 at 120s brought in",
                 "soils": [{"name": "A", "capital": 50, "outputs": [1]},
                           {"name": "B", "capital": 50, "outputs": [2, "3/2"]},
                           {"name": "A−1", "capital": 100, "outputs": ["3/2"]},
                           {"name": "A−2", "capital": 100, "outputs": [1]}],
                 "profit_rate": "1/5", "regulating": "auto", "former_price": 60, "expect": {"rtPrice": "120s a quarter", "rtRents": "60s, 300s, 60s, 0s", "rtTotal": "420s"}},
                {"id": "ricardo-case", "label": "A to D, with a second dose on D yielding ¾ quarter",
                 "soils": [{"name": "A", "capital": 50, "outputs": [1]},
                           {"name": "B", "capital": 50, "outputs": [2]},
                           {"name": "C", "capital": 50, "outputs": [3]},
                           {"name": "D", "capital": 50, "outputs": [4, "3/4"]}],
                 "profit_rate": "1/5", "regulating": "auto", "former_price": 60, "expect": {"rtPrice": "80s a quarter", "rtRents": "20s, 100s, 180s, 260s", "rtTotal": "560s"}},
            ],
            "panel_title": "When the extra corn costs more",
            "panel_intro": (
                "Each soil's doses go in, with the former price of 60s. The least productive "
                "dose in use sets the new price; every soil's rent is recomputed at it. "
                "Compare the three presets' rents on A: the worst soil pays rent in all of "
                "them."
            ),
        }),
        "steps_title": "Computing rents when the price rises",
        "steps_intro": "Four steps, when the extra product needs a dearer source.",
        "steps": [
            ("Price the new source",
             "Divide the capital and profit of the dose or soil that supplies the extra product "
             "by its output. If it is above the old price, it is the new regulating price."),
            ("Revalue every dose",
             "Value each dose in use at the new price, less its capital and profit. Every dose "
             "that is cheaper than the new regulator now has a surplus."),
            ("Add per soil",
             "Sum each soil's surpluses. The old regulating soil now pays rent; the new "
             "regulator pays none."),
            ("Compare with the lease",
             "Set the new rents beside the old. Where a rent is fixed by lease, a tenant adding "
             "weak doses bears their losses himself, which is why he stops sooner."),
        ],
        "worked": {
            "title": "Marx's soils A−1 and A−2",
            "intro": [
                "A yields 1 quarter on 50 shillings; B yields 2 and 1½ on two doses of 50s; the "
                "extra corn needs A−1, 1½ quarters on 100s, and A−2, 1 quarter on 100s. Profit "
                "is 20%. You want the price and the rents.",
            ],
            "lines": [
                "A−2:  120 / 1 = 120 shillings a quarter",
                "A:  120 − 60 = 60 shillings",
                "B:  (7/2) · 120 − 120 = 300 shillings",
                "A−1:  (3/2) · 120 − 120 = 60 shillings",
                "total:  60 + 300 + 60 + 0 = 420 shillings",
            ],
            "after": [
                "Marx's £3 on A and £15 on B. Before the new soils came in, at 60s, A paid "
                "nothing and B 90s.",
            ],
        },
        "quiz_title": "A rising price and the rents",
        "quiz": [
            {"q": "A yields 1 quarter on 50s at 20%, and the extra corn needed comes from a dose "
                  "on C yielding ½ quarter on 50s. What rent does A now pay?",
             "a": ["Nothing", "60s", "120s", "30s"],
             "c": 1,
             "why": "The new regulating price is `60 / (1/2) = 120`s, so A's quarter fetches "
                    "120s against 60s, a rent of 60s. Nothing was its rent at the old price; "
                    "120s is its whole product; 30s halves the wrong figure."},
            {"q": "On Ricardo's account, which Marx accepts in part, why does corn become "
                  "dearer when demand grows?",
             "a": ["Because landlords raise their rents",
                   "Because the extra corn comes from land or capital that produces it at a higher cost",
                   "Because farmers' profits rise",
                   "Because wages fall"],
             "c": 1,
             "why": "The price is set by the costliest source the market needs; rent is the "
                    "surplus the cheaper sources make at that price. Profits fall in Ricardo's "
                    "account, and wages rise in money with the price of bread."},
            {"q": "What does Marx add to Ricardo in the chapter's conclusion?",
             "a": ["That rent enters the price of corn as a tax would",
                   "That a rent fixed by lease stops tenants adding weak doses sooner, so the price rises earlier",
                   "That the price of corn never rises",
                   "That only the worst soil pays rent"],
             "c": 1,
             "why": "Marx calls the existence of rent &ldquo;a reason for the earlier and more "
                    "rapid rise&rdquo; of the price, because a tenant who must keep paying the "
                    "rent cannot set weak doses against it. He does not say it enters as a tax; "
                    "the price does rise in this case; and in it the worst soil is the one that "
                    "starts paying."},
        ],
        "mistakes": [
            ("Thinking rent is the cause of high food prices",
             "Dear bread and high rents rise together, so the rents look like the cause. In the "
             "worse-investment preset the price rises to 80s because the extra 1½ quarters "
             "cost 80s each to grow; the rents of 20s on A and 160s on B are what the cheaper "
             "doses make at that price. Marx's qualification is narrower than the "
             "misconception: a fixed rent makes the rise come sooner, by stopping the tenant "
             "from offsetting weak doses against strong ones."),
            ("Thinking diminishing returns always raise the price",
             "Weak doses raise the price only when they are needed and nothing cheaper is "
             "available. In the constant-price lesson every second dose was weaker than the "
             "first and the price did not move."),
            ("Taking Engels' opening for Marx's",
             "The bracketed first part of the chapter, with its bushel tables, is Engels', "
             "written because the manuscript had only the title. The conclusions about the "
             "lease and the earlier rise are Marx's."),
        ],
        "standard": (
            "Finish when you can compute the rents after a rise in the regulating price.",
            "Given each soil's doses and outputs and the former regulating price, compute the "
            "new regulating price, each soil's rent including the old regulating soil's, and "
            "the total."
        ),
        "note": (
            "The lab values doses separately at the regulating price. Marx's argument about "
            "the lease turns on the alternative, the acre's individual average price, which "
            "the lab does not compute; the figures for it in the lesson are his. The "
            "ricardo-case preset's ¾ quarter is illustrative. Engels' Tables VII to XXIV, "
            "which mostly price a soil's product at its average, are not reproduced."
        ),
    },
    # ---------------------------------------------------------------- 08
    # Kerr vol. 3, l. 6418 (the worst soil may also carry a rent). Inline:
    # l. 6414-6416 (3¾ on A, 4 on A-1, 3½ on B; 15¾, 9½, 6¼; A a rent of ½),
    # l. 6422-6424 (Engels: 1/9 and 4½), l. 6432 (A-1 at 4: rent of one
    # pound on A), l. 6462 (A at 3¾: a rent of ¾), l. 6454 (property
    # raises the price of production). Tables: Kerr p. 858 (before: A 1, B
    # 3½, C 5½, D 7½ at £3, rent £31½; after: price £3½, rents ½, 6¼, 13¼,
    # 20¼, total £40¼).
    {
        "slug": "rent-on-the-worst-soil",
        "title": "Differential Rent Also on the Worst Cultivated Soil",
        "module": "Chapter 44 · Differential Rent Even upon the Worst Soil under Cultivation",
        "one_line": "If the cheapest way to get more corn is another dose on a better soil, that dose sets the price, and the worst soil's first capital, now cheaper than the regulator, pays a differential rent.",
        "summary": (
            "Chapter 44 finds a differential rent on soil A without any worse soil in use. "
            "Compute the rents when the extra quarter comes from a weaker dose on B at 70s, "
            "when it comes from a second dose on A itself at 75s, and when both are on offer "
            "and the cheaper one is chosen; then compare Marx's figures with the correction "
            "Engels printed beside them."
        ),
        "key": [
            "regulator: a second dose on a better soil",
            "B's extra dose at 70s: A pays 10s",
            "A's own second dose at 75s: A pays 15s",
            "cheaper extra source is the one used",
            "Engels' average rule: A pays £1/9",
        ],
        "key_label": "The worst soil's rent in five lines",
        "concepts_intro": (
            "Until now A paid no rent unless something worse came in below it. Chapter 44 "
            "shows the rule of the regulating investment can put a better soil's dose in that "
            "place."
        ),
        "concepts": [
            ("A dose as regulator",
             "The investment that sets the price need not be the first capital on the worst "
             "soil. It is whichever source supplies the last quarters the market needs at the "
             "least cost per quarter, and it may be a second or third dose on B."),
            ("Rent on the worst soil",
             "When a dose dearer than A's first one regulates, A's first capital produces "
             "below the price and has a surplus. It is a differential rent, measured against "
             "that dose, with nothing worse than A in use."),
            ("Engels' correction",
             "Engels argued that the tenant of B sells his whole product and pays a fixed rent, "
             "so the regulating price is his average cost per quarter including the old rent. "
             "On that rule A's rent is much smaller."),
        ],
        "read_title": "The claim first, then three ways to get one more quarter",
        "read_intro": (
            "The passage states the chapter's result. Marx reaches it by pricing an extra "
            "quarter of wheat three ways."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 44.</strong> &ldquo;As soon as differential rent "
                  "No. II comes into action by successive investments of capital, the limits of "
                  "the rising price of production may be regulated by better soil, and the worst "
                  "soil, the basis of differential rent No. I, may also carry a rent.&rdquo;"),
            ("p", "Picture three ways a country can grow one more quarter of wheat: plough some "
                  "worse land, put a second capital on its worst land, or put another capital on "
                  "a better field. Whichever is cheapest per quarter will be used, and whichever "
                  "is used sets the price. Marx prices all three. A yields 1 quarter at 60s, his "
                  "£3; B yields 3½ quarters from two doses, C 5½ and D 7½, as in his first "
                  "table on page 858, where the rents are 90s, 210s and 330s. The extra "
                  "quarter would cost 80s on a worse soil A−1, 75s from a second dose on A (his "
                  "&ldquo;3¾ pounds sterling&rdquo;), and 70s from another dose on B (his "
                  "&ldquo;3½ pounds sterling&rdquo;)."),
            ("p", "B's is cheapest, so B's extra dose regulates at 70s. That is the marx preset. "
                  "(Marx's extra quarter costs 70s from a dose of its own size; the lab takes "
                  "equal doses, so it enters as 6/7 of a quarter from a dose of 50s, the same "
                  "70s a quarter.) B's first two doses now earn 125s, Marx's "
                  "&ldquo;6¼ pounds sterling, as against the former 4½&rdquo;. And A, the worst "
                  "soil, whose single quarter costs 60s and sells for 70s, earns 10s: "
                  "&ldquo;one acre of A would also yield a rent of ½ pound sterling&rdquo;. C "
                  "and D, valued at 70s, pay 265s and 405s. The tile prints rents of 10s, 125s, "
                  "265s and 405s, 805s in all, which is the £40¼ of Marx's second table."),
            ("p", "The both preset makes the choice explicit. It offers the lab A's second dose "
                  "at 75s and B's third at 70s, with a market just large enough for the doses already in use and one extra dose. The "
                  "lab takes the cheapest doses first, B's third dose fills the market, A's "
                  "second is not used, and the rents are the marx preset's again. That is Marx's "
                  "reasoning: if the quarter cost more on B than on A, &ldquo;then it would "
                  "naturally be produced upon A, not upon B&rdquo;."),
            ("p", "The on-a preset is the second route, A's own second dose at 75s. Marx takes "
                  "the averaging rule first here: A's two quarters cost 135s together, an average "
                  "of 67s 6d, his 3⅜ pounds, and if that average regulates, A pays no rent. Only "
                  "if the second quarter is sold at its own 75s does A regulate through its second "
                  "capital, and then its first capital, at 60s, earns "
                  "15s: &ldquo;the soil A would yield a rent of ¾ pound sterling&rdquo;, as Marx "
                  "says, and B's rent rises to 142s 6d, C's to 292s 6d and D's to 442s 6d. Marx adds that this can last only as "
                  "long as no unfarmed land of A's quality is on offer, because new A at 60s "
                  "would bring the price back down; unless, that is, the landlord has had time "
                  "to fix the surplus in a lease. Worse soil, A−1 at 80s, would be a different "
                  "case: A would pay 20s, his &ldquo;one pound sterling&rdquo;, but as the "
                  "better of two soils, under differential rent I."),
            ("def", ("Differential rent on the worst soil",
                     "The surplus that the worst cultivated soil's first capital makes when "
                     "the regulating price is set by a dearer additional dose, on that soil or "
                     "a better one, with no worse soil in use.")),
            ("p", "Engels, editing the chapter, objected to Marx's figures in a bracketed note, "
                  "and opened it bluntly: &ldquo;This, again, is not quite "
                  "correctly calculate.&rdquo; B's tenant, he argues, has to meet 9½ pounds of "
                  "cost and profit for his 4½ quarters and the 4½ pounds of rent already fixed in "
                  "his lease, 14 pounds in all, or 3 1/9 pounds a quarter; that average becomes "
                  "the regulating price. (The Kerr text prints the average as 3½ pounds, twice; "
                  "14 pounds over 4½ quarters is 3 1/9, and only 3 1/9 leaves A the 1/9 pound "
                  "Engels states.) Then &ldquo;the rent upon A would amount to 1/9 pound "
                  "sterling instead of ½ pound sterling and that upon B would remain 4½ pounds "
                  "sterling&rdquo;. Engels' rule is the average price of the acre, which the last "
                  "lesson met; Marx's figures value the extra dose by itself. The lab follows "
                  "Marx's rule, and both men reach the chapter's point: the regulating price can "
                  "be set by a better soil, and the worst soil can pay rent."),
            ("p", "The chapter's last pages generalise. When a natural power suffices for the "
                  "demand, it adds nothing to price; when more is needed and the extra must be "
                  "had by spending capital, &ldquo;a new additional element enters into "
                  "capital&rdquo; and the price rises. And it draws a consequence for landed "
                  "property: by fixing in rent the surplus of better-farmed A, the landlord "
                  "&ldquo;would maintain a higher price of production than the necessary one "
                  "and thus create a rent&rdquo;."),
            ("p", "A later economist would put the whole chapter in one sentence: the price is "
                  "set by the marginal source of supply, whichever field it lies on, and every "
                  "inframarginal unit earns a rent. On that account nothing is special about "
                  "the worst soil. What the chapter adds is the lease again, in Engels' "
                  "correction and in the landlord fixing a surplus as rent."),
            ("p", "Every rent so far has been differential, a difference between two prices of "
                  "production. The next lesson, “Absolute Ground Rent”, asks whether the worst "
                  "soil pays rent even when nothing is dearer than it."),
        ],
        "lab": ("capkit", {
            "mode": "rent",
            "view": "dr2",
            "money_unit": "s",
            "qty_unit": "quarter",
            "price_case": "worst-soil",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's table, p. 858: B's extra dose at 70s a quarter (his £3½)",
                 "soils": [{"name": "A", "capital": 50, "outputs": [1]},
                           {"name": "B", "capital": 50, "outputs": [2, "3/2", "6/7"]},
                           {"name": "C", "capital": 50, "outputs": [3, "5/2"]},
                           {"name": "D", "capital": 50, "outputs": [4, "7/2"]}],
                 "profit_rate": "1/5", "regulating": "auto", "former_price": 60, "expect": {"rtPrice": "70s a quarter", "rtRents": "10s, 125s, 265s, 405s", "rtTotal": "805s"}},
                {"id": "on-a", "label": "Marx's figures: a second dose on A at 75s a quarter (his £3¾)",
                 "soils": [{"name": "A", "capital": 50, "outputs": [1, "4/5"]},
                           {"name": "B", "capital": 50, "outputs": [2, "3/2"]},
                           {"name": "C", "capital": 50, "outputs": [3, "5/2"]},
                           {"name": "D", "capital": 50, "outputs": [4, "7/2"]}],
                 "profit_rate": "1/5", "regulating": "auto", "former_price": 60, "expect": {"rtPrice": "75s a quarter", "rtRents": "15s, 142s 6d, 292s 6d, 442s 6d", "rtTotal": "892s 6d"}},
                {"id": "both", "label": "Both extra doses on offer; the market takes one of them",
                 "soils": [{"name": "A", "capital": 50, "outputs": [1, "4/5"]},
                           {"name": "B", "capital": 50, "outputs": [2, "3/2", "6/7"]},
                           {"name": "C", "capital": 50, "outputs": [3, "5/2"]},
                           {"name": "D", "capital": 50, "outputs": [4, "7/2"]}],
                 "profit_rate": "1/5", "regulating": "auto", "market_limit": "257/14",
                 "former_price": 60, "expect": {"rtPrice": "70s a quarter", "rtRents": "10s, 125s, 265s, 405s", "rtTotal": "805s"}},
            ],
            "panel_title": "Who sets the price of the last quarter",
            "panel_intro": (
                "Soils A to D and their doses go in. The least productive dose in use, or with "
                "a market limit the last one needed, sets the price; A's first capital, cheaper "
                "than that, pays rent. Compare marx with on-a: the cheaper extra dose means a "
                "lower price and a smaller rent on A."
            ),
        }),
        "steps_title": "Finding a rent on the worst soil",
        "steps_intro": "Four steps, when the market needs more than the first capitals supply.",
        "steps": [
            ("Price every extra source",
             "For each way of getting the extra product, a worse soil, a second dose on the "
             "worst soil or a further dose on a better one, compute capital and profit per "
             "quarter."),
            ("Choose the cheapest",
             "The cheapest source that supplies what the market needs is the one used, and "
             "its price per quarter becomes the regulating price."),
            ("Value the worst soil's first capital",
             "If it produces below the new price, the difference on its output is a "
             "differential rent, though nothing worse is in use."),
            ("Recompute the other rents",
             "Value every other dose in use at the new price, and add per soil."),
        ],
        "worked": {
            "title": "Marx's extra quarter on B",
            "intro": [
                "A yields 1 quarter on 50 shillings at 20%; B yields 2 and 1½ on two doses "
                "(C and D are left out here); "
                "the extra quarter costs 70s on B, 75s on A and 80s on worse soil. You want "
                "the price and the rents.",
            ],
            "lines": [
                "cheapest extra source:  B, at 70 shillings",
                "A:  70 − 60 = 10 shillings",
                "B, first two doses:  (7/2) · 70 − 120 = 125",
                "B, extra dose:  no surplus at its own price",
                "A and B together:  10 + 125 = 135 shillings",
            ],
            "after": [
                "Marx's ½ pound on A and 6¼ pounds on B. On Engels' rule the price is 3 1/9 "
                "pounds, about 62s, A pays 1/9 pound and B keeps its old 4½ pounds.",
            ],
        },
        "quiz_title": "Rent on the worst soil",
        "quiz": [
            {"q": "A yields 1 quarter for 60s of cost and profit. The extra corn needed comes "
                  "from a dose on C that costs 66s a quarter, and nothing worse than A is "
                  "farmed. What rent does A pay on its first quarter?",
             "a": ["Nothing, because A is the worst soil", "6s", "66s", "60s"],
             "c": 1,
             "why": "C's dose regulates at 66s, so A's quarter fetches 66s against 60s, a rent of "
                    "6s. Being the worst soil does not exempt it once a dearer dose sets the "
                    "price; 66s and 60s are the price and the cost, not the difference."},
            {"q": "An extra quarter would cost 70s from a dose on B and 75s from a second dose "
                  "on A. Which sets the price, on Marx's reasoning?",
             "a": ["A's dose, because A is the worst soil",
                   "B's dose, because it is cheaper",
                   "The average of the two, 72½s",
                   "Neither; A's first capital still sets it at 60s"],
             "c": 1,
             "why": "The extra quarter is produced where it is cheapest, so B's dose is made and "
                    "regulates at 70s. Marx: if it cost more on B it &ldquo;would naturally be "
                    "produced upon A&rdquo;. A's 60s no longer covers the market's needs."},
            {"q": "What did Engels object to in Marx's figures for this chapter?",
             "a": ["That A can never pay rent",
                   "That B's tenant, who must still pay his old rent, prices his whole product at its average cost, so A's rent is 1/9 pound, not ½",
                   "That the price should be set by A−1 at 4 pounds",
                   "That the profit rate should be 15%, not 20%"],
             "c": 1,
             "why": "Engels kept Marx's conclusion, that A can pay rent, and changed the rule: "
                    "14 pounds over 4½ quarters is 3 1/9 pounds, leaving A 1/9 pound. A−1 is "
                    "dearer than B's dose and is not used, and the rate of profit is not in "
                    "question."},
        ],
        "mistakes": [
            ("Thinking the worst soil can never pay differential rent",
             "In differential rent I the worst soil sets the price, so it has no surplus. But "
             "once a dearer additional dose sets the price, the worst soil's first capital is "
             "no longer the regulator. In the marx preset nothing worse than A is farmed and A "
             "still pays 10s, Marx's ½ pound, because B's extra dose regulates at 70s."),
            ("Assuming the dearest available source regulates",
             "The regulator is the source actually used, which is the cheapest that meets the "
             "demand. In the both preset A's second dose at 75s is on offer and unused; B's at "
             "70s sets the price."),
            ("Treating Marx's ½ pound as settled",
             "Engels printed a correction beside it: on the tenant's average cost, A's rent is "
             "1/9 pound and B's stays 4½. The lab computes Marx's rule; state which rule a "
             "figure belongs to."),
        ],
        "standard": (
            "Finish when you can find the rent the worst soil pays under a dearer dose.",
            "Given the worst soil's yield, the doses on a better soil and the cost of each "
            "possible extra source, compute the regulating price, the rent of the worst "
            "soil's first capital and the other rents, by Marx's rule, and state Engels' "
            "alternative."
        ),
        "note": (
            "The lab values each dose by itself at the regulating price, which is Marx's rule "
            "in this chapter; Engels' correction prices the acre's whole product at its "
            "average cost including the old rent, and the lab does not compute it. Marx's "
            "extra quarter on B is entered as 6/7 of a quarter on a 50s dose to keep the "
            "doses equal; its price per quarter, and so every rent, is his."
        ),
    },
    # ---------------------------------------------------------------- 09
    # Kerr vol. 3, l. 6641-6643 (private property prevents equalisation).
    # Inline: l. 6548 (P+r; will the landlord rent for nothing?), l. 6552
    # (a tax), l. 6578 (monopoly price), l. 6580 (rent the cause of the
    # increase in price), l. 6582-6584 (85c + 15v, 75c + 25v, 120),
    # l. 6566 (a question for statistics), l. 6591 (would disappear), l. 6593
    # (with the progress of civilization),
    # l. 6542 (Ricardo and the colonies).
    {
        "slug": "absolute-ground-rent",
        "title": "Absolute Ground Rent",
        "module": "Chapter 45 · Absolute Ground-Rent",
        "one_line": "Landed property can stop the surplus value of farming from being shared out in the average profit, and the part it keeps is absolute rent, paid even by the worst soil, without any price above value.",
        "summary": (
            "Ricardo's worst soil paid no rent. Marx asks why any landowner would lend land "
            "for nothing, and answers with the gap between value and price of production. "
            "Compute agriculture's value and its price of production when its capital employs "
            "more labour than industry's, the absolute rent that gap allows, the case where "
            "the gap disappears, and a market that will not pay the whole of it."
        ),
        "key": [
            "industry 85c + 15v, farming 75c + 25v",
            "s/v = 100%: values 115 and 125",
            "equalised: price of production 120",
            "absolute rent ≤ 125 − 120 = 5",
            "same composition: no absolute rent",
        ],
        "key_label": "Absolute rent in five lines",
        "concepts_intro": (
            "Chapter 45 adds a second kind of rent to the differential kind. It needs one "
            "assumption from Volume III's Part II, that prices of production differ from "
            "values according to the composition of capital."
        ),
        "concepts": [
            ("Absolute rent",
             "Rent the worst soil pays, not from any difference in fertility, because a "
             "landowner will not let land be farmed for nothing. Marx locates it in the excess "
             "of agriculture's value over its price of production."),
            ("Lower composition",
             "A capital that spends more on wages and less on means of production than the "
             "social average. At the same rate of surplus value it produces more surplus "
             "value than it receives as average profit."),
            ("A barrier to equalisation",
             "Prices of production arise as capital moves between branches until profits are "
             "equal. Landed property stands in the way of that movement into agriculture and "
             "keeps part of farming's surplus value back from the average."),
        ],
        "read_title": "The nature of absolute rent first, then the arithmetic",
        "read_intro": (
            "The passage is Marx's summary near the end of the chapter. The figures he gives "
            "for it come a little before."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 45.</strong> &ldquo;In industry these different "
                  "masses of surplus-value are leveled into an average profit and distributed "
                  "among the individual capitals uniformly and as aliquot parts of the social "
                  "capital. Private property in land prevents such an equalization among "
                  "capitals invested in the soil, whenever production requires real estate, "
                  "either for agriculture or for the extraction of raw materials, and catches a "
                  "portion of the surplus value which would otherwise assist in the formation of "
                  "the average rate of profits.&rdquo;"),
            ("p", "Ricardo's theory says the worst land in use pays no rent. Marx asks a "
                  "landlord's question: why would anyone lend land for nothing? If the price of "
                  "corn just covers a tenant's capital and the average profit on the worst soil, "
                  "&ldquo;will the landlord rent such lands for nothing&rdquo;? &ldquo;By no "
                  "means.&rdquo; The market price must rise a little above the price of "
                  "production, to P + r in Marx's letters, before the land is let. So the worst "
                  "soil pays a rent, and the next question is what it is a share of."),
            ("p", "The obvious answer is that it is a monopoly price, a tax the landlord levies "
                  "on bread. Marx says it need not be, and his reason comes from Average Profit "
                  "and Its Fall. A capital that employs more labour per pound than the average "
                  "produces more surplus value than the average profit it receives; its value is "
                  "above its price of production. If farming is such a capital, corn can sell "
                  "above its price of production and still at or below its value."),
            ("p", "Here are Marx's figures, which the marx preset uses. Non-agricultural capital "
                  "is 85c + 15v; agricultural capital is 75c + 25v; the rate of surplus value is "
                  "100% in both. Industry's product is worth 115, agriculture's 125. Equalise "
                  "the two, each with a capital of 100, and the 40 of surplus value is 20% on "
                  "200: both sell at 120. Agriculture's product sells 5 below its value, "
                  "industry's 5 above. Landed property, by refusing to let land below a rent, "
                  "can hold farming's price up toward its value, and the gap is the room for "
                  "absolute rent. The lab prints agriculture's price of production of £120 and "
                  "an absolute rent of up to £5."),
            ("def", ("Absolute ground rent",
                     "Rent paid even on the worst cultivated soil, which on Marx's account is "
                     "part or all of the excess of agricultural value over price of production, "
                     "kept from the general equalisation of profit by landed property.")),
            ("p", "&ldquo;Up to&rdquo;, because how much of the 5 becomes rent &ldquo;will "
                  "depend wholly upon the relation between supply and demand&rdquo;. The "
                  "market-limited preset sets the highest price the market bears at 122: the "
                  "absolute rent is then up to 2. Either way the corn sells at what Marx still "
                  "calls &ldquo;a monopoly price, not because their price would exceed their "
                  "value, but because their price would be equal to their value, or because their "
                  "price would be lower than their value but higher than their price of "
                  "production&rdquo;. And the causal order is the opposite of the last lessons': "
                  "here &ldquo;the rent is the cause of the increase in the price of the "
                  "product&rdquo;."),
            ("p", "The whole construction hangs on one assumption, and Marx says so twice. "
                  "Whether farming's composition is in fact lower than the average &ldquo;is a "
                  "question which can be decided only by statistics&rdquo;. And if it is not, "
                  "absolute rent in this sense &ldquo;would disappear&rdquo;. The "
                  "average-composition preset gives agriculture industry's 85c + 15v: value and "
                  "price of production are both 115, and the tile reads up to £0. Marx adds that "
                  "the same would follow if farming's composition &ldquo;would gradually become "
                  "the same as that of the average social capital with the progress of "
                  "civilization&rdquo;."),
            ("p", "Ricardo comes in for one more criticism. He set out to study the effect of "
                  "the appropriation of land, Marx says, and then took his examples from "
                  "colonies, where land is not yet appropriated and anyone may farm new land. "
                  "Where land is owned, the owner's power to withhold it is the point. Marx "
                  "notes, citing Fourier, that in every civilised country &ldquo;a comparatively "
                  "considerable portion of the land always remains uncultivated&rdquo;."),
            ("p", "This is the most disputed chapter of the Part. Economists after Marx, "
                  "following Ricardo, mostly hold that the marginal land pays no rent, or only "
                  "the rent its best alternative use would pay, and treat what it does pay as "
                  "reward for scarcity, not as a share of surplus value. Others dispute the "
                  "construction from inside Marx's own terms: it depends on reading values and "
                  "prices of production as Chapter 9 does, inputs at value, which is the "
                  "assumption the transformation debate after Bortkiewicz questions. What the "
                  "chapter itself supplies is the assumption, named, and the case in which it "
                  "fails."),
            ("p", "Absolute and differential rent are, Marx says, &ldquo;the only normal "
                  "ones&rdquo;. The next lesson, “Building Rent, Mining Rent, the Price of "
                  "Land”, carries both off the farm, to building plots and mines, and returns to "
                  "the price of land."),
        ],
        "lab": ("capkit", {
            "mode": "rent",
            "view": "absolute",
            "money_unit": "£",
            "preset": "marx",
            "presets": [
                {"id": "marx", "label": "Marx's figures: industry 85c + 15v, agriculture 75c + 25v, s/v 100%",
                 "agri": {"c": 75, "v": 25}, "industry": {"c": 85, "v": 15}, "s_rate": 1, "expect": {"rtPrice": "£120", "rtAbsolute": "up to £5"}},
                {"id": "average-composition", "label": "Agriculture at industry's composition, 85c + 15v",
                 "agri": {"c": 85, "v": 15}, "industry": {"c": 85, "v": 15}, "s_rate": 1, "expect": {"rtPrice": "£115", "rtAbsolute": "up to £0"}},
                {"id": "market-limited", "label": "Marx's figures; the market bears no more than 122",
                 "agri": {"c": 75, "v": 25}, "industry": {"c": 85, "v": 15}, "s_rate": 1,
                 "market_limit": 122, "expect": {"rtPrice": "£120", "rtAbsolute": "up to £2"}},
            ],
            "panel_title": "Value, price of production and absolute rent",
            "panel_intro": (
                "Agriculture's and industry's capitals go in, with the rate of surplus value. "
                "The lab equalises profit over the two and compares agriculture's price of "
                "production with its value. Choose average-composition: the gap, and the rent, "
                "are gone."
            ),
        }),
        "steps_title": "Computing absolute rent",
        "steps_intro": "Four steps, for one agricultural and one non-agricultural capital.",
        "steps": [
            ("Value each product",
             "Each capital's c + v plus its surplus value, the rate of surplus value times v."),
            ("Equalise the profit",
             "Add the two surplus values and divide by the two capitals for the average rate "
             "of profit."),
            ("Price agriculture's product",
             "Agriculture's capital plus the average profit on it is its price of production."),
            ("Take the difference",
             "Agriculture's value less its price of production is the most absolute rent can "
             "be without a price above value; a lower market limit caps it there."),
        ],
        "worked": {
            "title": "Marx's two capitals",
            "intro": [
                "Industry is 85c + 15v, agriculture 75c + 25v, and the rate of surplus value is "
                "100%. You want agriculture's value, its price of production and the absolute "
                "rent.",
            ],
            "lines": [
                "industry's value:  85 + 15 + 15 = 115",
                "agriculture's value:  75 + 25 + 25 = 125",
                "average profit:  (15 + 25) / 200 = 20%",
                "agriculture's price:  100 + 20 = 120",
                "absolute rent:  at most 125 − 120 = 5",
            ],
            "after": [
                "Give agriculture industry's composition and both values are 115, the price of "
                "production is 115, and absolute rent in this sense disappears.",
            ],
        },
        "quiz_title": "Value, price and absolute rent",
        "quiz": [
            {"q": "Industry is 80c + 20v and agriculture 60c + 40v, with s/v at 100% in both. "
                  "What is the most absolute rent can be without a price above value?",
             "a": ["10", "20", "40", "0"],
             "c": 0,
             "why": "Agriculture's value is 140; the average profit is `60 / 200 = 30%`, so its "
                    "price of production is 130; the gap is 10. Twenty is the difference in v; "
                    "40 is agriculture's whole surplus value."},
            {"q": "According to Marx, when would absolute rent in his sense disappear?",
             "a": ["When the worst soil is improved",
                   "When agriculture's composition of capital reaches or passes the social average",
                   "When the rate of interest falls",
                   "When differential rent rises"],
             "c": 1,
             "why": "Then agriculture's value is no longer above its price of production, and "
                    "Marx says absolute rent &ldquo;would disappear&rdquo;. Improving soils "
                    "changes differential rent, and the rate of interest changes the price of "
                    "land, not rent."},
            {"q": "Marx calls the price of corn under absolute rent a monopoly price. In what "
                  "sense?",
             "a": ["It is above the value of corn",
                   "It is set by the landlords at will",
                   "It is held above the price of production, at or below value, by landed property",
                   "It is a tax levied by the state"],
             "c": 2,
             "why": "Agricultural products are not levelled to their price of production as "
                    "other goods are, and can sell up to their value. Marx distinguishes this "
                    "from an actual monopoly price set by buyers' wants, and from a tax."},
        ],
        "mistakes": [
            ("Thinking absolute rent is a monopoly price the landlord can set at will",
             "If the worst soil pays rent, it looks as if landlords simply add a charge to "
             "bread. On Marx's account the rent is limited from above by the value of the "
             "product: in the marx preset it is at most 5, and in the market-limited preset 2. "
             "Set agriculture at the average composition and there is nothing to take; the "
             "tile reads up to £0. A price fixed only by buyers' eagerness and means, apart from "
             "value and price of production, is what Marx calls an actual monopoly price, a "
             "different case."),
            ("Thinking absolute rent contradicts differential rent",
             "Marx shows the differences are unchanged: if every price rises by the worst "
             "soil's rent r, each better soil's rent still exceeds A's by the same d, 2d, 3d. "
             "Absolute rent adds a constant to the series."),
            ("Treating the lower composition as established",
             "Marx calls it a question for statistics and expects the gap to narrow. The "
             "lesson's figures follow his assumption; they do not show it holds."),
        ],
        "standard": (
            "Finish when you can compute the absolute rent a composition of capital allows.",
            "Given agriculture's and industry's constant and variable capital and the rate of "
            "surplus value, compute agriculture's value, its price of production equalised "
            "with industry, and the absolute rent, with and without a market limit."
        ),
        "note": (
            "The lab equalises two capitals of equal size, as Marx's example assumes; a real "
            "economy would weight them by size. Its values and prices of production are "
            "computed with inputs at value, the reading of Chapter 9 that the transformation "
            "debate questions. Whether agriculture's composition is lower than industry's is "
            "the empirical question Marx leaves to statistics, and the lab does not answer it."
        ),
    },
    # ---------------------------------------------------------------- 10
    # Kerr vol. 3, l. 6651 (the owner's passiveness). Inline: l. 6655
    # (Capps: 300, 400 or 500), l. 6659 (99 years), l. 6663 (Scottish coal
    # mines), l. 6665-6667 (vineyard; monopoly price creates the rent),
    # l. 6667-6669 (good fathers of families), l. 6675 (fall of the rate of
    # interest), l. 6701-6703 (60s to two quarters at 40s), l. 6709 (Soho).
    {
        "slug": "building-rent-mining-rent-land-price",
        "title": "Building Rent, Mining Rent, the Price of Land",
        "module": "Chapter 46 · Building Lot Rent. Mining Rent. Price of Land",
        "one_line": "A building plot's rent rises as the town grows around it, a mine's follows the same laws as a farm's, and the price of land can rise for reasons that have nothing to do with the land.",
        "summary": (
            "Chapter 46 carries rent off the farm. Compute a building plot's price as a town "
            "reaches it and its rent triples, the rise in a speculator's ground rent from "
            "Marx's London witness, and a Scottish mine that pays no rent and so has no price; "
            "then sort the reasons a price of land can rise into those that touch the rent "
            "and those that do not."
        ),
        "key": [
            "price of land = rent / rate of interest",
            "plot: £50 → £150 a year as the town grows",
            "at 5%: £1,000 → £3,000",
            "no rent, no price: the Scottish mine",
            "price may rise with rent unchanged",
        ],
        "key_label": "The chapter in five lines",
        "concepts_intro": (
            "The chapter is short and mixed: building rent, mining rent, monopoly price, and "
            "the ways the price of land moves. It returns to the first lesson's rule with what "
            "the Part has added since."
        ),
        "concepts": [
            ("Building rent",
             "The rent of land as a site. Location dominates it, and it rises with the town "
             "around it: with population, and with the railways, docks and factories built "
             "nearby."),
            ("Monopoly price",
             "A price set only by buyers' eagerness and means, like a rare wine's. Here the "
             "monopoly price creates the rent; in absolute rent, by contrast, the rent "
             "creates the price."),
            ("Movements of the price of land",
             "The price of land can rise because the rate of interest falls, because interest "
             "on capital sunk in it rises, or because rent rises; and rent can rise with the "
             "price of corn steady or falling."),
        ],
        "read_title": "The passage first, then the town and the mine",
        "read_intro": (
            "The passage is Marx's description of what distinguishes building and mining "
            "rent. Its phrase about the owner is the one most often quoted from the Part."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 46.</strong> &ldquo;This form of rent is "
                  "distinguished, first, by the overwhelming influence exerted by location upon "
                  "differential rent (an influence which is very considerable in vineyards and in "
                  "building lots of large cities); secondly, by the palpable passiveness of the "
                  "owner, whose sole activity consists (especially in mines) in exploiting the "
                  "progress of social development, toward which he contributes nothing and for "
                  "which he risks nothing, unlike the industrial capitalist&rdquo;."),
            ("p", "If you have watched a field at the edge of a town become a street of houses, "
                  "you have watched this chapter. The field's owner did nothing, and the plot is "
                  "suddenly worth many times what it was. Marx's account uses the first lesson's "
                  "rule and the Part's differential rent: a building plot's advantage is its "
                  "location, and the town confers it. The lab's two town presets run an "
                  "illustrative plot. At £50 a year and 5% it is priced at £1,000; when the town "
                  "reaches it and its rent is £150, its price is £3,000. Not a brick on it is the "
                  "landowner's."),
            ("p", "Marx's witness is a London builder, Edward Capps, examined by the Select "
                  "Committee on Bank Acts. A builder, Capps said, makes little out of the houses; "
                  "he takes land at £300 a year, builds the right class of houses, and may make "
                  "&ldquo;400 or 500 pounds sterling&rdquo; a year out of it, so that his profit lies "
                  "in &ldquo;the increased ground-rent&rdquo;. The capps preset takes the lower "
                  "figure, £400: at 5% the ground goes from £6,000 to £8,000. And at the end of "
                  "the usual lease, &ldquo;at the end of 99 years&rdquo;, the land, the "
                  "buildings and the raised rent go back to the original landowner."),
            ("p", "Mining rent, Marx says, is &ldquo;determined in the same way as the "
                  "agricultural rent&rdquo;: the best mines pay differential rent against the "
                  "worst. His example of the worst comes from Adam Smith. Some Scottish coal "
                  "mines yield only enough to replace the capital with the ordinary profit, so "
                  "they can be worked only by their owners: &ldquo;The landowner does not permit "
                  "anybody to work them without the payment of rent, but no one can pay any rent "
                  "for them.&rdquo; The mine preset gives such a mine a rent of nothing, and the "
                  "lab prices it at £0. A price of land is capitalised rent; where there is no "
                  "rent there is nothing to capitalise."),
            ("p", "Then monopoly price. A vineyard whose wine can be made only in small "
                  "quantities sells at a price set by the &ldquo;wealth and the fine appetite of "
                  "the rich wine drinkers&rdquo;, and the surplus becomes the vineyard owner's "
                  "rent: &ldquo;Here, then, the monopoly price creates the rent.&rdquo; Corn "
                  "would be the opposite case, where rent created a monopoly price, if landed "
                  "property held its price above its value. Building rent, Marx says, often rests "
                  "on monopoly price, and he adds that poverty is a more lucrative source for house rent "
                  "&ldquo;than the mines of Potosi ever were for Spain&rdquo;."),
            ("def", ("Building rent",
                     "The rent of land as a site for houses, works or docks, ruled above all by "
                     "location, which the growth of the surrounding town confers, and "
                     "capitalised like any rent into a price.")),
            ("p", "The second half of the chapter sorts the movements of the price of land, and "
                  "it is a useful list to keep. The price can rise without the rent: when the "
                  "rate of interest falls, as in the first lesson's £4,000 becoming £5,000, or "
                  "when interest on capital sunk in the land rises. It can rise because the rent "
                  "rises, and the rent can rise with the price of corn rising, steady, or even "
                  "falling. Marx's last case: an acre that yielded one quarter at 60s yields two "
                  "at 40s, so its product is worth 80s, a third more, though the quarter is a "
                  "third cheaper. So it &ldquo;will not do to conclude offhand that a rise in the "
                  "price of land signifies also a rise of rent&rdquo;."),
            ("p", "The chapter's most remembered sentences are not arithmetic. A title to land, "
                  "Marx says, is transferred by sale, never created by it; and from the point of "
                  "view of a higher form of society, private ownership of the globe will seem as "
                  "absurd as ownership of one person by another. &ldquo;Even a whole society, a "
                  "nation, or even all societies together, are not the owners of the globe. They "
                  "are only its possessors, its users, and they have to hand it down to the "
                  "coming generations in an improved condition, like good fathers of "
                  "families.&rdquo;"),
            ("p", "The rise in site values was the theme of Henry George's <em>Progress and "
                  "Poverty</em>, published in 1879 and read far more widely than Capital in its "
                  "day. George held that the rent of land, created by the community, should be "
                  "taken by a single tax, leaving labour and capital untaxed. Economists since "
                  "have argued about land value taxes on George's terms: rent rewards no effort, "
                  "so taxing it distorts nothing. What this chapter bears on is narrower: the "
                  "rent of a site is fixed by the development around it, and its price by that "
                  "rent and the rate of interest."),
            ("p", "Every rent in this Part has been a surplus over profit in a world of "
                  "capitalist tenants. The last lesson, “Genesis of Capitalist Ground Rent”, "
                  "goes back to rent before there was any profit, when it was the whole of the "
                  "surplus."),
        ],
        "lab": ("capkit", {
            "mode": "rent",
            "view": "price",
            "money_unit": "£",
            "preset": "town-before",
            "presets": [
                {"id": "town-before", "label": "A plot at the town's edge: £50 a year at 5%",
                 "rent": 50, "interest_rate": "1/20", "expect": {"rtPrice": "£1,000", "rtTrueRent": "£50"}},
                {"id": "town-grows", "label": "The town reaches it: £150 a year at 5%",
                 "rent": 150, "interest_rate": "1/20", "expect": {"rtPrice": "£3,000", "rtTrueRent": "£150"}},
                {"id": "capps", "label": "Capps's ground: £300 a year raised to £400, at 5%",
                 "rent": 400, "interest_rate": "1/20", "expect": {"rtPrice": "£8,000", "rtTrueRent": "£400"}},
                {"id": "mine", "label": "Smith's Scottish mine: no rent at all",
                 "rent": 0, "interest_rate": "1/20", "expect": {"rtPrice": "£0", "rtTrueRent": "£0"}},
            ],
            "panel_title": "What a site is worth",
            "panel_intro": (
                "The yearly ground rent and the rate of interest go in; the price is the one "
                "divided by the other. Step from town-before to town-grows: the site's price "
                "triples because its rent did, and nothing was built on it by its owner."
            ),
        }),
        "steps_title": "Reading a change in the price of land",
        "steps_intro": "Four steps, for any rise in what a piece of land sells for.",
        "steps": [
            ("Capitalise before and after",
             "Divide each year's rent by the rate of interest in force at the time."),
            ("Separate the rate",
             "Recompute the new price at the old rate of interest. Whatever change remains is "
             "due to the rent; the rest is due to the rate."),
            ("Separate the improvements",
             "Of a rise in the payment, take out the interest on capital sunk in the land by "
             "anyone. What is left is a rise in ground rent proper."),
            ("Name the source",
             "Say what raised the rent: the town or market around the land, more capital on "
             "it, a dearer product, or a monopoly price."),
        ],
        "worked": {
            "title": "A plot the town reaches",
            "intro": [
                "A plot rents for £50 a year at the edge of a town, and for £150 once the "
                "streets reach it. The rate of interest is 5%. You want the price before and "
                "after, and what the price would be if the rate then fell to 4%.",
            ],
            "lines": [
                "before:  £50 / (1/20) = £1,000",
                "after:  £150 / (1/20) = £3,000",
                "after, at 4%:  £150 / (1/25) = £3,750",
            ],
            "after": [
                "The first rise came from the rent, which the town created; the last from the "
                "rate of interest alone.",
            ],
        },
        "quiz_title": "Sites, mines and land prices",
        "quiz": [
            {"q": "A site's ground rent rises from £80 to £200 a year as a railway station is "
                  "built beside it, with interest at 5%. By how much does its price rise?",
             "a": ["£2,400", "£120", "£4,000", "£1,600"],
             "c": 0,
             "why": "The price goes from `80 / (1/20) = 1,600` to `200 / (1/20) = 4,000`, a "
                    "rise of £2,400. £120 is the rise in rent, £4,000 the new price and £1,600 "
                    "the old one."},
            {"q": "Why can Smith's Scottish mine be worked only by its owner?",
             "a": ["Because the law forbids leasing mines",
                   "Because it covers only its capital and the ordinary profit, leaving nothing for rent",
                   "Because mining rent is a monopoly price",
                   "Because its coal is worth more than any tenant could pay"],
             "c": 1,
             "why": "No tenant can pay rent from it, and the owner will let no one work it "
                    "without rent, so only the owner, as his own capitalist, works it. With no "
                    "rent, it has no price as land."},
            {"q": "The price of a piece of land rises while its rent is unchanged. Which of "
                  "these could explain it, on the chapter's account?",
             "a": ["A rise in the price of corn",
                   "A fall in the rate of interest",
                   "A rise in differential rent",
                   "The town growing around it"],
             "c": 1,
             "why": "Marx's first case: a fall in the rate of interest capitalises the same rent "
                    "into a higher price. The other three each work by raising the rent, which "
                    "the question holds fixed."},
        ],
        "mistakes": [
            ("Thinking a rising land price reflects improvements made by the owner",
             "A dearer plot looks like a better plot, and better looks like someone's work. In "
             "the town presets the rent goes from £50 to £150 and the price from £1,000 to "
             "£3,000 because the town reached the plot; the owner, in Marx's phrase, "
             "&ldquo;contributes nothing&rdquo; and &ldquo;risks nothing&rdquo;. Where an owner "
             "has improved the land, the interest on that capital is a separate part of the "
             "payment, as the first lesson's improvements preset shows."),
            ("Thinking a rise in land prices means a rise in rent",
             "A fall in the rate of interest raises the price with the rent unchanged. Marx "
             "warns against concluding &ldquo;offhand&rdquo; that the one means the other."),
            ("Thinking all rent on sites and mines is monopoly price",
             "Most of it follows the laws of differential rent, by location and by the "
             "richness of the deposit. Monopoly price proper, set by buyers' wants, is the "
             "exception, like the rare vineyard's."),
        ],
        "standard": (
            "Finish when you can price a site and say why its price changed.",
            "Given a site's ground rent before and after a change and the rate of interest, "
            "compute its price before and after, and divide the change into the part due to "
            "the rent and the part due to the rate of interest."
        ),
        "note": (
            "The town presets' £50 and £150 are illustrative; Capps's £300 and £400 are his "
            "figures as Marx quotes them, and the 5% is the rate of the first lesson. The lab "
            "capitalises a perpetual rent; a 99-year building lease, which ends in the "
            "landowner's favour, would be priced lower by the lessee."
        ),
    },
    # ---------------------------------------------------------------- 11
    # Kerr vol. 3, l. 6769-6771 (labour rent: separated by space and time).
    # Inline: l. 6759 (rent and surplus-value identical), l. 6779 (two days
    # per week), l. 6785 (rent in kind; no longer separated), l. 6795-6797
    # (money rent), l. 6811 (rent a surplus over profit), l. 6721 (the
    # difficulty), l. 6727 (the physiocrats).
    {
        "slug": "genesis-of-capitalist-ground-rent",
        "title": "Genesis of Capitalist Ground Rent",
        "module": "Chapter 47 · Genesis of Capitalist Ground-Rent",
        "one_line": "Before capitalism rent was the whole of the surplus, and in labour rent it was visible as days worked on the lord's field; the capitalist tenant turned it into a surplus over profit.",
        "summary": (
            "The last chapter of the Part runs rent back through its history: labour rent, "
            "rent in kind, money rent, share-cropping and peasant property, to the capitalist "
            "tenant. Compute the rate of surplus labour in labour rent from days on the lord's "
            "land and days on one's own, compare it with the rate on a wage-worker's day, and "
            "see what changes when the rent is paid in produce and then in money."
        ),
        "key": [
            "labour rent: rent = surplus labour",
            "rate = lord's days / own days",
            "2 days in 6 for the lord: 50%",
            "rent in kind, money rent: same substance",
            "capitalist rent: a surplus over profit",
        ],
        "key_label": "The genesis in five lines",
        "concepts_intro": (
            "Chapter 47 explains why rent was a puzzle for economists of Marx's time and not "
            "for earlier ones, by following the forms rent took before profit existed."
        ),
        "concepts": [
            ("Labour rent",
             "The direct producer works some days on his own holding with his own tools and "
             "the others on the lord's land, unpaid. Rent and surplus labour are the same "
             "thing, and they are visible."),
            ("Rent in kind and money rent",
             "The producer works all week on his own holding and hands over part of the "
             "product, or later its price in money. The surplus is the same in substance; it "
             "is no longer separated from his own labour in time and place."),
            ("Capitalist ground rent",
             "Once a capitalist tenant stands between landlord and labourer, profit is the "
             "normal form of surplus value and rent is only the surplus over the average "
             "profit, which is why explaining it needed the whole of Part VI."),
        ],
        "read_title": "Labour rent first, then the forms that followed it",
        "read_intro": (
            "The passage is from the section on labour rent, the simplest form, and says what "
            "makes it simple."
        ),
        "body": [
            ("p", "<strong>Volume III, Chapter 47, §2.</strong> &ldquo;Furthermore, the identity "
                  "of surplus-value with unpaid labor of others does not need to be demonstrated "
                  "by any analysis in this case, because it still exists in its visible, palpable "
                  "form, for the labor of the direct producer for himself is still separated by "
                  "space and time from his labor for the landlord, and this last labor appears "
                  "clearly in the brutal form of forced labor for another.&rdquo;"),
            ("p", "Begin with the puzzle the chapter opens on. For the economists of Marx's day "
                  "the difficulty was never that farming yields a surplus; that was explained "
                  "with all surplus value. It was explaining &ldquo;the excess of agricultural "
                  "profit over the average profit&rdquo;. Earlier writers did not have that "
                  "problem. For Petty and Cantillon rent was the normal form of surplus and "
                  "profit not yet a category of its own, still mixed up with wages; for the "
                  "physiocrats, the French economists around "
                  "Quesnay, agriculture was the only productive labour and rent the only "
                  "surplus. To see why, Marx goes back to rent before capital."),
            ("p", "In labour rent the producer has his own holding, plough and cattle, and works "
                  "part of the week on it and the rest on the lord's estate without pay. There "
                  "is nothing to analyse: rent and surplus value are &ldquo;identical&rdquo;, and "
                  "the line between them is drawn on the ground and in the calendar. Marx's own "
                  "example is forced labour that &ldquo;originally amounted to two days per "
                  "week&rdquo;, fixed by custom or law. In a six-day week that is the two-days "
                  "preset: 2 days of surplus labour against 4 of necessary labour, a rate of 50%. "
                  "The three-three preset gives the lord three days and the producer three, "
                  "100%; the four-two preset, four days to two, 200%."),
            ("p", "Marx draws a consequence from the two days being fixed. The days a peasant "
                  "works for himself are his to make more productive; better methods, new "
                  "wants and a market for his surplus all spur him on, and the custom that "
                  "fixes the lord's share protects his. So labour rent leaves open what Marx "
                  "calls &ldquo;a certain economic development&rdquo; on the serf's side, "
                  "depending on circumstances."),
            ("p", "Rent in kind changes the form and not the substance. The producer now works "
                  "his whole time on his own holding and hands over a share of the product. "
                  "&ldquo;The labor of the producer for himself and his labor for the landlord "
                  "are no longer palpably separated by time and space.&rdquo; Money rent changes "
                  "it again: he pays the price of the share, so he must sell, and his economy is "
                  "drawn into the market. In each the surplus is still the rent, and the lab's "
                  "rate is unchanged if the share of produce or money handed over is the share "
                  "of the week's labour it costs: two days' product out of six is still 50%."),
            ("def", ("Labour rent",
                     "Rent paid as days of unpaid work on the landowner's land by a producer "
                     "who works the rest of his time on his own holding. Its rate of surplus "
                     "labour is the lord's days over the producer's own.")),
            ("p", "The chapter's last stage is the one the Part began with. Money rent dissolves "
                  "the old relation: some tributary peasants buy themselves free, others hire "
                  "day-labourers and grow into capitalist tenants, and money from the towns "
                  "leases land to farm for profit. Once the capitalist tenant stands between "
                  "landlord and labourer, the surplus is extracted by him as profit, and rent "
                  "becomes &ldquo;a mere surplus of this surplus labor over that portion of it, "
                  "which is appropriated by the exploiting capitalist in the form of "
                  "profit&rdquo;. Profit, instead of rent, &ldquo;has now become the normal form "
                  "of surplus-value&rdquo;."),
            ("p", "That is why the comparison in the lab matters to Marx. A wage-worker of "
                  "Volume I who works 12 hours, 6 of them replacing the value of his wage, gives "
                  "the same 100% as the three-three preset's peasant. The difference is that "
                  "the peasant can count his days on the lord's field, while in the factory "
                  "nothing marks which hours are which; the wage appears to pay for all of them. "
                  "On the chapter's accounting the two are the same rate in different forms."),
            ("p", "That accounting is exactly what most economists after Marx reject. On the "
                  "marginal-productivity theory that John Bates Clark set out in 1899, a "
                  "competitive wage pays the worker what the last hour of his labour adds to "
                  "output, so no hour is unpaid; the corvée peasant's lost days are a coercion a "
                  "free labour market does not have. What this chapter bears on is the "
                  "definition both accounts start from: Marx counts as unpaid the labour beyond "
                  "what replaces the value of labour-power, and on that definition the "
                  "peasant's and the wage-worker's rates can be compared at all."),
            ("p", "Part VI ends here, with rent traced from the corvée to the capitalist "
                  "tenant. The next course, Revenues and Their Sources, reads Part VII, where "
                  "wages, profit and rent are set beside one another as if each came from a "
                  "source of its own."),
        ],
        "lab": ("capkit", {
            "mode": "workday",
            "view": "corvee",
            "money_unit": "hours",
            "preset": "two-days",
            "presets": [
                {"id": "two-days", "label": "Marx's figures: two days a week for the lord, four for oneself",
                 "lord_days": 2, "own_days": 4, "expect": {"wdSurplus": "2 days", "wdRate": "1/2 = 50%"}},
                {"id": "three-three", "label": "Three days for the lord, three for oneself",
                 "lord_days": 3, "own_days": 3, "expect": {"wdSurplus": "3 days", "wdRate": "1 = 100%"}},
                {"id": "four-two", "label": "Four days for the lord, two for oneself",
                 "lord_days": 4, "own_days": 2, "expect": {"wdSurplus": "4 days", "wdRate": "2 = 200%"}},
            ],
            "panel_title": "The week of a peasant owing labour rent",
            "panel_intro": (
                "Days on the lord's land and days on one's own go in; the bar shows the week "
                "split, and the tiles give the surplus labour and its rate. Compare "
                "three-three with a wage-worker's 6 hours of 12: the same rate, visible here "
                "and not there."
            ),
        }),
        "steps_title": "Reading the rate of labour rent",
        "steps_intro": "Four steps, for labour rent and the forms that follow it.",
        "steps": [
            ("Count the days",
             "Separate the days worked on the landowner's land from the days worked on the "
             "producer's own holding."),
            ("Compute the rate",
             "Divide the lord's days by the producer's own: surplus labour over necessary "
             "labour."),
            ("Translate the form",
             "For rent in kind or money rent, find the share of the week's labour the product "
             "or money handed over costs, and compute the same rate from it."),
            ("Compare with wages",
             "Set the rate beside a wage-worker's, surplus hours over the hours that replace "
             "the wage. Equal rates are the same exploitation on the chapter's definitions, in "
             "a different form."),
        ],
        "worked": {
            "title": "Marx's two days a week",
            "intro": [
                "A peasant owes the lord two days' work a week and works four on his own "
                "holding. You want the rate of surplus labour, and the rent in kind that would "
                "leave it the same.",
            ],
            "lines": [
                "rate:  2 / 4 = 1/2 = 50%",
                "share of the week to the lord:  2 / 6 = 1/3",
                "rent in kind at the same rate:  1/3 of the product",
            ],
            "after": [
                "Three days for the lord and three for himself is 100%, the rate of a "
                "wage-worker in Volume I who works 12 hours and replaces his wage in 6.",
            ],
        },
        "quiz_title": "Labour rent and its successors",
        "quiz": [
            {"q": "A peasant works 5 days a week on his own holding and 1 on the lord's. What "
                  "is the rate of surplus labour?",
             "a": ["20%", "1/6", "500%", "100%"],
             "c": 0,
             "why": "Surplus over necessary labour is `1 / 5 = 20%`. A sixth is the lord's share "
                    "of the whole week, not the rate; 500% inverts it."},
            {"q": "What does rent in kind change compared with labour rent, on Marx's account?",
             "a": ["It abolishes surplus labour",
                   "The producer works all week on his own holding and the surplus is no longer separated from his own labour in time and place",
                   "It makes rent a surplus over profit",
                   "It requires a capitalist tenant"],
             "c": 1,
             "why": "Marx: the two labours &ldquo;are no longer palpably separated by time and "
                    "space&rdquo;, but the rent is still the whole surplus. Rent becomes a "
                    "surplus over profit only with the capitalist tenant."},
            {"q": "On the chapter's accounting, how does a wage-worker who works 12 hours and "
                  "replaces his wage in 6 compare with a peasant giving 3 days of 6 to the lord?",
             "a": ["The wage-worker gives no unpaid labour",
                   "The peasant's rate is higher, because his labour is forced",
                   "The rate is the same, 100%; only the peasant's is visible",
                   "They cannot be compared, because one is paid in money"],
             "c": 2,
             "why": "Both work as much again for another as for themselves. The chapter's point "
                    "is that labour rent shows it &ldquo;in its visible, palpable form&rdquo; "
                    "and the wage does not. The first option is the reading the lesson's "
                    "mistakes take up."},
        ],
        "mistakes": [
            ("Thinking the wage-worker, unlike the serf, gives no unpaid labour",
             "The serf plainly works for nothing on the lord's days; the wage-worker is paid for "
             "every hour he is at work. On Marx's definitions the comparison runs the other "
             "way: three days for the lord in six is 100%, and so is a 12-hour day in which "
             "6 hours replace the wage. The wage hides the division the corvée shows. The "
             "marginal-productivity account rejects that definition, and the lesson says so; "
             "the arithmetic is the same either way."),
            ("Thinking rent in kind or money rent is a smaller exploitation than labour rent",
             "The form changes, and the producer gains room to arrange his own time; but the "
             "substance is still the surplus handed over. Two days' product in six is the same "
             "50% as two days' work."),
            ("Reading pre-capitalist rent as a surplus over profit",
             "In labour rent, rent in kind and money rent, rent is the whole surplus and "
             "profit, if any, grows up behind it. Only with the capitalist tenant does rent "
             "become the excess over the average profit that the rest of Part VI explains."),
        ],
        "standard": (
            "Finish when you can compute the rate of labour rent and compare it with a wage.",
            "Given the days worked on the landowner's land and on the producer's own, compute "
            "the rate of surplus labour, the share of product that would leave it unchanged "
            "as rent in kind, and compare it with a wage-worker's rate."
        ),
        "note": (
            "The lab counts days and divides; it cannot say that a corvée day and a factory "
            "hour are the same kind of thing, which is the definition the comparison rests "
            "on. Marx's two days a week are his; the three-day and four-day weeks are "
            "illustrative, and the history in the chapter is told without figures."
        ),
    },
]
