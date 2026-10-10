# How the figures in ../PLAN.md were measured

Every figure in `PLAN.md` marked *designer-measured* came out of one of these
scripts, run on 2026-10-10 over the four source files `fetch.sh` downloads
(CMUdict at cmusphinx/cmudict master, BSD-2; Pride and Prejudice, Gutenberg
#1342, and The Importance of Being Earnest, Gutenberg #844, public domain;
the Moby Part-of-Speech list, Gutenberg #3203, public domain) plus the lists
already in the repository (`scripts/wordlists/ngsl.tsv`, CC BY-SA 4.0;
`/usr/share/dict/american-english`, SCOWL). The outputs are in `out/`.

    ./fetch.sh
    /usr/bin/python3 -I m_cmudict.py   # endings, stress, letters-to-sounds, a/an, linking
    /usr/bin/python3 -I m_corpus.py    # helping verbs, boxes, time prepositions, tags, contractions, phrasal verbs, comparatives, coverage
    /usr/bin/python3 -I m_nouns.py     # plurals and -ly, against the dictionary
    /usr/bin/python3 -I m_follow.py    # the refinements the plan relies on
    /usr/bin/python3 -I m_last.py      # the Wilde excerpt, Chapter XXVI, data sizes

sha256 of the sources as fetched on 2026-10-10:

    81917843c7f44ce2b094ac63873c2c7a4cf802040792c455ba3ca406891c3d22  cmudict.dict
    3f6bb9d6f78e0293b56acd4714dd68cb7d6d1d293402031ce9d5a216bcaf9d75  pg1342.txt
    1b8a58099bb1cdef6a845277a4bacf2f4a268702c165bde30124d4b5105d1851  pg844.txt
    cc81458b820a36253fbeb8106045166a345209d0fbf4cbfc20be2b189f24af82  mobypos.txt

These are design measurements, not the shipped computation. The kit engineer
re-derives every figure from the page with `node scripts/labcheck.js
--observe`, and the lessons state what the page prints. Where the two differ,
the page wins and the plan is corrected, not the page.

## The shipped data

The files the pages read are not written by these scripts. They are written by
committed scripts in `scripts/wordlists/` that read the same four sources from
`data/` here (or `--sources DIR`), check each one's sha256 against the list
above before using it, and have a `--check` mode that fails when a committed
file is out of date:

    /usr/bin/python3 scripts/wordlists/clean_nouns.py        # plural_nouns.json
    /usr/bin/python3 scripts/wordlists/clean_adjectives.py   # ly_adjectives.json
    /usr/bin/python3 scripts/wordlists/concordance.py        # content/english/data: the lines and the chapter
    /usr/bin/python3 scripts/wordlists/sounds.py             # verb_sounds.json, an_sounds.json (after the two above)
    node scripts/wordlists/english_check.js                  # every figure the new presets pin

Where a shipped figure differs from a design figure in `PLAN.md`, the cause is
in the script's docstring (a cut that now starts at a sentence boundary, a
stoplist, the irregular-plural override); the page's figure is the one a lesson
states.
