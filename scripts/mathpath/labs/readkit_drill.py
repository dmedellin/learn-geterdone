"""readkit_drill -- the drill engine every timed reading on a readkit page runs.

Browser only, and inert until a button is clicked: rdDrillInit() attaches
click and key handlers and does nothing else, so the labcheck shim (which
never clicks) sees no timer, no animation and no flash (PLAN D.0, D.2).

A page carries SLOTS = {key: slot} (key '' for a single drill, 'A'/'B' for a
comparison, '1'..'4' for runs, 'W' for a warm-up). A slot names its passage,
its display, whether questions follow, and `write`: which of the view's text
inputs its measurement fills ({words: 'wordsA', seconds: 'secondsA', ...}).
Score writes those inputs through rdWrite() -- the same path a preset takes --
so the tiles come from one computation whichever source filled the boxes.

Flows: read (Start, Done, questions, Score), sections (Next section between),
reread (two readings, no questions), recall (free recall, then idea-unit
ticks), inspect (a time-limited look, then questions), find (click the
answer to each prompt), coverage (click the words you do not know), practice
(a pool passage or pasted text, pacer optional, "test reading" tick).

Displays: normal, pacer, mask, rsvp, phrases, gist, preview, aloud. Every
timed step is a setTimeout chain started from a click; times are measured
with performance.now() and kept only as whole milliseconds.
"""

