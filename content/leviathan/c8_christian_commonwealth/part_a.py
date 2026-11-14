"""Course 8, lessons 1-4 -- Part III, Chapters 32 to 36.

Every quotation is copied from the operator's copy of the 1651 text (Tuck's
Cambridge edition keeps Hobbes's spelling); the comment beside each lesson
gives its chapter and page. Italics are dropped, nothing else is changed.
Lessons 2 and 3 use the new `levkit`; they are kept as separate constants so
the course can be assembled and previewed without them until the kit is
registered (see __init__.py).
"""

# ------------------------------------------------------------------ 01
# Leviathan ch. 32, 1651 p. 197; PDF p. 353 of the operator's copy.
L1 = {
    "slug": "the-principles-of-christian-politics",
    "title": "The Principles of Christian Politics",
    "module": "Chapter 32 · Of the Principles of Christian Politiques",
    "one_line": "Hobbes keeps reason and adds Scripture, and says a prophet is known by two marks together: a miracle and the established doctrine.",
    "summary": (
        "Chapter 32 opens Part III. Hobbes has reasoned from nature and definitions; now "
        "he must reason from what God has revealed, and he asks first how anyone can know "
        "that a man who says God spoke to him is telling the truth. His answer is two "
        "marks of a true prophet, to be found together. Treat that answer as a "
        "conjunction and test five candidates against it."
    ),
    "key": [
        "acknowledged = miracle and right doctrine",
        "either mark alone does not suffice",
        "a miracle without the doctrine: no",
        "the doctrine without a miracle: no",
        "no miracles now: Scripture in their place",
    ],
    "key_label": "The two marks in five lines",
    "concepts_intro": (
        "The chapter is short and does three jobs. It says what Part III will rest on, "
        "it says why one man's claim to revelation cannot bind another, and it gives the "
        "test that is meant to settle what is left."
    ),
    "concepts": [
        ("Reason is kept",
         "Part III will rest on the prophetic word of God as well as the natural one, "
         "but Hobbes insists that we do not &ldquo;renounce our Senses, and Experience&rdquo;. "
         "Reason is a talent put into our hands to trade with, and he will not have it "
         "folded up in a napkin. Where Scripture is above reason he says it is not against "
         "it, and where it seems so he blames our interpretation or our reasoning. To "
         "&ldquo;captivate&rdquo; the understanding, he explains, is not to hand one's "
         "intellect to another man but to give the will to obedience, where obedience is due."),
        ("A private revelation binds only its owner",
         "If a man says God spoke to him, Hobbes asks what he can offer you that should "
         "oblige you to believe it. A dream is a dream, a vision is a dream between waking "
         "and sleeping, and inspiration is a strong feeling for which he can give no "
         "natural reason. God can speak by any of these, Hobbes allows, but he &ldquo;obliges "
         "no man to beleeve he hath so done to him that pretends it&rdquo;. A sovereign may "
         "require outward obedience; no one can require you to think otherwise than your "
         "reason persuades you."),
        ("Two marks, together, and then none",
         "Prophets contradict each other: of four hundred whom the king of Israel "
         "consulted, one was true. So Scripture must supply a test, and Hobbes finds two "
         "marks, a miracle and teaching no other religion than the one already "
         "established. Neither suffices alone. And since miracles have ceased, no private "
         "man's claim can now meet the test; Scripture takes the place of prophecy."),
    ],
    "read_title": "The passage first, then the chapter line by line",
    "read_intro": (
        "The sentence that gives the test comes after Hobbes has raised the objection to "
        "it himself, so the passage is worth reading with the question in front of it: if "
        "one prophet can deceive another, how does anyone know?"
    ),
    "body": [
        ("p", "<strong>Chapter 32.</strong> &ldquo;To which I answer out of the Holy "
              "Scripture, that there be two marks, by which together, not asunder, a true "
              "Prophet is to be known. One is the doing of miracles; the other is the not "
              "teaching any other Religion than that which is already established. Asunder "
              "(I say) neither of these is sufficient.&rdquo;"),
        ("p", "Where does a book about sovereignty suddenly find itself needing a theory of "
              "prophets? Think of England when Hobbes wrote. He began the book in Paris, "
              "where he had gone in 1640 as the quarrel between Charles I and Parliament "
              "turned dangerous, and it was printed in 1651, after a civil war and a king's "
              "execution. In those years men and women on every side said that the Spirit "
              "had told them what to do, and preachers, soldiers and pamphleteers claimed "
              "authority on that ground. Hobbes has spent two Parts showing that peace "
              "needs a single sovereign judge. Part III has to deal with the one claim that "
              "seems to outrank him: that God has spoken to me, and I must obey God rather "
              "than man."),
        ("p", "He begins by saying what he is doing. Until now he has argued &ldquo;from "
              "the Principles of Nature onely&rdquo;, from experience of men and from "
              "definitions. The Christian commonwealth depends on revelation, so the "
              "ground of the discourse must also be the prophetic word. But reason stays "
              "in the room. We are, he says, not to renounce our senses and experience, "
              "since they are &ldquo;the talents which he hath put into our hands to "
              "negotiate&rdquo; and are &ldquo;not to be folded up in the Napkin of an "
              "Implicite Faith&rdquo;. He allows that many things in God's Word are above "
              "reason, that is, they can be neither demonstrated nor refuted by it; what he "
              "denies is that anything in it is contrary to reason."),
        ("p", "Then comes a sentence that people often misread. When Scripture bids us "
              "&ldquo;captivate&rdquo; our understanding, Hobbes says, it means no "
              "&ldquo;Submission of the Intellectual faculty, to the Opinion of any other "
              "man; but of the Will to Obedience, where obedience is due&rdquo;. He gives "
              "a reason: sense, memory, understanding, reason and opinion are not in our "
              "power to change, so they cannot be what is commanded. What can be commanded "
              "is that we forbear contradiction, speak as lawful authority bids, and live "
              "accordingly. That is how he can stay a believer in Scripture and a defender "
              "of the sovereign's right to command outward acts, in one move."),
        ("p", "Now the problem. God may speak to a man immediately, or through another man "
              "to whom he spoke immediately. Those to whom he has spoken know well enough "
              "what that is; no one else does. If a man claims a dream, Hobbes says, he is "
              "claiming that he dreamed that God spoke, which would not persuade anyone who "
              "knows that dreams are mostly natural. A voice or a vision is a dream "
              "between sleeping and waking; inspiration is an ardent desire to speak, or a "
              "strong opinion of oneself, for which he &ldquo;can alledge no naturall and "
              "sufficient reason&rdquo;. And so God can do all this, yet &ldquo;he obliges "
              "no man to beleeve he hath so done to him that pretends it; who (being a "
              "man) may erre, and (which is more) may lie.&rdquo; A critic could say the "
              "argument proves too much, since the prophets and apostles were themselves "
              "persons who reported such things. Hobbes's reply is the test that follows: "
              "the Scriptures themselves set out how a true prophet is to be known."),
        ("p", "The test is brought in by the case that makes it necessary. Of four hundred "
              "prophets whom the king of Israel consulted before the war at Ramoth Gilead, "
              "he says, &ldquo;only Micaiah was a true one&rdquo;. And a true prophet, "
              "shown to be one by two miracles done in his presence, was deceived by an "
              "old prophet who spoke, as from God, and asked him to a meal. If one prophet deceives another, what certainty is there "
              "except by reason? Hobbes answers with the passage you read first. The "
              "first mark is a miracle. The second is teaching nothing but the religion "
              "already established. He cites Deuteronomy for both: a prophet who works a "
              "miracle and then says, &lsquo;let us follow strange gods&rsquo;, is to be "
              "put to death, because the wonder is God testing Israel's constancy. The "
              "proof that a miracle alone is not enough is in the same book: &ldquo;the "
              "works of the Egyptian Sorcerers, though not so great as those of Moses, yet "
              "were great miracles&rdquo;."),
        ("p", "Hobbes then does something typical of him. He reads the second mark as a "
              "political one. The words &lsquo;revolt from the Lord your God&rsquo; are, in "
              "that place, &ldquo;equivalent to revolt from your King&rdquo;, since Israel "
              "had made God its king by a pact at Sinai and was ruled through Moses. A "
              "miracle that tends to stir up revolt is to be taken as a trial of allegiance. "
              "He finds the same pattern in the New Testament, where Christ warns that false "
              "prophets will do great wonders, and where Paul says an angel from heaven "
              "preaching another gospel is accursed; the gospel in question, Hobbes says, "
              "was that Christ is King."),
        ("p", "The test also cuts the other way. A man who teaches no false doctrine and "
              "shows no miracle is &ldquo;never the more to bee regarded for his "
              "pretence&rdquo;. And a prediction is only a mark if it can be checked: the "
              "miracles that oblige us to believe a prophet, he says, ought to be confirmed "
              "&ldquo;by an immediate, or a not long deferr'd event&rdquo;, since a prophet "
              "can always foretell something that will come to pass one time or other. "
              "The lab turns the test into a conjunction, which is a reading: Hobbes says "
              "neither mark suffices alone and that together they are the only marks "
              "Scripture gives, and the lab takes that as acknowledgment if and only if both "
              "hold."),
        ("p", "Then the conclusion Hobbes draws for his own century: &ldquo;Seeing "
              "therefore Miracles now cease, we have no sign left, whereby to acknowledge "
              "the pretended Revelations, or Inspirations of any private man&rdquo;. "
              "That is one of the places where a reader who thinks Hobbes is hostile to "
              "religion and a reader who thinks he is devout both have something to point "
              "to. He is saying that revelation in the strict sense was real, that its "
              "tests are in Scripture, and that, the tests being unmeetable now, a "
              "private claim to the Spirit has no authority over anyone else. The "
              "objection that comes at once from his contemporaries is aimed at the first "
              "mark and the second together: the apostles and the Reformers taught "
              "something other than the religion established in their day, so a test that "
              "requires agreement with the established religion would have failed them. "
              "Hobbes's own texts answer by fixing what is established: for Israel it is "
              "the law as the sovereign prophet Moses delivered it, and for Christians "
              "the one article that Jesus is the Christ, as Chapter 36 will say. Whether "
              "that reply satisfies is what the disputes of the 1640s were about."),
        ("p", "He closes by saying where the Discourse goes next: the Scripture, from "
              "which &ldquo;all rules and precepts necessary to the knowledge of our duty "
              "both to God and man&rdquo; may be deduced. The next lesson, &ldquo;The Books "
              "of Holy Scripture&rdquo;, asks what Scripture is, who wrote it and what "
              "gives it the force of law."),
        ("p", 'The presets run the same rule five ways. In both, the miracle and the '
              'doctrine are given, and the argument is valid with no counterexample. In '
              'miracle-alone only the miracle is given, and in doctrine-alone only the '
              'sound doctrine: each leaves one counterexample row, so each is invalid, '
              'which is the point that Hobbes says neither mark is sufficient asunder. In '
              'sorcerers the miracle teaches a strange god, and the conclusion that he is '
              'not to be acknowledged follows, with no counterexample. In ceased there is '
              'no miracle, so the conclusion again follows and nobody can be acknowledged: '
              "Hobbes's &ldquo;no sign left&rdquo;."),
    ],
    "lab": ("argkit", {
        "mode": "validity",
        "preset": "both",
        "show": "all",
        "presets": [
            {"id": "both", "label": "Miracle and right doctrine together (A acknowledged, M miracle, D doctrine)",
             "premises": ["A <-> (M & D)", "M & D"], "conclusion": "A",
             "expect": {"vaRows": "8", "vaCounter": "0", "vaVerdict": "Valid"}},
            {"id": "miracle-alone", "label": "A miracle, doctrine unexamined",
             "premises": ["A <-> (M & D)", "M"], "conclusion": "A",
             "expect": {"vaRows": "8", "vaCounter": "1", "vaVerdict": "Invalid"}},
            {"id": "doctrine-alone", "label": "Sound doctrine, no miracle",
             "premises": ["A <-> (M & D)", "D"], "conclusion": "A",
             "expect": {"vaRows": "8", "vaCounter": "1", "vaVerdict": "Invalid"}},
            {"id": "sorcerers", "label": "A miracle that teaches strange gods",
             "premises": ["A <-> (M & D)", "M", "~D"], "conclusion": "~A",
             "expect": {"vaRows": "8", "vaCounter": "0", "vaVerdict": "Valid"}},
            {"id": "ceased", "label": "Miracles have ceased",
             "premises": ["A <-> (M & D)", "~M"], "conclusion": "~A",
             "expect": {"vaRows": "8", "vaCounter": "0", "vaVerdict": "Valid"}},
        ],
        "panel_title": "Two marks as a conjunction",
        "panel_intro": (
            "Each preset is a candidate prophet. A means the claim is to be acknowledged, "
            "M that he has done a miracle, D that he teaches nothing but the religion "
            "established, and the first premise, A if and only if M and D, is the "
            "lesson's reading of Hobbes's two marks. The lab lists every assignment of true "
            "and false and marks those that make all premises true and the conclusion "
            "false. It cannot say whether the reading is Hobbes's."
        ),
    }),
    "steps_title": "Testing a claim to be a prophet",
    "steps_intro": "Four steps, in the order the chapter puts them.",
    "steps": [
        ("State the claim in a letter",
         "Give each thing the candidate offers its own letter: the miracle, the doctrine "
         "he teaches, and the conclusion you are asked to draw, that he is to be "
         "acknowledged as a prophet."),
        ("Write the rule once",
         "Put both marks in one sentence: acknowledged if and only if the miracle and the "
         "right doctrine hold. If the rule is only an 'if', it will say what is enough "
         "but not what is needed; Hobbes says both."),
        ("Add what you know of the candidate",
         "Enter only what has been seen or checked: that a miracle was done, or that "
         "he teaches strange gods. A claim to inspiration goes in as nothing, since it "
         "adds nothing to either mark."),
        ("Look for the counterexample",
         "A row that makes the rule and the known facts true while the conclusion is "
         "false shows that the facts do not settle the case. If there is none, the "
         "conclusion follows."),
    ],
    "worked": {
        "title": "The Egyptian sorcerers",
        "intro": [
            "Take the fourth preset. Pharaoh's magicians turn rods to serpents, so M is "
            "true by Hobbes's own account: their works were &ldquo;great miracles&rdquo;. "
            "But what they serve is Pharaoh's religion against the one Moses brings, so "
            "D is false.",
        ],
        "lines": [
            "premises:  A iff (M and D);  M;  not D",
            "rows:  three letters give 2·2·2 = 8",
            "A = true needs D true, and D is false: no row",
            "so not A holds in every row that fits the premises",
            "counterexamples: 0,  verdict: valid",
        ],
        "after": [
            "Swap the second and third premises for the miracle-alone preset: 'A iff "
            "(M and D)' and M. Now D is not given. One row, A false, M true and D false, "
            "makes the premises true and the conclusion false. That row is the sorcerer "
            "again, and it is why a wonder with no doctrine attached cannot carry you to "
            "'acknowledge him'.",
        ],
    },
    "quiz_title": "Applying the two marks",
    "quiz": [
        {"q": "On the lesson's reading, a man works a wonder nobody can explain and "
              'teaches the established religion. What may you conclude?',
         "a": [
               'Nothing, because a wonder cannot count as a mark',
               'He is to be acknowledged as a true prophet',
               'He is a false prophet, because he has asked for belief',
               'He is to be acknowledged only if he is also the sovereign',
         ],
         "c": 1,
         "why": 'Both marks hold, so the conjunction holds and the lab marks the '
                "argument valid. 'Nothing' contradicts the first mark, which is a "
                "miracle. 'False, because he has asked for belief' is not in the "
                'chapter: Hobbes does not make a claim to be heard a mark against the '
                "claimant. 'Only if he is the sovereign' adds a requirement the chapter "
                'does not state here.'},
        {"q": 'A man teaches exactly the established religion, but has done no '
              'miracle. What does the chapter say about his claim to speak by '
              'immediate revelation?',
         "a": [
               'That he is a true prophet, since his doctrine is sound',
               'That he is a false prophet, since he has no miracle',
               'That his claim is true if he can foretell a distant event',
               'That he is never the more to be regarded for his pretence',
         ],
         "c": 3,
         "why": 'Hobbes says in so many words that a man who teaches no false doctrine '
                "but shows no miracle is not to be regarded for his pretence. 'True, "
                "since his doctrine is sound' ignores the miracle mark, and 'false, "
                "since he has no miracle' turns an absent proof into a proof of "
                "falsehood, which the lab's invalid row shows does not follow. 'True if "
                "he can foretell a distant event' is what Hobbes warns about: a "
                'prediction put off beyond a lifetime cannot be checked.'},
        {"q": "What does the lab show about the fifth preset, 'Miracles have ceased'?",
         "a": [
               'Nobody can be acknowledged as a prophet, whatever he teaches',
               'Everyone can be acknowledged, since the first mark is absent',
               'Nothing, because the premises have no counterexample either way',
               'Only the sovereign can be acknowledged',
         ],
         "c": 0,
         "why": 'With M false the conjunction is false in every row, so A is false in '
                "every row: valid, no counterexample. That is Hobbes's 'no sign left'. "
                "'Everyone can be acknowledged' reverses the rule. 'No counterexample "
                "either way' misreads a valid argument as an empty one. 'Only the "
                "sovereign' is a thesis of other chapters, not a result of this "
                'conjunction.'},
        {"q": "Which step in the chapter's argument does a critic dispute who says "
              'the apostles themselves taught against the religion established in '
              'their time?',
         "a": [
               'The claim that dreams are mostly natural',
               'The claim that Micaiah was one of four hundred',
               "The reading of 'established' in the second mark",
               'The claim that reason is a talent to be used',
         ],
         "c": 2,
         "why": 'The objection is about what counts as the established religion, which '
                'is the second mark. The other three are premises about dreams, about '
                'the story in 1 Kings and about reason, and the objector accepts them '
                'or does not touch them.'},
    ],
    "mistakes": [
        ("Thinking a miracle alone proves the prophet",
         "The sorcerers' works were great miracles, and Deuteronomy tells Israel to put "
         "a wonder-worker who teaches strange gods to death. In the lab's first two "
         "presets the same rule and the same miracle give opposite results, depending "
         "only on the doctrine."),
        ("Reading 'captivate the understanding' as giving up reason",
         "Hobbes says the captivity is of the will to obedience, not the intellect, and "
         "that Scripture is above reason but never against it. A reader who takes the "
         "chapter as a call to stop thinking has the opposite of what is written."),
        ("Thinking Hobbes says God cannot speak to a man",
         "He says God can speak by dreams, visions, voice and inspiration, and that "
         "none of these obliges anyone else to believe the man who reports them. The "
         "limit is on what a report can make others owe, not on what God can do."),
    ],
    "standard": (
        "Finish when you can say why the marks work only together.",
        "Given a candidate prophet's miracle and teaching, state whether the two marks "
        "are met, and name the counterexample that shows one mark alone leaves the "
        "question open."
    ),
    "note": (
        "The lab treats the two marks as a biconditional, which is the lesson's reading; "
        "Hobbes says neither is sufficient alone and that together they are the marks, "
        "and a reader who takes them only as necessary conditions would not get the "
        "valid results shown. It also cannot decide whether any actual claimant did a "
        "miracle or taught the established religion, or whether 'established' means what "
        "Hobbes's chapters take it to mean."
    ),
}

