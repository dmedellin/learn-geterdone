"""Accumulation and the Employments of Capital, lessons 1-5 -- Book II, Chapters 3-5.

Every quotation is copied from /mnt/project-files/wealth-texts/wealth-of-nations-psu.txt
(the Electronic Classics Series edition, Pennsylvania State University, 2005);
the line numbers in the comments are that file's. Chapter 3 is read in two lessons,
productive labour and then parsimony; Chapter 5 in two, the four employments and then
the three branches of wholesale trade.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # PSU text l. 10768-10998 (Book II, Chapter 3, first part). l. 10771-10794
    # (the manufacturer and the menial servant); l. 10795-10825 (the sovereign,
    # churchmen, players; the produce); l. 10826-10875 (capital and revenue);
    # l. 10876-10997 (the proportion, towns); l. 10998-11003 (capital and industry).
    {
        "slug": "productive-and-unproductive-labour",
        "title": "Productive and Unproductive Labour",
        "module": "Book II, Chapter 3, first part · Of the Accumulation of Capital, or of Productive and Unproductive Labour",
        "one_line": "A manufacturer's workman restores his wages with a profit in the thing he makes; a menial servant's work perishes as it is done, so the first is maintained by capital and the second by revenue.",
        "summary": (
            "Smith divides labour into the sort that adds to the value of its subject "
            "and the sort that does not, and puts the sovereign, the army, churchmen, "
            "lawyers and players with the servants. Split a year's produce into a part "
            "that replaces capital and a part that is revenue, then compute a capital "
            "when its owner spends the revenue on servants, saves half of it, or saves "
            "all of it."
        ),
        "key": [
            "productive labour fixes itself in a thing",
            "capital replaces and employs productive hands",
            "revenue may keep productive or idle hands",
            "revenue = capital × return",
            "spent on servants: capital stays where it was",
        ],
        "key_label": "Productive labour in five lines",
        "concepts_intro": (
            "Chapter 3 opens with a distinction that the rest of Book II leans on. It has "
            "three parts: the test, the two funds and the proportion between them."
        ),
        "concepts": [
            ("The test",
             "Labour is productive if it adds to the value of its subject and fixes "
             "itself in something vendible that outlasts the labour, so that its "
             "price can later set an equal quantity of labour to work. A servant's "
             "services perish at the moment they are given."),
            ("Capital and revenue",
             "A year's produce divides in two. One part replaces capital and pays "
             "productive hands only. The other is revenue, as profit or rent, and its "
             "owner may keep either productive or unproductive hands on it."),
            ("The proportion decides",
             "Where capital is large against revenue, industry prevails; where revenue "
             "is large against capital, idleness. Smith reads the character of "
             "towns and of ages from this proportion."),
        ],
        "read_title": "The servant and the manufacturer, then the two funds",
        "read_intro": (
            "The chapter opens on a distinction and a comparison. Smith is careful to "
            "say the distinction is not a judgement of worth."
        ),
        "body": [
            ("p", "<strong>Book II, Chapter 3.</strong> There is one sort of labour &ldquo;which "
                  "adds to the value of the subject upon which it is bestowed; there "
                  "is another which has no such effect. The former as it produces a value, "
                  "may be called productive, the latter, unproductive labour.&rdquo;"),
            ("p", "The first example is a workman and a servant. The labour of a "
                  "manufacturer &ldquo;adds generally to the value of the materials which "
                  "he works upon, that of his own maintenance, and of his master's "
                  "profit&rdquo;. The master advances his wages, but the master is not out "
                  "of pocket, since the wages are restored, with a profit, in the improved "
                  "value of the thing. &ldquo;But the maintenance of a menial servant never "
                  "is restored.&rdquo; Hence the sentence people remember: a man grows "
                  "rich by employing a multitude of manufacturers, and poor by keeping "
                  "a multitude of menial servants."),
            ("p", "Smith is not saying the servant's work is worthless. &ldquo;The labour "
                  "of the latter, however, has its value, and deserves its reward as well "
                  "as that of the former.&rdquo; The difference is in what is left. The "
                  "manufacturer's labour &ldquo;fixes and realizes itself in some "
                  "particular subject or vendible commodity&rdquo;. It is &ldquo;as it "
                  "were, a certain quantity of labour stocked and stored up, to be "
                  "employed, if necessary, upon some other occasion&rdquo;, because the "
                  "price of the commodity can later buy an equal quantity of labour. The "
                  "servant's services &ldquo;generally perish in the very instant of "
                  "their performance&rdquo;."),
            ("p", "Then he makes the list uncomfortable. &ldquo;The sovereign, for example, "
                  "with all the officers both of justice and war who serve under him, the "
                  "whole army and navy, are unproductive labourers. They are the servants "
                  "of the public, and are maintained by a part of the annual produce of the "
                  "industry of other people.&rdquo; &ldquo;Their service, how honourable, "
                  "how useful, or how necessary soever, produces nothing for which an "
                  "equal quantity of service can afterwards be procured.&rdquo; And with "
                  "them, &ldquo;some both of the gravest and most important, and some of "
                  "the most frivolous professions; churchmen, lawyers, physicians, men of "
                  "letters of all kinds; players, buffoons, musicians, opera-singers, "
                  "opera-dancers, etc.&rdquo;. What joins the judge and the buffoon is that "
                  "the work of each &ldquo;perishes in the very instant of its "
                  "production&rdquo;. The test is about whether something remains to be "
                  "exchanged later, and Smith adds that the noblest and the meanest of "
                  "them have their value &ldquo;regulated by the very same "
                  "principles&rdquo; as any other labour."),
            ("p", "Now the two funds, and the arithmetic. All hands are maintained out of "
                  "the same annual produce, which has limits. When it comes from the ground "
                  "or from the hands of the labourers it divides into two. One part "
                  "replaces a capital. &ldquo;to maintain any but productive hands. It pays "
                  "the wages of productive labour only&rdquo;, and the owner expects it back "
                  "with a profit. The other part is a revenue to someone, as profit or "
                  "as rent. Smith is firm that the capital part &ldquo;never is "
                  "immediately employed&rdquo; to maintain unproductive hands; "
                  "it is only the revenue, and what the workmen have spare from their "
                  "wages, that is spent that way. &ldquo;Unproductive labourers, and those "
                  "who do not labour at all, are all maintained by revenue&rdquo;."),
            ("p", "A man who owns a capital may therefore use what it earns in two ways. "
                  "Put numbers on it, written for this lesson. A capital of £1,000 returns "
                  "ten per cent a year over and above replacing itself, so its revenue is "
                  "£100. If a year's keep of one productive hand is £25, the capital "
                  "maintains 40 of them. If the owner spends the whole £100 on servants, "
                  "the capital is £1,000 next year and the year after, and still maintains "
                  "40. If he saves half, the capital becomes £1,050 and then £1,102.50, and "
                  "maintains 42 and then 44.1. If he saves it all, £1,100 and then £1,210, "
                  "and 44 and then 48.4. The three presets run these over two years. The "
                  "servants are fed in the first case from the £100, which is a revenue; "
                  "nothing in the sum says they are idle or unworthy, only that "
                  "what feeds them is not returned."),
            ("p", "Smith draws a conclusion about character from the proportion between the "
                  "two funds, and it is the part of the chapter most open to argument. "
                  "&ldquo;The proportion between capital and revenue, therefore, seems "
                  "everywhere to regulate the proportion between industry and "
                  "idleness.&rdquo; &ldquo;Wherever capital predominates, industry "
                  "prevails; wherever revenue, idleness.&rdquo; In towns where the "
                  "lower ranks &ldquo;are chiefly maintained by the employment of "
                  "capital, they are in general industrious, sober, and thriving&rdquo;, "
                  "like Glasgow and the Dutch towns; where they live on the spending of "
                  "a court or of courts of justice they are &ldquo;in general idle, "
                  "dissolute, and poor&rdquo;, as in his picture of Versailles and the "
                  "parliament towns of France. He puts the point as a proverb: &ldquo;It "
                  "is better, says the proverb, to play for nothing, than to work for "
                  "nothing.&rdquo; Our ancestors, he says, were idle &ldquo;for want of a "
                  "sufficient encouragement to industry&rdquo;, because the funds for "
                  "industry were small against the funds for idleness."),
            ("p", "Smith adds that the sense is not the only one in use. A note at the "
                  "chapter's head says that &ldquo;Some French authors of great learning "
                  "and ingenuity have used those words in a different sense&rdquo;, and "
                  "that in the last chapter of the fourth book he will try to show their "
                  "sense an improper one. Those authors are the Physiocrats, for whom "
                  "only agriculture was productive; the note is kept for Book IV, and this "
                  "Subject reaches it in a later course."),
            ("p", "Three later objections need stating, because the distinction has had "
                  "more argument than almost any other in the book. Jean-Baptiste Say, "
                  "whose <em>Treatise</em> appeared in 1803, held that a physician's or a "
                  "teacher's service is a product like any other, an immaterial one, "
                  "consumed as it is made, and that a definition that excludes it "
                  "mistakes the form of the thing for its usefulness. Modern accounts of "
                  "national output count services as output for the same reason. Marx "
                  "kept Smith's word and changed its test, and the sausage-factory worker "
                  "and the private tutor in Capital's lesson <em>Absolute and Relative "
                  "Surplus Value</em> are productive or not according to whether they "
                  "produce surplus value for a capitalist; that lesson is the place for "
                  "his reasons. And a defender of Smith can say that his question was "
                  "narrower than the one it is accused of answering: it asks what leaves "
                  "a fund behind for next year, which is the question of accumulation, "
                  "and not what is worth doing."),
            ("p", "The next lesson, <em>Parsimony and the Prodigal</em>, follows the "
                  "other half of Chapter 3: how a capital grows when its owner saves, and "
                  "what happens to one whose owner spends it."),
        ],
        "lab": ("wonkit", {
            "mode": "stock",
            "view": "accumulate",
            "money_unit": "£",
            "preset": "all-spent",
            "presets": [
                {"id": "all-spent", "label": "The owner spends all his revenue on servants, written for this lesson",
                 "capital": 1000, "return": 10, "saved": 0, "years": 2, "wage": 25, "expect": {"wstFirst": "revenue £100: £0 added to the capital, £100 spent", "wstRate": "0% a year", "wstAfter": "£1,000 after 2 years", "wstChange": "0%", "wstLabour": "40 → 40 workers", "wstSecond": "no second saving given"}},
                {"id": "half-saved", "label": "He saves half of it, written for this lesson",
                 "capital": 1000, "return": 10, "saved": 50, "years": 2, "wage": 25, "expect": {"wstFirst": "revenue £100: £50 added to the capital, £50 spent", "wstRate": "+5% a year", "wstAfter": "£1,102.5 after 2 years", "wstChange": "+10.25%", "wstLabour": "40 → 44.1 workers", "wstSecond": "no second saving given"}},
                {"id": "all-saved", "label": "He saves all of it, written for this lesson",
                 "capital": 1000, "return": 10, "saved": 100, "years": 2, "wage": 25, "expect": {"wstFirst": "revenue £100: £100 added to the capital, £0 spent", "wstRate": "+10% a year", "wstAfter": "£1,210 after 2 years", "wstChange": "+21%", "wstLabour": "40 → 48.4 workers", "wstSecond": "no second saving given"}},
            ],
            "panel_title": "A capital and its revenue, two years on",
            "panel_intro": (
                "A capital returns a stated share of itself each year as revenue. The lab "
                "adds the share of that revenue that is saved to the capital, year by "
                "year, and divides the capital by the yearly keep of a productive "
                "hand. The figures are written for this lesson; Smith gives none."
            ),
        }),
        "steps_title": "Following a capital through a year",
        "steps_intro": "Four steps, repeated for each year.",
        "steps": [
            ("Find the revenue",
             "Multiply the capital by its return. That is what the capital produces "
             "above replacing itself, and it is the owner's to spend or to save."),
            ("Split it into spent and saved",
             "The saved share goes back into the capital. The spent share maintains "
             "whatever hands the owner chooses to keep, and Smith expects it to "
             "maintain unproductive ones more often than not."),
            ("Compute next year's capital",
             "Add the saved revenue to the capital. If the owner spends all of it, the "
             "capital does not change, and the same number of productive hands is "
             "maintained."),
            ("Count the hands",
             "Divide the capital by the yearly keep of one productive hand. A bigger "
             "capital maintains more of them; that is the whole of Smith's claim about "
             "what saving does."),
        ],
        "worked": {
            "title": "A thousand pounds, saved in three ways",
            "intro": [
                "Take the three presets. The figures are written for the lesson. A capital "
                "of £1,000 returns ten per cent a year and a productive hand costs £25 "
                "a year to keep.",
            ],
            "lines": [
                "revenue:  1,000 · 1/10 = 100",
                "hands at the start:  1,000 / 25 = 40",
                "all spent:  1,000 + 0 = 1,000, still 40",
                "half saved, year one:  1,000 + 50 = 1,050, so 42",
                "all saved, year two:  1,100 + 110 = 1,210, so 48.4",
            ],
            "after": [
                "The hands are counted in whole and part, because the lab divides "
                "exactly and does not round. What it shows is Smith's arithmetic: the "
                "owner who spends keeps the same fund, and each pound saved is a pound "
                "added to the fund for the productive.",
            ],
        },
        "quiz_title": "Which labour leaves a fund behind",
        "quiz": [
            {"q": "Which of these does Smith class as unproductive labour?",
             "a": ["A weaver making cloth for sale",
                   "A farm labourer ploughing for his master",
                   "An opera-singer",
                   "A workman making hats for a manufacturer"],
             "c": 2,
             "why": "His list of unproductive labourers includes &ldquo;players, buffoons, "
                    "musicians, opera-singers, opera-dancers&rdquo;, because their work "
                    "&ldquo;perishes in the very instant of its production&rdquo;. The "
                    "weaver, the farm labourer and the hatter all fix their labour in "
                    "something vendible."},
            {"q": "A gentleman has a capital of 2,000 returning 10 per cent a year. He "
                  "spends all of the revenue on servants. On Smith's account, what is "
                  "his capital next year?",
             "a": ["2,200",
                   "2,000",
                   "1,800",
                   "2,400"],
             "c": 1,
             "why": "The revenue is `2,000 · 1/10 = 200`, and it is spent on servants, so "
                    "none is added: the capital is unchanged at 2,000. It would be 2,200 "
                    "if he saved all of it. It would fall only if he spent more than "
                    "the revenue, which is the next lesson."},
            {"q": "Why does Smith say the master of a manufacturer's workman is not made "
                  "poorer by his wages, while the master of a menial servant is?",
             "a": ["Servants are paid more than manufacturing workmen",
                   "A servant's labour has no value and deserves no reward",
                   "The workman is paid out of revenue and the servant out of capital",
                   "The workman's wages are restored with a profit in the improved value "
                   "of what he works upon, and the servant's maintenance never is"],
             "c": 3,
             "why": "Smith's reason is that &ldquo;the value of those wages being generally restored, together "
                    "with a profit, in the improved value of the subject upon which his "
                    "labour is bestowed. But the maintenance of a menial servant never is "
                    "restored.&rdquo; Smith says of the servant's labour that it "
                    "&ldquo;has its value, and deserves its reward&rdquo;, and the "
                    "funds run the other way round: capital maintains the workman, "
                    "revenue the servant."},
            {"q": "A year's produce divides into a part that replaces capital and a part "
                  "that is revenue. What does Smith say the first part maintains?",
             "a": ["Productive hands only",
                   "Productive and unproductive hands alike",
                   "Only the owner of the capital",
                   "Hands in proportion to their rank"],
             "c": 0,
             "why": "That part of the annual produce &ldquo;pays the wages of productive "
                    "labour only&rdquo;. The revenue, as profit or as rent, may maintain "
                    "either kind, and Smith says its owners seem to have &ldquo;some "
                    "predilection&rdquo; for the idle ones."},
        ],
        "mistakes": [
            ("Reading unproductive as useless or disreputable",
             "Smith puts the sovereign, the judge and the physician in the list and says "
             "of the lowest of them that their labour has &ldquo;a certain value&rdquo; "
             "like all labour. The word marks whether the labour leaves something that "
             "can later buy an equal quantity of labour, and nothing else. The lab's "
             "servants are maintained out of revenue, not for being idle."),
            ("Thinking the owner who spends his revenue impoverishes himself",
             "If he spends only the revenue, his capital is where it was: in the "
             "first preset it is £1,000 after two years. What he does not do is add "
             "to it. Smith's warning is about spending the capital itself, and the "
             "next lesson runs that case."),
            ("Taking the distinction as Smith's last word on it",
             "Say, Marx and the national accounts all draw it elsewhere, and each has "
             "reasons. Smith's test answers one question, which labour leaves a fund "
             "behind for the next year, and the objections are mostly about a different "
             "one. A reader should keep the two apart before taking sides."),
        ],
        "standard": (
            "Finish when you can say what makes labour productive and follow a capital "
            "when its revenue is spent.",
            "State Smith's test, say which of two stated hands is productive, and compute "
            "a capital and the hands it maintains after a stated number of years when a "
            "stated share of its revenue is saved."
        ),
        "note": (
            "The lab compounds a capital from a return and a saved share. It cannot say "
            "which labour is productive: that is Smith's definition, and the next "
            "chapter's, and the lab takes the shares as given. The ten per cent return "
            "and the £25 keep are written for this lesson, and the physician and the "
            "player cannot be put in as numbers without deciding the very question the "
            "chapter raises."
        ),
    },
    # ---------------------------------------------------------------- 02
    # PSU text l. 11000-11404 (Book II, Chapter 3, rest). l. 11004-11039 (parsimony,
    # not industry; saved is consumed); l. 11040-11061 (the frugal man; the prodigal);
    # l. 11082-11128 (money and the prodigal); l. 11129-11186 (the desire of bettering
    # our condition; public prodigality); l. 11187-11298 (England; the French wars;
    # kings and ministers); l. 11299-11404 (durable expense).
    {
        "slug": "parsimony-and-the-prodigal",
        "title": "Parsimony and the Prodigal",
        "module": "Book II, Chapter 3, second part · Of the Accumulation of Capital, or of Productive and Unproductive Labour",
        "one_line": "Capital grows by what is saved and shrinks by what a prodigal spends of it, and a nation is more often ruined by its government's prodigality than by its people's.",
        "summary": (
            "Smith says that parsimony, and not industry, is the immediate cause of the "
            "increase of capital, that what is saved is consumed as surely as what is "
            "spent but by different people, and that every prodigal is a public enemy and "
            "every frugal man a public benefactor. Compound a capital for ten years under "
            "a frugal and a prodigal owner, and read Smith's reasons why private "
            "prodigality seldom matters and public prodigality can."
        ),
        "key": [
            "capital next year = capital + saved revenue",
            "saved revenue is spent, on productive hands",
            "prodigal: spends revenue and some capital",
            "same consumption, different consumers",
            "public prodigality can impoverish a nation",
        ],
        "key_label": "Parsimony in five lines",
        "concepts_intro": (
            "The rest of Chapter 3 argues from the distinction in the first part. It has "
            "three claims, and the third is about governments."
        ),
        "concepts": [
            ("Parsimony, not industry",
             "Industry provides what parsimony accumulates. Whatever industry earns, "
             "unless it is saved and stored up, the capital is never the greater."),
            ("Saved is consumed too",
             "What is saved is eaten as truly as what is spent. The difference is "
             "who eats it: productive labourers who reproduce its value with a profit, "
             "or idle guests and servants who leave nothing behind."),
            ("Private and public prodigality",
             "The prodigal diminishes the funds for productive labour, but the frugality "
             "of the rest compensates. A government that spends on unproductive hands "
             "can outrun all the frugality of its subjects."),
        ],
        "read_title": "The frugal man, the prodigal and the king",
        "read_intro": (
            "The second half of the chapter is longer, and it goes from a single "
            "owner's table to the wars of a century. The sums are small and the claims "
            "are large."
        ),
        "body": [
            ("p", "<strong>Book II, Chapter 3.</strong> &ldquo;Capitals are increased by "
                  "parsimony, and diminished by prodigality and misconduct.&rdquo; Then the "
                  "mechanism. &ldquo;Whatever a person saves from his revenue he adds to "
                  "his capital, and either employs it himself in maintaining an additional "
                  "number of productive hands, or enables some other person to do so, by "
                  "lending it to him for an interest, that is, for a share of the "
                  "profits.&rdquo;"),
            ("p", "The next sentence is the one that readers quote, because it appears to "
                  "demote the thing most of us think of as the engine. &ldquo;Parsimony, "
                  "and not industry, is the immediate cause of the increase of "
                  "capital.&rdquo; But Smith does not leave industry out. &ldquo;Industry, "
                  "indeed, provides the subject which parsimony accumulates; but whatever "
                  "industry might acquire, if parsimony did not save and store up, the "
                  "capital would never be the greater.&rdquo; Think of a farmer with a good "
                  "harvest who eats the whole of it. He has been industrious, and his "
                  "capital is the same as last year's."),
            ("p", "The part of the argument that a modern reader is likely to doubt is the "
                  "next. Saving is not hoarding. &ldquo;What is annually saved, is as "
                  "regularly consumed as what is annually spent, and nearly in the same "
                  "time too: but it is consumed by a different set of people.&rdquo; The "
                  "rich man who spends his revenue feeds idle guests and menial servants "
                  "who &ldquo;leave nothing behind them in return for their "
                  "consumption&rdquo;. The one who saves it sets labourers to work who "
                  "&ldquo;reproduce, with a profit, the value of their annual "
                  "consumption&rdquo;. &ldquo;The consumption is the same, but the "
                  "consumers are different.&rdquo; Nothing in Smith's saver puts money "
                  "under a mattress; the saving is immediately employed as capital, by him "
                  "or by a borrower."),
            ("p", "He adds a longer view, in a passage that is nearer to a sermon than to a "
                  "sum. &ldquo;By what a frugal man annually saves, he not only affords "
                  "maintenance to an additional number of productive hands, for that of "
                  "the ensuing year, but like the founder of a public work-house he "
                  "establishes, as it were, a perpetual fund for the maintenance of an "
                  "equal number in all times to come.&rdquo; The prodigal does the reverse. "
                  "&ldquo;By not confining his expense within his income, he encroaches "
                  "upon his capital.&rdquo; He &ldquo;pays the wages of idleness with those "
                  "funds which the frugality of his forefathers had, as it were, "
                  "consecrated to the maintenance of industry&rdquo;."),
            ("p", "The lab runs these as a decade. The capital is £1,000, its return ten "
                  "per cent a year and a productive hand costs £25 to keep, all written for "
                  "this lesson. A frugal owner who saves half of each year's revenue "
                  "multiplies the capital by 1.05 each year, so after ten years it is about "
                  "£1,628.89 and maintains about 65 hands. One who saves all of it "
                  "multiplies by 1.1, and ends at about £2,593.74 and 104 hands. One who "
                  "saves nothing stays at £1,000 and 40. A prodigal who spends the whole "
                  "revenue and a further half of it out of capital multiplies by 0.95, and "
                  "in the fourth preset ends at about £598.74, with fewer than 24. Smith's "
                  "sentence is the first and the last of these: capitals are increased "
                  "and diminished, and the difference compounds."),
            ("p", "Smith then asks a question that sounds like a Mercantilist's: if the "
                  "prodigal buys only home-made goods, does the country lose anything, "
                  "since the money stays? He answers in values: the food and clothing "
                  "the unproductive consume ought to have maintained productive hands, who "
                  "would have reproduced their value with a profit. &ldquo;There would "
                  "have been two values instead of one.&rdquo; And the gold that goes "
                  "abroad when a country declines is &ldquo;not the cause, but the "
                  "effect of its declension&rdquo;. Whatever you think the real wealth of a "
                  "country consists in, he concludes, whether &ldquo;in the value of the "
                  "annual produce of its land and labour, as plain reason seems to "
                  "dictate, or in the quantity of the precious metals which circulate "
                  "within it, as vulgar prejudices suppose; in either view of the matter, "
                  "every prodigal appears to be a public enemy, and every frugal man a "
                  "public benefactor.&rdquo;"),
            ("p", "Then comes the reassurance, which is the part of the chapter most often "
                  "forgotten. &ldquo;It can seldom happen, indeed, that the circumstances "
                  "of a great nation can be much affected either by the prodigality or "
                  "misconduct of individuals&rdquo;, since the frugality of others more "
                  "than compensates. The reason he gives is a motive: the principle that "
                  "prompts to expense is &ldquo;the passion for present enjoyment&rdquo;, "
                  "momentary and occasional, and the one that prompts to save is &ldquo;the "
                  "desire of bettering our condition; a desire which, though generally "
                  "calm and dispassionate, comes with us from the womb, and never leaves us "
                  "till we go into the grave&rdquo;. Bankrupts, he says, are &ldquo;not "
                  "much more, perhaps, than one in a thousand&rdquo; of those in business. "
                  "The figure is his guess, and he gives no source."),
            ("p", "Governments are a different matter. &ldquo;Great nations are never "
                  "impoverished by private, though they sometimes are by public "
                  "prodigality and misconduct.&rdquo; The public revenue is employed "
                  "almost wholly on unproductive hands, courts, churches, fleets and "
                  "armies, which in peace produce nothing and in war acquire nothing "
                  "that repays them. He counts the cost in England: &ldquo;In the course of "
                  "the four French wars, the nation has contracted more than £145,000,000 "
                  "of debt, over and above all the other extraordinary annual expense "
                  "which they occasioned&rdquo;, so that the whole &ldquo;cannot be "
                  "computed at less than £200,000,000&rdquo;. Yet England grew richer "
                  "through them, because the effort of every man to better his condition "
                  "&ldquo;protected by law, and allowed by liberty to exert itself in the "
                  "manner that is most advantageous, which has maintained the progress of "
                  "England towards opulence and improvement&rdquo;. He is dry about the "
                  "conclusion: kings and ministers are &ldquo;themselves always, and "
                  "without any exception, the greatest spendthrifts in the society. Let "
                  "them look well after their own expense, and they may safely trust "
                  "private people with theirs.&rdquo; Sumptuary laws and bans on foreign "
                  "luxuries are, in his words, a &ldquo;presumption&rdquo;."),
            ("p", "The chapter closes on a question of taste with an economic edge. A "
                  "rich man's expense may be in things consumed at once, a table and "
                  "servants, or in things that last, a house, books, pictures. The second "
                  "accumulates, and it passes down: &ldquo;What was formerly a seat of "
                  "the family of Seymour, is now an inn upon the Bath road.&rdquo; It "
                  "also maintains productive rather than unproductive hands. Smith "
                  "stops himself from drawing a moral: &ldquo;I would not, however, by all "
                  "this, be understood to mean, that the one species of expense always "
                  "betokens a more liberal or generous spirit than the other.&rdquo;"),
            ("p", "Three objections, each stated at the strength its holders gave it. "
                  "Mandeville's <em>Fable of the Bees</em> (1714) had argued that the "
                  "spending of the vicious supported trade; Smith's answer is that the "
                  "same pound spent otherwise would have fed productive hands. Malthus "
                  "argued in 1820 that saving can outrun the demand that makes it "
                  "profitable, so that capital piles up unemployed, and Keynes in 1936 "
                  "argued that if everyone saves more at once, incomes fall; Smith's "
                  "reply, that the saved is consumed by someone, assumes the saving "
                  "finds an employer, which is the point they dispute. Marx replied to "
                  "Smith's claim that what is accumulated is consumed by productive "
                  "labourers in Capital's lesson <em>Surplus Value into Capital</em>, "
                  "which this lesson does not repeat."),
            ("p", "The next lesson, <em>Stock Lent at Interest</em>, follows a saving "
                  "that is not employed by its owner but lent to someone who will employ "
                  "it, which is what Smith turns to in Chapter 4."),
        ],
        "lab": ("wonkit", {
            "mode": "stock",
            "view": "accumulate",
            "money_unit": "£",
            "preset": "frugal",
            "presets": [
                {"id": "frugal", "label": "An owner saving half his revenue for ten years, written for this lesson",
                 "capital": 1000, "return": 10, "saved": 50, "years": 10, "wage": 25, "expect": {"wstFirst": "revenue £100: £50 added to the capital, £50 spent", "wstRate": "+5% a year", "wstAfter": "≈ £1,628.89 after 10 years", "wstChange": "≈ +62.89%", "wstLabour": "40 → ≈ 65.16 workers", "wstSecond": "no second saving given"}},
                {"id": "all-saved", "label": "An owner saving all of it, written for this lesson",
                 "capital": 1000, "return": 10, "saved": 100, "years": 10, "wage": 25, "expect": {"wstFirst": "revenue £100: £100 added to the capital, £0 spent", "wstRate": "+10% a year", "wstAfter": "≈ £2,593.74 after 10 years", "wstChange": "≈ +159.37%", "wstLabour": "40 → ≈ 103.75 workers", "wstSecond": "no second saving given"}},
                {"id": "even", "label": "An owner whose expense just equals his revenue, written for this lesson",
                 "capital": 1000, "return": 10, "saved": 0, "years": 10, "wage": 25, "expect": {"wstFirst": "revenue £100: £0 added to the capital, £100 spent", "wstRate": "0% a year", "wstAfter": "£1,000 after 10 years", "wstChange": "0%", "wstLabour": "40 → 40 workers", "wstSecond": "no second saving given"}},
                {"id": "prodigal", "label": "A prodigal spending his revenue and half as much again out of capital, written for this lesson",
                 "capital": 1000, "return": 10, "saved": -50, "years": 10, "wage": 25, "expect": {"wstFirst": "revenue £100: £150 spent, £50 of it taken from the capital", "wstRate": "−5% a year", "wstAfter": "≈ £598.74 after 10 years", "wstChange": "≈ −40.13%", "wstLabour": "40 → ≈ 23.95 workers", "wstSecond": "no second saving given"}},
            ],
            "panel_title": "A capital for ten years",
            "panel_intro": (
                "A capital returns a stated share of itself each year as revenue; a "
                "stated share of the revenue is saved, or, if negative, taken out of "
                "the capital to be spent. The lab compounds year by year and divides "
                "the capital by a productive hand's yearly keep. The figures are written "
                "for this lesson."
            ),
        }),
        "steps_title": "Compounding a capital under saving",
        "steps_intro": "Four steps, repeated for as many years as you like.",
        "steps": [
            ("Find the yearly factor",
             "Multiply the return by the share saved, and add one. A return of 10 per "
             "cent with half saved is `1 + 1/10 · 1/2`, which is 21/20."),
            ("Multiply year by year",
             "Each year's capital is the last year's times the factor. Do not add the "
             "saving to the original capital each time: the saving earns a return too."),
            ("Read a negative share as a prodigal's",
             "A negative share takes capital out and spends it as well as the revenue. "
             "The factor falls below one and the capital shrinks, at an increasing "
             "rate in pounds only if the factor is below zero, which it is not here."),
            ("Count the hands",
             "Divide each year's capital by the yearly keep of a productive hand. The "
             "difference between the paths, in hands, is Smith's difference between "
             "the benefactor and the public enemy."),
        ],
        "worked": {
            "title": "The frugal and the prodigal, two years",
            "intro": [
                "Take the first and fourth presets, for two years by hand. The figures are "
                "written for the lesson: a capital of £1,000, a return of ten per cent, a "
                "keep of £25 a hand.",
            ],
            "lines": [
                "frugal factor:  1 + 1/10 · 1/2 = 21/20",
                "frugal, two years:  1,000 · 21/20 · 21/20 = 1,102.50",
                "prodigal factor:  1 − 1/10 · 1/2 = 19/20",
                "prodigal, two years:  1,000 · 19/20 · 19/20 = 902.50",
                "hands, two years:  1,102.50 / 25 = 44.1 and 902.50 / 25 = 36.1",
            ],
            "after": [
                "In ten years the frugal path reaches about 1,628.89 and the prodigal's "
                "falls to about 598.74. The gap in hands maintained is about 41. "
                "That gap is Smith's perpetual fund, set against its opposite.",
            ],
        },
        "quiz_title": "Saving, spending and the nation",
        "quiz": [
            {"q": "On Smith's account, what is the immediate cause of the increase of "
                  "capital?",
             "a": ["Industry",
                   "Foreign trade",
                   "Parsimony",
                   "A larger quantity of money"],
             "c": 2,
             "why": "&ldquo;Parsimony, and not industry, is the immediate cause of the "
                    "increase of capital.&rdquo; Industry provides what is saved, but "
                    "without saving, he says, &ldquo;the capital would never be the "
                    "greater&rdquo;."},
            {"q": "A capital of 2,000 returns 10 per cent a year, and the owner saves half "
                  "of the revenue each year. What is the capital after one year?",
             "a": ["2,200",
                   "2,100",
                   "2,050",
                   "2,000"],
             "c": 1,
             "why": "The revenue is `2,000 · 1/10 = 200`, half of it saved is 100, and "
                    "`2,000 + 100 = 2,100`. The capital is 2,200 only if all the revenue "
                    "is saved, and 2,050 would mean saving a quarter."},
            {"q": "What difference does Smith say there is between what is saved and what "
                  "is spent?",
             "a": ["What is saved is not consumed at all, and what is spent is",
                   "What is saved is consumed at once, and what is spent is kept",
                   "There is no difference, since the same goods are eaten",
                   "Both are consumed, but by different people: labourers who reproduce "
                   "the value with a profit, or idle guests and servants who leave "
                   "nothing behind"],
             "c": 3,
             "why": "&ldquo;What is annually saved, is as regularly consumed as what is "
                    "annually spent, and nearly in the same time too: but it is consumed "
                    "by a different set of people.&rdquo; Smith does not say saving is "
                    "hoarding, and he does not say the consumption is the same in effect."},
            {"q": "What does Smith say of kings and ministers who pretend to watch over "
                  "the economy of private people?",
             "a": ["It is presumption, since they are themselves always the greatest "
                   "spendthrifts in the society",
                   "They are right to do so, since private people are the greatest spendthrifts",
                   "They should tax every luxury to keep it from the poor",
                   "They should do so only in time of war"],
             "c": 0,
             "why": "&ldquo;They are themselves always, and without any exception, the "
                    "greatest spendthrifts in the society. Let them look well after "
                    "their own expense, and they may safely trust private people with "
                    "theirs.&rdquo;"},
        ],
        "mistakes": [
            ("Reading parsimony as hoarding",
             "Smith's saver does not shut money in a chest. What he saves is "
             "&ldquo;immediately employed as a capital&rdquo;, by himself or by someone he "
             "lends it to, and is consumed by labourers. In the lab the saved share is "
             "added to the capital that earns a return, so it is working from the first "
             "year."),
            ("Thinking Smith blames the private prodigal for national decline",
             "He says the opposite: private prodigality is compensated, since the "
             "frugality of others is stronger, and &ldquo;Great nations are never "
             "impoverished by private, though they sometimes are by public prodigality and misconduct&rdquo;. What can impoverish one is "
             "public prodigality, and even that, he says, England's history shows the "
             "effort of private people can outweigh for a long time."),
            ("Reading &ldquo;Parsimony, and not industry&rdquo; as saying industry does not "
             "matter",
             "In the same sentence, &ldquo;Industry, indeed, provides the subject which "
             "parsimony accumulates&rdquo;. The claim is about the last step, which is "
             "saving what has been earned. The even preset, an owner who earns and "
             "spends it all, is as industrious as the frugal one and ends where he began."),
        ],
        "standard": (
            "Finish when you can compound a capital under saving and under prodigality "
            "and say why Smith distinguishes private from public prodigality.",
            "Given a capital, a return, a share saved or overspent and a number of "
            "years, compute the capital and the hands it maintains, and state Smith's "
            "reason for treating a government's prodigality differently from a "
            "person's."
        ),
        "note": (
            "The lab assumes a constant return on capital, which Smith himself says falls "
            "as capital grows (the next lesson). It also assumes that whatever is saved "
            "finds an employer at the same return, which is the point Malthus and Keynes "
            "dispute. The presets are written for this lesson; the only figures in it "
            "that are Smith's are the war debts, and they are not entered in the lab."
        ),
    },
    # ---------------------------------------------------------------- 03
    # PSU text l. 11405-11689 (Book II, Chapter 4). l. 11407-11444 (borrower and
    # lender; country gentlemen); l. 11445-11502 (the money is the deed of
    # assignment; A, B, C); l. 11503-11533 (interest falls as stock grows);
    # l. 11534-11623 (Locke, Law, Montesquieu; Hume); l. 11624-11671 (usury laws);
    # l. 11672-11689 (the price of land).
    {
        "slug": "stock-lent-at-interest",
        "title": "Stock Lent at Interest",
        "module": "Book II, Chapter 4 · Of Stock lent at Interest",
        "one_line": "A loan hands over a claim on the goods of the year, not the money that carries it; interest falls as stock grows, and land sells for as many years' rent as the rate of interest allows.",
        "summary": (
            "Chapter 4 says what is lent when money is lent, why the rate of interest "
            "falls as a country's stock increases, why a law fixing it should stand a "
            "little above the lowest market rate, and how the price of land follows the "
            "rate. Compute years' purchase and the price of an estate at ten, six, five "
            "and four per cent, and set it beside Smith's own years' purchase."
        ),
        "key": [
            "a loan assigns goods, not coin",
            "interest falls as stock grows",
            "years' purchase = 100 / rate",
            "price of land = rent × years' purchase",
            "legal rate: a little above market low",
        ],
        "key_label": "Interest and land in five lines",
        "concepts_intro": (
            "The chapter is short and has four arguments, which the lesson takes in "
            "the order Smith gives them."
        ),
        "concepts": [
            ("What a loan is",
             "The lender assigns to the borrower a portion of the annual produce, to "
             "use as he pleases. Money is only the deed of assignment, and the same "
             "pieces can serve many loans in a few days."),
            ("Why interest falls",
             "As stock increases, profits fall, because capitals compete for "
             "employment and for labourers, and interest, which is paid out of profit, "
             "falls with them. It does not fall because gold has become plentiful."),
            ("Land and the legal rate",
             "The price of land depends on the market rate of interest, and a law "
             "fixing a maximum rate works best when it stands somewhat above the lowest "
             "market rate, not at it and not far above it."),
        ],
        "read_title": "The loan, the rate, the law and the land",
        "read_intro": (
            "Chapter 4 is a quick walk through four questions, and the chapter's "
            "figures, a legal rate of five per cent and land at thirty years' "
            "purchase, are an age away from ours."
        ),
        "body": [
            ("p", "<strong>Book II, Chapter 4.</strong> &ldquo;He expects that in due time "
                  "it is to be restored to him, and that, in the mean time, the borrower "
                  "is to pay him a certain annual rent for the use of it.&rdquo; The "
                  "lender regards it as capital. The borrower may use it as a capital "
                  "too: &ldquo;he employs it in the maintenance of productive labourers, "
                  "who reproduce the value, with a profit&rdquo;, and so can restore it "
                  "and pay the interest. Or, using it for immediate consumption, he &ldquo;acts the part of a "
                  "prodigal&rdquo; and spends it, in which case he can pay neither "
                  "without selling something else. Smith thinks the first is much "
                  "commoner than people suppose, since a lender of common prudence "
                  "would laugh at being asked which kind he preferred, and he includes "
                  "a light remark about the country gentlemen who borrow on mortgage: "
                  "&ldquo;What they borrow, one may say, is commonly spent before they "
                  "borrow it.&rdquo; They borrow, that is, to replace the capitals of the "
                  "shopkeepers who gave them credit."),
            ("p", "Then the point of the chapter's opening half. &ldquo;Almost all loans "
                  "at interest are made in money, either of paper, or of gold and silver; "
                  "but what the borrower really wants, and what the lender readily "
                  "supplies him with, is not the money, but the money's worth, or the "
                  "goods which it can purchase.&rdquo; The lender &ldquo;assigns to the "
                  "borrower his right to a certain portion of the annual produce of the "
                  "land and labour of the country, to be employed as the borrower "
                  "pleases&rdquo;. Money is &ldquo;as it were, but the deed of "
                  "assignment&rdquo;."),
            ("p", "That is why the amount of stock lent in a country is not set by the "
                  "quantity of coin. Smith's illustration is three loans on the same "
                  "pieces. A lends £1,000 to W, who buys £1,000 of goods from B; B, who "
                  "needs no money, lends the same pieces to X, who buys from C; C lends "
                  "them to Y. &ldquo;In this manner, the same pieces, either of coin or of "
                  "paper, may, in the course of a few days, serve as the Instrument of "
                  "three different loans, and of three different purchases, each of "
                  "which is, in value, equal to the whole amount of those pieces.&rdquo; "
                  "Smith's sum: &ldquo;The stock lent by the three monied men is equal to the value "
                  "of the goods which can be purchased with it, and is three times "
                  "greater than that of the money with which the purchases are "
                  "made&rdquo;: three loans of £1,000 on £1,000 of coin make £3,000 of "
                  "stock lent."),
            ("p", "Now the rate. &ldquo;As the quantity of stock to be lent at interest "
                  "increases, the interest, or the price which must be paid for the use of "
                  "that stock, necessarily diminishes.&rdquo; The ordinary causes of a "
                  "price falling as the quantity rises are there, and one peculiar to "
                  "this case: as capitals increase, profits diminish, owners compete for "
                  "employments and for labourers, and &ldquo;Their competition raises "
                  "the wages of labour, and sinks the profits of stock&rdquo;. Interest, "
                  "which can only be paid out of profit, falls with them. So the "
                  "fall in the rate goes with a rise in wages, which is the "
                  "other side of Chapter 8 of Book I."),
            ("p", "Smith turns aside to correct three writers by name. Locke, Law and "
                  "Montesquieu, he says, thought the discovery of the Spanish West Indies "
                  "had lowered interest by making gold and silver plentiful. Hume had "
                  "exposed that, but Smith gives a short argument of his own, with "
                  "numbers. Say the value of silver had fallen to half in the countries "
                  "where interest fell from ten to five per cent. Then &ldquo;If £100 are "
                  "in those countries now of no more value than £50 were then, £10 must "
                  "now be of no more value than £5 were then.&rdquo; A fall in the value "
                  "of silver cuts the capital and the interest by the same proportion, "
                  "and leaves the rate where it was. But &ldquo;By reducing the rate of "
                  "interest, therefore, from ten to five per cent. we give for the use of "
                  "a capital, which is supposed to be equal to one half of its former "
                  "value, an interest which is equal to one fourth only of the value of "
                  "the former interest.&rdquo; The lower rate needs another cause, which "
                  "is that stock has grown. A different quantity of money changes the "
                  "number of pieces in a payment and leaves the goods the same."),
            ("p", "Interest and the law. Smith's view of the usury laws is not the simple "
                  "one. A ban on interest, he says, increases usury: &ldquo;as something "
                  "can everywhere be made by the use of money, something ought "
                  "everywhere to be paid for the use of it.&rdquo; In countries where "
                  "interest is allowed, a legal maximum &ldquo;ought always to be "
                  "somewhat above the lowest market price, or the price which is "
                  "commonly paid for the use of money by those who can give the most "
                  "undoubted security&rdquo;. If it is fixed at that lowest price, it "
                  "&ldquo;ruins, with honest people who respect the laws of their "
                  "country, the credit of all those who cannot give the very best "
                  "security, and obliges them to have recourse to exorbitant "
                  "usurers&rdquo;. If it is fixed much higher, at eight or ten per cent, "
                  "&ldquo;the greater part of the money which was to be lent, would be "
                  "lent to prodigals and projectors, who alone would be willing to give "
                  "this high interest&rdquo;. In Great Britain, with government "
                  "borrowing at three per cent and private people on good security at "
                  "four or four and a half, five per cent &ldquo;is perhaps as proper as "
                  "any&rdquo;. He adds that no law can bring the rate below the lowest "
                  "ordinary market rate of the time."),
            ("p", "Last, land. &ldquo;When interest was at ten per cent. land was commonly "
                  "sold for ten or twelve years purchase. As interest sunk to six, five, "
                  "and four per cent. the price of land rose to twenty, five-and-twenty, "
                  "and thirty years purchase.&rdquo; A years' purchase is the number of "
                  "years' rent a buyer pays, so the price is the rent times that number. "
                  "If land were a loan and nothing else, the number would be a hundred "
                  "divided by the rate: ten years at ten per cent, twenty at five. "
                  "The first preset runs that, on a rent of £100: £1,000 at ten per cent "
                  "and £2,000 at five. Smith's own figures sit a little above the bare "
                  "rule at the lower rates, twenty years at six per cent where the rule "
                  "gives sixteen and two thirds, because land has &ldquo;superior "
                  "security&rdquo; and other advantages, which &ldquo;will generally "
                  "dispose him to content himself with a smaller revenue from land, "
                  "than what he might have by lending out his money at interest&rdquo;. "
                  "The second preset sets six per cent beside four, whose rule is "
                  "twenty-five years, and Smith's figure for that case is thirty. The third "
                  "uses his comparison of countries: &ldquo;In England it commonly sells "
                  "at thirty, in France at twenty years purchase.&rdquo; The rates are "
                  "ours, not his: 10/3 per cent gives thirty years' purchase, and 5 per "
                  "cent gives twenty."),
            ("p", "Two things need saying about the lesson's honesty. The interest rates in "
                  "the presets are those the rule implies, not rates Smith reports, "
                  "except where he states them, and a reader should not take the lab for "
                  "an account of what England or France paid. And the chapter's two "
                  "famous positions have had famous critics. Jeremy Bentham's <em>Defence "
                  "of Usury</em> (1787), one of whose letters is addressed to Smith, "
                  "argued that a legal maximum keeps credit from the inventor and the "
                  "sober borrower with a new idea as well as the prodigal, and "
                  "that the law should leave the bargain to the parties. Marx treated "
                  "interest and the price of land as forms of a claim on surplus value; "
                  "Capital's lesson <em>Interest-Bearing Capital</em> reads that account, "
                  "which this lesson does not repeat."),
            ("p", "Chapter 5, the subject of the next two lessons, asks where a capital "
                  "does the most good once it is owned or lent: the next lesson is <em>The "
                  "Four Ways of Employing Capital</em>."),
        ],
        "lab": ("wonkit", {
            "mode": "interest",
            "view": "purchase",
            "money_unit": "£",
            "preset": "ten-and-five",
            "presets": [
                {"id": "ten-and-five", "label": "Interest at ten per cent and at five, on a rent of £100 (Smith's rates, a rent written for this lesson)",
                 "rent": 100, "rate": 10, "rate2": 5, "expect": {"witYp": "10 years’ purchase at 10%", "witPrice": "£1,000", "witYp2": "20 years’ purchase at 5%", "witPrice2": "£2,000 (+£1,000, +1 = +100%)", "witFetches": "no present yield given"}},
                {"id": "six-and-four", "label": "Interest at six per cent and at four (Smith's rates, a rent written for this lesson)",
                 "rent": 100, "rate": 6, "rate2": 4, "expect": {"witYp": "50/3 ≈ 16.67 years’ purchase at 6%", "witPrice": "≈ £1,666.67", "witYp2": "25 years’ purchase at 4%", "witPrice2": "£2,500 (≈ +£833.33, +1/2 = +50%)", "witFetches": "no present yield given"}},
                {"id": "england-france", "label": "England at thirty years' purchase and France at twenty (Smith's years; the rates are what they imply)",
                 "rent": 100, "rate": "10/3", "rate2": 5, "expect": {"witYp": "30 years’ purchase at 10/3 ≈ 3.33%", "witPrice": "£3,000", "witYp2": "20 years’ purchase at 5%", "witPrice2": "£2,000 (−£1,000, −1/3 ≈ −33.3%)", "witFetches": "no present yield given"}},
            ],
            "panel_title": "What an estate sells for",
            "panel_intro": (
                "Enter a yearly rent and a rate of interest, with a second rate to "
                "compare. The lab gives the years' purchase, a hundred divided by the "
                "rate, and the price, the rent times the years. The rent is written for "
                "this lesson; the rates and the years' purchase in the presets are "
                "Smith's, as the labels say."
            ),
        }),
        "steps_title": "From a rent and a rate to a price",
        "steps_intro": "Four steps, the same at any rate.",
        "steps": [
            ("Take the yearly rent",
             "The rent is what the estate pays its owner in a year, after the tenant "
             "has taken his wages and ordinary profit, as in Book I."),
            ("Find the years' purchase",
             "Divide 100 by the rate of interest in per cent. At ten per cent that is "
             "ten, at five twenty. A lower rate makes each year's rent worth more."),
            ("Multiply for the price",
             "The price of the estate is the rent times the years' purchase. This is the "
             "capital that would earn the same revenue at interest."),
            ("Compare with the market",
             "Set the figure beside what land actually sold for. Smith's years' purchase "
             "run above the rule at low rates, which he explains by the security of "
             "land, and the gap is the value of that advantage."),
        ],
        "worked": {
            "title": "An estate at ten per cent and at five",
            "intro": [
                "Take the first preset. A rent of £100 is written for the lesson, and the "
                "rates, ten and five per cent, are Smith's.",
            ],
            "lines": [
                "at ten per cent:  100 / 10 = 10 years' purchase",
                "price at ten per cent:  100 · 10 = 1,000",
                "at five per cent:  100 / 5 = 20 years' purchase",
                "price at five per cent:  100 · 20 = 2,000",
                "halving the rate doubles the price",
            ],
            "after": [
                "Smith's ten per cent is ten or twelve years' purchase, so the rule is "
                "close at ten. At six per cent the rule gives sixteen and two thirds "
                "and Smith twenty, at four per cent twenty-five and thirty. The "
                "difference grows as the rate falls, which is how he reads it: land's "
                "security is worth more years' rent as the alternative return falls.",
            ],
        },
        "quiz_title": "A loan, a rate and a price",
        "quiz": [
            {"q": "An estate pays a rent of 60 a year and the market rate of interest is "
                  "5 per cent. On the rule that the price is the rent times the years' "
                  "purchase, what does it sell for?",
             "a": ["300",
                   "3,000",
                   "1,200",
                   "120"],
             "c": 2,
             "why": "At 5 per cent the years' purchase is `100/5 = 20`, so the price is "
                    "`60 · 20 = 1,200`. 300 multiplies by the rate and not by its "
                    "reciprocal; 3,000 divides by it twice over."},
            {"q": "A lends £1,000 to W, who buys goods of that value from B; B lends the "
                  "same pieces to X, who buys from C; C lends them to Y. By Smith's "
                  "account, how much stock have A, B and C lent between them?",
             "a": ["£1,000",
                   "£3,000",
                   "£2,000",
                   "£4,000"],
             "c": 1,
             "why": "&ldquo;The stock lent by the three monied men is equal to the value "
                    "of the goods which can be purchased with it, and is three times "
                    "greater than that of the money with which the purchases are "
                    "made.&rdquo; Three loans of £1,000 each is £3,000."},
            {"q": "Where does Smith say the legal rate of interest should be fixed?",
             "a": ["Well below the lowest market rate, to protect borrowers",
                   "Precisely at the lowest market rate",
                   "At eight or ten per cent, to attract lenders",
                   "Somewhat above the lowest market rate, but not much above it"],
             "c": 3,
             "why": "&ldquo;This rate ought always to be somewhat above the lowest market "
                    "price&rdquo;, but &ldquo;ought not to be much above&rdquo; it. At the "
                    "lowest price it ruins the credit of those who cannot give the best "
                    "security; at eight or ten per cent the money goes to prodigals and "
                    "projectors."},
            {"q": "What does Smith give as the cause of the fall in interest in Europe?",
             "a": ["The increase of stock, which sinks profits and so interest",
                   "The discovery of the Spanish West Indies, which made silver more plentiful",
                   "Laws forbidding interest above a legal rate",
                   "A fall in the wages of labour"],
             "c": 0,
             "why": "As capitals increase, &ldquo;Their competition raises the wages of "
                    "labour, and sinks the profits of stock&rdquo;, and interest falls "
                    "with profit. The second answer is the view of Locke, Law and "
                    "Montesquieu, which Smith rejects; wages rise, not fall."},
        ],
        "mistakes": [
            ("Thinking a lender lends money",
             "What the borrower &ldquo;really wants&rdquo; is &ldquo;not the money, but the "
             "money's worth&rdquo;. A loan assigns a claim on the goods of the year, and "
             "the same coins can be lent three times in a few days, which is why the "
             "stock lent can exceed the coin."),
            ("Explaining a low rate by plenty of gold and silver",
             "If silver halves in value, both the capital and its interest halve, and the "
             "rate does not change. The rate falls, Smith says, because stock has "
             "grown and profits with it. In the lab the rate is an input because the "
             "chapter does not explain it from the quantity of money."),
            ("Thinking a low legal rate protects borrowers",
             "Fixed below the lowest market rate it is like a ban, and creditors take "
             "payment for the risk of breaking the law; fixed at that rate it shuts out "
             "those without the best security. Smith's rule is meant to keep the sober "
             "borrower ahead of the prodigal, not to cheapen money."),
        ],
        "standard": (
            "Finish when you can price an estate from its rent and the rate and say what "
            "a loan assigns.",
            "Given a rent and a rate of interest, compute the years' purchase and the "
            "price, compare two rates, and say, in Smith's terms, what is lent when "
            "money is lent and why the rate falls as stock grows."
        ),
        "note": (
            "The rule `100 / rate` is the lab's, not Smith's: it prices land as a loan, "
            "and Smith's own years' purchase run above it because land carries advantages "
            "the rule leaves out. The lab can do the sum; it cannot say what the "
            "advantages are worth, nor whether the rate caused the price or the price "
            "the rate. The rents are written for this lesson."
        ),
    },
    # ---------------------------------------------------------------- 04
    # PSU text l. 11690-11950 (Book II, Chapter 5, first part). l. 11693-11712
    # (four ways); l. 11713-11774 (each necessary; butchers and retailers);
    # l. 11775-11848 (the quantity of labour each puts in motion; nature in
    # agriculture); l. 11849-11918 (residence of capitals; an insufficient
    # capital); l. 11919-11950 (America; the course of prosperity).
    {
        "slug": "the-four-ways-of-employing-capital",
        "title": "The Four Ways of Employing Capital",
        "module": "Book II, Chapter 5, first part · Of the different Employment of Capitals",
        "one_line": "Equal capitals set very different quantities of productive labour going, according as they are laid out in farming, manufacturing, wholesale trade or retail; Smith ranks them in that order.",
        "summary": (
            "Chapter 5 sorts every capital into four employments and ranks them by the "
            "quantity of productive labour each puts in motion and the value each adds to "
            "the annual produce. Count the labour set going in each by the share of an "
            "equal capital that pays productive hands, and see that the order depends on "
            "that share, which is a premise and not a result."
        ),
        "key": [
            "farm, factory, wholesale, shop in order",
            "equal capitals, unequal labour set going",
            "labour set going = wages paid / yearly keep",
            "nature works with the farmer",
            "retailers can hurt one another, not the public",
        ],
        "key_label": "The four employments in five lines",
        "concepts_intro": (
            "Chapter 5 begins by classifying, and then ranks. The ranking is the part "
            "that critics have fought over."
        ),
        "concepts": [
            ("The four employments",
             "Raising the rude produce, manufacturing it, transporting it, and dividing "
             "it into small parcels for sale: these are the capitals of farmers, "
             "manufacturers, wholesale merchants and retailers, and each is necessary to "
             "the others."),
            ("Labour put in motion",
             "Equal capitals set unequal quantities of productive labour going, and add "
             "unequal values to the annual produce. A retailer's capital employs "
             "himself; a farmer's employs servants and cattle and also yields a rent."),
            ("Nature works in agriculture",
             "In farming, Smith says, Nature labours along with man, and the rent of "
             "the landlord is her work. In manufactures Nature does nothing and man does "
             "all, so the same labour reproduces less."),
        ],
        "read_title": "Four classes, then a ranking, then a warning",
        "read_intro": (
            "Smith is classifying employments by what they do for the country, not for "
            "their owners, and he says plainly that the two are not the same."
        ),
        "body": [
            ("p", "<strong>Book II, Chapter 5.</strong> &ldquo;A capital may be employed "
                  "in four different ways; either, first, in procuring the rude produce "
                  "annually required for the use and consumption of the society; or, "
                  "secondly, in manufacturing and preparing that rude produce for "
                  "immediate use and consumption; or, thirdly in transporting either the "
                  "rude or manufactured produce from the places where they abound to those "
                  "where they are wanted; or, lastly, in dividing particular portions of "
                  "either into such small parcels as suit the occasional demands of those "
                  "who want them.&rdquo;"),
            ("p", "Farmers, miners and fishermen take the first; master manufacturers the "
                  "second; wholesale merchants the third; retailers the fourth. "
                  "&ldquo;Each of those four methods of employing a capital is "
                  "essentially necessary, either to the existence or extension of the "
                  "other three, or to the general conveniency of the society.&rdquo; Smith "
                  "takes the trouble to defend the last, which he knows is the least "
                  "esteemed. Without retailers every man would be obliged to buy a whole "
                  "ox or a whole sheep at a time, and a poor workman would have to put "
                  "into his larder what he needed in his trade. &ldquo;The prejudices of "
                  "some political writers against shopkeepers and tradesmen are "
                  "altogether without foundation.&rdquo; Competition, not numbers, is "
                  "the check: with twenty grocers instead of two the chance of their "
                  "combining to raise the price is less, and their rivalry may ruin "
                  "some of them without hurting the buyer. The multitude of alehouses, "
                  "he adds, is an effect of a disposition to drink and not its cause."),
            ("p", "The ranking is the argument. All four are productive. &ldquo;Equal "
                  "capitals, however, employed in each of those four different ways, will "
                  "immediately put into motion very different quantities of productive "
                  "labour; and augment, too, in very different proportions, the value of the "
                  "annual produce of the land and labour of the society to which they "
                  "belong.&rdquo; Start at the bottom. &ldquo;The retailer himself is the "
                  "only productive labourer whom it immediately employs. In his profit "
                  "consists the whole value which its employment adds to the annual produce "
                  "of the land and labour of the society.&rdquo; His capital replaces the "
                  "merchant's, and that is its use."),
            ("p", "The wholesale merchant's capital replaces the capitals of farmers and "
                  "manufacturers, and also employs sailors and carriers: &ldquo;This is "
                  "all the productive labour which it immediately puts into motion, and "
                  "all the value which it immediately adds to the annual "
                  "produce.&rdquo; The manufacturer lays out part of his capital in "
                  "instruments, but &ldquo;a great part of it is always, either annually, "
                  "or in a much shorter period, distributed among the different workmen "
                  "whom he employs&rdquo;, so it &ldquo;puts immediately into motion, "
                  "therefore, a much greater quantity of productive labour, and adds a much "
                  "greater value to the annual produce of the land and labour of the "
                  "society, than an equal capital in the hands of any wholesale "
                  "merchant&rdquo;."),
            ("p", "At the top is the farmer. &ldquo;No equal capital puts into motion a "
                  "greater quantity of productive labour than that of the farmer. Not "
                  "only his labouring servants, but his labouring cattle, are productive "
                  "labourers.&rdquo; Why? Because &ldquo;Planting and tillage frequently "
                  "regulate more than they animate the active fertility of "
                  "Nature&rdquo;, and her share is the landlord's rent. &ldquo;It is the "
                  "work of Nature which remains, after deducting or compensating every "
                  "thing which can be regarded as the work of man. It is seldom less than "
                  "a fourth, and frequently more than a third, of the whole "
                  "produce.&rdquo; &ldquo;In them Nature does nothing; man does all; and "
                  "the reproduction must always be in proportion to the strength of the "
                  "agents that occasion it.&rdquo; Hence the verdict, &ldquo;Of all the "
                  "ways in which a capital can be employed, it is by far the most "
                  "advantageous to society.&rdquo;"),
            ("p", "The lab turns this into a count. Take equal capitals of £1,000 in each "
                  "employment and ask how much of each is paid to productive hands the "
                  "employment itself puts to work. Smith gives the order and no figures, "
                  "so the shares in the first preset are written for this lesson to "
                  "follow his order: £700 in the farm, for servants and cattle; £400 in "
                  "the factory, the rest being materials and instruments; £100 in the "
                  "warehouse, for sailors and carriers; £25 in the shop, which is the "
                  "retailer himself. At a keep of £25 a hand that is 28, 16, 4 and 1 "
                  "productive hands, in Smith's order, and the lab's ratio of the most "
                  "to the least is 28."),
            ("p", "Be clear what that sum shows. The count is computed from the shares "
                  "the lesson writes, so it cannot test Smith's ranking: it can only say "
                  "what the ranking amounts to in hands for a given set of shares. The "
                  "second preset makes the point. Give the factory a heavy fixed capital "
                  "that leaves only £150 for wages, and the wholesale trade a coal fleet "
                  "with £300 for sailors, and the order of manufacture and trade "
                  "reverses: 6 hands to 12. Smith knows it; he says elsewhere in the "
                  "chapter that the coal trade from Newcastle to London employs more "
                  "shipping than all the carrying trade of England. The order is a "
                  "premise about the shares, which is where the dispute is."),
            ("p", "He draws four consequences. Capitals in farming and in the retail trade "
                  "reside where they work, while the wholesale merchant's capital "
                  "&ldquo;may wander about from place to place, according as it can "
                  "either buy cheap or sell dear&rdquo;, so it matters little whether he "
                  "is a native or a foreigner. A country may not have capital for all "
                  "the employments at once, and if it must choose, it should take them "
                  "in his order: &ldquo;To attempt, however, prematurely, and with an "
                  "insufficient capital, to do all the three, is certainly not the "
                  "shortest way for a society, no more than it would be for an "
                  "individual, to acquire a sufficient one.&rdquo; The American colonies "
                  "grew fast because &ldquo;almost their whole capitals have hitherto been "
                  "employed in agriculture&rdquo;, and if they forced manufactures by "
                  "stopping European imports &ldquo;they would retard, instead of "
                  "accelerating, the further increase in the value of their annual "
                  "produce&rdquo;. And China, Egypt and Indostan, the richest countries in "
                  "the world by report, were renowned for agriculture and manufactures "
                  "more than for foreign trade."),
            ("p", "Now the objections, three of them. Ricardo, writing in 1817, held that "
                  "rent is not a bounty of Nature that agriculture adds to the world, but "
                  "the difference between better land and the worst land in use, so "
                  "that it is no proof that capital in farming employs more labour than "
                  "capital in a factory. A critic from the other side can point out that "
                  "manufactures also use natural powers, and Capital's lesson "
                  "<em>Differential Rent: General Remarks</em> begins with a waterfall "
                  "that drives a factory. And the idea that a country should take its "
                  "capitals in an order is the one that Friedrich List's later "
                  "<em>National System</em> reversed: he held that a young country must "
                  "build manufactures first, with protection, and then be rich enough "
                  "for the rest. Smith's own caution is that the order is not a law of "
                  "nature: it is what private profit and the policy of Europe happen to "
                  "have made of it, which the next lesson and Book III take up."),
            ("p", "The next lesson, <em>The Home, the Foreign and the Carrying Trade</em>, "
                  "ranks the three branches of wholesale trade the same way."),
        ],
        "lab": ("wonkit", {
            "mode": "stock",
            "view": "turnover",
            "money_unit": "£",
            "preset": "smith-order",
            "presets": [
                {"id": "smith-order", "label": "Four equal capitals, with wage shares written to follow Smith's order (his order, figures written for this lesson)",
                 "trades": [{"trade": "farm", "capital": 700, "returns": 1},
                            {"trade": "factory", "capital": 400, "returns": 1},
                            {"trade": "wholesale", "capital": 100, "returns": 1},
                            {"trade": "retail", "capital": 25, "returns": 1}],
                 "wage": 25, "expect": {"wstWork": "farm £700; factory £400; wholesale £100; retail £25", "wstTotal": "£1,225", "wstLabour": "farm 28; factory 16; wholesale 4; retail 1", "wstOrder": "farm, factory, wholesale, retail", "wstRatio": "28.00× (farm against retail)"}},
                {"id": "heavy-fixed", "label": "A factory with heavy fixed capital and a coal fleet, written for this lesson",
                 "trades": [{"trade": "farm", "capital": 700, "returns": 1},
                            {"trade": "factory", "capital": 150, "returns": 1},
                            {"trade": "wholesale", "capital": 300, "returns": 1},
                            {"trade": "retail", "capital": 25, "returns": 1}],
                 "wage": 25, "expect": {"wstWork": "farm £700; factory £150; wholesale £300; retail £25", "wstTotal": "£1,175", "wstLabour": "farm 28; factory 6; wholesale 12; retail 1", "wstOrder": "farm, wholesale, factory, retail", "wstRatio": "28.00× (farm against retail)"}},
            ],
            "panel_title": "Labour set going by equal capitals",
            "panel_intro": (
                "Each employment is a name, the sum of an equal capital that is paid to "
                "the productive hands it immediately employs, and the returns a year. The "
                "lab multiplies, divides by a hand's yearly keep and orders the trades. "
                "The shares are written for this lesson; Smith gives an order and no "
                "figures."
            ),
        }),
        "steps_title": "Counting the labour an employment sets going",
        "steps_intro": "Four steps, with the same capital laid out four ways.",
        "steps": [
            ("Fix equal capitals",
             "Smith compares equal capitals, so start every employment from the same "
             "sum. Without that the ranking compares sizes, not employments."),
            ("Find the part paid to productive hands",
             "For each employment, say how much of the capital goes to wages of the "
             "labourers it directly employs, and how much replaces other capitals, "
             "buys materials or lays out instruments."),
            ("Divide by the yearly keep",
             "The productive hands set going are the wage part times the returns a "
             "year, divided by the yearly keep of one hand."),
            ("Order the employments",
             "Rank them by hands set going. Then ask what the ranking rests on: a "
             "change in one share can change the order, and the shares are the "
             "premise."),
        ],
        "worked": {
            "title": "Four employments, one capital each",
            "intro": [
                "Take the first preset. The wage shares are written for the lesson to "
                "follow Smith's order, and the keep of a productive hand is £25 a year.",
            ],
            "lines": [
                "farm:  700 / 25 = 28 hands",
                "factory:  400 / 25 = 16 hands",
                "wholesale:  100 / 25 = 4 hands",
                "retail:  25 / 25 = 1 hand",
                "most to least:  28 / 1 = 28",
            ],
            "after": [
                "In the second preset the factory's share falls to 150 and the wholesale "
                "trade's rises to 300, so the hands become 28, 6, 12 and 1, and the "
                "wholesale trade ranks above the factory. The order Smith gives is the "
                "order those shares give; it is not a result of the sum.",
            ],
        },
        "quiz_title": "Which employment sets most labour going",
        "quiz": [
            {"q": "What are Smith's four employments of capital?",
             "a": ["Agriculture, mining, shipping and banking",
                   "Land, labour, stock and money",
                   "Agriculture, manufactures, wholesale trade and retail trade",
                   "Home trade, foreign trade, carrying trade and retail trade"],
             "c": 2,
             "why": "Capital is employed in raising the rude produce, in manufacturing it, "
                    "in transporting it, and in dividing it into small parcels, the "
                    "capitals of farmers, master manufacturers, wholesale merchants and "
                    "retailers. The home, foreign and carrying trades are the three "
                    "sorts of wholesale trade, and belong to the next lesson."},
            {"q": "Why does Smith put agriculture first?",
             "a": ["Because farmers are paid higher wages than manufacturers",
                   "Nature labours along with man in it, and her work is the rent of "
                   "the landlord, so the same labour reproduces more",
                   "Because land is the only thing that cannot be imported",
                   "Because farming needs no capital"],
             "c": 1,
             "why": "&ldquo;The labourers and labouring cattle, therefore, employed in "
                    "agriculture, not only occasion, like the workmen in manufactures, the "
                    "reproduction of a value equal to their own consumption&rdquo;, but "
                    "of &ldquo;a much greater value&rdquo;, because the landlord's rent is "
                    "&ldquo;the work of Nature&rdquo;."},
            {"q": "An employment lays out 500 of its capital in wages to the productive "
                  "hands it directly employs, once a year, and a hand costs 25 a year to "
                  "keep. How many hands does it set going?",
             "a": ["25",
                   "12.5",
                   "2",
                   "20"],
             "c": 3,
             "why": "`500 / 25 = 20`. Dividing by 40 gives 12.5, and 25 is the keep itself, "
                    "not a count of hands."},
            {"q": "What does Smith say of the multiplication of retailers?",
             "a": ["It can hurt the retailers themselves through competition, but cannot "
                   "hurt the public, who buy cheaper",
                   "It should be restrained by a tax, since it raises prices",
                   "It matters little, since retailers add nothing to the produce",
                   "It leads to a general disposition to drunkenness"],
             "c": 0,
             "why": "&ldquo;So far is it from being necessary either to tax them, or to "
                    "restrict their numbers&rdquo;, and competition tends to make them "
                    "&ldquo;both sell cheaper and buy dearer&rdquo; than a monopoly would. "
                    "On alehouses he says the disposition to drink gives employment "
                    "to the alehouses, not the other way round."},
        ],
        "mistakes": [
            ("Reading the ranking as a count of workers on the payroll",
             "Smith counts the productive labour a capital sets in motion, and in the "
             "retailer's case that is the retailer himself, because the capital's main "
             "use is to replace the merchant's. The shop's count in the lab is one hand "
             "from £25, however large the stock on its shelves."),
            ("Taking the lab's count as a test of Smith's order",
             "The shares are written to follow his order. A heavier fixed capital in the "
             "factory or a large fleet in the wholesale trade reverses two of the places in "
             "the second preset. Smith's ranking is a claim about the shares, and "
             "history, not the lab, has to say what they were."),
            ("Reading &ldquo;most advantageous to society&rdquo; as advice to farm",
             "Smith says plainly that owners choose by profit alone: the "
             "&ldquo;different quantities of productive labour which it may put into motion&rdquo; "
             "(and the values they add) &ldquo;never enter into his thoughts&rdquo;, and that in Europe agriculture's "
             "profits &ldquo;seem to have no superiority&rdquo;. His ranking compares "
             "what employments do for the country, and the next lesson shows he does not "
             "expect a policy to put capital where the ranking says."),
        ],
        "standard": (
            "Finish when you can count the labour set going by equal capitals and say what "
            "the ranking rests on.",
            "Given the part of each of several equal capitals paid to productive hands, "
            "compute the hands set going, order the employments, and say which "
            "premise would reverse a pair of places."
        ),
        "note": (
            "The lab turns stated wage shares into hands and cannot say what the shares "
            "were. Smith's ranking is argued from the nature of each employment and not "
            "from measurement, and the figures in both presets are written for this "
            "lesson. The ranking's critics, Ricardo, List, Marx, are disputing either the "
            "premise about Nature's share or the use to which the order is put."
        ),
    },
    # ---------------------------------------------------------------- 05
    # PSU text l. 11950-12230 (Book II, Chapter 5, rest). l. 11951-11963 (China,
    # Egypt, Indostan); l. 11964-12010 (the home trade and the foreign trade of
    # consumption; twelve and twenty-four); l. 12011-12074 (the round-about trade);
    # l. 12075-12115 (the carrying trade); l. 12116-12130 (the policy);
    # l. 12131-12164 (tobacco); l. 12165-12196 (carrying trade the effect, not
    # the cause); l. 12197-12227 (private profit; agriculture; Books III and IV).
    {
        "slug": "home-foreign-and-carrying-trade",
        "title": "The Home, the Foreign and the Carrying Trade",
        "module": "Book II, Chapter 5, second part · Of the different Employment of Capitals",
        "one_line": "A capital in the home trade returns more often and replaces two home capitals each time, so it gives more encouragement to home industry than the same capital in a distant foreign trade or the carrying trade.",
        "summary": (
            "Smith ranks the three branches of wholesale trade: the home trade first, the "
            "foreign trade of consumption second, the carrying trade last. Compute the "
            "labour an equal capital supports in each from its returns a year and the "
            "home capitals each return replaces, reproduce Smith's four-and-twenty to "
            "one, and read what he says policy should and should not do about it."
        ),
        "key": [
            "home trade: two capitals replaced a return",
            "foreign trade: one home capital replaced",
            "home capital = capital × returns a year",
            "four returns against one in three years: 12",
            "twelve returns, twice the effect: 24",
        ],
        "key_label": "Three trades in five lines",
        "concepts_intro": (
            "The second half of Chapter 5 has one calculation and one policy, and the "
            "calculation has two factors."
        ),
        "concepts": [
            ("Two capitals or one",
             "A home trade replaces two capitals employed at home each time it "
             "operates. A foreign trade of consumption replaces one, because the other "
             "belongs to the foreign country; a carrying trade replaces none at home, "
             "and only its profits return."),
            ("How often the capital returns",
             "Home returns come in within the year, sometimes three or four times; "
             "foreign returns seldom within a year, sometimes not for two or three. A "
             "capital that returns oftener supports more labour in a year."),
            ("Natural flow, not forcing",
             "Each branch is advantageous and unavoidable when it arises naturally, "
             "and Smith says policy should neither force nor allure capital into the "
             "remoter ones."),
        ],
        "read_title": "Two capitals, twelve returns, and the Dutch carrier",
        "read_intro": (
            "The chapter's last pages are arithmetic and a verdict on policy, and the "
            "verdict leans on a figure that is easy to misread."
        ),
        "body": [
            ("p", "<strong>Book II, Chapter 5.</strong> &ldquo;The capital which is "
                  "employed in purchasing in one part of the country, in order to sell in "
                  "another, the produce of the industry of that country, generally "
                  "replaces, by every such operation, two distinct capitals, that had both "
                  "been employed in the agriculture or manufactures of that "
                  "country&rdquo;. Wholesale trade, Smith says, is of three sorts: the "
                  "home trade, buying in one part of the country and selling in another; "
                  "the foreign trade of consumption, buying foreign goods for home use; "
                  "and the carrying trade, carrying the surplus produce of one foreign "
                  "country to another."),
            ("p", "The first factor. &ldquo;The capital which sends British goods to "
                  "Portugal, and brings back Portuguese goods to Great Britain, replaces, "
                  "by every such operation, only one British capital. The other is a "
                  "Portuguese one.&rdquo; So &ldquo;Though the returns, therefore, of the "
                  "foreign trade of consumption, should be as quick as those of the home "
                  "trade, the capital employed in it will give but one half of the "
                  "encouragement to the industry or productive labour of the "
                  "country.&rdquo;"),
            ("p", "The second factor is speed. &ldquo;The returns of the home trade "
                  "generally come in before the end of the year, and sometimes three or "
                  "four times in the year. The returns of the foreign trade of consumption "
                  "seldom come in before the end of the year, and sometimes not till "
                  "after two or three years.&rdquo; Four returns a year against one "
                  "in three years is twelve to one, which is Smith's number: &ldquo;A "
                  "capital, therefore, employed in the home trade, will sometimes make "
                  "twelve operations, or be sent out and returned twelve times, before a "
                  "capital employed in the foreign trade of consumption has made "
                  "one.&rdquo; Put the two factors together: &ldquo;If the capitals are "
                  "equal, therefore, the one will give four-and-twenty times more "
                  "encouragement and support to the industry of the country than the "
                  "other.&rdquo;"),
            ("p", "The lab shows it. Record the capital as the home capital replaced at "
                  "each return, which is where the first factor goes in: the home trade "
                  "of £1,000 replaces two home capitals of £1,000 and is entered as "
                  "£2,000, the foreign trade of £1,000 as £1,000. The returns a year are "
                  "4 for the home trade and 1/3 for the foreign. At a keep of £25 a hand "
                  "the home trade supports 320 and the foreign trade about 13.3, and the "
                  "ratio is 24. The figures of 4 and 1/3 are Smith's own and the capital "
                  "of £1,000 and the keep are written for this lesson. In the second "
                  "preset the foreign trade returns once a year, and the ratio falls to 8."),
            ("p", "The round-about trade, where the foreign goods are bought with other "
                  "foreign goods, is worse again, because the final return waits on two or "
                  "three trades: &ldquo;If the hemp and flax of Riga are purchased with the "
                  "tobacco of Virginia, which had been purchased with British "
                  "manufactures, the merchant must wait for the returns of two distinct "
                  "foreign trades&rdquo;. It does not matter if one merchant or three carry "
                  "it on: &ldquo;the final returns of the whole capital employed in the "
                  "trade will be just as slow as ever&rdquo;. Gold and silver as the "
                  "means of purchase make no essential difference, though they cost "
                  "less to carry than any other goods."),
            ("p", "The carrying trade is last. &ldquo;That part of the capital of any "
                  "country which is employed in the carrying trade, is altogether "
                  "withdrawn from supporting the productive labour of that particular "
                  "country, to support that of some foreign countries.&rdquo; His example "
                  "is the Dutch merchant who carries Poland's corn to Portugal and "
                  "Portugal's fruit and wine to Poland: he &ldquo;replaces by every such "
                  "operation two capitals, neither of which had been employed in "
                  "supporting the productive labour of Holland&rdquo;, and &ldquo;The "
                  "profits only return regularly to Holland, and constitute the whole "
                  "addition which this trade necessarily makes to the annual produce of "
                  "the land and labour of that country.&rdquo; The third preset puts the "
                  "three together, with the carrying trade's home capital entered at a "
                  "£100 of freight and profit, written for this lesson: 320 hands for the "
                  "home trade, 40 for the foreign trade at one return a year, and 4 for "
                  "the carrying trade."),
            ("p", "Smith does not say that the remoter trades are bad. The tobacco case "
                  "is his proof. &ldquo;About 96,000 hogsheads of tobacco&rdquo; a year "
                  "are bought in Virginia and Maryland with British goods, but &ldquo;the "
                  "demand of Great Britain does not require, perhaps, more than "
                  "14,000&rdquo;. &ldquo;If the remaining 82,000, therefore, could not "
                  "be sent abroad, and exchanged for something more in demand at home, the "
                  "importation of them must cease immediately&rdquo;, and with it the "
                  "labour of all the people making what bought them. So &ldquo;The most "
                  "round-about foreign trade of consumption, therefore, may, upon some "
                  "occasions, be as necessary for supporting the productive labour of "
                  "the country, and the value of its annual produce, as the most "
                  "direct.&rdquo; And the carrying trade is &ldquo;the natural effect and "
                  "symptom of great national wealth; but it does not seem to be the natural "
                  "cause of it&rdquo;, which Holland, the richest country in Europe for "
                  "its size, and also the greatest carrier, illustrates. Statesmen who "
                  "favour it have &ldquo;mistaken the effect and symptom for the "
                  "cause&rdquo;. The argument that the carrying trade breeds sailors "
                  "fares no better. The coal trade from Newcastle to London &ldquo;employs "
                  "more shipping than all the carrying trade of England&rdquo;."),
            ("p", "The policy follows. The riches and power of a country are in "
                  "proportion to its annual produce, and its political economy ought "
                  "&ldquo;to give no preference nor superior encouragement to the foreign "
                  "trade of consumption above the home trade, nor to the carrying trade "
                  "above either of the other two. It ought neither to force nor to allure "
                  "into either of those two channels a greater share of the capital of the "
                  "country, than what would naturally flow into them of its own "
                  "accord.&rdquo;"),
            ("p", "The last page asks what does move capital. &ldquo;The consideration "
                  "of his own private profit is the sole motive which determines the owner "
                  "of any capital to employ it either in agriculture, in manufactures, or "
                  "in some particular branch of the wholesale or retail trade.&rdquo; The "
                  "quantities of labour it sets going &ldquo;never enter into his "
                  "thoughts&rdquo;. Where agriculture is the most profitable employment, "
                  "capitals will go to it, and so be employed as is best for society; but "
                  "the profits of agriculture &ldquo;seem to have no superiority over "
                  "those of other employments in any part of Europe&rdquo;, and Smith "
                  "will explain in the two following books what in the policy of Europe "
                  "has given the towns so great an advantage over the country. The "
                  "text is plain that the harmony of private profit with the public "
                  "good is conditional, and what the conditions are is the question "
                  "the rest of the book answers. The phrase &ldquo;invisible hand&rdquo; "
                  "appears once in the book, in Book IV, Chapter 2, in a sentence about "
                  "why a merchant prefers the support of domestic to foreign industry, "
                  "and historians have noted how little weight it had for Smith "
                  "compared with the fame it earned later."),
            ("p", "Smith's critics here are three. Ricardo argued, in 1817, that trade "
                  "gains do not depend on how often the capital returns but on the "
                  "difference in costs between countries, so that even the slowest foreign "
                  "trade may enrich both. List argued that Smith's order took no account "
                  "of the power of producing wealth, which an infant industry needs "
                  "protection to build. And Capital's lesson <em>Turnover Time and the "
                  "Number of Turnovers</em> takes up the arithmetic of returns, which "
                  "Marx argues bears on profit as well as on employment; this lesson "
                  "does not repeat it."),
            ("p", "That ends Book II and this course. The next course, <em>The Progress "
                  "of Opulence</em>, starts Book III with Smith's account of how "
                  "the order of employments came out as it did in Europe, with the town "
                  "and the country in the places he describes."),
        ],
        "lab": ("wonkit", {
            "mode": "stock",
            "view": "turnover",
            "money_unit": "£",
            "preset": "smith-twenty-four",
            "presets": [
                {"id": "smith-twenty-four", "label": "Smith's four returns a year against one in three years, the home trade replacing two capitals (the returns are Smith's, the sums written for this lesson)",
                 "trades": [{"trade": "home-trade", "capital": 2000, "returns": 4},
                            {"trade": "foreign-trade-of-consumption", "capital": 1000, "returns": "1/3"}],
                 "wage": 25, "expect": {"wstWork": "home-trade £8,000; foreign-trade-of-consumption £1,000/3 ≈ £333.33", "wstTotal": "£25,000/3 ≈ £8,333.33", "wstLabour": "home-trade 320; foreign-trade-of-consumption ≈ 13.33", "wstOrder": "home-trade, foreign-trade-of-consumption", "wstRatio": "24.00× (home-trade against foreign-trade-of-consumption)"}},
                {"id": "one-a-year", "label": "The foreign trade returning once a year, written for this lesson",
                 "trades": [{"trade": "home-trade", "capital": 2000, "returns": 4},
                            {"trade": "foreign-trade-of-consumption", "capital": 1000, "returns": 1}],
                 "wage": 25, "expect": {"wstWork": "home-trade £8,000; foreign-trade-of-consumption £1,000", "wstTotal": "£9,000", "wstLabour": "home-trade 320; foreign-trade-of-consumption 40", "wstOrder": "home-trade, foreign-trade-of-consumption", "wstRatio": "8.00× (home-trade against foreign-trade-of-consumption)"}},
                {"id": "three-branches", "label": "All three branches, the carrying trade at a £100 of freight and profit (written for this lesson)",
                 "trades": [{"trade": "home-trade", "capital": 2000, "returns": 4},
                            {"trade": "foreign-trade-of-consumption", "capital": 1000, "returns": 1},
                            {"trade": "carrying-trade", "capital": 100, "returns": 1}],
                 "wage": 25, "expect": {"wstWork": "home-trade £8,000; foreign-trade-of-consumption £1,000; carrying-trade £100", "wstTotal": "£9,100", "wstLabour": "home-trade 320; foreign-trade-of-consumption 40; carrying-trade 4", "wstOrder": "home-trade, foreign-trade-of-consumption, carrying-trade", "wstRatio": "80.00× (home-trade against carrying-trade)"}},
            ],
            "panel_title": "Home capital supported in a year",
            "panel_intro": (
                "Each trade is a name, the home capital it replaces at each return (the "
                "home trade's counted twice, the foreign trade's once) and its returns a "
                "year. The lab multiplies, divides by a hand's yearly keep and orders the "
                "trades. The returns in the first preset are Smith's; every sum is "
                "written for the lesson."
            ),
        }),
        "steps_title": "Comparing two trades by the labour they support",
        "steps_intro": "Four steps, and the first is where the home trade's advantage is entered.",
        "steps": [
            ("Count the home capitals replaced at each return",
             "A home trade replaces two, so enter twice the capital. A foreign trade of "
             "consumption replaces one, so enter the capital once. A carrying trade "
             "replaces none at home: enter only the freight and profit."),
            ("Multiply by the returns a year",
             "Home capital replaced in a year is the capital entered times the number of "
             "returns. A return once in three years is 1/3 a year."),
            ("Divide by the keep of a hand",
             "That gives the productive hands supported at home in a year, as in the last "
             "lesson."),
            ("Take the ratio",
             "Divide the larger by the smaller. With Smith's returns and the two home "
             "capitals, the home trade supports 24 times as many."),
        ],
        "worked": {
            "title": "Four-and-twenty to one",
            "intro": [
                "Take the first preset. The returns, 4 a year and 1/3, are Smith's; the "
                "capital of £1,000 and the keep of £25 are written for the lesson. The "
                "home trade replaces two capitals each return.",
            ],
            "lines": [
                "home capital replaced a return:  2 · 1,000 = 2,000",
                "home trade, a year:  2,000 · 4 = 8,000, so 320 hands",
                "foreign trade, a year:  1,000 · 1/3 = 1,000/3, so 40/3 hands",
                "ratio of returns:  4 / (1/3) = 12",
                "ratio of the two:  8,000 / (1,000/3) = 24",
            ],
            "after": [
                "Twelve is the speed and two is the doubling, and the product is "
                "Smith's four-and-twenty. If the foreign trade returned once a year, the "
                "speed ratio would be four and the whole ratio eight, which is the "
                "second preset.",
            ],
        },
        "quiz_title": "Which trade supports more home labour",
        "quiz": [
            {"q": "Why does Smith say the foreign trade of consumption gives only half the "
                  "encouragement of the home trade, if the returns were equally quick?",
             "a": ["Foreign goods are worth less than home goods",
                   "It employs no sailors",
                   "It replaces only one home capital each time; the other replaced is "
                   "the foreign country's",
                   "It is carried on by foreigners"],
             "c": 2,
             "why": "&ldquo;The capital which sends British goods to Portugal, and brings "
                    "back Portuguese goods to Great Britain, replaces, by every such "
                    "operation, only one British capital. The other is a Portuguese "
                    "one.&rdquo; Smith gives no argument from the value of goods or "
                    "from sailors for the half."},
            {"q": "A home-trade capital makes twelve returns for every one the foreign "
                  "trade makes, and replaces twice as many home capitals each time. On "
                  "Smith's reasoning, how many times more encouragement does it give "
                  "the country's industry?",
             "a": ["Twelve times",
                   "Twenty-four times",
                   "Six times",
                   "Thirty-six times"],
             "c": 1,
             "why": "Twelve times the returns and twice the home capitals replaced make "
                    "`12 · 2 = 24`. Twelve leaves out the doubling; six divides by it "
                    "instead of multiplying, and thirty-six is not a product of anything "
                    "in the passage."},
            {"q": "Smith says about 96,000 hogsheads of tobacco are bought a year in "
                  "Virginia and Maryland with British goods and Great Britain needs, "
                  "perhaps, 14,000. How many must be sent abroad again, or the importation "
                  "stops?",
             "a": ["14,000",
                   "96,000",
                   "110,000",
                   "82,000"],
             "c": 3,
             "why": "`96,000 − 14,000 = 82,000`, as Smith says: &ldquo;If the remaining "
                    "82,000, therefore, could not be sent abroad, and exchanged for "
                    "something more in demand at home, the importation of them must "
                    "cease immediately&rdquo;. His conclusion is that the round-about "
                    "trade may be as necessary as the direct."},
            {"q": "What does Smith say is the relation of the carrying trade to a "
                  "country's wealth?",
             "a": ["It is the natural effect and symptom of great national wealth, not "
                   "its cause",
                   "It is the natural cause of great national wealth",
                   "It is the surest way for a poor country to become rich",
                   "It has no connection with national wealth at all"],
             "c": 0,
             "why": "&ldquo;The carrying trade is the natural effect and symptom of great "
                    "national wealth; but it does not seem to be the natural cause of "
                    "it.&rdquo; Statesmen who encourage it have &ldquo;mistaken the effect "
                    "and symptom for the cause&rdquo;."},
        ],
        "mistakes": [
            ("Reading the twenty-four as a measure of how much better the home trade is",
             "It is a product of two assumptions: that the home capital returns four "
             "times a year against one in three years, and that the home trade replaces "
             "two home capitals where the foreign trade replaces one. Change the second "
             "preset's returns to once a year and the ratio is eight. The twenty-four "
             "follows from the chosen returns and is not a constant."),
            ("Thinking Smith wants the foreign and carrying trades discouraged",
             "He says each branch is &ldquo;not only advantageous, but necessary and "
             "unavoidable, when the course of things, without any constraint or "
             "violence, naturally introduces it&rdquo;. His point is that policy "
             "should neither force nor allure capital into them. The tobacco trade is "
             "round-about and necessary."),
            ("Reading his last page as a proof that private profit serves the public",
             "He says private profit &ldquo;is the sole motive&rdquo;, and that when "
             "agriculture is the most profitable employment capitals will go where "
             "they serve society best. Then he says that in Europe it is not, and "
             "promises to explain why. The harmony is conditional, which is why the "
             "book goes on."),
        ],
        "standard": (
            "Finish when you can compute the labour an equal capital supports in the "
            "home and foreign trades and say what Smith draws from it.",
            "Given the returns a year of each trade and the number of home capitals each "
            "return replaces, compute the home capital replaced in a year, the hands it "
            "supports and the ratio between two trades, and state the policy Smith "
            "draws from the ranking."
        ),
        "note": (
            "The ranking is computed from the returns and the replacements the lesson "
            "enters, so the lab cannot say whether home returns were four a year or "
            "foreign ones once in three: Smith states them without evidence. It also "
            "counts only the labour a capital supports at home, which is the one thing "
            "Smith counts, and not the gains from trade that Ricardo and later "
            "economists measure. The sums in all three presets are written for this "
            "lesson, apart from the returns in the first."
        ),
    },
]
