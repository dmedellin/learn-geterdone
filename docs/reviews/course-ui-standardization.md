# Course UI and taxonomy standardization

## Baseline and scope

- Branch: `review/course-ui-standardization`.
- Starting commit: `57788539d7463f4c5cd640e2571f3c40a9630750`.
- Starting tree: `4253209e051586d064223015835d42291e0a39e1`.
- Branch, HEAD, tree and clean tracked/untracked status were asserted before editing.
- Advisory audit read first: `/home/dmedellin/.hermes/evidence/learn-ui-codex/audit.last.md`; its event record and `/home/dmedellin/.hermes/evidence/learn-ui-live/` were inspected. Findings below were checked against the baseline sources, rather than accepted from screenshots alone.
- Root, `tests/`, `scripts/mathpath/`, `content/` and `.github/` instructions were read. No `scripts/AGENTS.md` or scoped documentation instructions exist.
- One writer modified this worktree. Two agents provided read-only content and source reviews.
- The parent's baseline result of 95 tests in 70.527 seconds is supplied evidence; this implementation did not rerun that canonical suite.

All current routes and assets are retained. `/paths/…/` remains a URL and internal identifier. No release, routing, CSP, authentication, analytics, storage-key, schema, lab implementation, arithmetic or asset manifest is changed. The two dated Trading capstone documents keep their specialized layouts; their existing shared style/sign-in injection is refreshed by the sanctioned patcher. They are not course or lesson families.

## Verified findings and decisions

The baseline index called subjects paths, displayed subject totals, and exposed course positions in search results. Trading subjects and course homes used different catalog and header structures from generated mathematics. Generated homes explicitly rendered course positions, an ordered syllabus claim and a first-lesson action. Generated lesson breadcrumbs omitted the subject. Progress counted subjects, numbered courses, described marks as finished courses, and carried an Algebra-specific footer clause.

The implementation uses the literal hierarchy **Learn library → Subject → Course → Lesson**. Course titles replace curricular numbered references. Authored display order remains, with title-only optional sibling links labelled “Related course”; the terminal link is “All [Subject] courses”. Lesson previous/next links remain neutral. Catalog totals count courses or lessons; subjects themselves are not counted or numbered. Recommended background names concepts. The generated “Check your understanding” heading retains the lesson's criterion.

Source ownership remains explicit:

- Mathematics copy lives in `content/`; chrome lives in `scripts/mathpath/`; `scripts/build_paths.py` writes its 237 pages.
- Trading HTML remains authored source. `scripts/add_progress_marks.py` is the sole bulk normalization path. Its one-time catalog migration recognizes legacy structures; subsequent runs preserve authored catalog prose. It derives its inventory from the published catalog, preflights all 118 lessons before writing, preserves authored scripts/hero controls, and is byte-idempotent. Unknown structures fail before any page is written.
- `site/index.html` owns the library and its inline search data/renderer.
- `scripts/build_auth_pages.py` owns the progress and callback pages. Changes are limited to shared chrome, labels and presentation; authentication and synchronization logic remain intact.

## Shared page-family contract

Every requested page has a single `main#main`, an accessible skip link, a shared masthead and footer, a literal page kind, and an unnumbered identity. The masthead order is Learn → Subjects/Courses/Progress → Sign in/theme. The brand's accessibility name is “Learn library”; the theme control retains “Toggle light and dark theme”. Breadcrumbs name all ancestors and the current page, with the subject included on every lesson.

| Family | Required ordered regions after the masthead |
| --- | --- |
| Library | Hero, subjects, course search |
| Subject | Breadcrumbs, hero, factual metadata, overview, course list, recommended background |
| Course | Breadcrumbs, hero, factual metadata, overview, lesson list, recommended background, optional related-course navigation |
| Lesson | Breadcrumbs, hero, preserved teaching/lab, completion mark, lesson navigation, feedback |
| Progress | Breadcrumbs, hero, factual mark totals, course lists grouped under linked subject names |

A shared inline CSS block specifies a 1160px maximum shell with 16px side gutters, system typography, boxed heroes, 14–18px card/hero radii, common spacing, surfaces and action styles. Hero lead text has a 65-character measure; prose is limited to 72 characters. At 720px, catalog/navigation grids collapse and the header places utilities beside the brand with navigation below. Shared actions and reset controls have at least 44px targets. Legacy Trading palette names are bridged to canonical surface/border tokens; accent ink follows the existing theme background without adding duplicate light-theme declarations. Course-specific diagrams, labs and hero controls remain in their authored containers.

The chosen 1160px width is an implementation decision; the advisory audit's proposed width was not treated as a product mandate. Desktop 1440×900 and mobile 390×844 rendered acceptance, both themes, overflow, content measure and touch usability remain the parent's explicit verification responsibility. The matrix below reports source/semantic contract checks, not browser acceptance.

## Finding ledger