# ------------------------------------------------------------------ 02
# Leviathan ch. 33, 1651 p. 200; PDF p. 357 of the operator's copy.
L2 = {
    "slug": "the-books-of-scripture",
    "title": "The Books of Holy Scripture",
    "module": "Chapter 33 · Of the Books of Holy Scripture",
    "one_line": "A book cannot have been written before the latest event it mentions, and by that test Hobbes finds Moses, Joshua and Samuel were not the last hands on their books.",
    "summary": (
        "Chapter 33 asks what the Scriptures are, who wrote them and what makes them law. "
        "Hobbes answers the second question from the books themselves, by the phrase "
        "'unto this day' and by the latest event each one mentions, and the third by "
        "the sovereign's authority. Date a short list of books with that test and see "
        "which must be later than their traditional authors."
    ),
    "key": [
        "written no earlier than its latest event",
        "'unto this day': written long after",
        "after the author's death: not his last hand",
        "titles name a subject as often as a writer",
        "canon = the books the sovereign makes law",
    ],
    "key_label": "The antiquity test in five lines",
    "concepts_intro": (
        "Chapter 33 has two arguments, one about dates and one about authority, and "
        "they are not the same kind of argument."
    ),
    "concepts": [
        ("The canon is a question of law",
         "The canonical books are those that ought to be the rule of Christian life. "
         "Rules of life that men are bound in conscience to observe are laws, so Hobbes "
         "says the question of Scripture is the question of what is law throughout "
         "Christendom. Since sovereigns are the sole legislators in their dominions, the "
         "books that are canonical are the ones the sovereign establishes."),
        ("The books tell us when, not always who",
         "History is the only proof of matter of fact, and reason serves only to convince "
         "the truth &ldquo;of consequence&rdquo;, so neither names the authors. The light "
         "that remains comes from the books themselves, which cannot tell us every writer "
         "but can give &ldquo;knowledge of the time, wherein they were written&rdquo;: "
         "a writer who says something has remained &ldquo;unto this day&rdquo; is writing "
         "after the event."),
        ("Authority comes from the lawful power, not the writer",
         "Asked from whence the Scriptures derive their authority, Hobbes says the "
         "question should read: by what authority are they made law? Where they agree "
         "with the law of nature they carry their own; otherwise only the commonwealth "
         "can make them law, and the church can do it only if it is the same thing as the "
         "commonwealth. A universal church over all Christians would make every "
         "Christian king a private person."),
    ],
    "read_title": "The passage first, then the chapter line by line",
    "read_intro": (
        "The passage is the best known of Hobbes's arguments from Scripture itself. "
        "Notice that it goes from a single phrase to a conclusion about when the words "
        "were written."
    ),
    "body": [
        ("p", "<strong>Chapter 33.</strong> &ldquo;We read in the last Chapter of "
              "Deuteronomie, ver. 6. concerning the sepulcher of Moses, that no man knoweth "
              "of his sepulcher to this day, that is, to the day wherein those words were "
              "written. It is therefore manifest, that those words were written after his "
              "interrement.&rdquo;"),
        ("p", "Suppose a friend gives you a letter that says it was written in 1900, and the "
              "letter says the new bridge 'still stands to this day'. You would look up "
              "when the bridge was built, then ask how long it had stood. Hobbes does "
              "with the Bible what you would do with the letter. The chapter begins "
              "elsewhere, with the question of which books are the canon, and he is "
              "plain that this is a question of law. But the part you have just read "
              "answers a different question, who wrote the books, and it is answered "
              "with no appeal to anyone's authority."),
        ("p", "His starting points are three. First, no other history tells us who wrote "
              "the books, and &ldquo;History&rdquo;, as he says, is &ldquo;the only proof "
              "of matter of fact&rdquo;. Second, reason will not do it either, because it "
              "convinces us of consequence and not of fact. Third, titles prove little: "
              "&ldquo;in titles of Books, the subject is marked, as often as the "
              "writer&rdquo;. The History of Livy names its author, and the History of "
              "Alexander names its subject, so the five Books of Moses may be books "
              "about Moses, as the Book of Ruth is not by Ruth. That leaves the books "
              "themselves."),
        ("p", "The Pentateuch comes first. The last chapter of Deuteronomy says that no one "
              "knows Moses's grave &ldquo;to this day&rdquo;, so the words were written "
              "after the burial, and it would be a strange interpretation, Hobbes says, "
              "to say Moses spoke of his own sepulchre by prophecy. A defender could say "
              "that only the last chapter is later. So Hobbes goes on: Genesis says "
              "&ldquo;the Canaanite was then in the land&rdquo;, which must be the words "
              "of someone writing when the Canaanite was no longer there, and so not "
              "Moses, who died before he came in. Numbers cites a Book of the Wars of the "
              "Lord, which recorded Moses's acts. His conclusion is moderate: the five "
              "books &ldquo;were written after his time, though how long after it be not "
              "so manifest&rdquo;."),
        ("p", "He does not strip Moses of authorship altogether. Moses did write what the "
              "books say he wrote: the volume of the law in Deuteronomy, chapters 11 to 27, "
              "which was to be written on stones, read to the people every seventh year, "
              "laid in the ark and, having been lost, found again by Hilkiah in the reign "
              "of Josiah. What Hobbes denies is that Moses compiled the books in the "
              "form we have them. He also adds that the phrase &ldquo;unto this day&rdquo; "
              "is one that &ldquo;signifieth a time past, beyond the memory of man&rdquo;. "
              "He finds it in Joshua, for the twelve stones set up in Jordan, for the "
              "name Gilgal and for the valley of Achor; in Judges, where Jonathan's sons "
              "are priests to the tribe of Dan until the captivity; and in Samuel, where "
              "a statute of David's and the name of a place are said to hold &ldquo;to "
              "this day&rdquo;."),
        ("p", "For Kings and Chronicles his argument is different and simpler: the history "
              "is carried down to the captivity in Babylon, and &ldquo;the Facts Registred "
              "are alwaies more ancient than the Register&rdquo;, much more than books "
              "that quote the register. Ezra and Nehemiah mention the return; Esther "
              "belongs to the captivity. For other books he is cautious. Job he takes to "
              "be a treatise on why the wicked prosper, since most of it is in verse; "
              "the Psalter was compiled after the return, because it includes psalms of "
              "that time; and for the New Testament he says its writers lived within an "
              "age of the Ascension but that the books were received by the church "
              "later. That is a historical claim made by textual evidence, and critics "
              "were already making the same kind of argument in the seventeenth "
              "century; Spinoza would later press it at greater length."),
        ("p", "The lab makes the test a calculation. You give each book a traditional "
              "author and his death on a stated scale of years, and each book the events "
              "it mentions, with their years. The latest event is the earliest the book "
              "can have been written. If that comes after the author's death, the "
              "book, as it stands, cannot be wholly his. The numbers are the lab's "
              "illustrative round figures, counted in years from the death of Moses; "
              "the test uses the order of events, not the size of the gaps, and Hobbes "
              "gives no dates."),
        ("p", "The second half of the chapter turns to authority, and it is an argument "
              "with a trap in it for the sovereign's critics. God is the sovereign of "
              "sovereigns and must be obeyed whatever any prince commands, Hobbes agrees; "
              "but the question is not of obedience to God but of &ldquo;what God hath said&rdquo;, which a subject "
              "who has no private revelation can know only by natural reason, that is, by "
              "obeying his commonwealth. So &ldquo;it is not the Writer, but the "
              "authority of the Church, that maketh a Book Canonicall&rdquo;, and the "
              "church, if it is one person, is the commonwealth of Christians. If it "
              "is not one person, it has no will or voice. If it is one commonwealth "
              "over all Christendom, every Christian king is its private subject. "
              "&ldquo;The question truly stated is, By what Authority they are made "
              "Law.&rdquo; Anyone who answers 'the Pope' or 'the Spirit in me' is saying "
              "something about who is sovereign, and Hobbes has already argued about "
              "that."),
        ("p", "That is the argument at its strongest and at its limit. The dating is open "
              "to anyone with a Bible, and many readers have accepted it while rejecting "
              "everything after it. The authority claim is the one the Church of "
              "Rome and the Presbyterian ministers disputed. The next lesson, &ldquo;Spirit, "
              "Angel and Inspiration&rdquo;, takes up the words Chapter 34 says must be "
              "fixed before the Discourse goes on."),
        ("p", 'The presets show the test in use. In moses-joshua the Pentateuch mentions an '
              "event 30 years after Moses's death, and Joshua mentions the stones standing "
              '&ldquo;unto this day&rdquo;, 200 years in, which is 170 years after Joshua '
              'died in year 30; both books are later than their traditional authors. In '
              "samuel the book of Samuel reaches year 700, 300 years after Samuel's death "
              'in year 400, and the Psalms include a psalm of the return from Babylon, year '
              '868, 428 years after David died in year 440; the lab counts both as written '
              'after. In no-test, Job mentions nothing dated, and the lab says it has no '
              'test for it, which is not a finding that Job is early.'),
    ],
    "lab": ("levkit", {
        "mode": "canon",
        "view": "date",
        "preset": "moses-joshua",
        "presets": [
            {"id": "moses-joshua", "label": "Moses and Joshua, years from the death of Moses",
             "books": [
                 ["Pentateuch", "Moses", 0],
                 ["Joshua", "Joshua", 30],
             ],
             "mentions": [
                 ["Pentateuch", "Moses-buried-his-grave-unknown-to-this-day", 0],
                 ["Pentateuch", "the-Canaanite-no-longer-in-the-land", 30],
                 ["Joshua", "twelve-stones-set-up-in-Jordan", 1],
                 ["Joshua", "the-stones-there-unto-this-day", 200],
             ],
             "expect": {"lcnAfter": "2: Pentateuch, Joshua", "lcnGap": "Pentateuch 30 years after Moses's death; Joshua 170 years after Joshua's death", "lcnNoTest": "0: none"}},
            {"id": "samuel", "label": "Samuel and David, with the same scale",
             "books": [
                 ["Samuel", "Samuel", 400],
                 ["Psalms", "David", 440],
             ],
             "mentions": [
                 ["Samuel", "Davids-statute-for-the-spoils", 430],
                 ["Samuel", "Perez-Uzzah-named-and-so-called-to-this-day", 700],
                 ["Psalms", "a-psalm-of-the-return-from-Babylon", 868],
                 ["Psalms", "a-psalm-of-David", 430],
             ],
             "expect": {"lcnAfter": "2: Samuel, Psalms", "lcnGap": "Samuel 300 years after Samuel's death; Psalms 428 years after David's death", "lcnNoTest": "0: none"}},
            {"id": "no-test", "label": "A book with no mention",
             "books": [
                 ["Job", "Job", 0],
             ],
             "mentions": [],
             "expect": {"lcnAfter": "0: none", "lcnGap": "Job no test", "lcnNoTest": "1: Job"}},
        ],
        "panel_title": "Date a book by what it mentions",
        "panel_intro": (
            "Years are counted from the death of Moses, which is year 0; they are round "
            "figures for the lab, not Hobbes's. The lab finds the latest event each book "
            "mentions and says whether that is after the traditional author's death."
        ),
    }),
    "steps_title": "Dating a book from inside it",
    "steps_intro": "Four steps, the same for any text that mentions its own past.",
    "steps": [
        ("Name the traditional author and his death",
         "Write down who the title or tradition says wrote it, and when he died, on "
         "one stated scale. Remember Hobbes's caution that a title may mark a subject "
         "and not a writer."),
        ("List what the book mentions",
         "Collect each event, monument or custom the book refers to as past, with the "
         "date you give it. 'Unto this day' belongs here: it means the event is far "
         "behind the writer."),
        ("Take the latest",
         "A book cannot have been written before the latest thing it mentions. That year "
         "is the earliest the book can have been written, in this form."),
        ("Compare with the author's death",
         "If the latest event is later than the death, the book is not wholly his. If "
         "it is earlier or equal, the test gives no verdict: he may have written it, "
         "and the book may still be later."),
    ],
    "worked": {
        "title": "The books of Moses and of Joshua",
        "intro": [
            "Take the first preset. The scale counts years from the death of Moses. The "
            "lab has two books and four mentions.",
        ],
        "lines": [
            "Pentateuch:  latest event 30  (the Canaanite gone)",
            "Moses died in year 0,  30 > 0: written after",
            "gap:  30 − 0 = 30 years",
            "Joshua:  latest event 200  (the stones, unto this day)",
            "Joshua died in year 30,  200 > 30:  gap 170",
        ],
        "after": [
            "Both books come out as written after their traditional authors. The "
            "burial alone, at year 0, would not: it equals the death and so tells "
            "nothing, which is why Hobbes needs the Canaanite and the "
            "words &lsquo;unto this day&rsquo;. For a book with no mentions the lab prints no "
            "test, as it should: a book is not shown to be early by saying nothing of "
            "its own time.",
        ],
    },
    "quiz_title": "Dating by the book's own words",
    "quiz": [
        {"q": "A book names its author's death as year 100 and mentions events up to "
              'year 300. What does the test say?',
         "a": [
               "It was written in year 100, the year of its author's death",
               'It was written by its author, and the later events were prophecy',
               'It cannot have been written before year 300, so it is later than its author',
               'It was written in year 200, halfway between',
         ],
         "c": 2,
         "why": 'A book cannot predate the latest event it mentions, so it dates from '
                "300 or later. 'Year 100' takes the earliest date for the writing. "
                "'Written by its author, the later events prophecy' is the reading "
                'Hobbes calls a strange interpretation when he says Moses did not speak '
                "of his own sepulchre by prophecy. 'Year 200' is not a result of the "
                'test.'},
        {"q": "Why does Hobbes say 'the Book of Ruth' proves nothing about who wrote "
              'Ruth?',
         "a": [
               'Ruth lived long before the Book was written',
               'Hebrew books have no authors',
               'In titles of books the subject is marked as often as the writer',
               'The title was added by the sovereign',
         ],
         "c": 2,
         "why": "That is the sentence. 'Ruth lived long before the Book was written' is "
                'a conclusion some readers would draw but Hobbes does not give it for '
                "Ruth. Neither 'Hebrew books have no authors' nor 'the sovereign added "
                "the title' is in the chapter."},
        {"q": 'What does Hobbes say makes a book canonical?',
         "a": [
               'The authority of the lawful power that makes it law',
               'That its writer was inspired',
               'That it was written by an apostle or prophet',
               'That it was received by every private believer',
         ],
         "c": 0,
         "why": 'He says those books only are canonical that are established as such by '
                'the sovereign authority, and that it is the authority of the church, '
                'which is a commonwealth of Christians, and not the writer that makes a '
                'book canonical. Inspiration, authorship by a prophet and private '
                'belief are the other candidates he sets aside.'},
    ],
    "mistakes": [
        ("Thinking the test shows who did write the book",
         "It only shows a book is later than the latest thing it mentions. It does not "
         "say who the real writer was, and Hobbes himself says the books do not name "
         "every writer. The lab prints a verdict about dates, never about people."),
        ("Thinking Hobbes denies Moses wrote anything",
         "He says Moses wrote what he is said to have written, such as the volume of the "
         "law in Deuteronomy, and denies only that he compiled the five books as we "
         "have them. In the lab the first preset's gap is a gap between Moses and the "
         "last hand, not a claim that there was no first one."),
        ("Reading the second half as another dating argument",
         "The authority argument is not about when. It says a rule of life is law only "
         "when a lawful power makes it so, and that the church is such a power only if it "
         "is the commonwealth. A reader who has accepted the dates has not thereby "
         "accepted that."),
    ],
    "standard": (
        "Finish when you can date a book from its own mentions.",
        "Given a book, its traditional author's death and the events it mentions, find the "
        "latest event, say whether the book is later than the author's death, and say "
        "what the test cannot show."
    ),
    "note": (
        "The dates are the lab's round figures and Hobbes gives none. The lab shows that "
        "if the events are as dated, the books are later than their traditional "
        "authors; it cannot show that the dates are right, who wrote the books, or that "
        "the sovereign has the authority over the canon that the second half of the chapter "
        "claims. Defenders of Mosaic authorship answered then, as now, that later hands "
        "added notes to an original that was Moses's."
    ),
}

