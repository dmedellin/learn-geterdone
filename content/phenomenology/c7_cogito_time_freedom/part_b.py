"""The Cogito, Time and Freedom, lessons 5-8 -- Part Three, Chapters 2 and 3.

Every quotation is copied from Colin Smith's translation, Routledge Classics
pagination (Part Three, pp. 429-530); the comment beside each lesson gives its
pages. Smith's ligatures are printed as plain letters, a word split by a
line-break hyphen is joined, and footnote numerals are left out. Nothing else
is changed. Freedom opens with several pages in the voice of the theory of
absolute freedom it then answers; the lessons say whose voice each sentence
is in.
"""

LESSONS = [
    # ---------------------------------------------------------------- 05
    # Smith p. 484 (opening passage: "With the arrival of every moment ... a
    # thin layer of time."; "the retention of a retention"; "Time is not a
    # line, but a network of intentionalities."; the diagram, from Husserl,
    # Zeitbewusstsein p. 22); p. 483 (the field of presence: this moment, the
    # day behind, the evening ahead; the back of a house); p. 485 (the
    # identifying synthesis objected; "as I see a pebble through the mass of
    # water which moves over it"; the suit before the armistice); p. 486
    # (Scheler's patient; operative intentionality; passive synthesis, "a term
    # which is clearly not a solution, but merely a pointer to the problem").
    # Smith prints "protections" for Husserl's protentions on pp. 483-484.
    {
        "slug": "the-field-of-presence",
        "title": "The Field of Presence",
        "module": "Part Three · 2 · Temporality",
        "one_line": "The present is not an instant but a field, holding the moment just past and leaning into the next; Husserl's diagram draws how each moment sinks, retained through the ones after it.",
        "summary": (
            "The chapter finds time first in the field of presence, the moment I am living "
            "with the day behind it and the evening ahead, and reproduces Husserl's diagram of "
            "retention and protention. Compute, for a present, the depth at which each "
            "earlier moment is retained and the moments protended, and say why retention is "
            "not memory."
        ),
        "key": [
            "field of presence: now, with its horizons",
            "retention: the moment just past, held",
            "a retention of a retention: depth 2",
            "depth = steps back from the present",
            "protention: the moment about to come",
            "time is a network, not a line",
        ],
        "key_label": "The field of presence in six lines",
        "concepts_intro": (
            "Husserl's lectures on the consciousness of internal time gave the chapter its "
            "vocabulary. Three terms carry this lesson."
        ),
        "concepts": [
            ("The field of presence",
             "The present in the wide sense: the moment I spend working, with the horizon of "
             "the day that has elapsed behind it and the evening and night ahead. The chapter "
             "calls it the primary experience in which time appears."),
            ("Retention",
             "Husserl's term for the way the moment just past is still held in the present, "
             "not recalled. When a further moment arrives, the retention is itself retained, "
             "and the past sinks one layer deeper."),
            ("Protention",
             "Husserl's term for the matching hold on what is about to come, which traces "
             "out in advance at least the style of the next moment."),
        ],
        "read_title": "The passage first, then the field of presence and the diagram",
        "read_intro": (
            "The passage is the chapter's description of what happens to a moment as the "
            "next arrives. The lesson starts with the field of presence, reads the passage and "
            "the diagram, then the objection and the reply."
        ),
        "body": [
            ("p", "<strong>Part Three, Chapter 2, p. 484.</strong> &ldquo;With the arrival of "
                  "every moment, its predecessor undergoes a change: I still have it in hand "
                  "and it is still there, but already it is sinking away below the level of "
                  "presents; in order to retain it, I need to reach through a thin layer of "
                  "time.&rdquo; The sentence is on page 484 of Smith's translation. Read from "
                  "the paragraph that begins on page 483 to the end of the paragraph on "
                  "passive synthesis on page 486, in your own copy before going on."),
            ("p", "The pages turn on a diagram, and the chapter reproduces it. Edmund Husserl, "
                  "the founder of phenomenology, drew it in his lectures on the consciousness "
                  "of internal time, which grew from a course of 1905 and were published in "
                  "1928, prepared by Edith Stein and edited by Martin Heidegger. A horizontal line is the series of present moments. "
                  "From each moment an oblique line runs down: that moment as it is seen, "
                  "shaded off, from each later present. The caption calls the vertical lines "
                  "the successive shadings of one and the same present moment; the lab reads "
                  "the vertical through a present as what that present holds, itself and the "
                  "shading of each earlier moment. Husserl's word for a shading is "
                  "Abschattung, and the chapter keeps it."),
            ("p", "Before the diagram, the chapter names where time is met: in my field of "
                  "presence, this moment that I spend working, with the horizon of the day "
                  "behind it and the evening and night in front of it (p. 483). I do not form "
                  "a picture of my day; it weighs on me, and though I recall no detail of it "
                  "I still have it in hand, in Husserl's phrase. The evening is there too, "
                  "like the back of a house of which I see only the front. The present itself "
                  "is not posited either: I reckon with my pen and paper rather than looking "
                  "at them. Husserl calls these holds on past and future retentions and "
                  "protentions. Smith prints protections for the second word on these pages; "
                  "Husserl's term is protentions, which Smith uses a few pages later."),
            ("p", "Now the passage. A moment arrives and its predecessor changes: still held, "
                  "still there, but already sinking. To keep it I reach through a thin layer "
                  "of time. When a third moment comes, the second changes again: from being a "
                  "retention it becomes &ldquo;the retention of a retention&rdquo;, and the "
                  "layer between it and me thickens. So the chapter concludes from the "
                  "diagram: &ldquo;Time is not a line, but a network of "
                  "intentionalities&rdquo; (p. 484). Intentionality, the directedness of "
                  "consciousness at something, runs here from each present to every moment "
                  "it still holds."),
            ("def", ("Retention (Husserl, as the chapter reads him)",
                     "The moment just past as it is still held in the present, given through "
                     "its later shadings and not reconstructed from them. A retention of a "
                     "retention is a moment held one layer further back.")),
            ("p", "The lab makes the diagram's counting exact. The <code>three</code> preset "
                  "takes moments A, B and C with C present. The retained tile prints A at "
                  "depth 2, B at depth 1: B is one step back, held directly, and A two steps "
                  "back, held through B. The column tile reads the vertical through C in "
                  "Husserl's notation, C, then B′ for B's first shading, then A′′ for A's "
                  "second. The protended tile prints the moments held ahead, and with a "
                  "protention span of 0 there are none. The <code>later</code> preset adds D "
                  "and makes it present: A at depth 3, B at 2, C at 1, and the column reads D, "
                  "C′, B′′, A′′′. Every moment has sunk one layer."),
            ("p", "The <code>span</code> preset gives the present C a protention span of 2 "
                  "over moments A to E, and the protended tile prints D, E. The chapter says "
                  "that to make the diagram complete the symmetrical perspective of "
                  "protentions would have to be added, and the lab adds it as a count. What "
                  "it cannot add is the chapter's caution that protention traces out only the "
                  "style of what is to come, and that we remain on the watch, perhaps to the "
                  "day of our death, for something else."),
            ("p", "The objection the chapter raises against itself is the natural one (pp. "
                  "484&ndash;485). For A′ to be recognised as a shading of A, and A′′ of A′, "
                  "must there not be a synthesis that identifies them all as one A, an ideal "
                  "unity as Kant requires? The chapter's answer is that such a synthesis would "
                  "abolish time: A would be identifiable for ever, and nothing would then "
                  "distinguish a sequence from a spatial array. What is given is not A′ first, "
                  "from which I infer A, but A itself seen through A′, and both through A′′, "
                  "&ldquo;as I see a pebble through the mass of water which moves over "
                  "it&rdquo; (p. 485)."),
            ("p", "Identifying syntheses exist, the chapter grants, but only in express memory "
                  "and the voluntary recall of the remote past. Its example: unsure when a "
                  "remembered scene took place, I reason that I had this suit made before the "
                  "armistice, since no English cloth has been available since. That reaches a "
                  "date, not the past itself. When I recover the memory's real place, it is "
                  "because it falls into a current of fear and hope running from Munich to the "
                  "outbreak of war, carried by the unbroken chain of retentions from then to "
                  "now. And if the past were available only in recollections, we would keep "
                  "turning to check it, like a patient Scheler describes who kept turning "
                  "round to make sure things were still there."),
            ("p", "Husserl's name for this unity is passive synthesis, and the chapter takes it "
                  "with a reservation: &ldquo;a term which is clearly not a solution, but "
                  "merely a pointer to the problem&rdquo; (p. 486). Beneath the intentionality "
                  "of acts, which posits an object, it recognises with Husserl an operative "
                  "intentionality that makes acts possible, and says that this is what "
                  "Heidegger calls transcendence. How faithful this is to Husserl is "
                  "disputed. The chapter reads the time lectures together with unpublished "
                  "manuscripts and with Eugen Fink, Husserl's last assistant, and specialists "
                  "still argue over whether Husserl's own account of the flow says what "
                  "Merleau-Ponty draws from it."),
            ("p", "The chapter adds at once that the diagram is an instantaneous cross-section "
                  "of time. What a single column cannot show is the passage from one column to "
                  "the next. The next lesson, “Time as Subject”, reads the chapter's account "
                  "of that passage, and of who lives it."),
        ],
        "lab": ("phenkit", {
            "mode": "time",
            "view": "diagram",
            "model": "Husserl's diagram, as the lesson's model",
            "preset": "three",
            "presets": [
                {"id": "three", "label": "Moments A, B, C; the present C",
                 "moments": "A, B, C", "present": "C",
                 "expect": {"tiRetained": "A at depth 2, B at depth 1", "tiColumn": "C, B′, A′′"}},
                {"id": "later", "label": "Moments A to D; the present D",
                 "moments": "A, B, C, D", "present": "D",
                 "expect": {"tiRetained": "A at depth 3, B at depth 2, C at depth 1", "tiColumn": "D, C′, B′′, A′′′"}},
                {"id": "span", "label": "Moments A to E; the present C, with a protention span of 2",
                 "moments": "A, B, C, D, E", "present": "C", "protention": 2,
                 "expect": {"tiRetained": "A at depth 2, B at depth 1", "tiProtended": "D, E"}},
            ],
            "panel_title": "Husserl's diagram, counted",
            "panel_intro": (
                "This lab is the lesson's model, made from Husserl's diagram: a line of "
                "moments, and for a chosen present the depth at which each earlier moment is "
                "held and the moments held ahead. Compare the three and later presets. The "
                "depth is a count of steps, not a measure of how far away anything feels."
            ),
        }),
        "steps_title": "Reading the diagram at a present",
        "steps_intro": "Four steps, the same for any present.",
        "steps": [
            ("List the moments",
             "Write the moments in order along the horizontal line and choose the present."),
            ("Count the depths",
             "Each earlier moment is retained at a depth equal to the number of steps "
             "between it and the present: the moment just before at depth 1."),
            ("Read the column",
             "Write the vertical through the present: the present, then each earlier "
             "moment with one prime for each step of depth."),
            ("Add the protention",
             "List the moments ahead, up to the protention span, that the present already "
             "holds as about to come."),
        ],
        "worked": {
            "title": "Three moments, then four",
            "intro": [
                "Take moments A, B and C, with C present; then let D arrive. You want the "
                "depth of each earlier moment, and the column through the present.",
            ],
            "lines": [
                "present C:  B at depth 1, A at depth 2",
                "column at C:  C, B′, A′′",
                "present D:  C at 1, B at 2, A at 3",
                "protention 2 at C:  D, E",
            ],
            "after": [
                "When D arrives, nothing is added to the past from outside: every moment "
                "already held sinks one layer, and A is now held through B and C. That is "
                "the passage's thin layer of time, thickening.",
            ],
        },
        "quiz_title": "Retention and the field of presence",
        "quiz": [
            {"q": "Moments A to E, with E present. At what depth is B retained?",
             "a": ["3", "2", "4", "1"],
             "c": 0,
             "why": "From E back to B is three steps: D at depth 1, C at 2, B at 3. Two is C's "
                    "depth, four is A's, and one is D's."},
            {"q": "On the chapter's account, how is A given when C is present?",
             "a": ["As a stored copy of A, recalled from memory",
                   "As A itself, seen through its later shadings, as a pebble is seen through "
                   "moving water",
                   "As an idea of A, identified across its shadings by an intellectual synthesis",
                   "Not at all, since only the present C is given"],
             "c": 1,
             "why": "That is the pebble sentence. A stored copy is the memory model the chapter "
                    "rejects, the identifying synthesis is the objection it answers, and the "
                    "field of presence holds more than C."},
            {"q": "Where, according to the chapter, do identifying syntheses really occur?",
             "a": ["In every retention of the moment just past",
                   "In protention, when the next moment is anticipated",
                   "In express memory and the voluntary recall of the remote past",
                   "Nowhere; the chapter denies them altogether"],
             "c": 2,
             "why": "The chapter grants identifying syntheses in deliberate recollection, as "
                    "with the suit made before the armistice, and says they are derived modes "
                    "resting on retention. It denies them in retention itself and does not "
                    "assign them to protention."},
            {"q": "What does the field of presence include?",
             "a": ["Only the instant now, without extent",
                   "Every memory I can call up",
                   "The remote past, made present again",
                   "The moment now, with the horizon of the day behind it and the evening "
                   "ahead"],
             "c": 3,
             "why": "The chapter's example is this moment of work with its horizons. An "
                    "instant without extent is the time the chapter rejects, and the remote "
                    "past is reached only by reopening time, not as part of the present field."},
        ],
        "mistakes": [
            ("Thinking retention is short-term memory, a stored copy of the moment just past",
             "A copy would be present, like the table's ink stain, and would point to the "
             "past only for someone who already had a sense of it. Retention, the chapter "
             "says after Husserl, is the past held in the present's own thickness: at C, A "
             "is held at depth 2, through B, and what is given is A itself seen through its "
             "shadings, as a pebble through water. Recollection is a different act, and only "
             "there do identifying syntheses occur."),
            ("Thinking the diagram shows time as a line",
             "The horizontal line is only one of three kinds of line in it. The obliques and "
             "verticals are what the chapter cares about, and its conclusion is the "
             "opposite of a line: &ldquo;Time is not a line, but a network of "
             "intentionalities.&rdquo;"),
            ("Taking a depth for how faint the past feels",
             "The lab's depth is a count of steps in the model: A at depth 2 means two "
             "moments have arrived since. It says nothing about vividness, and the chapter "
             "does not measure retention at all; it says that to retain is to hold, but at a "
             "distance."),
        ],
        "standard": (
            "Finish when you can read Husserl's diagram at any present and say what retention is not.",
            "Given a series of moments and a present, compute the depth of each earlier "
            "moment, the column through the present and the protended moments, and explain "
            "why retention is not a stored copy."
        ),
        "note": (
            "The model counts the steps of Husserl's diagram, and the chapter itself warns "
            "that the diagram is an instantaneous cross-section of time; the lab cannot show "
            "the passage between columns. The chapter's reading of Husserl, through Fink and "
            "the unpublished manuscripts, is disputed among his specialists."
        ),
    },
    # ---------------------------------------------------------------- 06
    # Smith p. 490 (opening passage: "We are not saying that time is for
    # someone ... time is someone" and "We must understand time as the subject
    # and the subject as time."; the fountain, pp. 489-490, "not in so far as
    # the river flows, but in so far as it is one with itself"; Husserl's
    # "a consciousness having behind it no consciousness to be conscious of
    # it"); p. 486 (the diagram as an instantaneous cross-section); p. 487
    # (one phenomenon of running-off; ek-stase); p. 488 (C not bereft of its
    # being; Bergson); p. 491 (not in time because it lives time); p. 492
    # ("What does not pass in time is the passing of time itself."; the
    # privilege of the present); p. 494 (Kant, Heidegger: "the affecting of
    # self by self"); p. 496 (passive synthesis; "I am not the creator of time
    # any more than of my heart-beats"); pp. 496-497 (Heidegger's historical
    # time; "It is always in the present that we are centered"); pp. 500-503
    # (soul and body, the nebula, other temporalities, the basis of freedom).
    {
        "slug": "time-as-subject",
        "title": "Time as Subject",
        "module": "Part Three · 2 · Temporality",
        "one_line": "The subject is neither in time like a thing nor outside it looking on; it is the passage itself, and the chapter's formula is that time is someone.",
        "summary": (
            "The diagram is only a cross-section; what there is, the chapter says, is one "
            "movement of passing, and the subject is that movement. Compute the diagram's "
            "column at each present in turn, show that one moment is held at a different "
            "depth in each while the order of moments never changes, and say why no single "
            "column is the time."
        ),
        "key": [
            "column at B: A 1",
            "column at C: A 2, B 1",
            "column at D: A 3, B 2, C 1",
            "A across the columns: 1, 2, 3",
            "order A, B, C in every column",
            "time as the subject, subject as time",
        ],
        "key_label": "Time as subject in six lines",
        "concepts_intro": (
            "The rest of Temporality draws on Husserl, Heidegger and Kant at once. Three "
            "ideas carry it."
        ),
        "concepts": [
            ("Ek-stase",
             "Heidegger's word, from the Greek for standing outside oneself: time as a "
             "movement out of itself towards future and past. The chapter takes it for the "
             "one law of time's passing."),
            ("Self-affection",
             "Kant's phrase for the mind affecting itself, which Heidegger transferred to "
             "time. The chapter uses it to say that what affects and what is affected are "
             "one, time as thrust and time as an unfolded series of presents."),
            ("Passive synthesis",
             "Husserl's term for a unity not made by an act. The chapter clarifies it: we "
             "make our way into the multiplicity of time but do not compose it."),
        ],
        "read_title": "The passage first, then the rest of Temporality",
        "read_intro": (
            "The passage is the chapter's thesis about the subject. The lesson starts from "
            "the cross-section the previous lesson ended on, follows the passage of time to "
            "the thesis, then reads what the chapter draws from it."
        ),
        "body": [
            ("p", "<strong>Part Three, Chapter 2, p. 490.</strong> &ldquo;We are not saying "
                  "that time is for someone, which would once more be a case of arraying it "
                  "out, and immobilizing it. We are saying that time is someone &hellip; We "
                  "must understand time as the subject and the subject as time.&rdquo; The "
                  "sentences are on page 490 of Smith's translation. Read from the paragraph "
                  "that begins on page 486, after the passive synthesis, to the end of the "
                  "chapter on page 503, in your own copy before going on."),
            ("p", "The case is the diagram again, and the chapter's remark that it is an "
                  "instantaneous cross-section (p. 486). What there really is, it says, is "
                  "not a past, a present and a future, nor separate instants A, B and C, nor "
                  "a heap of retentions and protentions, but one single phenomenon of running "
                  "off. When the present passes from B to C, B bursts into B′ and A′ into "
                  "A′′, and C, which announced its coming, begins at once to lose its "
                  "substance. The system of retentions collects into itself at each instant "
                  "what was, an instant earlier, the system of protentions. Martin Heidegger, "
                  "whose <em>Being and Time</em> (1927) made temporality the meaning of human "
                  "existence, called this movement an ek-stase, and the chapter takes the word."),
            ("p", "The lab sets the columns side by side. The <code>walk</code> preset takes "
                  "moments A to D and the presents B, C and D in turn. The columns tile "
                  "prints each present with the depths it holds: B: A 1; C: A 2, B 1; D: A "
                  "3, B 2, C 1. The depths tile reads the same table the other way, moment "
                  "by moment: A at 1, 2, 3, B at 1, 2, C at 1. The order tile checks every "
                  "column against the longest and prints that the order A, B, C is the same "
                  "in every column. One moment, held at a different depth under each present; "
                  "the order of moments never changes. That is the chapter's answer to how "
                  "time can pass without the moments losing their place."),
            ("p", "C does not lose its being when D pushes it into the past (p. 488). It had "
                  "been approaching, announced by fewer and fewer shadings, and its passing is "
                  "the reverse side of its arriving; since in time being and passing are one, "
                  "by becoming past the event does not cease to be. Here the chapter corrects "
                  "Henri Bergson and sides with him: he was wrong to explain the unity of time by its "
                  "continuity, as if past, present and future blurred into one another, and "
                  "right to hold on to continuity as essential. The moments are distinct, and "
                  "they run into each other."),
            ("p", "Then the turn to the subject. I do not watch the passage from one present "
                  "to the next as an onlooker; I effect it, as my gesture is already at its "
                  "goal (p. 489). Common sense half knows this, the chapter says: we say there "
                  "is time as we say there is a fountain, whose water changes while its form "
                  "remains, and the river image is justified &ldquo;not in so far as the river "
                  "flows, but in so far as it is one with itself&rdquo; (p. 490). Now the "
                  "passage. Time is not for someone, arrayed before a spectator and so "
                  "immobilised; time is someone. The subject is the one thrust that holds the "
                  "dimensions of time together while keeping them apart."),
            ("def", ("Time as the subject",
                     "The chapter's thesis that the subject is not a thing in time nor an "
                     "onlooker outside it, but the passage of time itself, which holds past and "
                     "future together while keeping them apart.")),
            ("p", "This needs, the chapter says with Husserl, &ldquo;a consciousness having "
                  "behind it no consciousness to be conscious of it&rdquo;, or there would "
                  "be an infinite regress of consciousnesses each watching the one before "
                  "(p. 490). Such a consciousness is not in time, because it takes up or "
                  "lives time. That is not eternity. &ldquo;What does not pass in time is the "
                  "passing of time itself&rdquo; (p. 492), and the feeling of eternity, like "
                  "the fountain's, feeds on the continuous pressure of the water. The present, "
                  "in the wide sense, keeps a privilege among the dimensions, as the zone in "
                  "which being and consciousness coincide."),
            ("p", "Two more presets. The <code>long</code> preset takes moments A to F and "
                  "the presents B to F, and the order tile prints that A, B, C, D, E keep "
                  "their order in every column, while A sinks to depth 5. The "
                  "<code>one</code> preset takes a single present, D, and the lab prints one "
                  "column, D: A 3, B 2, C 1, and the order tile, with only one column to "
                  "compare, says trivially that the order holds. That single column is the cross-section the "
                  "chapter warns against taking for time: it holds every depth and no "
                  "passing. The lab can lay columns side by side, but it cannot pass from one "
                  "to the next, which is what the chapter says the subject is."),
            ("p", "Self-affection is the chapter's next borrowing (p. 494). Kant applied the "
                  "phrase to the mind, and Heidegger, in <em>Kant and the Problem of "
                  "Metaphysics</em> (1929), transferred it to time: time is &ldquo;the "
                  "affecting of self by self&rdquo;. What affects is time as a thrust towards "
                  "a future; what is affected is time as an unfolded series of presents; and "
                  "they are one, because the thrust is nothing but the transition from one "
                  "present to another. If the subject is time, then positing oneself is no "
                  "longer a contradiction. Just before, the chapter shows the alternative with "
                  "Proust's Swann, an example its note credits to Sartre: a novelist who takes "
                  "consciousness as psychic facts says Swann's love causes his jealousy, and "
                  "the chapter replies that the love was jealousy from the start."),
            ("p", "So passive synthesis is clarified (p. 496). I do not compose the "
                  "multiplicity of time; I make my way into it. &ldquo;I am not the creator "
                  "of time any more than of my heart-beats&rdquo;: I did not choose to be "
                  "born, and once I am, time flows through me whatever I do. Yet I am not "
                  "simply subject to it, for a decision that binds me, or a concept I fix, "
                  "holds me back from what I was about to become. We are wholly active and "
                  "wholly passive, the chapter says, because we are the upsurge of time."),
            ("p", "Here the chapter parts from Heidegger. For <em>Being and Time</em> the "
                  "future is the primary dimension, and authentic historical time flows from "
                  "it, gathered by resolute decision. The chapter calls that impossible within "
                  "Heidegger's own thought: if time is an ek-stase, we can never wholly cease "
                  "to see it from the present, and &ldquo;It is always in the present that we "
                  "are centered&rdquo; (p. 497). Our decisions start from there and must be "
                  "carried forward. Whether this is fair to Heidegger, and how far the "
                  "chapter's time as subject agrees with Husserl's absolute flow, are both "
                  "disputed."),
            ("p", "The chapter's last pages apply the thesis. The relation of soul and body "
                  "becomes the relation of a present to its past and future: it is as much of "
                  "my essence to have a body as it is the future's to be the future of a "
                  "certain present (p. 501). The world before man, Laplace's nebula, is not "
                  "behind us but in front of us, in the cultural world that gives the "
                  "sentence its meaning. And two temporalities are not mutually exclusive as "
                  "two consciousnesses are: my living present can open onto other people's. "
                  "In the thickness of that pre-objective present the chapter finds our "
                  "bodily and social being, and the basis of our freedom (p. 503)."),
            ("p", "Freedom is the next chapter's subject, and it opens with a theory that "
                  "freedom is total. The next lesson, “The Rock and the Project”, reads that "
                  "theory and the chapter's first answer to it."),
        ],
        "lab": ("phenkit", {
            "mode": "time",
            "view": "ekstasis",
            "model": "the lesson's model of the diagram's columns",
            "preset": "walk",
            "presets": [
                {"id": "walk", "label": "Moments A to D; the presents B, C and D in turn",
                 "moments": "A, B, C, D", "presents": "B, C, D",
                 "expect": {"tiColumns": "B: A 1; C: A 2, B 1; D: A 3, B 2, C 1",
                            "tiDepths": "A: 1, 2, 3; B: 1, 2; C: 1",
                            "tiOrder": "the order A, B, C is the same in every column"}},
                {"id": "long", "label": "Moments A to F; the presents B to F",
                 "moments": "A, B, C, D, E, F", "presents": "B, C, D, E, F",
                 "expect": {"tiDepths": "A: 1, 2, 3, 4, 5; B: 1, 2, 3, 4; C: 1, 2, 3; D: 1, 2; E: 1",
                            "tiOrder": "the order A, B, C, D, E is the same in every column"}},
                {"id": "one", "label": "A single present, D: one column",
                 "moments": "A, B, C, D", "presents": "D",
                 "expect": {"tiColumns": "D: A 3, B 2, C 1", "tiDepths": "A: 3; B: 2; C: 1",
                            "tiOrder": "the order A, B, C is the same in every column"}},
            ],
            "panel_title": "One moment across many presents",
            "panel_intro": (
                "This lab is the lesson's model: from a list of moments it computes the "
                "column at each chosen present, each moment's depths across the columns, and "
                "whether the order of moments holds in every column. Compare the walk and one "
                "presets. It shows columns side by side and never the passing between them."
            ),
        }),
        "steps_title": "Following one moment across the presents",
        "steps_intro": "Four steps; the last is the chapter's.",
        "steps": [
            ("Compute each column",
             "For each present, list every earlier moment with its depth, the number of "
             "steps back."),
            ("Read across",
             "For each moment, list its depths in the columns in turn. Each new present adds "
             "one to every depth."),
            ("Check the order",
             "Compare each column with the longest: the moments appear in the same order in "
             "all of them."),
            ("Name what no column holds",
             "State what the table leaves out: the passage from one column to the next, "
             "which the chapter says is the subject itself."),
        ],
        "worked": {
            "title": "A across three presents",
            "intro": [
                "Take moments A to D and let B, C and D be present in turn. You want the "
                "column at each present and what happens to A.",
            ],
            "lines": [
                "at B:  A at depth 1",
                "at C:  A at depth 2, B at depth 1",
                "at D:  A at depth 3, B at depth 2, C at depth 1",
                "A across the columns:  1, 2, 3",
                "order in every column:  A, B, C",
            ],
            "after": [
                "A sinks one layer with each present, and never changes its place before B and "
                "C. That is how the chapter can say that the event, by becoming past, does not "
                "cease to be. What the three columns do not contain is the passing from one to "
                "the next, and that, on the chapter's thesis, is who the subject is.",
            ],
        },
        "quiz_title": "Time and the subject",
        "quiz": [
            {"q": "Moments A to E, with the presents B, C, D and E in turn. What depths does B "
                  "take across the columns in which it is past?",
             "a": ["1, 2, 3, 4", "1, 2, 3", "2, 3, 4", "0, 1, 2, 3"],
             "c": 1,
             "why": "B is past under C, D and E, at depths 1, 2 and 3. Four depths would need "
                    "a present F; starting at 2 skips C; and B at depth 0 would be B present, "
                    "which is not a column in which B is past."},
            {"q": "What does the chapter mean by saying that time is someone, not for someone?",
             "a": ["That time exists only in someone's mind",
                   "That each person has a private time of their own",
                   "That the subject is not an onlooker before whom time is arrayed, but the "
                   "passage itself",
                   "That time is a container in which persons exist"],
             "c": 2,
             "why": "For someone would array time before a spectator and immobilise it, which "
                    "the passage rejects. Time only in the mind is the idealist view the "
                    "chapter turned down in its first pages, private times contradict "
                    "its pages on other temporalities, and the container is time as a thing."},
            {"q": "Against Heidegger, which dimension of time does the chapter say keeps a "
                  "privilege?",
             "a": ["The future, from which authentic historical time flows",
                   "The past, which is acquired once and for all",
                   "None; the chapter makes all three equal in every respect",
                   "The present, with its horizons, where being and consciousness coincide"],
             "c": 3,
             "why": "It is always in the present that we are centred. The primacy of the future "
                    "is Heidegger's, which the chapter says is impossible on his own terms; the "
                    "past is acquired but not privileged; and though no dimension can be "
                    "deduced from the others, the present keeps a privilege."},
            {"q": "Why does the one preset's single column not show time, on the chapter's "
                  "account?",
             "a": ["A single column is an instantaneous cross-section, and time is the passing "
                   "from one to the next",
                   "Because a single column leaves out the future",
                   "Because depths cannot be counted at a single present",
                   "Because the order of the moments changes within it"],
             "c": 0,
             "why": "The chapter calls the diagram an instantaneous cross-section. The column "
                    "does count depths, D: A 3, B 2, C 1, and keeps the order; what it lacks is "
                    "passage. Adding a protention would not supply that either."},
        ],
        "mistakes": [
            ("Thinking the subject is in time as a thing is, or outside time looking on",
             "The chapter refuses both. A thing in time would be a series of states, and a "
             "new consciousness would be needed to be aware of the series, and so on for "
             "ever; an onlooker outside would array time and immobilise it. In the lab no "
             "column is the time: A is at depth 1, 2 and 3 under B, C and D, and the order "
             "A, B, C holds in every column. What no column holds is the passing, and the "
             "chapter's thesis is that the subject is that passing: time is someone."),
            ("Hearing time as the subject as idealism, time placed in the mind",
             "The passage says the opposite: &ldquo;We are not saying that time is for "
             "someone&rdquo;. A time laid out as the object of a constituting consciousness "
             "was rejected in the chapter's first pages as time brought down to one level. "
             "The subject here is not a mind containing time but the thrust of time itself."),
            ("Thinking the subject as time is a new kind of eternity",
             "The chapter asks this itself and answers no. What does not pass is only the "
             "passing of time; the feeling of eternity feeds on time, as the fountain keeps "
             "its form only by the pressure of the water, and the ultimate consciousness is "
             "the consciousness of the present."),
        ],
        "standard": (
            "Finish when you can follow a moment across several presents and say what no column holds.",
            "Given moments and a series of presents, compute the column at each present, each "
            "moment's depths across the columns and whether the order holds, and state why "
            "the chapter says no single column is time."
        ),
        "note": (
            "The model lays the diagram's columns side by side and counts; it cannot pass "
            "from one column to the next, which is the chapter's whole point. The chapter's "
            "readings of Husserl's absolute flow and of Heidegger's primacy of the future are "
            "its own, and both are disputed."
        ),
    },
    # ---------------------------------------------------------------- 07
    # Smith p. 511 (opening passage: "Whether or not I have decided to climb
    # them ... small for me."; "a natural self which does not budge from its
    # terrestrial situation"; the Alps as molehills; the dots and the cube);
    # pp. 504-507 (absolute freedom stated: "The alleged motive does not
    # burden my decision; on the contrary my decision lends the motive its
    # force." p. 505, the theory's voice, with Sartre cited in the note);
    # p. 507 (the rock, the theory's voice: "for anyone who is not intending
    # to surmount them"); pp. 508-510 (the theory turns against itself; Sartre
    # named, p. 509; "no freedom without a field", p. 510); p. 510 ("one rock
    # will appear as an obstacle, and another, being more negotiable, as a
    # means"); p. 512 ("There is an autochthonous significance of the world";
    # "there are no obstacles in themselves"); pp. 512-513 (pain and fatigue;
    # sedimentation).
    {
        "slug": "the-rock-and-the-project",
        "title": "The Rock and the Project",
        "module": "Part Three · 3 · Freedom",
        "one_line": "A rock is unclimbable only for someone who means to climb it, says the theory of absolute freedom; the chapter agrees, and adds that some mountains look high to someone with no plan to climb them.",
        "summary": (
            "Freedom opens with a theory of absolute freedom, recognisably Sartre's, on which "
            "obstacles exist only for a project. Classify rocks as obstacles relative to a "
            "project and then relative to the body's general level, and name the rock that "
            "stands out on the second reckoning and not on the first."
        ),
        "key": [
            "rocks: 1, 2 and 3 metres",
            "to climb, capacity 2: obstacle at 3",
            "to walk past: no obstacle on the project",
            "body's level 2: the 3-metre rock stands out",
            "express intentions and general ones",
            "no freedom without a field",
        ],
        "key_label": "The rock in six lines",
        "concepts_intro": (
            "The chapter's first half states absolute freedom and turns it against itself. "
            "Three ideas carry it."
        ),
        "concepts": [
            ("Absolute freedom",
             "The theory that consciousness is free in every act and to the same degree, "
             "that no motive acts on it, and that obstacles exist only in the light of its "
             "projects. The chapter states it, in the theory's own voice, for several pages."),
            ("A project",
             "An aim that organises a situation, such as climbing a rock. On the theory, it "
             "is the project that makes the rock high, difficult or a means."),
            ("General intentions",
             "The chapter's name for the valuations a body makes of its surroundings before "
             "any decision: the mountain that exceeds my stride looks high whether or not I "
             "mean to climb it."),
        ],
        "read_title": "The passage first, then the chapter's first nine pages",
        "read_intro": (
            "The passage is the chapter's turn against the theory it has been stating. The "
            "lesson starts with the theory in its own voice, follows the rock, then reads the "
            "passage and the pages on the body's valuations."
        ),
        "body": [
            ("p", "<strong>Part Three, Chapter 3, p. 511.</strong> &ldquo;Whether or not I "
                  "have decided to climb them, these mountains appear high to me, because "
                  "they exceed my body's power to take them in its stride, and, even if I "
                  "have just read Micromégas, I cannot so contrive it that they are small for "
                  "me.&rdquo; The sentence is on page 511 of Smith's translation. Read the "
                  "chapter from its first page, 504, to the sentences on sedimentation in the "
                  "middle of page 513, in your own copy before going on; the paragraph runs on "
                  "into the next lesson's first case."),
            ("p", "Picture a walk along a valley path with boulders beside it. If you mean to "
                  "scramble up one, each is suddenly easy or hard, a handhold or a wall. If "
                  "you are only walking past, they are scenery. That is a fair picture of "
                  "the theory the chapter opens with, and its first pages are in that "
                  "theory's voice, not Merleau-Ponty's, though its first sentence is one he "
                  "shares: no causal relation is conceivable between the subject and his body, "
                  "world or society. The theory goes on from there. I cannot be free in some actions "
                  "and determined in others, nor a little free. And motives do not act on me "
                  "either: &ldquo;The alleged motive does not burden my decision; on the "
                  "contrary my decision lends the motive its force&rdquo; (p. 505)."),
            ("p", "Whose theory? The footnotes cite Jean-Paul Sartre's <em>Being and "
                  "Nothingness</em> (1943), and Sartre is named once in the body of the text, "
                  "on page 509. Sartre, the novelist and philosopher who had known Merleau-Ponty "
                  "since the École normale and in 1945 founded the review <em>Les Temps "
                  "modernes</em> with him, had argued at length that freedom is the very "
                  "being of consciousness, total in every act, and that the world's "
                  "resistance appears only in the light of a freely chosen end. At its "
                  "strength the view explains a great deal: why the same fatigue halts one "
                  "walker and not another, why deliberation so often follows a decision "
                  "already made, why giving up a plan can bring relief."),
            ("p", "The rock is Sartre's own example. On the theory, an unclimbable rock face, "
                  "large or small, vertical or slanting, has no meaning &ldquo;for anyone who "
                  "is not intending to surmount them&rdquo;, for the rocks are only so many "
                  "forms that a subject's projects carve out of the uniform mass of being "
                  "(p. 507). The lab's model makes the reckoning a count. Every preset has "
                  "rocks of 1 m, 2 m and 3 m. The <code>climb</code> preset gives the "
                  "project climb and a capacity of 2 m, and the project tile prints 3 m: "
                  "only the rock strictly taller than the capacity is an obstacle. The "
                  "<code>pass</code> preset changes the project to walking past, and the "
                  "project tile prints none."),
            ("p", "The theory then runs into trouble of its own making (pp. 507&ndash;510). "
                  "If freedom is the same in all our actions, the slave as free in fear as in "
                  "breaking his chains, then there is no free action to point to, and the "
                  "idea of choice vanishes: to choose is to commit oneself, and a freedom "
                  "that the next instant finds just as free and indeterminate commits "
                  "nothing. As Sartre himself observes, the chapter says, dreaming is "
                  "incompatible with freedom because in imagination there is no obstacle and "
                  "nothing to do. Its conclusion is that there is no freedom without a field."),
            ("p", "So the chapter grants the first half (p. 510). When I say this rock is "
                  "unclimbable, that attribute, like being big or little, can be conferred on "
                  "it only by the project of climbing and by a human presence. But one and "
                  "the same project being given, &ldquo;one rock will appear as an obstacle, "
                  "and another, being more negotiable, as a means&rdquo;. Freedom lays down "
                  "that there are obstacles and ways through in general; it does not draw the "
                  "particular outline of this world. The theory's rejoinder is that this "
                  "makes no difference, since freedom is present wherever there is a here and "
                  "a there."),
            ("p", "The reply is the passage. Beside my express intentions, such as the plan I "
                  "now make to climb those mountains, there are general intentions that "
                  "evaluate my surroundings, and they work whether or not I decide anything. "
                  "Micromégas is Voltaire's tale of 1752 about a giant from Sirius who finds "
                  "the Earth's mountains tiny; I can read it and take his view in thought, "
                  "but beneath the thinking subject there is &ldquo;a natural self which does "
                  "not budge from its terrestrial situation&rdquo;. Even to take Sirius's "
                  "point of view I borrow from the Earth: I say the Alps are molehills."),
            ("def", ("General intentions (the chapter's term)",
                     "Valuations of the surroundings that a body makes by having hands, feet "
                     "and a stride, before and beneath any decision. They are general because "
                     "they cover every object at once and because they are not only mine.")),
            ("p", "The <code>body</code> preset gives no project and a general level of 2 m, "
                  "the lesson's illustrative figure for what the body takes in its stride. "
                  "The project tile prints none, because nothing is to be climbed; the level "
                  "tile prints 3 m, because that rock exceeds the level whatever the project. "
                  "That second tile prints 3 m in all three presets. The rock that is an "
                  "obstacle on the body's reckoning and not on the project's is the 3 m rock "
                  "when no climb is planned. Both reckonings are the lesson's model: the book "
                  "computes no heights, and its claim is that the body's valuation comes "
                  "before any chosen project."),
            ("p", "The general intentions are general in a second sense too: they are not "
                  "simply mine, and I expect to find them in everyone organised as I am. That "
                  "is why, as Gestalt psychology showed, a row of dots is always seen as six "
                  "pairs, and one figure always as a cube (p. 511). Ambiguous figures show "
                  "the same thing more clearly, since an absolute freedom could not choose "
                  "itself hesitant. &ldquo;There is an autochthonous significance of the "
                  "world&rdquo;, the chapter concludes (p. 512): a significance that springs "
                  "from the ground of our bodily dealings with it, and underlies every "
                  "deliberate gift of meaning."),
            ("p", "The same holds of pain and fatigue (pp. 512&ndash;513). It has been "
                  "observed, the chapter says, and the note cites Sartre again, that fatigue "
                  "halts me and not my companion because he likes the heat of the road and I "
                  "have chosen a different way of being in the world. The chapter accepts "
                  "this and adds a qualification: an attitude to the world that has often been "
                  "confirmed acquires a favoured status for us, a sedimentation of our life."),
            ("p", "Whether the theory the chapter answers is Sartre's is disputed. "
                  "<em>Being and Nothingness</em> has its own long account of situation and "
                  "facticity, the given that freedom never chose, and many readers think the "
                  "chapter answers a sharpened version of Sartre rather than Sartre. The two "
                  "later quarrelled over politics, and in 1955 Simone de Beauvoir, the "
                  "philosopher and novelist who was Sartre's lifelong companion, accused "
                  "Merleau-Ponty of attacking a pseudo-Sartreanism, in a reply to his later "
                  "book on Marxism and politics rather than to this chapter. The chapter itself names "
                  "Sartre only in the notes and once in passing."),
            ("p", "Sedimentation raises the question the rest of the chapter answers: how "
                  "much can a decision change what years have built? The next lesson, "
                  "“Freedom in Situation”, reads that answer, and the end of the book."),
        ],
        "lab": ("phenkit", {
            "mode": "schema",
            "view": "obstacle",
            "unit": "m",
            "model": "the lesson's model, a project's reckoning and the body's",
            "preset": "climb",
            "presets": [
                {"id": "climb", "label": "To climb, with a capacity of 2 m (illustrative)",
                 "rocks": "1, 2, 3", "project": "climb", "capacity": 2, "general_level": 2,
                 "expect": {"scProject": "3 m", "scLevel": "3 m"}},
                {"id": "pass", "label": "To walk past",
                 "rocks": "1, 2, 3", "project": "pass", "capacity": 2, "general_level": 2,
                 "expect": {"scProject": "none", "scLevel": "3 m"}},
                {"id": "body", "label": "No project; the body's general level 2 m (illustrative)",
                 "rocks": "1, 2, 3", "project": "none", "capacity": 2, "general_level": 2,
                 "expect": {"scProject": "none", "scLevel": "3 m"}},
            ],
            "panel_title": "Obstacles for a project, and for a body",
            "panel_intro": (
                "This lab is the lesson's model: it marks the rocks strictly taller than a "
                "climber's capacity when the project is to climb, and the rocks strictly "
                "taller than the body's general level whatever the project. Switch from the "
                "climb preset to the body preset. The heights are illustrative."
            ),
        }),
        "steps_title": "Two reckonings of an obstacle",
        "steps_intro": "Four steps; the last is the lesson's.",
        "steps": [
            ("List the rocks",
             "Write the height of each rock in one unit."),
            ("Reckon against the project",
             "If the project is to climb, mark each rock strictly taller than the "
             "capacity. Any other project marks none."),
            ("Reckon against the body",
             "Mark each rock strictly taller than the body's general level, whatever the "
             "project."),
            ("Name the difference",
             "State which rock is marked on the body's reckoning and not on the project's, "
             "and which view each reckoning stands for."),
        ],
        "worked": {
            "title": "Three rocks and three projects",
            "intro": [
                "Take rocks of 1 m, 2 m and 3 m, a climber's capacity of 2 m and a body's "
                "general level of 2 m. You want the obstacles on each reckoning.",
            ],
            "lines": [
                "climb:  3 > 2, so the 3-metre rock is an obstacle",
                "walk past:  no rock is an obstacle",
                "no project:  no rock is an obstacle",
                "body's level:  3 > 2, the 3-metre rock stands out",
            ],
            "after": [
                "On the project's reckoning the 3 m rock is an obstacle only for a climb. On "
                "the body's it stands out in every case. The difference is the chapter's: "
                "the mountains look high whether or not I have decided to climb them.",
            ],
        },
        "quiz_title": "The rock and the project",
        "quiz": [
            {"q": "Rocks of 1, 2, 3 and 4 m; the project is to climb, with a capacity of 3 m; "
                  "the body's general level is 2 m. What do the two tiles print?",
             "a": ["Project: 3 m, 4 m. Level: 3 m, 4 m", "Project: 4 m. Level: 4 m",
                   "Project: 4 m. Level: 3 m, 4 m", "Project: none. Level: 3 m, 4 m"],
             "c": 2,
             "why": "Strictly taller than 3 m is only the 4 m rock; strictly taller than 2 m "
                    "are 3 m and 4 m. Counting a rock equal to the capacity gives 3 m and 4 m "
                    "on the project, and none would be right only if the project were not a "
                    "climb."},
            {"q": "What does the chapter grant the theory of absolute freedom about the rock?",
             "a": ["That every rock is an obstacle to every project",
                   "That the body alone decides which rock to climb",
                   "That obstacles exist in themselves, before any project",
                   "That being unclimbable is conferred on it only by a project of climbing "
                   "and a human presence"],
             "c": 3,
             "why": "The chapter grants that the attribute unclimbable comes from the project, "
                    "and then adds that one and the same project finds one rock an obstacle and "
                    "another a means. It never says every rock blocks every project, it does "
                    "not make the body decide, and it says there are no obstacles in themselves."},
            {"q": "Why, on the chapter's account, do the mountains look high to someone with no "
                  "plan to climb them?",
             "a": ["Because they exceed the body's power to take them in its stride, a "
                   "valuation made before any decision",
                   "Because the walker has secretly decided to climb them",
                   "Because they are high in themselves, apart from any body",
                   "Because the walker has just read Micromégas"],
             "c": 0,
             "why": "The general intentions of a body value the surroundings whatever it "
                    "decides. A secret decision is how the theory would save itself, which the "
                    "chapter answers; height in itself is denied; and Micromégas, the chapter "
                    "says, makes no difference."},
            {"q": "In the body preset the project tile prints none and the level tile prints "
                  "3 m. Why the difference?",
             "a": ["The level is lower than the capacity in that preset",
                   "The project reckoning marks rocks only for a climb; the level reckoning "
                   "compares every rock with the body's level whatever the project",
                   "The lab ignores the 3 m rock when there is no project",
                   "The 3 m rock is an obstacle only for walking past"],
             "c": 1,
             "why": "Both thresholds are 2 m in every preset, so neither is lower. The level "
                    "tile still marks the 3 m rock with no project, and walking past marks no "
                    "rock on the project's reckoning."},
        ],
        "mistakes": [
            ("Thinking Merleau-Ponty agrees with the theory of absolute freedom that obstacles exist only for a project",
             "He agrees with the first half and denies the conclusion. The attribute "
             "unclimbable does come from a project of climbing. But beneath every chosen "
             "project the body gives a general valuation: in the lab, with no project the "
             "project tile prints none and the level tile still prints 3 m. That is why, "
             "for the chapter, freedom is always in a field, and the mountains look high "
             "whether or not I have decided to climb them."),
            ("Thinking the chapter brings back obstacles in themselves",
             "It says plainly that &ldquo;there are no obstacles in themselves&rdquo; (p. "
             "512). What it denies is that the self that qualifies them is an acosmic "
             "subject outside the world. The valuation is the incarnate subject's, made "
             "before any decision, and it is still a valuation."),
            ("Taking the body's general level for a fixed fact the lab measures",
             "The 2 m is the lesson's illustrative figure. The chapter computes no heights; "
             "it says the general intentions come from having hands, feet and a body, that "
             "they are shared with everyone organised alike, and that attitudes often "
             "confirmed acquire a favoured status. A threshold is the model's simplification "
             "of that."),
        ],
        "standard": (
            "Finish when you can reckon an obstacle two ways and say which view each stands for.",
            "Given rock heights, a project, a capacity and a general level, mark the obstacles "
            "relative to the project and relative to the body, name the rock that is an "
            "obstacle on one reckoning only, and say which view each reckoning represents."
        ),
        "note": (
            "Both reckonings are the lesson's model with illustrative heights; the book "
            "computes nothing about rocks, and a threshold cannot show that the body's "
            "valuation is a meaning rather than a measurement. Whether the theory the "
            "chapter answers is Sartre's own or a sharpened version of it is disputed."
        ),
    },
    # ---------------------------------------------------------------- 08
    # Smith p. 527 (opening passage: "There is, therefore, never determinism
    # and never absolute choice, I am never a thing and never bare
    # consciousness."; the torture: "What withstands pain is not, in short, a
    # bare consciousness, but the prisoner with his comrades"; "We choose our
    # world and the world chooses us."); p. 529 ("The fact remains that I am
    # free ... but by means of them."); pp. 513-514 (the inferiority complex:
    # "this past, though not a fate, has at least a specific weight");
    # p. 514 (the idealist's voice on class: exploitation before
    # revolutionaries); p. 515 ("objective thought and analytical reflection
    # are two aspects of the same mistake"); pp. 515-516 (the day-labourer:
    # "his life is synchronized with the life of the town labourers");
    # p. 518 ("it is not the greatest poverty which produces the most
    # clear-sighted revolutionaries"; prosperity and social space); p. 528
    # (field of freedom; Hegel); p. 530 (the questions; "to teach us to see
    # them clearly once more"; Saint-Exupery: "Man is but a network of
    # relationships, and these alone matter to him.").
    {
        "slug": "freedom-in-situation",
        "title": "Freedom in Situation",
        "module": "Part Three · 3 · Freedom",
        "one_line": "There is never determinism and never absolute choice: I am free not in spite of my motives but by means of them, and the book ends on what that asks of us.",
        "summary": (
            "The chapter's second half sets the theory of absolute freedom beside "
            "determinism and finds them two forms of one mistake. Compute the records of the "
            "two over the chapter's cases, the inferiority complex, the hardship that does "
            "not make revolutionaries, the day labourer and the prisoner, and name the case "
            "each fails and the cases both fail."
        ),
        "key": [
            "never determinism, never absolute choice",
            "free by means of my motives",
            "survivors: none",
            "split: the complex and the hardship",
            "both fail: the labourer, the prisoner",
            "we choose the world, it chooses us",
        ],
        "key_label": "Freedom in situation in six lines",
        "concepts_intro": (
            "The last sixteen pages of the book replace the choice between two pictures of "
            "conduct with a third. Three ideas carry them."
        ),
        "concepts": [
            ("Determinism",
             "Here, the view that conduct is caused by objective conditions, as objective "
             "thought derives class consciousness from the worker's objective position."),
            ("Motivation",
             "A relation between a situation and what I do that is neither a cause, which "
             "would make me a thing, nor a pretext freely invented, which would make me pure "
             "consciousness."),
            ("Freedom in situation",
             "The chapter's account: freedom always meets a field already given meaning by "
             "the body, the past and other people, and works through it, so that the share "
             "of situation and the share of freedom cannot be told apart."),
        ],
        "read_title": "The passage first, then the chapter's second half and the book's end",
        "read_intro": (
            "The passage is the chapter's conclusion in two sentences two pages apart. The "
            "lesson reads the cases that lead to it, codes them against the two accounts, "
            "then reads the conclusion and the book's last page."
        ),
        "body": [
            ("p", "<strong>Part Three, Chapter 3, pp. 527 and 529.</strong> &ldquo;There is, "
                  "therefore, never determinism and never absolute choice, I am never a thing "
                  "and never bare consciousness.&rdquo; And two pages later: &ldquo;The fact "
                  "remains that I am free, not in spite of, or on the hither side of, these "
                  "motivations, but by means of them.&rdquo; Read from the sentences on "
                  "sedimentation in the middle of page 513, where the previous lesson stopped, "
                  "to the end of the book on page 530, in your own "
                  "copy before going on."),
            ("p", "The first case is a sentence about a life (pp. 513&ndash;514). Having built "
                  "our life on an inferiority complex for twenty years, it is not probable "
                  "that we shall change. A summary rationalism, the chapter says, would reply "
                  "that there are no degrees of possibility: either the free act is possible "
                  "or it is not, and probable is a word for statistics, not for anything "
                  "real. The chapter's answer is that generality and probability are "
                  "phenomena. To say the change is improbable means I have made inferiority my "
                  "abode, and &ldquo;this past, though not a fate, has at least a specific "
                  "weight&rdquo;."),
            ("p", "The two accounts the lab codes are the chapter's own pair (pp. "
                  "514&ndash;515). Objective thought derives class consciousness from the "
                  "objective condition of the proletariat; idealist reflection reduces that "
                  "condition to the awareness the proletarian arrives at. The lesson calls them "
                  "determinism and absolute freedom, and the chapter says that objective "
                  "thought and analytical reflection are &ldquo;two aspects of the same "
                  "mistake&rdquo;, two ways of overlooking the phenomena. On the "
                  "inferiority complex, determinism predicts the life it finds, and absolute "
                  "freedom, for which a free act could blow the complex sky-high at any "
                  "moment, cannot say why the change is improbable."),
            ("p", "The second case comes first in the idealist's voice. There was exploitation "
                  "long before there were revolutionaries, and the working-class movement does "
                  "not always advance in hard times; so, the idealist concludes, revolt is not "
                  "the outcome of objective conditions but of the worker's decision (p. 514). "
                  "The chapter keeps the fact and refuses the conclusion. One is right, it "
                  "says later, to point out that &ldquo;it is not the greatest poverty which "
                  "produces the most clear-sighted revolutionaries&rdquo;, but one forgets to "
                  "ask why a return of prosperity often radicalises the masses: easier "
                  "conditions open a new structure of social space (p. 518), which shows, the "
                  "chapter says, not that the worker makes himself a revolutionary from "
                  "nothing but that he does so on a basis of coexistence. The lesson codes "
                  "only the fact as the idealist states it: on that, determinism fails and "
                  "absolute freedom absorbs it. The prosperity point, which tells against "
                  "both, is left out of the table."),
            ("p", "The third case is the day labourer (pp. 515&ndash;516), with no farm and no "
                  "tools, going from farm to farm at harvest and feeling an anonymous power "
                  "making a nomad of him. That life can go on without any class consciousness, "
                  "so the conditions alone do not produce it, and when prices rise he may "
                  "blame the town workers instead. If class consciousness appears, it is not "
                  "because he decided to become a revolutionary, but because he has perceived "
                  "concretely that &ldquo;his life is synchronized with the life of the town "
                  "labourers&rdquo;. Social space acquires a magnetic field. The lesson codes "
                  "both accounts as failing him."),
            ("p", "The fourth case is a prisoner under torture (p. 527). If he refuses to give "
                  "the names and addresses, it is not by a solitary, unsupported decision: he "
                  "still feels himself with his comrades, involved in the common struggle, or "
                  "he has staked his life for years on facing this test. &ldquo;What withstands "
                  "pain is not, in short, a bare consciousness, but the prisoner with his "
                  "comrades&rdquo;, or else a proudly willed solitude, which is again a way "
                  "of being with others. Absolute freedom fails him, since no bare "
                  "consciousness holds out alone; the lesson codes determinism as failing too, "
                  "since the pain that would cause him to talk does not."),
            ("p", "The <code>all</code> preset shows the four. The record tile prints, for "
                  "determinism, absorbs 1 of 4 and fails 3, and the same for absolute "
                  "freedom. The survivors tile prints none. The split tile lists the cases "
                  "on which one account has y and the other n: the inferiority complex and "
                  "the exploitation before revolutionaries. The labourer and the prisoner "
                  "fail both. The <code>past</code> preset keeps only the complex, and "
                  "determinism survives it. The <code>class</code> preset keeps the hardship "
                  "and the labourer: determinism fails both, absolute freedom fails one, and "
                  "the survivors tile prints none."),
            ("def", ("Freedom in situation",
                     "Freedom that is always exercised in a field the body, the past and "
                     "other people have already given a meaning, and that takes up that "
                     "meaning to confirm or change it, without ever wholly creating or "
                     "wholly receiving it.")),
            ("p", "Freedom in situation is not a column, and the chapter states it in prose. "
                  "Our own initiatives, once entered on, carry us by a state rather than an "
                  "act, and in the exchange between a situation and the person who takes it "
                  "up it is impossible to determine the share contributed by each (p. 527). "
                  "&ldquo;We choose our world and the world chooses us.&rdquo; Freedom, after "
                  "Husserl's phrase, has a field: it shrinks, without ever disappearing, as "
                  "the room left by the body and by institutions narrows (p. 528)."),
            ("p", "So the opening sentences are not a compromise. Partly free and partly "
                  "determined would keep both pictures and divide the act between them, and "
                  "the chapter refuses the division. Hegel's synthesis of the in itself and the "
                  "for itself, it says, has its truth, but it does not conjure away our "
                  "finitude: by taking up a present I transform my past, but only by committing "
                  "myself somewhere else (p. 528). Psychoanalysis cures, the chapter adds, not "
                  "by an awareness of the past but by a new relationship with the doctor. "
                  "Every explanation of my conduct by my past, temperament and surroundings is "
                  "true, if taken not as a separable contribution but as a moment of my whole "
                  "being. That is what being free by means of my motives means."),
            ("p", "The book's last page asks three questions. Shall I make this promise? Shall "
                  "I risk my life for so little? Shall I give up my liberty to save liberty? "
                  "There is no theoretical reply to them, the chapter says, but there is this "
                  "person you love and these men around you who live as slaves, and your "
                  "freedom cannot be willed without willing freedom for all. Philosophy's only "
                  "function, before things or historical situations, is &ldquo;to teach us to "
                  "see them clearly once more&rdquo;, and here what is needed is silence, "
                  "since only the hero lives out his relation to men and the world (p. 530)."),
            ("p", "So the book gives the last word to someone else. Antoine de Saint-Exupéry, "
                  "the aviator and writer, flew a reconnaissance mission over Arras in May 1940 "
                  "and wrote it up in <em>Pilote de guerre</em> (1942). The book closes on a "
                  "passage from it, about a son caught in a fire and the one who will save "
                  "him, which ends: &ldquo;Man is but a network of relationships, and these "
                  "alone matter to him.&rdquo;"),
            ("p", "That is the end of the book, and of this Subject. It began with a Preface "
                  "that asked what phenomenology is and answered with a method that cannot be "
                  "completed; it ends with a freedom that cannot be found outside a world. "
                  "If you read the Preface first, read it again now: "
                  "“Description, Not Explanation”, the first lesson of What Phenomenology Is, "
                  "will read differently after the body, the perceived world and time."),
        ],
        "lab": ("phenkit", {
            "mode": "cases",
            "view": "table",
            "accounts": ["determinism", "absolute freedom"],
            "preset": "all",
            "presets": [
                {"id": "all", "label": "All four cases",
                 "observations": ("twenty years of an inferiority complex, y, n; "
                                  "exploitation long before revolutionaries, n, y; "
                                  "the day labourer and the town labourers, n, n; "
                                  "the prisoner holds out with his comrades, n, n"),
                 "expect": {"caRecord": ("determinism: absorbs 1 of 4, fails 3, silent 0; "
                                         "absolute freedom: absorbs 1 of 4, fails 3, silent 0"),
                            "caSurvivors": "none",
                            "caSplit": "twenty years of an inferiority complex, exploitation long before revolutionaries"}},
                {"id": "past", "label": "The inferiority complex alone",
                 "observations": "twenty years of an inferiority complex, y, n",
                 "expect": {"caSurvivors": "determinism",
                            "caRecord": ("determinism: absorbs 1 of 1, fails 0, silent 0; "
                                         "absolute freedom: absorbs 0 of 1, fails 1, silent 0"),
                            "caSplit": "twenty years of an inferiority complex"}},
                {"id": "class", "label": "The hardship and the day labourer",
                 "observations": ("exploitation long before revolutionaries, n, y; "
                                  "the day labourer and the town labourers, n, n"),
                 "expect": {"caRecord": ("determinism: absorbs 0 of 2, fails 2, silent 0; "
                                         "absolute freedom: absorbs 1 of 2, fails 1, silent 0"),
                            "caSurvivors": "none",
                            "caSplit": "exploitation long before revolutionaries"}},
            ],
            "panel_title": "Determinism and absolute freedom over the cases",
            "panel_intro": (
                "This lab counts the lesson's coding: each of the chapter's cases is marked y, n "
                "or - against two opponent accounts, and the lab counts each record, the "
                "accounts that fail none, and the cases on which they part. The count is exact; "
                "the coding is the lesson's reading, and freedom in situation is in the prose."
            ),
        }),
        "steps_title": "Counting two accounts of conduct",
        "steps_intro": "Five steps; the last is not counted.",
        "steps": [
            ("Code each case",
             "Mark each case y, n or - against determinism and against absolute freedom, "
             "with the page."),
            ("Count each record",
             "For each account, count the cases it absorbs, fails and is silent on."),
            ("Find the survivors and the split",
             "List the accounts that fail no case, and the cases on which one has y and the "
             "other n."),
            ("Find the cases both fail",
             "List the cases marked n against both accounts."),
            ("State the third account",
             "Describe freedom in situation from the chapter's sentences, without scoring it."),
        ],
        "worked": {
            "title": "Four cases, two accounts",
            "intro": [
                "Code the inferiority complex, the hardship that does not make revolutionaries, "
                "the day labourer and the prisoner against determinism and absolute freedom.",
            ],
            "lines": [
                "determinism:  y, n, n, n;  absorbs 1 of 4, fails 3",
                "absolute freedom:  n, y, n, n;  absorbs 1 of 4, fails 3",
                "survivors:  none",
                "split:  cases 1 and 2",
                "both fail:  cases 3 and 4",
            ],
            "after": [
                "Each account absorbs exactly the case the other fails, and both fail the two "
                "cases in which conduct comes from coexistence with others: the labourer's "
                "common lot and the prisoner's comrades. The chapter's account is stated in "
                "prose, because a column the lesson coded for it would succeed by coding.",
            ],
        },
        "quiz_title": "Freedom in situation",
        "quiz": [
            {"q": "Determinism is coded y, n, n, n and absolute freedom n, y, n, n. On which "
                  "cases do they part?",
             "a": ["Cases 3 and 4", "All four cases", "None of the cases", "Cases 1 and 2"],
             "c": 3,
             "why": "A split is a case marked y against n. Cases 3 and 4 are n against n, "
                    "which both accounts fail rather than a split, so only cases 1 and 2 count."},
            {"q": "On the chapter's account, when the day labourer becomes class-conscious, why "
                  "does he?",
             "a": ["Because he perceives concretely that his life is synchronized with the town "
                   "labourers' and that all share a common lot",
                   "Because he decides to become a revolutionary and values his condition "
                   "accordingly",
                   "Because his poverty passes a fixed threshold",
                   "Because agitators persuade him of what he does not feel"],
             "c": 0,
             "why": "The chapter denies that he decided first, notes that the same conditions can "
                    "last without any class consciousness, and dismisses the agitator theory as "
                    "the prefect of police's view of history."},
            {"q": "Why is freedom in situation not partly free and partly determined?",
             "a": ["Because the two shares are always exactly equal",
                   "Because there is never determinism and never absolute choice; I am free by "
                   "means of my motives, not in a share they leave over",
                   "Because freedom is total and the situation only apparent",
                   "Because the situation is total and freedom only apparent"],
             "c": 1,
             "why": "The chapter says the shares cannot be determined at all, so they cannot "
                    "be equal; and making either side total is the return to absolute freedom "
                    "or to determinism that it rejects."},
            {"q": "What withstands pain, in the chapter's case of the prisoner?",
             "a": ["A bare consciousness deciding alone",
                   "His body's tolerance of pain",
                   "The prisoner with his comrades, or a proudly willed solitude that is "
                   "still a way of being with others",
                   "Nothing; the chapter says he speaks in the end"],
             "c": 2,
             "why": "The chapter says in so many words that what withstands pain is not a bare "
                    "consciousness. It says nothing of a physical tolerance, and its prisoner "
                    "refuses to give the names."},
        ],
        "mistakes": [
            ("Thinking freedom in situation is a compromise: partly free, partly determined",
             "The chapter rejects the arithmetic of shares without returning to either "
             "whole: there is never determinism and never absolute choice, and the share "
             "contributed by the situation and the share contributed by freedom cannot be "
             "determined. In the lab each opponent fails three of four cases and both fail "
             "the labourer and the prisoner, but a third column would not be a mixture of "
             "the two. I am free &ldquo;not in spite of, or on the hither side of, these "
             "motivations, but by means of them&rdquo;."),
            ("Thinking the chapter sides with determinism because it denies absolute freedom",
             "It denies both. Nothing determines me from outside, the book's last page says, "
             "not because nothing acts on me but because I am from the start outside myself "
             "and open to the world. The inferiority complex has weight, and it is still not "
             "a fate."),
            ("Reading the table's both-fail cases as Merleau-Ponty's score",
             "The labourer and the prisoner fail both accounts on the lesson's coding of four "
             "cases the lesson chose. Merleau-Ponty's own account is never a column and never "
             "scored; a column coded for it would have a clean sheet because the coding made "
             "it so."),
        ],
        "standard": (
            "Finish when you can count two accounts of conduct and state the third without scoring it.",
            "Given the chapter's cases coded against determinism and absolute freedom, compute "
            "each record, the survivors, the split and the cases both fail, and state freedom "
            "in situation from the chapter's sentences."
        ),
        "note": (
            "The four cases are the book's reports, chosen and coded by the lesson; the count "
            "is exact and the coding is an interpretation, especially for the prisoner, whom "
            "the chapter does not set against determinism in so many words. The lab measures "
            "no one's freedom. How fairly the chapter treats Sartre is disputed."
        ),
    },
]
