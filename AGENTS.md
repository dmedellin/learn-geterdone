# Working agreement for learn-geterdone

Read this before changing anything. It is the contract between whoever (human or
agent) edits this repository and the platform that will eventually serve it.

## 0. Nothing is inert any more: all eight Subjects publish

`content/system_design/`, `content/algorithms/` and `content/operations_research/`
were in the tree for months publishing nothing. All three are now in
`GENERATED_PATHS` and all three are live.

| Subject | state |
|---|---|
| System Design | **published** — 10 courses, 114 lessons, wired 2026-09-25 (369 pages became 494) |
| Algorithms | **published** — 9 courses, 112 lessons, wired 2026-09-27 |
| Operations Research | **published** — 10 courses, 92 lessons, wired 2026-09-27 (494 pages became 719) |
| Philosophy | **published** — 10 courses, 108 lessons, 119 pages, wired 2026-10-08 (719 pages became 838) |
| English | **published** — 10 courses, 41 lessons, 52 pages; first wired 2026-10-09 at 4 courses (838 pages became 853), widened by English v2 on 2026-10-10 (853 pages became 890) |

98 lab modes are registered and all eighteen kits in
`build_paths.KITS_WITH_EXPECTATIONS` now serve published pages: `node
scripts/labcheck.js --generated` executes 758 generated pages, 263 of them with
pinned figures, and compares every pinned tile string against what the page
prints. Philosophy's two kits, `argkit` and `choicekit`, account for 98 of those
pages and English's `english` kit for 41.
Before the last two Subjects were wired it said "0 with pinned figures" — those
expectations were written, verified against scratch renders, and then fired
against nothing.

**Wiring a Subject is not a flag flip**, and the next person to do one should
plan for about two dozen declaration sites rather than the four the URL rule in
section 1 names. The list, taken from the two commits that wired System Design
and the one that wired these two:

- `scripts/build_paths.py` (the switch), and then `scripts/generated-pages.txt`
  and `scripts/generated-expectations.json`, which the build rewrites;
- `scripts/smoke.py`, `scripts/canvas_sources.js`;
- `release/contract.json`, `release/contract.example.json` — **both**, the suite
  checks them together — and `release/contract.schema.json`, which pins every
  check id by name and carries a `minItems` that must equal the pin count;
- `Containerfile.release` and `.github/workflows/ci.yml`, whose page
  enumerations are backslash-continued shell word lists (see below);
- `tests/test_site_invariants.py`, `tests/content_preservation.json`,
  `tests/test_review_remediation.py`, `tests/test_public_copy.py`,
  `tests/test_course_ui.py`, `tests/test_canvas_contract.py`,
  `tests/test_browser_source.py`, `tests/test_responsive_ui.py`,
  `tests/test_generation4.py`, `tests/test_generation5_catalog.py`,
  `tests/browser_acceptance.js`, `tests/browser_contrast.js`,
  `tests/browser_interactions.js`;
- `site/index.html`, which is hand-authored and needs a subject card and one
  entry per course in its inline search array — that array builds TEXT NODES, so
  an HTML entity written into it reaches the reader as its own characters;
- `site/progress/index.html` and `site/oauth2/spa/callback/index.html`, which
  embed the library inventory: re-run `scripts/build_auth_pages.py`;
- `content/spoken/<package>.py`, ONE file named for the Subject's package:
  `speechcheck.py` loads exactly that name, so per-course spoken files are
  invisible to it (render.py merges every file in the directory, so they still
  reach the pages and hide the gap). Two files giving one run two readings is a
  `test_speech` failure;
- the shape checks `TestGeneratedPathIsCurrent`, `TestLessonDataMatchesTheRenderer`
  and `TestEveryLabBuilds`, whose import lists name Discrete Mathematics,
  Algebra and Philosophy. Philosophy was added on wiring and the escaped-field
  check immediately found thirteen mistake titles showing `&ldquo;` literally;
  System Design, Algorithms and Operations Research are still not in those lists;
- and this section, section 1, and `README.md`'s URL layout.