RD_DRILL_JS = r"""
  /* ---- the drill engine (browser only; nothing here runs until a click) ---- */
  var RD_ST = {};
  var RD_TIMED = { pacer: 1, mask: 1, rsvp: 1, phrases: 1 };
  function rdE(name, k) { return document.getElementById(name + k); }
  function rdShow(el, on) { if (el) el.style.display = on ? '' : 'none'; }
  function rdMsg(k, text) { var m = rdE('rdMsg', k); if (m) m.textContent = text; }
  function rdMsText(ms) {
    ms = Math.max(1, Math.round(ms));
    var w = Math.floor(ms / 1000), f = ms % 1000;
    return f ? w + '.' + String(f + 1000).slice(1).replace(/0+$/, '') : String(w);
  }
  function rdSpecId(key) { for (var i = 0; i < SPEC.length; i++) if (SPEC[i].key === key) return SPEC[i].id; return null; }
  /* Tokens as spans; data-i is the token's index in the whole passage. */
  function rdTokHtml(paras, clickable) {
    var n = 0;
    return paras.map(function (p) {
      var head = rdHeading(p), toks = rdTokens(p).map(function (t) {
        var w = rdIsWord(t);
        return '<span class="rdw" data-i="' + (n++) + '"' + (w ? ' data-w="1"' : '')
          + (clickable && w ? ' tabindex="0" role="button"' : '') + '>' + rdEsc(t) + '</span>';
      }).join(' ');
      return head ? '<h4 style="margin:10px 0 4px;">' + toks + '</h4>' : '<p>' + toks + '</p>';
    }).join('');
  }
  function rdClearTimers(st) { (st.timers || []).forEach(function (t) { clearTimeout(t); }); st.timers = []; }
  function rdLater(st, fn, ms) { st.timers.push(setTimeout(fn, Math.max(0, ms))); }
  function rdPassageOf(k) { var S = SLOTS[k], st = RD_ST[k]; return st.passage || (S.passage ? PASSAGES[S.passage] : null); }
  function rdTargetOf(k) {
    var S = SLOTS[k], text = S.targetKey ? field(rdSpecId(S.targetKey)).value : S.target, r = Rparse(rdClean(text));
    return r && Rsign(r) > 0 ? Number(r.n) / Number(r.d) : null;
  }
  function rdButtons(k, start, done, next) {
    rdShow(rdE('rdStart', k), start); rdShow(rdE('rdDone', k), done); rdShow(rdE('rdNext', k), next);
  }
  function rdHideText(k) { var t = rdE('rdText', k); t.innerHTML = ''; rdShow(t, false); }
  function rdResetSlot(k, keepOut) {
    var st = RD_ST[k];
    rdClearTimers(st);
    RD_ST[k] = { phase: 'idle', timers: [], ms: 0 };
    rdHideText(k);
    var w = rdE('rdWork', k); w.innerHTML = ''; rdShow(w, false);
    if (!keepOut) rdE('rdOut', k).innerHTML = '';
    var s = rdE('rdStart', k); s.textContent = 'Start';
    rdE('rdDone', k).textContent = 'Done';
    rdButtons(k, true, false, false);
    rdMsg(k, SLOTS[k].intro);
  }

  /* The first of these passage ids that the log does not hold yet, or null. */
  function rdFirstUnlogged(ids) {
    var used = {};
    rdLogRead().forEach(function (e) { used[e.passage] = true; });
    for (var i = 0; i < ids.length; i++) if (!used[ids[i]]) return ids[i];
    return null;
  }
  var RD_STREAM_CAP = 600;
  /* ---- reading ---- */
  function rdStart(k) {
    var S = SLOTS[k], st = RD_ST[k];
    if (st.phase === 'reread1') { rdBeginRead(k); return; }
    rdResetSlot(k, false);
    st = RD_ST[k];
    st.display = S.display; st.kind = S.kind;
    if (S.flow === 'practice' && !rdPracticeSetup(k)) return;
    if (S.pool && S.flow !== 'practice') {
      var id = rdFirstUnlogged(S.pool);
      if (!id) { rdMsg(k, 'Every passage offered here is already in your log; reading one again would measure your memory of it.'); return; }
      st.passage = PASSAGES[id];
      if (S.kinds && S.kinds[id]) st.kind = S.kinds[id];
    }
    var P = rdPassageOf(k);
    if (!P) { rdMsg(k, 'There is no passage to read.'); return; }
    if (RD_TIMED[st.display]) {
      st.target = rdTargetOf(k);
      if (!st.target) { rdMsg(k, 'Type a target rate in words per minute (more than 0) first.'); return; }
      if ((st.display === 'rsvp' || st.display === 'phrases') && st.target > RD_STREAM_CAP) {
        rdMsg(k, 'This display runs at ' + RD_STREAM_CAP + ' wpm or less: beyond that it is a flicker, not reading. Set a lower target.');
        return;
      }
    }
    rdBeginRead(k);
  }
  function rdBeginRead(k) {
    var S = SLOTS[k], st = RD_ST[k], P = rdPassageOf(k), text = rdE('rdText', k), d = st.display;
    rdShow(text, true);
    rdButtons(k, false, true, S.flow === 'sections' || S.flow === 'find');
    if (S.flow === 'find') { rdFindBegin(k); return; }
    if (S.flow === 'coverage') {
      text.innerHTML = rdTokHtml(P.paragraphs, true); st.phase = 'mark'; st.t0 = performance.now();
      rdE('rdDone', k).textContent = 'Count my marks';
      rdMsg(k, 'Click (or Tab to and press Enter on) every word you do not know; click again to unmark. Then press Count my marks.');
      return;
    }
    var again = st.phase === 'reread1';
    st.phase = again ? 'reread2' : 'reading';
    var paras = P.paragraphs;
    if (S.flow === 'sections') paras = P.paragraphs.slice(0, S.split);
    if (d === 'gist') paras = rdGistParas(P);
    if (d === 'preview') paras = rdPreviewParas(P);
    st.t0 = performance.now();
    if (d === 'rsvp' || d === 'phrases') { rdStream(k, P); return; }
    text.innerHTML = rdTokHtml(paras, false);
    var say = { normal: 'Read at your usual pace and press Done when you finish.',
                aloud: 'Read the passage ALOUD at a natural pace and press Done when you finish speaking.',
                pacer: 'Keep your eyes on the highlighted line as it moves.',
                mask: 'Keep up with the highlighted line; the lines above it disappear.',
                gist: 'Skim: only headings and first sentences are shown, and they disappear after ' + S.limit + ' s.',
                preview: 'Preview: headings, the first and the last paragraph, for ' + S.limit + ' s; then the whole passage. The clock runs through both.' };
    var m = say[d] || say.normal;
    if (d === 'normal' && S.limit && S.flow !== 'inspect') m = 'The passage disappears after ' + S.limit + ' s; press Done if you finish first.';
    if (S.say) m = S.say + ' Press Done when you finish.';
    rdMsg(k, again ? 'Read it again, then press Done.' : (S.flow === 'sections' ? 'Section 1 of 2. Press Next section when you reach its end. ' : '') + m);
    if (d === 'pacer' || d === 'mask') rdPacer(k);
    if (d === 'gist' || (S.limit && S.flow === 'inspect')) rdLater(st, function () { rdFinish(k); }, S.limit * 1000);
    if (d === 'preview') rdLater(st, function () {
      if (st.phase !== 'reading') return;
      text.innerHTML = rdTokHtml(P.paragraphs, false);
      rdMsg(k, 'Now the whole passage. Press Done when you finish.');
    }, S.limit * 1000);
    if (S.limit && (d === 'pacer' || d === 'mask' || d === 'normal') && S.flow !== 'inspect') rdLater(st, function () { rdFinish(k); }, S.limit * 1000);
  }
  function rdNextSection(k) {
    var S = SLOTS[k], st = RD_ST[k], P = rdPassageOf(k);
    if (S.flow === 'find') { rdFindStep(k, false); return; }
    if (st.phase !== 'reading' || st.split !== undefined) return;
    st.split = Math.round(performance.now() - st.t0);
    rdE('rdText', k).innerHTML = rdTokHtml(P.paragraphs.slice(S.split), false);
    rdShow(rdE('rdNext', k), false);
    rdMsg(k, 'Section 2 of 2. Press Done when you finish.');
  }
  function rdFinish(k) {
    var S = SLOTS[k], st = RD_ST[k];
    if (st.phase === 'mark') { rdCoverageScore(k); return; }
    if (st.phase !== 'reading' && st.phase !== 'reread2') return;
    if (S.flow === 'sections' && st.split === undefined) { rdMsg(k, 'Press Next section first, at the end of section 1.'); return; }
    rdClearTimers(st);
    st.ms += Math.max(1, Math.round(performance.now() - st.t0));
    rdHideText(k);
    rdButtons(k, false, false, false);
    if (S.flow === 'reread') {
      if (st.phase === 'reading') {
        st.phase = 'reread1';
        var s = rdE('rdStart', k); s.textContent = 'Read it again'; rdShow(s, true);
        rdMsg(k, 'Now read the same passage a second time. Press Read it again when you are ready.');
        return;
      }
      st.phase = 'done'; rdLogReread(k); return;
    }
    st.phase = 'after';
    if (S.tick) { rdTickAsk(k); return; }
    rdAfterReading(k);
  }
  /* A box the reader ticks (or not) after Done: kept in the entry's extra. */
  function rdTickAsk(k) {
    var S = SLOTS[k], w = rdE('rdWork', k), st = RD_ST[k];
    rdShow(w, true);
    /* A count tick (lapses) is a number box; any other is a checkbox. */
    w.innerHTML = '<label class="small-copy">' + (S.tick.count ? rdEsc(S.tick.label) + ': <input type="number" min="0" step="1" value="0" style="width:5rem;">'
      : '<input type="checkbox"> ' + rdEsc(S.tick.label)) + '</label> <button class="btn small" type="button">Continue</button>';
    w.getElementsByTagName('button')[0].addEventListener('click', function () {
      var box = w.getElementsByTagName('input')[0];
      st.tick = S.tick.count ? Math.max(0, Math.floor(+box.value) || 0) : !!box.checked;
      rdAfterReading(k);
    });
  }
  function rdAfterReading(k) {
    var S = SLOTS[k], st = RD_ST[k], P = rdPassageOf(k);
    if (S.flow === 'recall') { rdRecallWrite(k); return; }
    var qs = S.questions && P.questions ? P.questions.filter(function (q) { return S.qkinds !== 'gist' || q.kind === 'gist'; }) : [];
    st.qs = qs;
    if (!qs.length) { rdScore(k, []); return; }
    rdMsg(k, 'The passage is hidden. Answer each question; there is no going back.');
    rdAsk(rdE('rdWork', k), qs, function (answers) {
      var w = rdE('rdWork', k);
      w.innerHTML = '<button class="btn small primary" type="button">Score</button>';
      w.firstChild.addEventListener('click', function () { rdScore(k, answers); });
      rdMsg(k, 'All answered. Press Score.');
    });
  }
  /* One question at a time, four options, no going back; done(answers). */
  function rdAsk(work, qs, done) {
    var answers = [];
    rdShow(work, true);
    function ask(n) {
      if (n >= qs.length) { done(answers); return; }
      var q = qs[n];
      work.innerHTML = '<p class="small-copy" style="margin:0 0 6px;">Question ' + (n + 1) + ' of ' + qs.length + '</p><p><strong>'
        + rdEsc(q.q) + '</strong></p><div class="choice-grid">' + q.a.map(function (a, i) {
          return '<button class="choice" type="button" data-a="' + i + '">' + rdEsc(a) + '</button>';
        }).join('') + '</div>';
      var bs = work.getElementsByTagName('button');
      for (var i = 0; i < bs.length; i++) bs[i].addEventListener('click', function (e) {
        answers.push(+e.currentTarget.getAttribute('data-a')); ask(n + 1);
      });
      if (bs[0]) bs[0].focus();
    }
    ask(0);
  }
  function rdTally(qs, answers) {
    var t = { correct: 0, total: qs.length, gist: 0, gistTotal: 0, detail: 0, detailTotal: 0 };
    qs.forEach(function (q, i) {
      var ok = answers[i] === q.c;
      if (ok) t.correct += 1;
      t[q.kind + 'Total'] += 1;
      if (ok) t[q.kind] += 1;
    });
    return t;
  }
  function rdReview(qs, answers) {
    if (!qs.length) return '';
    return '<ol class="small-copy">' + qs.map(function (q, i) {
      var ok = answers[i] === q.c;
      return '<li><strong>' + (ok ? 'Right' : 'Wrong') + '.</strong> ' + rdEsc(q.q) + ' Your answer: ' + rdEsc(q.a[answers[i]])
        + (ok ? '' : '; the passage says: ' + rdEsc(q.a[q.c])) + '</li>';
    }).join('') + '</ol>';
  }
  function rdScore(k, answers) {
    var S = SLOTS[k], st = RD_ST[k], P = rdPassageOf(k), t = rdTally(st.qs || [], answers);
    var words = rdPassageWords(P), sec = rdMsText(st.ms), vals = {};
    var got = { words: words, chars: rdPassageChars(P), seconds: sec, correct: t.correct, total: t.total,
                gist: t.gist, gistTotal: t.gistTotal, detail: t.detail, detailTotal: t.detailTotal,
                found: t.correct, targets: t.total, phrases: rdPhrases(P).length };
    if (st.display === 'gist') got.shown = rdWordsIn(rdGistParas(P));
    if (S.tick && S.tick.count) got.lapses = st.tick;
    if (S.flow === 'sections') {
      got.words1 = rdWordsIn(P.paragraphs.slice(0, S.split)); got.words2 = rdWordsIn(P.paragraphs.slice(S.split));
      got.seconds1 = rdMsText(st.split); got.seconds2 = rdMsText(st.ms - st.split);
    }
    Object.keys(S.write || {}).forEach(function (g) { if (got[g] !== undefined) vals[S.write[g]] = got[g]; });
    if (Object.keys(vals).length) rdWrite(vals);
    var rate = rdRate(R(BigInt(words)), Rparse(sec));
    /* A skim is not a reading rate: its line gives the time and the gist score only. */
    var line = (st.display === 'gist' ? 'Skimmed for ' + rdUnit(Rparse(sec), 's') : rdFig(R(BigInt(words))) + ' words in ' + rdUnit(Rparse(sec), 's') + ': ' + rdUnit(rate, 'wpm'))
      + (t.total ? ', ' + t.correct + ' of ' + t.total + ' right' : ', no questions') + '.'
      + (S.tick && st.tick !== undefined ? ' (' + S.tick.label + ': ' + (S.tick.count ? st.tick : st.tick ? 'yes' : 'no') + '.)' : '');
    rdE('rdOut', k).innerHTML = rdEsc(line) + rdReview(st.qs || [], answers);
    rdLogAppend({ mode: S.mode, view: S.view, side: k, passage: P.id || 'pasted', display: st.display, words: words, chars: got.chars,
                  ms: st.ms, correct: t.correct, total: t.total, kind: st.kind,
                  extra: { gist: t.gist, gistTotal: t.gistTotal, detail: t.detail, detailTotal: t.detailTotal,
                           target: st.target || null, split: st.split === undefined ? null : st.split, order: S.order || null,
                           kept: S.tick && S.tick.key === 'kept' ? !!st.tick : null,
                           lapse: S.tick && S.tick.key === 'lapse' ? !!st.tick : null,
                           lapses: S.tick && S.tick.count ? st.tick : null } }, rdE('rdMsg', k));
    var w = rdE('rdWork', k); w.innerHTML = ''; rdShow(w, false);
    st.phase = 'idle';
    var s = rdE('rdStart', k); s.textContent = 'Start again'; rdShow(s, true);
    rdMsg(k, 'Scored and logged. Reading the same passage again measures your memory of it, not your reading.');
    if (typeof rdAfterScore === 'function') rdAfterScore(k);
  }
  function rdDrillInit() {
    Object.keys(SLOTS).forEach(function (k) {
      RD_ST[k] = { phase: 'idle', timers: [], ms: 0 };
      var S = SLOTS[k];
      rdE('rdStart', k).addEventListener('click', function () { rdStart(k); });
      rdE('rdDone', k).addEventListener('click', function () { rdFinish(k); });
      rdE('rdReset', k).addEventListener('click', function () { rdResetSlot(k, false); rdMsg(k, 'Reset: nothing was logged. ' + S.intro); });
      var nx = rdE('rdNext', k);
      if (nx) nx.addEventListener('click', function () { rdNextSection(k); });
      if (rdE('rdAlt', k) && typeof rdAloudInit === 'function') rdAloudInit(k);
      if ((S.flow === 'find' || S.flow === 'coverage') && typeof rdFindInit === 'function') rdFindInit(k);
    });
  }
"""

