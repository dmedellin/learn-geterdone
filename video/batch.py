#!/usr/bin/env python3
"""Make every video for a Subject, a course or a lesson, unattended, on the ThinkCentre.

    ~/.cache/loop-reels/venv/bin/python video/batch.py algebra                  # a Subject (its /paths/ slug)
    ~/.cache/loop-reels/venv/bin/python video/batch.py lines-functions-and-graphs   # a course
    ~/.cache/loop-reels/venv/bin/python video/batch.py <course>/<lesson> [...]
    ... --publish        # also upload each finished lesson (needs VIDEO_DEST; docs/VIDEO.md)
    ... --dry-run        # list what would be done

For each lesson that has scripts (video/episodes/<course>/<lesson>/short.md and
long.md), in site order:

  1. art     if the scripts name art that is missing, run Codex on the lesson's
             prompts (video/art/<course>/<lesson>/scenes.prompt.md, thumb.prompt.md)
             and cut the sheets into video/assets/art/<course>/<lesson>/
  2. render  short and long, unless video/out/<course>/<lesson>/ already has them
  3. publish (with --publish) via video/publish.py

A lesson that fails is logged and skipped; the run carries on. The summary is
printed at the end and kept in video/work/batch-<time>.json. Re-running the same
command resumes: finished lessons are skipped.
"""

import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))

from video import episode as E  # noqa: E402
from video import lessons as L  # noqa: E402

PY = sys.executable
GRID = re.compile(r"(\d+)\s+columns?\s+x\s+(\d+)\s+rows?", re.I)
CELL = re.compile(r"^\s*\d+\.\s+([a-z0-9][a-z0-9-]*):", re.M)


def log(msg):
    print("[%s] %s" % (time.strftime("%H:%M:%S"), msg), flush=True)


def targets(names):
    keys = []
    for p, c, l in L.all_lessons():
        k = L.key(c, l)
        if any(n in (p["slug"], c["slug"], k) for n in names) and (E.EPISODES / k / "long.md").exists():
            keys.append(k)
    return keys


def missing_art(key):
    return [e for n in ("short", "long") for e in E.check(E.EPISODES / key / (n + ".md")) if "art " in e]


def make_art(key):
    prompts = HERE / "art" / key
    out = HERE / "assets" / "art" / key
    for kind in ("scenes", "thumb"):
        prompt = prompts / (kind + ".prompt.md")
        sheet = prompts / (kind + ".png")
        if not prompt.exists():
            raise RuntimeError("no art prompt %s" % prompt.relative_to(ROOT))
        text = prompt.read_text()
        if not sheet.exists():
            log("%s: Codex draws %s" % (key, kind))
            subprocess.run(["timeout", "900", "codex", "exec", "--sandbox", "workspace-write",
                            "-c", "model_reasoning_effort=high", "--", text],
                           cwd=ROOT, stdin=subprocess.DEVNULL, check=True)
        if not sheet.exists():
            raise RuntimeError("Codex did not save %s" % sheet.relative_to(ROOT))
        if kind == "thumb":
            grid, names = "1x1", ["thumb"]
        else:
            m = GRID.search(text)
            grid = "%sx%s" % (m.group(1), m.group(2)) if m else "2x3"
            names = CELL.findall(text)
        subprocess.run([PY, str(HERE / "art" / "slice.py"), "--art", str(sheet), grid, ",".join(names), "--out", str(out)],
                       check=True, stdout=subprocess.DEVNULL)


def rendered(key):
    return all((HERE / "out" / key / (n + ".mp4")).exists() for n in ("short", "long"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("names", nargs="+")
    ap.add_argument("--publish", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    keys = targets(args.names)
    log("%d lessons with scripts" % len(keys))
    if args.dry_run:
        for k in keys:
            print(k, "rendered" if rendered(k) else ("needs art" if missing_art(k) else "ready"))
        return
    results, t0 = [], time.time()
    for n, key in enumerate(keys, 1):
        t1 = time.time()
        r = {"lesson": key}
        try:
            if missing_art(key):
                make_art(key)
                still = missing_art(key)
                if still:
                    raise RuntimeError("; ".join(still))
            errs = [e for n2 in ("short", "long") for e in E.check(E.EPISODES / key / (n2 + ".md"))]
            if errs:
                raise RuntimeError("; ".join(errs))
            if not rendered(key):
                log("[%d/%d] %s: render" % (n, len(keys), key))
                subprocess.run([PY, str(HERE / "make_video.py"), key], cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
            if args.publish:
                subprocess.run([PY, str(HERE / "publish.py"), key], cwd=ROOT, check=True)
            r["ok"] = True
        except Exception as exc:  # noqa: BLE001 -- one lesson's failure must not stop the batch
            r["ok"], r["error"] = False, str(exc)[-600:]
            log("[%d/%d] %s FAILED: %s" % (n, len(keys), key, r["error"]))
        r["seconds"] = round(time.time() - t1)
        results.append(r)
        left = (time.time() - t0) / n * (len(keys) - n)
        log("[%d/%d] %s %s in %ds; about %.1f h left" % (n, len(keys), key, "ok" if r["ok"] else "FAILED", r["seconds"], left / 3600))
    (HERE / "work").mkdir(exist_ok=True)
    report = HERE / "work" / ("batch-%s.json" % time.strftime("%Y%m%d-%H%M%S"))
    report.write_text(json.dumps(results, indent=1) + "\n")
    bad = [r for r in results if not r["ok"]]
    print("%d of %d lessons done, %d failed; report %s" % (len(results) - len(bad), len(results), len(bad), report.relative_to(ROOT)))
    for r in bad:
        print("  %s: %s" % (r["lesson"], r["error"]))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
