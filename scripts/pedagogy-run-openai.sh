#!/usr/bin/env bash
# Continue the pedagogy pass with OpenAI Codex CLI, one Algebra course at a time.
#
# This is the quota-fallback lane. The first 16 courses were assessed by the
# Claude Code pedagogical-expert on Fable 5. Fable's all-model weekly quota was
# exhausted; the user explicitly selected OpenAI for the remaining nine.
#
# Run only on pedagogy/openai-algebra. Each course is committed locally by Codex,
# independently reverified here, then pushed to that branch. Nothing pushes main,
# so nine content passes produce one reviewed merge and one deployment.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO"
LOGDIR="$REPO/.pedagogy-logs/openai"
mkdir -p "$LOGDIR"

COURSES=(
  algebra-foundations
  linear-equations-and-inequalities
  lines-functions-and-graphs
  polynomials-and-factoring
  rational-and-radical-expressions
  quadratics-and-complex-numbers
  exponential-and-logarithmic-functions
  systems-and-matrices
  sequences-and-series
)

targets=("$@")
[ ${#targets[@]} -eq 0 ] && targets=("${COURSES[@]}")

for slug in "${targets[@]}"; do
  if [ -f "docs/pedagogy/$slug.md" ]; then
    echo "== SKIP $slug (docs/pedagogy/$slug.md exists)"
    continue
  fi

  branch="$(git branch --show-current)"
  if [ "$branch" != "pedagogy/openai-algebra" ]; then
    echo "!! refusing to run on $branch; expected pedagogy/openai-algebra" >&2
    exit 1
  fi
  if [ -n "$(git status --porcelain)" ]; then
    echo "!! working tree is dirty before $slug" >&2
    git status --short >&2
    exit 1
  fi

  before="$(git rev-parse HEAD)"
  prompt="$LOGDIR/$slug.prompt.md"
  last="$LOGDIR/$slug.last.md"
  events="$LOGDIR/$slug.jsonl"

  cat > "$prompt" <<EOF
You are the pedagogical expert for learn.geterdone.io. Work on the single course
`$slug` in $REPO.

First read AGENTS.md sections 1, 1a and 2 and then read
.claude/agents/pedagogical-expert.md in full. Adopt that role contract even though
this invocation is OpenAI Codex rather than Claude Code. You have full authority
to add, split, merge, reorder, retitle or remove lessons when pedagogy requires it.

This is one course in the generated Algebra path. The source of truth is
content/algebra/, NEVER hand edits to site/. Read every lesson in the course before
changing any of them. Full coverage is mandatory; do not sample and generalize.

Deliver exactly this course:
1. Write docs/pedagogy/$slug.md citing lesson slugs: what works, what fails, what it
   claims but does not teach, where learners get stuck, prerequisites used before
   teaching, misconceptions, and the repairs made.
2. Refactor against those findings. Observable objectives, prerequisite order,
   cognitive load, worked-example -> faded guidance -> independent practice,
   retrieval with error-specific feedback, and misconception handling are the bar.
3. Edit content/algebra/ and shared lab source as needed, then rebuild with
   /usr/bin/python3 scripts/build_paths.py. Do not hand-edit generated pages.
4. If any URL changes, update all five URL declarations in the same commit. Retired
   URLs stay retired, especially /market-structure-lab/.
5. Run these exact gates, with no tail/head pipeline masking exit status:
     /usr/bin/python3 -m unittest discover -s tests
     /usr/bin/python3 scripts/build_paths.py --check
     /usr/bin/python3 scripts/validate_release_contract.py release/contract.json
     node scripts/mathcheck.js
     node scripts/labcheck.js --generated
6. For any new arithmetic, mutation-test the checker: deliberately break the shipped
   implementation, prove the checker itself exits nonzero, restore exact bytes, and
   prove it exits zero. Never report a piped tail/head exit code as the test result.
7. Commit only this course's cohesive work on the CURRENT branch. Do NOT push and do
   not merge. The outer runner independently verifies and pushes after you finish.

The current branch is pedagogy/openai-algebra. Platform, release, deployment, DNS,
edge, containers and host state are outside this task. Do not edit CI/CD or deploy.

At the end, report the assessment path, changed source/lab paths, actual gate counts
and exit states, mutation evidence where applicable, and the commit SHA. Do not claim
a gate you did not run to completion.
EOF

  echo "== $slug (OpenAI Codex gpt-5.6-sol / deep / xhigh)"
  codex -p deep exec --sandbox danger-full-access --json \
    --output-last-message "$last" - < "$prompt" > "$events" 2>&1 || {
      echo "!! Codex exited nonzero for $slug; see $events" >&2
      exit 1
    }

  after="$(git rev-parse HEAD)"
  [ "$after" != "$before" ] || { echo "!! $slug produced no commit" >&2; exit 1; }
  test -f "docs/pedagogy/$slug.md" || { echo "!! no assessment for $slug" >&2; exit 1; }
  [ -z "$(git status --porcelain)" ] || {
    echo "!! $slug left a dirty tree after its commit" >&2
    git status --short >&2
    exit 1
  }

  echo "-- independently verifying $slug"
  /usr/bin/python3 -m unittest discover -s tests
  /usr/bin/python3 scripts/build_paths.py --check
  /usr/bin/python3 scripts/validate_release_contract.py release/contract.json
  node scripts/mathcheck.js
  node scripts/labcheck.js --generated
  git diff --check "$before..$after"

  git push origin HEAD:pedagogy/openai-algebra
  echo "== $slug OK  $after"
done

echo "done"
