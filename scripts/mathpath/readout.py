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
      + 'nav,form,button,script,style,svg,canvas,[aria-hidden=true],[data-listen=skip]';
    var BLOCK = 'h1,h2,h3,h4,p,li,.mathblock,.lesson-row,.note,.callout>div,table,pre,'
      + '.defbox>.label,.thm>.label,.example>.label';
    var css = document.createElement('style');
    css.textContent = '.listen-bar{position:fixed;left:50%;bottom:16px;transform:translateX(-50%);z-index:60;'
      + 'display:flex;flex-wrap:wrap;gap:6px;align-items:center;padding:8px 10px;max-width:calc(100vw - 32px);'
      + 'background:var(--panel-solid);border:1px solid var(--line-strong);border-radius:var(--radius);box-shadow:var(--shadow)}'
      + '.listen-bar[hidden]{display:none}.listen-bar .btn,body[data-page-kind] .listen-bar .btn{padding:7px 11px;font-size:.83rem;white-space:nowrap}'
      + '.listen-status{font-size:.8rem;color:var(--muted);padding:0 4px}'
      + '.listen-voice{max-width:14em;min-height:44px;padding:6px 8px;font:inherit;font-size:.8rem;color:var(--text);'
      + 'background:var(--panel-2);border:1px solid var(--line-strong);border-radius:10px}.listen-voice[hidden]{display:none}'
      + '.listen-current{outline:2px solid var(--cyan);outline-offset:4px}'
      + '@media (max-width:560px){.listen-bar{left:16px;right:16px;transform:none;max-width:none;justify-content:space-between;gap:4px}'
      + '.listen-bar .btn,body[data-page-kind] .listen-bar .btn{flex:1 1 0;min-width:0;justify-content:center;white-space:nowrap;padding:7px 4px;font-size:.8rem}.listen-status{order:-1;flex:1 1 25%}'
      + '.listen-voice{order:-1;flex:1 1 60%;max-width:none}.listen-bar .btn,body[data-page-kind] .listen-bar .btn{flex-basis:18%}}'
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
      // Definition · Sets: a voice may say middle dot; it is a pause
      return spoken(el).replace(/\s+\u00b7\s+/g, ', ').replace(/\s+/g, ' ').trim();
    }
    // A Chrome network voice stops after about fifteen seconds of one
    // utterance, so a long block is spoken a sentence or two at a time.
    function chunks(s) {
      var parts = [];
      // No lookbehind: Safari before 16.4 cannot parse it, and this script
      // shares one <script> element with the theme, quiz, lab and progress code.
      s.replace(/([.!?;])\s+/g, '$1\n').split('\n').forEach(function (p) {
        parts = parts.concat(p.length > 220 ? p.replace(/,\s+/g, ',\n').split('\n') : [p]);
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
        next = btn('Next ›', 'Next paragraph'), speed = btn(rate + '×', 'Reading speed ' + rate + '×'),
        stop = btn('Stop'), status = document.createElement('span');
    status.className = 'listen-status';  // not live: 3 of 42 at each block would talk over the voice
    var picker = document.createElement('select');
    picker.className = 'listen-voice'; picker.setAttribute('aria-label', 'Voice'); picker.hidden = true;
    [prev, play, next, speed, stop, picker, status].forEach(function (n) { bar.appendChild(n); });
    document.body.appendChild(bar);

    // Voices differ more than anything else here: a neural voice (Edge Natural,
    // Apple Premium or Enhanced, Siri) sounds like a person and eSpeak like a
    // machine. Rank by what the name says, best first; the reader can override,
    // and the choice is remembered. The language is the page language, not the
    // browser language: a German browser must not read English with a German voice.
    var voice = null, voices = [];
    function quality(v) {
      if (/natural|neural|premium|enhanced|siri/i.test(v.name)) return 3;
      if (/google|online/i.test(v.name)) return 2;
      return /espeak/i.test(v.name) ? 0 : 1;
    }
    function pickVoice() {
      var lang = (document.documentElement.lang || 'en').slice(0, 2), saved = null;
      voices = synth.getVoices().filter(function (v) { return v.lang.slice(0, 2) === lang; });
      voices.sort(function (a, b) {
        return quality(b) - quality(a) || (b.default ? 1 : 0) - (a.default ? 1 : 0) || (a.name < b.name ? -1 : 1);
      });
      try { saved = localStorage.getItem('learn-listen-voice'); } catch (e) {}
      voice = voices.filter(function (v) { return v.voiceURI === saved; })[0] || voices[0] || null;
      picker.textContent = '';
      voices.forEach(function (v) {
        var o = document.createElement('option');
        o.textContent = v.name.replace(/^(Microsoft|Google) /, '').replace(/ - .*$/, '');
        o.selected = v === voice;
        picker.appendChild(o);
      });
      picker.hidden = voices.length < 2;
    }
    pickVoice();
    if ('onvoiceschanged' in synth) synth.addEventListener('voiceschanged', pickVoice);
    picker.addEventListener('change', function () {
      voice = voices[picker.selectedIndex] || null;
      try { localStorage.setItem('learn-listen-voice', voice ? voice.voiceURI : ''); } catch (e) {}
      if (playing) say();
    });

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
    function count() { status.removeAttribute('role'); status.textContent = (at + 1) + ' of ' + blocks.length; }
    function fail() { status.setAttribute('role', 'alert'); status.textContent = 'No voice is available on this device'; }
    function say() {
      var mine = ++token, busy = synth.speaking || synth.pending;
      if (busy) synth.cancel();
      if (at >= blocks.length) { finish(); return; }
      var b = blocks[at];
      mark(b.el);
      count();
      var u = new SpeechSynthesisUtterance(b.parts[part]);
      u.rate = rate; u.lang = document.documentElement.lang || 'en';
      if (voice) u.voice = voice;
      u.onstart = function () { heard = true; if (mine === token) count(); };
      u.onend = function () {
        if (mine !== token || !playing) return;
        if (++part >= b.parts.length) { part = 0; at++; }
        say();
      };
      u.onerror = function (e) {
        if (mine !== token || e.error === 'interrupted' || e.error === 'canceled') return;
        playing = false; play.textContent = 'Play'; fail();
      };
      // Chrome (Android especially) can drop an utterance spoken in the same
      // tick as a cancel.
      if (busy) setTimeout(function () { if (mine === token) synth.speak(u); }, 0);
      else synth.speak(u);
    }
    function go(i) { at = Math.max(0, Math.min(blocks.length - 1, i)); part = 0; if (playing) say(); else { mark(blocks[at].el); count(); } }
    function begin() {
      bar.hidden = false; playing = true; play.textContent = 'Pause'; heard = false;
      say();
      setTimeout(function () {
        if (playing && !heard) fail();
      }, 2500);
    }
    function finish() {
      playing = false; token++; synth.cancel(); mark(null);
      bar.hidden = true; at = 0; part = 0; start.focus({ preventScroll: true });
    }
    start.addEventListener('click', function () {
      if (bar.hidden) { at = 0; part = 0; }
      begin();
      play.focus({ preventScroll: true });  // the bar sits at the end of <body>
    });
    // Pause and speed resume from the current sentence, not the start of the block.
    play.addEventListener('click', function () {
      if (playing) { playing = false; token++; synth.cancel(); play.textContent = 'Play'; }
      else begin();
    });
    prev.addEventListener('click', function () { go(at - 1); });
    next.addEventListener('click', function () { go(at + 1); });
    stop.addEventListener('click', finish);
    speed.addEventListener('click', function () {
      rate = RATES[(RATES.indexOf(rate) + 1) % RATES.length];
      speed.textContent = rate + '×';
      speed.setAttribute('aria-label', 'Reading speed ' + rate + '×');
      try { localStorage.setItem('learn-listen-rate', String(rate)); } catch (e) {}
      if (playing) say();
    });
    addEventListener('pagehide', function () {
      token++; synth.cancel(); playing = false; play.textContent = 'Play';  // a back/forward-cache restore comes back paused
    });
  })();
"""
