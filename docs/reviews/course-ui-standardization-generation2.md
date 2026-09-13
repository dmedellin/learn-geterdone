# Course UI: second review remediation

This generation restores domain explanations and removes the reproduced curriculum cues while retaining **Learn library → Subject → Course → Lesson**. It changes no public URL or file inventory under `site/`. All 378 published files remain, including the same 369 HTML pages and nine non-HTML assets.

## Identity and authority

Before any edit, a single verification process read branch/HEAD/tree, read tracked and untracked status, and reread the identities. Both reads matched branch `review/course-ui-standardization`, rejected HEAD `3e1a3a028346054246f46e67b5ea48600c70015d`, tree `1d420aac5b4421bafc42d2210a5997f86abf1570`, with empty status. Original base remains `57788539d7463f4c5cd640e2571f3c40a9630750`.

The root agent was the sole writer. Three agents provided read-only content, guard, and taxonomy/scope audits. Root and scoped AGENTS files and applicable agent notes were read; the user's narrower scope governed. The exact-review JSON, delegation summary, and existing review document were treated as evidence. The incorrect tree mentioned in the older delegation evidence was not used.

## Repairs and source owners

- `content/`: 29 modules restore full explanations, prerequisites and boundaries, exact fraction/integer behavior, factoring rationale, adversarial practice, proof limitations, and named factual dependencies. The complete base-to-rejected inventory is 53 modules; the other 24 were audited and retained because their neutral edits preserve the teaching. Equally likely finite-outcome qualification and the corrected Sequences and Series reference remain.
- `scripts/add_progress_marks.py`: owns all Trading repairs, including normalized and pristine legacy inputs. It removes 37 Stage ordinals while preserving Lesson ranges, rewrites nine grouping passages grammatically, corrects the two specialized planning introductions, neutralizes four route-like hero illustrations, and fixes accessibility/fallback/capstone taxonomy. Course topic plots and Options' STRIKE annotation remain. The actual automation execution pipeline remains a legitimate domain diagram.
- `site/index.html`: owns the library's no-script Subject wording.
- `scripts/build_paths.py`: unchanged owner used to regenerate 54 mathematics pages. The sanctioned Trading normalizer changed 11 pages. Together with the index, 66 HTML files change. Independent diff inspection found identical CSS, JavaScript, and navigation/resource/form URLs across all 66; all 464 paragraphs on the eight Trading homes remain.
- Tests: the CSS evaluator supports static `:is`, `:where`, and `:not` with nested lists, combinators and correct specificity. The premium fixture executes the shipped rendering function against deterministic UI scenarios; arithmetic and chart drawing are stubbed, not reimplemented.

The interactive inventory is reusable in the independent browser via `learnInteractiveTargets.inventory(document)` from `tests/interactive_targets.js`. It enumerates links, buttons, every non-hidden input type, textareas, selects, summaries, interactive roles, focusable nodes and editable content, including dynamically created controls. It returns the control, associated labels, candidate hit-area owners and disabled state. Checkbox/radio labels are alternate owners; sliders remain their own manipulation targets. The next browser harness must inspect actual visibility, measure owners and exercise controls after each interaction. No native-input sizing was changed.

## Complete content-preservation contract

`tests/content_preservation.json` explicitly lists all 53 source modules, their immutable-base AST hashes, expected full AST hashes, and 453 exact approved changed/restored strings. AST serialization explicitly retains empty fields, avoiding Python 3.14 default-format drift; the same 53 hashes pass on Python 3.12 and 3.14. A fixed empty-field fingerprint failed RED before that portability fix. AST hashing protects all string/numeric values and structure while ignoring formatting/comments. Exact clauses provide readable diagnostics. The test discovers every module under every registered generated Subject and requires exact inventory equality, so omitting a module cannot pass. It does not depend on historical Git objects in a shallow checkout. A separate writer audit verified all 53 baseline hashes against the immutable base and the full base-to-rejected changed-module set.

Every row below is covered. **Restored** identifies a second-generation source repair; **Preserved** identifies a reviewed module whose rejected-generation neutral edit already retained substantive content.

