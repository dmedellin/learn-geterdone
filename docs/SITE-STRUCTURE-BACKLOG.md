# Site structure backlog

A review of how the library is organized: the home page, the Subject pages,
course listings, navigation and naming. Written 2026-10-25, after Reading Faster
became the twelfth Subject, in answer to "there is no order in the main page".

Two independent reviews fed it: a UX and learning-design pass (Fable) and an
architecture and maintainability pass (Opus). Neither edited anything. Their
findings were merged, the overlaps collapsed, and the load-bearing claims
re-checked against the tree. Line numbers are from `3f5f387`.

Nothing here is scheduled. Each item says what it touches so it can be picked up
on its own.

## Why the home page has no order

The twelve cards are in the order the Subjects were wired:
`[trading] + GENERATED_PATHS` (`scripts/build_paths.py:40-43`). Nobody chose
that order; it is the date each Subject went live. So Algebra, which Differential
Equations and Operations Research both assume, sits between Discrete Mathematics
and System Design, and the two read-alongs are separated from Philosophy by
English and Differential Equations.

The deeper cause is that the Subject list is kept by hand in at least four
places that each inherit build order:

| copy | where | kept by |
|---|---|---|
| home cards | `site/index.html:1428`, one 12 KB line | hand |
| home search array | `site/index.html`, `var COURSES = [...]` | hand, order pinned by `tests/test_course_ui.py:295` |
| progress and sign-in inventories | `scripts/build_auth_pages.py:85-99` `library_inventory()` | generated, in `GENERATED_PATHS` order |
| test inventory | `tests/test_site_invariants.py:1769-1795` `PATHS` | hand |

Reordering only the cards fixes what Dave sees today. Without a single catalog,
the thirteenth Subject is appended last again and Progress keeps the old order.

## Proposed home page structure

Group by domain, order by dependency inside each group. Both reviewers landed on
nearly the same groups; they differed only on Trading (see the note below).

| group | Subjects, in order | one-line group note |
|---|---|---|
| Mathematics | Algebra, Discrete Mathematics, Differential Equations | Algebra assumes only arithmetic; Differential Equations assumes Algebra |
| Computing and decisions | Algorithms, System Design, Operations Research | built on Discrete Mathematics; Operations Research also on Algebra |
| Philosophy and close reading | Philosophy, Phenomenology of Perception, Capital | none assumes another Subject |
| Language and study skills | Reading Faster, English | for any adult reader |
| Markets | Trading | educational only, synthetic data |

Card anatomy, identical for all twelve: an eyebrow that carries information (the
group, or "Read along"), the title, one sentence of at most about 20 words, a meta
line (`10 courses · 108 lessons · Beginner → Advanced`), a muted "assumes …" line
that links to other Subjects, and "View courses".

Trading: the UX review put it in its own Markets group at the end, so its notice
sits beside it rather than at the foot of a shared page; the architecture review
put it last in Computing and decisions. **Recommendation: a Markets group.** It
gives the disclaimer a natural home (B-6) and leaves room if a second markets
Subject ever comes.

The seven proposals in [FUTURE-SUBJECTS.md](FUTURE-SUBJECTS.md) fit without a
new group: PARA, Zettelkasten, Pomodoro and Idioms and languages under Language
and study skills; Fields (and Music, if built as acoustics) under Mathematics,
which could become "Mathematics and science"; biography-as-evidence under
Philosophy and close reading.

## Constraints any fix must respect

- **Copy rules on the home page.** `tests/test_course_ui.py:259-300` forbids in
  `<main>` the patterns `\d+ subjects`, `course \d`, `(learning )?paths` and
  "take … courses in order"; `LIBRARY_TAXONOMY_RE` in
  `tests/test_site_invariants.py` forbids "the path" and "browse paths". Group
  labels must be plain nouns. "14 courses" passes; "Course 14" fails.
- **Pinned home copy.** `tests/content_preservation.json` →
  `authored_semantic_copy.pages[""]` pins the h1, the "Subjects" h2 and its lead,
  and the h3 and blurb of Trading, Discrete Mathematics and Algebra, as a set
  rather than by position (`tests/test_public_copy.py:15-48`). Reordering and
  wrapping groups is safe. Rewording those three blurbs, renaming "Subjects", or
  demoting card titles below `h3` is a deliberate fixture change. Use a labelled
  `<section aria-labelledby>` or an eyebrow for group headings and keep cards at `h3`.
- **Courses are unnumbered by policy.** `tests/test_course_ui.py:339` asserts
  Subject pages do not number courses. Communicate order through dependency
  ("Builds on …"), not ordinals.
- **No URL renames.** Course homes are flat, retired URLs are never re-added and
  get no redirects, and progress ticks are keyed `course-slug/lesson-slug`. A
  rename costs all five URL declarations, the release contract, the expectations
  file, external links and every reader's progress. All naming fixes below are
  display-only.

## Backlog

Priority: **P1** answers the complaint or stops it recurring; **P2** is a clear
improvement to finding and following material; **P3** is polish or hygiene.
Effort: S (an hour or two), M (a session), L (several sessions).
Source: UX-n and ARCH-n are the reviewers' finding ids.