Five things that have each cost a day:

1. `content_errors` in `tests/test_review_remediation.py` builds its inventory
   *from* `GENERATED_PATHS` and compares with a SYMMETRIC DIFFERENCE, so joining
   that tuple makes every `.py` file in the package mandatory in
   `tests/content_preservation.json` — no partial option, no warning, and one
   opaque failure line naming all of them. Generate those entries with
   `/usr/bin/python3`; the fingerprint is Python-version sensitive.
2. `test_public_copy` requires a `<subject>_semantic_copy` block per generated
   Subject, whose expected strings are RENDERED text and not source: derive them
   from the built page rather than reimplementing the renderer's escaping.
3. `Containerfile.release`'s enumeration is a backslash-continued list. Ten
   missing trailing backslashes once produced `unknown instruction: done;`, and
   the root cause was reading the shipped block through a width-truncating pipe
   that chopped the backslash. Never inspect that file through `cut -c1-N`.
4. `ci.yml`'s enumeration is also a backslash-continued `for` loop. A YAML
   comment spliced into it is valid YAML and broken bash: the logical line ends
   at the comment and the `for` never reaches its `do`. Do not put a comment
   inside a continued list. `bash -n` every `run:` block before pushing.
5. A release-contract check id is capped at 72 characters by
   `release/contract.schema.json` and by a test. `algebra-course6-lesson-`
   `quadratic-equations-and-the-zero-product-property` is exactly 72. The check
   id prefixes are short for that reason: `math`, `algebra`, `sysdesign`,
   `algo`, `or`, `phil`.

`tests/test_site_invariants.py` checks a Subject's tagline and description
against its own course and lesson counts. Those sentences are written when a
Subject is scaffolded, before a lesson exists, and both of these advertised the
wrong number until the day they were finished.

A course module still being authored exports `COURSE = None`, which
`content/<subject>/__init__.py` filters out. No course is in that state today.

Half-finished lab kits for the last two Subjects were parked, unverified, on
the `wip/or-and-algorithms-kits` branch; they were recovered and are now in
`scripts/mathpath/labs/`. Nothing on `main` depends on that branch.

Seven further Subjects have been proposed and none is scheduled:
[docs/FUTURE-SUBJECTS.md](docs/FUTURE-SUBJECTS.md) records them with the only
question that decides whether each can be built the way this library builds
things — what does the reader compute? For one of them the answer is "nothing",
and that is written down rather than engineered around.

## 1. What this repository is

An educational static site published as **Learn** at `https://learn.geterdone.io`:

The site is a subject-agnostic LIBRARY OF PATHS. A path is an ordered sequence of
courses on one subject. There are eight: **Trading** (8 courses, 118 lessons,
hand-authored and normalized at intake), **Discrete Mathematics** (8 courses, 106
lessons), **Algebra** (9 courses, 112 lessons), **System Design** (10 courses,
114 lessons), **Algorithms** (9 courses, 112 lessons), **Operations Research**
(10 courses, 92 lessons), **Philosophy** (10 courses, 108 lessons) and **English**
(10 courses, 41 lessons) — the last seven GENERATED from `content/<subject>/`. 74
courses and 803 lessons in all. The
published URL space:

| URL | Served from |
| --- | --- |
| `learn.geterdone.io/` | `site/index.html` — the site index: the paths, plus course search |
| `learn.geterdone.io/paths/<subject>/` | `site/paths/<subject>/index.html` — one page per path: `trading`, `discrete-math`, `algebra`, `system-design`, `algorithms`, `operations-research`, `philosophy`, `english` |
| `learn.geterdone.io/<course>/` | `site/<course>/index.html` — one of the 74 course homes |
| `learn.geterdone.io/<course>/<lesson>/` | `site/<course>/<lesson>/index.html` — one of the 803 lessons |

The site index and the path pages are SHARED CHROME: they must not assume the
subject is trading — not in copy, not in a footer, not in metadata. Only course
and lesson pages are subject-specific. A path page is neither a course home nor a
lesson, even though it is two segments deep like a lesson; every guard declares
it separately rather than classifying pages by URL shape.

