"""/reels/: every published lesson's short video as one full-screen vertical feed.

The feed reads like a social reel: one reel per screen, snap scrolling (a swipe
on a phone, the wheel or trackpad on a desktop), the reel in view plays and
loops, the one that leaves pauses, and only the reel in view and its two
neighbours hold a <video> element at all, so a feed of 1,400 reels never holds
1,400 players. Arrow keys, j/k and PageUp/PageDown step; m toggles sound; a tap
pauses or resumes. The URL fragment follows the reel in view, so a lesson page
can link to its own reel at /reels/#<course>--<lesson>.

Self-containment (AGENTS.md section 2) decides the one place this differs from
loop.geterdone.io, which autoplays muted on load: here the page makes no request
beyond the document until the reader acts. No reel carries a src or poster in
its markup. Each reel is a static card (Subject, course, lesson title, a link to
the lesson) under a "Tap to start" overlay, and the media URLs live only in the
inline script's data, as they do in video.py. The first tap, click or key press
starts the reel in view WITH sound; from then on the feed autoplays.

The order is the library's: Subjects in scripts/catalog.py order, then each
Subject's courses and lessons in path order. A lesson appears only once
video/published.json lists a short for it.
"""

import json

from . import chrome
from .chrome import esc

URL = "/reels/"
RELATIVE = "reels/index.html"


def reel_id(course_slug, lesson_slug):
    """The fragment that names one reel. Slugs never contain "--", so it is unambiguous."""
    return "%s--%s" % (course_slug, lesson_slug)


def reels(paths, subjects, published):
    """[(reel id, "<course>/<lesson>", subject display, course title, lesson title)] in catalog order.

    `paths` are the generated PATH dicts, `subjects` the catalog entries (their
    order and optional short_title), `published` the video/published.json lessons.
    """
    by_slug = {path["slug"]: path for path in paths}
    out = []
    for entry in subjects:
        path = by_slug.get(entry["slug"])
        if path is None:  # Trading is hand-authored; its lessons carry no video yet
            continue
        display = entry.get("short_title", path["title"])
        for course in path["courses"]:
            for lesson in course["lessons"]:
                key = "%s/%s" % (course["slug"], lesson["slug"])
                if "short" in published.get(key, {}):
                    out.append((reel_id(course["slug"], lesson["slug"]), key, display,
                                course["title"], lesson["title"]))
    return out


def _reel(rid, key, subject, course, title):
    return (
        '        <article class="reel" id="%s"><div class="reel-frame"><div class="reel-info">'
        '<p class="reel-meta">%s &middot; %s</p><h2>%s</h2>'
        '<a class="btn primary" href="../%s/">Watch the full lesson</a></div></div></article>\n'
        % (esc(rid), esc(subject), esc(course), esc(title), esc(key))
    )


def body(listed):
    if not listed:
        return (
            '      <section class="reels-empty" data-ui="reel-feed">\n'
            '        <h1>Reels</h1>\n'
            '        <p>No reels are published yet. Each lesson gets a short video of its one idea, '
            'and they appear here as they are published.</p>\n'
            '        <p><a class="btn primary" href="../#paths">Browse subjects</a></p>\n'
            "      </section>\n"
        )
    return (
        '      <div class="reels-head"><h1>Reels</h1><p>One idea from each lesson in under a minute. '
        'Scroll or swipe for the next.</p></div>\n'
        '      <section class="reels-stage" id="reelsStage" data-ui="reel-feed" '
        'aria-label="Reels, one lesson each. Scroll, swipe or use the arrow keys for the next.">\n'
        '        <div class="reels-feed" id="reelsFeed">\n'
        "%s"
        "        </div>\n"
        '        <div class="reels-hud">\n'
        '          <div class="reels-frame-hud">\n'
        '            <p class="reels-count" id="reelsCount">1 / %d</p>\n'
        '            <button class="reels-sound" id="reelsSound" type="button" aria-pressed="true" hidden>Sound on</button>\n'
        '            <span class="reels-paused" aria-hidden="true">&#9654;</span>\n'
        '            <span class="reels-bar" aria-hidden="true"><span id="reelsBar"></span></span>\n'
        '            <button class="reels-start" id="reelsStart" type="button">'
        '<span class="reels-start-play" aria-hidden="true">&#9654;</span>'
        "<strong>Tap to start</strong><small>Plays with sound</small></button>\n"
        "          </div>\n"
        '          <div class="reels-nav">'
        '<button class="btn" type="button" data-step="-1" aria-label="Previous reel">&uarr;</button>'
        '<button class="btn" type="button" data-step="1" aria-label="Next reel">&darr;</button></div>\n'
        "        </div>\n"
        "      </section>\n"
        % ("".join(_reel(*r) for r in listed), len(listed))
    )


