"""The Cogito, Time and Freedom, lessons 1-4 -- Part Three, Chapter 1 and the
opening of Chapter 2.

Every quotation is copied from Colin Smith's translation, Routledge Classics
pagination (Part Three, pp. 429-530); the comment beside each lesson gives its
pages. Smith's ligatures are printed as plain letters, a word split by a
line-break hyphen is joined, and footnote numerals are left out. Nothing else
is changed. Merleau-Ponty states the views he rejects at length and in their
own words; each lesson says whose voice a quoted sentence is in.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Smith pp. 435-436 (opening passage: "I am not sure that there is over
    # there an ash-tray ..." p. 435, the Cartesian distinction in
    # Merleau-Ponty's words; "If I see an ash-tray ... To see is to see
    # something." p. 436, his reply); p. 429 (the scene at the desk);
    # pp. 430-435 (the idealist reading, Lachieze-Rey's); p. 435 ("On the
    # contrary, it is impossible."); p. 436 ("he takes up an untenable
    # position"); p. 437 ("it is certain only so long as actual sight is
    # equally so"); p. 439 (the objector: "A feeling, considered in itself, is
    # always true once it is felt."); p. 440 ("Besides true love, there is
    # false or illusory love."); p. 443 ("it was lived, not known, from start
    # to finish"); p. 444 (the cogito made impossible?); p. 445 ("it is not
    # because I think I am that I am certain of my existence"); p. 446 (the
    # cogito recognises this fact). Descartes's Second Replies and
    # Principles I.10 are cited from Descartes, not from Smith.
    {
        "slug": "the-cogito-and-the-certainty-of-seeing",
        "title": "The Cogito and the Certainty of Seeing",
        "module": "Part Three · 1 · The Cogito",
        "one_line": "Descartes holds that the thought of seeing is certain when the seeing is not; the chapter replies that the two certainties stand or fall together, and that even a feeling can be false.",
        "summary": (
            "Part Three opens by asking what the cogito, Descartes's I think, therefore I "
            "am, becomes after a book about the perceiving body. Set out the cogito as an "
            "inference and find the premise it would need to be valid; then set out the "
            "step from thinking I see an ash-tray to seeing one, and find the "
            "counterexample row that Descartes needs and the chapter says he cannot keep."
        ),
        "key": [
            "cogito as an inference: p, so q",
            "p, so q: invalid, one countercase",
            "adding if p then q: modus ponens",
            "seeing implies thinking I see",
            "conversely invalid: one countercase",
            "certain of seeing only if seeing",
            "feelings, too, can be illusory",
        ],
        "key_label": "The cogito and the ash-tray in seven lines",
        "concepts_intro": (
            "The chapter's first pages take the cogito apart and put it back together. "
            "Three ideas carry that work."
        ),
        "concepts": [
            ("The cogito",
             "Latin for I think. Descartes's first certainty: whatever I doubt, I cannot "
             "doubt that I am thinking while I doubt, and so that I exist. The chapter "
             "keeps the certainty and asks what kind of certainty it is."),
            ("The thought of seeing",
             "Descartes's distinction between seeing a thing and seeming to see it. The "
             "thing may not be there; that I seem to see it, that I think I see, cannot be "
             "false. The chapter argues that the two cannot be held apart."),
            ("True and false feelings",
             "A love can be lived in earnest and turn out later not to have been love. If "
             "so, an inner state is not known in advance either, and the certainty of the "
             "cogito cannot be the certainty of a transparent inner life."),
        ],
        "read_title": "The passage first, then the chapter's first eighteen pages",
        "read_intro": (
            "The passage is Descartes's distinction and the reply to it, a page apart. The "
            "lesson goes back to the chapter's first page, follows the reading of the cogito "
            "it sets aside, then reads the passage and the pages on feeling that follow."
        ),
        "body": [
            ("p", "<strong>Part Three, Chapter 1, pp. 435&ndash;436.</strong> &ldquo;I am not "
                  "sure that there is over there an ash-tray or a pipe, but I am sure that I "
                  "think I see an ash-tray or a pipe. &hellip; If I see an ash-tray, in the "
                  "full sense of the word see, there must be an ash-tray there, and I cannot "
                  "forego this assertion. To see is to see something.&rdquo; The first "
                  "sentence, on page 435 of Colin Smith's translation, states Descartes's "
                  "distinction in Merleau-Ponty's words; the second and third, on page 436, "
                  "are his reply. Read the chapter from its first page, 429, to the middle of "
                  "page 446, where the triangle begins, in your own copy before going on; the "
                  "lesson goes back through it a phrase at a time."),
            ("p", "René Descartes, the French mathematician and philosopher, set out in his "
                  "<em>Meditations</em> of 1641 to doubt everything that could be doubted: "
                  "the senses, which sometimes deceive, his own body, which he might be "
                  "dreaming, even arithmetic, which a deceiving god might falsify. One thing "
                  "survives. While I doubt, I think, and while I think, I am. The Second "
                  "Meditation then asks what this I is, a thing that thinks, and finds "
                  "seeing among its acts in a qualified sense: even if I am dreaming, it is "
                  "certain that I seem to see light. That is the thought of seeing, and it "
                  "is the target of the passage. The seeing may be false; the seeming, "
                  "Descartes holds, cannot."),
            ("p", "The chapter does not begin there. It begins at a desk: the author is "
                  "thinking of the Cartesian cogito, wanting to finish this book, feeling the "
                  "coolness of the paper under his hand and seeing the trees of the boulevard "
                  "through the window (p. 429). For the next six pages it then states, in the "
                  "voice of an idealist, a reading of the cogito as a thought outside time "
                  "that constitutes every object it finds. The footnotes name the reader he "
                  "has in mind, Pierre Lachièze-Rey, a French interpreter of Kant. Merleau-Ponty "
                  "follows the reading to its end, where my mind would be God, unique and "
                  "unable to recognise any other self, and concludes that the cogito must be "
                  "read on a middle course between that eternity and the scattered instants "
                  "of empiricism (p. 435). Only then does he take up Descartes's distinction."),
            ("p", "So, to the passage. The paragraph begins by granting that there can be no "
                  "doubt at all that I think. Then the distinction: not sure of the ash-tray, "
                  "sure that I think I see it. Can the two assertions be pulled apart, so that "
                  "the second keeps its certainty whatever becomes of the first? &ldquo;On the "
                  "contrary, it is impossible.&rdquo; Perception, the chapter says, is an act "
                  "that cannot be set apart from the thing it is directed at. If I see, in the "
                  "full sense, there is something there; if there is nothing there, I say that "
                  "I did not really see. &ldquo;To see is to see something&rdquo; is the "
                  "whole reply in five words, and the next pages defend it."),
            ("p", "The defence takes the thought of seeing in its two possible senses. Taken "
                  "as the mere impression of seeing, it is certain only as a possibility, and "
                  "we could not even have it unless we had on other occasions really seen. "
                  "Taken as the consciousness of a power that constitutes the world, it would "
                  "make the world as certain as the power, and transcendental idealism would "
                  "turn into absolute realism. Either way, the thought of seeing &ldquo;is "
                  "certain only so long as actual sight is equally so&rdquo; (p. 437). So "
                  "Descartes, holding the thing doubtful and the thought of it certain, "
                  "&ldquo;takes up an untenable position&rdquo; (p. 436). That is the "
                  "chapter's verdict, and it is aimed at the distinction, not at the cogito."),
            ("def", ("The cogito read as an inference",
                     "The reading on which I exist is a conclusion drawn from the premise I "
                     "think. It is valid only with a further premise connecting the two, and "
                     "the question is whether Descartes ever meant it so.")),
            ("p", "The lab tests that reading with propositional logic, in which nothing is "
                  "disputed. Let p be I think and q be I exist. The <code>bare</code> preset "
                  "writes the cogito as p, so q. The lab lists every assignment of true and "
                  "false to the two letters, four rows, and finds one in which the premise is "
                  "true and the conclusion false: p true, q false. One such counterexample row "
                  "is enough, and the verdict tile prints Invalid; the form tile finds no "
                  "catalogued form. The <code>major</code> preset adds the premise if I think, "
                  "I exist. Now no row makes both premises true and the conclusion false, the "
                  "counterexample tile prints 0, and the form tile names modus ponens. The lab "
                  "can only state the premise for me. The premise an inference would really "
                  "need is general, that whatever thinks exists, and the prose has to supply it."),
            ("p", "Descartes was asked about exactly this. In the Second Replies, printed with "
                  "the <em>Meditations</em> in 1641, he denied that the cogito is deduced by a "
                  "syllogism: someone who says I think, therefore I am recognises it as "
                  "self-evident by a simple intuition of the mind, and learns the general "
                  "premise from his own case, finding it impossible to think without "
                  "existing. In the <em>Principles</em> of 1644 (I.10) he allows that one must "
                  "already know that what thinks cannot fail to exist, as a presupposed notion "
                  "rather than a premise. Readers of Descartes still argue over which passage "
                  "states his view. What the lab shows is only the cost of the inference "
                  "reading: it needs a premise that Descartes, in the Replies, treated as "
                  "learned from the very case it would be used to prove."),
            ("p", "The chapter reads the cogito in neither way. On page 445 it reverses the "
                  "order of the two terms: &ldquo;it is not because I think I am that I am "
                  "certain of my existence&rdquo;; the certainty of my thoughts comes from "
                  "their actually being performed. I am sure that I love by loving and that "
                  "I doubt by doubting. A page later it keeps the formula I think, I am, "
                  "and says the two assertions are equivalent, but in the opposite sense "
                  "from the idealist's: the I think is folded back into the existing, not the "
                  "existing reduced to the consciousness of it."),
            ("p", "The <code>seeing</code> preset sets out Descartes's distinction itself. Let "
                  "s be I see an ash-tray and t be I think I see one. Descartes grants that "
                  "if I see, I think I see. The step from thinking I see to seeing is then "
                  "the form the lab names affirming the consequent, and it has one "
                  "counterexample row: t true, s false. That row is exactly what Descartes "
                  "needs to be possible, and propositional logic finds nothing wrong with it. "
                  "The chapter's objection is not that the row is inconsistent. It is that "
                  "in that row the thought of seeing is the mere impression of seeing, "
                  "certain only as a possibility, so the certainty Descartes wanted from it "
                  "is not there. The row is a line in a truth table, not anyone's experience."),
            ("p", "Then the objection that perception is a special case. Love and will, the "
                  "objector says, may mislead us about their objects but not about "
                  "themselves: &ldquo;A feeling, considered in itself, is always true once "
                  "it is felt&rdquo; (p. 439). That sentence is the objector's, and the next "
                  "one turns on it. The reply is a distinction the objector cannot make: "
                  "&ldquo;Besides true love, there is false or illusory love&rdquo; (p. 440). "
                  "It is not the lie I tell when I give the name of love to something "
                  "unworthy of it, which I knew all along. In illusory love I was really "
                  "committed, and only after disillusionment do I find beneath it something "
                  "else: the likeness of the loved woman to another, boredom, habit. It "
                  "touched one part of me, the man of forty, the traveller, the widower, and "
                  "not the whole."),
            ("p", "Max Scheler, the German phenomenologist of value, gives the chapter its "
                  "examples of feelings lived inauthentically: the girl who feels the "
                  "feelings of Isolde or Juliet and pours them into her own life, and has "
                  "no means of discovering the literary element in her love until a feeling "
                  "of her own arrives (pp. 441&ndash;442). And the discovery that one is in "
                  "love works the same way in reverse. Every sign was noticed, the "
                  "impatience, the silence, the waiting; the whole was not, and the love "
                  "&ldquo;was lived, not known, from start to finish&rdquo; (p. 443). A "
                  "consciousness transparent to itself and an unconscious that hides a love "
                  "already formed make, the chapter says, the same retrospective mistake: "
                  "both place inside me in advance what I learn about myself only later."),
            ("p", "Has the chapter now made the cogito impossible? It asks that itself (p. "
                  "444), and its answer is that existence is action. I can be sure of "
                  "willing, loving or believing provided that I actually do will, love or "
                  "believe. Doubting is certain in the act of doubting something, not as a "
                  "pure thought about doubting, and inner perception, like outer perception, "
                  "is a synthesis that is never complete and still affirms itself. The "
                  "cogito, on page 446, is the recognition of that fact."),
            ("p", "If even feeling is not transparent, pure thought looks like the last place "
                  "where the mind might coincide with itself. The next lesson, “The "
                  "Triangle”, reads the chapter's test of that: a geometer's proof."),
        ],
        "lab": ("argkit", {
            "mode": "validity",
            "preset": "bare",
            "show": "all",
            "presets": [
                {"id": "bare", "label": "I think, so I exist: p, so q (p for I think, q for I exist)",
                 "premises": ["p"], "conclusion": "q",
                 "expect": {"vaRows": "4", "vaCounter": "1", "vaVerdict": "Invalid", "vaForm": "no catalogued form"}},
                {"id": "major", "label": "If I think, I exist; I think; so I exist",
                 "premises": ["p -> q", "p"], "conclusion": "q",
                 "expect": {"vaRows": "4", "vaCounter": "0", "vaVerdict": "Valid", "vaForm": "modus ponens"}},
                {"id": "seeing", "label": "If I see an ash-tray I think I see one; I think I see one; so I see one (s for I see, t for I think I see)",
                 "premises": ["s -> t", "t"], "conclusion": "s",
                 "expect": {"vaRows": "4", "vaCounter": "1", "vaVerdict": "Invalid", "vaForm": "affirming the consequent"}},
            ],
            "panel_title": "The cogito as an inference",
            "panel_intro": (
                "This lab computes classical propositional logic, which nothing here "
                "disputes: it lists every row of true and false and marks the rows that make "
                "every premise true and the conclusion false. Compare the bare and major "
                "presets. What it cannot decide is whether the cogito is an inference at all."
            ),
        }),
        "steps_title": "Setting out the cogito as an inference",
        "steps_intro": "Four steps; the last is the chapter's.",
        "steps": [
            ("Write it in letters",
             "Give each simple sentence a letter: p for I think, q for I exist. Keep the "
             "words so, if and then as the connectives."),
            ("Find the counterexample rows",
             "List every assignment of true and false. A row that makes every premise true "
             "and the conclusion false refutes the form; p, so q has one."),
            ("Supply the missing premise",
             "Add the conditional that closes the gap, if p then q, and check that no "
             "counterexample row remains. State the general premise the instance stands for: "
             "whatever thinks exists."),
            ("State what the chapter reads instead",
             "Name the reading the chapter takes: the certainty of thinking comes from "
             "actually thinking, and the thought of seeing is certain only as far as the "
             "seeing is."),
        ],
        "worked": {
            "title": "The cogito with and without its premise",
            "intro": [
                "Take the cogito as an inference and test it twice, then test Descartes's step "
                "from thinking I see an ash-tray to seeing one.",
            ],
            "lines": [
                "p: I think;  q: I exist",
                "bare:  p, so q;  4 rows, 1 counterexample",
                "the countercase:  p true, q false",
                "with if p then q:  modus ponens, valid",
                "seeing:  if s then t; t; so s;  1 counterexample",
                "that row:  t true, s false",
            ],
            "after": [
                "The bare cogito is invalid, and valid only with a premise that Descartes in "
                "the Second Replies said is learned from the cogito itself. The step from "
                "seeming to see to seeing is invalid too, and its one counterexample row is the "
                "case Descartes needs; the chapter's reply is that in that row the thought of "
                "seeing has lost the certainty he wanted from it.",
            ],
        },
        "quiz_title": "The cogito and the ash-tray",
        "quiz": [
            {"q": "With p for I think and q for I exist, the argument p, so q has one "
                  "counterexample row. Which?",
             "a": ["p true, q false", "p false, q true", "p false, q false",
                   "None: the form is valid"],
             "c": 0,
             "why": "A counterexample row makes the premise true and the conclusion false, so "
                    "p must be true and q false. A row with p false makes the premise false "
                    "and refutes nothing, and since the row exists, the form is not valid."},
            {"q": "What did Descartes say in the Second Replies about how the cogito is known?",
             "a": ["That it is not deduced by a syllogism but recognised by a simple intuition "
                   "of the mind",
                   "That it is deduced from the major premise that everything which thinks "
                   "exists",
                   "That it is learned from reading the works of earlier philosophers",
                   "That it is a probable opinion, to be confirmed by experience"],
             "c": 0,
             "why": "The Replies deny the syllogistic reading and say the general premise is "
                    "learned from one's own case, which is the opposite of deducing the "
                    "cogito from it. Descartes did not take the cogito from books, and he "
                    "held it certain, not probable."},
            {"q": "On the chapter's account, what becomes of the thought that I see an "
                  "ash-tray if no ash-tray is there?",
             "a": ["It is the mere impression of seeing, certain only as a possibility",
                   "It stays certain, whatever becomes of the ash-tray",
                   "It proves that the ash-tray exists after all",
                   "It shows that nothing can ever be seen"],
             "c": 0,
             "why": "The thought of seeing, the chapter says, is certain only so long as actual "
                    "sight is; without the thing it is the impression of seeing. Staying "
                    "certain regardless is Descartes's position, which the chapter calls "
                    "untenable. Nothing in it proves an ash-tray, and real seeing is not denied."},
            {"q": "What does the chapter mean by an illusory love?",
             "a": ["A love I truly lived, which disillusionment shows touched only part of me "
                   "and was aimed at qualities rather than the person",
                   "A love I pretended to and knew all along was not love",
                   "A true love that is now dying",
                   "A feeling that was never felt at all"],
             "c": 0,
             "why": "The chapter separates illusory love from the deceit of calling something "
                    "love that I knew was not, and denies that it is only a true love dying. "
                    "It was felt and lived; what it lacked was the whole of me."},
        ],
        "mistakes": [
            ("Thinking the cogito is an inference from thinking to being",
             "Set out as p, so q, it is invalid: the row p true, q false refutes it. It "
             "becomes valid only with the premise if I think, I exist, standing for whatever "
             "thinks exists. Descartes himself denied the syllogistic reading in the Second "
             "Replies, calling the cogito a simple intuition and saying the general premise "
             "is learned from one's own case, though in the <em>Principles</em> he allows it "
             "as presupposed. The chapter reads it as neither: &ldquo;it is not because I "
             "think I am that I am certain of my existence&rdquo;; the certainty comes from "
             "the thinking actually being done."),
            ("Thinking the chapter gives up the cogito",
             "It grants at once that there can be no doubt that I think, and later that he "
             "who doubts cannot, while doubting, doubt that he doubts. What it rejects is "
             "Descartes's separation of the thought of seeing from seeing, and the idealist "
             "reading of the cogito as a thought outside time. The cogito stays; its sense "
             "changes."),
            ("Taking the counterexample row for an experience",
             "The <code>seeing</code> preset's row, t true and s false, is a line in a truth "
             "table: thinking I see true, seeing false. It shows that the step is not valid "
             "in logic, which no one disputes. Whether a thought of seeing in that row keeps "
             "any certainty is the philosophical question, and the chapter answers that it "
             "is then only the impression of seeing."),
        ],
        "standard": (
            "Finish when you can set out the cogito as an inference and say what it would need.",
            "Given an argument stated in words, write it in sentence letters, find its "
            "counterexample rows, name the premise that would make it valid, and state why the "
            "chapter does not read the cogito as such an inference."
        ),
        "note": (
            "The lab is propositional logic and decides only whether a form is valid. It "
            "cannot decide whether the cogito is an inference, and Descartes's own texts, the "
            "Second Replies and the Principles, are read both ways. The chapter's reading of "
            "Descartes, and its account of the idealist reading it sets aside, are readings "
            "too, and both have been contested."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Smith p. 449 (opening passage: "The construction makes explicit ... the
    # possibility of the transition."); p. 446 (the objection from pure
    # thought; the proof described); p. 447 (Wertheimer and Gurwitsch in the
    # notes; "The necessity of the proof is not an analytic necessity");
    # p. 448 ("There is no definition of a triangle which includes in advance
    # the properties subsequently to be demonstrated"); p. 449 ("The
    # construction is a gesture"; the words on, through, apex, extend);
    # p. 450 ("The subject of geometry is a motor subject."; Kant's motion
    # which generates space, via Lachieze-Rey); p. 451 ("it is from the world
    # of perception that I borrow the notion of essence"). Kant's own use of
    # the proof (Critique of Pure Reason A716-17/B744-45) is the lesson's
    # comparison; the chapter does not cite it.
    {
        "slug": "the-triangle",
        "title": "The Triangle",
        "module": "Part Three · 1 · The Cogito",
        "one_line": "A geometer's proof looks like the mind coinciding with itself; the chapter reads the construction that makes it work as a gesture of a body that inhabits space.",
        "summary": (
            "The proof that a triangle's angles make two right angles needs a line drawn "
            "through one corner parallel to the opposite side. Compute the third angle and "
            "the alternate angles of the construction at each vertex, and name what the "
            "construction adds that the definition of a triangle does not contain."
        ),
        "key": [
            "third angle = 180° less the other two",
            "parallel through a vertex",
            "alternate angles equal the base angles",
            "three angles on a line make 180°",
            "necessity, but not analytic necessity",
            "a construction is a gesture",
        ],
        "key_label": "The triangle in six lines",
        "concepts_intro": (
            "The chapter turns to geometry because pure thought is the strongest case for "
            "a mind that possesses itself. Three ideas carry its reading of the proof."
        ),
        "concepts": [
            ("The construction",
             "The line added to a figure to make a proof possible, here the parallel through "
             "one vertex. It is in no definition of a triangle, and without it the angle sum "
             "is not shown."),
            ("Analytic necessity",
             "The necessity of a conclusion contained in its premises or definitions, found "
             "by taking them apart. The chapter denies that the proof's necessity is of this "
             "kind."),
            ("A motor subject",
             "The chapter's name for the geometer: someone who knows spatial relations by "
             "describing them, at least potentially, with a body that moves, rather than a "
             "pure intellect contemplating an idea."),
        ],
        "read_title": "The passage first, then the pages on the triangle",
        "read_intro": (
            "The passage is the chapter's account of why the proof's conclusion is necessary. "
            "The lesson goes back to where the triangle comes in, follows the objection it "
            "answers, then reads the passage and the five pages around it."
        ),
        "body": [
            ("p", "<strong>Part Three, Chapter 1, p. 449.</strong> &ldquo;The construction "
                  "makes explicit the possibilities of the triangle, considered not in the "
                  "light of its definition and as a pure idea, but as a configuration and as "
                  "the pole towards which my movements are directed. The conclusion follows "
                  "of necessity from the hypothesis because, in the act of constructing, the "
                  "geometer has already experienced the possibility of the transition.&rdquo; "
                  "The two sentences are on page 449 of Smith's translation. Read from the "
                  "middle of page 446, where the chapter turns to pure thought, to the end of "
                  "the paragraph on page 451, in your own copy before going on."),
            ("p", "You were probably shown this proof at school. Draw a triangle, and through "
                  "its top corner draw a line parallel to the base. The two angles the new "
                  "line makes on either side of the corner are equal to the two base angles, "
                  "because they are alternate angles across parallel lines; and the three "
                  "angles at the corner lie along one straight line, so they make two right "
                  "angles. The <code>classic</code> preset does it with angles of 60° and 70°: "
                  "the third angle is `180 − 130 = 50`, and along the parallel `60 + 50 + 70 "
                  "= 180`. The chapter describes the same construction in the first person: I "
                  "think of the triangle, extend one of its sides, draw the parallel through "
                  "the apex, and perceive that the three angles there equal the triangle's "
                  "angles and two right angles (p. 446)."),
            ("p", "Why geometry? Because the chapter has just shown that feeling is not "
                  "transparent, and the objection now is that pure thought, at least, must "
                  "coincide with itself. The geometer is certain of the result. The "
                  "construction is not like a child's drawing, in which each stroke changes "
                  "what the drawing is, a house, then a boat, then a man; from start to "
                  "finish it has a triangle in view. The chapter cites two sources for the "
                  "description: Max Wertheimer, the Gestalt psychologist, who studied how "
                  "people solve problems by seeing a figure anew, and Aron Gurwitsch, a "
                  "phenomenologist then teaching in Paris. On their account the proof sees one "
                  "sum of angles in two groupings at once. The objector concludes that truth "
                  "is impossible without a mind that possesses itself absolutely (p. 447)."),
            ("p", "The reply starts by granting that there is an act here that overcomes the "
                  "scattering of thought in time. Then it asks what kind of act. "
                  "&ldquo;The necessity of the proof is not an analytic necessity&rdquo; (p. "
                  "447): the construction is not contained in the essence of the triangle, "
                  "only made possible by it. &ldquo;There is no definition of a triangle which "
                  "includes in advance the properties subsequently to be demonstrated&rdquo; "
                  "(p. 448), nor the steps that lead to them. Extending a side and drawing the "
                  "parallel are possible only for a triangle as it is drawn on paper, on a "
                  "blackboard or in the imagination, with its physiognomy. A formal proof "
                  "written afterwards, the chapter adds, is always retrospective: it feeds on "
                  "the intuitive one."),
            ("def", ("Construction (in a proof)",
                     "A line or figure added to the one given, so that a property not visible "
                     "before becomes visible and provable. It belongs to the proof, not to "
                     "the definition of what is proved.")),
            ("p", "Immanuel Kant, the German philosopher whose <em>Critique of Pure Reason</em> "
                  "(1781, 1787) set the terms of this question for a century, used this very "
                  "proof as his example (A716&ndash;17/B744&ndash;45). A philosopher "
                  "reflecting on the concept of a triangle, he wrote, could analyse it for ever "
                  "and find nothing about its angles; the geometer extends a side, draws the "
                  "parallel and reaches the result by constructing the figure in pure "
                  "intuition. At its strength Kant's view explains both halves of the "
                  "puzzle: the result is not in the concept, and it is still necessary, "
                  "because the intuition in which the figure is built is the form of all our "
                  "sensing. The chapter does not cite this passage, and the comparison is the "
                  "lesson's. Merleau-Ponty agrees with Kant that the concept is not enough. "
                  "Where they part is the place of the construction."),
            ("p", "For the chapter, the words the construction needs, on, through, apex, "
                  "extend, have a meaning only for a triangle situated in a perceptual field, "
                  "oriented up and down, right and left, and caught up in my general grip on "
                  "the world (pp. 448&ndash;449). &ldquo;The construction is a "
                  "gesture&rdquo;: the lines drawn are the outward expression of an intention, "
                  "and the triangle I construct on was, before I drew anything, traversed by "
                  "lines of force, full of directions not traced out yet possible. That is the "
                  "passage's sense of a configuration and a pole of movement. The geometer "
                  "has already experienced the transition, because he has placed himself at a "
                  "point of the figure and tended towards another."),
            ("p", "So the chapter's formula is: &ldquo;The subject of geometry is a motor "
                  "subject&rdquo; (p. 450). It means first that the body is not an object "
                  "and its movement not a mere change of place. Kant conceded, the chapter "
                  "says, a motion which generates space, distinct from motion in space; but if "
                  "a constituting consciousness thinks that motion, the body is not even its "
                  "instrument, only an object among objects. The body's motion can play a part "
                  "in knowing space only if it is itself an original intentionality, a way of "
                  "being directed at things."),
            ("p", "Now the lab. Its figure draws the construction, and its tiles print the "
                  "third angle, the two alternate angles at the parallel and the straight "
                  "angle along it. The redraw-only vertex menu moves the parallel. Through C, "
                  "for the <code>classic</code> preset, the alternate angles are 60° and 70°; "
                  "through A they are 70° and 50°; through B, 60° and 50°; and every time the "
                  "three angles along the parallel make 180°. The construction changes and the "
                  "triangle does not, which is the chapter's point that the first "
                  "configuration survives while the second establishes itself."),
            ("p", "The <code>right</code> preset, 90° and 30°, gives a third angle of 60°. "
                  "The <code>thin</code> preset, 1° and 1°, gives 178°, a sliver of a triangle "
                  "with the parallel almost on its long side, and still `1 + 178 + 1 = 180`. "
                  "The <code>refuse</code> preset asks for angles of 100° and 90°. Two angles "
                  "that already exceed two right angles belong to no triangle, and the lab "
                  "refuses with a sentence and prints a dash for every tile. Notice how the lab "
                  "knows: it computes the third angle from the theorem itself. It illustrates "
                  "the construction and proves nothing."),
            ("p", "The section ends with essence. I believe the triangle has always had and "
                  "always will have this angle sum because I have had the experience of a real "
                  "triangle, and a perceived thing presents itself as having everything it "
                  "will ever display; &ldquo;it is from the world of perception that I borrow "
                  "the notion of essence&rdquo; (p. 451). A few pages on, the chapter adds "
                  "that perceived triangles need not have this sum for all eternity, if the "
                  "space we live in is as amenable to non-Euclidean as to Euclidean geometry "
                  "(p. 455)."),
            ("p", "Thought outruns itself in construction; the chapter next finds it doing the "
                  "same in speech. The next lesson, “The Tacit Cogito”, reads what lies "
                  "beneath the cogito Descartes wrote down."),
        ],
        "lab": ("phenkit", {
            "mode": "triangle",
            "view": "parallel",
            "model": "the parallel construction of school geometry, as the lesson's model",
            "vertex": "C",
            "preset": "classic",
            "presets": [
                {"id": "classic", "label": "Angles of 60° and 70° (illustrative)", "a": 60, "b": 70,
                 "expect": {"trC": "50°", "trAlternate": "60° and 70°", "trStraight": "60° + 50° + 70° = 180°"}},
                {"id": "right", "label": "A right angle and 30°", "a": 90, "b": 30,
                 "expect": {"trC": "60°", "trAlternate": "90° and 30°", "trStraight": "90° + 60° + 30° = 180°"}},
                {"id": "thin", "label": "A sliver: 1° and 1°", "a": 1, "b": 1,
                 "expect": {"trC": "178°", "trAlternate": "1° and 1°", "trStraight": "1° + 178° + 1° = 180°"}},
                {"id": "refuse", "label": "100° and 90°: no such triangle", "a": 100, "b": 90,
                 "expect": {"trC": "—"}},
            ],
            "panel_title": "The parallel through a vertex",
            "panel_intro": (
                "This lab is the lesson's model: it draws the school construction, a parallel "
                "through one vertex, and computes the angles along it. Nothing in the geometry "
                "is disputed; what the chapter disputes is what kind of act the construction "
                "is. Move the parallel with the vertex menu."
            ),
        }),
        "steps_title": "Computing the construction",
        "steps_intro": "Five steps; the last is the lesson's.",
        "steps": [
            ("Compute the third angle",
             "Subtract the two given angles from 180°. If they already reach 180°, there is "
             "no triangle."),
            ("Draw the parallel",
             "Through one vertex, draw the line parallel to the opposite side."),
            ("Read the alternate angles",
             "On each side of the vertex the parallel makes an angle equal to the base angle "
             "on that side, across the parallel lines."),
            ("Read the straight angle",
             "The two alternate angles and the vertex's own angle lie along one line, so "
             "their sum is 180°, two right angles."),
            ("Name what was added",
             "State what the definition did not contain: the parallel, and the regrouping of "
             "the angles it makes visible."),
        ],
        "worked": {
            "title": "Angles of 60° and 70°",
            "intro": [
                "Take a triangle with angles of 60° at A and 70° at B. You want the third "
                "angle and the construction at each vertex.",
            ],
            "lines": [
                "60° + 70° = 130°",
                "third angle:  180° − 130° = 50°",
                "parallel through C:  60° and 70°",
                "along it:  60° + 50° + 70° = 180°",
                "through A:  70° and 50°;  through B:  60° and 50°",
            ],
            "after": [
                "Each construction regroups the same three angles along a different line, and "
                "each time they make two right angles. The third angle was computed with the "
                "theorem the construction shows, so the figures illustrate the proof; they do "
                "not repeat it.",
            ],
        },
        "quiz_title": "The parallel and the proof",
        "quiz": [
            {"q": "A triangle has angles of 40° and 75°. What is the third angle, and what are "
                  "the alternate angles at the parallel through the third vertex?",
             "a": ["65°; 40° and 75°", "65°; 40° and 65°", "105°; 40° and 75°",
                   "75°; 40° and 65°"],
             "c": 0,
             "why": "`180 − 115 = 65`. Through the third vertex the parallel makes angles equal "
                    "to the two base angles, 40° and 75°. 105° is the exterior angle, not the "
                    "third angle, and the other pairs mix the vertex's own angle into the "
                    "alternate angles."},
            {"q": "On the chapter's reading, why does the conclusion follow of necessity?",
             "a": ["Because in constructing, the geometer has already experienced the "
                   "possibility of the transition",
                   "Because the angle sum is contained in the definition of a triangle",
                   "Because the figure on the paper has been measured accurately",
                   "Because a pure intuition, independent of the body, guarantees it"],
             "c": 0,
             "why": "That is the passage. The chapter denies that the necessity is analytic, so "
                    "the definition does not contain it; it denies that the construction is a "
                    "manual operation, so measuring is not the proof; and a pure intuition "
                    "apart from the body is Kant's account, which the chapter's motor subject "
                    "replaces."},
            {"q": "The refuse preset asks for angles of 100° and 90°, and the lab prints a dash "
                  "for the third angle. Why?",
             "a": ["The two angles already exceed two right angles, so no triangle has them",
                   "The lab cannot draw an obtuse angle",
                   "A right angle has no alternate angle",
                   "The angles were entered in the wrong order"],
             "c": 0,
             "why": "`100 + 90 = 190`, more than 180, so there is nothing left for a third "
                    "angle and no triangle. The lab draws obtuse angles in other inputs, the "
                    "right preset has a right angle, and the order of a and b does not matter."},
            {"q": "What does the chapter mean by calling the subject of geometry a motor subject?",
             "a": ["That the geometer knows spatial relations by describing them, at least "
                   "potentially, with a body that moves",
                   "That the proof consists in the movement of the hand across the paper",
                   "That geometry is the science of moving bodies",
                   "That the body is an instrument a constituting mind uses to draw"],
             "c": 0,
             "why": "The chapter says the construction is not a purely manual operation, so the "
                    "hand's movement is not the proof; geometry here is about figures, not "
                    "mechanics; and it denies that the body is a mere instrument of a "
                    "constituting consciousness."},
        ],
        "mistakes": [
            ("Thinking the angle sum follows from the definition, as a consequence from axioms",
             "No definition of a triangle contains the parallel, and without the parallel the "
             "sum is not shown: through C the alternate angles 60° and 70° appear only once the "
             "line is drawn. Kant used this proof to make the same point against analysis of "
             "concepts, and read the construction as made in pure intuition. The chapter's "
             "reading competes with Kant's on Kant's own example: the necessity, it says, "
             "&ldquo;is not an analytic necessity&rdquo;, and the construction is the act of "
             "a motor subject, not of pure intuition."),
            ("Thinking the proof is the hand's movement",
             "If it were, the chapter says, there would be no difference between a "
             "construction and any arbitrary set of strokes. The construction is a gesture, "
             "the outward expression of an intention directed at the triangle as a "
             "configuration; the lines drawn express it and do not make it."),
            ("Thinking the chapter makes geometry a matter of measuring drawn triangles",
             "The geometer's synthesis keeps the character of necessity, and the chapter "
             "says so. What it denies is that the necessity comes from a concept that "
             "contains all the triangle's properties. The lab's figures are exact because "
             "they are computed from the theorem, not measured from the drawing."),
        ],
        "standard": (
            "Finish when you can compute the construction at any vertex and say what it adds.",
            "Given two angles of a triangle, compute the third, the alternate angles at the "
            "parallel through each vertex and the straight angle along it, refuse an "
            "impossible pair, and state what the construction adds to the definition."
        ),
        "note": (
            "The lab computes the third angle with the theorem it illustrates, so it shows "
            "the construction and proves nothing; the geometry is undisputed. What is "
            "disputed is what makes the proof necessary: a concept (the formalist), "
            "construction in pure intuition (Kant) or the body's grasp of space (the "
            "chapter). The comparison with Kant's use of the same proof is the lesson's, not "
            "the chapter's."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Smith p. 469 (opening passage: "Behind the spoken cogito ... myself
    # experienced by myself."); p. 470 ("The tacit cogito is a cogito only
    # when it has found expression for itself."); p. 452 ("speech cannot be
    # regarded as a mere clothing for thought"; "to find in his own words more
    # than the thought he was putting into them"); p. 457 ("The non-temporal
    # is the acquired."); p. 466 (the Second Meditation read; "One thinks,
    # therefore one is."); p. 468 ("were I not, before any speech can begin,
    # in contact with my own life and thought"; "This would be to forget half
    # the truth."); p. 469 (sleet); p. 470 ("speaks as we sing when we are
    # happy"; dread of death, another's gaze); p. 473 ("I am a field, an
    # experience."); p. 475 (rationality). Observation 3 is pp. 440-443.
    # Valery is quoted p. 465; Hegel does not appear in this chapter.
    {
        "slug": "the-tacit-cogito",
        "title": "The Tacit Cogito",
        "module": "Part Three · 1 · The Cogito",
        "one_line": "The cogito Descartes wrote down is a spoken one, reached through words; beneath it the chapter finds a tacit cogito, a presence of oneself to oneself that is not yet a thought in words.",
        "summary": (
            "Reading Descartes, I reach a cogito put into words, which the chapter says should "
            "read one thinks, therefore one is. Beneath it lies a tacit cogito that words "
            "presuppose and that becomes a cogito only when it finds expression. Compute two "
            "opponent accounts' records over the chapter's cases about language and thought, "
            "and find where they part."
        ),
        "key": [
            "spoken cogito: reached through words",
            "tacit cogito: myself present to myself",
            "a cogito only once it is expressed",
            "speech is not clothing for thought",
            "words find more than was put in them",
            "survivors: none; split on 1 and 2",
        ],
        "key_label": "The tacit cogito in six lines",
        "concepts_intro": (
            "The last third of the chapter is about language. Three ideas carry it."
        ),
        "concepts": [
            ("The spoken cogito",
             "The cogito as it is reached by reading Descartes's words or by putting one's "
             "own life into concepts. It is real, and it is mediated by language, which "
             "Descartes never mentions."),
            ("The tacit cogito",
             "The presence of oneself to oneself that the spoken cogito presupposes: a "
             "comprehensive, inarticulate grasp of oneself and the world, prior to any "
             "philosophy, which becomes a cogito only when it finds expression."),
            ("Originating speech",
             "Speech that brings a thought into existence rather than rendering one already "
             "acquired. The chapter distinguishes it from secondary speech, the use of "
             "words whose meanings are settled."),
        ],
        "read_title": "The passage first, then the chapter's pages on expression",
        "read_intro": (
            "The passage names the tacit cogito and its limit in two sentences a page apart. "
            "The lesson goes back to the chapter's account of speech, then to its reading of "
            "the Second Meditation, then to the passage and the chapter's last pages."
        ),
        "body": [
            ("p", "<strong>Part Three, Chapter 1, pp. 469&ndash;470.</strong> &ldquo;Behind "
                  "the spoken cogito, the one which is converted into discourse and into "
                  "essential truth, there lies a tacit cogito, myself experienced by "
                  "myself.&rdquo; And a page later: &ldquo;The tacit cogito is a cogito only "
                  "when it has found expression for itself.&rdquo; The first sentence is on "
                  "page 469 of Smith's translation, the second on page 470. Read from the "
                  "paragraph that begins on page 451, where the chapter turns from geometry "
                  "to expression, to the end of the chapter on page 475, in your own copy "
                  "before going on."),
            ("p", "The case is a reader with a book. On page 466 the chapter reads the Second "
                  "Meditation: by following the meaning of the words and the argument, I "
                  "reach the conclusion that because I think, I am. But I have grasped my "
                  "thought and my existence only through language, and the conclusion is "
                  "about a me in idea, anyone's who reflects. The true formula of this "
                  "cogito, the chapter says, would be &ldquo;One thinks, therefore one "
                  "is.&rdquo; Language has the strange property of making us forget it: my "
                  "eyes follow the lines and lose sight of them, and that is why Descartes "
                  "nowhere mentions it."),
            ("p", "The chapter has prepared this with an account of speech (pp. "
                  "451&ndash;458). It is obvious, it says, that &ldquo;speech cannot be "
                  "regarded as a mere clothing for thought&rdquo;, the translation into "
                  "signs of a meaning already clear to itself; if it were, language could "
                  "teach us nothing. A good book imposes its meaning on us, and the speaker, "
                  "too, must be able &ldquo;to find in his own words more than the thought "
                  "he was putting into them&rdquo;, or we would not see thought, even solitary "
                  "thought, seeking expression so persistently (p. 452). The poet Paul Claudel "
                  "is quoted for the writer's side of this. Secondary speech renders a thought "
                  "already acquired; originating speech brings one into existence, and every "
                  "settled word was once originating."),
            ("p", "So ideas are cultural objects, like a church or the Ninth Symphony, and "
                  "their seeming independence of time is an effect of expression. Once the "
                  "quadratic equation has appeared, a good or bad later statement of it adds "
                  "or subtracts nothing, and it lives on among us; but it has its historical "
                  "and geographical area, and would need fresh acts of expression if its "
                  "tradition were destroyed. &ldquo;The non-temporal is the acquired&rdquo; "
                  "(p. 457). That sentence is the hinge to the next chapter, on time."),
            ("def", ("The tacit cogito",
                     "Myself experienced by myself, before and beneath any words: a "
                     "presence to oneself that the spoken cogito presupposes, that knows "
                     "itself only under threat, and that is a cogito in the full sense only "
                     "once expressed.")),
            ("p", "The lab sets two opponent accounts against the chapter's cases. The names "
                  "are the lesson's. On the first, thought before language, thought is "
                  "complete and clear to itself and words are its clothing; this is the view "
                  "of expression the chapter, on page 452, says is obviously untenable. On "
                  "the second, language "
                  "before thought, thought is nothing but words, and consciousness is led by "
                  "language as the realist believes he is led by the world; the chapter raises "
                  "that conclusion itself on page 468 and answers: &ldquo;This would be to "
                  "forget half the truth.&rdquo;"),
            ("p", "The cases, as the lesson codes them, thought-first then language-first. "
                  "First, Descartes's book: I should be unable even to read it, the chapter "
                  "says, &ldquo;were I not, before any speech can begin, in contact with my "
                  "own life and thought&rdquo; (p. 468). Thought-first absorbs that; "
                  "language-first cannot. Second, the speaker who finds in his words more than "
                  "he put into them (p. 452): language-first absorbs it, and thought-first, for "
                  "which the meaning was there complete beforehand, cannot. Third, the "
                  "illusory love of the chapter's earlier pages (pp. 440&ndash;443), lived "
                  "and not known: a thought transparent to itself would have known it, so "
                  "thought-first fails it, and language-first, which says nothing about "
                  "feeling, is silent."),
            ("p", "The <code>all</code> preset shows the three. The record tile counts, for "
                  "each account, the observations it absorbs, fails and is silent on: "
                  "thought before language absorbs 1 of 3 and fails 2; language before "
                  "thought absorbs 1, fails 1 and is silent on 1. The survivors tile lists "
                  "the accounts that fail none, and prints none. The split tile lists the "
                  "observations on which the pair stand y against n, and prints the first "
                  "two; the third is n against silent, which is not a split. The "
                  "<code>books</code> preset keeps only the first case, and thought before "
                  "language survives it alone. The <code>expression</code> preset keeps the "
                  "second and third, and language before thought survives them. Each "
                  "survives only the cases chosen for it."),
            ("p", "Neither account is the tacit cogito, and the tacit cogito is not a column. "
                  "It is not a silent voice saying I think before I say it aloud. It does not "
                  "constitute the world, the word or the word's meaning; it &ldquo;speaks as "
                  "we sing when we are happy&rdquo; (p. 470). The word sleet, the chapter "
                  "says, I caught on to as one imitates a gesture, as a modulation of my body, "
                  "never inspected as an idea. The tacit cogito knows itself only in extreme "
                  "situations, in the dread of death or of another's gaze on me; it is a "
                  "grasp on the world like the infant's at its first breath, and it waits to "
                  "be won back by perception and speech."),
            ("p", "If ultimate subjectivity cannot think itself the moment it exists, how can "
                  "it ever do so? The chapter puts the objection to itself (p. 470) and "
                  "answers that it has withheld from the primordial I only objective, "
                  "positing thought, not all self-presence. What am I, then, beneath my "
                  "particular thoughts? &ldquo;I am a field, an experience&rdquo; (p. 473). "
                  "With my birth something began that can no longer cease to see or not to "
                  "see, a new possibility of situations, and the cogito retrieves that event."),
            ("p", "This is the most disputed idea in the chapter, and the first to dispute it "
                  "was Merleau-Ponty. In a working note of his last years, published after "
                  "his death in <em>The Visible and the Invisible</em> (1964), he wrote that "
                  "the tacit cogito is impossible: to have even the idea of thinking, of "
                  "returning to oneself, one already needs words. Readers disagree over "
                  "whether the note retracts the 1945 idea or only the way this chapter "
                  "states it, as a self-presence that seems to need no world of speech."),
            ("p", "The chapter ends with rationality: classical thought explains why "
                  "appearances agree by a world in itself or an absolute mind, and both "
                  "explanations borrow their force from the agreement they explain (p. 475). "
                  "It has restored to the cogito a temporal thickness, and the next chapter "
                  "asks what time is. The next lesson, “Time Is Not in Things”, begins with "
                  "a river."),
        ],
        "lab": ("phenkit", {
            "mode": "cases",
            "view": "table",
            "accounts": ["thought before language", "language before thought"],
            "preset": "all",
            "presets": [
                {"id": "all", "label": "All three cases",
                 "observations": ("the written cogito needs a reader already in contact with his own thought, y, n; "
                                  "the speaker finds in his words more than he put into them, n, y; "
                                  "an illusory love lived and not known, n, -"),
                 "expect": {"caRecord": ("thought before language: absorbs 1 of 3, fails 2, silent 0; "
                                         "language before thought: absorbs 1 of 3, fails 1, silent 1"),
                            "caSurvivors": "none",
                            "caSplit": ("the written cogito needs a reader already in contact with his own thought, "
                                        "the speaker finds in his words more than he put into them")}},
                {"id": "books", "label": "The cogito in a book",
                 "observations": "the written cogito needs a reader already in contact with his own thought, y, n",
                 "expect": {"caSurvivors": "thought before language",
                            "caSplit": "the written cogito needs a reader already in contact with his own thought"}},
                {"id": "expression", "label": "Expression and the illusory love",
                 "observations": ("the speaker finds in his words more than he put into them, n, y; "
                                  "an illusory love lived and not known, n, -"),
                 "expect": {"caRecord": ("thought before language: absorbs 0 of 2, fails 2, silent 0; "
                                         "language before thought: absorbs 1 of 2, fails 0, silent 1"),
                            "caSurvivors": "language before thought",
                            "caSplit": "the speaker finds in his words more than he put into them"}},
            ],
            "panel_title": "Two accounts of language and thought",
            "panel_intro": (
                "This lab counts the lesson's coding: each case is marked y, n or - against two "
                "opponent accounts, and the lab counts each record, the accounts that fail "
                "none, and the cases on which the two part. The count is exact; the coding is "
                "the lesson's reading, and the tacit cogito is in the prose, not in a column."
            ),
        }),
        "steps_title": "Counting two accounts over the cases",
        "steps_intro": "Five steps; the last is not counted.",
        "steps": [
            ("Code each case",
             "Mark each case y, n or - against each account: consistent, inconsistent, or "
             "silent. Give the page for each mark."),
            ("Count each record",
             "For each account, count the cases it absorbs, fails and is silent on."),
            ("Find the survivors",
             "List the accounts that fail no case. With every case shown, there are none."),
            ("Find the split",
             "List the cases on which one account has y and the other n. A case marked n "
             "against silent is not a split."),
            ("State what neither account is",
             "Describe the tacit cogito from the chapter's own sentences, without scoring it."),
        ],
        "worked": {
            "title": "Three cases, two accounts",
            "intro": [
                "Code the written cogito, the speaker's surplus and the illusory love against "
                "thought before language and language before thought.",
            ],
            "lines": [
                "thought first:  y, n, n",
                "language first:  n, y, silent",
                "records:  1 of 3, fails 2;  1 of 3, fails 1",
                "survivors:  none",
                "split:  cases 1 and 2",
            ],
            "after": [
                "Each account fails somewhere, and each survives only a table chosen for it. "
                "The illusory love fails thought before language and finds language before "
                "thought silent, so it is not a split. What neither account captures is the "
                "chapter's tacit cogito, which the lesson states and does not score.",
            ],
        },
        "quiz_title": "The spoken and the tacit cogito",
        "quiz": [
            {"q": "Language before thought is coded n, y and silent on the three cases. What "
                  "is its record?",
             "a": ["absorbs 1 of 3, fails 1, silent 1", "absorbs 1 of 3, fails 2, silent 0",
                   "absorbs 2 of 3, fails 1, silent 0", "absorbs 1 of 2, fails 1, silent 0"],
             "c": 0,
             "why": "One y, one n and one silent cell out of three cases. Counting the silent "
                    "cell as a failure gives fails 2, counting it as absorbed gives 2 of 3, and "
                    "dropping it from the total gives 1 of 2."},
            {"q": "What does the chapter mean by a spoken cogito?",
             "a": ["The cogito reached through Descartes's words, whose true formula would be "
                   "one thinks, therefore one is",
                   "A cogito said aloud rather than thought silently",
                   "Descartes's first, unwritten experience of his own existence",
                   "The cogito as it is used in everyday conversation"],
             "c": 0,
             "why": "The spoken cogito is the one put into words and understood in words, a me "
                    "in idea. Saying it aloud is not the point, since reading silently gives the "
                    "same thing. Descartes's unwritten glimpse of his existence is what the "
                    "chapter calls the tacit cogito he was seeking."},
            {"q": "Which describes the tacit cogito as the chapter presents it?",
             "a": ["A presence of oneself to oneself, prior to words, that knows itself only "
                   "under threat and is a cogito only once expressed",
                   "A silent sentence, I think, said inwardly before it is said aloud",
                   "A complete thought that words later clothe",
                   "An unconscious representation of the self"],
             "c": 0,
             "why": "The chapter says the tacit cogito cannot yet be thought, knows itself in "
                    "the dread of death or another's gaze, and is a cogito only when it has "
                    "found expression. A silent sentence would already be words, the clothing "
                    "view is the one it rejects, and it denies that what lies beneath is an "
                    "unconscious."},
            {"q": "In the expression preset, language before thought survives. What does that "
                  "show?",
             "a": ["Only that it fails none of the two cases shown; the full table has no "
                   "survivor",
                   "That the chapter holds language before thought",
                   "That thought before language is refuted by the book",
                   "That the illusory love is a case about language"],
             "c": 0,
             "why": "A survivor is a count over the cases chosen. With the first case restored, "
                    "language before thought fails it. The chapter says that view forgets half "
                    "the truth, the coding is the lesson's, and the love is in the table as a "
                    "case about self-knowledge."},
        ],
        "mistakes": [
            ("Thinking the tacit cogito is a silent inner voice that thinks in words before speaking",
             "The chapter says the opposite. The tacit cogito is not yet a thought in words "
             "at all: it speaks as we sing when we are happy, knows itself only under "
             "threat, and &ldquo;is a cogito only when it has found expression for "
             "itself&rdquo;. An inner voice saying I think would already be a spoken cogito, "
             "spoken silently. The lab cannot show the difference, which is why the tacit "
             "cogito is in the prose and not in the table, where both coded accounts fail."),
            ("Thinking the chapter puts language before thought",
             "It raises that conclusion and rejects it: it would be to forget half the truth. "
             "Words such as cogito and sum would be meaningless to me, the chapter says, if I "
             "were not already in contact with my own life and thought, and that is why "
             "languages can be translated and learned."),
            ("Taking the table's result for the chapter's verdict",
             "Survivors none is a count over three cases the lesson chose and coded. It "
             "shows that each account fails somewhere on that coding; it does not show that "
             "the tacit cogito is right, which is never a column and never scored."),
        ],
        "standard": (
            "Finish when you can count two accounts over the cases and say what neither is.",
            "Given cases coded against two accounts of language and thought, compute each "
            "account's record, the survivors and the split, and describe the tacit cogito "
            "from the chapter's own sentences."
        ),
        "note": (
            "The table is the lesson's coding of three cases, one of them from the chapter's "
            "earlier pages on feeling; the count is exact and the coding is an "
            "interpretation. The tacit cogito itself is disputed, first by Merleau-Ponty, "
            "whose late working notes call it impossible, and the lab cannot represent "
            "anything that is not yet expressed."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Smith p. 477 (opening passage: "Change presupposes ... Time
    # presupposes a view of time."; the water from the glacier; "this often
    # repeated metaphor is in reality extremely confused"; "shapes cut out by
    # a finite observer"); p. 478 (Heraclitus; the bank and the boat; "like a
    # storm on the horizon"; "arises from my relation to things"; "the water
    # which will flow by tomorrow is at this moment at its source"; "What is
    # past or future for me is present in the world."; Leibniz, Augustine;
    # "The objective world is too much of a plenum for there to be time.");
    # p. 479 (instances of now; Bergson on memory); p. 480 (the table's
    # traces); pp. 481-482 (time constituted by consciousness; time brought
    # down to one level); p. 483 (a dimension of our being).
    {
        "slug": "time-is-not-in-things",
        "title": "Time Is Not in Things",
        "module": "Part Three · 2 · Temporality",
        "one_line": "The river of time smuggles in an observer: in things there is only the present of each, and past and future need someone for whom they are past and future.",
        "summary": (
            "Temporality opens with the oldest image of time, a river, and shows that it "
            "works only with a witness on its bank. Classify the same water as past and "
            "future from the bank and from a boat carried by the current, then remove the "
            "observer and see what is left."
        ),
        "key": [
            "no events without someone they happen to",
            "bank: water gone by is past",
            "bank: water at the source is to come",
            "boat: the reverse, from the same water",
            "no observer: past none, future none",
            "past and future are present in the world",
        ],
        "key_label": "The river in six lines",
        "concepts_intro": (
            "Temporality's first pages take away two homes for time, the world and the "
            "contents of consciousness. Three ideas carry them."
        ),
        "concepts": [
            ("Objective time",
             "Time as a feature of the world in itself, a succession of instants with no one "
             "to whom they are present. The chapter argues there is no such time: the world "
             "alone holds only what is."),
            ("The witness",
             "The observer the river image tacitly includes. Past and future appear only "
             "from a standpoint, and two standpoints on the same water give opposite answers."),
            ("A trace",
             "A mark the past leaves in the present, in a table or a brain. The chapter "
             "argues that no trace, bodily or psychic, can by itself give a consciousness of "
             "the past, because a trace is present."),
        ],
        "read_title": "The passage first, then the chapter's first seven pages",
        "read_intro": (
            "The passage is the chapter's diagnosis of the river image. The lesson starts "
            "with the image as the chapter gives it, follows the diagnosis, then reads the "
            "pages that refuse time a home in memory."
        ),
        "body": [
            ("p", "<strong>Part Three, Chapter 2, p. 477.</strong> &ldquo;Change presupposes "
                  "a certain position which I take up and from which I see things in "
                  "procession before me: there are no events without someone to whom they "
                  "happen and whose finite perspective is the basis of their individuality. "
                  "Time presupposes a view of time.&rdquo; The sentences are on page 477 of "
                  "Smith's translation. Read the chapter from its first page, 476, to the end "
                  "of the paragraph at the top of page 483, in your own copy before going on."),
            ("p", "Stand on a bridge and watch the water. It came down from the hills, it is "
                  "under you now, and it will reach the sea, and nothing seems more natural "
                  "than to say that time flows the same way. The chapter begins exactly there: "
                  "the water I see rolling by was made ready a few days ago in the mountains "
                  "with the melting of the glacier, and it makes its way towards the sea. If "
                  "time is like a river, it flows from the past towards the present and the "
                  "future. And then: &ldquo;this often repeated metaphor is in reality "
                  "extremely confused&rdquo; (p. 477)."),
            ("p", "Why confused? In the objective world, the melting of the snows and what "
                  "follows from it are not successive events at all. To say that the glacier "
                  "produced, the day before yesterday, the water passing now, I must assume a "
                  "witness tied to a spot, who saw the snow melt and followed the water down, "
                  "or waited two days on the bank for the wood he threw in at the source. The "
                  "events are &ldquo;shapes cut out by a finite observer&rdquo; from the "
                  "world's totality; the world itself, taken alone, is one indivisible being "
                  "that does not change. That is the passage. Change needs a position from "
                  "which things are seen in procession, and time presupposes a view of time."),
            ("p", "The image is old. Heraclitus, the Greek philosopher of around 500 BC, is "
                  "remembered for saying that you cannot step into the same river twice, and "
                  "the chapter says the metaphor has lasted from his time to ours only because "
                  "we surreptitiously put a witness of its course into the river. We do it "
                  "already when we say that the stream discharges itself into the sea, as "
                  "though it had an inside that showed itself outside (p. 478)."),
            ("p", "Now put the witness in openly, and the relations reverse. Stand him on the "
                  "bank: the water already carried by is sinking into the past, and what is to "
                  "come is on the side of the source, &ldquo;like a storm on the "
                  "horizon&rdquo;. The lab's model makes this a count. The <code>bank</code> "
                  "preset puts seven parcels of water at positions 1 to 7, the source at 1, "
                  "and an observer on the bank at 4. The world tile lists each parcel at its "
                  "position. The past tile prints w5, w6, w7, the water that has gone by; the "
                  "future tile prints w1, w2, w3, the water still on its way; w4 is in front "
                  "of him."),
            ("p", "Put him in a boat instead, carried by the current. Then, the chapter says, "
                  "he is moving downstream towards his future, though the future lies in the "
                  "new landscapes waiting at the estuary, and the course of time is no longer "
                  "the stream but the landscape rolling by. The lab's model keeps the water "
                  "and the positions and changes only the standpoint. The "
                  "<code>current</code> preset prints past w1, w2, w3 and future w5, w6, w7: "
                  "the same water, the opposite answer. The chapter puts the boatman's future "
                  "in the landscape, not the water, and the lab, which has only positions, "
                  "counts what lies ahead of the boat."),
            ("p", "Then take the observer away. The <code>none</code> preset prints none for "
                  "the past and none for the future, and the world tile still lists every "
                  "parcel at its place. That is the chapter's claim: within things, &ldquo;the "
                  "water which will flow by tomorrow is at this moment at its source&rdquo;, "
                  "and the water just passed is a little further down the valley. "
                  "&ldquo;What is past or future for me is present in the world&rdquo; (p. "
                  "478). Time is not a real process that I record; it arises from my relation "
                  "to things."),
            ("def", ("Time presupposes a view of time",
                     "The chapter's thesis that past and future are not properties of things "
                     "but appear only for someone situated among them, so that a world "
                     "without a standpoint holds only what is.")),
            ("p", "It is often said, the chapter goes on, that in things the future is not "
                  "yet and the past is no longer, so that only an infinitesimal present is "
                  "left. That is why Leibniz could call the objective world a momentary mind, "
                  "and why Saint Augustine, the bishop of Hippo whose <em>Confessions</em> "
                  "of about 400 made the question famous, needed a presence of the "
                  "past and of the future besides the presence of the present. The chapter "
                  "reads them in its own way: the world is not too narrow to hold time; "
                  "&ldquo;The objective world is too much of a plenum for there to be "
                  "time&rdquo;. What being lacks, to be temporal, is not-being: elsewhere, "
                  "formerly, tomorrow."),
            ("p", "Moving time into consciousness does not help if consciousness is again a "
                  "series of nows. Psychologists explain the past by memories and the future "
                  "by memories projected ahead. Henri Bergson, the most widely read French "
                  "philosopher of the century's first decades, had refuted the physiological "
                  "theory of memory in <em>Matter and Memory</em> (1896), showing that "
                  "nothing in the brain accounts for how memories are lost in aphasia. The "
                  "chapter accepts the refutation and turns it on Bergson's own memories kept "
                  "in the unconscious: no trace, bodily or psychic, makes consciousness of the "
                  "past understandable. The table bears my initials and an ink stain; the "
                  "traces are present, and they point to the past only for someone who "
                  "already has a sense of it (pp. 479&ndash;480)."),
            ("p", "The last escape is the idealist's: say that consciousness constitutes time, "
                  "laying out past, present and future as its objects. Then time is "
                  "brought down to one uniform level, every moment spread out before thought "
                  "at once, and it is no longer time (pp. 481&ndash;482). There is time only "
                  "if it is never completely laid out. Its synthesis must always be "
                  "undertaken afresh, and the chapter will look for it in experience rather "
                  "than above it."),
            ("p", "Where, then? In the present I am living through, with the day behind it "
                  "and the evening ahead. The next lesson, “The Field of Presence”, reads the "
                  "diagram Husserl drew of it."),
        ],
        "lab": ("phenkit", {
            "mode": "time",
            "view": "river",
            "model": "the lesson's model of the chapter's river",
            "preset": "bank",
            "presets": [
                {"id": "bank", "label": "Water at 1 to 7, the source at 1, an observer on the bank at 4",
                 "parcels": "w1, 1; w2, 2; w3, 3; w4, 4; w5, 5; w6, 6; w7, 7", "observer": 4, "standpoint": "bank",
                 "expect": {"tiWorld": "w1 at 1, w2 at 2, w3 at 3, w4 at 4, w5 at 5, w6 at 6, w7 at 7",
                            "tiPast": "w5, w6, w7", "tiFuture": "w1, w2, w3"}},
                {"id": "current", "label": "The same water, the observer carried by the current from 4",
                 "parcels": "w1, 1; w2, 2; w3, 3; w4, 4; w5, 5; w6, 6; w7, 7", "observer": 4, "standpoint": "current",
                 "expect": {"tiPast": "w1, w2, w3", "tiFuture": "w5, w6, w7"}},
                {"id": "none", "label": "The same water, no observer",
                 "parcels": "w1, 1; w2, 2; w3, 3; w4, 4; w5, 5; w6, 6; w7, 7", "observer": "none",
                 "expect": {"tiPast": "none", "tiFuture": "none"}},
            ],
            "panel_title": "The river from two standpoints",
            "panel_intro": (
                "This lab is the lesson's model of the chapter's river: parcels of water at "
                "positions, and a rule for what counts as past and future from the bank and "
                "from the current. Switch from the bank preset to the none preset. It "
                "computes classifications, not anyone's sense of time."
            ),
        }),
        "steps_title": "Classifying the river's water",
        "steps_intro": "Four steps; the last is the chapter's.",
        "steps": [
            ("Place the water",
             "Number the parcels along the river from the source; the source is at 1."),
            ("Classify from the bank",
             "For an observer on the bank, water downstream of him has gone by and is past; "
             "water upstream, still coming, is future."),
            ("Classify from the boat",
             "For an observer carried by the current, what lies ahead downstream is future "
             "and what lies behind is past."),
            ("Remove the observer",
             "With no standpoint, every parcel is simply at its position: nothing is past "
             "and nothing is future."),
        ],
        "worked": {
            "title": "Seven parcels and an observer at 4",
            "intro": [
                "Take water at positions 1 to 7, the source at 1, and an observer at 4. You "
                "want past and future on the bank, in a boat, and with no one there.",
            ],
            "lines": [
                "bank:  past w5, w6, w7;  future w1, w2, w3",
                "boat:  past w1, w2, w3;  future w5, w6, w7",
                "no observer:  past none;  future none",
            ],
            "after": [
                "The water is the same in all three, and the two standpoints classify it in "
                "opposite ways. Without a standpoint the lab finds no past and no future, "
                "only parcels at their places, which is the chapter's claim that what is past "
                "or future for me is present in the world.",
            ],
        },
        "quiz_title": "The river and its witness",
        "quiz": [
            {"q": "Water at positions 1 to 7, the source at 1, and an observer on the bank at "
                  "2. What does the model count as past?",
             "a": ["w3, w4, w5, w6, w7", "w1", "w1, w2", "none"],
             "c": 0,
             "why": "From the bank, water downstream has gone by: everything beyond position 2. "
                    "w1, upstream, is still to come; w2 is in front of him; and none is the "
                    "answer only with no observer."},
            {"q": "With no observer the lab prints none for past and future. What does the "
                  "chapter say is left in the world?",
             "a": ["Each thing present where it is: what is past or future for me is present "
                   "in the world",
                   "A past that no longer is and a future that is not yet",
                   "Only an infinitesimal instant",
                   "Time flowing on as before, unobserved"],
             "c": 0,
             "why": "The chapter says past and future exist only too unmistakably in the world, "
                    "in the present. The not-yet and no-longer, with an infinitesimal present, "
                    "is what it reports is often said and then reinterprets; time flowing on "
                    "unobserved is the river image it calls confused."},
            {"q": "Why does the observer on the bank put what is to come on the side of the "
                  "source?",
             "a": ["Because the water still on its way to him comes from there",
                   "Because the past pushes the present into being",
                   "Because the source is higher than the bank",
                   "Because the glacier is older than the sea"],
             "c": 0,
             "why": "From the bank, the water yet to reach him is upstream. The chapter denies "
                    "that the past pushes the present; height and age are facts about the "
                    "landscape, not about what is to come for him."},
            {"q": "What is the chapter's objection to explaining the past by traces, in the "
                  "brain or in the unconscious?",
             "a": ["A trace is present, and points to the past only for someone who already "
                   "has a sense of the past",
                   "Traces fade too quickly to be useful",
                   "The brain stores no traces at all",
                   "Traces are reliable only for the recent past"],
             "c": 0,
             "why": "The table's initials are in the present; a revived perception would be a "
                    "fresh perception. The objection is not about how long traces last or how "
                    "reliable they are, and it does not depend on whether the brain stores any."},
        ],
        "mistakes": [
            ("Thinking past and future are in the world, and we only observe them",
             "The lab gives the chapter's answer a shape. From the bank, w5 to w7 are past and "
             "w1 to w3 future; from the boat, the reverse; with no observer, neither. The "
             "water did not change; only the standpoint did. In things there is only the "
             "present of each, and past and future need someone for whom they are past and "
             "future: &ldquo;Time presupposes a view of time.&rdquo;"),
            ("Thinking the chapter makes time unreal, or a construction of the mind",
             "It refuses the idealist's way out as firmly as the realist's: time laid out as "
             "the object of a constituting consciousness is time brought down to one level, "
             "and no longer time. Time arises from my relation to things, which needs both "
             "the things and someone situated among them."),
            ("Taking the lab's two standpoints for the chapter's two kinds of time",
             "The lab computes positions relative to a point. The chapter's boat case puts "
             "the future in the landscapes ahead, not in the water, and its point is that "
             "the image changes with the witness. The figures are the lesson's model, not a "
             "theory of time."),
        ],
        "standard": (
            "Finish when you can classify the river from two standpoints and with none.",
            "Given parcels of water at positions and an observer, compute what counts as "
            "past and as future from the bank and from the current, show that without an "
            "observer neither exists, and state the chapter's conclusion from it."
        ),
        "note": (
            "The model is the lesson's: positions on a line and a rule for each standpoint. "
            "It cannot represent what the chapter says time needs, a not-being that only a "
            "subject brings, or the field of presence the next lesson reads; and the "
            "boatman's future, which the chapter places in the landscape, it places in the "
            "water ahead."
        ),
    },
]