# ------------------------------------------------------------------ 03
# Leviathan ch. 34; PDF p. 366 of the operator's copy.
L3 = {
    "slug": "spirit-angel-and-inspiration",
    "title": "Spirit, Angel and Inspiration",
    "module": "Chapter 34 · Of the Signification of Spirit, Angel, and Inspiration",
    "one_line": "Hobbes takes body, substance and spirit as names with definitions, and finds that 'incorporeal substance' adds names that cancel.",
    "summary": (
        "Chapter 34 fixes the meaning of the words Scripture uses before anything is "
        "inferred from it. Body and substance, Hobbes says, name the same thing, so "
        "'incorporeal substance' destroys itself; spirit means a thin body or an image "
        "of the fancy or, figuratively, a disposition; angels are messengers; "
        "inspiration is a metaphor. Reckon eight claims from those definitions and see "
        "which are true, false or absurd."
    ),
    "key": [
        "body = what fills some room",
        "substance and body: the same thing",
        "spirit: a thin body, or an idol of the brain",
        "an angel: a messenger",
        "incorporeal substance: names that cancel",
    ],
    "key_label": "Hobbes's definitions in five lines",
    "concepts_intro": (
        "Hobbes called reasoning a reckoning with names (Chapter 5). This chapter does "
        "that reckoning on the words of religion."
    ),
    "concepts": [
        ("Body and substance",
         "Body, in its most general sense, &ldquo;filleth, or occupyeth some certain "
         "room&rdquo;, and is a real part of the universe. The same thing is called "
         "substance when we think of it as subject to changes, which are its accidents. "
         "So substance and body signify one thing, and &lsquo;incorporeal substance&rsquo; is "
         "like &lsquo;an incorporeal body&rsquo;."),
        ("Spirit, in two senses and some figures",
         "Common speech calls thin things we feel as wind or breath spirits, and "
         "so spirit in its proper sense is either a subtle, fluid, invisible body or a "
         "ghost or other phantasm of the imagination. Hobbes lists a number of "
         "figurative uses, for dispositions, gifts of understanding, zeal and so on, "
         "and says no other meaning for the word can be found."),
        ("Angels and inspiration",
         "An angel is a messenger, most often God's, and what makes one is its use, "
         "not its shape. In most Old Testament places it is an image raised in the "
         "fancy or a voice; Hobbes also grants, against his own earlier leaning, that "
         "the New Testament forces him to admit angels that are substantial and "
         "permanent. Inspiration, taken properly, would be the blowing of air into a man; "
         "in Scripture it is a metaphor."),
    ],
    "read_title": "The passage first, then the chapter line by line",
    "read_intro": (
        "The sentence to read is the one where the argument is a single piece of "
        "reckoning: two names put together, and the result."
    ),
    "body": [
        ("p", "<strong>Chapter 34.</strong> &ldquo;Substance incorporeall are words, which "
              "when they are joined together, destroy one another, as if a man should say, "
              "an Incorporeall Body.&rdquo;"),
        ("p", "That sentence is the whole of the argument in miniature, and it makes sense "
              "only after the reckoning that comes before it. Hobbes has said in "
              "Chapter 5 that to reason is to add and subtract names; this is a sum that "
              "does not add up. In the chapter he explains why he begins here: the "
              "foundation of all true ratiocination is the constant signification of "
              "words, and in the doctrine that follows the meaning of a word depends "
              "neither on the writer's will nor on common use but on the sense it carries "
              "in Scripture. He proposes to settle the meaning of body and spirit, which "
              "&ldquo;in the language of the Schools are termed, Substances, Corporeall, "
              "and Incorporeall&rdquo;."),
        ("p", "He starts with body: &ldquo;that which filleth, or occupyeth some certain "
              "room, or imagined place&rdquo;, which does not depend on the imagination "
              "and is a real part of the universe, the aggregate of all bodies. Bodies "
              "are subject to change, and in that guise they are called substances. "
              "&ldquo;Substance and Body, signifie the same thing&rdquo;, hence the "
              "sentence you read first. Hobbes then admits the ordinary use of the word. "
              "Common people call body only what they can feel resist or see, and "
              "they call air and breath by the name of spirit, because the Latin "
              "<em>spiritus</em> means breath. In that vulgar sense, he says, an "
              "incorporeal substance is not nothing: it is &ldquo;a thin Substance "
              "Invisible, but that hath the same dimensions that are in grosser "
              "Bodies&rdquo;. The word is not the trouble; the trouble is a sense of "
              "&lsquo;incorporeal&rsquo; that means no body at all."),
        ("p", "Spirit has a second meaning, and he insists that the two be kept apart. "
              "Sometimes it is a ghost or other idol of the brain, seen in a dream or in "
              "a looking-glass, of which he says the apostle says they are nothing. "
              "&ldquo;The proper signification of Spirit in common speech, is either a "
              "subtile, fluid, and invisible Body, or a Ghost, or other Idol or Phantasme "
              "of the Imagination.&rdquo; Beyond these there are, he says, many "
              "metaphorical senses: a disposition, a gift of wisdom, an unexpected zeal, "
              "the gift of prediction in dreams and visions, life, subordination to "
              "authority. He then goes through the passages one by one. When the Spirit "
              "of God moved on the waters it is a wind; when Pharaoh calls Joseph's "
              "wisdom the Spirit of God it is a gift; when God takes of the Spirit "
              "that is on Moses and gives it to seventy elders, it is a mind conformable "
              "to Moses's. &ldquo;Other signification of Spirit I find no where any.&rdquo; "
              "Where none will serve, the place falls outside human understanding "
              "and, he says, belief there is submission, not opinion."),
        ("p", "Angels get the same treatment. The word means a messenger, and what makes "
              "something an angel is &ldquo;not the shape; but their use&rdquo;, which is "
              "to signify God's presence in a supernatural work. A pillar of cloud is an "
              "angel no less than a man with wings would be. In Genesis the same "
              "apparition is called an angel of the Lord and God; a voice from heaven "
              "stays Abraham's hand; Jacob's ladder is a dream. His first conclusion was "
              "that angels were nothing but supernatural apparitions of the fancy. Then he "
              "turns: the New Testament, in places where there is no suspicion of "
              "corruption, &ldquo;have extorted from my feeble Reason, an acknowledgment, "
              "and beleef, that there be also Angels substantiall, and permanent&rdquo;. "
              "A permanent angel is, on his definitions, a body, subtle as it may be. "
              "What cannot be shown from Scripture, he says, is that angels are in no "
              "place; and to say they are incorporeal in that sense is &ldquo;to say in "
              "effect, there is no Angel nor Spirit at all&rdquo;."),
        ("p", "Inspiration follows from spirit. Taken properly, it is blowing thin air into a "
              "man as one fills a bladder, or else the blowing in of a phantasm, which is "
              "impossible since a phantasm is not a thing. So it is a metaphor: when Genesis "
              "says God inspired the breath of life, it means he gave life; when Paul says "
              "all Scripture is given by inspiration, it means God inclined the writers' "
              "minds. The graces of God, he says, &ldquo;are Vertues, not Bodies to be "
              "carryed hither and thither, and to be powred into men, as into "
              "barrels&rdquo;. The same applies to the Holy Ghost at Pentecost, where the "
              "wind is a sign, not the Spirit."),
        ("p", "It would be easy to read this chapter as a materialist's attack on religion, "
              "and some of Hobbes's contemporaries did. It reads differently from the "
              "inside. His account has God a Spirit in a sense we do not understand, for "
              "God's nature is incomprehensible, and the attributes we give him are "
              "honours, not descriptions. The target is a philosophical word, "
              "&lsquo;incorporeal substance&rsquo;, which he says belongs to the Schools and "
              "comes from the Gentiles' notion of demons, and not any text of Scripture. "
              "The strongest reply to him comes from the philosophers who took the "
              "other side. Henry More and the Cambridge Platonists held that a spirit "
              "may occupy room and yet not be a body, because it is penetrable, which "
              "bodies are not. If that is allowed, &lsquo;body&rsquo; cannot simply be "
              "&lsquo;whatever fills room&rsquo;, and the definition from which Hobbes's "
              "sum is reckoned is the premise in dispute."),
        ("p", "The lab does the reckoning and leaves that dispute alone. It takes a handful "
              "of Hobbes's definitions as given, expands each name into the simple names "
              "that make it up, and gives each claim a verdict. A claim is true if "
              "everything in the predicate is in the subject, absurd if the two together "
              "contain names that cannot be added, and insignificant if it uses a name "
              "that has no definition, which is how the lab says a name stands for "
              "nothing. The simple names, 'extended' and 'unextended', are the lesson's "
              "way of writing Hobbes's body and the Schools' incorporeal, and are not "
              "his own terms."),
        ("p", "The next lesson, &ldquo;The Kingdom of God and the Word of God&rdquo;, "
              "takes the chapters in which the fixing of words is put to political use."),
        ("p", 'The one preset, hobbes, holds all nine claims at once. On the definitions as '
              'written the lab gives three true, two false, three absurd and one '
              'insignificant: the three that a subtle spirit is a body and a substance, and '
              'that an angel of subtle body is a spirit, are true; that an apparition is a '
              'body, and that a ghost is a body, are false; the three that put incorporeal '
              'with substance or with a body are absurd; and &ldquo;inspiration is '
              'infusion&rdquo; is insignificant because neither word is defined or simple.'),
    ],
    "lab": ("levkit", {
        "mode": "reckon",
        "view": "names",
        "preset": "hobbes",
        "presets": [
            {"id": "hobbes", "label": "Hobbes's definitions of body, spirit and angel",
             "simple": ["extended", "real", "thin", "invisible", "unextended", "imagined", "messenger"],
             "defs": [
                 ["body", "extended real"],
                 ["substance", "body"],
                 ["subtle-spirit", "body thin invisible"],
                 ["incorporeal", "unextended"],
                 ["incorporeal-substance", "incorporeal substance"],
                 ["ghost", "imagined"],
                 ["angel-apparition", "messenger ghost"],
                 ["angel-body", "messenger subtle-spirit"],
             ],
             "opposed": [["extended", "unextended"]],
             "claims": [
                 ["a-subtle-spirit-is-a-body", "subtle-spirit", "body"],
                 ["a-subtle-spirit-is-a-substance", "subtle-spirit", "substance"],
                 ["an-angel-of-flesh-thin-body-is-a-spirit", "angel-body", "subtle-spirit"],
                 ["an-angel-that-is-an-apparition-is-a-body", "angel-apparition", "body"],
                 ["a-ghost-is-a-body", "ghost", "body"],
                 ["an-angel-in-a-body-is-incorporeal", "angel-body", "incorporeal"],
                 ["a-substance-is-incorporeal", "substance", "incorporeal"],
                 ["an-apparition-is-an-incorporeal-substance", "angel-apparition", "incorporeal-substance"],
                 ["inspiration-is-infusion", "inspiration", "infusion"],
             ],
             "expect": {"lrkCounts": "3 true, 2 false, 3 absurd, 1 insignificant", "lrkTrue": "3: a-subtle-spirit-is-a-body, a-subtle-spirit-is-a-substance, an-angel-of-flesh-thin-body-is-a-spirit", "lrkFalse": "2: an-angel-that-is-an-apparition-is-a-body, a-ghost-is-a-body", "lrkAbsurd": "3: an-angel-in-a-body-is-incorporeal, a-substance-is-incorporeal, an-apparition-is-an-incorporeal-substance", "lrkEmpty": "1: inspiration-is-infusion"}},
        ],
        "panel_title": "Reckon what follows from the definitions",
        "panel_intro": (
            "Names are defined as sums of other names, down to simple names. A claim is "
            "true when the subject contains the whole predicate, and absurd when the "
            "names together include a pair that cannot be added. Change a definition and "
            "watch the verdicts."
        ),
    }),
    "steps_title": "Reckoning on definitions",
    "steps_intro": "Four steps, the same on any set of defined words.",
    "steps": [
        ("Write each definition as a sum",
         "State each word as the names it is made of, down to simple names that are "
         "left undefined. Hobbes does this for body, substance and spirit."),
        ("Name the pairs that cannot be added",
         "List the simple names that exclude each other, such as extended and "
         "unextended. The lesson's choice of pair is the premise that matters."),
        ("Expand and compare",
         "Replace each word by its simple names. A claim of the form 'S is P' is true "
         "if all of P's simple names are among S's."),
        ("Check for absurdity and emptiness",
         "If S, P or their sum contains an excluded pair, the claim is absurd; if a "
         "name has no definition and is not simple, the claim is insignificant. "
         "Otherwise a claim that is not true is simply false."),
    ],
    "worked": {
        "title": "Why an incorporeal substance cancels",
        "intro": [
            "Take 'a substance is incorporeal'. Substance is defined as body, and body "
            "as extended and real; incorporeal is defined as unextended.",
        ],
        "lines": [
            "substance = body = extended + real",
            "incorporeal = unextended",
            "sum:  extended + real + unextended",
            "extended and unextended cannot be added",
            "verdict: absurd",
        ],
        "after": [
            "Compare 'a subtle spirit is a body'. Subtle spirit is body, thin and "
            "invisible, so every simple name of body is in it, and the claim is true. "
            "'A ghost is a body' is false and not absurd: a ghost is just 'imagined', "
            "which lacks extended and real but adds nothing that clashes. Hobbes's "
            "own verdict on ghosts is harsher, that they are nothing; the lab shows only "
            "what the lesson's definitions give.",
        ],
    },
    "quiz_title": "Reading the verdicts",
    "quiz": [
        {"q": "On the lesson's definitions, which claim is true?",
         "a": [
               'A substance is incorporeal',
               'A ghost is a body',
               'An angel in a body is incorporeal',
               'A subtle spirit is a substance',
         ],
         "c": 3,
         "why": 'A subtle spirit contains body, and substance is defined as body, so it '
                "contains all of substance. 'A substance is incorporeal' and 'An angel "
                "in a body is incorporeal' put extended with unextended and are absurd. "
                "'A ghost is a body' is false, since a ghost is only imagined."},
        {"q": 'Which of these does the lab call absurd and not merely false?',
         "a": [
               'An apparition is a body',
               'An apparition is an incorporeal substance',
               'A ghost is a body',
               'A body is extended',
         ],
         "c": 1,
         "why": "'Incorporeal substance' contains both extended and unextended, so any "
                "claim that uses it is absurd. 'An apparition is a body' and 'A ghost "
                "is a body' are false but contain no clashing pair. 'A body is "
                "extended' is true."},
        {"q": "What does Hobbes allow, in this chapter, about the word 'incorporeal'?",
         "a": [
               'It is always meaningless in Scripture',
               'It means an image of the fancy and nothing else',
               'It names angels and no other thing',
               'In the vulgar sense it may mean a thin invisible substance, which is real',
         ],
         "c": 3,
         "why": 'He says that if corporeal is taken for what we perceive by the '
                'external senses, then incorporeal substance is a thin invisible '
                'substance with the same dimensions as grosser bodies. What he denies '
                "is the sense 'not body'. The other answers are not what he says."},
        {"q": "Which premise is the one a reply such as Henry More's would reject?",
         "a": [
               'That angels are messengers',
               'That whatever occupies room is a body',
               'That inspiration is a metaphor in Scripture',
               'That reasoning is a reckoning with names',
         ],
         "c": 1,
         "why": 'More held that a spirit may occupy room and be penetrable. That denies '
                'that occupying room makes a thing a body. The other three are not what '
                'that reply is directed at.'},
    ],
    "mistakes": [
        ("Thinking Hobbes says there are no angels",
         "He says that angels in the Old Testament are mostly messengers appearing in "
         "dreams and visions, but that the New Testament, as he reads it, has made him "
         "believe in angels that are substantial and permanent. What he rejects is that "
         "they are in no place. The lab's claim 'an angel in a body is incorporeal' is "
         "absurd for that reason."),
        ("Calling 'absurd' a verdict that something is false",
         "In the lab a claim is false when its parts simply fail to match, and absurd when "
         "it adds names that cannot be added. 'A ghost is a body' is false; 'a substance is "
         "incorporeal' is absurd. Hobbes's own distinction between a false and an "
         "insignificant speech is the same kind."),
        ("Reading the definitions as the lab's discovery",
         "They are Hobbes's, taken as the lesson states them. The lab computes what "
         "follows, and one definition, that body is what fills room, carries nearly all "
         "of the result. Whether it is right is the philosophers' question."),
    ],
    "standard": (
        "Finish when you can show why one word-sum cancels.",
        "Given definitions of body, substance and incorporeal, expand a claim into "
        "simple names and decide whether it is true, false or absurd."
    ),
    "note": (
        "The lab computes from the lesson's list of definitions and simple names, and "
        "everything depends on that list, above all on counting extension as the mark "
        "of body. It cannot say whether spirits exist, what Scripture means by them, or "
        "whether a critic is right that a thing may fill room without being a body."
    ),
}