# The timed displays (pacer, mask, rsvp, phrases): shipped only where a slot uses one.
RD_TIMED_JS = r"""
  /* The pacer: lines are read from layout when it starts (word spans grouped
     by offsetTop); each line is lit for its words x 60,000 / target ms. */
  function rdPacer(k) {
    var st = RD_ST[k], spans = rdE('rdText', k).getElementsByClassName('rdw'), lines = [], top = null;
    for (var i = 0; i < spans.length; i++) {
      var s = spans[i];
      if (top === null || s.offsetTop > top + 2 || s.offsetTop < top - 2) { lines.push([]); top = s.offsetTop; }
      lines[lines.length - 1].push(s);
    }
    var at = 0;
    function words(line) { return line.filter(function (s) { return s.getAttribute('data-w'); }).length; }
    function light(n) {
      if (st.phase !== 'reading') return;
      lines.forEach(function (line, j) {
        line.forEach(function (s) {
          s.style.background = j === n ? 'var(--line-strong)' : '';
          s.style.boxShadow = j === n ? 'inset 0 -2px 0 currentColor' : '';
          s.style.visibility = (st.display === 'mask' && j < n) ? 'hidden' : '';
        });
      });
      if (n >= lines.length) { rdFinish(k); return; }
      at += Math.max(1, words(lines[n])) * 60000 / st.target;
      rdLater(st, function () { light(n + 1); }, st.t0 + at - performance.now());
    }
    light(0);
  }
  /* RSVP (chunk words at a time) and phrases: centred, ends by itself. */
  function rdStream(k, P) {
    var S = SLOTS[k], st = RD_ST[k], text = rdE('rdText', k), items = [];
    if (st.display === 'phrases') {
      items = rdPhrases(P).map(function (t) { return { t: t, w: rdWordCount(t) }; });
    } else {
      var toks = [];
      P.paragraphs.forEach(function (p) { rdTokens(p).forEach(function (t) {
        if (rdIsWord(t) || !toks.length) toks.push(t); else toks[toks.length - 1] += ' ' + t;
      }); });
      for (var i = 0; i < toks.length; i += S.chunk) items.push({ t: toks.slice(i, i + S.chunk).join(' '), w: S.chunk });
    }
    text.innerHTML = '<div style="min-height:5rem;display:flex;align-items:center;justify-content:center;text-align:center;'
      + 'font-size:1.9rem;font-weight:600;border:1px solid var(--line-strong);border-radius:14px;padding:18px;"></div>';
    var box = text.firstChild, at = 0;
    rdMsg(k, 'Watch the box: the passage is shown ' + (st.display === 'phrases' ? 'a phrase' : (S.chunk > 1 ? S.chunk + ' words' : 'one word')) + ' at a time and ends by itself.');
    function show(n) {
      if (st.phase !== 'reading') return;
      if (n >= items.length) { rdFinish(k); return; }
      box.textContent = items[n].t;
      at += items[n].w * 60000 / st.target;
      rdLater(st, function () { show(n + 1); }, st.t0 + at - performance.now());
    }
    show(0);
  }
"""

