"""Things, the World and Others, lessons 5-7 -- the end of Part Two, Chapter 3, and Chapter 4.

Every quotation is copied from Colin Smith's translation, Routledge Classics
pagination (Chapter 3's pages on hallucination run pp. 389-402; Chapter 4,
Other Selves and the Human World, runs pp. 403-425); the comment beside each
lesson gives its pages. Smith's ligatures are printed as plain letters, a word
split by a line-break hyphen is joined, footnote numerals are left out, and
Smith's single quote marks inside a quotation are printed as
&lsquo;...&rsquo;. Nothing else is changed.

Chapter 4 has no section breaks of its own. The lessons divide it where it
turns, on p. 414, from the perception of others ("But is it indeed other
people that we arrive at in this way?") to what that perception cannot
overcome.
"""

LESSONS = [
    # ---------------------------------------------------------------- 05
    # Smith p. 395 (opening passage: "The victim of hallucination enjoys no
    # such belief ... or to the experience of the sane"); p. 389
    # ("Hallucination causes the real to disintegrate ... a quasi-reality in
    # its place"; "The all-important point ..."; the pricking and the
    # injection; the man in the garden, "'Yes, there is someone there, but
    # it's somebody else.'"); p. 390 (the gramophone voices; the powder, damp
    # and dry; the guinea pig; telephone and radio; Alain and Montaigne);
    # pp. 390-1 (the patients argue against their hallucinations; the rats;
    # the doctor in the boat); p. 391 (empiricism's physiological account; the
    # common priority of objective thought; the intellectualist cogito);
    # pp. 392-4 (we must understand him; the insulin injection; the doctor
    # with the patient); pp. 394-5 (the perceived world as the one possible
    # for me and for others; "Can't you hear my voices?"; "packed with small
    # perceptions"; the initiative comes from us); pp. 395-6 (no thickness of
    # duration; the dream); p. 396 (hallucination bears on one's own body;
    # "as if I heard with my mouth"; extracampine hallucination); p. 397
    # (mescalin, Sartre's unpublished self-observation; short-lived
    # phenomena); p. 398 (not a judgement; the woman at the market); p. 399
    # ("The hallucination is not a perception, but it has the value of
    # reality"; one primordial function; the normal person); p. 400 (primary
    # opinion, Husserl's Urdoxa); pp. 400-1 (no apodeictic certainty; the
    # sunrise; another perception which rectifies it); p. 402 (I know myself
    # only in ambiguity). The patients' reports are the sources' (Zucker,
    # Minkowski, Schroeder, Specht, Jaspers, Straus, Menninger-Lerchental).
    # The modern aside (PLAN F.1) is Anil Seth's, in the second-last p.
    {
        "slug": "hallucination",
        "title": "Hallucination",
        "module": "Part Two · 3 · The Thing · Hallucination",
        "one_line": "The patients the chapter reports tell their hallucinations from their perceptions, and the chapter reads what a hallucination lacks as what makes a perceived thing real.",
        "summary": (
            "The chapter ends with hallucination, which takes the real apart and puts a "
            "quasi-reality in its place. Its sources' patients mostly tell hallucination from "
            "perception, so it is neither a sensation nor a false belief. Compute what a coded "
            "set of perceived things has in common, and what a reported hallucination lacks "
            "of it: a place in the shared world, a path to the rest of experience, detail, "
            "depth in time."
        ),
        "key": [
            "the patients tell the two apart",
            "not a sensation, not a judgement",
            "core: shared world, explorable, detail",
            "hallucination: no path to the rest",
            "still, it has the value of reality",
        ],
        "key_label": "Hallucination in five lines",
        "concepts_intro": (
            "The chapter reads hallucination to confirm what it has said about the thing and "
            "the world. Three ideas carry that reading."
        ),
        "concepts": [
            ("Hallucination",
             "An experience of a voice, a figure or a touch with nothing in the world to "
             "answer to it. The chapter's sources are clinical, and its patients are mainly "
             "people diagnosed with schizophrenia, delirium tremens and senile dementia, as "
             "the psychiatry of the early twentieth century reported them."),
            ("The perceived world's texture",
             "What the chapter says a real thing has and a hallucination lacks: a place in "
             "the one world others share, a path from it to the rest of experience, an "
             "inexhaustible fullness of detail, and depth in time."),
            ("Primary opinion",
             "The chapter's name, after Husserl's <em>Urdoxa</em>, for the faith that "
             "places us in the world before any science or verification. Perception and "
             "hallucination both draw on it, which is how a hallucination can take a "
             "perception's place."),
        ],
        "read_title": "The passage first, then the pages on hallucination line by line",
        "read_intro": (
            "The passage is the chapter's summary of what a hallucination lacks. The lesson "
            "goes back to the patients' reports with which the pages begin, follows the "
            "argument against both classical accounts, and then reads the passage and what "
            "follows it."
        ),
        "body": [
            ("p", "<strong>Part Two, Chapter 3, p. 395.</strong> &ldquo;The victim of "
                  "hallucination enjoys no such belief: the hallucinatory phenomenon is no part "
                  "of the world, that is to say, it is not accessible, there is no definite path "
                  "leading from it to all the remaining experiences of the deluded subject, or "
                  "to the experience of the sane.&rdquo; The sentence is from page 395 of "
                  "Smith's translation. Read the chapter's last part from its first line on "
                  "page 389 to the chapter's end on page 402, in your own copy before going on."),
            ("p", "The pages begin with their claim: &ldquo;Hallucination causes the real to "
                  "disintegrate before our eyes, and puts a quasi-reality in its place&rdquo;, "
                  "and so confirms what the chapter has said about the thing and the world. The "
                  "evidence is the testimony of patients, taken from the psychiatrists the "
                  "chapter cites: Zucker, Minkowski, Schröder, Jaspers and others. They were "
                  "people in hospital care, reported as the clinical literature of the time "
                  "reported them. The book's argument concerns the reports as given, and the "
                  "lab codes those reports, not the people they describe."),
            ("p", "&ldquo;The all-important point is that the patients, most of the time, "
                  "discriminate between their hallucinations and their perceptions.&rdquo; "
                  "Patients who feel hallucinated pricking or an electric current jump at a "
                  "real injection and tell the doctor that this time he was the cause. A man "
                  "who said he saw someone standing in the garden under his window was shown a "
                  "real person placed at the spot, dressed and standing the same way, and said, "
                  "&ldquo;&lsquo;Yes, there is someone there, but it&rsquo;s somebody "
                  "else.&rsquo;&rdquo; An old woman who complained of powder in her bed found "
                  "a real layer of toilet powder there and asked what it was: this powder was "
                  "damp, the other was dry (pp. 389&ndash;90). Patients often say the voices "
                  "come by telephone or radio, which the chapter reads as their way of saying "
                  "that the morbid world is artificial."),
            ("p", "The empiricist account is the natural first answer, and at its strength it "
                  "is simply physiology: some irritation of a nerve centre produces sense-data "
                  "just as a stimulus acting on the same centre would, so a hallucination is a "
                  "perception with an inner cause instead of an outer one (p. 391). But then the "
                  "patients should not be able to tell the two apart, and they can; the "
                  "hallucination, the chapter concludes, is not a sensory content."),
            ("p", "Then it must be a judgement or a belief: that is the intellectualist answer, "
                  "and the chapter states it through the French philosopher Alain, who quotes "
                  "Montaigne on madmen who believe they see what they do not really see. The "
                  "patients, the chapter replies, do not believe they see; questioned, they "
                  "correct themselves, and they argue against their hallucinations: rats cannot "
                  "come out of the mouth and go back into the stomach, and a doctor who heard "
                  "voices rowed out to sea to convince himself no one was speaking. When the "
                  "attack comes, the rat and the voices are still there (pp. 390&ndash;1). A "
                  "hallucination is not a belief for the same reason it is not a sensation: "
                  "either would posit it as true, which is just what the patients do not do."),
            ("p", "What the two accounts share, page 391 says, is the priority of objective "
                  "thought. Each has one mode of being, the objective, and forces the "
                  "hallucination into it: for empiricism it is an event in a causal chain, and "
                  "for intellectualism, starting from a consciousness that knows everything it "
                  "contains, a false perception cannot really be a perception at all, which "
                  "leaves no way to understand how a consciousness could be deceived about what "
                  "it constitutes. The method the chapter proposes instead is to understand the "
                  "patient, not to take him at his word and not to reduce his experience to the "
                  "doctor's: the doctor with the patient, as the chapter puts it, is a "
                  "two-sided phenomenon in which each learns to know the other (pp. "
                  "392&ndash;4)."),
            ("p", "Now the passage. I call my interlocutor's voices hallucinations because I "
                  "find nothing like them in my own world; what I see is the only possible "
                  "spectacle for me and for others, and other spectators' views are implied in "
                  "mine as the back of a thing is perceived with its front. The hallucination "
                  "has none of this. It is <em>not accessible</em>: no path leads from it to "
                  "the rest of the patient's experience, or to anyone else's. &ldquo;&lsquo;Can&rsquo;t "
                  "you hear my voices?&rsquo; asks the patient; &lsquo;then I must be the only "
                  "one to hear them.&rsquo;&rdquo; And so it lacks the real thing's fullness: &ldquo;The "
                  "hallucinatory thing is not, as is the real thing, packed with small "
                  "perceptions which sustain it in existence.&rdquo; It has no depth that holds "
                  "a thickness of duration, and where a perceived thing answers my intention "
                  "from outside, with a phantasm the initiative comes from me (pp. 395&ndash;6)."),
            ("p", "The lab computes what a set of things has in common, on the lesson's coding "
                  "of these pages. Each perceived thing is coded with five properties: "
                  "<em>in-the-shared-world</em>, <em>explorable</em>, "
                  "<em>packed-with-detail</em>, <em>thick-with-duration</em> and "
                  "<em>real-for-me</em>, and with the sense it is given to. Each hallucination "
                  "is coded with the one property the chapter leaves it: on page 399, it "
                  "&ldquo;has the value of reality&rdquo; for the patient. In the "
                  "<code>vision</code> preset, the real person placed in the garden and the man "
                  "the patient saw there: the tile <strong>core</strong> lists all six of the "
                  "person's properties, the sense included, since there is only one perceived "
                  "thing to compare, and the tile <strong>break</strong> says the patient's man "
                  "lacks five of them: <em>seen</em>, since page 397 says the thing in "
                  "hallucination is never seen and never visible, and the four that place a thing in the "
                  "world. Nothing varies, so the tile for what varies reads <em>none</em>. The <code>voice</code> preset does the same for a voice from "
                  "the next room and the voices a patient hears."),
            ("p", "The <code>all</code> preset sets three perceived things, a voice from the "
                  "next room, the person placed in the garden and the damp powder in the bed, "
                  "beside the dry powder of the old woman's complaint. The core is the five "
                  "properties; the tile <strong>vary</strong> lists what differs among the "
                  "perceived things, <em>heard</em>, <em>seen</em> and <em>touched</em>; and the "
                  "break is the four the dry powder lacks. What every perceived thing has, on "
                  "this coding, is not a sense but a place in one world, and that is what the "
                  "hallucination lacks. The coding is the lesson's, and a reader could add a "
                  "property the chapter mentions, or code one differently."),
            ("p", "Where, then, is the hallucination? Not in the world but before it, page 396 "
                  "says, because the patient's body no longer has its place in the system of "
                  "appearances. All hallucination bears first on one's own body: patients say "
                  "it is as if they heard with their mouth. A man under mescalin, in a "
                  "self-observation by Jean-Paul Sartre that the chapter cites, saw the world "
                  "covered in swellings, then everything clammy and scaly like serpents, and "
                  "felt that the world simply is thus (p. 397). Most hallucinations, the chapter "
                  "adds, are not many-sided things but brief phenomena, pricks, jolts, sparks "
                  "and draughts; a real thing such as a rat appears only in its general style."),
            ("p", "And yet the patient may stand by the hallucination against every argument. "
                  "A woman who felt a gaze fall on her at the market like a blow could not say "
                  "it came from a person in common space, and the arguments against her left "
                  "her unmoved (p. 398). &ldquo;The hallucination is not a perception, but it "
                  "has the value of reality&rdquo;, page 399 says, and it can take a "
                  "perception's place only because hallucination and perception are modes of "
                  "one primordial function by which we set up a world around us. The normal "
                  "person, the chapter adds, has the same wound through which illusion enters: "
                  "we believe what we see without verifying it, on a primary faith that Husserl "
                  "called <em>Urdoxa</em>."),
            ("p", "So the chapter's conclusion cuts both ways (pp. 400&ndash;2). Perception has "
                  "no apodeictic certainty, the certainty of a proof, and consciousness is not "
                  "fully transparent to itself, or hallucination could not happen. But the "
                  "perceived is not therefore merely probable: the sun rises for the scientist "
                  "as for anyone, each perception is replaced only by another that corrects it, "
                  "and what is certain is that there is a world. I know myself, the chapter "
                  "ends, only in ambiguity."),
            ("p", "One modern view runs close to this chapter and the other way from it. The "
                  "neuroscientist Anil Seth, in <em>Being You</em> (2021), describes perception "
                  "as a controlled hallucination, a phrase he did not coin: the brain's best "
                  "guess about the causes of its signals, held in check by those signals, so "
                  "that a hallucination is the same process less held in check. That runs the "
                  "other way from the chapter, which argues that a hallucination lacks what "
                  "perception has, not that perception is a hallucination kept in check. Both "
                  "sides can point to the page. The chapter itself makes perception and "
                  "hallucination modes of one function, says that with a phantasm the "
                  "initiative comes from us, and in a footnote on page 395 repeats without "
                  "objection the Hungarian philosopher Melchior Palágyi's description of "
                  "perception as a &ldquo;direct phantasm&rdquo; and hallucination as an "
                  "&ldquo;inverse phantasm&rdquo;; a reader of Seth can point to all three. "
                  "Against him, what the chapter says perception has is a place in a world "
                  "shared with others and a fullness of detail, not a better-checked guess. "
                  "Neither the chapter nor the lab settles the dispute."),
            ("p", "The world the patient falls out of is a world shared with others, and the "
                  "next chapter asks how there can be others at all. The next lesson, “The "
                  "Cultural World and Others”, begins it."),
        ],
        "lab": ("phenkit", {
            "mode": "variation",
            "view": "core",
            "preset": "all",
            "presets": [
                {"id": "voice",
                 "label": "A voice from the next room, and the voices a patient hears (the lesson's coding)",
                 "variants": "a voice from the next room, yes, heard in-the-shared-world explorable "
                             "packed-with-detail thick-with-duration real-for-me; "
                             "the voices a patient hears, no, real-for-me",
                 "expect": {"vrCore": "heard, in-the-shared-world, explorable, packed-with-detail, "
                                      "thick-with-duration, real-for-me",
                            "vrVary": "none",
                            "vrBreak": "the voices a patient hears lacks heard, in-the-shared-world, "
                                       "explorable, packed-with-detail, thick-with-duration"}},
                {"id": "vision",
                 "label": "The person placed in the garden, and the man the patient saw there (p. 389)",
                 "variants": "the person placed in the garden, yes, seen in-the-shared-world explorable "
                             "packed-with-detail thick-with-duration real-for-me; "
                             "the man the patient saw, no, real-for-me",
                 "expect": {"vrCore": "seen, in-the-shared-world, explorable, packed-with-detail, "
                                      "thick-with-duration, real-for-me",
                            "vrBreak": "the man the patient saw lacks seen, in-the-shared-world, "
                                       "explorable, packed-with-detail, thick-with-duration"}},
                {"id": "all",
                 "label": "Three perceived things and the dry powder of a complaint (pp. 389-90)",
                 "variants": "a voice from the next room, yes, heard in-the-shared-world explorable "
                             "packed-with-detail thick-with-duration real-for-me; "
                             "the person placed in the garden, yes, seen in-the-shared-world explorable "
                             "packed-with-detail thick-with-duration real-for-me; "
                             "the damp powder in the bed, yes, touched seen in-the-shared-world explorable "
                             "packed-with-detail thick-with-duration real-for-me; "
                             "the dry powder of the complaint, no, real-for-me",
                 "expect": {"vrCore": "in-the-shared-world, explorable, packed-with-detail, "
                                      "thick-with-duration, real-for-me",
                            "vrVary": "heard, seen, touched",
                            "vrBreak": "the dry powder of the complaint lacks in-the-shared-world, "
                                       "explorable, packed-with-detail, thick-with-duration"}},
            ],
            "panel_title": "What every perceived thing has, and a hallucination lacks",
            "panel_intro": (
                "This lab computes the invariant core of a set of variants on the lesson's "
                "coding of the chapter's reports: what every perceived thing keeps, what "
                "varies among them, and what a hallucination lacks of the core. The count is "
                "exact; the coding is the lesson's reading of pages 389 to 399, and the patients "
                "are known only through their doctors' reports."
            ),
        }),
        "steps_title": "Computing a core and what a variant lacks",
        "steps_intro": "Four steps, the last of which the chapter takes and the lab does not.",
        "steps": [
            ("Code each variant from the page",
             "List each perceived thing with the properties the chapter gives a real thing, "
             "and each hallucination with what the chapter leaves it. Mark which are of the "
             "kind, perceived things, and which are not."),
            ("Intersect the variants of the kind",
             "The core is what every perceived thing has. A property one of them lacks, such "
             "as a particular sense, goes into the list of what varies."),
            ("Compare the excluded variant with the core",
             "List the core properties the hallucination lacks. That list is what, on this "
             "coding, separates it from the perceived things."),
            ("Read the result against the patients' reports",
             "The patients say the hallucination is not the same thing as what they see. The "
             "core and the break are the lesson's way of setting out what the chapter says "
             "the difference is; they do not show what the experience is like."),
        ],
        "worked": {
            "title": "Three perceived things and the dry powder",
            "intro": [
                "Code the all preset as above and compute the core, what varies, and what "
                "the dry powder lacks.",
            ],
            "lines": [
                "core:  shared world, explorable, detail,",
                "       duration, real for me",
                "varies:  heard, seen, touched",
                "dry powder has:  real for me",
                "dry powder lacks:  the other four",
            ],
            "after": [
                "On this coding a perceived thing is not marked out by any one sense but by "
                "its place in one explorable world. The hallucination keeps only the value of "
                "reality it has for the patient, which, the chapter says, is enough for it to "
                "take a perception's place.",
            ],
        },
        "quiz_title": "Hallucination and the real",
        "quiz": [
            {"q": "Variants of a kind: A has p q r; B has p q s; C has p r s. Excluded: D has q. "
                  "What is the core, and what does D lack?",
             "a": ["Core p; D lacks p", "Core p q; D lacks p",
                   "Core p q r s; D lacks p r s", "Core q; D lacks nothing"],
             "c": 0,
             "why": "Only p is in all three of A, B and C, so the core is p, and D, which has "
                    "only q, lacks it. q is missing from C, so it varies. The union p q r s is "
                    "not the core, and q is not in every variant."},
            {"q": "Why does the chapter reject the empiricist account of hallucination?",
             "a": ["Nerve centres cannot be irritated",
                   "The patients mostly tell their hallucinations from their perceptions",
                   "Hallucinations are always visual",
                   "The patients believe whatever they see"],
             "c": 1,
             "why": "If a hallucination were a sensation from an inner cause, it should be "
                    "indistinguishable from a perception, and the patients distinguish them. "
                    "The chapter does not dispute the physiology as such; the schizophrenic's "
                    "hallucinations, it says, are mostly auditory and tactile; and the patients "
                    "do not believe they see."},
            {"q": "Why, on the chapter's reading, is a hallucination not a judgement either?",
             "a": ["Judgements are always correct",
                   "The patients cannot speak about what they experience",
                   "A judgement would posit it as true, which the patients do not do",
                   "A hallucination is a sensory content"],
             "c": 2,
             "why": "Page 390: the judgement or belief could only consist in positing the "
                    "hallucination as true, and that is just what the patients do not do; they "
                    "argue against it. Judgements can be false, the patients' reports are the "
                    "chapter's evidence, and the chapter denies that it is a sensory content."},
            {"q": "How does the lesson's aside set Anil Seth's view beside the chapter?",
             "a": ["Seth and the chapter agree that hallucination is a false belief",
                   "Seth's experiments show the chapter is wrong",
                   "Seth's view is the chapter's, in modern words",
                   "Seth calls perception a controlled hallucination; the chapter says a "
                   "hallucination lacks what perception has"],
             "c": 3,
             "why": "The two run in opposite directions, and the lesson states both sides: the "
                    "chapter's one function and its initiative from us are close to Seth, its "
                    "shared world is not. Neither holds hallucination a false belief, and the "
                    "lesson says neither the chapter nor the lab settles the dispute."},
        ],
        "mistakes": [
            ("Thinking a hallucination is a perception without an object, experienced exactly as one",
             "If it were, the patients could not tell the two apart, and the chapter's sources "
             "report that most of the time they do: the real powder is damp and the other dry, "
             "the real man in the garden is somebody else. On the lesson's coding the "
             "hallucination keeps only <em>real-for-me</em> and lacks the four properties every "
             "perceived thing has, a place in the shared world, a path to the rest of "
             "experience, detail, and depth in time."),
            ("Concluding that hallucination is a false belief",
             "Since it is not a sensation, the intellectualist concludes, it must be a "
             "judgement. The chapter's patients do not believe in their hallucinations as they "
             "believe in perceived things; they argue against them, and still the voices are "
             "there. A belief posits its object as true, and that is what they do not do."),
            ("Reading the chapter as saying perception is infallible",
             "Because the hallucination lacks what perception has, it can seem that perception "
             "can never mislead. The chapter says the opposite: perception has no apodeictic "
             "certainty, the normal person has the same wound through which illusion enters, "
             "and what is certain is only that there is a world, in which each perception can "
             "be corrected by another."),
        ],
        "standard": (
            "Finish when you can compute the core and the break and state why hallucination "
            "is neither sensation nor judgement.",
            "Given a coded set of perceived things and a hallucination, compute the core, what "
            "varies and what the hallucination lacks; state the empiricist and intellectualist "
            "accounts at strength and the chapter's objection to each, from the patients' "
            "reports."
        ),
        "note": (
            "The patients are known only through the clinical reports the chapter cites, and "
            "the lab codes the reports, not the patients; the properties are the lesson's "
            "reading of pages 389 to 399. The lab computes a core and a difference. It cannot "
            "compute what a hallucination is like for the person who has it, which the chapter "
            "itself says no one can coincide with, and the modern dispute over whether "
            "perception is a controlled hallucination is beyond what any table here could test."
        ),
    },
    # ---------------------------------------------------------------- 06
    # Smith p. 410 (opening passage: "There is nothing here resembling
    # 'reasoning by analogy'. As Scheler so rightly declares, reasoning by
    # analogy presupposes what it is called on to explain. ... Now the
    # perception of others is anterior to, and the condition of, such
    # observations"); pp. 403-4 (nature at the centre of subjectivity; the
    # first twenty-five years; natural time); p. 405 (the cultural world:
    # roads, a bell, a spoon, a pipe; footmarks in the sand; the evacuated
    # house; ruins; the presence of others beneath a veil of anonymity);
    # p. 406 (the reply by analogy, in the voice of "the theory"; how can the
    # word 'I' be put into the plural; "The very first of all cultural objects
    # ... vehicle of a form of behaviour"); pp. 406-7 ("a difficulty and an
    # outrage for objective thought"; two modes of being; the contradictory
    # operation); pp. 407-9 (the body as a third genus of being; "If my
    # consciousness has a body, why should other bodies not 'have'
    # consciousnesses?"; Cartesianism right about molecules); p. 410 (the
    # baby of fifteen months; "'Biting' has immediately, for it, an
    # intersubjective significance"; correlations as a clue when direct
    # perception fails; the internal relation); pp. 411-12 (one world in which
    # we all participate as anonymous subjects; the vortex; the child and
    # cultural objects; the body image); p. 413 (language and dialogue; the
    # child); pp. 413-14 (Piaget; Hegel's struggle). Mill is not named in the
    # chapter.
    {
        "slug": "the-cultural-world-and-others",
        "title": "The Cultural World and Others",
        "module": "Part Two · 4 · Other Selves and the Human World",
        "one_line": "The argument from analogy concludes to other minds from bodies like mine, and the chapter's objection is not that it is invalid but that it presupposes the perception of the other it was meant to explain.",
        "summary": (
            "Chapter 4 begins with the things people leave behind them, a spoon, a pipe, "
            "footprints in the sand, and asks how a thought can be seen outside the person "
            "who thinks it. Set out the argument from analogy for other minds, test it for "
            "validity, repair it, and see why the chapter, following Scheler, says the "
            "argument presupposes what it was meant to explain."
        ),
        "key": [
            "analogy: p, q, so r is invalid",
            "add q → r: valid, by modus ponens",
            "but q already needs r: a circle",
            "the first cultural object: another's body",
            "the baby bites back before any analogy",
        ],
        "key_label": "Analogy and its circle in five lines",
        "concepts_intro": (
            "The chapter moves from the cultural world to the other person who makes it "
            "human. Three ideas are needed to follow it."
        ),
        "concepts": [
            ("The cultural object",
             "A thing shaped by the human use it serves, a road, a bell, a spoon, which "
             "carries an atmosphere of humanity with it. The chapter's question is how a "
             "first-person act can settle into such a thing and be met there anonymously."),
            ("The argument from analogy",
             "The classical argument for other minds: my behaviour is joined to my mind; that "
             "body behaves as mine does; so its behaviour is joined to a mind. John Stuart "
             "Mill gave it its best-known form in 1865, as an inference from like effects to "
             "like causes."),
            ("Behaviour",
             "The chapter's alternative starting point. Another person is given first as a "
             "pattern of behaviour, a way of dealing with the world that my own body takes up "
             "directly, not as a moving object whose mind has to be inferred."),
        ],
        "read_title": "The passage first, then the chapter's first eleven pages line by line",
        "read_intro": (
            "The passage is the chapter's verdict on the argument from analogy. The lesson "
            "goes back to the cultural world where the chapter begins, follows the problem "
            "objective thought makes of other people, tests the argument in the lab, and "
            "reads the chapter's alternative."
        ),
        "body": [
            ("p", "<strong>Part Two, Chapter 4, p. 410.</strong> &ldquo;There is nothing here "
                  "resembling &lsquo;reasoning by analogy&rsquo;. As Scheler so rightly "
                  "declares, reasoning by analogy presupposes what it is called on to explain. "
                  "&hellip; Now the perception of others is anterior to, and the condition of, "
                  "such observations&rdquo;. The sentences are from page 410 of Smith's "
                  "translation, in the chapter titled &ldquo;Other Selves and the Human "
                  "World&rdquo;. Read the chapter from its first page, 403, to the paragraph on "
                  "page 414 that asks whether it is indeed other people that we arrive at, in "
                  "your own copy before going on."),
            ("p", "The chapter begins with nature inside me. My decisions give my past a "
                  "meaning after the event, but a natural time runs beneath my personal history "
                  "and is never wholly taken up by it, and my earliest years lie behind me like "
                  "an unknown land (pp. 403&ndash;4). Then the turn: just as nature reaches into "
                  "personal life, behaviour settles into nature as a cultural world. I live "
                  "among roads, villages, churches, a bell, a spoon, a pipe, each moulded to the "
                  "action it serves. A few footprints in the sand carry a faint atmosphere of "
                  "humanity; a house just abandoned, gone through room by room, a very definite "
                  "one (p. 405)."),
            ("p", "How is that possible? In the cultural object, the chapter says, I feel the "
                  "close presence of others beneath a veil of anonymity: someone uses the pipe "
                  "for smoking and the bell for summoning. The easy answer, given on page 406 in "
                  "the voice of the theory the chapter is about to question, is analogy: I see "
                  "what other people do with the implements around me and interpret their "
                  "behaviour by analogy with my own, whose meaning I know from inside. The "
                  "chapter's question is what that answer assumes: how can the word "
                  "<em>I</em> be put into the plural at all? And its first claim: &ldquo;The "
                  "very first of all cultural objects, and the one by which all the rest exist, "
                  "is the body of the other person as the vehicle of a form of behaviour.&rdquo;"),
            ("p", "The existence of other people, page 406 says, is &ldquo;a difficulty and an "
                  "outrage for objective thought&rdquo;, and the next page shows why. If "
                  "the body is the object the physiologist studies, then there are two modes of "
                  "being and only two, being in itself, the being of things in space, and being "
                  "for itself, the being of consciousness. Another person would have to be both "
                  "at once: an object over there, and a consciousness with no outside, which I "
                  "can reach only by being it. If I constitute the world, I cannot conceive "
                  "another consciousness that constitutes it too, for then I would not be the "
                  "constituting one. There is no room for other people in objective thought."),
            ("p", "The chapter's way out is the book's account of the body. If the body is not "
                  "an object but, as page 408 puts it, a third kind of being between the pure "
                  "subject and the object, and if consciousness is not a pure being-for-itself "
                  "but perceptual consciousness, being-in-the-world, the difficulty changes "
                  "shape: &ldquo;If my consciousness has a body, why should other bodies not "
                  "&lsquo;have&rsquo; consciousnesses?&rdquo; How meaning could come to dwell in "
                  "molecules or masses of cells can never be made intelligible, the chapter "
                  "grants, and there Cartesianism is right; but the body of experience is not "
                  "that, and another person can appear at the top of their phenomenal body."),
            ("p", "Now the passage. The argument from analogy, as the chapter states it, "
                  "deduces the other consciousness by comparing the other's expressions of "
                  "emotion with mine and recognising exact correlations between my behaviour "
                  "and my inner events. Max Scheler, the German phenomenologist whose book on "
                  "sympathy (1913, revised 1923) argued that we perceive other minds directly, "
                  "had objected that this reasoning presupposes what it is called on to explain, "
                  "and the chapter agrees. The perception of others comes first and makes the "
                  "comparisons possible; the comparisons do not make the perception."),
            ("p", "The example follows at once. A baby of fifteen months opens its mouth if I "
                  "playfully take one of its fingers between my teeth and pretend to bite it. It "
                  "has hardly seen its own face in a mirror, and its teeth are not like mine "
                  "anyway. Its own mouth, felt from inside, is something to bite with, and my "
                  "jaw, seen from outside, is at once capable of the same intentions: "
                  "&ldquo;&lsquo;Biting&rsquo; has immediately, for it, an intersubjective "
                  "significance.&rdquo; There was no resemblance for the baby to reason from. "
                  "Observed correlations, the chapter allows, may give me a clue when I set out "
                  "methodically to know someone, or when direct perception fails; they do not "
                  "teach me that others exist."),
            ("p", "The lab writes the argument in sentence letters. Let <em>p</em> be "
                  "<em>my behaviour expresses a mind</em>, <em>q</em> <em>that body behaves "
                  "as mine does</em>, and <em>r</em> <em>that body's behaviour expresses a "
                  "mind</em>. The <code>analogy</code> preset has premises p and q and "
                  "conclusion r. The truth table has 8 rows, the tile <strong>rows</strong>; "
                  "one of them, p and q true with r false, makes both premises true and the "
                  "conclusion false, the tile <strong>counterexample rows</strong>; and the tile "
                  "<strong>verdict</strong> reads <em>Invalid</em>. That is no surprise and no "
                  "objection: Mill, whom the chapter does not name, offered the argument as an inference from like effects to "
                  "like causes, which is inductive and was never meant to force its conclusion."),
            ("p", "The <code>valid</code> preset adds the premise the argument needs to become "
                  "deductive: <em>q → r</em>, whatever behaves as I do expresses a mind. Now no "
                  "row makes all three premises true and r false, the counterexample tile reads "
                  "0, and the verdict is <em>Valid</em>; the shape that does the work, from q and "
                  "<em>q → r</em> to r, is the one logicians call modus ponens. The tile <strong>form</strong>, which looks "
                  "an argument up in a catalogue of named shapes, reads <em>no catalogued "
                  "form</em> for all three presets, because each carries the premise p beside "
                  "the shape that does the work. The repair costs something, since the new premise "
                  "is a strong general claim, but the form is now beyond reproach."),
            ("p", "The <code>circle</code> preset is the lesson's way of setting the chapter's "
                  "objection out in the lab's terms. To know that premise q is true, that the body over there "
                  "<em>behaves</em> as mine does rather than merely moves, I must already "
                  "perceive it as conduct, the conduct of someone, and that is what r says. So "
                  "the preset gives the premises p and r and the conclusion r, over 4 rows, "
                  "since q has dropped out. The lab calls it valid, and it is; a conclusion that is already among the premises cannot "
                  "be false when they are true. The argument has become circular. On this "
                  "reading, that is what presupposing what it is called on to explain amounts "
                  "to, and no truth table "
                  "can catch it, since a circular argument is perfectly valid."),
            ("def", ("Presupposing what it explains",
                     "An argument presupposes its conclusion when the evidence for one of its "
                     "premises already requires the conclusion to be true. It can be valid, as "
                     "the circle preset is, and still give no support, because it could convince "
                     "only someone who already accepted where it ends.")),
            ("p", "What takes analogy's place is an internal relation between my body as I live "
                  "it and the other's body as I see it, page 410 says, which makes the other "
                  "appear as the completion of the system. As soon as my gaze falls on a living "
                  "body in action, the things around it take on a new layer of meaning: they "
                  "are what this other behaviour is about to make of them, and a kind of vortex "
                  "forms round the body towards which my world is drawn (pp. 411&ndash;12). The "
                  "child finds cultural objects around it like meteorites from another planet "
                  "and learns to use them because its body schema, which Smith translates as "
                  "the body image, makes what it sees done correspond at once to what it does."),
            ("p", "Language is the cultural object that matters most, page 413 says. In dialogue a "
                  "common ground forms; my thoughts and the other's are woven into a single "
                  "fabric, and his objection draws from me thoughts I did not know I had. The "
                  "child, as the Swiss psychologist Jean Piaget described it, lives in a world it "
                  "believes open to everyone and knows nothing of points of view; at about "
                  "twelve, Piaget says, it reaches the cogito. The chapter replies that the "
                  "child's outlook must be in some way vindicated against the adult's, for with "
                  "the cogito begins the struggle in which, as Hegel says, each consciousness "
                  "seeks the death of the other, and for that struggle to begin at all there "
                  "must first be a common ground (pp. 413&ndash;14)."),
            ("p", "And here the chapter turns on itself. Having found the other in shared "
                  "behaviour and shared speech, it asks whether it has found <em>other "
                  "people</em> at all, or only a confusion of selves. The next lesson, “The "
                  "Truth of Solipsism”, reads that question."),
        ],
        "lab": ("argkit", {
            "mode": "validity",
            "preset": "analogy",
            "show": "all",
            "presets": [
                {"id": "analogy",
                 "label": "The argument from analogy: p, q, so r",
                 "premises": ["p", "q"], "conclusion": "r",
                 "expect": {"vaRows": "8", "vaCounter": "1", "vaVerdict": "Invalid"}},
                {"id": "valid",
                 "label": "The deductive repair: p, q, q → r, so r",
                 "premises": ["p", "q", "q -> r"], "conclusion": "r",
                 "expect": {"vaRows": "8", "vaCounter": "0", "vaVerdict": "Valid",
                            "vaForm": "no catalogued form"}},
                {"id": "circle",
                 "label": "The circle: the repair's evidence is the conclusion, so p, r, so r",
                 "premises": ["p", "r"], "conclusion": "r",
                 "expect": {"vaRows": "4", "vaCounter": "0", "vaVerdict": "Valid"}},
            ],
            "panel_title": "Does the argument from analogy force its conclusion",
            "panel_intro": (
                "This lab tests whether premises force a conclusion, row by row over every "
                "assignment of true and false. Here p is my behaviour expressing a mind, q that "
                "body behaving as mine does, and r that body's behaviour expressing a mind. The "
                "logic is undisputed; what the letters stand for is the lesson's setting out of "
                "the argument."
            ),
        }),
        "steps_title": "Setting out the argument from analogy",
        "steps_intro": "Four steps; the last is the chapter's, and the lab cannot take it.",
        "steps": [
            ("Assign the sentence letters",
             "Write each claim the argument uses as one letter, and keep a key: p for my "
             "behaviour expressing my mind, q for the other body behaving as mine, r for its "
             "behaviour expressing a mind."),
            ("Test the bare argument",
             "Look for a row that makes every premise true and the conclusion false. One such "
             "row makes the argument invalid; an inductive argument is expected to have one."),
            ("Add the premise that makes it valid",
             "Find the general claim that closes the gap, here q → r, and check that no "
             "counterexample row is left."),
            ("Ask how each premise would be known",
             "For each premise, say what evidence it rests on. If the evidence for a premise "
             "already requires the conclusion, the argument presupposes what it explains, "
             "however valid its form."),
        ],
        "worked": {
            "title": "The argument from analogy, three ways",
            "intro": [
                "Take p, q and r as in the lab and test each version.",
            ],
            "lines": [
                "p, q, so r:  8 rows, 1 counterexample",
                "  the counterexample: p true, q true, r false",
                "p, q, q → r, so r:  0 counterexamples",
                "p, r, so r:  0 counterexamples, circular",
            ],
            "after": [
                "The repair turns an invalid argument into a valid one, and the circle is valid "
                "too. The chapter's objection is not to the form but to the evidence for q: to "
                "see that body as behaving like mine, I already perceive it as someone's "
                "conduct.",
            ],
        },
        "quiz_title": "Analogy and the perception of others",
        "quiz": [
            {"q": "An argument has premises p and p → q and conclusion q. How many of its four "
                  "rows are counterexamples?",
             "a": ["1", "0", "2", "4"],
             "c": 1,
             "why": "A counterexample needs p true, p → q true and q false; but with p true and "
                    "q false, p → q is false. So no row qualifies, and the argument, modus "
                    "ponens, is valid. One counterexample is what p, q, so r has."},
            {"q": "What is the chapter's objection to the argument from analogy?",
             "a": ["It is invalid because it is inductive",
                   "It fails because no two bodies ever behave exactly alike",
                   "It presupposes the perception of others that it is meant to explain",
                   "It relies on the baby's knowledge of its own face"],
             "c": 2,
             "why": "Page 410, after Scheler: reasoning by analogy presupposes what it is called "
                    "on to explain, since the perception of others is anterior to the "
                    "observations. Being inductive is the misconception the lesson answers. The "
                    "chapter never asks for exact likeness; the baby's unlike teeth show that "
                    "the perception does not wait for any likeness, and the baby has hardly "
                    "seen its own face."},
            {"q": "Why does the circle preset come out valid in the lab?",
             "a": ["Because r is a tautology",
                   "Because its premises cannot all be true together",
                   "Because the lab cannot detect bad arguments",
                   "Its conclusion is one of its premises, so no row makes the premises true "
                   "and the conclusion false"],
             "c": 3,
             "why": "With r among the premises, any row that makes the premises true makes r "
                    "true. r is not true in every row, and p and r can both be true. The lab "
                    "detects invalidity correctly; circularity is not invalidity, which is the "
                    "lesson's point."},
            {"q": "On the chapter's account, what does the fifteen-month-old baby show?",
             "a": ["That biting has a shared meaning for it before any comparison of bodies",
                   "That babies reason by analogy faster than adults",
                   "That it has learned its face from a mirror",
                   "That the other's body is an object it must interpret"],
             "c": 0,
             "why": "It opens its mouth though it has hardly seen its own face and its teeth are "
                    "unlike mine; biting has an intersubjective significance for it at once. "
                    "That leaves no room for an inference from resemblance, and no room for the "
                    "body as an object to be interpreted."},
        ],
        "mistakes": [
            ("Thinking the argument from analogy fails only because it is inductive",
             "Mill offered it as an induction, and an induction is expected to fall short of "
             "proof: the analogy preset has one counterexample in 8 rows. Add the general "
             "premise q → r and the argument is valid. The chapter's objection survives the "
             "repair. It presupposes what it should explain: to know q, that the body over "
             "there behaves as mine does, I must already perceive it as behaviour, someone's "
             "conduct, which is what r says."),
            ("Concluding that the chapter calls other minds an inference after all",
             "The chapter allows that observed correlations can help when I set out to know "
             "someone methodically or when direct perception fails. It denies that they teach "
             "me that others exist: the perception of others comes first and is the condition "
             "of those observations."),
            ("Reading the “two modes of being” as the chapter's own view",
             "Being in itself and being for itself, and the impossible demand that another "
             "person be both, are objective thought's terms, set out on page 407 to show why it "
             "has no room for others. The chapter's answer is a body that is a third kind of "
             "being, between the pure subject and the object."),
        ],
        "standard": (
            "Finish when you can test the argument, repair it, and say why the repair does not "
            "answer the chapter.",
            "Write the argument from analogy in sentence letters, find its counterexample row, "
            "add the premise that makes it valid, and explain in the chapter's terms why the "
            "valid argument still presupposes what it was meant to explain."
        ),
        "note": (
            "The truth tables are exact, and the logic is undisputed. What the lab cannot "
            "compute is how a premise is known, so it cannot see circularity: the circle preset "
            "is valid, and its fault lies in the evidence. Whether we perceive other people "
            "directly, as Scheler and the chapter hold, is a question about perception that no "
            "truth table settles."
        ),
    },
    # ---------------------------------------------------------------- 07
    # Smith p. 419 (opening passage: "Contrary to the social world ... strip
    # them of all their human significance. ... The truth of solipsism is
    # there."); p. 414 ("But is it indeed other people that we arrive at in
    # this way?"; the alter Ego follows the Ego); pp. 414-15 (I perceive the
    # grief or anger of the other in his conduct); p. 415 ("For him these
    # situations are lived through, for me they are displayed"; Paul, his
    # wife, his watch; the common project; objective thought and the cogito
    # not fictions; the interworld still a project of mine); p. 416 (no alter
    # Ego without reciprocity; the unequal couple; the chessboards; the
    # other's gaze strips me of part of my being); p. 417 ("There is here a
    # solipsism rooted in living experience and quite insurmountable"; the
    # insatiable being); pp. 417-18 (the escape into a universal subject and
    # God; Spinoza); p. 418 (a multiple solipsism; "Solitude and
    # communication cannot be the two horns of a dilemma, but two 'moments' of
    # one phenomenon"); p. 419 (given to myself; freedom as a fate;
    # Malebranche); pp. 419-20 (I can fly from being only into being; a
    # solipsist philosophy addresses a community; Valery); p. 420 ("it is
    # asserted" that the other transforms me into an object; "In fact the
    # other's gaze transforms me into an object, and mine him, only if both of
    # us withdraw into the core of our thinking nature"; the stranger; the
    # dog; the stranger who speaks); p. 421 (the philosopher's meditation is
    # dialogue; transcendental subjectivity is intersubjectivity; "a
    # permanent field or dimension of existence"); pp. 421-3 (Peguy; the
    # Russian peasants of 1917; Fabrice at Waterloo; class and nation as
    # modes of co-existence); pp. 423-5 (transcendence; death; "my life has a
    # social atmosphere just as it has a flavour of mortality"; a
    # phenomenology of phenomenology; the return to the cogito). Sartre is not
    # named in these pages; Hegel is named on p. 414 and Scheler on p. 410.
    # The baby and the dialogue are on pp. 410 and 413, read in lesson 06.
    {
        "slug": "the-truth-of-solipsism",
        "title": "The Truth of Solipsism",
        "module": "Part Two · 4 · Other Selves and the Human World",
        "one_line": "There is a solipsism rooted in lived experience that the chapter says cannot be overcome, and beneath it a coexistence with others that it says is lived before any withdrawal.",
        "summary": (
            "Having found the other in shared behaviour, the chapter asks whether it has "
            "found other people at all. It answers that the other's grief is displayed to me "
            "and lived by him, that a lived solipsism cannot be surpassed, and that solitude "
            "and communication are two moments of one phenomenon. Compute the records of "
            "analogy and of the objectifying look over four of the chapter's cases, and find "
            "the case both absorb and the case both fail."
        ),
        "key": [
            "his grief: lived by him, displayed to me",
            "a solipsism rooted in lived experience",
            "the look objectifies only if both withdraw",
            "solitude and communication: one phenomenon",
            "the social: a permanent field",
        ],
        "key_label": "Others and solitude in five lines",
        "concepts_intro": (
            "The second half of the chapter holds two claims together that seem to exclude "
            "each other. Three ideas are needed to see how."
        ),
        "concepts": [
            ("Lived solipsism",
             "Not the theory that only I exist, but the fact that every experience, of others "
             "included, is lived by me and from my side, so that I never live the other's "
             "experience as he does. The chapter says this cannot be surpassed."),
            ("The objectifying look",
             "The view that the other's gaze turns me into an object and mine turns him into "
             "one, so that two freedoms can only deny each other. The chapter states it as "
             "something &ldquo;asserted&rdquo; and does not name its author; it is widely "
             "read as Sartre's."),
            ("Coexistence",
             "The life shared with others before either withdraws into a private point of "
             "view: the dialogue, the common situation, the social world as a dimension of "
             "existence. The chapter's claim is that it is lived beneath solitude, not that it "
             "removes it."),
        ],
        "read_title": "The passage first, then the chapter's last twelve pages line by line",
        "read_intro": (
            "The passage is where the chapter names the truth in solipsism. The lesson goes "
            "back to the turn on page 414, follows the chapter through the other's grief and "
            "the failure of every escape, counts two accounts against its cases, and ends with "
            "the social world."
        ),
        "body": [
            ("p", "<strong>Part Two, Chapter 4, p. 419.</strong> &ldquo;Contrary to the social "
                  "world I can always use my nature as a sensory being, close my eyes, stop up "
                  "my ears, live as a stranger in society, treat others, ceremonies and "
                  "institutions as mere arrangements of colour and light, and strip them of all "
                  "their human significance. &hellip; The truth of solipsism is there.&rdquo; "
                  "The sentences are from page 419 of Smith's translation. Read the chapter from "
                  "the paragraph on page 414 that asks whether it is indeed other people we "
                  "arrive at to the end of the chapter and of Part Two on page 425, in your own "
                  "copy before going on."),
            ("p", "The last lesson ended with a common world, shared in behaviour and in speech. "
                  "On page 414 the chapter doubts its own result. If the perceiving subject is "
                  "anonymous, the other it perceives is anonymous too, and in a collective "
                  "consciousness the difficulty of a plurality of consciousnesses comes back. "
                  "I do perceive the other's grief or anger in his conduct, in his face and his "
                  "hands, without any recourse to an inner experience of my own. But his "
                  "behaviour, and even his words, are not the other."),
            ("p", "The example is a friend. &ldquo;For him these situations are lived through, "
                  "for me they are displayed.&rdquo; Paul suffers because he has lost his wife, "
                  "or is angry because his watch has been stolen; I suffer because Paul is "
                  "grieved, or am angry because he is angry, and our situations cannot be laid "
                  "one on the other (p. 415). Even a project we undertake together is not one "
                  "project, since Paul is Paul and I am myself. And this, the chapter insists, "
                  "is not a leftover of objective thought: the uniqueness of the cogito is a "
                  "well-founded phenomenon, and the conflict is there even in the blindness of "
                  "sacrifice, where the interworld I enter is still a project of mine."),
            ("p", "Reciprocity is not guaranteed either (p. 416). In a couple where one loves more "
                  "than the other, one throws his whole life into the love while the other "
                  "stays free; and if the second tries to reciprocate by making himself a mere "
                  "phenomenon in the other's world, he can do so only by an expansion of his "
                  "own life. Then the chapter's strongest sentence on page 417: &ldquo;There is "
                  "here a solipsism rooted in living experience and quite "
                  "insurmountable.&rdquo; I am the one by whom every experience is lived, and "
                  "with my first perception an insatiable being was launched that appropriates "
                  "everything it meets."),
            ("p", "Can it be escaped from inside? As a universal subject, an impartial spectator, "
                  "I would stand above myself and the other on equal terms; in God I could be "
                  "conscious of others as of myself. The chapter answers that the subjectivity "
                  "it has found is not God's, and that a love of others in God would in the end, "
                  "as Spinoza said, be God's love of himself through me (pp. 417&ndash;18). So "
                  "the problem returns in all its difficulty: consciousnesses present the "
                  "absurdity of a multiple solipsism. And the chapter's turn is a sentence: "
                  "&ldquo;Solitude and communication cannot be the two horns of a dilemma, but "
                  "two &lsquo;moments&rsquo; of one phenomenon&rdquo;, since in fact other "
                  "people do exist for me. If my experience did not present others, I could not "
                  "even call them inaccessible."),
            ("p", "Now the passage. I am given to myself, page 419 says, already situated in a "
                  "physical and social world, and my freedom, my power to be the subject of all "
                  "my experiences, is a fate: I cannot reduce myself to anything I experience. "
                  "So against the social world I can always fall back on my senses, close my "
                  "eyes and treat ceremonies as patches of colour, and against the natural world "
                  "I can fall back on thought and doubt each perception. <em>The truth of "
                  "solipsism is there.</em> But I can fly from being only into being, the "
                  "chapter goes on: from society into nature, from the real world into an "
                  "imagined one made of its fragments. Even a solipsist philosophy is written "
                  "for a community of speakers, and even the indefinite refusal to be anything, "
                  "in Paul Valéry's phrase, refuses something."),
            ("p", "The objectifying look comes next, and the chapter introduces it as something "
                  "asserted: the other turns me into an object and denies me, I turn him into "
                  "one and deny him. That is widely read as the analysis Jean-Paul Sartre gave in <em>Being and "
                  "Nothingness</em> (1943), where being seen by another reveals me as an object "
                  "in his world and is felt as shame, and the chapter answers it without naming "
                  "him. At its strength it explains why the other's presence can feel like a "
                  "theft of my world. The reply on page 420: &ldquo;In fact the other's gaze "
                  "transforms me into an object, and mine him, only if both of us withdraw into "
                  "the core of our thinking nature&rdquo;, if each feels his actions observed "
                  "like an insect's instead of taken up. That happens under a stranger's gaze; "
                  "but it is unbearable only because it takes the place of a possible "
                  "communication, and a dog's gaze embarrasses no one. Let the stranger say a "
                  "word, or make a gesture of impatience, and he already ceases to transcend me."),
            ("p", "The lab sets two opponents' accounts of other people against four of the "
                  "chapter's cases, in the lesson's coding. The argument from analogy, from the "
                  "last lesson, knows the other by inference from behaviour like mine; the "
                  "objectifying look knows him directly, as a gaze that makes me an object. "
                  "Scheler's account, that others are perceived directly in their expression, "
                  "is the one the chapter drew on and is not a column. The cases: the baby who "
                  "opens its mouth (p. 410), analogy <strong>n</strong>, since it has nothing to "
                  "reason from, the look <strong>y</strong>, since the other is given without "
                  "inference; Paul's grief, lived by him and displayed to me, <strong>y</strong> "
                  "for both, since each keeps the other's experience his own; the dialogue in "
                  "which two thoughts are woven into one fabric (p. 413), <strong>n</strong> for "
                  "both, since there is neither an inference nor an object; and the stranger's "
                  "silent gaze, <strong>-</strong> for analogy, which says nothing about being "
                  "looked at, and <strong>y</strong> for the look."),
            ("p", "With all four, the <code>all</code> preset, the tile <strong>record</strong> "
                  "gives analogy one case absorbed, two failed and one silent, and the look "
                  "three absorbed and one failed; the tile <strong>survivors</strong> reads "
                  "<em>none</em>; and the tile <strong>split</strong>, the cases on which the "
                  "two part, names the baby alone, since the stranger's gaze is a silence for "
                  "analogy and not a failure. Both absorb the grief, and that is the table's "
                  "version of the truth in solipsism. Both fail the dialogue. The "
                  "<code>infant</code> preset shows the baby alone, and there the look survives; "
                  "the <code>dialogue</code> preset shows the grief and the dialogue, and "
                  "neither survives and nothing splits them. The coding is the lesson's, cell by "
                  "cell, and the baby in particular is coded y for the look only because the "
                  "look's account gives the other without inference."),
            ("def", ("A permanent field",
                     "The chapter's term, on page 421, for how the social is given: "
                     "&ldquo;a permanent field or dimension of existence&rdquo;, which I can "
                     "turn away from but never cease to be situated in relation to, as I am "
                     "always situated in the natural world.")),
            ("p", "The chapter's own account is stated, not scored. Solipsism would be strictly "
                  "true only of someone tacitly aware of existing without being or doing "
                  "anything, which is impossible, page 421 says, since to exist is to be in and "
                  "of the world. Even the philosopher's meditation, which seems to cut him off "
                  "from everyone, is an act, a spoken word, and so a dialogue. "
                  "&ldquo;Transcendental subjectivity is a revealed subjectivity, revealed to "
                  "itself and to others, and is for that reason an intersubjectivity.&rdquo; "
                  "Both claims stand: the truth of solipsism, and the coexistence lived beneath "
                  "it. The chapter does not refute the first; it says what it cannot reach."),
            ("p", "The social world is the last example. It is as false, page 421 says, to put "
                  "ourselves in society as an object among objects as to put society in "
                  "ourselves as an object of thought. Charles Péguy found at the end of his "
                  "<em>Notre Patrie</em> a buried voice that had never stopped speaking; the "
                  "Russian peasants of 1917 joined the workers of Petrograd and Moscow because "
                  "they felt they shared a fate, and class was lived before it was willed. "
                  "Stendhal's Fabrice wanted to see the Battle of Waterloo as one sees a "
                  "landscape and found only confused episodes; the Emperor's map and the "
                  "historian's account miss it too. The true Waterloo, the chapter says, is what "
                  "comes about on the fringes of all their perspectives (p. 422)."),
            ("p", "Part Two ends on page 425 with transcendence in general. I shall never live "
                  "through the presence of another to himself, as I shall never live through the "
                  "instant of my own death, and yet each other person exists for me as an "
                  "unchallengeable style of coexistence: my life has a social atmosphere as it "
                  "has a flavour of mortality. A philosophy centred on such a contradiction, the "
                  "chapter grants, would be meaningless if it only laid bare magical "
                  "experiences; it needs a phenomenology of phenomenology, and a return to the "
                  "cogito. The next course, “The Cogito, Time and Freedom”, begins there, with "
                  "“The Cogito and the Certainty of Seeing”."),
        ],
        "lab": ("phenkit", {
            "mode": "cases",
            "view": "table",
            "accounts": ["the argument from analogy", "the objectifying look"],
            "preset": "all",
            "presets": [
                {"id": "all",
                 "label": "All four cases (the lesson's coding of pp. 410-420)",
                 "observations": "the baby who opens its mouth, n, y; "
                                 "Paul’s grief lived by him and displayed to me, y, y; "
                                 "a dialogue woven into one fabric, n, n; "
                                 "the stranger’s silent gaze, -, y",
                 "expect": {"caRecord": "the argument from analogy: absorbs 1 of 4, fails 2, silent 1; "
                                        "the objectifying look: absorbs 3 of 4, fails 1, silent 0",
                            "caSurvivors": "none",
                            "caSplit": "the baby who opens its mouth"}},
                {"id": "infant",
                 "label": "The baby of fifteen months (p. 410)",
                 "observations": "the baby who opens its mouth, n, y",
                 "expect": {"caSurvivors": "the objectifying look",
                            "caSplit": "the baby who opens its mouth"}},
                {"id": "dialogue",
                 "label": "Paul's grief and the dialogue (pp. 413, 415)",
                 "observations": "Paul’s grief lived by him and displayed to me, y, y; "
                                 "a dialogue woven into one fabric, n, n",
                 "expect": {"caSurvivors": "none", "caSplit": "none"}},
            ],
            "panel_title": "Two accounts of other people against four cases",
            "panel_intro": (
                "This lab counts the lesson's coding of the chapter's cases against two "
                "opponents' accounts of how others are known: by analogy from behaviour like "
                "mine, and directly, as a look that makes me an object. The count is exact and "
                "the coding is an interpretation. Scheler's account and the chapter's own are "
                "in the prose and are not columns."
            ),
        }),
        "steps_title": "Reading the table of others",
        "steps_intro": "Four steps; the last carries the chapter's two claims.",
        "steps": [
            ("State both accounts at strength",
             "Analogy: the other's mind is an inference, sound as far as like effects have "
             "like causes. The look: the other is met directly, as a freedom whose gaze makes "
             "me an object in his world."),
            ("Code each case, and mark silence",
             "Mark y where an account absorbs the case as the chapter reports it, n where it "
             "cannot, and - where it says nothing. A silence is not a failure and does not "
             "enter the split."),
            ("Count records, survivors and the split",
             "Find what each account absorbs and fails, whether either fails nothing, and the "
             "cases where one absorbs and the other fails."),
            ("Read the case both absorb and the case both fail",
             "The case both absorb is the truth the chapter grants solipsism; the case both "
             "fail is the coexistence it says is lived beneath it. State both, in prose."),
        ],
        "worked": {
            "title": "Four cases, two accounts",
            "intro": [
                "Code the four cases as the lesson does and count.",
            ],
            "lines": [
                "baby:  analogy n, look y",
                "Paul's grief:  analogy y, look y",
                "dialogue:  analogy n, look n",
                "stranger's gaze:  analogy silent, look y",
                "analogy: 1 absorbed, 2 failed, 1 silent",
                "look: 3 absorbed, 1 failed",
                "survivors: none; split: the baby",
            ],
            "after": [
                "Both accounts absorb the grief, which is lived by Paul and only displayed to "
                "me: that is the truth in solipsism. Both fail the dialogue, in which neither "
                "of us is an object for the other: that is the coexistence the chapter says "
                "is lived beneath it, and it is stated here in prose, not scored.",
            ],
        },
        "quiz_title": "Solitude and coexistence",
        "quiz": [
            {"q": "Two accounts, A and B. Cases: one is y for A and n for B; one is - for A and "
                  "y for B; one is n for both. Which cases are in the split?",
             "a": ["The first and the second", "All three", "Only the first",
                   "None, since both accounts fail something"],
             "c": 2,
             "why": "The split is the cases where one account absorbs and the other fails. The "
                    "second is a silence for A, not a failure, and the third is a failure for "
                    "both. That both fail something decides the survivors, not the split."},
            {"q": "What does the chapter call insurmountable?",
             "a": ["The theory that only I exist",
                   "The conflict between two looks that objectify each other",
                   "The gap between my body and the other's body",
                   "A solipsism rooted in living experience"],
             "c": 3,
             "why": "Page 417: a solipsism rooted in living experience and quite insurmountable, "
                    "the fact that every experience is lived by me. The theory that only I "
                    "exist is not what is meant. The objectifying conflict, page 420 says, "
                    "happens only if both withdraw, and the bodies, the last lesson showed, form "
                    "one system."},
            {"q": "When, according to page 420, does the other's gaze transform me into an "
                  "object?",
             "a": ["Only if both of us withdraw into the core of our thinking nature",
                   "Whenever he looks at me",
                   "Only when he speaks to me",
                   "Never, since the look is Sartre's error"],
             "c": 0,
             "why": "The chapter's reply to what it says is asserted: only if both of us "
                    "withdraw and make ourselves an inhuman gaze. It is not whenever he looks: a "
                    "dog's gaze causes no embarrassment, and a word ends the stranger's distance. "
                    "And the chapter grants that it does happen, under a stranger's gaze, so "
                    "'never' is wrong."},
            {"q": "Does the chapter refute solipsism?",
             "a": ["Yes: the dialogue proves that other minds exist",
                   "No: it grants a truth in solipsism and holds that coexistence is lived "
                   "beneath it",
                   "Yes: the argument from analogy, once repaired, proves it",
                   "No: it concludes that only I exist"],
             "c": 1,
             "why": "Page 419: the truth of solipsism is there; page 418: solitude and "
                    "communication are two moments of one phenomenon. The dialogue is a "
                    "description, not a proof; the repaired analogy is circular; and the chapter "
                    "denies that a solipsist can even be consistent."},
        ],
        "mistakes": [
            ("Thinking Merleau-Ponty refutes solipsism",
             "The chapter says the opposite in so many words: there is a solipsism rooted in "
             "living experience and quite insurmountable, and the truth of solipsism is there. "
             "It also says that solitude and communication are two moments of one phenomenon, "
             "and that coexistence is lived before and beneath any withdrawal. Both claims are "
             "in the chapter. The table shows only the first half, the grief both accounts "
             "absorb; the coexistence, which both fail in the dialogue, is in the prose."),
            ("Taking the objectifying look as the chapter's own view",
             "Page 416 describes the other's gaze stripping me of part of my being, and it is "
             "easy to read that as the chapter's claim. On page 420 the view is introduced as "
             "something asserted, and answered: the look objectifies only if both withdraw "
             "into their thinking nature, and it stops when the stranger speaks."),
            ("Reading lived solipsism as the theory that only I exist",
             "The chapter's solipsism is the fact that every experience, of others too, is "
             "lived by me and from my side; Paul's grief is displayed to me and lived by him. "
             "It is not the theory that others do not exist, which, the chapter says, could "
             "only be held by someone who existed without being or doing anything."),
        ],
        "standard": (
            "Finish when you can count the two accounts and state both of the chapter's "
            "claims.",
            "Given a coded table of the chapter's cases, compute each account's record, the "
            "survivors and the split, defend each cell from the page, and state in the "
            "chapter's terms the truth of solipsism and the coexistence it says is lived "
            "beneath it."
        ),
        "note": (
            "The table counts the lesson's coding of four cases, and the cells for the look are "
            "the most open to dispute, since its author, widely taken to be Sartre, is not "
            "named and the chapter states his view in a few lines. The lab cannot score the "
            "chapter's own position, which holds solitude and coexistence together, and it "
            "cannot show whether the coexistence is lived as the chapter says; that is a "
            "description to test against your own experience of a conversation."
        ),
    },
]