### Phase 0: display-only, no data-model change

| id | pri | item | effort | touches | source |
|---|---|---|---|---|---|
| B-1 | P1 | **Group and reorder the home cards** by hand into the five groups above, one card per line, cards kept at `h3`, the three pinned blurbs untouched. Search and Progress stay in build order until B-8; that inconsistency is known and temporary. | S | `site/index.html` | UX-1, UX-2, UX-18, ARCH-8 |
| B-2 | P1 | **Replace the "SUBJECT" eyebrow** on all twelve cards (it carries no information) with the group name, or "Read along" for Capital and Phenomenology. | S | `site/index.html` | UX-3, ARCH-12 |
| B-3 | P1 | **Shorten card descriptions** to one sentence each. They range from 11 words (Discrete Mathematics) to 60 (Capital), and the long ones are course roll-calls that the Subject page already shows. Shorten the nine unpinned ones; leave Trading, Discrete Mathematics and Algebra unless the fixture is updated on purpose. | S | `site/index.html` | UX-5, ARCH-19 |
| B-4 | P2 | **Fix the Subject page "Courses" header**: a long `sequence_intro` renders as a right-hand column beside the h2 (visible on Capital). Move the `<p>` inside the inner `<div>`, as the home page does, and rebuild. | S | `scripts/mathpath/render.py:537-539`, 11 Subject pages via build | ARCH-14 |
| B-5 | P2 | **Move course search above the Subjects** and name the nav item "Find a course" (it says "Courses" and lands on a search box ~1,500 px down on desktop, ~5,000 px on a phone). Optionally put the search field in the hero. Region order is not tested. | S | `site/index.html`, `scripts/mathpath/chrome.py` masthead, Trading pages via `add_progress_marks.py` | UX-16, UX-22, UX-23 |
| B-6 | P2 | **Move the Trading notice off the foot of the shared home page.** Keep a one-line notice under the Markets group linking to the full text on `/paths/trading/`; move the dated-exception paragraph there entirely (the home page never links that example). Check `scripts/smoke.py` and the Trading vocabulary scanner first. | S | `site/index.html`, `site/paths/trading/index.html` | UX-21 |
| B-7 | P3 | **Hide the empty progress pill** on generated course cards (`<span class="spine-progress"></span>` draws an empty bordered pill when there is no progress): `:empty { display:none }` or render with `hidden`. | S | `scripts/mathpath/progress.py` or theme CSS | ARCH-15 |

### Phase 1: one catalog, so order cannot rot again

Must come before any further home-page polish.

| id | pri | item | effort | touches | source |
|---|---|---|---|---|---|
| B-8 | P1 | **Add a `LIBRARY` catalog**: an ordered list of `{slug, group, short_title, card}` with a Trading stub carrying its level and assumes. Keep `GENERATED_PATHS` as the publish switch only. A test asserts catalog slugs equal `{trading}` plus the `GENERATED_PATHS` slugs. `library_inventory()` iterates the catalog, so Progress, the sign-in callback and the search array all follow it; regenerate the auth pages and reorder the search array (its order is test-pinned). | M | `scripts/build_paths.py` (or `scripts/catalog.py`), `scripts/build_auth_pages.py`, `site/progress/`, `site/oauth2/spa/callback/`, `site/index.html` search array | ARCH-1, ARCH-5, ARCH-16, UX-17 |
| B-9 | P2 | **Test that card order equals catalog order**, so a hand edit to the cards cannot drift. | S | `tests/test_course_ui.py` | ARCH-2 |
| B-10 | P3 | **Fix stale docs**: `site-architect.md` still names the removed `pages.yml`; `build_auth_pages.py:66` docstring says "the two mathematics paths"; README describes `/` as "the paths". | S | those three files | ARCH-17 |

### Phase 2: generate the home page

| id | pri | item | effort | touches | source |
|---|---|---|---|---|---|
| B-11 | P1 | **Generate the Subjects section and the `COURSES` array** between marker comments in `site/index.html`, from the catalog and content, with a `--check` mode in CI. The hero, notices and scripts stay hand-authored. Today 12 of 113 search descriptions match neither the course `summary` nor `blurb` (9 of 10 Differential Equations courses among them); pick one field. The array builds text nodes, so the generator must write literal characters, not entities. | L | new `scripts/build_index.py` or `build_auth_pages.py`, `.github/workflows/ci.yml`, `site/index.html`, AGENTS.md §0 | ARCH-3, ARCH-4, UX-20 |
| B-12 | P1 | **Card meta line**: courses, lessons, level, and the Subject's `level_note`. All of it already exists in the PATH dicts; free once B-11 lands. | S after B-11 | catalog, generator | UX-4, ARCH-12 |
| B-13 | P2 | **Link cross-Subject prerequisites.** Differential Equations names four Algebra courses, Algorithms needs Discrete Mathematics in full, Operations Research names both, all as plain prose; no Subject page links another. Add an optional `assumes_subjects` key, render it as links in the Assumes tile and on the home card, and render the reverse ("Used by …") on the prerequisite's page. | M | `render.py::path_page`, `content/*/__init__.py`, `tests/content_preservation.json` (regenerate with `/usr/bin/python3`) | UX-7, UX-15 |
| B-14 | P2 | **Shrink the wiring checklist** in AGENTS.md §0: the home card, search array and auth-page rebuild become "add one catalog entry". | S | `AGENTS.md` | ARCH-9 |
| B-15 | P3 | **Derive hard-coded counts** (113 courses, 105 generated, "twelve" in several tests and docs) from the catalog, keeping one deliberate total as a tripwire. | S-M | `tests/test_course_ui.py`, `tests/test_site_invariants.py`, `tests/test_public_copy.py` | ARCH-18 |