| Module | Review outcome |
| --- | --- |
| `content/algebra/__init__.py` | Restored |
| `content/algebra/c1_foundations/__init__.py` | Restored |
| `content/algebra/c1_foundations/part_a.py` | Preserved |
| `content/algebra/c1_foundations/part_b.py` | Preserved |
| `content/algebra/c2_equations/__init__.py` | Restored |
| `content/algebra/c2_equations/part_a.py` | Preserved |
| `content/algebra/c2_equations/part_b.py` | Preserved |
| `content/algebra/c3_functions/__init__.py` | Restored |
| `content/algebra/c3_functions/part_a.py` | Preserved |
| `content/algebra/c3_functions/part_b.py` | Preserved |
| `content/algebra/c4_polynomials/__init__.py` | Restored |
| `content/algebra/c4_polynomials/part_a.py` | Preserved |
| `content/algebra/c4_polynomials/part_b.py` | Preserved |
| `content/algebra/c5_rational/__init__.py` | Restored |
| `content/algebra/c5_rational/part_a.py` | Preserved |
| `content/algebra/c5_rational/part_b.py` | Preserved |
| `content/algebra/c6_quadratics/__init__.py` | Restored |
| `content/algebra/c6_quadratics/part_a.py` | Restored |
| `content/algebra/c6_quadratics/part_b.py` | Preserved |
| `content/algebra/c7_exponentials/__init__.py` | Restored |
| `content/algebra/c7_exponentials/part_a.py` | Preserved |
| `content/algebra/c7_exponentials/part_b.py` | Restored |
| `content/algebra/c8_systems/__init__.py` | Restored |
| `content/algebra/c8_systems/part_a.py` | Preserved |
| `content/algebra/c8_systems/part_b.py` | Restored |
| `content/algebra/c9_sequences/__init__.py` | Restored |
| `content/algebra/c9_sequences/part_a.py` | Restored |
| `content/algebra/c9_sequences/part_b.py` | Restored |
| `content/discrete_math/__init__.py` | Restored |
| `content/discrete_math/c1_logic/__init__.py` | Restored |
| `content/discrete_math/c1_logic/part_a.py` | Preserved |
| `content/discrete_math/c1_logic/part_b.py` | Preserved |
| `content/discrete_math/c2_sets/__init__.py` | Restored |
| `content/discrete_math/c2_sets/part_a.py` | Preserved |
| `content/discrete_math/c2_sets/part_b.py` | Preserved |
| `content/discrete_math/c3_induction/__init__.py` | Restored |
| `content/discrete_math/c3_induction/part_a.py` | Restored |
| `content/discrete_math/c3_induction/part_b.py` | Preserved |
| `content/discrete_math/c4_counting/__init__.py` | Restored |
| `content/discrete_math/c4_counting/part_a.py` | Preserved |
| `content/discrete_math/c4_counting/part_b.py` | Preserved |
| `content/discrete_math/c5_probability/__init__.py` | Restored |
| `content/discrete_math/c5_probability/part_a.py` | Restored |
| `content/discrete_math/c5_probability/part_b.py` | Preserved |
| `content/discrete_math/c6_number_theory/__init__.py` | Restored |
| `content/discrete_math/c6_number_theory/part_a.py` | Preserved |
| `content/discrete_math/c6_number_theory/part_b.py` | Preserved |
| `content/discrete_math/c7_graphs/__init__.py` | Restored |
| `content/discrete_math/c7_graphs/part_a.py` | Restored |
| `content/discrete_math/c7_graphs/part_b.py` | Restored |
| `content/discrete_math/c8_algorithms/__init__.py` | Restored |
| `content/discrete_math/c8_algorithms/part_a.py` | Restored |
| `content/discrete_math/c8_algorithms/part_b.py` | Preserved |

## RED → GREEN and negative proofs

The first focused runs preceded implementation changes in each reproduced class. The initial exploratory run also exposed a test fixture function-name typo; it was fixed before the definitive RED run. Logs preserve failures rather than reclassifying them as passes.