# The aloud fallback: shipped only where a slot reads aloud.
RD_ALOUD_JS = r"""
  /* Cannot read aloud here: the side takes the published figure instead of a
     reading (words = the figure, seconds = 60), labelled, not logged. */
  function rdAloudInit(k) {
    var S = SLOTS[k], alt = rdE('rdAlt', k);
    alt.addEventListener('click', function () {
      var vals = {}, W = S.write || {};
      rdResetSlot(k, false);
      if (W.words) vals[W.words] = S.published;
      if (W.seconds) vals[W.seconds] = 60;
      if (W.correct) vals[W.correct] = 0;
      if (W.total) vals[W.total] = 0;
      rdWrite(vals);
      rdShow(alt, false); rdShow(rdE('rdStart', k), false);
      rdE('rdOut', k).textContent = 'This side now holds the published figure for reading aloud, ' + S.published
        + ' wpm (Brysbaert 2019), as ' + S.published + ' words in 60 s. It is not your reading, and nothing was logged.';
      rdMsg(k, 'Using the published figure. Reset brings the drill back.');
    });
    rdE('rdReset', k).addEventListener('click', function () { rdShow(alt, true); });
  }
"""

# Reread and free recall (the recall mode): shipped only where a slot uses them.
RD_RECALL_JS = r"""
  /* ---- reread (delayed recall, side A): two readings, no questions ---- */
  function rdLogReread(k) {
    var S = SLOTS[k], st = RD_ST[k], P = rdPassageOf(k);
    var due = new Date(Date.now() + S.days * 86400000).toISOString();
    rdLogAppend({ mode: S.mode, view: S.view, side: k, passage: P.id, display: 'normal', words: rdPassageWords(P) * 2,
                  ms: st.ms, correct: 0, total: 0, kind: st.kind, due: due, title: P.title,
                  url: String((window.location && window.location.pathname) || '') }, rdE('rdMsg', k));
    rdE('rdOut', k).textContent = 'Read twice in ' + rdUnit(Rparse(rdMsText(st.ms)), 's') + '. The test on this passage is due on '
      + due.slice(0, 10) + '; this page will offer it then.';
    rdMsg(k, 'Logged. There is no test now: that is the point of this condition.');
    var s = rdE('rdStart', k); s.textContent = 'Start again'; rdShow(s, true);
  }
  /* ---- free recall: write, then tick the idea units (the reader scores it) ---- */
  function rdRecallWrite(k) {
    var S = SLOTS[k], w = rdE('rdWork', k);
    rdShow(w, true);
    rdMsg(k, S.summary ? 'The passage is hidden. Write a summary of three sentences in your own words.'
                       : 'The passage is hidden. Write down everything you remember, in any order.');
    w.innerHTML = '<textarea rows="8" style="width:100%;box-sizing:border-box;" aria-label="Your recall"></textarea>'
      + '<div style="margin-top:8px;"><button class="btn small primary" type="button">Finished writing</button></div>';
    w.getElementsByTagName('button')[0].addEventListener('click', function () {
      RD_ST[k].written = w.getElementsByTagName('textarea')[0].value;
      rdRecallTick(k);
    });
  }
  function rdRecallTick(k) {
    var S = SLOTS[k], st = RD_ST[k], P = rdPassageOf(k), w = rdE('rdWork', k);
    rdMsg(k, 'These are the passage\'s idea units. Tick each one your writing contains, in substance; you are the judge.');
    w.innerHTML = '<p class="small-copy" style="white-space:pre-wrap;border-left:3px solid var(--line-strong);padding-left:8px;">'
      + rdEsc(st.written || '(nothing written)') + '</p><ul style="list-style:none;padding:0;">' + P.ideas.map(function (u, i) {
        return '<li><label><input type="checkbox" data-u="' + i + '"> ' + rdEsc(u) + '</label></li>';
      }).join('') + '</ul><button class="btn small primary" type="button">Score</button>';
    w.getElementsByTagName('button')[0].addEventListener('click', function () {
      var boxes = w.getElementsByTagName('input'), n = 0;
      for (var i = 0; i < boxes.length; i++) if (boxes[i].checked) n += 1;
      /* With questions on, the passage's questions follow the ticks. */
      if (S.questions && P.questions && P.questions.length) {
        rdMsg(k, 'Now the passage\'s questions, one at a time; there is no going back.');
        rdAsk(w, P.questions, function (answers) { rdRecallScore(k, n, rdTally(P.questions, answers), rdReview(P.questions, answers)); });
        return;
      }
      rdRecallScore(k, n, null, '');
    });
  }
  function rdRecallScore(k, n, q, review) {
    var S = SLOTS[k], st = RD_ST[k], P = rdPassageOf(k), w = rdE('rdWork', k);
    var words = rdPassageWords(P), sec = rdMsText(st.ms), sw = rdWordCount(st.written || ''), vals = {};
    var got = { units: P.ideas.length, recalled: n, words: words, seconds: sec, summaryWords: sw,
                correct: q ? q.correct : 0, total: q ? q.total : 0 };
    Object.keys(S.write || {}).forEach(function (g) { if (got[g] !== undefined) vals[S.write[g]] = got[g]; });
    rdWrite(vals);
    rdLogAppend({ mode: S.mode, view: S.view, side: k, passage: P.id, display: 'normal', words: words, ms: st.ms,
                  correct: got.correct, total: got.total, kind: st.kind,
                  extra: { units: P.ideas.length, recalled: n, summaryWords: sw, summary: S.summary },
                  due: S.days ? new Date(Date.now() + S.days * 86400000).toISOString() : undefined, title: S.days ? P.title : undefined,
                  url: String((window.location && window.location.pathname) || '') }, rdE('rdMsg', k));
    rdE('rdOut', k).innerHTML = rdEsc(n + ' of ' + P.ideas.length + ' idea units ticked; ' + sw + ' words written'
      + (q ? '; ' + q.correct + ' of ' + q.total + ' questions right.' : '.')
      + (S.days ? ' The test on this passage is due in ' + S.days + ' days; this page will offer it then.' : '')) + review;
    w.innerHTML = ''; rdShow(w, false);
    st.phase = 'idle';
    var s = rdE('rdStart', k); s.textContent = 'Start again'; rdShow(s, true);
    rdMsg(k, 'Scored and logged.');
  }
"""

