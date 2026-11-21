#!/usr/bin/env python3
"""Render an episode script into a finished video.

    $VENV/python video/make_video.py gof-behavioral-requests/chain-of-responsibility/long   # 1920x1080
    $VENV/python video/make_video.py gof-behavioral-requests/chain-of-responsibility/short  # 1080x1920
    $VENV/python video/make_video.py gof-behavioral-requests/chain-of-responsibility         # both
    python3 video/make_video.py --check                                                       # check scripts (stdlib)

($VENV is ~/.cache/loop-reels/venv/bin: the same tools as loop-geterdone's videos.)

Writes video/out/<course>/<lesson>/<name>.mp4 plus .vtt (captions for the page's
player), .srt, .jpg (thumbnail or cover) and .json (length and chapters), which
video/publish.py uploads and records in video/published.json.

  1. voice     Kokoro af_heart (the pixelbattle.me voice), sentence by sentence
               with natural pauses
  2. timing    Whisper word timings on the finished voice, aligned to the script
  3. render    Remotion "Video" composition (layout follows the format)
  4. assemble  FFmpeg: voice at -14 LUFS, faststart MP4; thumbnail still
"""

import argparse
import difflib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))

from video import episode as E  # noqa: E402
from video import lessons as L  # noqa: E402


CACHE = Path(os.environ.get("VIDEO_CACHE", Path.home() / ".cache/loop-reels"))
KOKORO_DIR = Path(os.environ.get("KOKORO_DIR", Path.home() / ".cache/alchemist-lab-tts"))
VOICE = os.environ.get("VIDEO_VOICE", "af_heart")
WHISPER_MODEL = os.environ.get("VIDEO_WHISPER", "small.en")
FPS = 30
SITE_URL = "learn.geterdone.io"
# Pacing per format: (speed, pause between sentences, pause between scenes, lead-in, tail) in seconds.
PACE = {"long": (0.97, 0.34, 0.75, 0.6, 2.5), "short": (1.04, 0.22, 0.35, 0.3, 1.6)}
SIZE = {"long": (1920, 1080), "short": (1080, 1920)}


def log(msg):
    print("[%s] %s" % (time.strftime("%H:%M:%S"), msg), flush=True)


def ffmpeg():
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def sentences(text):
    return [s for s in re.split(r"(?<=[.?!])\s+", text.strip()) if s]


# ----------------------------------------------------------------- voice

def make_voice(scenes, fmt, work):
    import numpy as np
    import soundfile as sf
    from kokoro_onnx import Kokoro

    speed, s_gap, sc_gap, lead, tail = PACE[fmt]
    k = Kokoro(str(KOKORO_DIR / "kokoro-v1.0.onnx"), str(KOKORO_DIR / "voices-v1.0.bin"))
    sr, t, clips, spans = 24000, lead, [], []
    for sc in scenes:
        start = t
        for sent in sentences(sc["say"]):
            s, sr = k.create(sent, voice=VOICE, speed=speed, lang="en-us")
            loud = np.where(np.abs(s) > 0.01)[0]
            if len(loud):
                s = s[max(0, loud[0] - 360): min(len(s), loud[-1] + 1200)]
            s = s / max(1e-6, np.abs(s).max()) * 0.9
            clips.append((t, s))
            t += len(s) / sr + s_gap
        spans.append((start, t - s_gap))
        t += sc_gap - s_gap
    total = spans[-1][1] + tail
    out = np.zeros(int(total * sr) + 1, dtype=np.float32)
    for a, s in clips:
        i = int(a * sr)
        out[i:i + len(s)] = s
    sf.write(work / "voice.wav", out, sr, subtype="PCM_16")
    return spans, total


# ----------------------------------------------------------------- timing

def _norm(w):
    return re.sub(r"[^a-z0-9%]", "", w.lower())


