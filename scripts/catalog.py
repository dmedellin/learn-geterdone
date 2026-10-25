"""The library's catalog: which Subjects the home page shows, in what order,
under which heading, and with what one-line description.

GENERATED_PATHS in build_paths.py says what is PUBLISHED. This file says how
the library is PRESENTED. They were one list until there were twelve Subjects,
and the home page, the course search and the progress page all showed the order
the Subjects happened to be wired in -- a reader saw Algebra between Discrete
Mathematics and System Design, and the two read-alongs separated from
Philosophy by English and Differential Equations. Nobody had chosen that order;
it was the date each Subject went live.

Everything that lists Subjects reads its order from SUBJECTS below:

    site/index.html             scripts/build_index.py (cards and course search)
    site/progress/index.html    scripts/build_auth_pages.py (library_inventory)
    site/oauth2/spa/callback/   the same inventory

A new Subject is one entry here, in its group, at the place a reader should
meet it. tests/test_site_invariants.py fails if a published Subject is missing
from this file or a Subject here is not published.

Ordering rule: by domain, then by dependency inside the domain, so a Subject
that assumes another comes after it. Group notes and card text are home-page
copy and are swept by the same copy rules as the rest of that page: no "path",
no "N subjects", no "course N" and no "take these in order".
"""

# Each group is a heading on the home page. `note` is one sentence under it.
GROUPS = (
    {
        "key": "mathematics",
        "title": "Mathematics",
        "note": "Algebra and Discrete Mathematics assume school arithmetic and "
                "algebra; Differential Equations builds on Algebra.",
    },
    {
        "key": "computing",
        "title": "Computing and decisions",
        "note": "Algorithms, System Design and Operations Research build on "
                "Discrete Mathematics, the last two on Algebra as well; Code "
                "Complete assumes only that you can read a short routine.",
    },
    {
        "key": "philosophy",
        "title": "Philosophy and close reading",
        "note": "None of these assumes another Subject. The two read-alongs go "
                "through one book chapter by chapter.",
    },
    {
        "key": "language",
        "title": "Language and study skills",
        "note": "For adult readers; nothing else in the library is assumed.",
    },
    {
        "key": "markets",
        "title": "Markets",
        "note": "Educational material on synthetic data. Read the notice below "
                "before the courses.",
    },
)

# Display order. `slug` is the Subject's /paths/<slug>/ URL and never changes.
#
#   group        a GROUPS key
#   card         one sentence for the home card, HTML allowed (<em>, entities);
#                the course roll-call belongs on the Subject page, not here
#   short_title  shown on the home card when the Subject's own title carries a
#                format label; the Subject page and breadcrumbs keep the title
#   kind         a format label shown as the card's eyebrow
#   builds_on    other Subjects this one assumes, linked from the card
#
# Trading, Discrete Mathematics and Algebra keep the card text they have
# always had: tests/content_preservation.json pins it.
SUBJECTS = (
    {
        "slug": "algebra",
        "group": "mathematics",
        "card": "Expressions, equations, functions, polynomials, systems, "
                "matrices, sequences, and series.",
    },
    {
        "slug": "discrete-math",
        "group": "mathematics",
        "card": "Logic, proof, sets, counting, probability, number theory, "
                "graphs, and algorithms.",
    },
    {
        "slug": "differential-equations",
        "group": "mathematics",
        "card": "Rates of change and the integral, then first- and second-order "
                "equations, phase planes, oscillators and the Laplace transform.",
        "builds_on": ("algebra",),
    },
    {
        "slug": "algorithms",
        "group": "computing",
        "card": "Data structures and the classic families of algorithm, from "
                "sorting and graphs to dynamic programming and intractability.",
        "builds_on": ("discrete-math",),
    },
    {
        "slug": "system-design",
        "group": "computing",
        "card": "The arithmetic of a running service: capacity, latency, "
                "queues, caching, failure, replication and cost.",
        "builds_on": ("algebra", "discrete-math"),
    },
    {
        "slug": "operations-research",
        "group": "computing",
        "card": "Deciding under constraints: linear and integer programming, "
                "networks, scheduling, inventory, queues and simulation.",
        "builds_on": ("algebra", "discrete-math"),
    },
    {
        "slug": "code-complete",
        "group": "computing",
        "short_title": "Code Complete",
        "kind": "Read along",
        "card": "Steve McConnell&rsquo;s <em>Code Complete</em>, chapter by "
                "chapter, with each chapter&rsquo;s guidance measured on short "
                "pieces of code.",
    },
    {
        "slug": "philosophy",
        "group": "philosophy",
        "card": "Arguments, knowledge, decision, ethics, justice, mind and "
                "paradox, each worked as a problem you can check.",
    },
    {
        "slug": "phenomenology",
        "group": "philosophy",
        "short_title": "Phenomenology of Perception",
        "kind": "Read along",
        "card": "Merleau-Ponty&rsquo;s <em>Phenomenology of Perception</em>, "
                "section by section, from the Preface to Freedom.",
    },
    {
        "slug": "capital",
        "group": "philosophy",
        "short_title": "Capital",
        "kind": "Read along",
        "card": "Marx&rsquo;s <em>Capital</em>, all three volumes, chapter by "
                "chapter, with the arithmetic done beside the text.",
    },
    {
        "slug": "reading-faster",
        "group": "language",
        "card": "Timed reading with comprehension checks, and a training plan "
                "built on your own log of results.",
    },
    {
        "slug": "english",
        "group": "language",
        "card": "English for speakers of other languages: verb forms, articles, "
                "word order, spelling, stress and listening.",
    },
    {
        "slug": "trading",
        "group": "markets",
        "card": "Price structure, trade planning, options, indicators, order "
                "flow, risk management, backtesting, and automation.",
    },
)

# Course search descriptions written here because the course's own summary
# cannot be shown in search: it refers to "the path" or "this path", which the
# library's search copy may not say. Every other course is described by its
# summary, the same sentence its course home gives as its meta description, or
# by its blurb when the summary has that problem (scripts/build_index.py).
SEARCH_DESCRIPTIONS = {
    "logic-and-proof":
        "Propositional and predicate logic from truth values to written proofs: "
        "connectives, truth tables, equivalence, normal forms, quantifiers and "
        "their negations, inference rules, and direct, contrapositive, "
        "contradiction, and case proofs.",
    "sets-relations-functions":
        "Sets and their algebra, power sets and Cartesian products, relations and "
        "the structures they define, functions and their mapping properties, "
        "cardinality, and the pigeonhole principle.",
    "simulation-and-variance-reduction":
        "What to do when no exact method applies: run the model, and then refuse "
        "to pretend the number that came out is the answer. A seeded stream "
        "becomes draws, draws become an estimate, and the estimate arrives with a "
        "width attached \u2014 the only width the method can justify, which is "
        "Chebyshev's and says so. Then a queue run as an event calendar, the bias "
        "a run started empty puts in its own average, and four ways to make the "
        "width narrower without buying draws, each of them a covariance being "
        "moved and two of them shown failing.",
}

# Trading is hand-authored and has no PATH dict; this is the little the
# catalog needs to know about it.
TRADING = {"slug": "trading", "title": "Trading"}


def group(key):
    for entry in GROUPS:
        if entry["key"] == key:
            return entry
    raise KeyError(key)


def order_of(slug):
    """Position of a Subject in the catalog, for sorting."""
    for position, entry in enumerate(SUBJECTS):
        if entry["slug"] == slug:
            return position
    raise KeyError("%s is not in scripts/catalog.py" % slug)