# ------------------------------------------------------------------ 04
# Leviathan ch. 35, 1651 p. 218; PDF p. 378 of the operator's copy.
L4 = {
    "slug": "the-kingdom-of-god-and-the-word",
    "title": "The Kingdom of God and the Word of God",
    "module": "Chapters 35 and 36 · Of the Kingdome of God, and of the Word of God, and of Prophets",
    "one_line": "The kingdom of God is a civil kingdom over Israel, and one fulfilled prophecy from one of four hundred and one raises the odds a prophet is true only to one in forty-one.",
    "summary": (
        "Chapter 35 argues that the kingdom of God in Scripture is, in most places, a "
        "real commonwealth, with God as king by Israel's covenant; Chapter 36 goes through "
        "the senses of the word of God and of prophet, and says every man must examine a "
        "prophet before he obeys him. Use Hobbes's own count of four hundred false "
        "prophets and one true one as a prior and see what a fulfilled prophecy does to it."
    ),
    "key": [
        "the kingdom of God: a civil kingdom",
        "holy = God's own, as 'public' is the king's",
        "prophet: 1 true in 401, so prior 1/401",
        "Bayes factor = P(sign | true) / P(sign | not)",
        "one sign moves 1/401 to 1/41, not to 1",
    ],
    "key_label": "Kingdom and prophets in five lines",
    "concepts_intro": (
        "Two chapters that are mostly textual commentary carry the argument that makes "
        "the rest of Part III political."
    ),
    "concepts": [
        ("The kingdom of God is a civil kingdom",
         "Divines mostly take the kingdom of God for eternal felicity or for sanctification. "
         "Hobbes finds that in most places Scripture means a kingdom in the proper sense: "
         "a monarchy over subjects acquired by their own consent. Israel chose God for "
         "its king by covenant, and the high priest was his lieutenant. It was cast off "
         "when the people asked Samuel for a king, and Christ's coming is to restore it."),
        ("Holy, sacred, sacrament",
         "What God has by special right and not by general right is holy, as what the "
         "king has is public. What is holy by being given to God for public service is "
         "sacred, and a sacrament is a visible thing set apart as a sign of admission to "
         "God's kingdom, or of remembering it: circumcision and the Passover, then "
         "baptism and the Lord's Supper."),
        ("The word of God and prophets",
         "The word of God means the speech of God, or doctrine concerning God, or the "
         "thing God's word brought about, or what reason and equity dictate. A prophet "
         "may mean a spokesman, a foreteller, or a madman. Most often it is one to whom "
         "God speaks to be told to someone else, and God speaks by dreams and visions. "
         "Because false prophets were far more numerous than true, every man is bound "
         "to try the prophet by the marks."),
    ],
    "read_title": "The passage first, then the chapters line by line",
    "read_intro": (
        "The passage is the conclusion of a chain of textual arguments on one verse. "
        "It says what the kingdom of God is, and everything in Chapter 36 about "
        "obedience to prophets rests on it."
    ),
    "body": [
        ("p", "<strong>Chapter 35.</strong> &ldquo;It is therefore manifest enough by "
              "this one place, that by the Kingdome of God, is properly meant a "
              "Common-wealth, instituted (by the consent of those which were to be "
              "subject thereto) for their Civill Government, and the regulating of their "
              "behaviour, not onely towards God their King, but also towards one another "
              "in point of justice, and towards other Nations both in peace and "
              "warre&rdquo;"),
        ("p", "A great deal turns on a word. If you say the Church of England is the "
              "kingdom of God on earth, or that the kingdom of God is the church's "
              "spiritual rule over believers, you have said that some power besides the "
              "king governs Christians as Christians. Hobbes begins Chapter 35 by "
              "observing that divines mean one of two things, the kingdom of glory in "
              "heaven or the kingdom of grace in the heart, &ldquo;but never for the "
              "Monarchy, that is to say, the Soveraign Power of God over any Subjects "
              "acquired by their own consent&rdquo;. He finds the reverse in Scripture: "
              "&ldquo;a Kingdome properly so named, constituted by the Votes of the People "
              "of Israel&rdquo;."),
        ("p", "The evidence is mostly one passage of Exodus, which he reads with care. "
              "God says that if Israel keeps his covenant they will be a &lsquo;peculiar "
              "people&rsquo;, a &lsquo;sacerdotal kingdom&rsquo; and a &lsquo;holy "
              "nation&rsquo;. He argues that the best translation of peculiar is the "
              "Vulgate's <em>peculium</em>, something set aside, and that the reason "
              "God gives, that all the earth is his, shows that Israel was his in a "
              "different way: all nations are his by power, &ldquo;but you shall be mine, "
              "by your own Consent, and Covenant&rdquo;. The English translations that "
              "say &lsquo;a kingdom of priests&rsquo; and &lsquo;a precious "
              "treasure&rsquo; he thinks mistaken, and he adds that they have been "
              "translated so because the true meaning &ldquo;gives too much light to "
              "Christian Kings to see their right of Ecclesiasticall Government&rdquo;. "
              "A reader who knows how the quarrel over episcopacy was fought in the 1640s "
              "will see why he said it."),
        ("p", "Two more passages support the point. When the elders of Israel demanded a "
              "king, the Lord told Samuel, &lsquo;they have not rejected thee, but they "
              "have rejected me, that I should not reign over them&rsquo;; so God had "
              "been king. And the Prophets foretell his restoration on Mount Zion, on "
              "earth. The New Testament says the same: Christ is to have the throne of "
              "David, and was put to death as a claimant to the title, King of the Jews. "
              "Hence the prayer: &lsquo;Thy kingdom come&rsquo; would be superfluous if "
              "the kingdom had never been interrupted. The kingdom of grace is the "
              "promise of obedience made now; the kingdom of glory is when Christ comes "
              "in majesty."),
        ("p", "From the kingdom Hobbes derives holiness. A king is the public person, and "
              "what belongs to the commonwealth is public; so God, king of Israel, is the "
              "holy one of Israel, and the Sabbath, the temple, the tithes and the "
              "priests are holy because they are his. The Jews were a holy nation "
              "because they became his property by covenant. Degrees follow: the tribe of "
              "Levi, the priests, the high priest, the city, the temple and the holy of "
              "holies. A sacrament is the setting aside of a visible thing for a sign of "
              "admission to the kingdom or a reminder of it. This is the political work "
              "of the chapter: a sacred thing is the king's, and who the king is "
              "determines who may consecrate."),
        ("p", "Chapter 36 turns to the word of God. It means a speech, not a vocable; it may "
              "mean what God has said, or what is said of God, which is the doctrine of "
              "religion; and it may mean the thing itself that was said, or what reason "
              "and equity dictate. Prophet, likewise, is said in several ways, which he "
              "takes from Scripture: a spokesman, as Aaron for Moses; one who prays for a "
              "congregation; one who foretells; or one who speaks incoherently, as the "
              "Gentiles took their oracles. Most often it is one to whom God speaks, so "
              "he asks how God speaks to such a man. Not by a voice with organs, but by "
              "whatever way makes his will understood, which Scripture shows to be dreams "
              "and visions for the ordinary prophet, and for Moses and the high priests, "
              "a way the text does not describe, which he says can be understood only as "
              "a voice."),
        ("p", "Then he comes to the practical point. He who claims to teach men the way to "
              "happiness &ldquo;pretends to govern them&rdquo;, and so is &ldquo;worthy to "
              "be suspected of Ambition and Imposture&rdquo;. Everyone must therefore "
              "examine a prophet before obeying him, unless he has already given obedience "
              "in setting up a commonwealth, as when the prophet is the sovereign. And "
              "the odds are poor, because there have always been more false prophets than "
              "true. Hobbes makes the count: Ahab asked four hundred prophets, and "
              "&ldquo;they were all false Imposters, but onely one Michaiah.&rdquo; "
              "He adds that before the captivity the prophets were generally liars, citing "
              "Jeremiah, and that impostors &ldquo;gain in the opinion of the common "
              "sort of men, a greater reputation of Prophecy, by one casuall event that "
              "may bee but wrested to their purpose, than can be lost again by never so "
              "many failings&rdquo;. Both remarks are about weighing evidence, and that "
              "is the lab."),
        ("p", "The lab takes Hobbes's count as a base rate: of the prophets consulted, 401 in "
              "all, one is true. It then asks what the fulfilment of one prophecy does to "
              "that. A true prophet's word comes to pass, on the lesson's reading of "
              "Deuteronomy's test. A false prophet's may come to pass by chance, or by "
              "being wrested, at a rate the lesson sets at one in ten. The Bayes factor is "
              "the ratio of those two chances, 10, and applied to a prior of 1 in 401 it "
              "gives 1 in 41. The sign has made a true prophet ten times more likely than "
              "before and still only one chance in forty-one. If the prophecy is vague, so "
              "that a false prophet's chance is nine in ten, the factor is barely above 1; "
              "that is the case of the prophet who foretells that it will come to pass "
              "&lsquo;one time or other&rsquo;. If it fails, a true prophet is ruled out. "
              "None of this is Hobbes's arithmetic; it is the lesson's way of showing what "
              "his two remarks imply."),
        ("p", "The last step is the rule he draws. Every subject must try a prophet by "
              "his own natural reason and by the marks, but he must also look to the "
              "sovereign prophet, and for Christians that is the sovereign. A Christian "
              "who takes a private prophet over the sovereign must, he says, follow "
              "his own dreams or a foreign prince. A critic will say that a man who is "
              "told to test prophets and then to defer to the sovereign has been "
              "given a freedom that the sovereign can take away; Hobbes would answer "
              "that the freedom is of the heart, since thought is free, and the "
              "deference is of the tongue. The next lesson, &ldquo;Miracles and Their "
              "Use&rdquo;, applies the same test to wonders."),
        ("p", 'The four presets change one thing each. In ahab one of 401 prophets is true '
              'and one fulfilled prophecy leaves the chance that this prophet is true at '
              '1/41, a factor of 10. In two-signs two independent prophecies come true, the '
              'factors multiply to 100, and the chance rises to 1/5. In vague the false '
              'prophet fulfils the sign nine times in ten, the factor is only 10/9, and the '
              'chance is 1/361. In failed the prophecy does not come to pass, the true '
              "prophet's likelihood is 0, and the chance is 0: Hobbes's test of the prophet "
              'who fails.'),
    ],
    "lab": ("choicekit", {
        "mode": "update",
        "preset": "ahab",
        "presets": [
            {"id": "ahab", "label": "401 prophets consulted, one true; a prophecy comes true",
             "hyps": ["true prophet", "false prophet"], "prior": ["1/401", "400/401"],
             "outcomes": ["comes-true", "does-not"],
             "lik": [["1", "0"], ["1/10", "9/10"]],
             "data": ["comes-true"], "payoffs": None,
             "expect": {"upPost": "1/41", "upBF": "10", "upConf": "Confirms"}},
            {"id": "two-signs", "label": "two independent prophecies come true",
             "hyps": ["true prophet", "false prophet"], "prior": ["1/401", "400/401"],
             "outcomes": ["comes-true", "does-not"],
             "lik": [["1", "0"], ["1/10", "9/10"]],
             "data": ["comes-true", "comes-true"], "payoffs": None,
             "expect": {"upPost": "1/5", "upBF": "100", "upConf": "Confirms"}},
            {"id": "vague", "label": "a vague prophecy that a false prophet fulfils 9 times in 10",
             "hyps": ["true prophet", "false prophet"], "prior": ["1/401", "400/401"],
             "outcomes": ["comes-true", "does-not"],
             "lik": [["1", "0"], ["9/10", "1/10"]],
             "data": ["comes-true"], "payoffs": None,
             "expect": {"upPost": "1/361", "upBF": "10/9", "upConf": "Confirms"}},
            {"id": "failed", "label": "the prophecy does not come to pass",
             "hyps": ["true prophet", "false prophet"], "prior": ["1/401", "400/401"],
             "outcomes": ["comes-true", "does-not"],
             "lik": [["1", "0"], ["1/10", "9/10"]],
             "data": ["does-not"], "payoffs": None,
             "expect": {"upPost": "0", "upBF": "0", "upConf": "Refutes"}},
        ],
        "panel_title": "What a fulfilled prophecy is worth",
        "panel_intro": (
            "The prior is Hobbes's count: one true prophet among 401 consulted. The "
            "likelihoods are the lesson's: a true prophet's word comes to pass, a false "
            "prophet's does so at the rate in the second row. Change the rate, or the "
            "data, and watch the posterior; the menu at the foot of the controls "
            "chooses which hypothesis the tiles report."
        ),
    }),
    "steps_title": "Weighing a prophet's sign",
    "steps_intro": "Five steps, the same whatever the sign.",
    "steps": [
        ("Fix the base rate",
         "Say how many of the prophets one might meet are true. Hobbes's own count is "
         "one in four hundred and one; any other number is yours."),
        ("Say what a true prophet's sign looks like",
         "On Hobbes's reading of Deuteronomy a true prophet's prediction comes to pass, "
         "so the chance is 1 and a failure rules him out."),
        ("Say how often a false one's does",
         "A false prophet may be lucky, or may speak vaguely. That chance is the whole "
         "of the weight a fulfilled sign carries."),
        ("Divide the two chances",
         "The Bayes factor is the true prophet's chance divided by a false prophet's. "
         "It is 10 when the false chance is 1 in 10 and nearly 1 when it is 9 in 10."),
        ("Apply it to the prior",
         "Posterior odds are prior odds times the factor, so 1 to 400 becomes 10 to "
         "400, which is 1 in 41."),
    ],
    "worked": {
        "title": "One fulfilled prophecy against 401 prophets",
        "intro": [
            "Take the first preset. One prophet in 401 is true, and a false prophet's "
            "prediction comes to pass one time in ten.",
        ],
        "lines": [
            "prior:  1/401 true,  400/401 false",
            "chance of the sign:  1 if true,  1/10 if false",
            "true:  (1/401)·1 = 1/401",
            "false:  (400/401)·(1/10) = 40/401",
            "posterior:  (1/401) / (41/401) = 1/41,  factor 10",
        ],
        "after": [
            "Two signs, by the same reckoning, give 1/401 against 400/401·(1/100), which "
            "is 1 in 5. Even then four of five prophets who pass the test are false. "
            "Hobbes's remark that one casual event outweighs many failures is a remark "
            "about how people actually weigh evidence; on the lesson's numbers, one "
            "failure is decisive and one success is not.",
        ],
    },
    "quiz_title": "Weighing the prophets",
    "quiz": [
        {"q": "With the lesson's numbers, a prophet's first prophecy comes true. What "
              'is the chance he is a true prophet?',
         "a": [
               '1 in 10',
               '1 in 41',
               '1 in 2',
               "Certain, since a true prophet's word always comes to pass",
         ],
         "c": 1,
         "why": 'The factor is 10 and the prior odds are 1 to 400, so the posterior '
                "odds are 10 to 400, which is 1 in 41. '1 in 10' uses the false "
                "prophet's chance as if it were the posterior. '1 in 2' and 'certain' "
                'ignore the prior.'},
        {"q": "What happens to a true prophet's chance when the prophecy fails?",
         "a": [
               'It is halved',
               'It is unchanged, since prophets can be wrong',
               'It falls to zero',
               'It rises, because a hard test is a better test',
         ],
         "c": 2,
         "why": "On Hobbes's reading of Deuteronomy a true prophet's word does not "
                "fail, so the chance of 'does not' under that hypothesis is 0 and the "
                'posterior is 0. The other answers reject that reading, which is the '
                "lesson's premise."},
        {"q": 'Why does the vague prophecy give a smaller factor?',
         "a": [
               'A false prophet fulfils it almost as often as a true one',
               'A vague prophecy cannot come true',
               'A true prophet would never be vague',
               'The prior changes when the prophecy is vague',
         ],
         "c": 0,
         "why": 'The factor is 1 divided by 9/10, which is 10/9: the sign is nearly as '
                'likely from a false prophet as from a true one. The prior in this '
                "preset is the same, and 'cannot come true' and 'a true prophet would "
                "never be vague' are not what the numbers say."},
        {"q": "In Hobbes's chapter, who does a Christian turn to when he is told the "
              "prophet's marks cannot settle it?",
         "a": [
               'The pastor of his own congregation',
               'The sovereign prophet, who in a Christian commonwealth is the sovereign',
               'The Pope',
               'His own dreams, tested against Scripture',
         ],
         "c": 1,
         "why": "He says every man must consider who is the sovereign prophet, God's "
                'vicegerent on earth with the authority of governing Christian men, and '
                'take his doctrine as the rule. The others are what he says Christians '
                'who refuse the sovereign must fall back on.'},
    ],
    "mistakes": [
        ("Thinking the kingdom of God is only heaven",
         "That is the sense of divines, Hobbes says, and he finds it seldom in "
         "Scripture. He says the proper sense is a commonwealth Israel chose to be under "
         "God, and that it is why Christians pray for the kingdom to come."),
        ("Reading a fulfilled prophecy as proof",
         "On the lesson's numbers, a prophecy that comes true leaves a prophet more "
         "likely false than true. The mistake is to take a likelihood for a "
         "probability, which is what Hobbes says the common sort of men do."),
        ("Reading the base rate as Hobbes's statistic",
         "He counts four hundred false prophets and one true one in one story and "
         "says there were many more false than true in general. The lab uses the count "
         "as a stated assumption; it is not a measured rate."),
    ],
    "standard": (
        "Finish when you can update on a sign.",
        "Given a base rate of true prophets and the chances of a sign from a true and a "
        "false prophet, compute the Bayes factor and the posterior, and say what a "
        "failed sign does."
    ),
    "note": (
        "The lab computes from the base rate and chances the lesson states. The count of "
        "401 prophets is Hobbes's but the one-in-ten is not, and the reading of "
        "Deuteronomy that makes a true prophet's word certain is the lesson's. It cannot "
        "say whether the kingdom of God is the civil kingdom Hobbes finds in Scripture, "
        "or whether prophets are to be weighed by probabilities at all."
    ),
}

LESSONS = [L1, L2, L3, L4]