def word_times(scenes, spans, work):
    import numpy as np
    import soundfile as sf
    from faster_whisper import WhisperModel

    model = WhisperModel(WHISPER_MODEL, device="cpu", compute_type="int8", download_root=str(CACHE / "whisper"))
    audio, sr = sf.read(work / "voice.wav", dtype="float32")
    audio = np.interp(np.arange(0, len(audio), sr / 16000), np.arange(len(audio)), audio).astype(np.float32)
    segs, _ = model.transcribe(audio, language="en", word_timestamps=True, beam_size=5,
                               initial_prompt=" ".join(sc["say"] for sc in scenes)[:800])
    heard = [(w.word.strip(), w.start, w.end) for s in segs for w in s.words if _norm(w.word)]
    script = [(w, i) for i, sc in enumerate(scenes) for w in sc["say"].split()]
    a, b = [_norm(w) for w, _ in script], [_norm(w) for w, _, _ in heard]
    times = [None] * len(script)
    for blk in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks():
        for j in range(blk.size):
            times[blk.a + j] = heard[blk.b + j][1:]
    matched = sum(t is not None for t in times)
    i = 0
    while i < len(script):
        if times[i] is not None:
            i += 1
            continue
        j = i
        while j < len(script) and times[j] is None:
            j += 1
        lo = times[i - 1][1] if i > 0 else spans[script[i][1]][0]
        hi = times[j][0] if j < len(script) else spans[script[j - 1][1]][1]
        step = max(0.05, (hi - lo) / (j - i))
        for kk in range(i, j):
            times[kk] = (lo + (kk - i) * step, lo + (kk - i + 1) * step)
        i = j
    (work / "heard.txt").write_text(" ".join(w for w, _, _ in heard) + "\n")
    words = [{"w": w, "s": round(t[0], 3), "e": round(t[1], 3), "scene": sc} for (w, sc), t in zip(script, times)]
    return words, matched / max(1, len(script))


def caption_chunks(words, fmt):
    """Short: 1-3 words, big and burned in. Long: subtitle lines of up to ~7 words (SRT only)."""
    most = 3 if fmt == "short" else 7
    chunks, cur = [], []
    for w in words:
        if cur and (len(cur) == most or w["s"] - cur[-1]["e"] > 0.4 or cur[-1]["scene"] != w["scene"]):
            chunks.append(cur)
            cur = []
        cur.append(w)
        if re.search(r"[.?!]$", w["w"]) or (fmt == "short" and re.search(r"[,:;]$", w["w"])):
            chunks.append(cur)
            cur = []
    if cur:
        chunks.append(cur)
    return [{"s": c[0]["s"], "e": c[-1]["e"], "words": [{"w": x["w"], "s": x["s"], "e": x["e"]} for x in c]} for c in chunks]


