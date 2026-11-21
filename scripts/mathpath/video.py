"""The lesson's two videos: a short (9:16, under a minute) and the full lesson (16:9).

The videos are not in the image. video/make_video.py renders them on the
ThinkCentre, video/publish.py copies them to the production host's video
folder (served by deploy/Caddyfile at /video/) and records each lesson it
published in video/published.json. A lesson appears there only once its files
are live, so a page offers only videos that exist, and a lesson with no entry
renders byte for byte as it did before videos existed.

Self-containment (AGENTS.md section 2) still holds: the page loads nothing at
first. The watch strip is two buttons. A click builds the <video> element, and
only then does the browser fetch the same-origin file, the way a click on a
link does. The URLs live in the inline script's data, not in an href or src.
"""

import json
from pathlib import Path

from .chrome import esc

PUBLISHED = Path(__file__).resolve().parents[2] / "video" / "published.json"
_CACHE = None


def published():
    """{"<course>/<lesson>": {"short": {...}, "long": {...}}} for every live lesson video."""
    global _CACHE
    if _CACHE is None:
        _CACHE = json.loads(PUBLISHED.read_text(encoding="utf-8")).get("lessons", {}) if PUBLISHED.exists() else {}
    return _CACHE


def for_lesson(lesson_id):
    return published().get(lesson_id)


def _clock(seconds):
    s = int(round(seconds))
    return "%d:%02d" % (s // 60, s % 60)


LABELS = (("short", "Short", "the idea in under a minute"), ("long", "Full lesson", "the whole lesson, with chapters"))


def markup(lesson_id, entry):
    """The watch strip under the lesson head: one button per video, and the stage it plays in."""
    buttons = "".join(
        '<button type="button" class="watch-btn" data-video="%s" aria-controls="watchStage">'
        '<span class="watch-play" aria-hidden="true">&#9654;</span>'
        '<span><strong>%s</strong> <span class="watch-len">%s</span><small>%s</small></span></button>'
        % (name, label, _clock(entry[name]["seconds"]), note)
        for name, label, note in LABELS if name in entry
    )
    return (
        '    <section class="lesson-watch" id="watch" aria-label="Watch this lesson">\n'
        '      <div class="watch-row">%s</div>\n'
        '      <div class="watch-stage" id="watchStage" hidden></div>\n'
        "    </section>\n" % buttons
    )


def script(lesson_id, entry):
    """Builds the player on the first click. Guarded so labcheck's fake window can run it."""
    data = {
        "base": "../../video/%s/" % lesson_id,
        "videos": {name: {"chapters": entry[name].get("chapters", []), "portrait": name == "short"}
                   for name, _, _ in LABELS if name in entry},
    }
    return """
  (function () {
    var WATCH = %s;
    var stage = document.getElementById('watchStage');
    if (!stage || typeof document.createElement !== 'function'
        || typeof stage.appendChild !== 'function') return;
    var buttons = Array.prototype.slice.call(document.querySelectorAll('.watch-btn'));
    function clock(t) { t = Math.round(t); return Math.floor(t / 60) + ':' + ('0' + (t %% 60)).slice(-2); }
    function play(name) {
      var v = WATCH.videos[name];
      if (!v) return;
      while (stage.firstChild) stage.removeChild(stage.firstChild);
      stage.hidden = false;
      stage.className = 'watch-stage' + (v.portrait ? ' is-portrait' : '');
      var video = document.createElement('video');
      video.controls = true;
      video.playsInline = true;
      video.preload = 'metadata';
      video.poster = WATCH.base + name + '.jpg';
      video.src = WATCH.base + name + '.mp4';
      var track = document.createElement('track');
      track.kind = 'captions';
      track.label = 'English';
      track.srclang = 'en';
      track.src = WATCH.base + name + '.vtt';
      video.appendChild(track);
      stage.appendChild(video);
      if (v.chapters.length > 1) {
        var list = document.createElement('ol');
        list.className = 'watch-chapters';
        v.chapters.forEach(function (c) {
          var li = document.createElement('li');
          var b = document.createElement('button');
          b.type = 'button';
          b.textContent = clock(c.t) + '  ' + c.title;
          b.addEventListener('click', function () { video.currentTime = c.t; video.play(); });
          li.appendChild(b);
          list.appendChild(li);
        });
        stage.appendChild(list);
      }
      buttons.forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-video') === name ? 'true' : 'false'); });
      var started = video.play();
      if (started && typeof started.catch === 'function') started.catch(function () {});
    }
    buttons.forEach(function (b) {
      b.addEventListener('click', function () { play(b.getAttribute('data-video')); });
    });
  })();
""" % json.dumps(data, sort_keys=True)


CSS = """
    body[data-page-kind="lesson"] .lesson-watch { max-width: 38rem; margin: 18px auto 8px; padding: 0; border: 0; background: none; }
    .watch-row { display: flex; flex-wrap: wrap; gap: .7rem; }
    .watch-btn { display: flex; align-items: center; gap: .75rem; padding: .65rem 1rem; border-radius: var(--radius-sm);
                 border: 1px solid var(--line-strong); background: var(--panel-2); color: var(--text); cursor: pointer;
                 font: inherit; text-align: left; }
    .watch-btn:hover, .watch-btn[aria-pressed="true"] { border-color: var(--cyan); }
    .watch-btn:focus-visible { outline: 3px solid var(--cyan); outline-offset: 2px; }
    .watch-play { display: inline-grid; place-items: center; width: 2.1rem; height: 2.1rem; border-radius: 50%%;
                  background: var(--cyan); color: var(--on-accent); font-size: .85rem; flex: 0 0 auto; }
    .watch-len { color: var(--muted); font-variant-numeric: tabular-nums; }
    .watch-btn small { display: block; color: var(--muted); font-size: .82rem; }
    .watch-stage { margin-top: 1rem; }
    .watch-stage video { display: block; width: 100%%; aspect-ratio: 16 / 9; background: #000; border-radius: var(--radius-sm); }
    .watch-stage.is-portrait video { aspect-ratio: 9 / 16; max-height: 80vh; width: auto; max-width: 100%%; margin: 0 auto; }
    .watch-chapters { list-style: none; margin: .7rem 0 0; padding: 0; display: flex; flex-wrap: wrap; gap: .4rem; }
    .watch-chapters button { font: inherit; font-size: .86rem; padding: .3rem .65rem; border-radius: 999px; cursor: pointer;
                             border: 1px solid var(--line); background: transparent; color: var(--muted); white-space: pre; }
    .watch-chapters button:hover { color: var(--text); border-color: var(--cyan); }
""".replace("%%", "%")

__all__ = ["published", "for_lesson", "markup", "script", "CSS", "esc"]