- Content: rejected sources failed the complete contract; all 53 modules now pass. Mutations omit each of the 53 module entries and remove an actual approved string from each corresponding source in memory. Both inventory and semantic/phrase assertions bite.
- Taxonomy/planning: rejected output failed the complete visitor scan and course-specific planning checks. Planted instances cover all six measured phrases as normal text, accessibility attributes and no-script alternatives. A hidden referenced accessible name also failed RED before reference resolution was added.
- Heroes/source ownership: the rejected Market Structure illustration failed. An original-base automation hero exposed a legacy-tail escape and failed before its owner was fixed. Eight checksummed baseline SVG fixtures now protect legacy normalization without requiring Git history in CI. The highlighted-endpoint mutation also fails its intended assertion.
- Premium: the original defective markup failed the persistent-legend assertion. The rejected generation's existing repair passes four deterministic scenarios, including zero/tiny proportions. Seven mutations detect removal, movement into a bar, lost decorative semantics, hidden labels, direct/ancestor textContent overwrites, and omitted numeric updates. No premium product code needed changing.
- Functional selectors: the rejected parser ignored the functional override and failed four focused cases. Static nested matching/specificity now passes; an appended live `:is(.math, .absent)` nowrap override fails the real published math assertion.
- Catalog-order regression: restored prerequisite explanations exposed the old guard using first mentions anywhere on a page. The canonical suite failed two Subject subtests. Two focused RED tests also showed that correctly ordered cards could fail while reordered cards could pass. The guard now reads actual catalog cards and checks their order, titles and destinations; all three planted defects are rejected.
- Interactive inventory: absence of the owner failed RED. Nine Node fixtures cover native types, radio despite its absence from current pages, label ownership and dynamic button-role cells. Mutations remove input selection and label ownership. Naming assertions reject empty and dangling associations.

Complete mutation results: **140/140 new review mutations**, plus **26/26 existing UI**, **5/5 progress**, and **16/16 responsive** mutations: **187/187 total**. Mutations use temporary copies or memory; they leave the worktree inputs untouched.

## Visitor-text inventory and domain exceptions

The complete scanner covers all 369 HTML pages, not only the 366 shared families. It parses visible-source text, no-script alternatives, titles/metadata, accessible attributes and referenced accessible names. Comments, script/style bodies, identifiers and URL attributes do not enter the stream. CSS-dependent visibility and geometry are outside this source contract.

After regeneration, all six reproduced classes have zero matches: Stage N of M; START HERE; After the eight courses; Educational path; Open a path; last thing this path asks. Adjacent Course stages/path-position/numbered-waypoint/public-path identity checks also have zero matches.

The complete lexical inventory is retained at `/tmp/learn-remediation-generation2/visible-matches.json`, with each page, term and context. It contains 170 `path`, 88 `paths`, 22 `stage`, and 19 `stages` matches on 55 pages; no `progression` or `sequencing`. These remain graph/lattice/shortest paths, price/equity/Monte Carlo histories, execution/recursive paths, and arithmetic/proof/counting/procedural stages. Counts include visually rendered aria-hidden text and accessible ID references, so they are deliberately broader than the independent agent's accessibility-only census. Neutral numbered Lesson lists and previous/next Lesson navigation remain.

## Commands and observed results

Verification commands ran under `PYTHONDONTWRITEBYTECODE=1`, `PYTHONPATH=tests`, with `/usr/bin/python3` for Python, except the explicitly named Python 3.12 portability check. Suites were serialized. The machine-readable command ledger and full stdout/stderr logs are retained in `/home/dmedellin/.hermes/evidence/learn-ui-remediation-generation2-20260906/` (the execution originals are under `/tmp/learn-remediation-generation2/commands.jsonl`); the table lists every recorded execution, including failed attempts. Source preparation and read-only inspection commands are described below; they do not imply a test pass.