### Inside Subjects and courses

| id | pri | item | effort | touches | source |
|---|---|---|---|---|---|
| B-16 | P2 | **Label the course pager by dependency.** Both previous and next say "Related course" (`render.py:397,404`), so the reader cannot tell what this course builds on from what builds on it. Use "Builds on" and "Used by", which the no-numbering rule allows. | S | `render.py`, Trading via `intake_course.build_pager`, pager tests | UX-13 |
| B-17 | P2 | **Show order inside a Subject without numbers**: a "builds on <previous>" line per course card (first card "assumes nothing"), and on desktop a single-column spine or level bands, so the 2-column row-major grid stops hiding the sequence. | M | `render.py::path_page`, shared stylesheet, `tests/test_course_ui.py`, `tests/test_responsive_ui.py` | UX-14 |
| B-18 | P2 | **Replace "Format: Interactive" on course homes** with Level (every course is interactive by construction, so the tile says nothing). | S | `render.py::course_page`, `intake_course.py`, course-home tests | UX-12 |
| B-19 | P2 | **Bring Trading's Subject page to the generated template**: the same four stats (Courses, Lessons, Level, Assumes), per-course level chips, progress rings, a `sequence_intro`. Through `add_progress_marks.py`, never by hand, since Trading pages are the source. | M | `site/paths/trading/index.html`, `scripts/add_progress_marks.py` | UX-11, ARCH-13 |
| B-20 | P3 | **"In this Subject" strip on course homes**: the sibling courses, current one highlighted, with progress ticks, so a reader arriving from search sees where the course sits. | S | `render.py::course_page`, Trading homes | UX-25 |
| B-21 | P3 | **Sibling-Subject links on Subject pages** ("Goes well with …"), from the B-13 graph, so moving between Subjects does not mean returning to the home page. | S after B-13 | `render.py::path_page` | UX-15 |

### Naming, display-only

| id | pri | item | effort | touches | source |
|---|---|---|---|---|---|
| B-22 | P2 | **Drop "Read Along" from the displayed Subject name** on cards via the catalog's `short_title` ("Capital", "Phenomenology of Perception") and show "Read along" as the eyebrow. Leave `PATH["title"]` alone: it feeds ~200 breadcrumbs and the test inventory. Deciding to change breadcrumbs too is a separate, larger item. | S | catalog, home page | UX-8, ARCH-11 |
| B-23 | P3 | **One level scale.** Ten Subjects use Beginner/Intermediate/Advanced ranges; English says "Foundational" and Trading declares none. Make English "Beginner" and give Trading a value. | S | `content/english/__init__.py`, Trading stub, preservation fixtures | UX-19 |
| B-24 | P3 | **"Subject" everywhere in copy.** Subject-page footers still say "on this path" while the home page bans the word. Reword the eleven `material` clauses (URLs stay `/paths/`). | S | `content/*/__init__.py`, `TestGeneratedPathIsCurrent`, `test_public_copy` | UX-24 |
| B-25 | P3 | **Crumb root and nav agree**: the crumb says "Learn library", the nav says "Subjects", for the same destination. | S | `chrome.py`, `intake_course.py`, Trading pages, crumb tests | UX-27 |
| B-26 | P3 | **Write the slug rule for future Subjects** in AGENTS.md §1a: new Subjects prefix course slugs with the Subject's short name (Capital, Phenomenology and Reading Faster already do; `dynamic-programming` and `dynamic-programming-and-sequential-decisions` show why). Rename nothing that exists. | S | `AGENTS.md` | UX-9, ARCH-10 |

## Not recommended

- **Renaming any published URL** (course slugs, `/paths/discrete-math/`,
  `/paths/phenomenology/`) for consistency. Costs in "Constraints" above; the
  benefit is cosmetic.
- **Reordering `GENERATED_PATHS` to set display order.** It works, but it mixes
  what is published with how it is presented. Use the catalog (B-8).
- **Unifying course title grammar across Subjects** (noun pairs, chapter titles,
  imperatives). Each is right within its Subject; search already shows the
  Subject next to every title.

## Suggested first slice

B-1, B-2, B-3 and B-4 together are one small PR that answers the complaint
today. B-8 should follow before the next Subject is wired, or the new card is
appended last and the problem returns.