def script(listed):
    """The feed. Guarded so labcheck's and feedbackcheck's fake windows can run it."""
    data = {"base": "../video/", "ids": [key for _rid, key, _s, _c, _t in listed]}
    return """
  (function () {
    var REELS = %s;
    if (typeof document === 'undefined' || typeof document.getElementById !== 'function'
        || typeof document.createElement !== 'function') return;
    var stage = document.getElementById('reelsStage');
    var feed = document.getElementById('reelsFeed');
    if (!stage || !feed || typeof feed.querySelectorAll !== 'function' || !stage.classList) return;
    var reels = Array.prototype.slice.call(feed.querySelectorAll('.reel'));
    if (!reels.length || reels.length !== REELS.ids.length) return;
    var startBtn = document.getElementById('reelsStart');
    var soundBtn = document.getElementById('reelsSound');
    var countEl = document.getElementById('reelsCount');
    var bar = document.getElementById('reelsBar');
    var navBtns = Array.prototype.slice.call(stage.querySelectorAll('[data-step]'));
    var started = false, muted = false, current = -1, held = false;
    var videos = {};

    function make(i) {
      if (i < 0 || i >= reels.length || videos[i]) return;
      var base = REELS.base + REELS.ids[i] + '/short.';
      var v = document.createElement('video');
      v.className = 'reel-video';
      v.loop = true;
      v.muted = muted;
      v.playsInline = true;
      v.setAttribute('playsinline', '');
      v.preload = 'auto';
      v.poster = base + 'jpg';
      v.src = base + 'mp4';
      var track = document.createElement('track');
      track.kind = 'captions';
      track.label = 'English';
      track.srclang = 'en';
      track.src = base + 'vtt';
      v.appendChild(track);
      v.addEventListener('timeupdate', function () {
        if (videos[current] === v && v.duration) bar.style.width = (100 * v.currentTime / v.duration) + '%%';
      });
      v.addEventListener('play', function () { if (videos[current] === v) stage.classList.remove('is-paused'); });
      v.addEventListener('pause', function () { if (videos[current] === v) stage.classList.add('is-paused'); });
      var frame = reels[i].querySelector('.reel-frame');
      frame.insertBefore(v, frame.firstChild);
      reels[i].classList.add('has-video');
      videos[i] = v;
    }
    function drop(i) {
      var v = videos[i];
      delete videos[i];
      v.pause();
      v.removeAttribute('src');
      v.load();
      if (v.parentNode) v.parentNode.removeChild(v);
      reels[i].classList.remove('has-video');
    }
    function keepNeighbours() {
      Object.keys(videos).forEach(function (k) { if (Math.abs(k - current) > 1) drop(+k); });
      make(current); make(current + 1); make(current - 1);
    }
    function paintSound() {
      soundBtn.textContent = muted ? 'Sound off' : 'Sound on';
      soundBtn.setAttribute('aria-pressed', muted ? 'false' : 'true');
      Object.keys(videos).forEach(function (k) { videos[k].muted = muted; });
    }
    function playCurrent() {
      var v = videos[current];
      if (!v) return;
      held = false;
      v.muted = muted;
      var p = v.play();
      if (p && typeof p.catch === 'function') p.catch(function (e) {
        // A browser that will not play this element with sound gets it muted;
        // the sound button says so and one tap on it turns sound back on.
        if (e && e.name === 'NotAllowedError' && !muted && videos[current] === v) {
          muted = true; paintSound();
          var q = v.play();
          if (q && typeof q.catch === 'function') q.catch(function () { stage.classList.add('is-paused'); });
        }
      });
    }
    function show(i) {
      if (i === current || i < 0 || i >= reels.length) return;
      var old = videos[current];
      if (old) { old.pause(); try { old.currentTime = 0; } catch (e) {} }
      current = i;
      // The text node is kept and rewritten, never replaced.
      if (countEl.firstChild) countEl.firstChild.nodeValue = (i + 1) + ' / ' + reels.length;
      bar.style.width = '0';
      navBtns.forEach(function (b) {
        var to = i + Number(b.getAttribute('data-step'));
        b.hidden = to < 0 || to >= reels.length;
      });
      if (started) {
        if (history.replaceState) history.replaceState(null, '', '#' + reels[i].id);
        stage.classList.remove('is-paused');
        keepNeighbours();
        playCurrent();
      }
    }
    function start() {
      if (started) return;
      started = true;
      stage.classList.add('is-started');
      startBtn.hidden = true;
      soundBtn.hidden = false;
      if (typeof stage.scrollIntoView === 'function') stage.scrollIntoView({ block: 'start' });
      if (history.replaceState) history.replaceState(null, '', '#' + reels[current].id);
      keepNeighbours();
      paintSound();
      playCurrent();
    }
    // A sticky masthead (wide screens) sits over the top of the page, so the
    // stage is sized to the screen below it and scrolls to just under it.
    function fit() {
      var mh = document.querySelector('[data-ui="masthead"]'), top = 0;
      if (mh && typeof window.getComputedStyle === 'function'
          && /sticky|fixed/.test(window.getComputedStyle(mh).position)) {
        top = Math.ceil(mh.getBoundingClientRect().bottom) + 8;
      }
      stage.style.setProperty('--reels-top', top + 'px');
      stage.style.scrollMarginTop = top + 'px';
    }
    function inView() {
      var h = feed.clientHeight || 1;
      return Math.max(0, Math.min(reels.length - 1, Math.round(feed.scrollTop / h)));
    }
    function go(i, smooth) {
      i = Math.max(0, Math.min(reels.length - 1, i));
      var top = i * feed.clientHeight;
      if (typeof feed.scrollTo === 'function') feed.scrollTo({ top: top, behavior: smooth ? 'smooth' : 'auto' });
      else feed.scrollTop = top;
      if (!smooth) show(i);
    }
    function step(d) { go(current + d, true); }
    function toggleSound() {
      muted = !muted;
      paintSound();
      if (videos[current] && videos[current].paused && !held) playCurrent();
    }
    function togglePause() {
      var v = videos[current];
      if (!v) return;
      if (v.paused) playCurrent();
      else { held = true; v.pause(); }
    }
    function byHash() {
      var id = (location.hash || '').slice(1);
      try { id = decodeURIComponent(id); } catch (e) {}
      for (var i = 0; i < reels.length; i++) if (reels[i].id === id) return i;
      return -1;
    }

    var ticking = false;
    feed.addEventListener('scroll', function () {
      if (ticking) return;
      ticking = true;
      (window.requestAnimationFrame || setTimeout)(function () { ticking = false; show(inView()); });
    });
    feed.addEventListener('click', function (e) {
      if (e.target && typeof e.target.closest === 'function' && e.target.closest('a, button')) return;
      if (!started) start(); else togglePause();
    });
    startBtn.addEventListener('click', start);
    soundBtn.addEventListener('click', toggleSound);
    navBtns.forEach(function (b) {
      b.addEventListener('click', function () { start(); step(Number(b.getAttribute('data-step'))); });
    });
    var KEYS = { ArrowDown: 1, j: 1, PageDown: 1, ArrowUp: -1, k: -1, PageUp: -1 };
    document.addEventListener('keydown', function (e) {
      if (e.altKey || e.ctrlKey || e.metaKey) return;
      var t = e.target, tag = t && t.tagName;
      if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT' || (t && t.isContentEditable)) return;
      if (KEYS.hasOwnProperty(e.key)) { e.preventDefault(); start(); step(KEYS[e.key]); }
      else if (e.key === 'm') { if (started) toggleSound(); else start(); }
      else if (!started && (e.key === 'Enter' || e.key === ' ') && (t === document.body || t === document.documentElement)) {
        e.preventDefault(); start();
      }
    });
    window.addEventListener('hashchange', function () { var i = byHash(); if (i >= 0) go(i, false); });
    window.addEventListener('resize', function () { fit(); if (current >= 0) feed.scrollTop = current * feed.clientHeight; });
    document.addEventListener('visibilitychange', function () {
      var v = videos[current];
      if (!v) return;
      if (document.hidden) v.pause();
      else if (!held) playCurrent();
    });

    fit();
    var first = byHash();
    if (first >= 0) {
      if (typeof stage.scrollIntoView === 'function') stage.scrollIntoView({ block: 'start' });
      go(first, false);
    } else {
      show(inView());
    }
  })();
""" % json.dumps(data, separators=(",", ":"))