| Log | Exact command | Exit | Observed result |
| --- | --- | ---: | --- |
| `001.log` | `/usr/bin/python3 -m unittest test_review_remediation -v` | 1 | Ran 5 tests in 4.085s; FAILED (failures=6, errors=1) |
| `002.log` | `/usr/bin/python3 -m unittest test_review_remediation -v` | 1 | Ran 6 tests in 4.028s; FAILED (failures=7) |
| `003.log` | `/usr/bin/python3 -m unittest test_review_remediation.TestFunctionalSelectors -v` | 0 | Ran 1 test in 0.001s; OK |
| `004.log` | `/usr/bin/python3 -m unittest test_review_remediation.TestInteractiveInventory -v` | 1 | Ran 2 tests in 3.545s; FAILED (failures=1) |
| `005.log` | `/usr/bin/python3 -c "import subprocess, unittest; from test_review_remediation import check_premium; check_premium(unittest.TestCase(), subprocess.check_output(['git','show','57788539:site/options-trading/option-premium/index.html'],text=True))"` | 1 |     raise self.failureException(msg); AssertionError: 1 != 0 : persistent premium legend |
| `006.log` | `/usr/bin/python3 tests/mutate_review_remediation.py --premium-only` | 1 |            ^^^^^^^^^^^^^^^^^^^^^; AssertionError: ('label moved inside narrow bar', "'true' == 'true' : premium labels accessible") |
| `007.log` | `/usr/bin/python3 tests/mutate_review_remediation.py --premium-only` | 0 | 7/7 review mutations caught; worktree inputs untouched. |
| `008.log` | `/usr/bin/python3 -c "from pathlib import Path; import json; root=Path('/tmp/learn-remediation-generation2/draft'); files=json.loads(Path('tests/content_preservation.json').read_text())['modules']; changed=[f for f in files if (root/f).read_bytes()!=Path(f).read_bytes()]; [(Path(f).write_bytes((root/f).read_bytes())) for f in changed]; print(len(changed),'content modules restored from reviewed draft')"` | 0 | 29 content modules restored from reviewed draft |
| `009.log` | `/usr/bin/python3 -m unittest test_review_remediation.TestReviewRemediation.test_topic_illustrations_have_no_highlighted_curricular_endpoint -v` | 1 | Ran 1 test in 0.010s; FAILED (failures=1) |
| `010.log` | `/usr/bin/python3 scripts/build_paths.py` | 0 | 237 generated pages in total; wrote 54 page(s), 183 already current |
| `011.log` | `/usr/bin/python3 scripts/add_progress_marks.py` | 0 | 130 page(s) visited, 11 rewritten. |
| `012.log` | `/usr/bin/python3 -m unittest test_review_remediation test_responsive_ui -v` | 0 | Ran 14 tests in 44.984s; OK |
| `013.log` | `/usr/bin/python3 -m unittest test_course_ui -v` | 0 | Ran 22 tests in 55.663s; OK |
| `014.log` | `/usr/bin/python3 -m unittest test_review_remediation.TestReviewRemediation.test_domain_exceptions_and_text_boundaries -v` | 1 | Ran 1 test in 0.002s; FAILED (failures=1) |
| `015.log` | `/usr/bin/python3 -m unittest test_review_remediation.TestReviewRemediation.test_legacy_hero_normalization_preserves_domain_and_is_neutral -v` | 1 | Ran 1 test in 4.852s; FAILED (failures=1) |
| `016.log` | `/usr/bin/python3 scripts/add_progress_marks.py` | 0 | 130 page(s) visited, 3 rewritten. |
| `017.log` | `/usr/bin/python3 -m unittest test_review_remediation -v` | 0 | Ran 11 tests in 13.446s; OK |
| `018.log` | `/usr/bin/python3 tests/mutate_review_remediation.py` | 0 | 137/137 review mutations caught; worktree inputs untouched. |
| `019.log` | `/usr/bin/python3 tests/mutate_course_ui.py` | 0 | 26/26 UI guard mutations caught; worktree inputs untouched.; 5/5 progress UI mutations caught; worktree inputs untouched.; 16/16 responsive mutations caught; worktree inputs untouched. |
| `020.log` | `/usr/bin/python3 /tmp/learn-remediation-report-data.py` | 0 | 53/53 immutable-base content contracts verified; all 378 public files retained; protected sources and non-HTML assets unchanged |
| `021.log` | `/usr/bin/python3 -m unittest discover -s tests -v` | 1 | Ran 133 tests in 183.304s; FAILED (failures=2) |
| `022.log` | `/usr/bin/python3 scripts/build_paths.py --check` | 0 | 237 generated pages in total |
| `023.log` | `/usr/bin/python3 -m unittest test_review_remediation.TestCatalogOrderGuard -v` | 1 | Ran 2 tests in 0.003s; FAILED (failures=2) |
| `024.log` | `/usr/bin/python3 -m unittest test_review_remediation.TestCatalogOrderGuard test_site_invariants.TestPathPage -v` | 0 | Ran 6 tests in 1.708s; OK |
| `025.log` | `/usr/bin/python3 tests/mutate_review_remediation.py` | 0 | 140/140 review mutations caught; worktree inputs untouched. |
| `026.log` | `/usr/bin/python3 -m unittest discover -s tests -v` | 0 | Ran 135 tests in 171.188s; OK |
| `027.log` | `/usr/bin/python3 -m unittest test_review_remediation.TestReviewRemediation.test_content_fingerprint_keeps_empty_fields_across_python_versions -v` | 1 | Ran 1 test in 0.001s; FAILED (failures=1) |
| `028.log` | `/usr/bin/python3 -m unittest test_review_remediation.TestReviewRemediation.test_content_fingerprint_keeps_empty_fields_across_python_versions test_review_remediation.TestReviewRemediation.test_all_generated_content_is_preserved -v` | 0 | Ran 2 tests in 0.429s; OK |
| `029.log` | `python3.12 -m unittest test_review_remediation.TestReviewRemediation.test_content_fingerprint_keeps_empty_fields_across_python_versions test_review_remediation.TestReviewRemediation.test_all_generated_content_is_preserved -v` | 0 | Ran 2 tests in 0.449s; OK |
| `030.log` | `/usr/bin/python3 tests/mutate_review_remediation.py` | 0 | 140/140 review mutations caught; worktree inputs untouched. |
| `031.log` | `/usr/bin/python3 -m unittest discover -s tests -v` | 0 | Ran 136 tests in 170.358s; OK |
| `032.log` | `/usr/bin/python3 scripts/build_paths.py` | 0 | 237 generated pages in total; wrote 0 page(s), 237 already current |
| `033.log` | `/usr/bin/python3 scripts/build_paths.py --check` | 0 | 237 generated pages in total |
| `034.log` | `/usr/bin/python3 scripts/add_progress_marks.py` | 0 | 130 page(s) visited, 0 rewritten. |
| `035.log` | `node scripts/mathcheck.js` | 0 | every arithmetic assertion passes |
| `036.log` | `node scripts/labcheck.js --generated` | 0 | 237 page(s) executed, 0 failing |
| `037.log` | `node scripts/progresscheck.js` | 0 | all checks passed |
| `038.log` | `node scripts/feedbackcheck.js` | 0 | all checks passed |
| `039.log` | `/usr/bin/python3 scripts/validate_release_contract.py --schema release/contract.schema.json --github release/contract.json release/contract.example.json` | 0 | release/contract.json: valid against release/contract.schema.json; release/contract.example.json: valid against release/contract.schema.json |
| `040.log` | `WEB_ROOT=site GITHUB_OUTPUT=/tmp/learn-remediation-generation2/workflow/github-output bash /tmp/learn-remediation-generation2/workflow/01.sh` | 0 | Web root: site |
| `041.log` | `WEB_ROOT=site GITHUB_OUTPUT=/tmp/learn-remediation-generation2/workflow/github-output bash /tmp/learn-remediation-generation2/workflow/02.sh` | 0 | Published URL space: 369/369 pages plus 8 assets present under site. |
| `042.log` | `WEB_ROOT=site GITHUB_OUTPUT=/tmp/learn-remediation-generation2/workflow/github-output bash /tmp/learn-remediation-generation2/workflow/07.sh` | 0 | hvn-lvn/index.html: 235 element(s) checked, 0 error(s); site/volume-and-order-flow/volume-and-order-flow-trading-rules/index.html: 240 element(s) checked, 0 error(s); site/volume-and-order-flow/volume-confirmation/index.html: 235 element(s) checked, 0 error(s); site/volume-and-order-flow/volume-fundamentals/index.html: 232 element(s) checked, 0 error(s); site/volume-and-order-flow/volume-profile/index.html: 235 element(s) checked, 0 error(s); site/volume-and-order-flow/volume-weighted-average-price/index.html: 240 element(s) checked, 0 error(s) |
| `043.log` | `WEB_ROOT=site GITHUB_OUTPUT=/tmp/learn-remediation-generation2/workflow/github-output bash /tmp/learn-remediation-generation2/workflow/08.sh` | 0 | ::notice file=site/volume-and-order-flow/volume-weighted-average-price/index.html,line=725::reviewed outbound link: https://learn.geterdone.io; Self-containment: 375 file(s) scanned, 0 violation(s), 529 reviewed outbound link(s). |
| `044.log` | `WEB_ROOT=site GITHUB_OUTPUT=/tmp/learn-remediation-generation2/workflow/github-output bash /tmp/learn-remediation-generation2/workflow/09.sh` | 0 | Link check: 369 page(s), 0 error(s). |
| `045.log` | `WEB_ROOT=site GITHUB_OUTPUT=/tmp/learn-remediation-generation2/workflow/github-output bash /tmp/learn-remediation-generation2/workflow/11.sh` | 0 | ::notice::hadolint not available on this runner; running the built-in Containerfile checks only. |
| `046.log` | `WEB_ROOT=site GITHUB_OUTPUT=/tmp/learn-remediation-generation2/workflow/github-output bash /tmp/learn-remediation-generation2/workflow/12.sh` | 0 | Shared-private-edge contract verified: platform-private-edge 10.89.2.22:8080. |
| `047.log` | `WEB_ROOT=site GITHUB_OUTPUT=/tmp/learn-remediation-generation2/workflow/github-output bash /tmp/learn-remediation-generation2/workflow/14.sh` | 0 | No credential-shaped files tracked. |
| `048.log` | `git diff --check` | 0 |  |
| `049.log` | `/usr/bin/python3 /tmp/learn-remediation-report-data.py` | 0 | 53/53 immutable-base content contracts verified; all 378 public files retained; protected sources and non-HTML assets unchanged |