| Finding | Status | Resolution or ownership |
| --- | --- | --- |
| Paths/subject totals/course ordinals in UI and search | Resolved | Named subjects/courses; inline result renderer executed in a Node fixture |
| Conflicting headers, breadcrumbs and page identity | Resolved | Shared masthead, literal kind and complete ancestor trail |
| Catalog/order/prerequisite copy | Resolved | Factual overview and recommended concepts; optional title-only sibling links |
| Completion heading and progress vocabulary | Resolved | Understanding criterion retained; readable completion states; neutral aggregate footer |
| Legacy Trading structure and source ownership | Resolved | Sanctioned, preflighted migration; authored copy persistence and pristine-layout fixtures |
| Broad Trading replacement altered execution-path wording | Resolved | Restored baseline inputs; shell-scoped taxonomy plus explicit numbered curricular references |
| Double-escaped inventory titles and repeated footer names | Resolved | Decode inventory once; remove footer ordinal prefix before resolving titles |
| First-pass progress-toggle non-idempotence | Resolved | Accept original and annotated toggle containers; pristine fixtures and repeat run |
| Legacy color tokens and small reset controls | Resolved | Theme-aware token bridge and 44px shared sizing |
| Completion label outside Trading card padding | Resolved | Label inside the existing card content; no whitespace residue |
| Taxonomy guard missed adjacent elements | Resolved | Visible-text boundaries; factual totals explicitly distinguished from ordinals |
| Stale Algebra numbered reference after course split | Resolved | Constant-ratio sequence follow-up names Sequences and Series; topical regression guard |
| `build_paths.py --check` allegedly mutates progress | Resolved by measured verification | Direct implementation inspection found writes guarded by `not args.check`; final tracked-byte assertion checks the actual execution, including import effects |
| Canonical suite, workflow checks, served smoke, responsive browser acceptance, security scan and exact-tree review | Pending parent acceptance | Explicitly reserved by the implementation brief; not claimed as passed here |

No requested implementation family is omitted. Pending parent acceptance is not an implementation exception.

## Legitimate domain exceptions

“Path” remains valid in graph paths, shortest paths, execution workflows, filesystem paths, URL slugs and internal identifiers. The authored Trading headings “Keep the trading path explicit” and the security lesson's “normal trading path is unreliable” describe execution workflows and are preserved. Graph-theory path lessons and their controls remain unchanged.

“Sequence” remains valid for mathematical sequences and series, operation ordering, proof steps, algorithms, event/order processing and procedural instructions inside a lesson. The subject route `/paths/`, internal `PATH`/`GENERATED_PATHS`, CSS class names such as `spine`, and stored inventory field names remain compatibility details, not visible taxonomy. Neutral numbered lesson lists and previous/next lesson controls describe the available lessons without prescribing completion.

## Generated course verification matrix

The generated inventory below covers all 25 course homes and all 336 lessons. “Pass” means the published semantic contract is present and the focused UI suite passed. Visual acceptance remains pending with the parent.

| Subject | Course | Home | Lesson family |
| --- | --- | --- | --- |
| Trading | Market Structure | Pass | Pass (7/7) |
| Trading | Trade Setup and Execution | Pass | Pass (15/15) |
| Trading | Options Trading | Pass | Pass (16/16) |
| Trading | Technical Indicators | Pass | Pass (16/16) |
| Trading | Volume and Order Flow | Pass | Pass (16/16) |
| Trading | Trading Risk Management | Pass | Pass (16/16) |
| Trading | Backtesting and Trading Systems | Pass | Pass (16/16) |
| Trading | Algorithmic and Automated Trading | Pass | Pass (16/16) |
| Discrete Mathematics | Logic and Proof | Pass | Pass (14/14) |
| Discrete Mathematics | Sets, Relations, and Functions | Pass | Pass (14/14) |
| Discrete Mathematics | Induction and Recursion | Pass | Pass (12/12) |
| Discrete Mathematics | Combinatorics and Counting | Pass | Pass (14/14) |
| Discrete Mathematics | Discrete Probability | Pass | Pass (12/12) |
| Discrete Mathematics | Number Theory and Cryptography | Pass | Pass (14/14) |
| Discrete Mathematics | Graphs and Trees | Pass | Pass (14/14) |
| Discrete Mathematics | Algorithms and Complexity | Pass | Pass (12/12) |
| Algebra | Foundations of Algebra | Pass | Pass (13/13) |
| Algebra | Linear Equations and Inequalities | Pass | Pass (13/13) |
| Algebra | Lines, Functions and Graphs | Pass | Pass (14/14) |
| Algebra | Polynomials and Factoring | Pass | Pass (13/13) |
| Algebra | Rational and Radical Expressions | Pass | Pass (12/12) |
| Algebra | Quadratics and Complex Numbers | Pass | Pass (14/14) |
| Algebra | Exponential and Logarithmic Functions | Pass | Pass (12/12) |
| Algebra | Systems and Matrices | Pass | Pass (10/10) |
| Algebra | Sequences and Series | Pass | Pass (11/11) |

Generated using the published inventory in `test_site_invariants.PATHS`, reading each declared course/lesson page with the `Elements` parser in `tests/test_course_ui.py`. The independent page-family guard covers 366 requested pages (library, subjects, courses, lessons and progress).

## Verification performed