CSS = """
    body[data-page-kind="reels"] .shell { padding-bottom: 24px; }
    .reels-head { display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 16px; margin: 4px 0 4px; }
    body[data-page-kind="reels"] .reels-head h1 { margin: 0; font-size: 1.6rem; line-height: 1.2; }
    .reels-head p { margin: 0; color: var(--muted); }
    .reels-stage { position: relative; height: calc(100vh - var(--reels-top, 0px)); height: calc(100dvh - var(--reels-top, 0px)); margin: 8px 0 24px; border-radius: var(--radius-sm);
                   background: #05080c; color: #ffffff; }
    .reels-feed { height: 100%; border-radius: inherit; overflow-y: scroll; scroll-snap-type: y mandatory; scroll-behavior: auto;
                  overscroll-behavior-y: contain; scrollbar-width: none; outline: none; }
    .reels-feed::-webkit-scrollbar { display: none; }
    .reel { height: 100%; scroll-snap-align: start; scroll-snap-stop: always; display: flex; justify-content: center; }
    .reel-frame { position: relative; height: 100%; aspect-ratio: 9 / 16; max-width: 100%; overflow: hidden; cursor: pointer;
                  background-color: #0b1824; background-image: linear-gradient(160deg, #123247 0%, #0b1824 55%, #05080c 100%); }
    .reel-video { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; background: #000; display: block; }
    .reel-info { position: absolute; left: 0; right: 0; bottom: 0; padding: 72px 18px 26px; color: #ffffff;
                 background: linear-gradient(rgba(0, 0, 0, 0), rgba(0, 0, 0, .82) 45%); }
    .reel-meta { margin: 0; font-size: .86rem; color: #d7e2ea; }
    body[data-page-kind="reels"] .reel-info h2 { margin: 4px 0 14px; font-size: 1.3rem; line-height: 1.3; color: #ffffff; }
    .reel:not(.has-video) .reel-info { top: 0; padding-top: 72px; background: none; }
    .reel:not(.has-video) .reel-info h2 { font-size: clamp(1.5rem, 5vw, 2.1rem); }
    .reels-hud { position: absolute; inset: 0; display: flex; justify-content: center; pointer-events: none; }
    .reels-frame-hud { position: relative; height: 100%; aspect-ratio: 9 / 16; max-width: 100%; }
    .reels-hud button { pointer-events: auto; }
    .reels-count { position: absolute; top: 14px; left: 16px; margin: 0; padding: 2px 10px; border-radius: 999px;
                   background: rgba(0, 0, 0, .6); color: #ffffff; font-size: .82rem; font-variant-numeric: tabular-nums; }
    .reels-sound { position: absolute; top: 8px; right: 12px; padding: 6px 14px; border-radius: 999px; cursor: pointer;
                   border: 1px solid rgba(255, 255, 255, .5); background: rgba(0, 0, 0, .6); color: #ffffff; font: inherit; font-size: .85rem; }
    .reels-sound[aria-pressed="false"] { border-color: #ffd166; color: #ffd166; }
    .reels-sound:focus-visible, .reels-start:focus-visible { outline: 3px solid var(--cyan); outline-offset: 2px; }
    .reels-paused { position: absolute; top: 50%%; left: 50%%; transform: translate(-50%%, -50%%); font-size: 4rem;
                    color: rgba(255, 255, 255, .85); display: none; }
    .reels-stage.is-started.is-paused .reels-paused { display: block; }
    .reels-bar { position: absolute; left: 0; right: 0; bottom: 0; height: 4px; background: rgba(255, 255, 255, .2); }
    .reels-bar span { display: block; height: 100%%; width: 0; background: var(--cyan); transition: width .25s linear; }
    .reels-start { position: absolute; top: 62%%; left: 50%%; transform: translate(-50%%, -50%%); display: grid; justify-items: center;
                   gap: 6px; padding: 22px 30px; border-radius: 18px; border: 1px solid rgba(255, 255, 255, .45); cursor: pointer;
                   background: rgba(0, 0, 0, .72); color: #ffffff; font: inherit; }
    .reels-start strong { font-size: 1.15rem; }
    .reels-start small { color: #d7e2ea; font-size: .85rem; }
    .reels-start-play { display: grid; place-items: center; width: 64px; height: 64px; border-radius: 50%%;
                        background: var(--cyan); color: var(--on-accent); font-size: 1.6rem; }
    .reels-nav { position: absolute; right: 20px; top: 50%%; transform: translateY(-50%%); display: flex; flex-direction: column; gap: 10px; }
    body[data-page-kind="reels"] .reels-nav .btn { width: 48px; height: 48px; padding: 0; border-radius: 50%%; font-size: 1.2rem; }
    .reels-nav .btn[hidden] { display: none; }
    @media (max-width: 720px) {
      .reels-stage { margin: 8px -16px 16px; border-radius: 0; }
      .reels-nav { display: none; }
    }
    @media (prefers-reduced-motion: reduce) { .reels-bar span { transition: none; } }
""".replace("%%", "%")


def page(paths, subjects, published):
    """The /reels/ document."""
    listed = reels(paths, subjects, published)
    count = len(listed)
    description = ("Every lesson's short video in one vertical feed: one idea in under a minute, "
                   "each linking to its full lesson.")
    return "".join([
        chrome.head(title="Reels | Learn · geterdone.io", description=description,
                    canonical_path=URL, favicon=chrome.FAVICON_PATH, extra_css=CSS, page_kind="reels"),
        chrome.topbar(up="../"),
        chrome.crumbs([("Learn library", "../"), ("Reels", None)]),
        chrome.noscript(
            "<strong>JavaScript plays the reels.</strong> With scripting off each reel "
            "is a card that links to its lesson, and the lessons read normally."
        ) if count else "",
        '\n    <main id="main">\n',
        body(listed),
        "    </main>\n",
        chrome.footer(
            "<strong>Reels.</strong> Each reel is one idea from a lesson in under a minute. "
            "The lesson behind it has the full reading, the lab and the checks.",
            "a reel is a summary of a lesson, not a substitute for working through it."),
        chrome.close(script(listed) if count else ""),
    ])