Preparation/inspection commands (all local): `git symbolic-ref --short HEAD`, `git rev-parse HEAD`, `git rev-parse HEAD^{tree}`, and `git status --porcelain=v1 --untracked-files=all` inside the identity verifier (exit 0); `rg --files`/`rg -n`, `cat`, targeted `sed -n`, `wc`, `git diff --stat/--numstat/--name-only`, and targeted `git show` reads for the instructions, evidence, content diffs, normalizer, tests, heroes and workflow (successful reads, with expected no-match rg exit 1). The first bounded file search also excluded generated HTML. No full generated lesson, release manifest, or invariant-test module was dumped.

Writer helpers retained in `/tmp`: `content-delta.py` enumerated all changed metadata strings (exit 0); `prepare-content-remediation.py` prepared 53 contracts and 29 source drafts before source edits (exit 0); `fix-responsive-parser.py` applied the reviewed parser (exit 0); `polish-content-remediation.py` applied seven explicit grammar/neutrality corrections to sources and their contracts (exit 0); `learn-remediation-report-data.py` verified 53 immutable-base contracts and 378 retained public files (recorded above); `learn-remediation-workflow.py` extracted and syntax-checked all 14 exact workflow blocks (exit 0). Other edits used explicit patches or short checked replacement scripts. `command -v gitleaks`, `gitleaks version`, and `gitleaks git --help` confirmed installed version 8.30.1 (exit 0). No dependencies were installed.