All verification ran in the foreground. No full canonical suite, workflow-equivalent run, served smoke, browser acceptance, production access, push, PR, deployment or credential access was performed.

Commands below used `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tests` for Python checks. Times are measured process elapsed seconds; unittest-reported test times are quoted separately. Retained detailed logs are under `/tmp/learn-ui-*.log` in this workspace session. The durable results are recorded here.

| Command actually run | Exit | Exact result | Elapsed |
| --- | ---: | --- | ---: |
| `/usr/bin/python3 scripts/add_progress_marks.py` | 0 | 130 page(s) visited, 74 rewritten. | 10.786s |
| `/usr/bin/python3 scripts/add_progress_marks.py` | 0 | 130 page(s) visited, 0 rewritten. | 10.620s |
| `/usr/bin/python3 scripts/build_paths.py` | 0 | wrote 37 page(s), 200 already current | 0.521s |
| `/usr/bin/python3 scripts/build_auth_pages.py` | 0 | wrote site/oauth2/spa/callback/index.html (55231 bytes); wrote site/progress/index.html (103065 bytes) | 0.253s |
| `/usr/bin/python3 -m unittest test_course_ui -v` | 1 | Ran 22 tests in 53.847s; FAILED (failures=2) | 54.210s |
| `/usr/bin/python3 -m unittest test_site_invariants.TestPinnedConventions test_site_invariants.TestCourseContext test_site_invariants.TestSharedChromeIsSubjectAgnostic test_site_invariants.TestChromeRendersWhatItMeans test_site_invariants.TestContent.test_course_pages_retain_the_disclaimer test_site_invariants.TestGeneratedPathIsCurrent test_site_invariants.TestLessonDataMatchesTheRenderer -v` | 1 | Ran 30 tests in 20.415s; FAILED (failures=336) | 20.678s |
| `/usr/bin/python3 -m unittest test_course_ui -v` | 0 | Ran 22 tests in 51.223s; OK | 51.566s |
| `/usr/bin/python3 -m unittest test_site_invariants.TestPinnedConventions test_site_invariants.TestCourseContext test_site_invariants.TestSharedChromeIsSubjectAgnostic test_site_invariants.TestChromeRendersWhatItMeans test_site_invariants.TestContent.test_course_pages_retain_the_disclaimer test_site_invariants.TestGeneratedPathIsCurrent test_site_invariants.TestLessonDataMatchesTheRenderer -v` | 0 | Ran 30 tests in 19.643s; OK | 19.894s |
| `node scripts/mathcheck.js` | 0 | every arithmetic assertion passes | 17.735s |
| `node scripts/labcheck.js --generated` | 0 | 237 page(s) executed, 0 failing | 2.240s |
| `node scripts/progresscheck.js` | 0 | all checks passed | 0.379s |
| `node scripts/feedbackcheck.js` | 0 | all checks passed | 0.755s |
| `/usr/bin/python3 tests/mutate_course_ui.py` | 0 | 26/26 UI guard mutations caught; worktree inputs untouched.; 5/5 progress UI mutations caught; worktree inputs untouched. | 57.914s |
| `/usr/bin/python3 scripts/build_paths.py` | 0 | wrote 1 page(s), 236 already current | 0.498s |
| `/usr/bin/python3 -m unittest test_course_ui.TestVisitorTaxonomy test_course_ui.TestPublishedUI test_course_ui.TestGeneratedLessonUI -v` | 0 | Ran 6 tests in 7.832s; OK | 8.197s |
| `/usr/bin/python3 scripts/build_paths.py --check` + tracked snapshot assertion | 0 | 237 pages current; 537 tracked files byte/mode-identical; `TRACKED_DRIFT=[]`; `STATUS_UNCHANGED=True` | 0.786s |

The tracked snapshot included every tracked file’s mode and SHA-256, plus `git status --porcelain=v1 -z`. Before and after digest: `d23c06383d1428c535d1886dbcbb81e8b21f58b8e006d0a2daa340dd6342eef3`. This is measured non-mutation; a printed passing message alone was not accepted.

The first final UI pass exposed two false positives for the legitimate “Courses 8” catalog total after improving text-node boundaries. Both guards now distinguish factual counts from curricular identity. The first convention pass exposed the former verbatim pager tag; its pinned constant now includes `data-ui="lesson-navigation"`, retaining the exact class, accessible label and uniqueness requirement. Intake imports that same constant.

### RED → GREEN record

Each row names the focused command target actually exercised with `/usr/bin/python3 -m unittest TARGET -v`, under the environment above; the first hierarchy check was invoked with `unittest discover -s tests -p test_course_ui.py -v`. The progress row used `node scripts/progresscheck.js`. Every RED below exited 1. Every test is green in the 22-test UI run, subsequent 6-test copy pass, or 30-test convention run; the progress assertions are green in the final Node run.

