"""Episode scripts: video/episodes/<course-slug>/<lesson-slug>/<long|short>.md.

Adapted from loop-geterdone's video/episode.py (the same format and voice), so a
script reads the same on both sites. A script is written to be read aloud, like a
person explaining at a whiteboard. The lesson is source material only: a script
retells it in its own words and order.

    ---
    format: long            # long = 1920x1080 full lesson, short = 1080x1920 reel
    lesson: gof-behavioral-requests/chain-of-responsibility
    title: Chain of Responsibility, in one sentence
    thumb: Who takes the request?   # long only: the thumbnail's second line
    ---

    @chapter The problem             # long-form chapter (a small label + the player's chapter list)
    @words text="Who answers?"       # what is on screen while the next paragraph is spoken
    You click for help on a button...

Every `@kind key=value ...` line starts a scene; the paragraph(s) under it are
its narration. Values with spaces go in double quotes. Scene kinds:

    @title  text=".." sub=".." [art=name]   opening card
    @art    name [zoom=in|out]              an illustration from video/assets/art/
    @words  text=".." [sub=".."]            one key line, big
    @list   heading=".." items="a@phrase|b@phrase|c"
            each item appears when its phrase is spoken (no phrase: spread through the scene)
    @quote  text=".." cite=".."             a short quotation the lesson itself quotes
    @code   block=N lines=a-b focus="2@phrase|4-5@phrase" [comments=keep]
            the lesson's N-th code block; each focus range lights up when its phrase is spoken
    @end    text=".."                        call to action with the lesson URL

Stdlib only: tests/test_video.py checks every script without TTS or Node.
"""

import re
import shlex
from pathlib import Path

from . import lessons as L

HERE = Path(__file__).resolve().parent
EPISODES = HERE / "episodes"
ART = HERE / "assets" / "art"
KINDS = {"title", "art", "code", "words", "list", "quote", "end"}
SPEAKABLE = re.compile(r"^[A-Za-z0-9 .,?!'’:;%\-\n]+$")


class ScriptError(ValueError):
    pass


def parse(path):
    text = Path(path).read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise ScriptError("%s: missing the --- header ---" % path)
    meta = {}
    for line in m.group(1).splitlines():
        if line.strip():
            k, _, v = line.partition(":")
            meta[k.strip()] = v.split("#")[0].strip()
    body = text[m.end():]
    scenes, chapter, cur = [], None, None
    for raw in body.splitlines():
        line = raw.strip()
        if line.startswith("#") and not line.startswith("#!"):
            continue
        if line.startswith("@chapter"):
            chapter = line[len("@chapter"):].strip()
            continue
        if line.startswith("@"):
            parts = shlex.split(line[1:].split("  #")[0])
            kind, args = parts[0], parts[1:]
            opts, pos = {}, []
            for a in args:
                if "=" in a:
                    k, _, v = a.partition("=")
                    opts[k] = v
                else:
                    pos.append(a)
            cur = {"kind": kind, "opts": opts, "pos": pos, "say": "", "chapter": chapter}
            chapter = None
            scenes.append(cur)
            continue
        if cur is not None:
            cur["say"] = (cur["say"] + " " + line).strip() if line else cur["say"]
    return meta, scenes


def rng(s, default=None):
    if s is None:
        return default
    a, _, b = s.partition("-")
    return int(a), int(b or a)


def focus_list(s):
    """'2@phrase|4-5@other phrase' -> [((2, 2), 'phrase'), ((4, 5), 'other phrase')]"""
    out = []
    for part in (s or "").split("|"):
        if part.strip():
            lines, _, phrase = part.partition("@")
            out.append((rng(lines.strip()), phrase.strip()))
    return out


def list_items(s):
    """'a@phrase|b' -> [('a', 'phrase'), ('b', None)]"""
    out = []
    for part in (s or "").split("|"):
        text, _, phrase = part.partition("@")
        out.append((text.strip(), phrase.strip() or None))
    return out


def tokens(text):
    return re.findall(r"[a-z0-9%]+", text.lower().replace("’", "").replace("'", ""))


def spoken_at(phrase, say):
    p, s = tokens(phrase), tokens(say)
    for i in range(len(s) - len(p) + 1):
        if p and s[i:i + len(p)] == p:
            return i
    return None


def check(path):
    """Problems that would break a render or mislead (not style rules)."""
    errs = []
    try:
        meta, scenes = parse(path)
    except ScriptError as e:
        return [str(e)]
    name = "/".join(Path(path).parts[-3:])

    def bad(i, msg):
        errs.append("%s scene %s: %s" % (name, i, msg))

    if meta.get("format") not in ("long", "short"):
        bad("header", "format must be long or short")
    try:
        _, course, lesson = L.find(meta.get("lesson", ""))
    except KeyError as e:
        return errs + ["%s: %s" % (name, e)]
    where = Path(path).parent
    if "%s/%s" % (where.parent.name, where.name) != L.key(course, lesson):
        bad("header", "keep the script in video/episodes/%s/" % L.key(course, lesson))
    codes = L.code_sources(lesson)
    if not scenes or scenes[-1]["kind"] != "end":
        bad("last", "the last scene must be @end")
    for i, sc in enumerate(scenes, 1):
        k, o = sc["kind"], sc["opts"]
        if k not in KINDS:
            bad(i, "unknown scene @%s" % k)
            continue
        if not sc["say"]:
            bad(i, "no narration under @%s" % k)
        elif not SPEAKABLE.match(sc["say"]):
            odd = sorted({c for c in sc["say"] if not SPEAKABLE.match(c)})
            bad(i, "narration has symbols the voice reads badly, write them as words: %s" % " ".join(odd))
        art = o.get("art") or (sc["pos"][0] if k == "art" and sc["pos"] else None)
        if k == "art" and not art:
            bad(i, "@art needs a name")
        if art and not (ART / (art + ".png")).exists():
            bad(i, "art %r is not in video/assets/art/" % art)
        if k == "code":
            code = codes.get(o.get("block", "1"))
            if not code:
                bad(i, "the lesson has no code block %s (it has %d)" % (o.get("block", "1"), len(codes)))
                continue
            n = len(code.split("\n"))
            a, b = rng(o.get("lines"), (1, n))
            if not 1 <= a <= b <= n:
                bad(i, "lines %s outside 1..%d" % (o.get("lines"), n))
            for (fa, fb), phrase in focus_list(o.get("focus")):
                if not a <= fa <= fb <= b:
                    bad(i, "focus %d-%d outside the lines shown" % (fa, fb))
                if spoken_at(phrase, sc["say"]) is None:
                    bad(i, "focus phrase %r is not in the narration, so it cannot be timed" % phrase)
        if k in ("words", "title", "quote") and not o.get("text"):
            bad(i, "@%s needs text=" % k)
        if k == "list":
            if not o.get("items"):
                bad(i, "@list needs items=")
            for item in (o.get("items") or "").split("|"):
                _, _, phrase = item.partition("@")
                if phrase and spoken_at(phrase, sc["say"]) is None:
                    bad(i, "list cue %r is not in the narration" % phrase)
    return errs


def all_scripts():
    return sorted(EPISODES.glob("*/*/*.md"))


def check_all():
    return [e for p in all_scripts() for e in check(p)]