The exact workflow scripts and SHA-256 inventory are retained under `/tmp/learn-remediation-generation2/workflow/`. Arithmetic, progress, feedback, generated labs, canonical unittest and release-contract steps reuse their separately recorded equivalent executions; the remaining eight checked-in run blocks execute directly with `WEB_ROOT=site` and a temporary `GITHUB_OUTPUT`.

## Exact changed-file inventory

All file changes belong to the source owners above. The complete list follows; no route/asset was added, removed, renamed or redirected.

- `content/algebra/__init__.py`
- `content/algebra/c1_foundations/__init__.py`
- `content/algebra/c2_equations/__init__.py`
- `content/algebra/c3_functions/__init__.py`
- `content/algebra/c4_polynomials/__init__.py`
- `content/algebra/c5_rational/__init__.py`
- `content/algebra/c6_quadratics/__init__.py`
- `content/algebra/c6_quadratics/part_a.py`
- `content/algebra/c7_exponentials/__init__.py`
- `content/algebra/c7_exponentials/part_b.py`
- `content/algebra/c8_systems/__init__.py`
- `content/algebra/c8_systems/part_b.py`
- `content/algebra/c9_sequences/__init__.py`
- `content/algebra/c9_sequences/part_a.py`
- `content/algebra/c9_sequences/part_b.py`
- `content/discrete_math/__init__.py`
- `content/discrete_math/c1_logic/__init__.py`
- `content/discrete_math/c2_sets/__init__.py`
- `content/discrete_math/c3_induction/__init__.py`
- `content/discrete_math/c3_induction/part_a.py`
- `content/discrete_math/c4_counting/__init__.py`
- `content/discrete_math/c5_probability/__init__.py`
- `content/discrete_math/c5_probability/part_a.py`
- `content/discrete_math/c6_number_theory/__init__.py`
- `content/discrete_math/c7_graphs/__init__.py`
- `content/discrete_math/c7_graphs/part_a.py`
- `content/discrete_math/c7_graphs/part_b.py`
- `content/discrete_math/c8_algorithms/__init__.py`
- `content/discrete_math/c8_algorithms/part_a.py`
- `docs/reviews/course-ui-standardization-generation2.md`
- `scripts/add_progress_marks.py`
- `site/algebra-foundations/index.html`
- `site/algorithmic-and-automated-trading/index.html`
- `site/algorithms-and-complexity/index.html`
- `site/algorithms-and-complexity/searching-and-sorting/index.html`
- `site/backtesting-and-trading-systems/index.html`
- `site/combinatorics-and-counting/index.html`
- `site/discrete-probability/computing-probabilities/index.html`
- `site/discrete-probability/index.html`
- `site/exponential-and-logarithmic-functions/change-of-base/index.html`
- `site/exponential-and-logarithmic-functions/common-and-natural-logarithms/index.html`
- `site/exponential-and-logarithmic-functions/compound-interest-and-continuous-growth/index.html`
- `site/exponential-and-logarithmic-functions/exponential-functions/index.html`
- `site/exponential-and-logarithmic-functions/growth-and-decay/index.html`
- `site/exponential-and-logarithmic-functions/index.html`
- `site/exponential-and-logarithmic-functions/logarithmic-functions-and-their-graphs/index.html`
- `site/exponential-and-logarithmic-functions/logarithmic-scales/index.html`
- `site/exponential-and-logarithmic-functions/solving-exponential-equations/index.html`
- `site/exponential-and-logarithmic-functions/solving-logarithmic-equations/index.html`
- `site/exponential-and-logarithmic-functions/the-laws-of-logarithms/index.html`
- `site/exponential-and-logarithmic-functions/the-number-e/index.html`
- `site/exponential-and-logarithmic-functions/what-a-logarithm-is/index.html`
- `site/graphs-and-trees/graph-colouring/index.html`
- `site/graphs-and-trees/graphs-and-graph-models/index.html`
- `site/graphs-and-trees/index.html`
- `site/index.html`
- `site/induction-and-recursion/index.html`
- `site/induction-and-recursion/recursive-definitions/index.html`
- `site/linear-equations-and-inequalities/index.html`
- `site/lines-functions-and-graphs/index.html`
- `site/logic-and-proof/conditional-statements/index.html`
- `site/logic-and-proof/contraposition-and-contradiction/index.html`
- `site/logic-and-proof/direct-proof/index.html`
- `site/logic-and-proof/index.html`
- `site/logic-and-proof/logical-connectives/index.html`
- `site/logic-and-proof/logical-equivalence/index.html`
- `site/logic-and-proof/negating-quantified-statements/index.html`
- `site/logic-and-proof/nested-quantifiers/index.html`
- `site/logic-and-proof/normal-forms-and-boolean-algebra/index.html`
- `site/logic-and-proof/predicates-and-quantifiers/index.html`
- `site/logic-and-proof/proof-by-cases-and-counterexample/index.html`
- `site/logic-and-proof/propositions-and-truth-values/index.html`
- `site/logic-and-proof/rules-of-inference/index.html`
- `site/logic-and-proof/tautologies-and-satisfiability/index.html`
- `site/logic-and-proof/truth-tables/index.html`
- `site/market-structure/index.html`
- `site/number-theory-and-cryptography/index.html`
- `site/options-trading/index.html`
- `site/paths/algebra/index.html`
- `site/paths/discrete-math/index.html`
- `site/paths/trading/index.html`
- `site/paths/trading/iren-analysis-2026-08-16/index.html`
- `site/paths/trading/iren-analysis-2026-08-16/slides/index.html`
- `site/polynomials-and-factoring/index.html`
- `site/quadratics-and-complex-numbers/complex-numbers/index.html`
- `site/quadratics-and-complex-numbers/index.html`
- `site/rational-and-radical-expressions/index.html`
- `site/sequences-and-series/index.html`
- `site/sequences-and-series/sequences-and-recursion/index.html`
- `site/sequences-and-series/the-general-term-of-an-expansion/index.html`
- `site/sets-relations-functions/index.html`
- `site/systems-and-matrices/index.html`
- `site/systems-and-matrices/systems-of-inequalities-and-linear-programming/index.html`
- `site/technical-indicators/index.html`
- `site/trade-setup-execution/index.html`
- `site/trading-risk-management/index.html`
- `site/volume-and-order-flow/index.html`
- `tests/content_preservation.json`
- `tests/interactive_targets.js`
- `tests/legacy_course_heroes.json`
- `tests/mutate_review_remediation.py`
- `tests/premium_labels.js`
- `tests/test_responsive_ui.py`
- `tests/test_review_remediation.py`
- `tests/test_site_invariants.py`