| RED log suffix | Focused target | Observed RED result |
| --- | --- | --- |
| `01` | `test_course_ui.TestGeneratedLessonUI.test_lesson_hierarchy` | Ran 1 test in 0.161s; FAILED (failures=18) |
| `02` | `test_course_ui.TestSharedMasthead.test_navigation_and_control_order` | Ran 1 test in 0.001s; FAILED (failures=1) |
| `03` | `test_course_ui.TestGeneratedLessonUI.test_understanding_and_terminal_navigation` | Ran 1 test in 0.009s; FAILED (failures=1) |
| `03b` | `test_course_ui.TestGeneratedLessonUI.test_understanding_and_terminal_navigation` | Ran 1 test in 0.010s; FAILED (failures=1) |
| `04` | `test_course_ui.TestGeneratedCatalogUI.test_course_overview_has_factual_identity_and_optional_navigation` | Ran 1 test in 0.080s; FAILED (failures=17) |
| `04b` | `test_course_ui.TestGeneratedCatalogUI.test_course_overview_has_factual_identity_and_optional_navigation` | Ran 1 test in 0.083s; FAILED (failures=13) |
| `05` | `test_course_ui.TestGeneratedCatalogUI.test_subject_catalog_has_unnumbered_courses` | Ran 1 test in 0.007s; FAILED (failures=1) |
| `06` | `test_course_ui.TestTradingNormalization.test_lesson_shell_preserves_instruction_and_is_idempotent` | Ran 1 test in 1.869s; FAILED (failures=118) |
| `07` | `test_course_ui.TestTradingNormalization.test_failed_preflight_writes_nothing` | Ran 1 test in 4.733s; FAILED (failures=1) |
| `08` | `test_course_ui.TestTradingNormalization.test_course_and_subject_catalog_contract` | Ran 1 test in 5.264s; FAILED (failures=9) |
| `09` | `test_course_ui.TestLibraryUI.test_library_browses_subjects_and_search_reports_subject_names` | Ran 1 test in 0.014s; FAILED (failures=1) |
| `10` | `node scripts/progresscheck.js` | 5 UI checks failed; exit 1 |
| `11` | `test_course_ui.TestMarkLabels.test_course_marks_have_readable_state` | Ran 1 test in 0.045s; FAILED (failures=1) |
| `12` | `test_course_ui.TestPublishedUI.test_every_page_family_exposes_the_shared_contract` | Ran 1 test in 3.202s; FAILED (failures=1) |
| `13` | `test_course_ui.TestVisitorTaxonomy.test_published_copy_uses_subjects_and_course_titles` | Ran 1 test in 3.272s; FAILED (failures=1) |
| `14` | `test_course_ui.TestTradingIntakeUI.test_intake_breadcrumb_and_terminal_return` | Ran 1 test in 0.093s; FAILED (failures=1) |
| `15` | `test_course_ui.TestTradingNormalization.test_incomplete_inventory_is_rejected_before_transformation` | Ran 1 test in 0.055s; FAILED (failures=1) |
| `16` | `test_course_ui.TestLibraryUI.test_library_browses_subjects_and_search_reports_subject_names` | Ran 1 test in 0.062s; FAILED (failures=1) |
| `17` | `test_course_ui.TestPublishedUI.test_every_page_family_exposes_the_shared_contract` | Ran 1 test in 2.924s; FAILED (failures=1) |
| `18` | `test_course_ui.TestTradingNormalization.test_legacy_shells_preserve_domain_copy_and_hero_controls` | Ran 1 test in 0.021s; FAILED (failures=1) |
| `18b` | `test_course_ui.TestTradingNormalization.test_legacy_shells_preserve_domain_copy_and_hero_controls` | Ran 1 test in 0.043s; FAILED (failures=1) |
| `19` | `test_course_ui.TestTradingNormalization.test_authored_inventory_names_are_decoded_once` | Ran 1 test in 0.002s; FAILED (failures=1) |
| `20` | `test_course_ui.TestTradingNormalization.test_normalized_catalog_prose_remains_authored` | Ran 1 test in 0.181s; FAILED (failures=1) |
| `21` | `test_course_ui.TestTradingNormalization.test_published_trading_names_are_literal` | Ran 1 test in 0.547s; FAILED (failures=1) |
| `22` | `test_course_ui.TestTradingNormalization.test_legacy_palette_and_hero_controls_support_shared_styles` | Ran 1 test in 0.151s; FAILED (failures=8) |
| `22b` | `test_course_ui.TestTradingNormalization.test_legacy_palette_and_hero_controls_support_shared_styles` | Ran 1 test in 0.199s; FAILED (failures=4) |
| `23` | `test_course_ui.TestTradingNormalization.test_trading_lesson_state_is_inside_the_card_content` | Ran 1 test in 0.001s; FAILED (failures=1) |
| `23b` | `test_course_ui.TestTradingNormalization.test_trading_lesson_state_is_inside_the_card_content` | Ran 1 test in 0.002s; FAILED (failures=1) |
| `24` | `test_course_ui.TestPublishedUI.test_every_page_family_exposes_the_shared_contract` | Ran 1 test in 3.446s; FAILED (failures=1) |
| `25` | `test_course_ui.TestVisitorTaxonomy.test_visible_copy_separates_adjacent_elements` | Ran 1 test in 0.001s; FAILED (failures=1) |
| `26` | `test_course_ui.TestVisitorTaxonomy.test_generated_cross_references_use_titles_and_topics` | Ran 1 test in 0.057s; FAILED (failures=1) |
| `26b` | `test_course_ui.TestVisitorTaxonomy.test_generated_cross_references_use_titles_and_topics` | Ran 1 test in 0.019s; FAILED (failures=1) |
| `26d` | `test_course_ui.TestVisitorTaxonomy.test_generated_cross_references_use_titles_and_topics` | Ran 1 test in 0.048s; FAILED (failures=1) |
| `conventions-final` | `test_site_invariants.TestPinnedConventions.test_every_lesson_carries_the_pinned_pager_markup` | 336 expected mismatches against the former pager tag; 30 tests in 20.415s; exit 1 |

