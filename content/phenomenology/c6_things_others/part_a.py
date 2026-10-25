"""Things, the World and Others, lessons 1-4 -- Part Two, Chapter 3, The Thing and the Natural World.

Every quotation is copied from Colin Smith's translation, Routledge Classics
pagination (Chapter 3 runs pp. 348-402); the comment beside each lesson gives
its pages. Smith's ligatures are printed as plain letters, a word split by a
line-break hyphen is joined, footnote numerals are left out, and Smith's single
quote marks inside a quotation are printed as &lsquo;...&rsquo;. Nothing else
is changed.

The chapter has four parts, which Smith marks only by a blank line: the
perceptual constancies (p. 348, from the chapter's first line, to p. 370), the
thing as an inter-sensory entity (p. 370, "We are now in a position to approach
the analysis of the thing ...", to p. 381), the natural world (p. 381, "What
needs to be elucidated, then, is this primary comprehension of the world", to
p. 389) and hallucination (p. 389, "Hallucination causes the real to
disintegrate ...", to p. 402). The constancies take two lessons, size and shape
(pp. 348-354) and colour and lighting (pp. 354-370); the other three parts take
one each, the last of them in part_b.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Smith p. 351 (opening passage: "For science and objective thought ...
    # at ten yards", cut with an ellipsis; "the constant product of the
    # distance multiplied by the apparent size" is from the cut sentence);
    # p. 348 (the chapter's first question; perceptual constants); pp. 348-9
    # (the psychologist's conventional standard; "how can there be
    # objectivity?"); pp. 349-51 (the size as the law of the appearances, the
    # fountain-pen held near the eyes, the oblique square, Kant's positing of
    # a world: all in the voice of the view the chapter then questions);
    # p. 351 (the table; the hundred yards); p. 352 (the optimum distance,
    # the picture in the gallery, the living body too near and too far, "a
    # tension which fluctuates round a norm", the oblique position felt as a
    # lack of balance); p. 353 note 2 (Koffka's sphere, the horizon moon);
    # p. 354 ("I am not the spectator, I am involved"; Kant's Dialectic and
    # Analytic). Helmholtz and Brunswik are not named in the chapter.
    {
        "slug": "size-and-shape-constancy",
        "title": "Size and Shape Constancy",
        "module": "Part Two · 3 · The Thing · Constancies",
        "one_line": "A thing keeps its size and shape across distances and angles, and the chapter argues that this is neither a convention nor an inference but the body's hold on the thing at its best distance.",
        "summary": (
            "The chapter opens by asking on what basis we take a size or a shape to be the "
            "object's own. Compute what the retinal-image account and an unconscious "
            "inference each predict for a person across a room, and how far a reported size "
            "lies between them on Brunswik's ratio. Then read the chapter's answer: the real "
            "size is the one the thing shows at the distance from which it is best seen."
        ),
        "key": [
            "retinal = size × standard / distance",
            "inferred = retinal × distance / standard",
            "ratio = (report − retinal) / (size − retinal)",
            "the real size: the thing at its best distance",
            "distance: a tension round a norm",
        ],
        "key_label": "Size constancy in five lines",
        "concepts_intro": (
            "The chapter's first pages set two accounts of constancy against each other and "
            "then reject both. Three ideas are needed to follow them."
        ),
        "concepts": [
            ("Perceptual constancy",
             "A thing keeps its size, shape and colour through changes of distance, angle "
             "and light that change the stimulus it sends the eye. A person crossing a room "
             "does not appear to shrink. The chapter takes these constants as its way into "
             "the question of what it is for something to be real."),
            ("The two classical predictions",
             "The retinal-image account says perceived size follows the angle the thing "
             "subtends, so a person four times as far off should look a quarter of the size. "
             "The inference account says the mind corrects the angle by the distance it "
             "takes the thing to be at, so the person should be judged at full size."),
            ("The optimum distance",
             "The chapter's own answer. For each thing there is a distance and an angle from "
             "which it shows most of itself, and the other appearances are taken as steps "
             "towards that one. The real size is the size the thing has there, not a result "
             "computed from the others."),
        ],
        "read_title": "The passage first, then the chapter's opening pages line by line",
        "read_intro": (
            "The passage is the chapter's sharpest statement of the view it rejects, with "
            "its reply in the next sentence. The lesson goes back to the chapter's first "
            "page, follows the two accounts it examines, and then reads the reply."
        ),
        "body": [
            ("p", "<strong>Part Two, Chapter 3, p. 351.</strong> &ldquo;For science and "
                  "objective thought, an apparently small object seen a hundred yards away is "
                  "indistinguishable from the same object seen ten yards away at a greater "
                  "angle &hellip; But for me the perceiver, the object a hundred yards away is "
                  "not real and present in the sense in which it is at ten yards&rdquo;. The "
                  "two sentences are from page 351 of Colin Smith's translation, in the chapter "
                  "he titles &ldquo;The Thing and the Natural World&rdquo;. Read the chapter "
                  "from its first page, 348, to the paragraph on page 354 that turns to colour, "
                  "in your own copy before going on; the lesson goes back through it a phrase "
                  "at a time."),
            ("p", "Someone you know walks away from you down a long corridor, turns at the end "
                  "and waves. The angle their body fills at your eye has fallen to a fraction "
                  "of what it was when they stood beside you, and they have not, for you, "
                  "become a small person. That is a perceptual constancy, and the chapter "
                  "begins with it. A thing, it says on page 348, has stable characteristics "
                  "even if they do not entirely define it, and it proposes to approach the "
                  "phenomenon of reality by studying these constants. The first is size and "
                  "shape: we do not attribute the changing appearances to the thing, but to "
                  "our relations with it. On what basis, the chapter asks, do we judge that a "
                  "size or a shape is the object's own?"),
            ("p", "The first answer is given in the voice of &ldquo;the psychologist&rdquo;, "
                  "meaning the experimental psychology of perception the book argues with "
                  "throughout. Every size and shape varies with the perspective, the "
                  "psychologist says, and it is merely conventional to count as true the size "
                  "a thing has within reach and the shape it has face on; our body makes these "
                  "positions typical, so we can always recognise them and use them as a "
                  "standard. The chapter's objection is that this takes for granted what had "
                  "to be explained: a range of determinate sizes from which one is chosen. The "
                  "question is how any determinate size, true or apparent, comes to be given "
                  "at all, or, as page 349 puts it, &ldquo;how can there be "
                  "objectivity?&rdquo;"),
            ("p", "The second answer looks at first, the chapter says, like a way round the "
                  "question, and it gives the answer two pages in its own words before "
                  "questioning it. The true size is not a quality found in any one "
                  "perception; it is the law that governs how the appearance varies with the "
                  "distance. Hold a fountain-pen up to your eye so that it hides the whole "
                  "scene, and it stays small, because the pen that hides everything is also a "
                  "pen seen close to. Followed out, this leads with Kant to the positing of a "
                  "world as a strictly interrelated system. Immanuel Kant, the Königsberg "
                  "philosopher whose <em>Critique of Pure Reason</em> (1781) made the mind's "
                  "own forms the conditions of any possible experience, is where the view "
                  "leads. The passage states what the object then is for size, for science "
                  "and objective thought: &ldquo;the constant product of the distance "
                  "multiplied by the apparent size&rdquo;."),
            ("p", "That product is something the lab can compute. Description, Not Explanation "
                  "computed one angular size, a size over a distance; this lab computes two "
                  "predictions from one. The <code>far</code> preset is a person 170 cm tall "
                  "at 8 m, with a standard viewing distance of 2 m; the figures are "
                  "illustrative. The retinal-image account, which is the constancy hypothesis "
                  "of Classical Prejudices applied to size, takes the angle as the datum, and "
                  "the lab states it as the height a person at the standard 2 m would need to "
                  "subtend the same angle, which the lesson calls the retinal-equivalent size: "
                  "`170 × 2/8 = 85/2` cm, the tile "
                  "<strong>retinal-image prediction</strong>. On that account the person should "
                  "look a quarter of their height. The inference account multiplies back by "
                  "the distance: `(85/2) × 8/2 = 170` cm, the tile for the size an "
                  "<strong>inference</strong> would conclude. That is the view usually credited to Hermann von Helmholtz, "
                  "the German physicist and physiologist whose <em>Treatise on Physiological "
                  "Optics</em> (1856&ndash;67) called it unconscious inference. The chapter "
                  "does not name him; the product it states for science and objective "
                  "thought is the same computation."),
            ("p", "The inference is only as good as the distance it assumes. In the "
                  "<code>misjudged</code> preset the person is still at 8 m, but the distance "
                  "is taken to be 4 m: the lab gives `(85/2) × 4/2 = 85` cm. Done right, the "
                  "inference predicts perfect constancy; done wrong, it predicts a definite "
                  "error. Either way it predicts a figure, and that is the point the chapter "
                  "presses next."),
            ("p", "Kant is right, the chapter grants on page 351, that perception is by its "
                  "nature directed towards the object. What his account cannot make sense of "
                  "is appearance as appearance: if the size is a law, it is treated as a "
                  "variable already measured, when the question was how it becomes determinate "
                  "at all, and the subject thinks his perception instead of perceiving it. Then "
                  "the reply. The table in my room is not, for me, a rule governing a parade of "
                  "appearances. It is because I perceive the table with its definite size that "
                  "I expect each change of distance to bring a change of appearance, and not "
                  "the reverse. That is the passage's second sentence: the object at a hundred "
                  "yards is not real and present in the way it is at ten."),
            ("p", "Why not? Because, page 352 says, for each object, as for each picture in "
                  "an art gallery, &ldquo;there is an optimum distance from which it requires "
                  "to be seen&rdquo;, and a direction from which it shows most of itself. "
                  "Nearer or farther, the perception is blurred by excess or by lack. A living "
                  "body seen too close, a patch of skin under a magnifying glass, is a mass of "
                  "matter as strange as a lunar landscape; seen too far, it is a puppet. The "
                  "living body appears when its detail is neither too visible nor too little, "
                  "and that moment also fixes its real size and shape. The distance from me to "
                  "the thing, the chapter concludes, is not a size that grows and shrinks but "
                  "&ldquo;a tension which fluctuates round a norm&rdquo;."),
            ("def", ("Brunswik's ratio",
                     "A measure of how far a reported size lies between the two predictions: "
                     "(reported − retinal-equivalent) / (size − retinal-equivalent). It is 0 "
                     "when the report matches the retinal-image prediction and 1 when it "
                     "matches perfect constancy. It is named after the psychologist Egon "
                     "Brunswik, who proposed it around 1930; the book does not use it, and it "
                     "is the lesson's addition.")),
            ("p", "The <code>far</code> preset also carries a reported size, 160 cm, and it is "
                  "illustrative, not a measurement from the book, which gives none. The lab's "
                  "third tile places it: `(160 − 85/2) / (170 − 85/2) = 47/51`, about 92 per "
                  "cent, the tile <strong>Brunswik ratio</strong>. The <code>none</code> preset "
                  "reports 85/2 cm and gets 0; the <code>full</code> preset reports 170 cm and "
                  "gets 1. A figure strictly between 0 and 1 is a report that neither model "
                  "predicts. The ratio only says where a report lies between two predictions; "
                  "it says nothing about what the person across the room looks like, which is "
                  "the chapter's subject and not the lab's."),
            ("p", "Shape is treated the same way. For the psychologist a square seen at an "
                  "angle is a diamond-shaped appearance referred to its frontal form; on the "
                  "law view the two appearances are equated in advance by a system of "
                  "relations. The lesson's own example is a coin tilted so that the cosine of the tilt is 3/5, "
                  "which projects as an ellipse with axes 1 and 3/5. The chapter's reply on page "
                  "352 is that an oblique position is not measured by the angle the object "
                  "makes with the plane of my face but felt as a lack of balance, an unequal "
                  "spread of its pull on me. When I turn a thing in my fingers to see it better, "
                  "each attitude of my body is, at once, the power of obtaining a certain view. "
                  "I know how appearances depend on my position not by a formula, but because I "
                  "have a body and am at grips with the world."),
            ("p", "A footnote on page 353 links this to the moon of the Preface lessons. Kurt "
                  "Koffka, one of the founders of Gestalt psychology, reported that constancy "
                  "is far more perfect in the horizontal than in the vertical plane, and the "
                  "chapter calls the huge horizon moon a particular case of the same law; for "
                  "apes, who move up trees as easily as we move along the ground, vertical "
                  "constancy is faultless. Constancy, the note begins by saying, is not an "
                  "intellectual function but an existential one, tied to the way a subject "
                  "takes up its place in the world."),
            ("p", "So the chapter keeps Kant's point and moves it. Any perception of a real "
                  "size does refer to a world and a system of experience, page 354 grants. But "
                  "that system is not spread before me as if I were God; it is lived from a "
                  "point of view: &ldquo;I am not the spectator, I am involved&rdquo;. The "
                  "world is an open and indefinite unity in which I have my place, as Kant "
                  "shows in the Transcendental Dialectic, the chapter says, and seems to "
                  "forget in the Analytic. Whether that reading of Kant is fair is a question "
                  "the chapter does not stop to argue."),
            ("p", "Size and shape, the chapter then says, teach us less about a thing than its "
                  "colour, hardness or weight. The next lesson, “Colour and Lighting”, reads "
                  "its pages on colour, and Gelb's experiment with a black disc in a hidden "
                  "beam of light."),
        ],
        "lab": ("phenkit", {
            "mode": "size",
            "view": "constancy",
            "model": "the retinal-image account and Helmholtz's unconscious inference",
            "preset": "far",
            "presets": [
                {"id": "far",
                 "label": "A person 170 cm tall at 8 m, standard distance 2 m, distance assumed correctly; reported 160 cm (illustrative)",
                 "size": 170, "distance": 800, "standard_distance": 200, "reported": 160, "unit": "cm",
                 "expect": {"szRetinal": "85/2 cm", "szInferred": "170 cm",
                            "szBrunswik": "47/51 ≈ 92.2%"}},
                {"id": "misjudged",
                 "label": "The same person, the distance assumed to be 4 m (illustrative)",
                 "size": 170, "distance": 800, "standard_distance": 200, "assumed": 400,
                 "reported": 160, "unit": "cm",
                 "expect": {"szRetinal": "85/2 cm", "szInferred": "85 cm"}},
                {"id": "none",
                 "label": "Reported 85/2 cm: the retinal-image prediction (illustrative)",
                 "size": 170, "distance": 800, "standard_distance": 200, "reported": "85/2", "unit": "cm",
                 "expect": {"szBrunswik": "0 = 0%"}},
                {"id": "full",
                 "label": "Reported 170 cm: perfect constancy (illustrative)",
                 "size": 170, "distance": 800, "standard_distance": 200, "reported": 170, "unit": "cm",
                 "expect": {"szBrunswik": "1 = 100%"}},
            ],
            "panel_title": "Two predictions of size, and a reported size between them",
            "panel_intro": (
                "This lab computes two classical models of size perception: the retinal-image "
                "account, which takes the angle as the datum, and Helmholtz's unconscious "
                "inference, which corrects it by an assumed distance. Brunswik's ratio, the "
                "lesson's addition, places a reported size between them. Every figure is a "
                "prediction or a measure, and none of them is how the person looks."
            ),
        }),
        "steps_title": "Computing the two predictions and the ratio",
        "steps_intro": "Four steps; the last is the one the chapter cares about.",
        "steps": [
            ("Put the distances in one unit",
             "Write the actual distance and the standard distance in the same unit as each "
             "other, and the size in the unit you want the answers in."),
            ("Compute the retinal-equivalent size",
             "Multiply the size by the standard distance and divide by the actual distance. "
             "That is the size a thing at the standard distance would need to subtend the "
             "same angle, and it is what the retinal-image account predicts."),
            ("Compute the inferred size and the ratio",
             "Multiply the retinal-equivalent size by the assumed distance over the standard "
             "distance. With the true distance this gives the size itself. Then subtract the "
             "retinal-equivalent size from the reported size and from the true size, and "
             "divide the first difference by the second."),
            ("Say what the figures are figures of",
             "The first two are predictions of two models and the third places a report "
             "between them. None of them is the size the thing has for the perceiver, which "
             "the chapter places at the thing's optimum distance, not in a computation."),
        ],
        "worked": {
            "title": "A person at the end of a room",
            "intro": [
                "A person 170 cm tall stands 8 m away; the standard distance is 2 m, and the "
                "illustrative report is 160 cm. You want both predictions and the ratio.",
            ],
            "lines": [
                "retinal-equivalent:  170 × 2/8 = 85/2 cm",
                "inferred, true distance:  (85/2) × 8/2 = 170 cm",
                "inferred, 4 m assumed:  (85/2) × 4/2 = 85 cm",
                "ratio:  (160 − 85/2) / (170 − 85/2)",
                "        = (235/2) / (255/2) = 47/51 ≈ 92%",
            ],
            "after": [
                "The two models bracket the report, and the report fits neither. The chapter "
                "does not offer a third formula for it. It says the size is given with the "
                "thing at its optimum distance, and that every other appearance is taken as a "
                "step towards that one.",
            ],
        },
        "quiz_title": "Constancy and the two predictions",
        "quiz": [
            {"q": "A lamp-post 6 m tall stands 30 m away; the standard distance is 2 m. What "
                  "is the retinal-equivalent size?",
             "a": ["2/5 m", "90 m", "6 m", "1/5 m"],
             "c": 0,
             "why": "`6 × 2/30 = 2/5` m, the height a post at 2 m would need to subtend the "
                    "same angle. Multiplying by 30/2 instead gives 90 m, the inversion. 6 m is "
                    "the inference account's answer, not the retinal-image account's, and 1/5 "
                    "m, which is `6/30`, forgets the standard distance."},
            {"q": "In the misjudged preset the inferred size falls to 85 cm. What does that "
                  "show?",
             "a": ["That the person looks half their height",
                   "That the inference account's prediction depends on the distance it assumes",
                   "That the retinal image has changed",
                   "That the chapter's account predicts 85 cm"],
             "c": 1,
             "why": "Only the assumed distance changed, from 8 m to 4 m, and the inferred size "
                    "halved with it. The retinal-equivalent size is still 85/2 cm. The figure "
                    "is a model's output, not a report of how anyone looks, and the chapter's "
                    "own account is stated in prose and computes nothing."},
            {"q": "Which view does the chapter state at length before questioning it, and "
                  "credit to Kant?",
             "a": ["That the true size is the one we see most often",
                   "That the true size is fixed by convention, within reach",
                   "That the true size is the law by which the appearance varies with distance",
                   "That the true size is the size at the thing's optimum distance"],
             "c": 2,
             "why": "Pages 349 to 351 state the law view and, following it out, arrive with "
                    "Kant at a world posited as a system. The convention within reach is the "
                    "psychologist's view, rejected first. The optimum distance is the "
                    "chapter's own answer on page 352, not the view it questions."},
            {"q": "On page 352, what does the chapter say the distance between me and a thing "
                  "is?",
             "a": ["A size that increases or decreases",
                   "An angle measured from the plane of my face",
                   "A quantity the mind infers from cues",
                   "A tension that fluctuates round a norm"],
             "c": 3,
             "why": "The chapter contrasts the two directly: not a size which increases or "
                    "decreases, but a tension round a norm. The angle from the plane of the face "
                    "is how it says an oblique position is not given, and inference from cues "
                    "is the account it is answering."},
        ],
        "mistakes": [
            ("Thinking the real size is inferred from the projected one",
             "This is the view usually credited to Helmholtz, and the chapter states it at "
             "strength as what the object is for science and objective thought: the "
             "constant product of distance and apparent size. The lab shows what it predicts when done right: `(85/2) × 8/2 = "
             "170` cm, perfect constancy, with no room for a report in between. The chapter's "
             "objection is not that the arithmetic fails but that it treats sizes as already "
             "determinate: the real size is not behind the appearance but is how the thing "
             "appears when seen at its best, and the other appearances are taken as steps "
             "towards that view."),
            ("Reading the retinal-equivalent size as what is seen",
             "The lab's 85/2 cm is the height a person at 2 m would need to subtend the same "
             "angle. It is a figure computed from geometry, and the retinal-image account "
             "predicts that it is what the person looks like. Nobody in the chapter reports "
             "that, and the chapter's point is that the angle is not the datum perception "
             "starts from."),
            ("Taking the optimum distance for a convention",
             "The psychologist also picks out a privileged distance, the one within reach, "
             "and calls it conventional. The chapter's optimum is not chosen. It is where the "
             "thing's detail is neither too much nor too little visible, and it differs from "
             "thing to thing, as a picture in a gallery asks to be seen from its own distance."),
        ],
        "standard": (
            "Finish when you can compute both predictions and the ratio, and say whose each is.",
            "Given a size, a distance, a standard distance and an assumed distance, compute the "
            "retinal-equivalent and inferred sizes and Brunswik's ratio for a reported size, "
            "name the model each figure belongs to, and state the chapter's reply to both."
        ),
        "note": (
            "The person, the distances and the reported 160 cm are illustrative, and Brunswik's "
            "ratio is a measure the book does not use. "
            "The lab computes what two models predict and where a report lies between them. "
            "It cannot compute the size a person has for someone who sees them, which the "
            "chapter says is given with the thing at its best distance; nothing in a formula "
            "can show whether that is right."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Smith p. 358 (opening passage: "If we so arrange it ... with the disc as
    # its base"); p. 354 (the brown table; the remembered colour, Hering's
    # Gedaechtnisfarbe, in the empiricist's voice); p. 355 (white paper in
    # shadow; the grey paper in the light; the judgement; "The weakness of
    # both empiricism and intellectualism ... a way into the thing"); p. 356
    # (Katz's coloured areas and surface colours); p. 357 (gaslight, the
    # photometer, the screen, the painter); p. 358 (the two boxes; Gelb's disc
    # and the white paper); p. 360 ("It is not seen itself, but causes us to
    # see the rest"); p. 361 (the guide in the apartment); p. 362 (the white
    # disc in the shady corner; "The lighting is not on the side of the
    # object, it is what we assume, what we take as the norm"; electric
    # light); p. 363 (the level; the paper and the cone); p. 365 (the woolly
    # blue; the constancy of the world); pp. 365-70 (weight and touch;
    # p. 367 the movement of one's own body is to touch what lighting is to
    # vision). Wallach is not named in the book (1945; his paper is 1948).
    {
        "slug": "colour-and-lighting",
        "title": "Colour and Lighting",
        "module": "Part Two · 3 · The Thing · Constancies",
        "one_line": "A thing's own colour is not the light it sends the eye but a colour seen through a lighting that is not itself seen, and the chapter reads Gelb's experiment to show it.",
        "summary": (
            "A black disc in a hidden beam sends the eye as much light as white paper in the "
            "room, and when a scrap of white paper is put in the beam the disc is seen black "
            "and strongly lit. Compute the luminances and each surface's ratio to its "
            "surround, and name what changed. Then read the chapter's account of lighting as "
            "what we see by, not what we see."
        ),
        "key": [
            "luminance = reflectance × illumination",
            "disc in the beam: 1/20 × 16 = 4/5",
            "paper in the beam: the disc's ratio is 1/16",
            "lighting: not seen, it shows the rest",
            "colour: a way into the thing",
        ],
        "key_label": "Colour constancy in five lines",
        "concepts_intro": (
            "The chapter's pages on colour lean on two psychologists, Gelb and Katz, and "
            "read their experiments against both classical accounts. Three terms carry it."
        ),
        "concepts": [
            ("Luminance",
             "The light a surface sends the eye: in the lab's simple model, the fraction of "
             "the light falling on it that it reflects, times the light falling on it. On the "
             "empiricist's view the luminance is the sensation, and a surface's colour should "
             "follow it."),
            ("Lighting",
             "The light a scene is lit by, as distinct from the colours of the things lit. "
             "The chapter's claim is that lighting is not seen as one more thing in the scene; "
             "it is taken as the norm against which the things' own colours stand out."),
            ("Modes of appearance",
             "David Katz's name for the different ways colour can be given: as a coloured "
             "area floating at a vague distance, as the surface of a thing, as the colour of "
             "a transparent volume, as gloss or glow. They obey different laws, and the "
             "chapter takes them as different colour-functions, not one sensation dressed "
             "differently."),
        ],
        "read_title": "The passage first, then the chapter's pages on colour line by line",
        "read_intro": (
            "The passage is Gelb's experiment as the chapter reports it. The lesson goes "
            "back to the brown table where the colour pages begin, follows them to the "
            "experiment, and then reads what the chapter makes of it."
        ),
        "body": [
            ("p", "<strong>Part Two, Chapter 3, p. 358.</strong> &ldquo;If we so arrange it "
                  "that the beam of an arc lamp falls exactly upon a black disc, and if the "
                  "latter is set in motion to eliminate the influence of the roughness which is "
                  "always present on its surface&mdash;the disc appears, like the rest of the "
                  "room, faintly lighted, and the beam of light is a whitish solid with the "
                  "disc as its base.&rdquo; The sentence is from page 358 of Smith's "
                  "translation. Read the colour pages from the paragraph on page 354 that "
                  "begins with the qualities of the thing to the end of the pages on touch on "
                  "page 370, in your own copy before going on."),
            ("p", "The pages open with an everyday case. The table in the room is, and remains, "
                  "brown under daylight, lamplight and dusk. What is this real colour? The first "
                  "answer, given in the empiricist's voice, is that it is the colour the table "
                  "has most often, in daylight and close to; under coloured light I substitute "
                  "a remembered colour, imprinted by many experiences. The physiologist Ewald "
                  "Hering called it memory colour. The chapter replies from the experiments: a "
                  "white paper seen in shadow and recognised as white is not simply white, and "
                  "a white wall in shade beside a grey paper in the light does not stay white "
                  "while the paper stays grey; the paper is the lighter. Constancy is not a "
                  "remembered quality laid over the light."),
            ("p", "The intellectualist answer fares no better, page 355 says. A judgement that "
                  "discounted the lighting would arrive at the object's true colour, and the "
                  "experiments show that the colour does not in fact stay identical. Then the "
                  "sentence that states the chapter's diagnosis of both: &ldquo;The weakness of "
                  "both empiricism and intellectualism lies in their refusing to recognize any "
                  "colours other than those fixed qualities which make their appearance in a "
                  "reflective attitude, whereas colour in living perception is a way into the "
                  "thing.&rdquo; Max Scheler, the German philosopher the chapter cites "
                  "here, put it that perception goes straight to the thing and by-passes the "
                  "colour, as it can catch the expression of a gaze without noting the colour "
                  "of the eyes."),
            ("p", "David Katz, a German psychologist whose book on the world of colour the "
                  "chapter draws on throughout, had shown that colour comes in modes. Smith "
                  "translates Katz's <em>Flächenfarben</em> as &ldquo;coloured areas&rdquo;, "
                  "the spongy colour of the spectrum, always parallel to the face and vaguely "
                  "placed, and <em>Oberflächenfarbe</em> as &ldquo;surface colour&rdquo;, "
                  "dense, holding the gaze on a surface at any angle. In gaslight a blue paper "
                  "looks blue, though a photometer shows that it sends the eye the mixture of "
                  "rays a brown paper sends in daylight. A screen with a small window turns "
                  "one mode into the other: a dimly lit white wall seen through it looks "
                  "bluish-grey. The painter does the same by half-closing his eyes. What the screen removes, the chapter says, is the articulation of the "
                  "whole field."),
            ("p", "Two more experiments, both reported by Adhémar Gelb, the Frankfurt "
                  "psychologist who also studied the patient Schneider with Kurt Goldstein, "
                  "show what the field needs. Look into two large boxes, one painted black "
                  "inside and strongly lit, one painted white and faintly lit, so that each "
                  "sends the eye the same light, and they cannot be told apart. Put a white "
                  "paper in the black box and at once the box appears black and strongly lit. For "
                  "lighting to appear as lighting there must be at least two surfaces of "
                  "different reflecting power. The disc in the passage is the same lesson in "
                  "a single room."),
            ("p", "The lab computes luminance in the simple model the empiricist needs: "
                  "reflectance times illumination, the reflectances illustrative. In the "
                  "<code>room</code> preset, all lit at 1, white paper reflects 4/5, the black "
                  "disc 1/20 and the wall, which is the surround, 1/2: the tile "
                  "<strong>luminance</strong> reads `4/5`, `1/20` and `1/2`. In the "
                  "<code>gelb</code> preset the hidden beam gives the disc an illumination of "
                  "16: `1/20 × 16 = 4/5`, exactly the white paper's luminance in the room. The "
                  "tile <strong>greatest luminance</strong> names the paper and the disc "
                  "together, a tie. If the light a surface sends were its colour, the disc would now have "
                  "the paper's colour. As the chapter reports it, the disc appears faintly lit "
                  "like the rest of the room, and the beam looks like a solid; nothing yet "
                  "shows a black disc under a strong light. The test comes with the paper."),
            ("p", "The <code>paper</code> preset puts a scrap of white paper in the beam, in "
                  "front of the disc. The disc's luminance has not changed: it is still `4/5`. "
                  "The paper's is `4/5 × 16 = 64/5`. What changed, the chapter reports from "
                  "Gelb, is everything: the disc is seen black, the paper white, and both under "
                  "a strong light, so completely that one seems to see a fresh disc. The tile "
                  "<strong>ratio to the surround</strong> divides each luminance by the "
                  "surround's. With the paper as surround, the disc's ratio is `(4/5) / (64/5) "
                  "= 1/16`; in the <code>gelb</code> preset, with the wall as surround, it was "
                  "`(4/5) / (1/2) = 8/5`, the same as the paper's own ratio in the room."),
            ("def", ("Wallach's ratio principle",
                     "Hans Wallach's proposal, published in 1948, three years after the book, "
                     "that the lightness a surface is seen to have follows the ratio of its "
                     "luminance to that of its surround, not its luminance alone. It is the "
                     "lesson's addition; the chapter does not compute anything.")),
            ("p", "So Wallach's principle, which came later, predicts the disc black beside the "
                  "paper, and the empiricist's luminance cannot. That is as far as a lab can "
                  "go, and the chapter goes further. On page 363 it reads the same experiment "
                  "as a change in the meaning of the whole: the paper forces us to recognise "
                  "that the cone of light is not solid, the beam and the disc come apart, and "
                  "the lighting takes on the quality of lighting. It is as if the significance "
                  "of one part of the spectacle made us re-read the whole. A ratio is a "
                  "relation between two figures; the chapter's claim is about the organisation "
                  "of a field in which there is lighting at all, and the ratio is not offered "
                  "as that."),
            ("p", "What, then, is lighting? Painters took centuries, page 360 says, to see the "
                  "reflection on the eye without which a face in an early painting looks dull "
                  "and sightless. The reflection went unnoticed and yet did its work: "
                  "&ldquo;It is not seen itself, but causes us to see the rest.&rdquo; The "
                  "chapter's comparison is with being led through a strange flat towards its "
                  "owner by someone who knows the way: the lighting directs my gaze, so that in "
                  "a sense it knows and sees the object. We perceive in conformity with the "
                  "light, it says, as we think in conformity with other people in conversation."),
            ("p", "And lighting is lived from where the body is. A white disc in a shady "
                  "corner of a bright room is imperfectly white; the white improves as you "
                  "approach the shade and is perfect when you are in it (p. 362). Yellow "
                  "electric light looks yellow as you come in from the day and soon has no "
                  "colour at all, so that a remnant of daylight in the room looks blue. "
                  "&ldquo;The lighting is not on the side of the object, it is what we "
                  "assume, what we take as the norm&rdquo;. Each colour becomes determinate "
                  "against a level that can change, page 363 says, as the spatial level did "
                  "in Up and Down, and taking up a new level is something the body does by "
                  "entering the new atmosphere."),
            ("p", "The pages end by widening the claim. A colour is never merely a colour but "
                  "the colour of some object, and the blue of a carpet, page 365 says, would "
                  "not be the same blue if it were not a woolly blue. The constancy of colour "
                  "is only an abstract part of the constancy of things, which rests in turn on "
                  "the constancy of the world as the horizon of all experience. Weight and "
                  "touch follow the same pattern: an object lifted with the hand, the head or "
                  "the foot weighs the same, which no induction from impressions could secure, "
                  "and the movement of one's own body, page 367 says, is to touch what "
                  "lighting is to vision."),
            ("p", "The carpet's woolly blue points to the next part of the chapter, where the "
                  "thing's qualities are read together. The next lesson, “The Thing and the "
                  "Real”, reads it."),
        ],
        "lab": ("phenkit", {
            "mode": "light",
            "view": "ratio",
            "model": "luminance as reflectance × illumination, with Wallach's ratio principle (1948, later than the book)",
            "preset": "room",
            "presets": [
                {"id": "room",
                 "label": "White paper, black disc and wall, all in the room's light (illustrative reflectances)",
                 "surfaces": "white paper, 4/5, 1; black disc, 1/20, 1; wall, 1/2, 1",
                 "surround": "wall",
                 "expect": {"liLuminance": "white paper 4/5, black disc 1/20, wall 1/2",
                            "liRatio": "white paper 8/5, black disc 1/10, wall 1",
                            "liBrightest": "white paper"}},
                {"id": "gelb",
                 "label": "Gelb's experiment: the disc alone in a hidden beam 16 times the room's light",
                 "surfaces": "white paper, 4/5, 1; black disc, 1/20, 16; wall, 1/2, 1",
                 "surround": "wall",
                 "expect": {"liLuminance": "white paper 4/5, black disc 4/5, wall 1/2",
                            "liRatio": "white paper 8/5, black disc 8/5, wall 1",
                            "liBrightest": "white paper, black disc"}},
                {"id": "paper",
                 "label": "A scrap of white paper placed in the beam, in front of the disc",
                 "surfaces": "black disc, 1/20, 16; paper in the beam, 4/5, 16",
                 "surround": "paper in the beam",
                 "expect": {"liLuminance": "black disc 4/5, paper in the beam 64/5",
                            "liRatio": "black disc 1/16, paper in the beam 1",
                            "liBrightest": "paper in the beam"}},
            ],
            "panel_title": "The light each surface sends, and its ratio to the surround",
            "panel_intro": (
                "This lab computes the empiricist's model of a colour sensation, luminance as "
                "reflectance times illumination, and beside it Wallach's ratio principle, "
                "published after the book: each surface's luminance over the surround's. The "
                "reflectances are illustrative. Compare the gelb and paper presets: the "
                "disc's luminance is the same in both, and only the surround differs."
            ),
        }),
        "steps_title": "Computing luminance and the ratio to the surround",
        "steps_intro": "Four steps, the last of which the lab cannot take for you.",
        "steps": [
            ("Multiply reflectance by illumination",
             "For each surface, the fraction of light it reflects times the light falling on "
             "it gives its luminance, in the lab's units."),
            ("Find the surround",
             "Pick the surface the others are seen against: the wall in the room, the paper "
             "once it is placed in the beam. Its luminance is the divisor."),
            ("Divide",
             "Each surface's ratio to the surround is its luminance over the surround's. A "
             "surface with a ratio above 1 sends more light than its surround, and one below "
             "1 less."),
            ("Say which model each figure belongs to",
             "Luminance is what the empiricist takes the sensation to be; the ratio is "
             "Wallach's later principle. The chapter's claim, that the paper makes the beam "
             "appear as lighting, is about the organisation of the field, and neither figure "
             "states it."),
        ],
        "worked": {
            "title": "Gelb's disc, with and without the paper",
            "intro": [
                "Take white paper at reflectance 4/5, the disc at 1/20 and the wall at 1/2, the "
                "room's light as 1 and the hidden beam as 16. You want the disc's luminance "
                "and its ratio to the surround, before and after the paper goes into the beam.",
            ],
            "lines": [
                "disc in the room:  1/20 × 1 = 1/20",
                "disc in the beam:  1/20 × 16 = 4/5",
                "paper in the room:  4/5 × 1 = 4/5",
                "disc / wall:  (4/5) / (1/2) = 8/5",
                "paper in the beam:  4/5 × 16 = 64/5",
                "disc / paper in the beam:  (4/5) / (64/5) = 1/16",
            ],
            "after": [
                "The disc's luminance is 4/5 before and after the paper is added; only the "
                "surround changed. The empiricist's model cannot tell the two situations apart, "
                "and Wallach's later ratio can. The chapter reads the change as the lighting "
                "appearing as lighting, which neither figure computes.",
            ],
        },
        "quiz_title": "Gelb's disc and the lighting",
        "quiz": [
            {"q": "A grey card of reflectance 3/10 lies under a lamp giving illumination 4. What "
                  "is its luminance, and its ratio to a surround of luminance 2?",
             "a": ["3/40 and 3/80", "6/5 and 3/5", "6/5 and 5/3", "12/10 and 12/5"],
             "c": 1,
             "why": "`3/10 × 4 = 6/5`, and `(6/5) / 2 = 3/5`. Dividing the reflectance by the "
                    "illumination gives 3/40. Turning the ratio over gives 5/3, the surround's "
                    "ratio to the card, and 12/10 is 6/5 unreduced but 12/5 multiplies by the "
                    "surround instead of dividing."},
            {"q": "When the white paper is placed in the beam, what happens to the disc's "
                  "luminance in the lab?",
             "a": ["It falls to 1/16",
                   "It falls to 1/20, the disc's luminance in the room",
                   "Nothing: it stays 4/5, and only its surround changes",
                   "It rises to 64/5"],
             "c": 2,
             "why": "The disc is still reflecting 1/20 of a beam of 16, so its luminance is "
                    "still 4/5. 1/16 is its ratio to the new surround, not its luminance. 1/20 "
                    "is the disc without the beam, and 64/5 is the paper's luminance."},
            {"q": "What does the chapter say lighting is, on pages 360 to 362?",
             "a": ["A colour added to the colours of things",
                   "A judgement that subtracts the light from each colour",
                   "A remembered colour that replaces the actual one",
                   "What we see by and take as the norm, not one more thing seen"],
             "c": 3,
             "why": "Lighting is not seen itself but causes us to see the rest, and is what we "
                    "assume, what we take as the norm. The subtracting judgement is the "
                    "intellectualist's account the chapter rejects on page 355, and the "
                    "remembered colour is Hering's, in the empiricist's voice."},
            {"q": "According to the chapter, what goes wrong in both the empiricist and the "
                  "intellectualist accounts of colour constancy?",
             "a": ["Both recognise only fixed qualities seen in a reflective attitude",
                   "Both deny that colours stay constant",
                   "Both ignore the physics of reflected light",
                   "Both rely on Wallach's ratio principle"],
             "c": 0,
             "why": "Page 355: their weakness lies in refusing to recognise any colours other "
                    "than fixed qualities that appear in a reflective attitude, where colour in "
                    "living perception is a way into the thing. Neither denies constancy; each "
                    "explains it. The chapter is not against the physics, and Wallach's "
                    "principle came three years after the book."},
        ],
        "mistakes": [
            ("Thinking the disc's colour is the light it sends the eye",
             "In the beam the disc sends the eye `1/20 × 16 = 4/5`, white paper's luminance "
             "in the room, and on the empiricist's view that light is the sensation of its "
             "colour. Then putting a paper in the beam should change nothing about the disc, "
             "whose luminance stays 4/5. Gelb's report, as the chapter gives it, is that the "
             "disc is at once seen black and strongly lit. The light the disc sends did not "
             "change; the field did."),
            ("Taking the ratio for the chapter's explanation",
             "The ratio to the surround gets the disc's change right, and it is tempting to "
             "read it as what the chapter means by the organisation of the field. The ratio is "
             "Wallach's, published in 1948, and it relates two luminances. The chapter's claim "
             "is that the paper makes the cone of light appear as lighting rather than as a "
             "solid, a change in what the whole spectacle means, and it computes nothing."),
            ("Reading lighting as one more colour in the scene",
             "On this reading the eye sees the yellow of the lamp and subtracts it. The "
             "chapter's yellow electric light soon has no colour at all, and the remnant of "
             "daylight looks blue: the lighting has become the norm, and is not seen beside "
             "the things it lights."),
        ],
        "standard": (
            "Finish when you can compute Gelb's luminances and ratios and say what the paper "
            "changed.",
            "Given reflectances, illuminations and a surround, compute each surface's luminance "
            "and ratio, show that the disc's luminance is the same with and without the paper, "
            "name the model each figure belongs to, and state the chapter's reading of the "
            "change."
        ),
        "note": (
            "The reflectances and the beam's 16 are illustrative; the chapter gives no figures "
            "for Gelb's experiment. The lab computes the empiricist's luminance and Wallach's "
            "ratio, which came after the book. It cannot compute whether a surface is seen as "
            "lit or as coloured, and the chapter's claim that lighting appears only in an "
            "organised field is a description no ratio tests."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Smith p. 372 (opening passage: "The unity of the thing beyond all its
    # fixed properties ... a second order expression"); p. 370 (the thing as
    # an inter-sensory entity; the moon's pale disc and the skull; not a
    # collection of stable attributes nor the notion of one); p. 371
    # (Berkeley's fly; a phenomenon striking one sense only is a phantom, the
    # wind; Cezanne and the smell of the landscape); p. 372 (the glass; the
    # sick man who sees the devil; heat and colour, "it is a priori necessary
    # that an extremely hot object should redden"; the thing understood as a
    # new kind of behaviour); p. 373 (the ash-tray; "in person", "in the
    # flesh"; anthropological predicates); p. 375 ("a genuine
    # in-itself-for-us"); p. 376 ("a resolutely silent Other"; Cezanne's
    # early portraits; the pre-world, Novotny's phrase; the carpet "made of
    # wool"); p. 377 (the picture and the real; the imaginary has no depth,
    # after Sartre's L'Imaginaire; the person at the door); p. 378 (the
    # stone broken up; the die); pp. 378-9 (the four reductions); p. 379
    # (realism; "In order to perceive things, we need to live them"); p. 380
    # (synthesis and the thing's transcendence; the pebble; the logic of the
    # world); p. 381 (Umwelt and Welt). Honey is named only in passing, among
    # tactile phenomena, on p. 368; Sartre's analysis of the viscous is not in
    # this chapter.
    {
        "slug": "the-thing-and-the-real",
        "title": "The Thing and the Real",
        "module": "Part Two · 3 · The Thing · The Real",
        "one_line": "A thing is not a bundle of qualities and not a concept that unifies them, but one manner of being that each of its qualities expresses, and it holds itself apart from the person who perceives it.",
        "summary": (
            "Having read the constancies sense by sense, the chapter turns to the thing that "
            "unites them. Compute two classical accounts' records over three of the "
            "chapter's observations about the thing, and find the observation on which they "
            "part and the one both fail. Then read the chapter's own account: the unity is a "
            "single manner of existing, and the thing is for us and yet rests in itself."
        ),
        "key": [
            "not a substratum, not a concept",
            "one manner of being in every quality",
            "the thing: an in-itself-for-us",
            "split: the hot object, the aloof thing",
            "both fail: the carpet's woolly colour",
        ],
        "key_label": "The thing in five lines",
        "concepts_intro": (
            "This part of the chapter asks what holds a thing's qualities together, and then "
            "why the thing so held seems to owe us nothing. Three ideas carry it."
        ),
        "concepts": [
            ("The inter-sensory thing",
             "The thing as given to sight, touch, hearing and smell at once, and the same "
             "for all of them. The chapter's question is what makes it one: the qualities "
             "added up, a concept that joins them, or something else."),
            ("A manner of existing",
             "The chapter's answer. The thing's unity is a single accent found in each of its "
             "qualities, as a person's style is found in each of their gestures, and the "
             "qualities express it. It is neither one more quality nor an idea behind them."),
            ("In-itself-for-us",
             "The chapter's name for the thing's double character. It exists only as "
             "something perceived, and yet presents itself as resting in itself, indifferent "
             "to the one who perceives it. Explaining both at once is the problem this part "
             "of the chapter sets."),
        ],
        "read_title": "The passage first, then the pages on the thing line by line",
        "read_intro": (
            "The passage is the chapter's own definition of the thing's unity. The lesson "
            "reads it phrase by phrase, sets out the two accounts it is directed against, "
            "counts them over three observations, and follows the chapter to the aloof thing "
            "and the die."
        ),
        "body": [
            ("p", "<strong>Part Two, Chapter 3, p. 372.</strong> &ldquo;The unity of the thing "
                  "beyond all its fixed properties is not a substratum, a vacant X, a subject in "
                  "which properties inhere, but that unique accent which is to be found in each "
                  "one of them, that unique manner of existing of which they are a second order "
                  "expression.&rdquo; The sentence is from page 372 of Smith's translation. "
                  "Read this part of the chapter from the paragraph on page 370 that begins "
                  "with the analysis of the thing as an inter-sensory entity to the end of the "
                  "paragraph on page 381 that ends with the natural world, in your own copy "
                  "before going on."),
            ("p", "The paragraph before the passage says what a thing is not. The moon's pale "
                  "disc to the eye, my own skull under my fingers, is neither a quality that "
                  "simply subsists nor the idea of one; it is what my gaze or my movement finds, "
                  "a question to which the thing gives a fitting reply. The qualities make one "
                  "thing, page 370 says, as my sight, my touch and my other senses are the "
                  "powers of one body in one action. A phenomenon that strikes only one sense, "
                  "a reflection or a light gust of wind, is a mere phantom; the wind comes close "
                  "to real existence when it blows hard enough to be seen in the tumult it makes "
                  "in the countryside (p. 371). And Cézanne, the chapter reports, said that a "
                  "picture contains even the smell of the landscape: a thing would not have this "
                  "colour if it did not also have this shape, this feel, this sound and this "
                  "smell."),
            ("p", "Now the passage. A <em>substratum</em>, a <em>vacant X</em>, a "
                  "<em>subject in which properties inhere</em>: three names for the "
                  "traditional picture of a thing as an unknown bearer under its qualities, "
                  "and the chapter rejects all three. What it puts in their place is an "
                  "<em>accent</em>, found in each quality, and a <em>manner of existing</em> of "
                  "which the qualities are a second-order expression. The examples follow at "
                  "once. The glass's brittleness, hardness, transparency and ring translate a "
                  "single manner of being; the lesson The Unity of the Senses read that case. "
                  "Heat comes into experience as a kind of vibration of the thing, and colour "
                  "as the thing thrust outside itself, so that &ldquo;it is a priori necessary "
                  "that an extremely hot object should redden&rdquo;. We understand a thing, "
                  "the chapter says, as we understand a new kind of behaviour: not by bringing "
                  "it under a concept, but by taking up the manner of existing its signs "
                  "outline."),
            ("p", "The two accounts these pages set aside are the Introduction's two. For "
                  "empiricism, the thing is a sum of sensory qualities, each delivered by its "
                  "own sense and joined to the others by association, because they have so "
                  "often come together. At its strength the view is economical: it needs "
                  "nothing but what the senses deliver and what experience repeats. For "
                  "intellectualism, the thing is a unity posited by thought, the law or concept "
                  "under which its appearances are brought, and at its strength it explains "
                  "why a thing's properties belong together and do not merely co-occur. The "
                  "chapter names the pair in one line on page 370: the question of defining the "
                  "thing as a collection of stable attributes, or as the notion of that "
                  "collection, will not arise."),
            ("p", "The lab counts the two accounts over three observations from these pages, in "
                  "the lesson's coding. A <strong>y</strong> means the account absorbs the "
                  "observation, an <strong>n</strong> that it cannot, a <strong>-</strong> "
                  "that it is silent. First, a very hot object must redden: empiricism "
                  "<strong>n</strong>, because association joins heat and red only as often "
                  "seen together, and the chapter calls the link a priori, that is, necessary "
                  "in advance of any experience of hot things; intellectualism "
                  "<strong>y</strong>, because a concept or law can carry a necessary "
                  "connection between properties. Second, the carpet's colour implies its "
                  "wool: <strong>n</strong> for both, for the reason the next paragraphs give. "
                  "Third, the thing rests aloof in itself: empiricism <strong>y</strong>, "
                  "because sensations are caused by things that exist without us; "
                  "intellectualism <strong>n</strong>, because a unity posited by thought is a "
                  "unity for thought, and page 380 says that on the synthetic view the thing "
                  "loses its transcendence and opacity, its standing beyond what thought "
                  "grasps of it."),
            ("p", "With all three observations, the <code>all</code> preset, the tile "
                  "<strong>record</strong> gives each account one observation absorbed and two "
                  "failed; the tile <strong>survivors</strong>, the accounts that fail nothing, "
                  "reads <em>none</em>; and the tile <strong>split</strong>, the observations on "
                  "which the two accounts part, names the hot object and the aloof thing. The "
                  "<code>qualities</code> preset shows the first two observations alone, and "
                  "still nothing survives. The <code>alien</code> preset shows only the third, "
                  "and empiricism survives it: a record depends on which observations are on "
                  "the table, and the coding of each cell is the lesson's reading, to be checked "
                  "against the page."),
            ("p", "The second observation is on page 376, and it is the one both accounts "
                  "fail. The chapter had said on page 365 that the blue of a carpet would not "
                  "be the same blue if it were not a woolly blue. Here it says &ldquo;it is "
                  "impossible completely to describe the colour of the carpet without saying "
                  "that it is a carpet, made of wool&rdquo;, and without implying in the colour "
                  "a certain feel, weight and resistance to sound. For the empiricist the "
                  "colour is one quality and the woolliness another. For the intellectualist "
                  "the sensed colour is a mere material that a concept organises, so the wool "
                  "is in the concept and not in the colour. The observation is that the colour "
                  "as seen is already woolly."),
            ("def", ("In-itself-for-us",
                     "The thing as it presents itself to the one who perceives it: as "
                     "existing in itself, apart from us. The chapter's phrase, on page 375, "
                     "is &ldquo;a genuine in-itself-for-us&rdquo;, and it names the problem "
                     "rather than a solution.")),
            ("p", "The third observation is the problem that phrase names. We cannot conceive "
                  "anything perceived without someone to perceive it, the chapter grants on "
                  "page 375, and yet the thing presents itself as a thing in itself. In daily "
                  "life we attend to things just enough to find their familiar presence. "
                  "Suspend those concerns and pay the thing a disinterested attention, and it "
                  "becomes hostile and alien, no longer a partner in dialogue but "
                  "&ldquo;a resolutely silent Other&rdquo;. Cézanne, in his early years, tried "
                  "to paint the expression of a face first, and never caught it; he learned "
                  "that expression is the language of the thing itself and comes from its "
                  "visible configuration, and his paintings, in a phrase the chapter takes from "
                  "the art historian Fritz Novotny, are those of a pre-world in which no men "
                  "yet existed."),
            ("p", "The real differs from a picture, page 377 says, because in the picture "
                  "significance comes before existence and wears only as much matter as it "
                  "needs, while in the real the two are one. Tear up a picture and you hold "
                  "pieces of daubed canvas; break a stone and break the pieces again, and they "
                  "are still stone. The real lends itself to unending exploration. The "
                  "imaginary has no depth and does not answer to a change of standpoint, the "
                  "chapter adds, citing Jean-Paul Sartre's study of the imagination: when you "
                  "wait at a door in a badly lit street, the familiar figure emerges from the "
                  "crowd as the earth from a ground mist, while in imagination, the chapter "
                  "says, I believe I have seen as soon as I mean to see."),
            ("p", "Then the die, on page 378. To someone in the natural attitude, who has never "
                  "wondered about perception, the die is simply there, and as they walk round "
                  "it they see not signs or projections but its sides. Reflection performs a "
                  "series of reductions: the die is for me only; it is only for sight, a shell "
                  "of colour and shape; it is a set of perspective views, some distorted; and at "
                  "last it is a sensation, a change in my body. The chapter's point is that the "
                  "experience of the thing does not go through these steps, and that any "
                  "definition built from them, whether a pole of my bodily life, a permanent "
                  "possibility of sensations or a synthesis of appearances, puts a "
                  "reconstruction in the thing's place."),
            ("p", "How can the thing be both the correlate of my body and indifferent to it? "
                  "Realism, which makes perception a coincidence with the thing, cannot say "
                  "what the event of perceiving is; the idealism of synthesis makes the thing "
                  "transparent to thought and so takes away what makes it a thing. &ldquo;In "
                  "order to perceive things, we need to live them.&rdquo; To live a thing, page "
                  "380 says, is neither to coincide with it nor to embrace it in thought. When I "
                  "see a pebble I am not expressly aware that I know it only through my eyes, "
                  "and yet I am not surprised when reflection says so. The chapter's account, "
                  "stated here and not scored in the table, is that I perceive with my body: "
                  "there is a logic of the world to which the whole body conforms, and through "
                  "it things with an inter-sensory meaning are possible for us."),
            ("p", "That account carries the thing beyond the body. Animal behaviour, page 381 "
                  "says, is aimed at an animal setting; human behaviour opens on a world beyond "
                  "the tools it makes, and can even treat its own body as an object. What has to "
                  "be explained next is that first understanding of the world. The next lesson, "
                  "“The Natural World”, reads it."),
        ],
        "lab": ("phenkit", {
            "mode": "cases",
            "view": "table",
            "accounts": ["empiricism", "intellectualism"],
            "preset": "all",
            "presets": [
                {"id": "all",
                 "label": "All three observations (the lesson's coding of pp. 372-376)",
                 "observations": "a very hot object must redden, n, y; "
                                 "the carpet’s colour implies its wool, n, n; "
                                 "the thing rests aloof in itself, y, n",
                 "expect": {"caRecord": "empiricism: absorbs 1 of 3, fails 2, silent 0; "
                                        "intellectualism: absorbs 1 of 3, fails 2, silent 0",
                            "caSurvivors": "none",
                            "caSplit": "a very hot object must redden, the thing rests aloof in itself"}},
                {"id": "qualities",
                 "label": "The qualities: the hot object and the carpet",
                 "observations": "a very hot object must redden, n, y; "
                                 "the carpet’s colour implies its wool, n, n",
                 "expect": {"caSurvivors": "none", "caSplit": "a very hot object must redden"}},
                {"id": "alien",
                 "label": "The aloof thing alone",
                 "observations": "the thing rests aloof in itself, y, n",
                 "expect": {"caSurvivors": "empiricism", "caSplit": "the thing rests aloof in itself"}},
            ],
            "panel_title": "Two accounts of the thing against three observations",
            "panel_intro": (
                "This lab counts the lesson's coding of the chapter's observations against "
                "the two classical accounts of the thing, empiricism's sum of qualities and "
                "intellectualism's unity posited by thought. The count is exact and the "
                "coding is an interpretation. Merleau-Ponty's own account is in the prose and "
                "is not a column."
            ),
        }),
        "steps_title": "Reading a table of accounts against observations",
        "steps_intro": "Four steps, the same for every table in this Subject.",
        "steps": [
            ("State each account at strength",
             "Write each account as its best defender would: the thing as associated "
             "qualities, the thing as a unity of thought. A weak statement makes every cell "
             "an easy n."),
            ("Code each cell from the page",
             "For each observation, ask whether the account can absorb it as the chapter "
             "reports it, and mark y, n or - for silent. Write down the reason, so that a "
             "reader can check it."),
            ("Count",
             "An account survives if it fails nothing. The split is the observations where "
             "one account absorbs and the other fails, which are the ones that tell them apart."),
            ("Put the chapter's account beside the table",
             "The chapter's own account is not a column. State it in prose, after the count, "
             "and say which observation it is built to meet."),
        ],
        "worked": {
            "title": "Three observations, two accounts",
            "intro": [
                "Code the three observations as the lesson does and count.",
            ],
            "lines": [
                "hot object: empiricism n, intellectualism y",
                "woolly carpet: empiricism n, intellectualism n",
                "aloof thing: empiricism y, intellectualism n",
                "empiricism: 1 absorbed, 2 failed",
                "intellectualism: 1 absorbed, 2 failed",
                "survivors: none; split: rows 1 and 3",
            ],
            "after": [
                "Each account fails somewhere, they part on the first and third observations, "
                "and both fail the carpet. The chapter's answer to the carpet, a single manner "
                "of existing found in each quality, is stated in prose and is not scored.",
            ],
        },
        "quiz_title": "The thing and its unity",
        "quiz": [
            {"q": "On the lesson's coding, why does empiricism fail the observation that a very "
                  "hot object must redden?",
             "a": ["Empiricism denies that hot objects redden",
                   "Empiricism has no account of colour",
                   "Association can only join heat and red as often found together, and the "
                   "chapter calls the link a priori",
                   "The chapter says empiricism is silent about heat"],
             "c": 2,
             "why": "Associated qualities are linked by repetition, so the link is contingent, "
                    "while page 372 calls it a priori necessary. Empiricism does not deny the "
                    "fact and does have an account of colour; the cell is n, not silent."},
            {"q": "In the alien preset only the aloof thing is shown, and empiricism survives. "
                  "What does that show?",
             "a": ["That the chapter sides with empiricism",
                   "That intellectualism is refuted",
                   "That the thing is a sum of qualities",
                   "That an account's record depends on which observations are on the table"],
             "c": 3,
             "why": "With all three observations empiricism fails two. Survival is relative to "
                    "the observations counted, and the coding is the lesson's. One n does not "
                    "refute intellectualism outright, and the chapter rejects the sum of "
                    "qualities in the passage itself."},
            {"q": "What does the chapter say the unity of the thing is?",
             "a": ["A unique manner of existing, of which the qualities are an expression",
                   "A substratum in which the qualities inhere",
                   "A concept under which the understanding brings the qualities",
                   "The quality that the most senses report"],
             "c": 0,
             "why": "The passage says it is not a substratum, a vacant X or a subject of "
                    "inherence, but an accent in each quality and a manner of existing. A "
                    "concept is the intellectualist's answer, which the chapter rejects on page "
                    "370, and no single quality is privileged."},
            {"q": "Why does the chapter call the thing an in-itself-for-us?",
             "a": ["It exists in itself and is never perceived",
                   "It exists only as perceived and yet presents itself as resting in itself",
                   "It is a mental image that we take to be outside us",
                   "It is whatever several perceivers agree on"],
             "c": 1,
             "why": "Page 375: we cannot conceive a thing without someone to perceive it, and "
                    "yet it presents itself as a thing in itself. A thing never perceived drops "
                    "the second half, a mental image drops the first, and agreement among "
                    "perceivers is not the chapter's criterion here."},
        ],
        "mistakes": [
            ("Thinking the real thing is the sum of its qualities, held together by the mind",
             "This joins the two accounts the chapter rejects: the sum is empiricism's and the "
             "mind's binding is intellectualism's. The table is the lab's half of the answer: "
             "the sum fails the hot object and the carpet, and the binding fails the carpet "
             "and the aloof thing. The chapter's half is in prose: the unity is a manner of "
             "existing that each quality expresses, which is not one more quality and not a "
             "concept, and the carpet's colour cannot be described without its wool."),
            ("Reading the aloof thing as a thing beyond perception",
             "The resolutely silent Other sounds like Kant's thing in itself, unknowable "
             "behind appearances. The chapter's thing is the perceived thing, met with "
             "disinterested attention; its aloofness is something it shows, and the chapter "
             "says it presents itself as in itself, not that it hides."),
            ("Taking the die's reductions for the order of perception",
             "Reflection takes the die apart into a thing for me, a visual shell, perspective "
             "views and finally a bodily sensation, and it is tempting to read the last as the "
             "first thing given. The chapter says the experience of the thing does not go "
             "through these steps, and that the thing built from them is a reconstruction."),
        ],
        "standard": (
            "Finish when you can count the two accounts and state the chapter's alternative.",
            "Given a coded table of the chapter's observations, compute each account's record, "
            "the survivors and the split, defend each cell from the page, and state, in the "
            "chapter's terms, what the unity of the thing is and why the thing rests in itself."
        ),
        "note": (
            "The table counts the lesson's coding of three observations, and a reader may code "
            "a cell differently; the hot object, in particular, could be argued silent for "
            "empiricism. The lab cannot score the chapter's own account, which is stated in "
            "the prose and would have a clean sheet only because the lesson coded it so. What "
            "the lab shows is where the two classical accounts part; whether a manner of "
            "existing is a better answer is the chapter's claim to weigh."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Smith p. 385 (opening passage: "The natural world is the horizon of all
    # horizons ... personal and historical life"); p. 381 (the primary
    # comprehension of the world; not Kant's system of invariable relations;
    # the crystal cube); p. 382 (the individual recognised by his style; "I
    # experience the unity of the world as I recognize a style"; ten years of
    # friendship; the permanent being within which I make all corrections;
    # "I may be mistaken ... compatible and compossible"; the distant roar of
    # a great city); p. 383 (no subject without a world; the deaf and blind;
    # the south side of the street; Paris); p. 384 (the perceiving body and
    # its points of view; driving towards a town, "I finally pass the
    # judgement: 'It is Chartres'"; the double image; "transition-synthesis";
    # the next room and the horizon); pp. 384-5 (Cezanne's vase); p. 385 (how
    # can any thing present itself if its synthesis is never complete; the
    # stone that is there); pp. 385-7 (the contradiction resolved in time; "If
    # I am at all times and everywhere ..."); pp. 387-8 (the white, hard, cool
    # stone; the world and time of Descartes); pp. 388-9 (mystery, not a
    # problem; the world is not an object). p. 401, in the Hallucination
    # pages ("disappears only to give place to another perception which
    # rectifies it"). The broad flat stone that turns out to be a patch of
    # sunlight is on p. 346, at the end of Chapter 2 (Lived Space), not in
    # this chapter.
    {
        "slug": "the-natural-world",
        "title": "The Natural World",
        "module": "Part Two · 3 · The Thing · The Natural World",
        "one_line": "The world is not a sum of things that might each be doubted but the horizon within which every perception is corrected by another, and its unity is recognised as a style is.",
        "summary": (
            "The chapter turns from the thing to the world it belongs to: one style "
            "recognised before it is defined, the horizon of all horizons, and the place where "
            "every mistake is corrected. Count the interpretations a judgement-from-cues "
            "model keeps as cues to a town on the horizon arrive, and notice what was never "
            "among them. Then read the chapter's answer to the sceptic."
        ),
        "key": [
            "the world: the horizon of all horizons",
            "its unity: recognised as a style",
            "a judgement welds two views of one world",
            "cues: 3 interpretations, then 2, then 1",
            "nothing there: never a candidate",
        ],
        "key_label": "The natural world in five lines",
        "concepts_intro": (
            "These eight pages ask what the world is, if it is not a thing, and how it can "
            "be real when no view of it is ever complete. Three ideas carry them."
        ),
        "concepts": [
            ("Horizon",
             "What lies beyond what is now in view and is present with it as more to be "
             "seen: the back of the cup, the next room, the land beyond the hill. A horizon "
             "is not imagined or recalled; it is part of how the present view is given."),
            ("Style",
             "A manner of dealing with situations, recognised in a person or a writer before "
             "anyone can define it. The chapter says the world's unity is known in this way, "
             "as a style rather than as a formula."),
            ("Transition-synthesis",
             "The chapter's word for how one perspective passes into the next. "
             "The views are not linked by the understanding after the fact; each slides into "
             "the other, as the two images of a pressed eye merge into one thing when the "
             "pressure stops."),
        ],
        "read_title": "The passage first, then the pages on the world line by line",
        "read_intro": (
            "The passage is the section's summary sentence. The lesson goes back to where the "
            "section begins, follows it through style, the outlines of a town and the sceptic's "
            "worry, and then reads its answer in time."
        ),
        "body": [
            ("p", "<strong>Part Two, Chapter 3, p. 385.</strong> &ldquo;The natural world is "
                  "the horizon of all horizons, the style of all possible styles, which "
                  "guarantees for my experiences a given, not a willed, unity underlying all the "
                  "disruptions of my personal and historical life.&rdquo; The sentence is from "
                  "page 385 of Smith's translation. Read the section from its first line on "
                  "page 381, where the chapter asks about the primary comprehension of the "
                  "world, to the end of the paragraph on page 389, just before the pages on "
                  "hallucination, in your own copy before going on."),
            ("p", "The section begins by saying what the world is not. The natural world, the "
                  "chapter had just said, is the schema of the relations among the senses. That "
                  "is not meant, as Kant would mean it, as a system of invariable relations to "
                  "which everything knowable is subject. The world is not like a crystal cube, "
                  "whose every side can be conceived from its geometry and whose hidden sides "
                  "show through. It has its unity even where the mind has not managed to fit its "
                  "facets into one geometrical projection (p. 381)."),
            ("p", "What kind of unity, then? The unity, page 382 says, of a person I recognise "
                  "before I could ever state the formula of their character, because they keep "
                  "the same style in everything they say and do. &ldquo;I experience the unity "
                  "of the world as I recognize a style.&rdquo; After ten years of friendship I "
                  "seem to be dealing with a different person, and after ten years in a "
                  "district, it is as if it were another; and yet, the chapter says, only the "
                  "knowledge of things has changed. The world stays the same world because it is "
                  "the permanent being within which I make all my corrections."),
            ("p", "Then the sentence the lesson's misconception is set against: &ldquo;I may be "
                  "mistaken, and need to rearrange my certainties, and reject the being to "
                  "which my illusions give rise, but I do not for a moment doubt that in "
                  "themselves things have been compatible and compossible&rdquo;. From the "
                  "start, the chapter goes on, I am in communication with one being, a vast "
                  "individual that persists on the horizon of my life as the distant roar of a "
                  "great city lies behind everything we do in it. You can conceive a subject "
                  "with no hearing; you cannot conceive one with no world. Even someone deaf "
                  "and blind from birth has something before them to be deciphered (p. 383)."),
            ("p", "The world does present itself in outlines. Here I see only the south side of "
                  "the street; I see nothing but Paris, and the countryside I have just left has "
                  "lapsed into a latent life. But the outlines do not stand side by side before "
                  "me. When they do come apart, page 384 says, as when I drive towards a town "
                  "and look at it only now and then, there is no longer a perception of the town: "
                  "I am suddenly faced with another object with no common measure with the one "
                  "before. &ldquo;I finally pass the judgement: &lsquo;It is "
                  "Chartres&rsquo;&rdquo;, and weld the two appearances together. The chapter's "
                  "point is in the next clause: I can do so only because both are drawn from one "
                  "and the same perception of the world."),
            ("p", "That judgement is something a lab can model. The model the lab computes is the "
                  "sceptic's picture of perception: a stream of cues, each read as a sign, and "
                  "interpretations kept while they fit and dropped when they do not, so that "
                  "any reading might always turn out false. The candidates and cues are the "
                  "lesson's illustration, since the chapter gives none: <em>a stand of "
                  "poplars</em> fits the first cue only, <em>a village church</em> the first "
                  "two, and <em>Chartres</em> all three. The cues are c1, tall shapes rise from "
                  "the plain far ahead; c2, a spire stands above a cluster of roofs; c3, two "
                  "spires, one plain and one ornate, over a town on a rise."),
            ("p", "The <code>first</code> preset shows c1 alone. The tile <strong>candidates "
                  "kept</strong> reads 3, the next tile names all three in list order, and the "
                  "tile <strong>removed by the last cue</strong> reads <em>none</em>. The step slider runs from 1 to 3; in this preset a step past 1 "
                  "is clamped, and the banner says so. The <code>all</code> preset shows the "
                  "three cues: at step 2 the count is 2 and the poplars are removed, and at step "
                  "3 the count is 1, Chartres, with the village church removed. Each "
                  "interpretation was dropped because another cue, another look at the horizon, "
                  "ruled it out."),
            ("p", "Now look at what was never in the list. Every candidate is a thing in the "
                  "landscape; none is <em>nothing at all</em>, and no cue could have put it "
                  "there. René Descartes, the French philosopher whose <em>Meditations</em> "
                  "(1641) began by doubting everything that could be doubted, gave the sceptic's "
                  "strongest form in the First Meditation: the senses sometimes deceive us, and "
                  "it is prudent never to trust wholly what has once deceived. The chapter "
                  "states the worry in its own words on page 385: since a thing's synthesis is "
                  "never complete, I can always expect it to break down and fall to the status of "
                  "a mere illusion. It answers on page 401, in the pages on hallucination: each "
                  "perception, though it can always be cancelled, &ldquo;disappears only to give "
                  "place to another perception which rectifies it&rdquo;. What is certain is that "
                  "there is a world."),
            ("def", ("The horizon of all horizons",
                     "Every perceived thing comes with horizons, more of it and more around it "
                     "to be seen. The world is not one more thing with a horizon but the "
                     "horizon in which all of these are, and the style that every particular "
                     "style belongs to.")),
            ("p", "With that, the passage reads plainly. My present view is not shut within my "
                  "visual field, page 384 says: the next room, the landscape behind the hill, "
                  "the inside of an object, are not recalled or pictured but already there. "
                  "When I see the bright green of one of Cézanne's vases, it does not make me "
                  "think of pottery; it presents it, smooth outside and porous within. The "
                  "world is the <em>horizon of all horizons</em>, and its unity is "
                  "<em>given, not willed</em>: I do not make it hold together by deciding to, "
                  "and it holds through every disruption of my personal and historical life. "
                  "Its counterpart in me, the chapter adds, is the general, pre-personal life of "
                  "my senses, in which the body was defined."),
            ("p", "But how can the world be a real individual if no view of it is complete and "
                  "its horizons are always open? Belief in the world seems to require a finished "
                  "synthesis, and the perspectives make finishing impossible. The chapter's "
                  "answer, pages 385 to 387, is that the contradiction holds only while we think "
                  "in terms of being, and dissolves into a general condition of experience once "
                  "we think in terms of time. The synthesis of horizons is a temporal process. If "
                  "I could survey the world from no point of view, at every time and place at "
                  "once, then, the chapter says, I would be at no time and nowhere, and nothing "
                  "would exist for me. The ambiguity of being here and also elsewhere is not a "
                  "defect of consciousness but its definition."),
            ("p", "Descartes appears once more, as the author of a picture of being. This stone "
                  "is white, hard and cool, and seems to need no time to exist; we are tempted "
                  "to think the world a collection of such things and time a collection of "
                  "perfect instants. &ldquo;Such are the world and time of Descartes&rdquo;, "
                  "page 388 says, and it grants that the picture is almost inevitable, since I "
                  "have a visual field with distinct objects. But each thing can show itself "
                  "fully only if others recede into the distance, so a sum of things makes no "
                  "sense. The thing and the world are mysterious, the section says near its "
                  "end, not as a "
                  "problem awaiting a solution but because they are not of the order of "
                  "objective thought, where there are solutions."),
            ("p", "This chapter's own example is the town, two appearances welded by a "
                  "judgement rather than an illusion corrected. The book's best-known "
                  "corrected illusion, the broad flat stone on a sunken path that turns out to be a "
                  "patch of sunlight, comes at the end of the chapter on space, on page 346, and "
                  "the lesson Lived Space reads it. The world in which every illusion is "
                  "corrected is also the world that a hallucination falls out of. The next "
                  "lesson, “Hallucination”, reads the chapter's last part."),
        ],
        "lab": ("phenkit", {
            "mode": "cues",
            "view": "sequence",
            "model": "the sceptic's picture of perception as an interpretation from cues that may always be false",
            "preset": "all",
            "cue_text": {
                "c1": "tall shapes rise from the plain far ahead",
                "c2": "a spire stands above a cluster of roofs",
                "c3": "two spires, one plain and one ornate, over a town on a rise",
            },
            "presets": [
                {"id": "first",
                 "label": "The first glance from the road: cue c1 only (illustrative)",
                 "candidates": "a stand of poplars, c1; a village church, c1 c2; Chartres, c1 c2 c3",
                 "cues": "c1",
                 "expect": {"cuCount": "3",
                            "cuCandidates": "a stand of poplars, a village church, Chartres",
                            "cuRemoved": "none"}},
                {"id": "all",
                 "label": "Three glances on the way to Chartres: cues c1 to c3 (illustrative)",
                 "candidates": "a stand of poplars, c1; a village church, c1 c2; Chartres, c1 c2 c3",
                 "cues": "c1, c2, c3",
                 "expect": {"cuCount": "1", "cuCandidates": "Chartres",
                            "cuRemoved": "a village church"}},
            ],
            "panel_title": "Interpretations kept as the cues arrive",
            "panel_intro": (
                "This lab computes the sceptic's picture of perception: each cue is a sign, and "
                "an interpretation is kept while it fits every cue so far. The candidates and "
                "cues are the lesson's illustration. Move the step slider in the all preset "
                "and watch the count fall; then look at what the list never contained."
            ),
        }),
        "steps_title": "Following interpretations through a sequence of cues",
        "steps_intro": "Four steps; the fourth is the chapter's question, not the model's.",
        "steps": [
            ("List the candidates and the cues each fits",
             "Write each interpretation with the cues it is consistent with. An "
             "interpretation that fits a cue stays when that cue arrives."),
            ("Apply the cues in order",
             "At each step keep the candidates that fit every cue so far, and note which "
             "were removed by the latest one."),
            ("Read the count",
             "The count is how many interpretations the cues leave standing. One left means "
             "the cues have decided between the candidates, not that the last one is true."),
            ("Ask what was never a candidate",
             "Check whether any candidate was the absence of anything. The model only ever "
             "chooses among things in a world; the chapter's point is that every correction "
             "presupposes that world."),
        ],
        "worked": {
            "title": "Three glances at the horizon",
            "intro": [
                "Take the three candidates and three cues of the all preset and count after "
                "each cue.",
            ],
            "lines": [
                "after c1:  poplars, church, Chartres: 3",
                "after c2:  church, Chartres: 2 (poplars removed)",
                "after c3:  Chartres: 1 (church removed)",
                "nothing there:  never a candidate",
            ],
            "after": [
                "Each reading was dropped because a later look ruled it out, and the reading "
                "that replaced it was another thing on the horizon. That is the model's version "
                "of the chapter's reply: a perception is cancelled only by another perception, "
                "which already counts on the world.",
            ],
        },
        "quiz_title": "The world and its corrections",
        "quiz": [
            {"q": "Candidates: a hedge (fits c1), a wall (c1, c2), a barn (c1, c2, c3). After "
                  "cues c1 and c2, which remain?",
             "a": ["the barn only", "the hedge, the wall and the barn", "the hedge only",
                   "the wall and the barn"],
             "c": 3,
             "why": "Keep the candidates that fit every cue so far. The hedge fails c2; the wall "
                    "and the barn fit both. The barn alone is what remains after c3, and the "
                    "hedge alone is the one removed."},
            {"q": "How does the chapter say the unity of the world is known?",
             "a": ["As a style is recognised, before any formula for it",
                   "As a system of invariable relations, the way Kant conceives it",
                   "As the sum of every thing ever perceived",
                   "By a judgement that links each pair of perspectives"],
             "c": 0,
             "why": "Page 382: I experience the unity of the world as I recognise a style. Page "
                    "381 says the world is not Kant's system of invariable relations. A sum of "
                    "things, page 388 says, makes no sense, and the Chartres judgement welds two "
                    "views only because both are already drawn from one world."},
            {"q": "Which reply to the sceptic does the chapter give?",
             "a": ["Perceptions are never mistaken",
                   "A perception is cancelled only by another perception that corrects it",
                   "God guarantees that clear perceptions are true",
                   "Since each thing may be an illusion, so may the world"],
             "c": 1,
             "why": "Page 401: each perception disappears only to give place to another which "
                    "rectifies it. The chapter admits mistakes (page 382), the guarantee by God "
                    "is Descartes's later answer, not this chapter's, and the last option is the "
                    "sceptic's step the chapter refuses."},
            {"q": "In the Chartres passage, what makes the final judgement possible, on the "
                  "chapter's reading?",
             "a": ["The judgement creates the link between two unrelated appearances",
                   "The driver remembers a map of the region",
                   "Both appearances are drawn from one and the same perception of the world",
                   "The two appearances are identical"],
             "c": 2,
             "why": "Page 384: I weld the two appearances together, but I can do so because "
                    "both come from one perception of the world. The judgement does not create "
                    "the link from nothing; no map is mentioned; and the appearances have, the "
                    "chapter says, no common measure."},
        ],
        "mistakes": [
            ("Thinking that because any perception may be an illusion, all of them might",
             "This is the Cartesian sceptic of the First Meditation, at strength: the senses "
             "have deceived before, so none of their reports is safe. The chapter grants that "
             "each perception can be cancelled, and denies the step from each to all. An "
             "illusion is unmasked only by another perception, which counts on the world. The "
             "lab's candidates, a stand of poplars, a village church, Chartres, are all "
             "interpretations of something there; dropping one never produced nothing."),
            ("Reading the world as the largest thing",
             "The world sounds like everything added up. The chapter says the world is not an "
             "object and not a sum of things, since each thing shows itself only as others "
             "recede; it is the horizon of all horizons, the setting within which things "
             "appear and are corrected."),
            ("Hearing the mystery of the world as an unsolved problem",
             "On page 388 the thing and the world are an absolute mystery. That is not a gap "
             "that more knowledge could close; the chapter says the mystery is not of the "
             "order of objective thought, where there are solutions."),
        ],
        "standard": (
            "Finish when you can count the interpretations and state the chapter's reply to "
            "the sceptic.",
            "Given candidates and the cues each fits, count the interpretations left after "
            "each cue and name those removed, say what was never a candidate, and state in the "
            "chapter's terms why every correction presupposes the world."
        ),
        "note": (
            "The candidates and cues are the lesson's illustration; the chapter gives only the "
            "judgement &lsquo;It is Chartres&rsquo; and no cues. The model computes what a "
            "judgement from signs keeps, and in it the world is presupposed by the list of "
            "candidates, which the lesson wrote. Whether perception is in fact such a "
            "judgement, and whether the world is given as a style, the lab cannot decide."
        ),
    },
]