# Find and coverage (click the words): shipped only where a slot uses them.
RD_FIND_JS = r"""
  /* Click and key handlers on the passage's words (find and coverage). */
  function rdFindInit(k) {
    var text = rdE('rdText', k);
    text.addEventListener('click', function (e) {
      var t = e.target;
      if (t && t.classList && t.classList.contains('rdw')) rdTokenHit(k, t);
    });
    text.addEventListener('keydown', function (e) {
      var t = e.target;
      if (!t || !t.classList || !t.classList.contains('rdw')) return;
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); rdTokenHit(k, t); return; }
      if (e.key === 'ArrowRight' || e.key === 'ArrowLeft' || e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        var all = text.querySelectorAll('.rdw[tabindex]'), i = Array.prototype.indexOf.call(all, t);
        var j = i + (e.key === 'ArrowRight' || e.key === 'ArrowDown' ? 1 : -1);
        if (j >= 0 && j < all.length) { e.preventDefault(); all[j].focus(); }
      }
    });
  }
  /* A slot's targets: one list, or one list per passage of its pool. */
  function rdTargetsOf(k) { var T = SLOTS[k].targets; return Array.isArray(T) ? T : T[rdPassageOf(k).id]; }
  /* ---- find: click the word that answers each prompt ---- */
  function rdFindBegin(k) {
    var S = SLOTS[k], st = RD_ST[k], P = rdPassageOf(k);
    st.phase = 'find'; st.ti = 0; st.found = 0; st.wrong = 0;
    rdE('rdText', k).innerHTML = rdTokHtml(P.paragraphs, true);
    var n = rdE('rdNext', k); n.textContent = 'Skip this one';
    rdShow(rdE('rdDone', k), false);
    st.t0 = performance.now();
    if (S.limit) rdLater(st, function () { rdFindEnd(k); }, S.limit * 1000);
    rdFindPrompt(k);
  }
  function rdFindPrompt(k) {
    var S = SLOTS[k], st = RD_ST[k];
    var T = rdTargetsOf(k);
    rdMsg(k, 'Target ' + (st.ti + 1) + ' of ' + T.length + ': ' + T[st.ti].q + ' Click the word that answers it.');
  }
  function rdFindStep(k, hit) {
    var S = SLOTS[k], st = RD_ST[k];
    if (st.phase !== 'find') return;
    if (hit) st.found += 1;
    st.ti += 1;
    if (st.ti >= rdTargetsOf(k).length) { rdFindEnd(k); return; }
    rdFindPrompt(k);
  }
  function rdFindEnd(k) {
    var S = SLOTS[k], st = RD_ST[k], P = rdPassageOf(k);
    if (st.phase !== 'find') return;
    rdClearTimers(st);
    st.ms = Math.max(1, Math.round(performance.now() - st.t0));
    st.phase = 'idle';
    rdHideText(k); rdButtons(k, true, false, false);
    var words = rdPassageWords(P), n = rdTargetsOf(k).length, vals = {}, got = { found: st.found, wrong: st.wrong, seconds: rdMsText(st.ms), words: words,
      targets: n };
    Object.keys(S.write || {}).forEach(function (g) { if (got[g] !== undefined) vals[S.write[g]] = got[g]; });
    rdWrite(vals);
    rdLogAppend({ mode: S.mode, view: S.view, side: k, passage: P.id, display: 'normal', words: words, ms: st.ms,
                  correct: st.found, total: n, kind: st.kind, extra: { wrong: st.wrong } }, rdE('rdMsg', k));
    rdE('rdOut', k).textContent = st.found + ' of ' + n + ' found, ' + st.wrong + ' wrong clicks, in '
      + rdUnit(Rparse(rdMsText(st.ms)), 's') + '.';
    rdE('rdStart', k).textContent = 'Start again';
    rdMsg(k, 'Logged.');
  }
  function rdTokenHit(k, span) {
    var S = SLOTS[k], st = RD_ST[k], i = +span.getAttribute('data-i');
    if (st.phase === 'find') {
      var at = rdTargetsOf(k)[st.ti].at;
      if (i >= at[0] && i <= at[1]) { span.style.outline = '2px solid var(--green, green)'; rdFindStep(k, true); }
      else { st.wrong += 1; span.style.outline = '2px dashed var(--red, #b00)'; }
    } else if (st.phase === 'mark' && span.getAttribute('data-w')) {
      var on = span.getAttribute('data-u') !== '1';
      span.setAttribute('data-u', on ? '1' : '0');
      span.style.background = on ? 'var(--line-strong)' : '';
      span.style.textDecoration = on ? 'underline wavy' : '';
      span.setAttribute('aria-pressed', on ? 'true' : 'false');
    }
  }
  function rdCoverageScore(k) {
    var S = SLOTS[k], st = RD_ST[k], P = rdPassageOf(k), spans = rdE('rdText', k).getElementsByClassName('rdw'), n = 0;
    for (var i = 0; i < spans.length; i++) if (spans[i].getAttribute('data-u') === '1') n += 1;
    st.ms = Math.max(1, Math.round(performance.now() - st.t0));
    st.phase = 'idle';
    rdHideText(k); rdButtons(k, false, false, false);
    /* With questions on, the passage's questions follow, the passage hidden. */
    if (S.questions && P.questions && P.questions.length) {
      rdMsg(k, 'The passage is hidden. Answer each question; there is no going back.');
      rdAsk(rdE('rdWork', k), P.questions, function (a) { rdCoverageEnd(k, n, rdTally(P.questions, a), rdReview(P.questions, a)); });
      return;
    }
    rdCoverageEnd(k, n, null, '');
  }
  function rdCoverageEnd(k, n, q, review) {
    var S = SLOTS[k], st = RD_ST[k], P = rdPassageOf(k), vals = {}, sec = rdMsText(st.ms);
    var got = { tokens: rdPassageWords(P), unknown: n, seconds: sec, correct: q ? q.correct : 0, total: q ? q.total : 0 };
    Object.keys(S.write || {}).forEach(function (g) { if (got[g] !== undefined) vals[S.write[g]] = got[g]; });
    rdWrite(vals);
    rdLogAppend({ mode: S.mode, view: S.view, side: k, passage: P.id, display: 'normal', words: got.tokens, ms: S.timed ? st.ms : 0,
                  correct: got.correct, total: got.total, kind: st.kind, extra: { unknown: n } }, rdE('rdMsg', k));
    var w = rdE('rdWork', k); w.innerHTML = ''; rdShow(w, false);
    rdButtons(k, true, false, false);
    rdE('rdOut', k).innerHTML = rdEsc(n + ' unknown words marked out of ' + got.tokens + (S.timed ? ', in ' + rdUnit(Rparse(sec), 's') : '')
      + (q ? '; ' + q.correct + ' of ' + q.total + ' questions right.' : '.')) + review;
    rdMsg(k, 'Counted and logged.');
  }
"""

__all__ = ["RD_DRILL_JS", "RD_TIMED_JS", "RD_RECALL_JS", "RD_FIND_JS", "RD_ALOUD_JS"]