The first RED hierarchy sweep reports 18 failures: 17 course subtests plus its non-empty coverage assertion. Trading’s first shell sweep reports 118 failing lessons. Later fixtures specifically reject domain-copy damage, loss of hero/reset controls, second-pass drift, premature writes, double escaping, duplicate identity, overwritten authored catalog copy, misplaced completion labels, missing color tokens, duplicate theme declarations and a wrong sequence-course reference.

### Earlier focused attempts

This table preserves intermediate outcomes, including unsuccessful attempts with filenames containing “green”. The filename is not treated as a result. Targets are the unittest cases named by their logs; generation and Node commands are shown explicitly.

| Log | Command / target | Exit | Result |
| --- | --- | ---: | --- |
| `learn-ui-auth-build-01.log` | `/usr/bin/python3 scripts/build_auth_pages.py` | 1 | NameError: name 'canonical_path' is not defined |
| `learn-ui-auth-build-02.log` | `/usr/bin/python3 scripts/build_auth_pages.py` | 0 | wrote site/oauth2/spa/callback/index.html (54876 bytes); wrote site/progress/index.html (102726 bytes) |
| `learn-ui-build-01.log` | `/usr/bin/python3 scripts/build_paths.py` | 0 | 237 generated pages in total; wrote 237 page(s), 0 already current |
| `learn-ui-build-02.log` | `/usr/bin/python3 scripts/build_paths.py` | 0 | 237 generated pages in total; wrote 148 page(s), 89 already current |
| `learn-ui-build-03.log` | `/usr/bin/python3 scripts/build_paths.py` | 0 | 237 generated pages in total; wrote 237 page(s), 0 already current |
| `learn-ui-build-04.log` | `/usr/bin/python3 scripts/build_paths.py` | 0 | 237 generated pages in total; wrote 237 page(s), 0 already current |
| `learn-ui-context-guards.log` | `/usr/bin/python3 -m unittest test_site_invariants.TestCourseContext test_site_invariants.TestSharedChromeIsSubjectAgnostic test_site_invariants.TestPathPage -v` | 0 | Ran 11 tests in 5.328s; OK |
| `learn-ui-focused-01.log` | `/usr/bin/python3 -m unittest test_course_ui -v` | 0 | Ran 19 tests in 46.501s; OK |
| `learn-ui-green-01.log` | `/usr/bin/python3 -m unittest test_course_ui.TestGeneratedLessonUI.test_lesson_hierarchy -v` | 0 | Ran 1 test in 0.147s; OK |
| `learn-ui-green-02.log` | `/usr/bin/python3 -m unittest test_course_ui.TestSharedMasthead.test_navigation_and_control_order -v` | 0 | Ran 1 test in 0.001s; OK |
| `learn-ui-green-03.log` | `/usr/bin/python3 -m unittest test_course_ui.TestGeneratedLessonUI.test_understanding_and_terminal_navigation -v` | 0 | Ran 1 test in 0.010s; OK |
| `learn-ui-green-04.log` | `/usr/bin/python3 -m unittest test_course_ui.TestGeneratedCatalogUI.test_course_overview_has_factual_identity_and_optional_navigation -v` | 0 | Ran 1 test in 0.081s; OK |
| `learn-ui-green-05.log` | `/usr/bin/python3 -m unittest test_course_ui.TestGeneratedCatalogUI.test_subject_catalog_has_unnumbered_courses -v` | 0 | Ran 1 test in 0.011s; OK |
| `learn-ui-green-06.log` | `/usr/bin/python3 -m unittest test_course_ui.TestTradingNormalization.test_lesson_shell_preserves_instruction_and_is_idempotent -v` | 0 | Ran 1 test in 9.636s; OK |
| `learn-ui-green-07.log` | `/usr/bin/python3 -m unittest test_course_ui.TestTradingNormalization.test_failed_preflight_writes_nothing -v` | 0 | Ran 1 test in 4.660s; OK |
| `learn-ui-green-08.log` | `/usr/bin/python3 -m unittest test_course_ui.TestTradingNormalization.test_course_and_subject_catalog_contract -v` | 0 | Ran 1 test in 7.107s; OK |
| `learn-ui-green-09.log` | `/usr/bin/python3 -m unittest test_course_ui.TestLibraryUI.test_library_browses_subjects_and_search_reports_subject_names -v` | 0 | Ran 1 test in 0.050s; OK |
| `learn-ui-green-10.log` | `node scripts/progresscheck.js` | 0 | ; all checks passed |
| `learn-ui-green-11.log` | `/usr/bin/python3 -m unittest test_course_ui.TestMarkLabels.test_course_marks_have_readable_state -v` | 0 | Ran 1 test in 0.090s; OK |
| `learn-ui-green-12.log` | `/usr/bin/python3 -m unittest test_course_ui.TestPublishedUI.test_every_page_family_exposes_the_shared_contract -v` | 0 | Ran 1 test in 3.633s; OK |
| `learn-ui-green-13.log` | `/usr/bin/python3 -m unittest test_course_ui.TestVisitorTaxonomy.test_published_copy_uses_subjects_and_course_titles -v` | 0 | Ran 1 test in 3.293s; OK |
| `learn-ui-green-14.log` | `/usr/bin/python3 -m unittest test_course_ui.TestTradingIntakeUI.test_intake_breadcrumb_and_terminal_return -v` | 0 | Ran 1 test in 0.089s; OK |
| `learn-ui-green-15.log` | `/usr/bin/python3 -m unittest test_course_ui.TestTradingNormalization.test_incomplete_inventory_is_rejected_before_transformation -v` | 0 | Ran 1 test in 0.014s; OK |
| `learn-ui-green-16.log` | `/usr/bin/python3 -m unittest test_course_ui.TestLibraryUI.test_library_browses_subjects_and_search_reports_subject_names -v` | 0 | Ran 1 test in 0.075s; OK |
| `learn-ui-green-18.log` | `/usr/bin/python3 -m unittest test_course_ui.TestTradingNormalization.test_legacy_shells_preserve_domain_copy_and_hero_controls -v` | 0 | Ran 1 test in 0.084s; OK |
| `learn-ui-green-18b.log` | `/usr/bin/python3 -m unittest test_course_ui.TestTradingNormalization.test_legacy_shells_preserve_domain_copy_and_hero_controls -v` | 0 | Ran 1 test in 0.079s; OK |
| `learn-ui-green-19.log` | `/usr/bin/python3 -m unittest test_course_ui.TestTradingNormalization.test_authored_inventory_names_are_decoded_once -v` | 0 | Ran 1 test in 0.001s; OK |
| `learn-ui-green-20.log` | `/usr/bin/python3 -m unittest test_course_ui.TestTradingNormalization.test_normalized_catalog_prose_remains_authored -v` | 0 | Ran 1 test in 0.174s; OK |
| `learn-ui-green-22.log` | `/usr/bin/python3 -m unittest test_course_ui.TestTradingNormalization.test_legacy_palette_and_hero_controls_support_shared_styles -v` | 0 | Ran 1 test in 0.148s; OK |
| `learn-ui-green-22b.log` | `/usr/bin/python3 -m unittest test_course_ui.TestTradingNormalization.test_legacy_palette_and_hero_controls_support_shared_styles -v` | 0 | Ran 1 test in 0.196s; OK |
| `learn-ui-green-23.log` | `/usr/bin/python3 -m unittest test_course_ui.TestTradingNormalization.test_trading_lesson_state_is_inside_the_card_content -v` | 0 | Ran 1 test in 0.001s; OK |
| `learn-ui-green-23b.log` | `/usr/bin/python3 -m unittest test_course_ui.TestTradingNormalization.test_trading_lesson_state_is_inside_the_card_content -v` | 0 | Ran 1 test in 0.002s; OK |
| `learn-ui-green-25.log` | `/usr/bin/python3 -m unittest test_course_ui.TestVisitorTaxonomy.test_published_copy_uses_subjects_and_course_titles -v` | 1 | Ran 2 tests in 4.548s; FAILED (failures=1) |
| `learn-ui-green-25b.log` | `/usr/bin/python3 -m unittest test_course_ui.TestVisitorTaxonomy.test_visible_copy_separates_adjacent_elements -v` | 0 | Ran 1 test in 0.000s; OK |
| `learn-ui-green-26.log` | `/usr/bin/python3 -m unittest test_course_ui.TestVisitorTaxonomy.test_generated_cross_references_use_titles_and_topics -v` | 0 | Ran 1 test in 0.047s; OK |
| `learn-ui-green-26b.log` | `/usr/bin/python3 -m unittest test_course_ui.TestVisitorTaxonomy.test_generated_cross_references_use_titles_and_topics -v` | 1 | Ran 1 test in 0.027s; FAILED (failures=1) |
| `learn-ui-green-26c.log` | `/usr/bin/python3 -m unittest test_course_ui.TestVisitorTaxonomy.test_generated_cross_references_use_titles_and_topics -v` | 0 | Ran 1 test in 0.052s; OK |
| `learn-ui-mutations-01.log` | `/usr/bin/python3 tests/mutate_course_ui.py` | 1 | AssertionError: mutation was not caught by an assertion: published taxonomy[] |
| `learn-ui-mutations-02.log` | `/usr/bin/python3 tests/mutate_course_ui.py` | 1 | AssertionError: mutation was not caught by an assertion: subject context[(<test_site_invariants.TestCourseContext testMethod=test_every_course_home_declares_subject_and_page_kind>, |
| `learn-ui-mutations-03.log` | `/usr/bin/python3 tests/mutate_course_ui.py` | 0 | CAUGHT Trading lesson parity: 'lesson' != 'module'; 25/25 UI guard mutations caught; worktree inputs untouched. |
| `learn-ui-obsolete-position.log` | `/usr/bin/python3 -m unittest test_site_invariants.TestPathPosition -v (former contract)` | 1 | Ran 3 tests in 1.656s; FAILED (failures=25) |
| `learn-ui-progress-mutations.log` | `/usr/bin/python3 tests/mutate_course_ui.py --progress-only` | 0 | CAUGHT progress: subject headings link to subject courses; 5/5 progress UI mutations caught; worktree inputs untouched. |
| `learn-ui-trading-build-01.log` | `/usr/bin/python3 scripts/add_progress_marks.py` | 0 | Trading path: 8 courses, 118 lessons now tickable.; 130 page(s) visited, 130 rewritten. |
| `learn-ui-trading-build-02.log` | `/usr/bin/python3 scripts/add_progress_marks.py` | 0 | Trading path: 8 courses, 118 lessons now tickable.; 130 page(s) visited, 118 rewritten. |
| `learn-ui-trading-build-03.log` | `/usr/bin/python3 scripts/add_progress_marks.py` | 0 | Trading path: 8 courses, 118 lessons now tickable.; 130 page(s) visited, 72 rewritten. |
| `learn-ui-trading-build-04.log` | `/usr/bin/python3 scripts/add_progress_marks.py` | 0 | Trading path: 8 courses, 118 lessons now tickable.; 130 page(s) visited, 127 rewritten. |
| `learn-ui-trading-build-05.log` | `/usr/bin/python3 scripts/add_progress_marks.py` | 0 | Trading path: 8 courses, 118 lessons now tickable.; 130 page(s) visited, 130 rewritten. |
| `learn-ui-trading-build-06.log` | `/usr/bin/python3 scripts/add_progress_marks.py` | 1 | ValueError: missing palette token --line-strong |
| `learn-ui-trading-build-07.log` | `/usr/bin/python3 scripts/add_progress_marks.py` | 0 | Trading path: 8 courses, 118 lessons now tickable.; 130 page(s) visited, 130 rewritten. |
| `learn-ui-trading-build-08.log` | `/usr/bin/python3 scripts/add_progress_marks.py` | 0 | Trading path: 8 courses, 118 lessons now tickable.; 130 page(s) visited, 8 rewritten. |
| `learn-ui-trading-build-09.log` | `/usr/bin/python3 scripts/add_progress_marks.py` | 0 | Trading path: 8 courses, 118 lessons now tickable.; 130 page(s) visited, 8 rewritten. |

The mutation runner initially exposed the adjacent-element blind spot. Its next attempt caught a runner setup error: it invoked a class-based invariant without `setUpClass`; the runner now uses `unittest.TestSuite`. Neither was accepted as a passing mutation check. A later complete run caught all 26 Python/UI mutations and all five Node progress mutations. Mutations use temporary file copies or temporary in-memory mocks, never the published worktree.

The earlier auth build failed on an undefined local variable introduced during this refactor; it was corrected before subsequent successful builds. The first restored Trading run rejected a legacy slide palette without `--line2` during preflight; the bridge now uses its existing `--line`, and no staged migration output was written on that failed pass.

### Review and final checks

- Complete diff scope was reviewed through every source/script/test change, structured content comparisons and full-page-family coverage, without dumping generated HTML. A read-only reviewer independently accounted for every changed HTML file and compared Trading IDs, SVGs and authored scripts to the baseline.
- 369 HTML files: 237 mathematics outputs, 129 sanctioned Trading outputs, two auth/progress outputs and the authored index. All published non-HTML assets and JSON files remain unchanged. No protected release, infrastructure, lab arithmetic or build-registration file changed.
- Matrix generation and report assembly: `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=tests /usr/bin/python3 /tmp/learn-ui-report.py` (exit 0).
- Final drift assertion command: `/usr/bin/python3 /tmp/learn-ui-check-drift.py` (exit 0); this invokes the explicit generated check and compares the tracked snapshots described above.
- A final copy-only follow-up made the sequence-course reference a direct factual description. The generator changed one page; all six relevant published taxonomy, page-family and lesson-criterion tests then passed. Lab/arithmetic/auth code did not change after their successful checks.
- `git diff --check`: exit 0; no output.


Changed-path accounting: **191 source, 4 test, 239 generated, 1 docs; 435 total**. Source includes 130 authored HTML pages, 53 content modules and 8 source scripts. Test includes the three test artifacts and `scripts/progresscheck.js`. Generated includes 237 mathematics pages and two auth/progress pages. No deleted or renamed path.

## Responsive remediation of frozen candidate `13ba6d4`

The parent tested exact commit `13ba6d48d528825d9e6db95314844bb5dfd42105` in Chrome 140.0.7339.207 over CDP with touch emulation, served at `http://127.0.0.1:18080`. The read-only evidence is `/home/dmedellin/.hermes/evidence/learn-ui-candidate/responsive-browser.jsonl` and `course-contract-matrix.json` in the same directory. These are **pre-fix measurements**, retained as failures; the earlier semantic matrix and declaration checks did not establish responsive browser acceptance.

| Observed failure at `13ba6d4` | Systemic remediation | Verification status |
| --- | --- | --- |
| Across all 336 lesson routes, document overflow affected 62 at 390×844 and 114 at 320×800. `/logic-and-proof/proof-by-cases-and-counterexample/` measured 627px scroll width against 390px client width, with uncontained inline math. | `.math` now uses normal whitespace and emergency wrapping for long tokens. Unicode text remains selectable; `.mathblock` retains local horizontal scrolling and preserved expression lines. No global overflow masking was added. | Published cascade guard passes; post-fix CDP pending. |
| Mobile masthead Sign in anchors were approximately 38–40px wide by 44px high. The earlier statement about 44px targets was incomplete: height passed, width did not. | The shared masthead rule now also sets `min-width: 44px`, overriding both legacy widths in effective sizing. The compact mobile treatment and accessible Sign in label remain. | Published anchor sizing contract passes for both source families; post-fix CDP pending. |
| At 768×1024, `/market-structure/` had a 753px client width and 351.5px cards. The legacy 760px media rule placed a fixed 296px thumbnail beside the text; the lesson body reached x816.02 beyond the card's x737 right edge and was clipped. | Each shared course step is a named inline-size container. At a card width of 560px or less, its card stacks and its thumbnail returns to automatic width with the bottom divider restored. Wider desktop cards retain the authored row and 296px thumbnail; card clipping remains intentional. This applies to all eight Trading course homes. | Cascade checks cover media boundaries, the 753px client-width case, and desktop rows; post-fix CDP pending. |

Only `scripts/mathpath/theme.py` changed implementation behavior. Its shared CSS is consumed by `scripts/build_paths.py`, `scripts/add_progress_marks.py`, and `scripts/build_auth_pages.py`; all published changes came from those canonical generators/normalizer. An exact before/after substitution check verified that all 369 changed HTML files differ only by these shared CSS changes. Public routes, filenames, markup, scripts, authored content, and **Learn library → Subject → Course → Lesson** remain unchanged.

`tests/test_responsive_ui.py` reads actual published elements and their ancestor selectors through the existing comment-stripping/nesting-aware CSS helpers. It resolves the supported component declarations using specificity, source order, `!important`, media width and named container width. It is a deterministic CSS contract, **not a browser layout engine**: intrinsic text widths, line boxes, inherited styles, interactive pseudo states and rendered clipping remain outside its proof. The new guards were run before the source fix and failed on all three intended defects. During guard development, media whitespace handling, capstone capability scope and the preserved stacking below the legacy desktop breakpoint were corrected before accepting a green result.

Focused verification in this remediation used `/usr/bin/python3`, with `PYTHONDONTWRITEBYTECODE=1` and `PYTHONPATH=tests` for unittest commands:

| Command | Observed result |
| --- | --- |
| `/usr/bin/python3 -m unittest test_responsive_ui -v` before source changes | 3 tests, 3 intended failures: nowrap math, horizontal narrow card, undersized Sign in width. |
| `/usr/bin/python3 scripts/build_paths.py` | 237 pages written. |
| `/usr/bin/python3 scripts/add_progress_marks.py` | 130 pages visited and rewritten; second run visited 130 and rewrote 0. |
| `/usr/bin/python3 scripts/build_auth_pages.py` | Callback and progress pages regenerated. |
| `/usr/bin/python3 scripts/build_paths.py --check` | Every published generated page matches its content. |
| `/usr/bin/python3 -m unittest test_responsive_ui -v` after regeneration | 3 tests passed in 13.291s. |
| `/usr/bin/python3 tests/mutate_course_ui.py --responsive-only` | All 11 mutations caught by their intended assertions, on temporary copies: nowrap, unbreakable tokens, block clipping, global masking, both legacy anchor widths, anchor height, tablet row, fixed thumbnail, missing query ancestor, and lost desktop row. |
| `/usr/bin/python3 -m unittest test_course_ui.TestPublishedUI test_course_ui.TestVisitorTaxonomy.test_published_copy_uses_subjects_and_course_titles test_site_invariants.TestGeneratedPathIsCurrent -v` | 6 tests passed in 7.872s. |
| `node scripts/mathcheck.js` | Every arithmetic assertion passes. |
| `node scripts/labcheck.js --generated` | 237 pages executed, 0 failing. |
| `node scripts/progresscheck.js` and `node scripts/feedbackcheck.js` | All checks passed in both. |

The full unittest suite, container build, final serial gates and post-fix CDP measurements remain with the parent. This remediation does not claim a new overflow count or browser acceptance, and did not push, merge or deploy.
