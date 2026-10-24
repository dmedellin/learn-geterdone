"""What Phenomenology Is, lessons 1-4 -- the Preface, one lesson per theme.

Every quotation is copied from Colin Smith's translation, Routledge Classics
pagination (Preface pp. vii-xxiv); the comment beside each lesson gives its
pages. Smith's ligatures are printed as plain letters, a word split by a
line-break hyphen is joined, and footnote numerals are left out. Nothing else
is changed. The Preface has no figures and no cases, so each lab is the
lesson's illustration of the method, and each lesson says so.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Smith pp. ix-x (opening passage: "It is a matter of describing ..." and
    # "To return to things themselves ... a river is"); p. vii (the opening
    # question); p. ix (the foreswearing of science, the realm of science,
    # second-order expression, naive and dishonest, the absolute source);
    # p. xi (described, not constructed; the background of all acts).
    # The horizon moon is treated later in the book: Introduction 3, pp. 32
    # and 36, and Part Two, Chapter 2 (depth), p. 302.
    {
        "slug": "description-not-explanation",
        "title": "Description, Not Explanation",
        "module": "Preface",
        "one_line": "Phenomenology describes the world as it is perceived before it explains it, because every explanation, the scientific kind included, is about a world already perceived.",
        "summary": (
            "The Preface opens by asking what phenomenology is and answers first with a "
            "demand: describe, do not explain or analyse. Compute the angle the moon "
            "subtends at the horizon and overhead, find that the overhead moon is the "
            "larger by the angle, and say which question the figures answer and which "
            "they leave to description."
        ),
        "key": [
            "describe; do not explain or analyse",
            "science: a second-order expression",
            "science maps a world already perceived",
            "angular size = size / distance",
        ],
        "key_label": "The first theme in four lines",
        "concepts_intro": (
            "The Preface's first theme takes two pages. It sets phenomenology against two "
            "ways of doing without the perceived world, one scientific and one "
            "philosophical."
        ),
        "concepts": [
            ("Description",
             "To describe is to say what is given, as it is given, before asking what "
             "caused it or what it is made of. The Preface asks for a direct description "
             "of experience without its psychological origin or the causal explanations "
             "a scientist, historian or sociologist could supply."),
            ("A second-order expression",
             "Science is built on the world as directly experienced, and speaks about it "
             "in a sign-language of its own. The Preface does not call the sign-language "
             "false. It calls it derivative, as a map is derivative of the land it maps."),
            ("Analytical reflection",
             "The second procedure the demand excludes. Descartes and Kant went back from "
             "the world to the subject as its condition. The Preface's objection is that "
             "this rebuilds the world from outside experience and offers a "
             "reconstruction where a description was needed."),
        ],
        "read_title": "The passage first, then the Preface's opening pages line by line",
        "read_intro": (
            "The passage is the demand itself and the comparison that explains it. The "
            "lesson then goes back to the Preface's first page, where the question is "
            "asked, and follows the argument to the comparison."
        ),
        "body": [
            ("p", "<strong>Preface, pp. ix&ndash;x.</strong> &ldquo;It is a matter of "
                  "describing, not of explaining or analysing. &hellip; To return to things "
                  "themselves is to return to that world which precedes knowledge, of which "
                  "knowledge always speaks, and in relation to which every scientific "
                  "schematization is an abstract and derivative sign-language, as is "
                  "geography in relation to the country-side in which we have learnt "
                  "beforehand what a forest, a prairie or a river is.&rdquo; The two "
                  "sentences are from pages ix and x of Colin Smith's translation. Read the "
                  "Preface from its first page, vii, to the end of the first paragraph on "
                  "page xii, just before the reduction is introduced, in your own copy "
                  "before going on; the lesson goes back through it a phrase at a time."),
            ("p", "Think of the last time you saw the full moon come up behind the roofs: "
                  "enormous, low, almost close enough to touch, and an hour later, high in "
                  "the sky, an ordinary coin of light. Ask why and you will be offered an "
                  "explanation. The lab first does something plainer. It computes the angle "
                  "the moon subtends at your eye, from modern astronomy's figures: 3,474 km "
                  "across at 384,400 km gives `3474 / 384400 = 1737/192200`, about `0.0090` "
                  "radians or half a degree. That is the <code>horizon</code> preset. The "
                  "moon is the lesson's example, not the Preface's, which has no examples of "
                  "this kind; the book comes back to the horizon moon in Introduction III, on "
                  "attention and judgement, and again in Part Two, Chapter 2, on depth."),
            ("p", "Now the Preface itself. It begins with a question that sounds as if it "
                  "should have been settled: &ldquo;What is phenomenology?&rdquo; Half a "
                  "century after Husserl's first works, Merleau-Ponty says, it still has not "
                  "been answered, and he shows why by setting out what looks like a list of "
                  "contradictions. Phenomenology studies essences, and puts essences back "
                  "into existence. It suspends the assertions of the natural attitude, the "
                  "everyday stance in which the world is simply taken for granted, and "
                  "holds that the world is always already there before reflection begins. "
                  "It wants to be a rigorous science, and gives an account of space, time "
                  "and the world as we live them. It describes experience without its "
                  "causes, and yet Husserl's last works speak of a genetic phenomenology. A "
                  "reader pressed for time, he says, will wonder whether a philosophy which "
                  "cannot define its scope is not a myth or a fashion."),
            ("p", "His answer is not a definition. Phenomenology, he says, can be practised "
                  "and recognised as a manner or style of thinking; it existed as a movement "
                  "before it was fully aware of itself as a philosophy, and it is accessible "
                  "only through its own method. So the Preface does not define it. It runs "
                  "through the celebrated themes one by one, and the first is description."),
            ("def", ("Describing, explaining, analysing",
                     "To explain is to say what caused a thing; to analyse, in the Preface's "
                     "sense, is to go back from the world to the acts of a subject that "
                     "would have put it together. To describe is to say what is given, as "
                     "it is given, before either.")),
            ("p", "Edmund Husserl trained as a mathematician before he turned to philosophy, "
                  "and the slogan he gave the movement, back to the things themselves, was "
                  "an instruction to look before theorising. The Preface reads his early "
                  "directive, that phenomenology should be a descriptive psychology and "
                  "return to the things themselves, as &ldquo;a foreswearing of "
                  "science&rdquo;. That is a strong phrase, and it is the Preface's own. "
                  "Read on to see what is forsworn. The next sentences are in the first "
                  "person: I am not the meeting-point of causes that settle my body and my "
                  "mind, I cannot think of myself as a mere object of biology, psychology or "
                  "sociology, and &ldquo;I cannot shut myself up within the realm of "
                  "science&rdquo;. What is refused is a standpoint, taking oneself as nothing "
                  "but a bit of the world, and not a result."),
            ("p", "The reason follows. Everything I know about the world, scientific "
                  "knowledge included, is gained from my own point of view, or from an "
                  "experience of the world without which the symbols of science would mean "
                  "nothing. The universe of science is built on the world as directly "
                  "experienced, and if we want to judge exactly what science means and how "
                  "far it reaches, we have to start by reawakening the experience of which "
                  "science is the &ldquo;second-order expression&rdquo;. Scientific points "
                  "of view on which my existence is one moment of the world's are, he says, "
                  "&ldquo;naïve and at the same time dishonest&rdquo;, because they take "
                  "for granted, without saying so, the other point of view, that of "
                  "consciousness, through which a world first forms round me and begins to "
                  "exist for me."),
            ("p", "Now go back to the passage's second sentence. The world &ldquo;which "
                  "precedes knowledge&rdquo; is the one you were in before you learned "
                  "anything about it. Knowledge &ldquo;always speaks&rdquo; of it: there is "
                  "nothing else for knowledge to be about. And every scientific "
                  "schematization stands to it as geography stands to the countryside. A map "
                  "is not false, and you can steer by it. But you can read its symbol for a "
                  "forest only because you have been in one; you &ldquo;have learnt "
                  "beforehand what a forest, a prairie or a river is&rdquo;. The map depends "
                  "on the countryside, and the countryside does not depend on the map."),
            ("p", "The demand for description rules out a second procedure as well, and "
                  "this one is harder to see as an opponent, because it also turns from the "
                  "world to the subject. Descartes, and Kant above all, showed that I could "
                  "not grasp anything as existing unless I first experienced myself as "
                  "existing in the act of grasping it, and they made consciousness the "
                  "condition of there being anything at all. At its strength the argument is "
                  "simple: whatever world there is, it is a world for someone. The Preface "
                  "grants that the act of relating is nothing without the world in which "
                  "relations are found, and that for Kant the unity of consciousness comes "
                  "with the unity of the world. Its objection is that analytical reflection "
                  "goes back to the subject as a condition distinct from experience, and so "
                  "offers a reconstruction in place of an account. The alternative is one "
                  "sentence: &ldquo;The real has to be described, not constructed or "
                  "formed.&rdquo;"),
            ("p", "That is why perception cannot be put in the same class as judgements. "
                  "Your field of perception is full of flickers of colour, noises and "
                  "passing touches you could not place precisely, and you place them in the world at once, without "
                  "ever confusing them with daydreams. If the reality of what you perceive "
                  "rested on the coherence of your representations, you would be forever "
                  "taking apart bad syntheses and making new ones, and you are not. "
                  "Perception, the Preface says, is not a science of the world and not even "
                  "a deliberate act; it is &ldquo;the background from which all acts stand "
                  "out&rdquo;."),
            ("p", "Back to the moon. The <code>zenith</code> preset puts it overhead, about "
                  "one Earth radius nearer you: `3474 / 378029`, about `0.0092` radians. By "
                  "the angle the overhead moon is the larger, by about two per cent, and it "
                  "is the one that looks small. The <code>disc</code> preset is a 7 mm disc "
                  "held at 77 cm: `1/110`, about `0.0091` radians, enough to cover the "
                  "horizon moon at the lab's mean distance and not quite enough for the moon "
                  "overhead. In Introduction III the book reports the old test of a cardboard tube or a "
                  "telescope, through which the horizon moon looks no bigger than at the "
                  "zenith. The intellectualist takes that to show the size never changed; "
                  "Merleau-Ponty replies that the tube makes a different, analytic kind of "
                  "looking, and settles nothing about the moon seen freely."),
            ("p", "So which question do the figures answer? How large an angle the moon "
                  "subtends at your eye, from a size and a distance that astronomers measured "
                  "and you have taken on trust. Which do they leave open? How large the moon "
                  "looks, low over the roofs. The usual next step is an explanation, and the "
                  "book reports an old one: the many objects between you and the horizon "
                  "stress the distance and so enlarge the moon. The Preface asks for "
                  "something that comes before any such account, a description of the huge "
                  "moon as it is given. Nothing in the lab's figures is denied by that. They "
                  "are the map, and the moon over the roofs is the countryside."),
            ("p", "Description needs a way of seeing what is usually too close to notice. "
                  "The next lesson, “The Reduction and Its Limit”, reads the Preface's "
                  "account of that step, and of why it can never be finished."),
        ],
        "lab": ("phenkit", {
            "mode": "size",
            "view": "angle",
            "model": "geometric optics (the small-angle form)",
            "preset": "horizon",
            "presets": [
                {"id": "horizon",
                 "label": "The moon at the horizon: 3,474 km across at 384,400 km (modern astronomy's figures)",
                 "size": 3474, "distance": 384400, "unit": "km",
                 "expect": {"szRatio": "1737/192200 ≈ 0.0090 rad", "szDegrees": "≈ 0.52°"}},
                {"id": "zenith",
                 "label": "The moon overhead: about one Earth radius nearer, at 378,029 km",
                 "size": 3474, "distance": 378029, "unit": "km",
                 "expect": {"szRatio": "3474/378029 ≈ 0.0092 rad", "szDegrees": "≈ 0.53°"}},
                {"id": "disc",
                 "label": "A 7 mm disc held at 77 cm (illustrative)",
                 "size": 7, "distance": 770, "unit": "mm",
                 "expect": {"szRatio": "1/110 ≈ 0.0091 rad", "szDegrees": "≈ 0.52°"}},
            ],
            "panel_title": "The angle the moon subtends",
            "panel_intro": (
                "This lab computes geometric optics in its small-angle form: the angle an "
                "object subtends at the eye is its size divided by its distance, in "
                "radians. Compare the horizon and zenith presets: the figures are exact, and "
                "neither is a report of how large the moon looks."
            ),
        }),
        "steps_title": "Computing an angular size, and what it answers",
        "steps_intro": "Four steps, the last of which is the lesson's.",
        "steps": [
            ("Put size and distance in one unit",
             "Write the object's size and its distance in the same unit, kilometres with "
             "kilometres or millimetres with millimetres. The ratio then has no unit left."),
            ("Divide",
             "The angle subtended is size divided by distance, in radians. For an angle "
             "this small the ratio and the angle agree far more closely than the figures "
             "themselves are known."),
            ("Convert if degrees are wanted",
             "Multiply by 180 and divide by π, about 57.3. The lab marks every degree "
             "figure approximate, because π is not a fraction."),
            ("Name what the figure answers",
             "State the question the number settles, how wide an angle the object "
             "subtends at the eye, and the question it leaves open: how large the object "
             "looks, which is a matter for description."),
        ],
        "worked": {
            "title": "The moon low and high",
            "intro": [
                "Take the moon as 3,474 km across, 384,400 km away at the horizon and about "
                "one Earth radius, 6,371 km, nearer when it is overhead. You want both "
                "angles, and which is larger.",
            ],
            "lines": [
                "horizon:  3474 / 384400 = 1737/192200 ≈ 0.0090 rad",
                "overhead distance:  384400 − 6371 = 378029 km",
                "overhead:  3474 / 378029 ≈ 0.0092 rad",
                "in degrees:  ≈ 0.52° low, ≈ 0.53° high",
                "a 7 mm disc at 770 mm:  7 / 770 = 1/110 ≈ 0.0091 rad",
            ],
            "after": [
                "By the angle the overhead moon is the larger, and it is the one that looks "
                "small. The disc covers the horizon moon and falls just short of the moon "
                "overhead. Every figure here is correct, and none of them is the huge moon "
                "over the roofs: that is what the Preface asks you to describe.",
            ],
        },
        "quiz_title": "Description and the figures",
        "quiz": [
            {"q": "A coin 9 mm across is held 99 cm from the eye. What angle does it subtend, "
                  "as a ratio?",
             "a": ["1/110 rad", "1/11 rad", "11/1000 rad", "110 rad"],
             "c": 0,
             "why": "Put both in millimetres: `9 / 990 = 1/110`. Dividing 9 by 99 mixes "
                    "millimetres and centimetres and gives `1/11`, ten times too large. "
                    "`11/1000` is close in size but is not the ratio, and 110 rad is the "
                    "ratio upside down."},
            {"q": "The lab gives about 0.0090 rad for the horizon moon and about 0.0092 rad "
                  "for the moon overhead. What do these figures settle?",
             "a": ["How large an angle the moon subtends at the eye in each position",
                   "How large the moon looks in each position",
                   "Why the horizon moon looks larger",
                   "That the horizon moon is an error of perception"],
             "c": 0,
             "why": "Size over distance is the angle subtended, and that is all it is. How "
                    "large the moon looks is what the figures leave open, which is why the "
                    "overhead moon can be larger by the angle and look smaller. They give no "
                    "cause of the difference, and calling it an error already assumes the "
                    "angle is what should be seen."},
            {"q": "In the Preface's comparison, geography stands to the countryside as "
                  "science stands to what?",
             "a": ["The world as perceived, which comes before any knowledge of it",
                   "The measurements scientists take",
                   "Consciousness, as the condition of there being a world",
                   "A map drawn more carefully"],
             "c": 0,
             "why": "The countryside is where we learnt beforehand what a forest or a river "
                    "is: the perceived world that knowledge speaks of. Measurements belong "
                    "to the map side. Consciousness as the world's condition is analytical "
                    "reflection's answer, which the Preface rejects in the next paragraph, "
                    "and a better map is still a map."},
            {"q": "The demand for pure description, the Preface says, excludes two "
                  "procedures. Which two?",
             "a": ["Scientific explanation and analytical reflection",
                   "Scientific explanation and the study of essences",
                   "Every kind of reflection and every kind of science",
                   "Measurement and memory"],
             "c": 0,
             "why": "The text names scientific explanation on the one hand and the analytical "
                    "reflection of Descartes and Kant on the other. The study of essences is "
                    "part of phenomenology, as the Preface's first page says. Reflection is "
                    "not excluded as such, only the kind that reconstructs the world from "
                    "a subject outside experience, and memory is not mentioned."},
        ],
        "mistakes": [
            ("Thinking phenomenology rejects science",
             "The Preface does call Husserl's directive &ldquo;a foreswearing of "
             "science&rdquo;, and a reader who stops there takes phenomenology to deny "
             "what science finds. What is refused is shutting oneself up within science "
             "and taking oneself for nothing but its object. The figures stay: the overhead "
             "moon subtends `3474/378029`, about `0.0092` rad, more than the horizon moon's "
             "`0.0090`, and nothing in the Preface says otherwise. What it denies is that the "
             "figure is the first word about the moon you saw. Science is the "
             "&ldquo;second-order expression&rdquo; of a world already perceived, as "
             "geography is of the countryside, and naïve when it forgets that."),
            ("Taking description for a report of private feelings",
             "Describing is not introspection, a list of inner states with the world left "
             "out. What the Preface asks to have described is the world as perceived: the "
             "huge moon is a moon over the roofs, not a sensation in you. Later in the "
             "Preface the view that we only ever experience states of ourselves is named "
             "sensationalism and set aside, and the Introduction argues against it at length."),
            ("Hearing the first person as idealism",
             "Sentences such as &ldquo;I am the absolute source&rdquo; sound like the subject "
             "of Descartes or Kant laying down the world. The Preface says at once that its "
             "return to things is absolutely distinct from the idealist return to "
             "consciousness: analytical reflection rebuilds the world from a subject outside "
             "experience, and the Preface wants the world described as it is given to a "
             "subject already in it."),
        ],
        "standard": (
            "Finish when you can compute an angular size and say what it does not tell you.",
            "Given an object's size and distance, compute the angle it subtends as a ratio "
            "and in degrees, compare two such figures, and state which question about the "
            "object the figures answer and which they leave to description."
        ),
        "note": (
            "The moon's figures are modern astronomy's mean values, and the moon is the "
            "lesson's example: the Preface gives none. The lab computes the angle the moon "
            "subtends, which nothing in the Preface disputes. It cannot compute how large "
            "the moon looks, and nothing in it decides whether description should come "
            "before explanation; that is the Preface's claim, and the book argues for it "
            "over five hundred pages."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Smith p. xv (opening passage: "Reflection does not withdraw ... strange
    # and paradoxical"; Fink's 'wonder'; the constant theme of philosophy;
    # the most important lesson; absolute mind; no thought embracing all our
    # thought; perpetual beginner); p. xiv (refuse it our complicity, ohne
    # mitzumachen, 'out of play'); p. x (Descartes's methodical doubt).
    # The book's reversible cube: Part Two, Chapter 2 (depth), p. 306, Fig. 1.
    {
        "slug": "the-reduction-and-its-limit",
        "title": "The Reduction and Its Limit",
        "module": "Preface",
        "one_line": "The reduction does not doubt the world; it loosens our hold on it so that the hold can be seen, and it can never be completed.",
        "summary": (
            "Husserl's phenomenological reduction, read through his assistant Eugen Fink, "
            "is a step back that lets the threads tying us to the world show, and its most "
            "important lesson is that it can never be complete. Compute what a drawing of "
            "a cube fits: two solids that draw the identical edges, so that which face is "
            "in front is not in the drawing at all."
        ),
        "key": [
            "reduction: suspend, do not doubt",
            "it makes the world strange, and visible",
            "no complete reduction is possible",
            "wire cube: 12 edges, 2 readings",
            "solid cube: 9 edges, 1 reading",
        ],
        "key_label": "The reduction in five lines",
        "concepts_intro": (
            "The reduction is the most argued-over idea in Husserl, and the Preface gives "
            "it a reading of its own. Three ideas carry that reading."
        ),
        "concepts": [
            ("The reduction",
             "Husserl's name for the philosopher's step back from the natural attitude, "
             "in which the world is simply taken for granted. On the Preface's reading it "
             "withdraws nothing; it suspends our complicity with the world so that the "
             "world, and our tie to it, can be seen."),
            ("Wonder",
             "Eugen Fink's word for the reduction, which the Preface calls its best "
             "formulation. What is familiar becomes strange, and only then is it noticed."),
            ("The limit",
             "Because the one reflecting is in the world and in time, no reflection can "
             "take in everything it rests on. The philosopher is always beginning, and "
             "that, the Preface says, is the reduction's chief lesson."),
        ],
        "read_title": "The passage first, then the reduction line by line",
        "read_intro": (
            "The passage is the Preface's own description of the reduction, given right "
            "after it names Fink. The lesson reads it phrase by phrase, then the rest of its "
            "paragraph, which says why the reduction cannot be finished."
        ),
        "body": [
            ("p", "<strong>Preface, p. xv.</strong> &ldquo;Reflection does not withdraw "
                  "from the world towards the unity of consciousness as the world's basis; "
                  "it steps back to watch the forms of transcendence fly up like sparks from "
                  "a fire; it slackens the intentional threads which attach us to the world "
                  "and thus brings them to our notice; it alone is consciousness of the "
                  "world because it reveals that world as strange and paradoxical.&rdquo; "
                  "The sentence is on page xv of Smith's translation. Read the section from "
                  "its first line on page xii, where the reduction is introduced, to the end "
                  "on page xvi, in your own copy before going on."),
            ("p", "The sentence comes straight after a name. The best formulation of the "
                  "reduction, the Preface says, is probably Eugen Fink's, when he spoke of "
                  "&ldquo;wonder&rdquo; in the face of the world. Fink was Husserl's "
                  "assistant in Freiburg from 1928, and in 1933 he published a defence of "
                  "Husserl against his critics to which Husserl added a foreword saying it "
                  "spoke for him. Merleau-Ponty cites that essay here, and he leans "
                  "throughout the section on Fink and on Husserl's unpublished manuscripts. "
                  "That is the first thing to know about this reading of the reduction: it "
                  "is a reading, it draws on texts most of Husserl's readers in 1945 had not "
                  "seen, and whether it is Husserl's own view is still disputed."),
            ("p", "The reading it sets aside is Husserl's best-known presentation. For a long "
                  "time, the Preface says, and even in recent texts, the reduction was "
                  "presented as a return to a transcendental consciousness before which the "
                  "world lies spread out and completely transparent, so that the "
                  "philosopher's task is to rebuild, from the result, the acts that gave it "
                  "meaning. The Preface's example is a red book: my sensation of redness is "
                  "taken as showing a redness, the redness a red surface, the surface a piece "
                  "of red cardboard, and that a red thing, this book. Followed to the end, "
                  "that road leads to an idealism in which the world is meaning, and Peter's "
                  "view and Paul's are the same view seen from nowhere in particular."),
            ("p", "Now the passage. Reflection &ldquo;does not withdraw from the "
                  "world&rdquo;: it does not retreat into consciousness as the world's "
                  "foundation, which is the move just described. It &ldquo;steps "
                  "back&rdquo;, which is a different thing: you step back from a painting to "
                  "see it, not to stop looking. What it sees are &ldquo;the forms of "
                  "transcendence&rdquo;, the ways consciousness is always already out among "
                  "things, and they fly up like sparks: they were there all along, and the "
                  "step back is what lets them show. Then the image the section is known "
                  "for: reflection &ldquo;slackens the intentional threads which attach us to "
                  "the world&rdquo;. A thread pulled tight is invisible from inside the pull. "
                  "Let it go slack and you see it."),
            ("p", "The sentences before the passage say why the step is needed at all. We "
                  "are through and through made of relationships with the world, so the only "
                  "way to become aware of them is to suspend them, &ldquo;to refuse it our "
                  "complicity&rdquo;, to look on, in Husserl's phrase, &ldquo;ohne "
                  "mitzumachen&rdquo;, without joining in, or to put it &ldquo;out of "
                  "play&rdquo;. Not because the certainties of common sense are rejected; "
                  "they are &ldquo;the constant theme of philosophy&rdquo;. It is because "
                  "they are the basis of every thought that they go unnoticed, and to bring "
                  "them into view we have to suspend our acceptance of them for a moment."),
            ("def", ("The phenomenological reduction (the Preface's reading)",
                     "A suspension of our complicity with the world, so that the ties "
                     "taken for granted in the natural attitude come into view. It "
                     "withdraws no belief and is not a doubt; it makes the familiar world "
                     "appear strange and paradoxical.")),
            ("p", "It is easy to hear this as Descartes again, and the comparison deserves "
                  "its full strength. In the <em>Meditations</em> of 1641 Descartes resolves "
                  "to withhold assent from anything that can be doubted, the existence of his "
                  "own body and of the world included, until he reaches something that "
                  "cannot: that he thinks, and so is. Husserl himself introduced his "
                  "suspension by way of Descartes's attempt at universal doubt, while "
                  "insisting that the two differ. The Preface's own remark on Descartes, back on "
                  "page x, is a concession to idealism made just before an objection: in "
                  "Descartes &ldquo;methodical doubt does not deprive us of anything&rdquo;, "
                  "since the whole world comes back in the cogito, as certain as before, but "
                  "labelled thought of the world. The objection follows at once: if subject "
                  "and world were really on a par, the world's certainty would be given with "
                  "the cogito's, and what comes back is only the world as thought. Doubt "
                  "withdraws assent and wins the world back as thought. The reduction, on the "
                  "Preface's reading, withdraws nothing: it suspends our complicity to see "
                  "the ground we were already standing on."),
            ("p", "Then the turn the section is building to. Every misunderstanding between "
                  "Husserl and his interpreters, the Preface says, and between Husserl and "
                  "himself, comes from the same two facts: to see the world as strange we "
                  "must break with our familiar acceptance of it, and from that break we "
                  "learn nothing but the world's unmotivated upsurge. &ldquo;The most "
                  "important lesson which the reduction teaches us is the impossibility of a "
                  "complete reduction.&rdquo; That is why Husserl kept going back to it. "
                  "&ldquo;If we were absolute mind, the reduction would present no "
                  "problem.&rdquo; We are not. We are in the world, our reflections happen in "
                  "the flow of time they are trying to grasp, and so &ldquo;there is no "
                  "thought which embraces all our thought&rdquo;."),
            ("p", "The section then unfolds one phrase from Husserl's unpublished work: the "
                  "philosopher is &ldquo;a perpetual beginner&rdquo;. It means, the Preface "
                  "says, that he takes nothing for granted that people, learned or not, "
                  "believe they know; that philosophy may not take itself for granted either, "
                  "even when it has said something true; and that reflection at its most "
                  "radical is an awareness of its own dependence on an unreflective life it "
                  "can never get behind. So, the Preface concludes, the reduction is not a "
                  "procedure of idealist philosophy at all. It belongs to existential "
                  "philosophy, and Heidegger's being-in-the-world appears only against its "
                  "background."),
            ("p", "The lab gives the step back a shape you can compute. The Preface has no "
                  "drawing; the reversible cube is the lesson's illustration of something "
                  "habit had supplied. The <code>cube</code> preset draws a wire cube in "
                  "parallel projection, with the back square offset by half an edge. Reading "
                  "A takes one square as the front; reading B is its mirror image across the "
                  "plane perpendicular to the line of sight, with front and back exchanged. "
                  "Both draw the identical 12 edges, so the lab prints 2 readings. You saw a "
                  "cube with a front at once. Which square is in front is not in the lines; "
                  "it was your contribution, and the drawing that can flip is what lets you "
                  "notice it."),
            ("p", "The <code>box</code> preset does the same with a wire box 2 by 1 by 1: 12 "
                  "edges, 2 readings, identical drawings. The <code>solid</code> preset is "
                  "different. A solid cube hides three of its edges, so reading A draws 9; "
                  "reading B would hide three others and draw a different 9, and the lab "
                  "prints 1 reading. Opaque things settle what wire leaves open. The book "
                  "has its own reversible figure, in Part Two, Chapter 2, on depth (page "
                  "306): a cube seen from below with one face in front, or from above with "
                  "the other, or as a flat mosaic of ten triangles and a square."),
            ("p", "Nothing about the drawing was doubted in any of this. The edges are where "
                  "they are, and the lab's 12 is exact. What changed is that a setting you "
                  "had supplied without noticing became visible, which is the Preface's "
                  "point about the reduction in small. The next lesson, “Essences and "
                  "Existence”, asks what the step back is for, if it is not to leave the "
                  "world behind."),
        ],
        "lab": ("phenkit", {
            "mode": "perspective",
            "view": "necker",
            "model": "parallel projection",
            "preset": "cube",
            "presets": [
                {"id": "cube", "label": "A wire cube, back square offset by half an edge",
                 "object": "wire cube", "offset": "1/2",
                 "expect": {"peEdges": "12", "peReadings": "2", "peSame": "identical drawings"}},
                {"id": "box", "label": "A wire box 2 by 1 by 1",
                 "object": "wire box 2 1 1", "offset": "1/2",
                 "expect": {"peEdges": "12", "peReadings": "2", "peSame": "identical drawings"}},
                {"id": "solid", "label": "A solid cube: hidden edges left out",
                 "object": "solid cube", "offset": "1/2",
                 "expect": {"peEdges": "9", "peReadings": "1", "peSame": "different drawings"}},
            ],
            "panel_title": "One drawing, two solids",
            "panel_intro": (
                "This lab computes parallel projection: it draws a figure as reading A, "
                "draws its mirror image with front and back exchanged as reading B, and "
                "compares the edges. Switch from the cube preset to the solid preset and "
                "watch the readings tile."
            ),
        }),
        "steps_title": "Finding what a drawing does not decide",
        "steps_intro": "Four steps, the same for any line drawing of a solid.",
        "steps": [
            ("Draw reading A",
             "Project the solid onto the page along a fixed direction and list the edges "
             "drawn. For a wire figure every edge is drawn; for a solid one the hidden "
             "edges are left out."),
            ("Form reading B",
             "Take the mirror image of the solid across the plane perpendicular to the "
             "line of sight. Its front is A's back, and its back is A's front."),
            ("Compare the drawings",
             "Project B the same way. If it draws exactly A's edges, the drawing fits both "
             "solids; if it draws different ones, the drawing fits A only."),
            ("Name what was supplied",
             "Where both readings fit, state what the drawing does not contain, which face "
             "is in front, and so what a viewer who saw one reading at once had supplied."),
        ],
        "worked": {
            "title": "A wire cube and a solid one",
            "intro": [
                "Take a cube drawn with its back square offset by half an edge, first as "
                "wire, then as a solid whose hidden edges are left out. You want the number "
                "of readings each drawing fits.",
            ],
            "lines": [
                "wire cube, reading A:  4 + 4 + 4 = 12 edges",
                "reading B:  front and back squares exchanged",
                "B projected:  the same 12 segments as A",
                "readings the wire drawing fits:  2",
                "solid cube:  12 − 3 = 9 edges drawn",
                "solid, reading B:  a different 9, so 1 reading",
            ],
            "after": [
                "Four edges in the front square, four in the back, four joining them: the "
                "wire drawing is the same whichever square is in front, so the front was "
                "never in it. The solid drawing hides three edges, which three depends on "
                "the reading, and so it decides.",
            ],
        },
        "quiz_title": "The step back",
        "quiz": [
            {"q": "On the Preface's reading, what does the reduction suspend?",
             "a": ["Our complicity with the world, so that our ties to it can be seen",
                   "Our belief that the world exists, until doubt has proved it",
                   "Our bodies, so that only the mind remains",
                   "Perception, in favour of pure thought"],
             "c": 0,
             "why": "The text says the reduction refuses the world our complicity, puts it "
                    "out of play, and does so not because the certainties of common sense "
                    "are rejected but because they go unnoticed. Holding the world in doubt until "
                    "it is proved is Descartes's procedure, not this one. The body is not set "
                    "aside, and the step brings perception into view rather than leaving it."},
            {"q": "Why, according to the Preface, can the reduction never be completed?",
             "a": ["Because we are in the world, and our reflection takes place in the flow "
                   "of time it is trying to grasp",
                   "Because Husserl died before finishing it",
                   "Because the world may not exist",
                   "Because doubt, once begun, has no end"],
             "c": 0,
             "why": "If we were absolute mind there would be no problem; since we are in the "
                    "world and in time, no thought embraces all our thought. Husserl's death "
                    "is not the reason the text gives. The reduction does not raise the "
                    "question of the world's existence, and it is not a doubt."},
            {"q": "In the cube preset, a wire cube is drawn with its back square offset by "
                  "half an edge. How many solids does the drawing fit, on the lab's model?",
             "a": ["Two, and both draw the identical 12 edges",
                   "One, because one square is drawn in front",
                   "Two, but they draw different edges",
                   "None, because a flat drawing fits no solid"],
             "c": 0,
             "why": "Reading B, the mirror image with front and back exchanged, projects "
                    "onto exactly A's 12 segments, so the drawing fits both. Neither square "
                    "is drawn in front; that is what the viewer supplies. If the edges "
                    "differed it would fit one, and the drawing plainly fits a cube."},
            {"q": "The solid preset draws 9 edges and the lab prints 1 reading. Why only one?",
             "a": ["Reading B would hide three other edges and draw a different 9",
                   "A solid cube has only 9 edges",
                   "Solid things cannot be reversed in thought",
                   "The offset is too small to show depth"],
             "c": 0,
             "why": "Which three edges are hidden depends on which face is in front, so the "
                    "two readings draw different drawings and only A's matches. A cube has 12 "
                    "edges whatever it is made of. Nothing stops you imagining the reversal; "
                    "the drawing just fails to fit it. The offset is the same in all three "
                    "presets."},
        ],
        "mistakes": [
            ("Thinking the reduction doubts the world, as Descartes doubted",
             "Descartes withholds assent from whatever can be doubted, the world included, "
             "to find a certain ground. The Preface's reduction withdraws no belief: it "
             "suspends our complicity, and the certainties of common sense are, it says, "
             "&ldquo;the constant theme of philosophy&rdquo;. The lab shows the difference "
             "in small. Nothing about the drawing is doubted, and its 12 edges are exact; "
             "what shows is that which square is in front was never in it."),
            ("Thinking the reduction can be finished",
             "That would need a consciousness before which the world is spread out and "
             "completely transparent, which is the reading of Husserl the Preface sets "
             "aside. Because we reflect from inside the world and inside time, the "
             "reduction's chief lesson is that it cannot be complete, and the philosopher "
             "is a perpetual beginner."),
            ("Taking the reversible drawing for proof that perception deceives",
             "Neither reading of the wire cube is wrong: both fit the drawing exactly, and "
             "the lab prints 2. What the flip shows is not an error but a contribution, a "
             "setting habit supplied without notice. The book's own reversible figure, in "
             "Part Two, Chapter 2, is used the same way, to ask what organises a field, not "
             "to catch the eye out."),
        ],
        "standard": (
            "Finish when you can show that one drawing fits two solids and say what it leaves out.",
            "Given a line drawing of a wire or solid box, find the readings it fits by "
            "comparing each reading's edges with its mirror image's, and state what the "
            "drawing does not decide, and so what a viewer who saw one reading supplied."
        ),
        "note": (
            "The lab counts readings as solids, so it prints 2 for the wire cube; the book's "
            "own figure has a third, flat reading the lab cannot represent. The cube is the "
            "lesson's illustration, not the Preface's. And the reading of the reduction "
            "here is Merleau-Ponty's, drawn from Fink and from manuscripts most readers had "
            "not seen; how far it is Husserl's own is a dispute this lesson does not settle."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Smith p. xvi (opening passage: "But it is clear that the essence is
    # here not the end ... particularizations"; from the Dasein to the Wesen;
    # the Vienna Circle; logical positivism the antithesis); p. vii (the
    # study of essences; puts essences back into existence); p. xvii (the
    # fisherman's net; Jean Wahl; the separated essences are those of
    # language); p. xviii (not what I think, but what I live through);
    # p. xix (bases the possible on the real).
    {
        "slug": "essences-and-existence",
        "title": "Essences and Existence",
        "module": "Preface",
        "one_line": "Phenomenology seeks essences, but as a means of bringing our involvement in the world into view, not as the place where it stops.",
        "summary": (
            "Every reduction, Husserl says, is eidetic: to scrutinise perception we must "
            "pass from the fact of our existence to its nature. The Preface insists that "
            "the essence is a means and not the end. Compute the invariant core of a set "
            "of variations of a tone, a table and a melody, and find that what a melody "
            "keeps through transposition is a relation, not a part."
        ),
        "key": [
            "every reduction is also eidetic",
            "essence: a means, not the end",
            "core = what every variant keeps",
            "a variant lacking the core leaves the kind",
            "melody: the intervals stay, notes move",
        ],
        "key_label": "Essences in five lines",
        "concepts_intro": (
            "The Preface's first sentence says phenomenology is the study of essences, "
            "and its next says phenomenology puts essences back into existence. This "
            "section shows how both can be true."
        ),
        "concepts": [
            ("Essence",
             "What a thing must have to be the kind of thing it is: the nature of "
             "perception, of consciousness, of the world, as against the fact that this "
             "perception or this world exists. Husserl's word is <em>Wesen</em>; Greek "
             "<em>eidos</em> gives the adjective eidetic."),
            ("Free variation",
             "Husserl's way to an essence: take an example, vary it in imagination in "
             "every way you can, and keep what cannot be varied without the example "
             "ceasing to be of its kind. The Preface names the eidetic step but not this "
             "procedure; the lab is the lesson's illustration of it."),
            ("Facticity",
             "The plain fact that we exist, and that there is a world, before any account "
             "of either. The Preface's claim is that essences serve to bring this fact into "
             "view, and that it is what has to be understood."),
        ],
        "read_title": "The passage first, then the section on essences line by line",
        "read_intro": (
            "The passage is the section's pivot, set right after Husserl's claim that every "
            "reduction is eidetic. The lesson reads it phrase by phrase, then follows the "
            "section through the Vienna Circle and Jean Wahl to the world as lived."
        ),
        "body": [
            ("p", "<strong>Preface, p. xvi.</strong> &ldquo;But it is clear that the essence "
                  "is here not the end, but a means, that our effective involvement in the "
                  "world is precisely what has to be understood and made amenable to "
                  "conceptualization, for it is what polarizes all our conceptual "
                  "particularizations.&rdquo; The sentence is on page xvi of Smith's "
                  "translation. Read the section, from page xvi to the end of its paragraph "
                  "on page xix, in your own copy before going on."),
            ("p", "The Preface's first page had said two things that seemed to pull apart: "
                  "&ldquo;Phenomenology is the study of essences&rdquo;, and &ldquo;But "
                  "phenomenology is also a philosophy which puts essences back into "
                  "existence&rdquo;. The section on essences is where the two are joined. It "
                  "opens with a misunderstanding like the one about the reduction, and with "
                  "Husserl's thesis that every reduction, as well as being transcendental, is "
                  "necessarily eidetic. To scrutinise our perception of the world we must stop "
                  "simply living in it, draw back from our commitment so that it appears as a "
                  "spectacle, and pass from the fact of our existence to its nature, "
                  "&ldquo;from the Dasein to the Wesen&rdquo;: from being there to what being "
                  "there is."),
            ("p", "Now the passage. &ldquo;The essence is here not the end, but a "
                  "means&rdquo;: the eidetic step is taken for the sake of something else. "
                  "What that is comes next: &ldquo;our effective involvement in the "
                  "world&rdquo;, which is what has to be understood. And the reason is in the "
                  "last clause. It is our involvement that &ldquo;polarizes&rdquo; our "
                  "concepts, as a magnet lines up filings: every particular concept we form "
                  "takes its direction from it. The Preface adds why the detour is needed at "
                  "all. Our existence is held too tightly in the world to know itself at the "
                  "moment it is involved, and it needs the field of ideality, the distance of "
                  "a concept, to become acquainted with its own facticity and prevail over it."),
            ("p", "Then a story with an opponent in it. The Vienna Circle was a group of "
                  "philosophers and scientists who met in Vienna in the 1920s and 1930s, "
                  "Moritz Schlick, Rudolf Carnap and Otto Neurath among them, and who held "
                  "that a statement means something only if there is a way to check it. "
                  "Stated at its strength, their caution about a word like "
                  "<em>consciousness</em> runs like this: words carry old metaphysics with "
                  "them, and a philosopher who thinks he is looking straight at "
                  "consciousness may only be looking at the history of a word. The Preface "
                  "puts their view this way: we can enter into relations only with meanings, "
                  "and consciousness is a complex meaning that developed late, to be handled "
                  "with care and only after its earlier meanings have been made explicit."),
            ("p", "Its reply is flat: &ldquo;Logical positivism of this kind is the antithesis "
                  "of Husserl's thought.&rdquo; Whatever the history of the word, we have "
                  "direct access to what it designates, because we have the experience of "
                  "ourselves, of the consciousness we are, and it is by that experience that "
                  "every linguistic meaning is assessed. Then the image the section is "
                  "remembered for. &ldquo;Husserl's essences are destined to bring back all "
                  "the living relationships of experience, as the fisherman's net draws up "
                  "from the depths of the ocean quivering fish and seaweed.&rdquo; The net is "
                  "not the catch. You throw it to bring up what is alive."),
            ("p", "So the French philosopher Jean Wahl, the Preface says, was wrong to write "
                  "that &ldquo;Husserl separates essences from existence&rdquo;. Wahl, who "
                  "had written on Kierkegaard and on Hegel's unhappy consciousness and had "
                  "called for a philosophy turned towards the concrete, was making a serious "
                  "charge: that the eidetic method trades the living thing for its "
                  "definition. The answer is that &ldquo;The separated essences are those of "
                  "language.&rdquo; It is language that makes essences look separate, and "
                  "only apparently, because language itself still rests on a life of "
                  "consciousness before any predication."),
            ("def", ("The eidetic reduction (the Preface's reading)",
                     "The passage from a fact to its essence, taken as a means: the essence "
                     "is sought in order to bring to light the world as it is before we "
                     "fall back on ourselves, and is not itself the object of philosophy.")),
            ("p", "Near its end the section says what the essence of the world is not. "
                  "Sensationalism reduces the world to states of ourselves; transcendental "
                  "idealism reduces it to the correlate of our knowledge. The eidetic "
                  "reduction, on the contrary, is the resolve to bring the world to light as "
                  "it is before we fall back on ourselves. We must not wonder whether we "
                  "really perceive a world; we must say that the world is what we perceive. "
                  "And then the sentence that turns the section round: &ldquo;The world is "
                  "not what I think, but what I live through.&rdquo; The eidetic method, on "
                  "this account, is a positivism of a phenomenological kind, one which "
                  "&ldquo;bases the possible on the real&rdquo;."),
            ("p", "The lab runs free variation on three examples, all the lesson's own. The "
                  "<code>sound</code> preset takes a tone and varies it five ways, in pitch "
                  "(two pitches), loudness (soft and loud) and timbre (flute and violin), and "
                  "adds a sixth variant with no duration, marked as no longer a sound. The "
                  "lab prints the core as <code>some-duration</code>: everything else varied "
                  "among the five, and the sixth lacks exactly that. The <code>table</code> "
                  "preset varies a table in wood and steel, high and low, four legs and "
                  "three, and adds one with no top: the core is <code>top</code>."),
            ("p", "Notice how little the core says. Having some duration is true of every "
                  "tone and tells you nothing about the one you are hearing. That is the "
                  "Preface's point in miniature: the invariant is the net, and the tone with "
                  "its pitch and grain is the catch. The coding is the lesson's too. It "
                  "decided that a tone with no duration is no tone and that a table needs a "
                  "top; the lab only counts."),
            ("p", "The <code>melody</code> preset is the one that matters most. In 1890 the "
                  "Austrian philosopher Christian von Ehrenfels asked what stays the same "
                  "when a melody is transposed. Play its first three notes in C, as C, E and "
                  "G, then in D, as D, F sharp and A, then in B flat, as B flat, D and F. "
                  "Against the C version every note has changed, and anyone who knows the "
                  "tune hears the same tune. The lab's core is <code>major-third-up, "
                  "minor-third-up</code>: the steps between the notes, and no note at all. A "
                  "fourth variant plays the C notes backwards, G, E, C, marked as a different "
                  "melody: it has every note of the first and lacks the core. What a melody "
                  "keeps is a relation, and the Gestalt psychologists, whom the book draws on "
                  "throughout, took that lesson from Ehrenfels."),
            ("p", "An essence, then, is reached by going through the variants, and it is "
                  "worth having for what it brings back up. The next lesson, "
                  "“Intentionality and Rationality”, turns to the Preface's last themes: how "
                  "consciousness is directed at a world, and what it means to say the world "
                  "makes sense."),
        ],
        "lab": ("phenkit", {
            "mode": "variation",
            "view": "core",
            "preset": "sound",
            "presets": [
                {"id": "sound",
                 "label": "A tone varied five ways, and one with no duration (illustrative)",
                 "variants": "low soft flute, yes, pitch-220 soft flute some-duration; "
                             "high soft flute, yes, pitch-880 soft flute some-duration; "
                             "high loud flute, yes, pitch-880 loud flute some-duration; "
                             "high loud violin, yes, pitch-880 loud violin some-duration; "
                             "low loud violin, yes, pitch-220 loud violin some-duration; "
                             "no duration, no, pitch-220 loud violin",
                 "expect": {"vrCore": "some-duration", "vrBreak": "no duration lacks some-duration"}},
                {"id": "table",
                 "label": "A table in wood and steel, high and low, and one with no top (illustrative)",
                 "variants": "oak table, yes, wood low four-legs top; "
                             "steel table, yes, steel high four-legs top; "
                             "tripod table, yes, wood high three-legs top; "
                             "no top, no, wood high four-legs",
                 "expect": {"vrCore": "top", "vrBreak": "no top lacks top"}},
                {"id": "melody",
                 "label": "A melody's first three notes in C, D and B flat, and the C notes backwards (after Ehrenfels, 1890)",
                 "variants": "in C, yes, C E G major-third-up minor-third-up; "
                             "in D, yes, D F-sharp A major-third-up minor-third-up; "
                             "in B flat, yes, B-flat D F major-third-up minor-third-up; "
                             "C notes backwards, no, G E C minor-third-down major-third-down",
                 "expect": {"vrCore": "major-third-up, minor-third-up",
                            "vrBreak": "C notes backwards lacks major-third-up, minor-third-up"}},
            ],
            "panel_title": "Free variation",
            "panel_intro": (
                "This lab counts the lesson's coding: each variant's properties, and whether "
                "it is still of the kind, are the lesson's choices. The lab prints what "
                "every variant of the kind keeps, what varies, and what the others lack. "
                "Compare the sound and melody presets."
            ),
        }),
        "steps_title": "Finding an invariant core",
        "steps_intro": "Four steps, the same for any set of variations.",
        "steps": [
            ("Code each variant",
             "List each variant's properties as separate words, and mark whether it is "
             "still of the kind. Both are decisions about the example, not results."),
            ("Intersect the variants of the kind",
             "Keep the properties that every variant marked yes has. That set is the core."),
            ("List what varies",
             "Every property some yes variant has and another lacks varies, and so belongs "
             "to no essence of the kind."),
            ("Check the variants marked no",
             "For each, name the core properties it lacks. If it lacks none, either the "
             "coding is missing a property or the variant was wrongly marked."),
        ],
        "worked": {
            "title": "A tone in five variations",
            "intro": [
                "Take the sound preset: five tones at two pitches, soft or loud, on flute or "
                "violin, each of some duration, and a sixth with no duration. You want the "
                "core and what the sixth lacks.",
            ],
            "lines": [
                "pitch:  220 and 880 both occur, so it varies",
                "loudness:  soft and loud both occur, so it varies",
                "timbre:  flute and violin both occur, so it varies",
                "some duration:  in all 5 tones, so it is the core",
                "the sixth variant:  lacks some duration",
            ],
            "after": [
                "Pitch, loudness and timbre each take two values among the five, so none of "
                "them belongs to the core; having some duration is the one property every "
                "tone keeps. The core is exact, and as thin as a core usually is: it is the "
                "net, not the fish.",
            ],
        },
        "quiz_title": "The essence as a means",
        "quiz": [
            {"q": "Three cups are all coded as cups: glass with a handle that holds liquid, "
                  "clay with a handle that holds liquid, and clay without a handle that holds "
                  "liquid. What is the core?",
             "a": ["holds liquid", "clay, holds liquid", "handle, holds liquid", "none"],
             "c": 0,
             "why": "Only holding liquid is in all three. Clay is missing from the glass cup "
                    "and the handle from the third, so each varies. The core is not empty, "
                    "because one property is shared by every cup."},
            {"q": "In the melody preset, the tune is played in C, in D and in B flat. What "
                  "does the lab find stays?",
             "a": ["The intervals between the notes",
                   "The note C",
                   "The first note",
                   "Nothing: every note changes"],
             "c": 0,
             "why": "Every version rises a major third and then a minor third. C is missing "
                    "from the D and B flat versions, the first note differs in each, and "
                    "although every note changes, the relation between them does not."},
            {"q": "What, according to the Preface, is the essence for?",
             "a": ["It is a means of understanding our involvement in the world",
                   "It is the end of the inquiry, where phenomenology stops",
                   "It is a word's meaning, to be handled with care",
                   "It is a fiction phenomenology has given up"],
             "c": 0,
             "why": "The passage says the essence is not the end but a means, and that our "
                    "involvement in the world is what has to be understood. Treating essences "
                    "as meanings of words is the Vienna Circle's view, which the Preface calls "
                    "the antithesis of Husserl's, and the Preface keeps essences, calling "
                    "every reduction eidetic."},
            {"q": "Jean Wahl wrote that Husserl separates essences from existence. What does "
                  "the Preface reply?",
             "a": ["Essences look separate only in language, which still rests on lived "
                   "experience",
                   "Wahl is right, and phenomenology accepts the separation",
                   "Essences exist in a realm of their own, apart from the world",
                   "There are no essences, so nothing is separated"],
             "c": 0,
             "why": "The text says the separated essences are those of language, and that "
                    "the separation is merely apparent because language rests on the life of "
                    "consciousness. The Preface says Wahl is wrong. A realm apart is the "
                    "separation it denies, and it does not deny that there are essences."},
        ],
        "mistakes": [
            ("Thinking phenomenology ends where the invariant is found",
             "The Preface's first sentence does say that phenomenology is the study of "
             "essences, and a reader who stops there takes the core to be the result. The "
             "section says the opposite: the essence is not the end but a means. The lab "
             "shows why in its own terms. The sound preset's core is "
             "<code>some-duration</code>, true of every tone and silent about the one you "
             "hear, and the melody's core is a pair of intervals, a relation that is "
             "found only by going through the melodies themselves."),
            ("Treating an essence as the meaning of a word",
             "That is the Vienna Circle's view as the Preface states it: we deal only with "
             "meanings, and consciousness is a late and complex one. The Preface replies "
             "that we have direct access to what the word designates, in the experience of "
             "ourselves, and that the separated essences are those of language."),
            ("Expecting the core to be a part of every variant",
             "A melody transposed from C to D shares no note with the original, and the lab "
             "still finds a core: the intervals. The C notes played backwards keep every "
             "note and lose the core. What stays through variation can be a relation "
             "between parts, and in the Gestalt examples the book draws on it usually is."),
        ],
        "standard": (
            "Finish when you can find a set's invariant core and say what it is for.",
            "Given a coded set of variants and which of them are still of the kind, compute "
            "the core, list what varies, name what each excluded variant lacks, and state "
            "how, on the Preface's account, the core serves to bring the concrete case "
            "into view."
        ),
        "note": (
            "Free variation is meant to run through every possibility in imagination, and a "
            "list of six variants does not; the lab's core is only as good as the lesson's "
            "coding of them, and a property nobody coded can never appear in it. The tone, "
            "the table and the melody are the lesson's examples, the melody after "
            "Ehrenfels; the Preface names the eidetic step but gives no example of it."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Smith p. xxii (opening passage: "To say that there exists rationality
    # ... a meaning emerges" and "The phenomenological world is not pure being
    # ... like gears"; absolute Spirit; impartial spectator; an act of
    # initiative); p. xvii (all consciousness is consciousness of something);
    # p. xx (intentionality of act, operative intentionality, desires and
    # landscape, furnishing the text); p. xxi (Marx: history's head and feet);
    # p. xxiii (true philosophy, relearning to look); p. xxiv (not a sign of
    # failure; Balzac, Proust, Valery, Cezanne).
    # "House seen from nowhere": Part One, introduction, p. 77.
    {
        "slug": "intentionality-and-rationality",
        "title": "Intentionality and Rationality",
        "module": "Preface",
        "one_line": "Consciousness is directed at a world it lives in before it judges, and the world makes sense because perspectives confirm one another, not because a view from nowhere checks them.",
        "summary": (
            "The Preface ends with intentionality, which it widens from the acts of "
            "judgement to an operative intentionality already at work in desire and in the "
            "landscape, and with a rationality that is the agreement of perspectives, "
            "guaranteed by no standpoint above them. Compute which faces of a cube several "
            "viewpoints see, which no view sees, and whether each viewer's report fits "
            "the direction they look from."
        ),
        "key": [
            "consciousness is of something",
            "act intentionality: judging, choosing",
            "operative: the unity lived before that",
            "rationality: views confirm each other",
            "no view from nowhere checks them",
            "face seen if the view points toward it",
        ],
        "key_label": "The Preface's last themes in six lines",
        "concepts_intro": (
            "The last pages of the Preface move fast, from intentionality through history "
            "to rationality. Three ideas hold them together."
        ),
        "concepts": [
            ("Intentionality",
             "Consciousness is always consciousness of something. The Preface says this is "
             "too often taken for phenomenology's great discovery, and that it can only be "
             "understood through the reduction."),
            ("Operative intentionality",
             "Husserl's <em>fungierende Intentionalität</em>: the directedness that makes the "
             "world and our life one before any judgement, at work in desires, evaluations "
             "and the landscape we see. Its counterpart is the intentionality of acts, "
             "which judges and takes positions."),
            ("Rationality",
             "On the Preface's account, the fact that perspectives blend, perceptions "
             "confirm one another and a meaning emerges. It is not set in a realm apart, "
             "and nothing outside the perspectives guarantees it."),
        ],
        "read_title": "The passage first, then the Preface's last pages line by line",
        "read_intro": (
            "The passage is the Preface's account of rationality, near its end. The lesson "
            "reads it, goes back to the pages on intentionality that prepare it, and "
            "follows the Preface to its last sentence."
        ),
        "body": [
            ("p", "<strong>Preface, p. xxii.</strong> &ldquo;To say that there exists "
                  "rationality is to say that perspectives blend, perceptions confirm each "
                  "other, a meaning emerges. &hellip; The phenomenological world is not pure "
                  "being, but the sense which is revealed where the paths of my various "
                  "experiences intersect, and also where my own and other people's intersect "
                  "and engage each other like gears.&rdquo; The two sentences are from page "
                  "xxii of Smith's translation. Read from the section on intentionality, "
                  "which begins on page xix, to the end of the Preface on page xxiv, in "
                  "your own copy before going on."),
            ("p", "Picture a cereal box on the table between you and someone sitting "
                  "opposite. You see the front, with its picture; they see the back, with "
                  "the list of ingredients; both of you see the top. Neither of you has "
                  "seen the box whole, and neither of you doubts that it is one box. If they "
                  "read out the ingredients, you do not check the claim against a view of "
                  "the box from nowhere. There is no such view to check it against. What you "
                  "have is your side, theirs, and the top you share, fitting together. That, "
                  "in a kitchen, is what the passage calls rationality."),
            ("p", "The Preface reaches it by way of intentionality, and it begins by "
                  "deflating the idea. Intentionality is too often cited as phenomenology's "
                  "main discovery, it says, when it can only be understood through the "
                  "reduction. &ldquo;All consciousness is consciousness of "
                  "something&rdquo;: there is nothing new in that. The idea came to Husserl "
                  "from his teacher Franz Brentano, who in 1874 had made directedness at an "
                  "object the mark of the mental, and the Preface points further back, to "
                  "Kant. In the Refutation of Idealism Kant showed that inner perception is "
                  "impossible without outer perception, so that the world is already "
                  "anticipated in the consciousness of my own unity."),
            ("p", "What is new, the Preface says, is that the world's unity is lived as "
                  "ready-made, already there, before knowledge posits it, sets it down as an "
                  "object, in a specific act. "
                  "It finds the first sign of this in Kant himself, in the <em>Critique of "
                  "Judgement</em>: in finding something beautiful I feel a harmony between "
                  "sensation and concept, and between myself and others, that is itself "
                  "without a concept. And from there Husserl draws the distinction the whole "
                  "book will use. There is the intentionality of acts, of our judgements and "
                  "the positions we deliberately take, the only kind the <em>Critique of Pure "
                  "Reason</em> discusses. And there is &ldquo;operative "
                  "intentionality&rdquo;, which makes the world and our life one before any "
                  "judgement, and shows itself in &ldquo;our desires, our evaluations and in "
                  "the landscape we see&rdquo;, more clearly than in knowledge, "
                  "&ldquo;furnishing the text which our knowledge tries to translate into "
                  "precise language&rdquo;."),
            ("def", ("Operative intentionality",
                     "The directedness at a world that is already at work before any act of "
                     "judgement, giving the world and our life their unity; knowledge "
                     "translates what it furnishes, and does not produce it.")),
            ("p", "The pages that follow widen the point to history, and here the Preface "
                  "makes a joke, borrowed and then improved. It is true, as "
                  "Marx says, that history does not walk on its head, and also true that "
                  "&ldquo;it does not think with its feet&rdquo;; it is neither its head nor "
                  "its feet we should worry about, the Preface says, but its body. Economic "
                  "and psychological explanations of a doctrine are all true, since a "
                  "thinker thinks only from what he is, and every view of an event or a "
                  "doctrine is true provided it is not isolated: followed deep enough, each "
                  "reaches one core of existential meaning. That is the passage's idea before it is "
                  "stated: many views, one sense, found where they cross."),
            ("p", "Now the passage. Rationality is &ldquo;precisely proportioned&rdquo;, the "
                  "sentence before it says, to the experiences in which it is disclosed: "
                  "there is exactly as much of it as there is agreement among them. "
                  "&ldquo;Perspectives blend, perceptions confirm each other, a meaning "
                  "emerges&rdquo;: three verbs, none of them a verdict from outside. Then the "
                  "refusal, in the sentence the passage leaves out. Rationality is not to be "
                  "set in a realm apart, in absolute Spirit, as Hegel would have it, or in a "
                  "world in the realist sense, a world in itself behind every view. The sense "
                  "is &ldquo;where the paths of my various experiences intersect&rdquo;, "
                  "and where mine and other people's do, meshing &ldquo;like gears&rdquo;."),
            ("p", "That refusal is the Preface's target throughout, and it deserves its "
                  "strongest statement. If every view is only a view, the idealist argues, "
                  "nothing among the views can tell a true one from a false one; something "
                  "that is not a view, a consciousness that holds them all together, must "
                  "be the condition of their agreeing. For Kant every representation must be "
                  "able to be accompanied by one <em>I think</em>, and earlier pages of the "
                  "Preface describe the idealism in which we are all one light and Peter's "
                  "and Paul's perspectives blend because they were one perspective all "
                  "along. The Preface's answer is that the philosopher, the meditating ego, "
                  "the &ldquo;impartial spectator&rdquo;, does not rediscover a rationality "
                  "already given. It establishes it, &ldquo;by an act of initiative which "
                  "has no guarantee in being&rdquo;, and whose only justification, the "
                  "Preface adds, is the power it gives us to take our own history upon "
                  "ourselves."),
            ("p", "The lab puts the passage's views on a cube. The <code>three</code> preset "
                  "has three viewers. One looks from front, right and above, along the "
                  "direction <code>1 2 2</code>, whose length is 3; the lab's projection "
                  "draws the front at `2/3` of its true area, the right side at `1/3` and the "
                  "top at `2/3`. One looks from back, left and above, along <code>-2 1 "
                  "-2</code>, and the projection draws the back at `2/3`, the left at `2/3` "
                  "and the top at `1/3`. One looks straight at the front and it is drawn "
                  "whole. Between them they see 5 of the 6 faces, and the cover tile adds "
                  "that the two oblique viewers already see all five between them: the third, "
                  "looking straight at the front, adds no face, only a second sight of one. "
                  "The top is seen by two viewers, projected differently, and is one top. "
                  "Nobody sees the bottom, and nobody needs to, to see a cube."),
            ("p", "The <code>two</code> preset has one viewer in front and one behind: 1 face "
                  "each, 2 of 6 between them, and nothing seen in common. The "
                  "<code>conflict</code> preset keeps the three viewers and has the first "
                  "report seeing front, right and below. The lab's consistency tile prints "
                  "<code>no: front-right-above (below)</code>: a viewer looking down on the "
                  "cube cannot see its underside. Notice how the lab knows. It checks each "
                  "report against a cube it holds complete, from outside every view, which "
                  "is exactly the standpoint the Preface denies us when it says, in the "
                  "section on the reduction, that there is no thought which embraces all "
                  "our thought. In perception "
                  "the report would be caught the other way, by failing to mesh with the "
                  "other views."),
            ("p", "The Preface ends by refusing to call any of this unfinished in the bad "
                  "sense. Rationality is not a problem with an unknown behind it; the world "
                  "and reason may be called mysterious, but that mystery defines them and no "
                  "solution dispels it. &ldquo;True philosophy consists in relearning to look "
                  "at the world&rdquo;, and the unfinished character of phenomenology is "
                  "&ldquo;not to be taken as a sign of failure&rdquo;. Its last comparison is "
                  "with novelists, a poet and a painter: phenomenology, it says, &ldquo;is as "
                  "painstaking as the works of Balzac, Proust, Valéry or Cézanne&rdquo;, by "
                  "the same attentiveness and wonder, and the same will to seize the meaning "
                  "of the world as it comes into being."),
            ("p", "The Preface has said what the method is. The book now turns to what stands "
                  "in its way: Classical Prejudices reads the Introduction, where "
                  "Merleau-Ponty takes apart the two theories of perception he calls "
                  "empiricism and intellectualism, beginning with the idea of a pure "
                  "sensation."),
        ],
        "lab": ("phenkit", {
            "mode": "perspective",
            "view": "faces",
            "model": "parallel projection",
            "preset": "three",
            "presets": [
                {"id": "three", "label": "Three views of a cube: front-right-above, back-left-above and front",
                 "object": "cube",
                 "views": "1 2 2, front-right-above; -2 1 -2, back-left-above; front",
                 "expect": {"peVisible": "front-right-above: front 2/3, right 1/3, above 2/3; "
                                         "back-left-above: back 2/3, left 2/3, above 1/3; front: front 1",
                            "peUnion": "5 of 6", "peMax": "3", "peConsistent": "—"}},
                {"id": "two", "label": "One view from the front and one from the back",
                 "object": "cube",
                 "views": "front; back",
                 "expect": {"peUnion": "2 of 6", "peMax": "1", "peCover": "front, back (2 views)"}},
                {"id": "conflict", "label": "The three views, with the first reporting front, right and below",
                 "object": "cube",
                 "views": "1 2 2, front-right-above, front right below; -2 1 -2, back-left-above; front",
                 "expect": {"peUnion": "5 of 6", "peConsistent": "no: front-right-above (below)"}},
            ],
            "panel_title": "Faces and views",
            "panel_intro": (
                "This lab computes parallel projection: a face is seen from a direction when "
                "the direction points towards it, foreshortened by the cosine between them. "
                "It prints what each view sees, what all of them see between them, and "
                "whether each report fits its direction."
            ),
        }),
        "steps_title": "Computing what several views see",
        "steps_intro": "Five steps, for any set of whole-number view directions.",
        "steps": [
            ("Find each direction's length",
             "Square the three components, add them and take the root. The kit accepts only "
             "directions whose length is a whole number, such as 1 2 2, of length 3."),
            ("List the faces each view sees",
             "A view sees the right face if its first component is positive and the left if "
             "negative, the top or bottom by the second, and the front or back by the third."),
            ("Foreshorten",
             "In the projection a face seen at an angle is drawn at its component over the "
             "direction's length, as a fraction of its true area: from 1 2 2 the right face "
             "is drawn at 1/3."),
            ("Take the union",
             "Collect every face some view sees, and name the faces no view sees."),
            ("Check each report",
             "Compare what each viewer says they see with the faces their direction allows; "
             "a face the direction cannot see makes the report inconsistent."),
        ],
        "worked": {
            "title": "Three viewers and one cube",
            "intro": [
                "Take the three preset: views along 1 2 2, along −2 1 −2, and straight at "
                "the front. You want what each sees, at what fraction of its true area the "
                "projection draws it, and what they see together.",
            ],
            "lines": [
                "first view:  1 + 4 + 4 = 9, so its length is 3",
                "first view sees:  right 1/3, above 2/3, front 2/3",
                "second view:  4 + 1 + 4 = 9, length 3",
                "second view sees:  left 2/3, above 1/3, back 2/3",
                "third view sees:  front 1",
                "together:  5 of 6 faces; no view sees below",
            ],
            "after": [
                "The top is seen twice, projected at `2/3` and at `1/3`, and is one top; the "
                "front is seen twice, projected at `2/3` and whole. Nobody sees the bottom, and the cube is no "
                "less a cube for that. No view here is the true one. Each is partial, and "
                "they fit.",
            ],
        },
        "quiz_title": "Perspectives that confirm each other",
        "quiz": [
            {"q": "Two viewers look at a cube, one along 1 2 2 and one straight at the "
                  "front. How many faces do they see between them?",
             "a": ["3 of 6", "4 of 6", "2 of 6", "6 of 6"],
             "c": 0,
             "why": "The view along 1 2 2 sees right, above and front; the front view sees "
                    "only the front, which is already counted. That makes 3. Four would need a "
                    "face neither direction points towards, two leaves out the right side or "
                    "the top, and no pair of these views sees the back or the bottom."},
            {"q": "In the lab's projection along 1 2 2, at what fraction of its true area is "
                  "the top drawn?",
             "a": ["2/3", "1/3", "1", "2/9"],
             "c": 0,
             "why": "The length of 1 2 2 is 3, and the top's component is 2, so the top "
                    "is drawn at `2/3`. `1/3` is the right side's figure, 1 would mean looking "
                    "straight down, and `2/9` divides by the squared length instead of the "
                    "length."},
            {"q": "Which of these is operative intentionality, in the Preface's sense, rather "
                  "than the intentionality of an act?",
             "a": ["The unity of the landscape you see, before you judge anything about it",
                   "A judgement that the wall in front of you is white",
                   "A decision to take a position on a disputed question",
                   "The application of the understanding's categories to a manifold"],
             "c": 0,
             "why": "The Preface says operative intentionality shows itself in desires, "
                    "evaluations and the landscape we see, before any judgement. A judgement "
                    "and a deliberate position-taking are acts. The categories applied to a "
                    "manifold belong to the Critique of Pure Reason, which the Preface says "
                    "discusses only the intentionality of acts."},
            {"q": "On the Preface's account, what is it for there to be rationality?",
             "a": ["That perspectives blend, perceptions confirm each other and a meaning "
                   "emerges",
                   "That a viewpoint above every viewpoint certifies which views are true",
                   "That absolute Spirit realises itself in the world",
                   "That a world in itself, behind every view, matches our ideas"],
             "c": 0,
             "why": "That is the passage's own definition. The other three each place "
                    "rationality in a realm apart, outside the perspectives: the spectator "
                    "above them, absolute Spirit and the realist's world in itself are "
                    "exactly what the Preface says rationality should not be transposed into."},
        ],
        "mistakes": [
            ("Thinking rationality needs a viewpoint above all viewpoints to check them",
             "At its strongest this is the idealist's argument: views alone cannot sort true "
             "from false, so a consciousness outside them must be the condition of their "
             "agreeing. The Preface denies there is such a standpoint to occupy; the "
             "meditating ego and the impartial spectator establish rationality rather than "
             "find it. The lab shows the difference against itself. In the three preset the "
             "views confirm one another, the top projected at `2/3` and at `1/3` and still "
             "one top. The conflict preset's verdict, <code>no: front-right-above "
             "(below)</code>, is reached by checking against a complete cube the lab holds "
             "from nowhere, which is the one thing a perceiver never has."),
            ("Taking operative intentionality for a quiet kind of judgement",
             "Operative intentionality is not a judgement made quickly or without noticing. "
             "It comes before judgement and furnishes the text that judgement translates: it "
             "is in desire, evaluation and the landscape seen, and the Preface says it shows "
             "there more clearly than in objective knowledge."),
            ("Reading the unfinished as a failure",
             "The Preface expects phenomenology to stay unfinished, because it is itself in "
             "history and must question itself as it questions everything else. It says "
             "that this is not a sign of failure but was inevitable, because its task was "
             "to reveal the mystery of the world and of reason, and it compares the work to "
             "the novelist's or the painter's: to seize the world's meaning as it comes into "
             "being."),
        ],
        "standard": (
            "Finish when you can compute what several views see and say what makes them agree.",
            "Given whole-number view directions on a cube, compute the faces each sees and "
            "their foreshortening, the faces seen by some view and by none, and whether "
            "each report fits its direction, and state where, on the Preface's account, "
            "the agreement of the views comes from."
        ),
        "note": (
            "The lab can only check a report against a complete cube it holds in advance, "
            "the view from nowhere that the Preface says no perceiver occupies; it computes "
            "geometry, not the agreement of perspectives the Preface calls rationality. The "
            "cube and its viewers are the lesson's illustration. The book takes up the "
            "house seen from nowhere at the start of Part One, in Experience and Objective "
            "Thought."
        ),
    },
]