`site/` is the document root. Whatever `site/` contains is exactly what `/` serves;
an extra directory level in `site/` becomes an extra path segment in the public URL.

The full 890-page map (plus eight published JSON assets) is in
[README.md](README.md#url-layout), and it is enforced in five places that must
agree: `REQUIRED_PAGES` in `tests/test_site_invariants.py`, `scripts/smoke.py`,
`acceptance.checks` in `release/contract.json` (and in
`release/contract.example.json`, which the suite checks beside it), the
"Published URL space is complete" step in `.github/workflows/ci.yml`, and the
publish guard in `Containerfile.release`.

(It was six until `.github/workflows/pages.yml` was removed. That workflow was
a second delivery path to GitHub Pages, it was never how production is served,
and it failed on every push to main because Pages was never enabled on the
repository. Production is the Hetzner container platform and always was.)

Those five govern WHICH URLS EXIST. **Adding or removing a whole Subject is a
bigger change than that**, and the five are not the whole of it: roughly two
dozen files carry a hardcoded count of pages, lessons, courses or Subjects, and
several of the per-path constants in `tests/test_site_invariants.py` and
`scripts/smoke.py` are patterns to extend rather than numbers to bump. Find them
before starting, not one red test at a time.

The one that is invisible until it fires is `content_errors` in
`tests/test_review_remediation.py`. It builds its inventory **from
`GENERATED_PATHS` itself** and compares it to `tests/content_preservation.json`
with a symmetric difference, so the moment a new path joins that tuple, every
`.py` file in its content package becomes mandatory in the preservation
contract, each with an AST fingerprint. There is no "guard the old paths only"
option and nothing warns you. Generate those entries with `/usr/bin/python3`;
the fingerprint is Python-version sensitive and the file carries
`AST_DUMP_OPTIONS` for exactly that reason.

Every lesson carries a completion toggle and a feedback panel, so a lesson page
is also a piece of UI. The trading lessons are hand-written and were given those
controls in place by `scripts/add_progress_marks.py`, which is idempotent and is
the only sanctioned way to edit all 129 trading pages at once.

Three sets of URLs are retired, with no redirect stubs: the seven FLAT lesson URLs
course 1 published first, and the whole `/market-structure-lab/` prefix it used
until the paths layer landed (that slug names the repository and the application,
not the course, so the course took its own name — `/market-structure/`), and
`/systems-matrices-and-sequences/`, retired when that course was split in two.
Breaking all three was accepted deliberately, and no guard, test, or contract may
list them again.

The apex `geterdone.io` is a **separate, live GitHub Pages site that this repository
does not control**. Do not deploy to it, reconfigure it, or write anything that
implies we own its records. Linking to it is fine; changing it is out of scope.

## 1a. One path is authored, six are generated

The paths are built in opposite directions and must be edited differently.

**Trading** arrived as eight hand-authored HTML packages and was normalized INTO
the library's conventions by `scripts/intake_course.py`. Its pages are the source
of truth. Edit them directly.

**Discrete Mathematics**, **Algebra**, **System Design**, **Algorithms**,
**Operations Research**, **Philosophy** and **English** are generated. `content/<subject>/` holds each of them as
data — one Python module per course, with the lessons as dicts — and
`scripts/build_paths.py` renders all 758 of their pages from `scripts/mathpath/`
(one stylesheet, one chrome renderer, one lab kit per subject area). **Never
edit a page under one of those course slugs by hand**: the next build reverts it,
so the change appears to work and then vanishes.

    python3 scripts/build_paths.py                     # rebuild all six 
    python3 scripts/build_paths.py --check             # fail if any page is stale
    node scripts/mathcheck.js                          # check the arithmetic itself
    node scripts/labcheck.js --generated               # execute every lab

The last two are different questions and CI runs both. `labcheck.js` proves each
published lab runs, redraws, and survives its controls being moved: it sweeps
every option of every `<select>`, the two ends and a middle step of every
range, and a handful of hostile strings through every text box, firing each
control's own `change` handler the way a browser does. (Until 2026-09-26 this
sentence said "survives every value of its own controls" and the file did no
such thing -- it ran the page once and called `redrawLab()` once. Three kit
authors noticed independently, each wrote a private sweep, and each threw it
away; the sweep is now in `labcheck.js` and the claim is true. It found a
published page that dies on a typed `1/0`. Pass `--no-sweep` for the old
behaviour.)

