"""Which math runs does read-out still have to guess at?

Every run comes out as words (tests/test_speech.py proves that). A few shapes
read as words and can still be wrong, because the notation itself is
ambiguous: `x(t)` is a function of t, `λ(r + 1)` is lambda times r + 1.
`speech.ambiguous()` flags those shapes, and each flagged run needs a spoken
form in `content/spoken/<subject>.py` -- or the content rewritten to the
unambiguous convention (content/AGENTS.md, "Write math a voice can read").

    python3 scripts/speechcheck.py                    # count per subject
    python3 scripts/speechcheck.py --list algebra     # the worklist, as JSON

A Subject whose PATH sets "speech": "code" reads its runs as program text
(`speech.say_code`), not as mathematics: its runs are checked with that reader,
and the mathematical guesses (`f(x)` call or product?) do not arise. A `code`
body block is program text on every Subject; `code_lines()` finds those.
"""

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "content"))

from mathpath.speech import (  # noqa: E402
    CODE_DIALECT, ambiguous, dialect_of, is_table_row, load_overrides, say, say_code, unspoken)

_SPAN = re.compile(r"`([^`]+)`")


def runs(path):
    """(run, where, context) for every math run a subject's pages emit."""
    out = []

    def walk(node, where, context):
        if isinstance(node, str):
            for run in _SPAN.findall(node):
                out.append((run, where, node))
        elif isinstance(node, dict):
            where = "/".join(filter(None, [where, node.get("slug")])) if "slug" in node else where
            for key, value in node.items():
                if key in ("key", "lines") and isinstance(value, list) \
                        and all(isinstance(x, str) for x in value):
                    out.extend((line, where, "\n".join(value)) for line in value
                               if not is_table_row(line))
                else:
                    walk(value, where, context)
        elif isinstance(node, (list, tuple)):
            if isinstance(node, tuple) and len(node) == 2 and node[0] == "math":
                out.extend((line, where, "\n".join(node[1])) for line in node[1]
                           if not is_table_row(line))
            elif isinstance(node, tuple) and len(node) == 2 and node[0] == "code":
                pass  # program text, not math runs: code_lines() and say_code
            else:
                for item in node:
                    walk(item, where, context)

    walk(path, "", "")
    return out


def code_lines(path):
    """(line, where) for every line of every `code` body block in a Subject."""
    out = []
    for course in path.get("courses", []):
        for lesson in course["lessons"]:
            where = "%s/%s" % (course.get("slug"), lesson.get("slug"))
            for kind, payload in lesson.get("body", []):
                if kind == "code":  # a list of lines, or {"lines": [...], "marked": [...]}
                    lines = payload["lines"] if isinstance(payload, dict) else payload
                    out.extend((line, where) for line in lines if line.strip())
    return out


def reader(path):
    """The function that turns this Subject's math runs into words."""
    return say_code if dialect_of(path) == CODE_DIALECT else say


def reading(path, run, overrides):
    """What the page speaks for one run of this Subject."""
    return overrides.get(run) or reader(path)(run)


def subjects():
    from build_paths import GENERATED_PATHS, package_of

    for path in GENERATED_PATHS:
        yield path, load_overrides(package_of(path))


def unresolved(path, overrides):
    """Flagged runs with no spoken form, first sighting of each."""
    seen, code = {}, dialect_of(path) == CODE_DIALECT
    for run, where, context in runs(path):
        if run in overrides or run in seen:
            continue
        # program text has one reading; what can still go wrong is a character
        # the code reader has no word for
        reasons = (["unspoken"] if unspoken(say_code(run)) else []) if code else ambiguous(run)
        if reasons:
            seen[run] = {"run": run, "reading": reader(path)(run), "reasons": reasons,
                         "where": where, "context": context}
    return list(seen.values())


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--list", metavar="SLUG", help="print one subject's worklist as JSON")
    args = parser.parse_args()
    for path, overrides in subjects():
        todo = unresolved(path, overrides)
        if args.list:
            if path["slug"] == args.list:
                json.dump(todo, sys.stdout, ensure_ascii=False, indent=1)
                print()
        else:
            print("%-22s %4d unresolved   %4d spoken forms" % (path["slug"], len(todo), len(overrides)))


if __name__ == "__main__":
    main()
