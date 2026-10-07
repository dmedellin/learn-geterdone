"""Listen: the lesson read aloud by the browser's own voice.

`window.speechSynthesis` speaks in the reader's browser, so the page makes no
request and the self-containment invariant holds. Math is spoken from the
`data-say` attribute that render.py writes on every math run (speech.py
computes it at build time); everything else is the visible text.

The script builds its own button and player bar, so the same block serves the
generated lessons (appended by render.lesson_page_with_lab) and the hand-written
trading lessons (inserted between markers by scripts/add_progress_marks.py)
without editing either page's markup. It does nothing at all in a browser with
no speech engine.

What is read, in order: the visible teaching text inside <main> -- headings,
paragraphs, list items, math blocks, the mistakes and the understanding check.
Never read: the lab (it is driven, not read), the quiz, the feedback form,
kickers and eyebrows (they repeat the heading), and anything marked
data-listen="skip". A table or a code block is announced rather than read cell
by cell.
"""

READOUT_JS = r"""
  (function () {
    var synth = window.speechSynthesis, main = document.getElementById('main');
    if (!synth || !window.SpeechSynthesisUtterance || !main) return;
    var SKIP = '#lab,.quiz,.feedback,.hero-actions,.hero-card,.eyebrow,.kicker,.float-label,'
      + 'nav,form,button,script,style,svg,canvas,[aria-hidden="true"],[data-listen="skip"]';
    var BLOCK = 'h1,h2,h3,h4,p,li,.mathblock,.lesson-row,.note,.callout>div,table,pre,'
      + '.defbox>.label,.thm>.label,.example>.label';
    var css = document.createElement('style');
    css.textContent = '.listen-bar{position:fixed;left:50%;bottom:16px;transform:translateX(-50%);z-index:60;'
      + 'display:flex;flex-wrap:wrap;gap:6px;align-items:center;padding:8px 10px;max-width:calc(100vw - 32px);'
      + 'background:var(--panel-solid);border:1px solid var(--line-strong);border-radius:var(--radius);box-shadow:var(--shadow)}'
      + '.listen-bar[hidden]{display:none}.listen-bar .btn,body[data-page-kind] .listen-bar .btn{padding:7px 11px;font-size:.83rem;white-space:nowrap}'
      + '.listen-status{font-size:.8rem;color:var(--muted);padding:0 4px}'
      + '.listen-current{outline:2px solid var(--cyan);outline-offset:4px;border-radius:4px}'
      + '@media (max-width:560px){.listen-bar{left:16px;right:16px;transform:none;max-width:none;justify-content:space-between;gap:4px}'
      + '.listen-bar .btn,body[data-page-kind] .listen-bar .btn{flex:1 1 0;min-width:0;justify-content:center;white-space:nowrap;padding:7px 4px;font-size:.8rem}.listen-status{order:-1;flex-basis:100%;text-align:center}}'
      + '@media print{.listen-bar,.listen-start{display:none}}';
    document.head.appendChild(css);

    function spoken(node) {
      if (node.nodeType === 3) return node.nodeValue;
      if (node.nodeType !== 1 || node.matches(SKIP) || node.classList.contains('qed')) return '';
      if (node.hasAttribute('data-say')) return ' ' + node.getAttribute('data-say') + ' ';
      var out = '';
      for (var c = node.firstChild; c; c = c.nextSibling) out += spoken(c);
      return out + ' ';  // <strong>Finish.</strong><p>You ... must not run together
    }
    function text(el) {
      if (el.matches('table')) return 'a table, shown on the page.';
      if (el.matches('pre')) return 'a code block, shown on the page.';
      // "Definition · Sets": a voice may say "middle dot"; it is a pause
      return spoken(el).replace(/\s+\u00b7\s+/g, ', ').replace(/\s+/g, ' ').trim();
    }
    // A Chrome network voice stops after about fifteen seconds of one
    // utterance, so a long block is spoken a sentence or two at a time.
    function chunks(s) {
      var parts = [];
      s.split(/(?<=[.!?;])\s+/).forEach(function (p) {
        parts = parts.concat(p.length > 220 ? p.split(/(?<=,)\s+/) : [p]);
      });
      var out = [], cur = '';
      parts.forEach(function (p) {
        if (cur && (cur + ' ' + p).length > 220) { out.push(cur); cur = p; }
        else cur = cur ? cur + ' ' + p : p;
      });
      if (cur) out.push(cur);
      return out;
    }
    var blocks = [];
    main.querySelectorAll(BLOCK).forEach(function (el) {
      if (el.closest(SKIP) || (el.parentElement && el.parentElement.closest(BLOCK))) return;
      if (!el.getClientRects().length) return;
      var t = text(el);
      if (t) blocks.push({ el: el, parts: chunks(t) });
    });
    if (!blocks.length) return;

    var RATES = [0.8, 1, 1.25, 1.5], rate = 1;
    try { rate = +localStorage.getItem('learn-listen-rate') || 1; } catch (e) {}
    if (RATES.indexOf(rate) < 0) rate = 1;
    var voice = null;
    function pickVoice() {
      var lang = (navigator.language || 'en').slice(0, 2), vs = synth.getVoices();
      voice = vs.filter(function (v) { return v.default && v.lang.slice(0, 2) === lang; })[0]
        || vs.filter(function (v) { return v.lang.slice(0, 2) === lang; })[0] || null;
    }
    pickVoice();
    if ('onvoiceschanged' in synth) synth.addEventListener('voiceschanged', pickVoice);

    function btn(label, aria) {
      var b = document.createElement('button');
      b.type = 'button'; b.className = 'btn ghost'; b.textContent = label;
      if (aria) b.setAttribute('aria-label', aria);
      return b;
    }
    var start = btn('Listen', 'Listen to this lesson');
    start.classList.add('listen-start');
    var actions = main.querySelector('.hero-actions');
    if (actions) actions.appendChild(start);
    else { var h1 = main.querySelector('h1'); if (!h1) return; h1.insertAdjacentElement('afterend', start); }

    var bar = document.createElement('div');
    bar.className = 'listen-bar'; bar.hidden = true;
    bar.setAttribute('role', 'region'); bar.setAttribute('aria-label', 'Listen');
    var prev = btn('‹ Back', 'Previous paragraph'), play = btn('Pause'),
        next = btn('Next ›', 'Next paragraph'), speed = btn(rate + '×', 'Reading speed'),
        stop = btn('Stop'), status = document.createElement('span');
    status.className = 'listen-status'; status.setAttribute('aria-live', 'polite');
    [prev, play, next, speed, stop, status].forEach(function (n) { bar.appendChild(n); });
    document.body.appendChild(bar);

    var at = 0, part = 0, playing = false, token = 0, heard = false, current = null;
    var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
    function mark(el) {
      if (current) current.classList.remove('listen-current');
      current = el;
      if (!el) return;
      el.classList.add('listen-current');
      var r = el.getBoundingClientRect();
      if (r.top < 0 || r.bottom > innerHeight - 80)
        el.scrollIntoView({ block: 'center', behavior: reduce ? 'auto' : 'smooth' });
    }
    function say() {
      var mine = ++token;
      synth.cancel();
      if (at >= blocks.length) { finish(); return; }
      var b = blocks[at];
      mark(b.el);
      status.textContent = (at + 1) + ' of ' + blocks.length;
      var u = new SpeechSynthesisUtterance(b.parts[part]);
      u.rate = rate; u.lang = document.documentElement.lang || 'en';
      if (voice) u.voice = voice;
      u.onstart = function () { heard = true; };
      u.onend = function () {
        if (mine !== token || !playing) return;
        if (++part >= b.parts.length) { part = 0; at++; }
        say();
      };
      u.onerror = function (e) {
        if (mine !== token || e.error === 'interrupted' || e.error === 'canceled') return;
        playing = false; play.textContent = 'Play';
        status.textContent = 'No voice is available on this device';
      };
      synth.speak(u);
    }
    function go(i) { at = Math.max(0, Math.min(blocks.length - 1, i)); part = 0; if (playing) say(); else { mark(blocks[at].el); status.textContent = (at + 1) + ' of ' + blocks.length; } }
    function begin() {
      bar.hidden = false; playing = true; play.textContent = 'Pause'; heard = false;
      say();
      setTimeout(function () {
        if (playing && !heard) status.textContent = 'No voice is available on this device';
      }, 2500);
    }
    function finish() {
      playing = false; token++; synth.cancel(); mark(null);
      bar.hidden = true; at = 0; part = 0; start.focus();
    }
    start.addEventListener('click', function () { if (bar.hidden) { at = 0; part = 0; } begin(); });
    play.addEventListener('click', function () {
      if (playing) { playing = false; token++; synth.cancel(); play.textContent = 'Play'; }
      else { part = 0; begin(); }
    });
    prev.addEventListener('click', function () { go(at - 1); });
    next.addEventListener('click', function () { go(at + 1); });
    stop.addEventListener('click', finish);
    speed.addEventListener('click', function () {
      rate = RATES[(RATES.indexOf(rate) + 1) % RATES.length];
      speed.textContent = rate + '×';
      try { localStorage.setItem('learn-listen-rate', String(rate)); } catch (e) {}
      if (playing) { part = 0; say(); }
    });
    addEventListener('pagehide', function () { token++; synth.cancel(); });
  })();
"""