It also checks what a preset makes the page PRINT. `build_paths.py` writes
`scripts/generated-expectations.json` — page → `<select>` id → option value →
`{kpi element id: exact text}` — and `labcheck.js` selects each option,
dispatches the change handler and compares `textContent` against it. For a kit
listed in `build_paths.KITS_WITH_EXPECTATIONS` this is a gate: an option with no
expectation fails the page, and so does a preset menu that declares none — which
menus those are is decided by running the page and seeing which `<select>`
rewrites another control, never by reading a name. It exists because a preset's own menu text is prose
that no check can read, and a sweep of fifteen kits found 57 of those strings
false about the lab they described. `greedy.py` is converted; the switch is how
each remaining kit is turned on. `node scripts/labcheck.js --observe <page>`
prints every option's tiles as the page prints them, which is how the figures
are read.

`mathcheck.js` proves the arithmetic those labs are built on is right, by
executing the shipped JavaScript extracted from
`scripts/mathpath/labs/algebra_core.py`. A lab that reports confidently wrong
roots passes the first and fails the second.

`TestGeneratedPathIsCurrent` fails if a published page differs from what the
content package renders, and if a slug tuple in the test file disagrees with its
content package. Both are silent failures otherwise.

Adding a path: import it in `scripts/build_paths.py` and add it to
`GENERATED_PATHS`; that is the whole registration. It is deliberately not a scan
of `content/` — which paths are published is a decision, and it should be
readable in one place.

Adding a lesson: add a dict to the course module, run the build, then add the URL
to the four declarations listed in section 1 — the suite tells you which are
missing.

**Each path states its own material clause.** The licence line in the shared
footer ends with a sentence naming the intellectual hazard of that subject:
discrete mathematics warns that a worked example is not a proof, algebra that a
step which gives the right answer here is not thereby a valid rule. That clause
is a required `"material"` key on the PATH dict, not a module constant, because
it was a module constant once and became false the moment a second subject
rendered through the same chrome. A disclaimer that is false is worse than none.
`TestGeneratedPathIsCurrent` asserts every generated path states one, that no two
share it, and that it matches the pattern the page sweeps look for.

### A note on page weight

Self-containment means every lesson inlines the whole lab it uses, and the
generated labs share a large exact-arithmetic core. So pages get heavier as the
labs get richer:

Measured, not estimated -- these are medians and maxima over the pages actually
published, and every figure in the previous version of this table understated
the truth by 40% or more, which is how a budget quietly stops being a budget:

| page | raw (median / max) | gzipped (median / max) |
| --- | --- | --- |
| Discrete Mathematics lesson (106 pages) | 108 KB / 144 KB | 28 KB / 37 KB |
| Algebra, course 1 (5-mode lab, 13 pages) | 146 KB / 154 KB | 39 KB / 41 KB |
| Algebra, course 9 (11-mode lab, 11 pages) | 244 KB / 252 KB | 66 KB / 67 KB |

Re-measured 2026-10-07 when Listen landed: every lesson now carries the spoken
form of its math (`data-say`, from `scripts/mathpath/speech.py`) and the reader
script (`scripts/mathpath/readout.py`), about 3 KB gzipped a page in all.