def ts(t, srt=True):
    ms = int(round(t * 1000))
    if srt:
        return "%02d:%02d:%02d,%03d" % (ms // 3600000, ms // 60000 % 60, ms // 1000 % 60, ms % 1000)
    return "%d:%02d" % (int(t) // 60, int(t) % 60)


# ----------------------------------------------------------------- props

def build_props(meta, scenes, spans, total, words, chunks, work):
    fmt = meta["format"]
    path, course, lesson = L.find(meta["lesson"])
    codes = L.code_sources(lesson)
    gap = PACE[fmt][2]
    art_dir = work / "art"
    art_dir.mkdir(exist_ok=True)
    out, chapter_no = [], 0
    for i, sc in enumerate(scenes):
        o = sc["opts"]
        start = 0.0 if i == 0 else spans[i][0] - gap / 2
        end = total if i == len(scenes) - 1 else spans[i + 1][0] - gap / 2
        item = {"kind": sc["kind"], "from": int(round(start * FPS)), "dur": max(1, int(round((end - start) * FPS)))}
        sw = [w for w in words if w["scene"] == i]

        def at(phrase, start=start, sw=sw, say=sc["say"]):
            k = E.spoken_at(phrase, say) if phrase else None
            if k is None:
                return None
            seen, idx = 0, len(sw) - 1
            for j, w in enumerate(sw):
                if seen >= k:
                    idx = j
                    break
                seen += max(1, len(E.tokens(w["w"])))
            return max(0, int(round((sw[idx]["s"] - start) * FPS)) - 4)

        def art(name):
            shutil.copy(E.art_path(meta["lesson"], name), art_dir / (name + ".png"))
            return "art/%s.png" % name

        if sc["chapter"]:
            chapter_no += 1
            item["chapter"] = {"n": chapter_no, "title": sc["chapter"]}
        k = sc["kind"]
        if k == "title":
            item.update(text=o["text"], sub=o.get("sub", ""), art=art(o["art"]) if o.get("art") else "")
        elif k == "art":
            item.update(art=art(sc["pos"][0]), zoom=o.get("zoom", "in"))
        elif k == "code":
            # Trailing comments are dropped on screen unless comments=keep (the narration explains instead).
            code = L.display_lines(codes[o.get("block", "1")], strip_comments=o.get("comments") != "keep")
            a, b = E.rng(o.get("lines"), (1, len(code)))
            lang = o.get("lang", "java" if any(";" in x for x in code) else "text")
            item.update(lang=lang, label=o.get("label", lang.capitalize() if lang != "text" else ""),
                        firstLine=a, lines=code[a - 1:b],
                        focus=[{"a": fa, "b": fb, "at": at(ph)} for (fa, fb), ph in E.focus_list(o.get("focus"))])
        elif k == "quote":
            item.update(text=o["text"], cite=o.get("cite", ""))
        elif k == "words":
            item.update(text=o["text"], sub=o.get("sub", ""))
        elif k == "math":
            items = E.math_items(o["items"])
            n = len(items)
            spread = [int(item["dur"] * (0.05 + 0.75 * j / max(1, n))) for j in range(n)]
            item.update(heading=o.get("heading", ""), items=[t for t, _ in items],
                        itemsAt=[at(ph) if at(ph) is not None else spread[j] for j, (_, ph) in enumerate(items)])
        elif k == "list":
            items = E.list_items(o["items"])
            n = len(items)
            spread = [int(item["dur"] * (0.08 + 0.7 * j / max(1, n))) for j in range(n)]
            item.update(heading=o.get("heading", ""), items=[t for t, _ in items],
                        itemsAt=[at(ph) if at(ph) is not None else spread[j] for j, (_, ph) in enumerate(items)])
        elif k == "end":
            item.update(text=o.get("text", "The full lesson is on Learn"), url=SITE_URL + L.url_path(course, lesson))
        out.append(item)
    w, h = SIZE[fmt]
    return {"format": fmt, "width": w, "height": h, "fps": FPS, "durationInFrames": int(round(total * FPS)),
            "title": meta.get("title", L.plain(lesson["title"])), "thumb": meta.get("thumb", ""), "lesson": L.plain(lesson["title"]),
            "track": L.plain(path["title"]).replace(", Read Along", ""),
            "scenes": out, "captions": chunks if fmt == "short" else []}


def remotion(args, work):
    r = subprocess.run(["npx", "remotion"] + args + ["--public-dir=" + str(work), "--log=warn"],
                       cwd=HERE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if r.returncode:
        print(r.stdout[-4000:])
        raise SystemExit("remotion failed (exit %d)" % r.returncode)


def make(target, out_dir):
    course_slug, lesson_slug, name = target.split("/")
    path = E.EPISODES / course_slug / lesson_slug / (name + ".md")
    errs = E.check(path)
    if errs:
        sys.exit("\n".join(errs))
    meta, scenes = E.parse(path)
    vid = "%s-%s-%s" % (course_slug, lesson_slug, name)
    work = HERE / "work" / vid
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)
    dest = out_dir / course_slug / lesson_slug
    dest.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    log("%s: voice" % vid)
    spans, total = make_voice(scenes, meta["format"], work)
    log("%s: %d:%02d long" % (vid, int(total) // 60, int(total) % 60))
    log("%s: timing (Whisper)" % vid)
    words, acc = word_times(scenes, spans, work)
    log("%s: Whisper heard %.0f%% of the script%s" % (vid, acc * 100, "" if acc >= 0.9 else "  <-- check work/%s/heard.txt" % vid))
    chunks = caption_chunks(words, meta["format"])
    props = build_props(meta, scenes, spans, total, words, chunks, work)
    (work / "props.json").write_text(json.dumps(props))
    log("%s: render (Remotion, %d frames)" % (vid, props["durationInFrames"]))
    remotion(["render", "remotion/index.ts", "Video", str(work / "video.mp4"), "--props=" + str(work / "props.json"),
              "--muted", "--codec=h264", "--crf=18"], work)
    log("%s: assemble (FFmpeg)" % vid)
    final = dest / (name + ".mp4")
    # Re-encoded for the web: the scenes are mostly still, so CRF 26 is visually
    # clean at a fraction of the size, and +faststart lets playback begin at once.
    subprocess.run([ffmpeg(), "-y", "-loglevel", "error", "-i", str(work / "video.mp4"), "-i", str(work / "voice.wav"),
                    "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "slow", "-crf", "26", "-pix_fmt", "yuv420p",
                    "-tune", "stillimage", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000",
                    "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", str(final)], check=True)
    srt_chunks = chunks if meta["format"] == "long" else caption_chunks(words, "long")
    (dest / (name + ".srt")).write_text("\n".join("%d\n%s --> %s\n%s\n" % (n, ts(c["s"]), ts(c["e"]), " ".join(w["w"] for w in c["words"]))
                                                for n, c in enumerate(srt_chunks, 1)))
    (dest / (name + ".vtt")).write_text("WEBVTT\n\n" + "\n".join("%s --> %s\n%s\n" % (ts(c["s"]).replace(",", "."), ts(c["e"]).replace(",", "."),
                                                                                         " ".join(w["w"] for w in c["words"]))
                                                                  for c in srt_chunks))
    chapters = [{"t": round(s["from"] / FPS, 1), "title": s["chapter"]["title"]} for s in props["scenes"] if s.get("chapter")]
    if chapters:
        chapters[0]["t"] = 0
    if meta["format"] == "long":
        remotion(["still", "remotion/index.ts", "Thumbnail", str(dest / (name + ".jpg")), "--props=" + str(work / "props.json"),
                  "--image-format=jpeg"], work)
    else:
        subprocess.run([ffmpeg(), "-y", "-loglevel", "error", "-ss", "1.0", "-i", str(final), "-frames:v", "1", "-q:v", "3",
                        str(dest / (name + ".jpg"))], check=True)
    info = {"lesson": meta["lesson"], "format": meta["format"], "title": props["title"], "seconds": round(total, 1),
            "bytes": final.stat().st_size, "chapters": chapters, "whisper_match": round(acc, 3)}
    (dest / (name + ".json")).write_text(json.dumps(info, indent=1) + "\n")
    log("%s: done in %.0f s -> %s (%.1f MB)" % (vid, time.time() - t0, final.relative_to(ROOT), final.stat().st_size / 1e6))
    return info


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("targets", nargs="*", help="<course>/<lesson>[/<long|short>]; none = every script")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    # Named targets are checked one by one in make(); other lessons' missing art
    # (still to be drawn in a batch run) must not block them.
    errs = E.check_all() if args.check or not args.targets else []
    if errs or args.check:
        print("\n".join(errs) or "episode scripts OK (%d)" % len(E.all_scripts()))
        sys.exit(1 if errs else 0)
    out_dir = HERE / "out"
    out_dir.mkdir(exist_ok=True)
    targets = []
    for t in args.targets or ["/".join(p.parts[-3:])[:-3] for p in E.all_scripts()]:
        targets += [t] if t.count("/") == 2 else ["%s/%s" % (t, n) for n in ("short", "long")
                                                   if (E.EPISODES / t / (n + ".md")).exists()]
    print(json.dumps([make(t, out_dir) for t in targets], indent=2))


if __name__ == "__main__":
    main()
