#!/usr/bin/env python3
"""Upload rendered lesson videos to the production host and record them as live.

    VIDEO_DEST=user@host:/srv/platform-media/learn-geterdone/video \\
        python3 video/publish.py gof-behavioral-requests/chain-of-responsibility [...]
    python3 video/publish.py --all            # every lesson with both videos rendered in video/out/
    python3 video/publish.py --verify-only    # re-check every lesson in published.json over HTTPS

Stdlib only; needs rsync and ssh access to the host (docs/VIDEO.md). For each
lesson it copies short and long (.mp4, .jpg, .vtt) from video/out/<course>/<lesson>/
to $VIDEO_DEST/<course>/<lesson>/, then fetches each file's headers from
https://learn.geterdone.io/video/... and requires HTTP 200 and the same size.
Only a lesson that passes is written to video/published.json, which is what
makes its pages show the watch buttons on the next build
(python3 scripts/build_paths.py). A lesson is never listed before its files are live.
"""

import argparse
import json
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "out"
PUBLISHED = HERE / "published.json"
ORIGIN = os.environ.get("VIDEO_ORIGIN", "https://learn.geterdone.io")
NAMES = ("short", "long")
EXTS = (".mp4", ".jpg", ".vtt")


def load():
    return json.loads(PUBLISHED.read_text(encoding="utf-8"))


def save(data):
    data["lessons"] = dict(sorted(data["lessons"].items()))
    PUBLISHED.write_text(json.dumps(data, indent=1, sort_keys=False) + "\n", encoding="utf-8")


def rendered(key):
    d = OUT / key
    return all((d / (n + e)).exists() for n in NAMES for e in EXTS + (".json",))


def upload(key, dest):
    src = OUT / key
    files = [str(src / (n + e)) for n in NAMES for e in EXTS]
    remote_dir = "%s/%s/" % (dest.rstrip("/"), key)
    host, _, path = remote_dir.partition(":")
    subprocess.run(["ssh", host, "mkdir -p '%s'" % path], check=True, stdin=subprocess.DEVNULL)
    subprocess.run(["rsync", "-t", "--chmod=F644,D755"] + files + [remote_dir], check=True)


def live_size(url):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "learn-video-publish"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status, int(r.headers.get("Content-Length") or -1)


def verify(key):
    problems = []
    for n in NAMES:
        for e in EXTS:
            local = OUT / key / (n + e)
            url = "%s/video/%s/%s%s" % (ORIGIN, key, n, e)
            try:
                status, size = live_size(url)
            except Exception as exc:  # noqa: BLE001 -- report any failure, keep going
                problems.append("%s: %s" % (url, exc))
                continue
            if status != 200 or (local.exists() and size != local.stat().st_size):
                problems.append("%s: HTTP %s, %s bytes (local %s)" % (url, status, size,
                                                                     local.stat().st_size if local.exists() else "?"))
    return problems


def entry(key):
    out = {}
    for n in NAMES:
        info = json.loads((OUT / key / (n + ".json")).read_text())
        out[n] = {"seconds": info["seconds"], "chapters": info.get("chapters", []) if n == "long" else []}
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("lessons", nargs="*", help="<course>/<lesson>")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--verify-only", action="store_true")
    args = ap.parse_args()
    data = load()
    if args.verify_only:
        bad = {k: verify(k) for k in data["lessons"]}
        bad = {k: v for k, v in bad.items() if v}
        print(json.dumps(bad, indent=1) if bad else "all %d published lessons are live" % len(data["lessons"]))
        sys.exit(1 if bad else 0)
    dest = os.environ.get("VIDEO_DEST")
    if not dest:
        sys.exit("set VIDEO_DEST=user@host:/path/to/video (docs/VIDEO.md)")
    keys = args.lessons or (sorted("/".join(p.parent.relative_to(OUT).parts) for p in OUT.glob("*/*/long.json")) if args.all else [])
    if not keys:
        sys.exit("name lessons as <course>/<lesson>, or pass --all")
    failed = []
    for key in keys:
        if not rendered(key):
            failed.append((key, ["not fully rendered in video/out/%s (needs short and long)" % key]))
            continue
        upload(key, dest)
        problems = verify(key)
        if problems:
            failed.append((key, problems))
            continue
        data["lessons"][key] = entry(key)
        save(data)
        print("live: %s" % key, flush=True)
    for key, problems in failed:
        print("NOT published: %s\n  %s" % (key, "\n  ".join(problems)))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
