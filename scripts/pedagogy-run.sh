#!/usr/bin/env bash
# Run the pedagogical-expert subagent over every course, one at a time.
#
#   ./scripts/pedagogy-run.sh                 # all remaining courses, in order
#   ./scripts/pedagogy-run.sh market-structure options-trading
#   DRY=1 ./scripts/pedagogy-run.sh           # print what would run
#
# One course per Claude invocation. Never run two at once: they share this
# checkout, and the invariant suite plus the five URL declarations cannot be
# edited concurrently without one clobbering the other.
#
# A course is SKIPPED if docs/pedagogy/<slug>.md already exists, so a re-run
# resumes rather than redoing work. Delete that file to force a course again.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO"

LOGDIR="$REPO/.pedagogy-logs"
mkdir -p "$LOGDIR"

# Path order matters: a course is judged against the ones before it.
COURSES=(
  # Trading
  market-structure trade-setup-execution options-trading technical-indicators
  volume-and-order-flow trading-risk-management backtesting-and-trading-systems
  algorithmic-and-automated-trading
  # Discrete Mathematics
  logic-and-proof sets-relations-functions induction-and-recursion
  combinatorics-and-counting discrete-probability number-theory-and-cryptography
  graphs-and-trees algorithms-and-complexity
  # Algebra
  algebra-foundations linear-equations-and-inequalities lines-functions-and-graphs
  polynomials-and-factoring rational-and-radical-expressions
  quadratics-and-complex-numbers exponential-and-logarithmic-functions
  systems-and-matrices sequences-and-series
)

targets=("$@")
[ ${#targets[@]} -eq 0 ] && targets=("${COURSES[@]}")

for slug in "${targets[@]}"; do
  if [ -f "docs/pedagogy/$slug.md" ]; then
    echo "== SKIP $slug (docs/pedagogy/$slug.md exists)"
    continue
  fi

  echo "== $slug"
  if [ "${DRY:-}" = "1" ]; then continue; fi

  # Refuse to start on a dirty tree: the agent commits, and unrelated staged
  # work would be swept into its commit.
  if [ -n "$(git status --porcelain)" ]; then
    echo "!! working tree is dirty; commit or stash first" >&2
    git status --short >&2
    exit 1
  fi

  before="$(git rev-parse HEAD)"

  claude -p "Use the pedagogical-expert subagent on the course '$slug'.

Assess and refactor that course only, following its full method: read every
lesson before changing anything, write the assessment to docs/pedagogy/$slug.md
citing lesson slugs, refactor against your own findings, then verify, commit and
push to origin/main.

Run every gate before committing and do not commit if any is red. If the course
needs a structural change, update all five URL declarations in the same commit.
Report at the end: what you changed, which gates you ran, and the commit SHA." \
    --model fable \
    --permission-mode bypassPermissions \
    --max-turns 200 \
    --output-format json \
    > "$LOGDIR/$slug.json" 2>&1 || {
      echo "!! claude exited non-zero for $slug; see $LOGDIR/$slug.json" >&2
      exit 1
    }

  after="$(git rev-parse HEAD)"
  if [ "$before" = "$after" ]; then
    echo "!! $slug produced no commit; see $LOGDIR/$slug.json" >&2
    exit 1
  fi

  # Independent verification -- never trust the agent's own PASS claim.
  echo "-- verifying $slug"
  /usr/bin/python3 -m unittest discover -s tests
  /usr/bin/python3 scripts/build_paths.py --check
  /usr/bin/python3 scripts/validate_release_contract.py release/contract.json
  node scripts/mathcheck.js
  node scripts/labcheck.js --generated

  test -f "docs/pedagogy/$slug.md" || { echo "!! no assessment written for $slug" >&2; exit 1; }
  echo "== $slug OK  $after"
done

echo "done"