## Limits and handoff

No source blocker remains. The final canonical run passed 136 tests; all 187 mutations were caught. Both generators were current (zero rewrites); arithmetic passed, 237 generated labs ran, progress passed 44 checks, feedback passed 41 checks, and both release contracts validated. HTML/link/self-containment and static deployment-input gates passed. Two existing environment/workflow notices remain: hadolint is unavailable, so the workflow used its built-in lint; the unchanged allocation block ends its Python heredoc at EOF and emits a warning while passing. Release/workflow files were not edited.

These are source, semantic, runtime-UI-fixture and mutation results, not browser geometry. Inheritance, pseudo states, intrinsic sizes, line boxes, clipping, rendered visibility and target rectangles remain the fresh exact-commit browser process's responsibility. Mixed selector functions containing unsupported pseudo states are explicitly excluded by this limited evaluator. The final container and all-route Chromium matrix were not built/run in this writer session.

Release/deployment files, route files, authentication/storage contracts, progress semantics, feedback behavior and lab arithmetic remain unchanged. No credentials or production/private data were read. No push, PR, merge, deploy, or external-system action occurred. The older evidence package's missing security-scan reference was not rewritten; this candidate has its own local scan records. Final commit identity, parent, tree, cleanliness and exact candidate-range scan are recorded in the immutable-commit handoff outside this file to avoid self-reference.