Re-measured again 2026-10-08 when Philosophy was wired (KB here is 1,024
bytes). Philosophy's 108 lessons are 116 KB / 133 KB raw and 30 KB / 36 KB
gzipped, in Discrete Mathematics' range, so they have no row of their own; the
heaviest is Justice and Collective Choice (`choicekit`'s voting modes), whose
ten lessons are 35 KB / 36 KB gzipped.

Re-measured 2026-10-10 when English v2 was wired. English's 41 lessons are
134 KB / 176 KB raw and 36 KB / 52 KB gzipped. The kit's own budget
(`docs/english-v2/PLAN.md` §D.0) is 48 KB gzipped per English lesson, and
three pages are over it: the Vocabulary and Reading lessons, whose `coverage`
lab ships the whole headword list (9 KB gzipped), the novel passage and the
play excerpt (7 KB) and the two modern documents (5 KB) on every page, at
51 KB to 52 KB. Every other English lesson is at or under 44 KB. The library
ceiling below is unchanged.

Re-derive them rather than trusting them; they go stale every time a lab grows:

```
/usr/bin/python3 - <<'PY'
import gzip, pathlib
for line in open('scripts/generated-pages.txt'):
    p = pathlib.Path(line.strip())
    if p.is_file():
        b = p.read_bytes()
        print(len(gzip.compress(b, 9)), len(b), p)
PY
```

The second factor is the number of MODES a lab has. One function serves every
mode of a lab, so a page ships all of them: a reader on the sigma-notation
lesson downloads the annuity and Pascal code as well. Emitting only the active
mode is a real optimisation and a real change to the lab kit; it has not been
made, and 67 KB on the wire does not justify making it yet.

**67 KB gzipped is the current ceiling, and it is the number to check** before
anyone proposes "just extract the shared JavaScript into one file both paths
load" -- that would cut the bytes sharply and break the invariant in section 2,
which is the one rule this repository does not trade away. If page weight ever
does become a problem, the fix is a smaller lab, not a shared file.

A kit author designing a lab with ten or more modes should measure the page
before believing it fits. The heaviest page in the repository today is
`sequences-and-series/infinite-geometric-series` at 67 KB gzipped, and it is an
eleven-mode lab.

## 2. The self-containment invariant (non-negotiable)

**Every page under `site/` must render completely with zero network requests beyond
the document itself.** No external origin, no CDN, no web font, no analytics, no
build step, no package manager. CSS goes in `<style>`, JavaScript in `<script>`,
images inline as SVG or `data:` URIs.

Forbidden anywhere in `site/`:

- absolute `http(s)://` or protocol-relative `//host/` references;
- `<script src=...>` in any form — all JavaScript is inline;
- `<link>` to a remote origin, and any `@import`;
- `fetch()`, `XMLHttpRequest`, `WebSocket`, `EventSource`, `sendBeacon`,
  `importScripts`, dynamic `import()`, service workers.

Exactly three narrow exceptions exist, all enforced in
`.github/workflows/ci.yml` (step "Self-containment invariant"):

1. **Reviewed navigation origins.** A plain `<a href>` fetches nothing until a
   reader clicks it. The allowlist is the constant `ALLOWED_LINK_ORIGINS` in the
   CI step and currently holds `https://learn.geterdone.io` and
   `https://geterdone.io`. Adding an origin is a reviewed code change — never a
   runtime exception.
2. **XML namespace identifiers** (`http://www.w3.org/2000/svg` and friends) in
   `xmlns` attributes and `createElementNS` calls. They are identifiers, not URLs
   that get fetched.
3. **Same-origin metadata URLs** in `<link rel="canonical">`/`rel="alternate"` and
   `og:url`/`twitter:url`, which describe the page rather than load anything.

Why this matters beyond principle: the in-container Content-Security-Policy in
`deploy/Caddyfile` is `default-src 'none'` with no external origins. A page that
violates the invariant does not degrade — it breaks in production while passing a
casual local file:// check.

## 3. The site is served as a container, not as files

The platform has **no `file_server` and no host document root**. It serves apps
only as `reverse_proxy 127.0.0.1:<port>` to a container
(`platform-ops/docs/EDGE_ROUTING_CONTRACT.md` sections 5–7). Consequences:

- The static site ships inside an image built from `Containerfile.release`, with
  an in-container web server (`deploy/Caddyfile`) that serves `/srv` and answers
  `GET /healthz` with `200`. The health route is required by the deployment
  contract and is produced by that config, not by any file in `site/`.
- Host-native Caddy owns public TLS, ports 80/443, redirects and HSTS. The
  container speaks **plain HTTP** and must never add TLS, certificates, an
  HTTP→HTTPS redirect, HSTS, or trust in `X-Forwarded-*`.
- The container runs as UID 1000 with a read-only root filesystem, `cap_drop:
  [ALL]`, `no-new-privileges`, and bounded CPU/memory/PIDs. Do not weaken any of
  those; they are frozen registry fields, and a routine release may not change
  them.

## 4. The app is a tenant of the shared edge; it allocates nothing

This app is deployed by `/usr/local/sbin/platform-deploy-static`, and that wrapper
decides the runtime topology, not this repository. It renders its own Compose file
from `/etc/platform/templates/static-compose.yaml`, attaches the container to the
shared external network `platform-private-edge` at the fixed private address in
`/etc/platform/apps/learn-geterdone.env`, and writes and owns
`/etc/caddy/sites.d/learn-geterdone.caddy`. Nothing is published on host loopback.

So the two things this repository must get right are **fixed constants**, not
allocations:

- **The container listens on `8080`.** `deploy/Caddyfile` binds `:8080` and
  `Containerfile.release` EXPOSEs and healthchecks it. The shared Compose template
  probes `http://127.0.0.1:8080/healthz`; a different port is simply not deployable.
- **`/srv/release.txt` carries the release commit.** `Containerfile.release` takes
  `ARG RELEASE_SHA` and writes it there, and `release.yml` passes
  `build-args: RELEASE_SHA=${{ github.sha }}`. The wrapper fetches that file over
  the private address AND over the public domain and requires both to equal the SHA
  it was invoked with. It is served `no-store`: a cached copy would let a previous
  release's marker satisfy the check for the new one.

The old `__LOOPBACK_PORT__` and `__APP_SUBNET__` placeholders are **retired**, and
`compose.template.yaml` is deleted — the host renders its own. Both CI and the
release workflow now FAIL if either token reappears in `deploy/Caddyfile` or
`Containerfile.release`. Do not reintroduce them, and do not re-add a repo-side
Compose file: two Compose definitions for one app is exactly the disagreement the
wrapper's `rendered_sha256` check used to guard against.

**Never `10.89.2.0/24` as an app subnet.** That CIDR *is* `platform-private-edge`,
the network this app joins as a tenant. It belongs in `occupied_resources`, and an
app that declared it as its own would collide with the network it runs on.

Changing the private IPv4, the shared network, or the domain is a **platform**
change made in `dmedellin/platform-ops` plus `/etc/platform/apps/learn-geterdone.env`
on the host — never a workflow edit here.

## 5. Where authority actually lives

The platform contract is normative and lives outside this repository, in
`dmedellin/platform-ops`:

- `docs/DEPLOYMENT_CONTRACT.md` — workflow split, wrapper interface, release
  metadata, pointer/rollback invariants, evidence.
- `docs/EDGE_ROUTING_CONTRACT.md` — registry shape, domains, allocation, Caddy.
- `docs/APP_ONBOARDING.md` — the one-time onboarding transaction and its gates.
- `docs/IMMUTABLE_RELEASE_AND_ACTIVATION.md` — release identity and staging.
- `apps/registry.yaml` and `schemas/app-registry.schema.json` — the registry entry.

Read the real documents; do not reconstruct their rules from memory or from this
summary. **The root-owned host registry wins over anything in this repository.**
Release metadata may narrow behavior; it may never expand scope.

Ownership boundary: this repo owns the site, its tests, PR CI, the protected-main
build/publish job, the immutable Compose template, the release-contract schema and
the smoke client. The platform repo owns the registry, the deploy/rollback
wrapper, runner definitions, sudoers and Caddy fragments. The production host owns
credentials, release directories, pointers and audit records. Do not write a file
here that belongs on the other side of that line —
`deploy/registry-entry.PROPOSED.yaml` is a *proposal for review*, not an installed
registry.

## 6. Never commit

- Secrets of any kind: tokens, registry credentials, runner registration tokens,
  API keys, `.env` files, `*.key`, `*.pem`, certificates. The only credential this
  repository may use is the automatic `GITHUB_TOKEN`. If a secret ever lands in a
  commit, rotate it — deleting the file is not sufficient.
- **A hand-written image digest.** If you cannot verify a real digest against a
  registry, write `__BASE_IMAGE_DIGEST__` and stop. A plausible-looking invented
  `sha256:` is worse than an obvious placeholder: it looks verified.
- A loopback port, an app subnet, or a repo-side Compose file (see section 4).
  The host decides the topology; this repository pins only port 8080.
- CI status badges, or any claim that a build, deployment, or acceptance passed
  that you did not watch pass. A self-hosted runner and a `production`
  environment now exist, so "it deployed" is a checkable claim - check it against
  the run, the digest, and the live site rather than asserting it.
- Vendored third-party assets without shipping rights and recorded provenance.
- Generated build output, `node_modules/`, or anything in `.gitignore`.

## 7. Verifying a change

CI runs on every pull request to `main` and again on the merged commit. It checks
HTML well-formedness, the self-containment invariant, internal link resolution,
the Containerfile, the allocation guard, and that no credential-shaped file is
tracked. Nothing is installed from the network, so it is reproducible locally:

```sh
python3 -m unittest discover -s tests -v       # on-disk invariant suite
python3 -m http.server 8000 --directory site   # then open http://127.0.0.1:8000/
python3 scripts/smoke.py http://127.0.0.1:8000 # acceptance checks against a running server
```

Do not add a package manager, bundler, or test framework to make a check easier.
Dependency-light is a deliberate property of this repository, not an accident.

## 8. Reading this repository without burning a context window

**87% of this repository by bytes is generated output that nobody should read.**
Measured, tracked files only:

| area | files | bytes | ≈ tokens |
| --- | ---: | ---: | ---: |
| `site/` | 378 | 41.4 MB | **~10,400,000** |
| `content/` | 62 | 2.9 MB | ~714,000 |
| `scripts/` | 36 | 1.9 MB | ~470,000 |
| `release/` | 3 | 1.0 MB | ~245,000 |
| `tests/` | 1 | 0.2 MB | ~52,000 |

One Algebra course-9 lesson is 220 KB — **about 55,000 tokens**. Three of them
do not fit in a context window. This is not a hypothetical cost; it is the
single largest thing that can go wrong with an automated change here.

**Never read these whole. There is no task that requires it:**

- `site/**/*.html` — output. For the two generated paths it is rebuilt from
  `content/` by `scripts/build_paths.py`, so the source of truth is the content
  package and the renderer, never the page. For the trading path the page IS the
  source, but you still want a targeted range, not 27,000 tokens of inlined lab.
- `release/contract.json`, `release/contract.example.json` — 832 KB of generated
  URL manifest between them. Query them; do not open them.
- `scripts/mathpath/labs/algebra_systems.py` (264 KB) and its siblings — read the
  function you are changing.
- `tests/test_site_invariants.py` — 4,000+ lines. Find the class, read the class.

**Do this instead.** Every one of these answers a real question for a few
hundred tokens:

```sh
grep -rl 'data-lesson=' site | wc -l                 # which pages carry a hook
grep -n 'class TestSelfContainment' tests/test_site_invariants.py
sed -n '620,700p' tests/test_site_invariants.py      # then read just that range
python3 -c "import json;d=json.load(open('release/contract.json'));print(len(d['acceptance']['checks']))"
git diff --stat                                      # what actually changed
python3 scripts/build_paths.py --check               # is any page stale (no rebuild)
```

Prefer running a check over reading the thing it checks. The suites in section 7
and the Node checkers below are cheap and they answer questions that reading
cannot: `mathcheck.js` proves the arithmetic, `labcheck.js` proves every lab
runs, `progresscheck.js` proves the completion figures agree with each other,
`feedbackcheck.js` proves the recommendation panel records, ticks, escapes and
exports.

Some invariants exist ONLY in `.github/workflows/ci.yml` and the local suite will
not catch them — "exactly one `<title>` per document" is one, and an SVG
`<title>` violates it. Before pushing, run the workflow's own steps locally
rather than discovering them remotely.

## 9. Which agent does what, and on which model

The work here splits along blast radius, and the model should follow it. The
question is not "how hard is this task" but **"if this goes wrong, how long does
it stay wrong?"** A confidently wrong lab passes every markup check. A wrong
test passes silently, forever. Those get the strongest model regardless of how
small the diff looks.

| agent | tier | Claude | Codex | owns | why this tier |
| --- | --- | --- | --- | --- | --- |
| `site-architect` | deep | opus | `-p deep` | URL space, cross-path design, retirements | one decision reshapes five declarations and the public URL space |
| `chrome-renderer` | deep | opus | `-p deep` | `scripts/mathpath/{chrome,theme,render,progress,feedback,speech,readout}.py` | one edit lands on all 803 lessons at once |
| `lab-arithmetic` | deep | opus | `-p deep` | `scripts/mathpath/labs/`, `scripts/mathcheck.js` | exact rational arithmetic; a wrong answer is invisible to every other check |
| `invariants` | deep | opus | `-p deep` | `tests/test_site_invariants.py` | a test that is wrong passes, and keeps passing |
| `release-safety` | safety | opus | `-p safety` | `release/`, `Containerfile.release`, `.github/workflows/`, `deploy/` | irreversible and expensive; **read-only** |
| `content-author` | build | sonnet | `-p build` | `content/discrete_math/`, `content/algebra/` | high volume, and `mathcheck`/`labcheck` are real gates behind it |
| `trading-pages` | build | sonnet | `-p build` | the eight trading course trees, `scripts/add_progress_marks.py` | hand-authored, blast radius is one course |
| `self-containment` | build | sonnet | `-p build` | the invariant across its declaration sites | a pattern sweep with a fixed rule |
| `test-triage` | triage | haiku | `-p triage` | run the suites, read failures, report which ones and where | mechanical, high volume, no design judgement |

Two rules that matter more than the table:

1. **Escalate on evidence, not on nerves.** If a sonnet agent finds it is
   reasoning about the URL space, the release contract, or whether a test is
   itself correct, it should stop and hand back rather than proceed carefully.
2. **Never let a cheap model decide it is finished.** `test-triage` reports; it
   does not judge whether a failure is acceptable. That is the requesting
   agent's call.

Model names are also the only thing here that dates quickly. The tiers are the
contract; the specific model behind a tier is not.

### Running these

**Claude Code** discovers the nine agents in `.claude/agents/`; each carries its
own model and tool set, and the two that touch production have no edit or write
tool at all.

**Codex** takes the same tiers as profiles in `$CODEX_HOME`, verified against
this machine (CLI 0.144.6):

    codex -p deep      # gpt-5.6-sol   xhigh   workspace-write
    codex -p build     # gpt-5.6-terra medium  workspace-write
    codex -p triage    # gpt-5.6-luna  low     read-only
    codex -p safety    # gpt-5.6-sol   high    read-only

The read-only sandbox is enforced by the runtime, not merely requested in a
prompt — which is the whole reason the production tiers use it. Note that
`codex exec` sets `approval: never` because it is non-interactive; the sandbox
still applies, and that is what stops it.

Codex also reads **nested `AGENTS.md`** files, whose scope is the directory tree
they sit in, with the deepest file winning. `scripts/mathpath/`, `content/`,
`tests/`, `release/` and `.github/` each carry one, so an agent working there
gets that area's rules without the root document having to hold them all. The
root doc has a size budget (`project_doc_max_bytes`, 32 KB by default) and is
already at ~20 KB, so new detail belongs in a nested file, not here.

`site/` deliberately has NO `AGENTS.md`, even though it is the directory that
most needs the warning: everything under `site/` is published, and
`tests/test_site_invariants.py` fails on any published file that is not a
declared URL. Its rule lives in §8 above, which every agent loads anyway.
