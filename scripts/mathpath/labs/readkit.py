"""readkit -- the Reading Faster kit: drill, eye, flash and scan, and the entry point.

Specified in docs/reading/PLAN.md section D (D.0 conventions, D.1 modes),
with the review corrections recorded in docs/reading/kit-report.md. Eight
modes; this file builds four and readkit_b.py the other four (triage, text,
recall, log), imported only when one of them is asked for.

  drill   single, compare, ladder, repeat, sections, practice: timed readings
          with questions; displays normal pacer mask rsvp phrases gist preview aloud
  eye     budget, required, lines: the eye-movement model's arithmetic
  flash   span (letters identified by position in a brief flash), schulte
  scan    find (click the answer to each prompt), inspect (a timed look, then questions)

Every mode is a table of fields (text inputs, id <prefix>In<Key>), a list of
tiles, and one pure JS function <xx>Compute(view, inst, opts) that
scripts/mathcheck.js calls ("readkit" block). Passages arrive inside the cfg
as dicts (cfg["passage"] or cfg["passages"], PLAN section P plus "id"); the
kit never imports content/, validates every passage at build time and ships
only the passages it is given and only the active mode's JavaScript.

IDS. Tiles and inputs use the prefixes dr ey fl sc tr tx re lg; drill
elements use rd<Name><slot>. Grepped against scripts/mathpath/labs/*.py on
2026-10-24: no module-level JS function name collides (one page carries one
lab, so element ids shared with other kits' pages never meet).
"""

from . import readkit_core as rc

KIT = "readkit"
DISPLAYS = ("normal", "pacer", "mask", "rsvp", "phrases", "gist", "preview", "aloud")
TIMED = ("pacer", "mask", "rsvp", "phrases")

# ---------------------------------------------------------------------------
# drill
# ---------------------------------------------------------------------------

DRILL_JS = r"""
  /* drill: rate = words x 60 / seconds; comprehension = correct / total;
     effective rate = rate x comprehension (Jackson and McClelland 1979). */
  function drSide(inst, s, kinds) {
    var o = { s: s, words: inst['words' + s], seconds: inst['seconds' + s] };
    o.wpm = rdRate(o.words, o.seconds);
    if (kinds) {
      o.correct = Radd(inst['gist' + s], inst['detail' + s]); o.total = Radd(inst['gistTotal' + s], inst['detailTotal' + s]);
      if (Rcmp(inst['gist' + s], inst['gistTotal' + s]) > 0 || Rcmp(inst['detail' + s], inst['detailTotal' + s]) > 0) {
        return { refuse: 'Reading ' + s + ' has more questions right than asked' };
      }
    } else { o.correct = inst['correct' + s]; o.total = inst['total' + s]; }
    if (Rcmp(o.correct, o.total) > 0) {
      return { refuse: 'Reading ' + (s || '') + ' has more questions right (' + rdFig(o.correct) + ') than asked (' + rdFig(o.total) + ')' };
    }
    o.comp = Rzero(o.total) ? null : Rdiv(o.correct, o.total);
    o.err = o.comp ? Rmul(o.wpm, o.comp) : null;
    return o;
  }
  function drCompText(o) { return o.comp ? rdShare(o.comp) : 'no questions'; }
  function drErrText(o) { return o.err ? rdUnit(o.err, 'wpm') : 'no questions'; }
  function drMs(x) { return rdUnit(x, 'ms'); }
  /* The baseline range verdict, on a single reading's rate. */
  function drVerdict(wpm, lo, hi) {
    if (lo === null && hi === null) return 'no baseline readings yet';
    if (Rcmp(wpm, hi) > 0) return 'above the baseline range once — a fourth reading does this about one time in four';
    if (Rcmp(wpm, lo) < 0) return 'below the baseline range';
    return 'inside the baseline range';
  }
  function drBase(inst) {
    var lo = inst.baseLo === undefined ? null : inst.baseLo, hi = inst.baseHi === undefined ? null : inst.baseHi;
    if ((lo === null) !== (hi === null)) return { refuse: 'Give both ends of the baseline range, or neither' };
    if (lo !== null && Rcmp(lo, hi) > 0) return { refuse: 'The baseline range runs from the lower rate to the higher one' };
    return { lo: lo, hi: hi };
  }
  /* The hold target: the fastest pacer target whose last three readings all
     scored at least the hold share. entries: [{wpm (the target), correct, total}] in log order. */
  function drHoldOf(entries, hold) {
    var by = {}, keys = [], best = null;
    entries.forEach(function (e) { var k = Rtext(e.wpm); if (!by[k]) { by[k] = []; keys.push(k); } by[k].push(e); });
    keys.forEach(function (k) {
      var last = by[k].slice(-3);
      if (last.length < 3) return;
      if (last.every(function (e) { return Rcmp(Rdiv(e.correct, e.total), hold) >= 0; })) {
        if (best === null || Rcmp(last[0].wpm, best) > 0) best = last[0].wpm;
      }
    });
    return best;
  }
  /* The next pacer target: the last target T, times 21/20 after three holds
     in a row at T, times 19/20 after two misses in a row at T, else T. */
  function drNextOf(entries, hold) {
    if (!entries.length) return null;
    var T = entries[entries.length - 1].wpm, run = [];
    for (var i = entries.length - 1; i >= 0 && Rcmp(entries[i].wpm, T) === 0; i--) run.unshift(entries[i]);
    function held(e) { return Rcmp(Rdiv(e.correct, e.total), hold) >= 0; }
    if (run.length >= 3 && run.slice(-3).every(held)) return { wpm: Rmul(T, R(21n, 20n)), why: 'three holds in a row at ' + rdUnit(T, 'wpm') + ': up by 1/20' };
    if (run.length >= 2 && run.slice(-2).every(function (e) { return !held(e); })) return { wpm: Rmul(T, R(19n, 20n)), why: 'two misses in a row at ' + rdUnit(T, 'wpm') + ': down by 1/20' };
    return { wpm: T, why: 'stay at ' + rdUnit(T, 'wpm') };
  }
  /* A test reading is due when this many practice sessions have passed since the last test. */
  var DR_TEST_EVERY = 4;
  function drTestDueOf(since) {
    var n = Number(since.n), left = DR_TEST_EVERY - n;
    return left <= 0 ? 'due now: make the next reading a test' : 'after ' + left + ' more practice session' + (left === 1 ? '' : 's');
  }
  function drCompute(view, inst, opts) {
    var t = {}, said, rows = [], sides = opts.sides, o, k;
    if (view === 'single' || view === 'practice') {
      var d = sides[''].display;
      o = drSide(inst, '', false);
      if (o.refuse) return o;
      t.drWords = rdFig(o.words) + ' words';
      t.drTime = rdUnit(o.seconds, 's');
      t.drWpm = rdUnit(o.wpm, 'wpm');
      t.drComp = drCompText(o);
      if (d === 'gist') {
        if (Rcmp(inst.shown, o.words) > 0) return { refuse: 'The words shown cannot be more than the words in the passage' };
        t.drShown = rdShare(Rdiv(inst.shown, o.words));
        t.drGistPerMin = Rzero(o.total) ? 'no questions' : rdUnit(Rdiv(Rmul(o.correct, R(60n)), o.seconds), 'gist answers a minute');
        said = 'The skim showed ' + rdFig(inst.shown) + ' of ' + rdFig(o.words) + ' words for ' + rdUnit(o.seconds, 's')
          + (Rzero(o.total) ? '.' : ', and ' + rdFig(o.correct) + ' of ' + rdFig(o.total) + ' gist questions were right: '
          + rdFig(o.correct) + ' × 60 / ' + rdFig(o.seconds) + ' = ' + t.drGistPerMin + '. A skim is scored on gist, not as an effective reading rate.');
        return { tiles: t, status: said };
      }
      t.drErr = drErrText(o);
      if (view === 'single') t.drStdWpm = rdUnit(rdRate(Rdiv(inst.chars, R(6n)), o.seconds), 'standard wpm');
      if (d === 'rsvp') {
        t.drWordMs = drMs(Rdiv(Rmul(R(60000n), inst.chunk), inst.target));
        t.drWordMsSeen = drMs(Rdiv(Rmul(Rmul(o.seconds, R(1000n)), inst.chunk), o.words));
      }
      if (d === 'pacer' || d === 'mask') t.drPacerLineMs = drMs(Rdiv(Rmul(R(60000n), Rparse(opts.lineWords)), inst.target));
      if (d === 'phrases') t.drPhraseMs = drMs(Rdiv(Rmul(o.words, R(60000n)), Rmul(inst.target, inst.phrases)));
      if (view === 'practice') {
        var h = drHoldOf(inst.pacerLog, Rparse(opts.hold)), nx = drNextOf(inst.pacerLog, Rparse(opts.hold));
        t.drHold = h === null ? 'not yet' : rdUnit(h, 'wpm');
        t.drNextTarget = nx === null ? 'no pacer readings yet' : rdUnit(nx.wpm, 'wpm');
        t.drTestDue = drTestDueOf(inst.sinceTest);
      }
      said = rdFig(o.words) + ' words in ' + rdUnit(o.seconds, 's') + ' is ' + rdFig(o.words) + ' × 60 / ' + rdFig(o.seconds)
        + ' = ' + t.drWpm + (o.comp ? '; with ' + rdFig(o.correct) + ' of ' + rdFig(o.total) + ' right the effective rate is '
        + t.drErr : '; no questions were asked, so comprehension is not scored') + '. One reading is one measurement.'
        + (t.drWordMsSeen ? ' Each flash was requested for ' + t.drWordMs + '; the reading took ' + t.drWordMsSeen + ' a flash.' : '')
        + (view === 'practice' ? ' Next pacer target: ' + t.drNextTarget + (nx ? ' (' + nx.why + ')' : '') + '. A test reading: ' + t.drTestDue + '.' : '');
      return { tiles: t, status: said };
    }
    if (view === 'compare') {
      var A = drSide(inst, 'A', opts.kinds), B = drSide(inst, 'B', opts.kinds), base = drBase(inst);
      if (A.refuse) return A; if (B.refuse) return B; if (base.refuse) return base;
      [A, B].forEach(function (x) {
        t['drWpm' + x.s] = rdUnit(x.wpm, 'wpm'); t['drComp' + x.s] = drCompText(x); t['drErr' + x.s] = drErrText(x);
        if (opts.kinds) {
          t['drGist' + x.s] = Rzero(inst['gistTotal' + x.s]) ? 'no gist questions' : rdShare(Rdiv(inst['gist' + x.s], inst['gistTotal' + x.s]));
          t['drDetail' + x.s] = Rzero(inst['detailTotal' + x.s]) ? 'no detail questions' : rdShare(Rdiv(inst['detail' + x.s], inst['detailTotal' + x.s]));
        }
        rows.push([sides[x.s].label, rdFig(x.words), rdUnit(x.seconds, 's'), t['drWpm' + x.s], t['drComp' + x.s], t['drErr' + x.s]]);
      });
      var useErr = opts.ratioOf === 'err' && A.err && B.err && !Rzero(A.err);
      t.drErrDiff = (A.err && B.err) ? rdSigned(Rsub(B.err, A.err), 'wpm') : 'needs questions on both';
      t.drRatio = (opts.ratioOf === 'err' && A.err && B.err && Rzero(A.err)) ? 'A\'s effective rate is 0' : rdShare(useErr ? Rdiv(B.err, A.err) : Rdiv(B.wpm, A.wpm));
      t.drVerdictB = drVerdict(B.wpm, base.lo, base.hi);
      ['B', 'A'].forEach(function (s) {
        var d = sides[s].display;
        if ((d === 'pacer' || d === 'mask') && !t.drPacerLineMs) t.drPacerLineMs = drMs(Rdiv(Rmul(R(60000n), Rparse(opts.lineWords)), inst['target' + s]));
        if (d === 'rsvp' && !t.drWordMs) {
          t.drWordMs = drMs(Rdiv(Rmul(R(60000n), inst['chunk' + s]), inst['target' + s]));
          t.drWordMsSeen = drMs(Rdiv(Rmul(Rmul(inst['seconds' + s], R(1000n)), inst['chunk' + s]), inst['words' + s]));
        }
        if (d === 'phrases' && !t.drPhraseMs) t.drPhraseMs = drMs(Rdiv(Rmul(inst['words' + s], R(60000n)), Rmul(inst['target' + s], inst['phrases' + s])));
      });
      said = 'Reading A: ' + t.drWpmA + ', effective ' + t.drErrA + '. Reading B: ' + t.drWpmB + ', effective ' + t.drErrB
        + '. B against A: ' + t.drRatio + (useErr ? ' of the effective rate.' : ' of the rate.')
        + ' Two readings of two passages differ for reasons other than the condition; your baseline range says by how much.';
      return { tiles: t, status: said, table: { caption: 'The two readings', head: ['reading', 'words', 'time', 'rate', 'comprehension', 'effective rate'], rows: rows } };
    }
    if (view === 'ladder') {
      var runs = [];
      for (k = 1; k <= 3; k++) {
        o = drSide(inst, String(k), false);
        if (o.refuse) return o;
        o.target = inst['t' + k];
        runs.push(o);
        t['drWpm' + k] = rdUnit(o.wpm, 'wpm'); t['drErr' + k] = drErrText(o);
        rows.push(['run ' + k, rdUnit(o.target, 'wpm'), t['drWpm' + k], drCompText(o), t['drErr' + k]]);
      }
      var best = null, top = null;
      runs.forEach(function (r) {
        if (r.comp && Rcmp(r.comp, Rparse(opts.hold)) >= 0 && (best === null || Rcmp(r.target, best.target) > 0)) best = r;
        if (r.err && (top === null || Rcmp(r.err, top.err) > 0 || (Rcmp(r.err, top.err) === 0 && Rcmp(r.target, top.target) < 0))) top = r;
      });
      t.drBestTarget = best ? rdUnit(best.target, 'wpm') : 'none at ' + opts.hold + ' or better';
      t.drBestErr = best ? rdUnit(best.err, 'wpm') : RD_DASH;
      t.drTopErr = top ? rdUnit(top.err, 'wpm') + ' (target ' + rdUnit(top.target, 'wpm') + ')' : 'no questions';
      said = 'The fastest target at which comprehension held at ' + opts.hold + ' or better: ' + t.drBestTarget
        + '. The highest effective rate of the three runs: ' + t.drTopErr + '.';
      return { tiles: t, status: said, table: { caption: 'Three pacer runs', head: ['run', 'target', 'rate', 'comprehension', 'effective rate'], rows: rows } };
    }
    if (view === 'repeat') {
      var w = [];
      for (k = 1; k <= 4; k++) {
        o = drSide(inst, String(k), false);
        if (o.refuse) return o;
        w.push(o.wpm);
        t['drWpm' + k] = rdUnit(o.wpm, 'wpm');
        rows.push([k < 4 ? 'repeated passage, reading ' + k : 'new passage', t['drWpm' + k], drCompText(o)]);
      }
      t.drRepeatGain = rdSigned(Rsub(w[2], w[0]), 'wpm');
      t.drTransferGain = rdSigned(Rsub(w[3], w[0]), 'wpm');
      said = 'On the repeated passage the rate moved ' + t.drRepeatGain + ' from the first reading to the third; on the new passage, '
        + t.drTransferGain + ' against the first. Only the second is a change in the reader.';
      return { tiles: t, status: said, table: { caption: 'Four readings', head: ['reading', 'rate', 'comprehension'], rows: rows } };
    }
    /* sections */
    var r1 = rdRate(inst.words1, inst.seconds1), r2 = rdRate(inst.words2, inst.seconds2);
    var whole = { words: Radd(inst.words1, inst.words2), seconds: Radd(inst.seconds1, inst.seconds2), correct: inst.correct, total: inst.total };
    if (Rcmp(inst.correct, inst.total) > 0) return { refuse: 'More questions right than asked' };
    whole.wpm = rdRate(whole.words, whole.seconds);
    whole.comp = Rzero(inst.total) ? null : Rdiv(inst.correct, inst.total);
    whole.err = whole.comp ? Rmul(whole.wpm, whole.comp) : null;
    t.drRateS1 = rdUnit(r1, 'wpm'); t.drRateS2 = rdUnit(r2, 'wpm'); t.drWpm = rdUnit(whole.wpm, 'wpm');
    t.drComp = drCompText(whole); t.drErr = drErrText(whole);
    said = 'Section 1: ' + t.drRateS1 + '; section 2: ' + t.drRateS2 + '. The whole passage: ' + t.drWpm + ', effective ' + t.drErr + '.';
    return { tiles: t, status: said };
  }
"""

PRACTICE_JS = r"""
  /* drill/practice: the pool passage not yet in the log, a pacer or not, a
     test tick, or pasted text; the pacer log for the hold tile. All of this
     runs on a click, except filling the pacer log from storage at load. */
  function rdPacerLogText() {
    return rdLogRead().filter(function (e) {
      return e.mode === 'drill' && e.view === 'practice' && e.display === 'pacer' && e.total > 0 && e.extra && e.extra.target;
    }).map(function (e) { return Math.round(e.extra.target) + '/' + e.correct + '/' + e.total; }).join(', ');
  }
  function rdPoolNext() { return rdFirstUnlogged(RD_POOL); }
  /* Practice sessions logged since the last test reading (any lesson). */
  function rdSinceTest() {
    var n = 0;
    rdLogRead().forEach(function (e) { if (e.kind === 'test') n = 0; else if (e.kind === 'practice' && e.mode === 'drill') n += 1; });
    return n;
  }
  function rdPracticeSetup(k) {
    var st = RD_ST[k], test = document.getElementById('rdTest').checked, pace = document.getElementById('rdPacer').checked;
    var pasted = rdClean(document.getElementById('rdPaste').value);
    st.kind = test ? 'test' : 'practice';
    st.display = (pace && !test) ? 'pacer' : 'normal';
    if (pasted !== '') {
      st.passage = { id: 'pasted', title: 'Your text', paragraphs: pasted.split(/\n\s*\n/).filter(function (p) { return p.trim(); }), questions: [] };
      st.kind = 'practice';
      return true;
    }
    var id = rdPoolNext();
    if (!id) { rdMsg(k, 'You have read every passage in this pool. Paste a text of your own to keep practising.'); return false; }
    st.passage = PASSAGES[id];
    rdMsg(k, 'Next unread passage: ' + st.passage.title + '.');
    return true;
  }
  function rdPracticeAfter() { var v = { sinceTest: rdSinceTest() }, t = rdPacerLogText(); if (t !== '') v.pacerLog = t; rdWrite(v); }
"""

PRACTICE_INIT_JS = r"""
  (function () {
    var t = rdPacerLogText(), v = {};
    if (t !== '') v.pacerLog = t;
    if (rdLogRead().length) v.sinceTest = rdSinceTest();
    if (t !== '' || v.sinceTest !== undefined) rdWrite(v);
    var id = rdPoolNext(), m = document.getElementById('rdPool');
    if (m) m.textContent = id ? 'Next unread passage: ' + PASSAGES[id].title + '.' : 'Every passage in the pool is in your log.';
  })();
"""

BASELINE_UI_JS = r"""
  /* The baseline range from the log: the first three readings logged as
     "baseline" (rate = words x 60,000 / ms, exact). Filled at load only when
     the shipped preset leaves the range empty; the button fills it on request. */
  function rdBaselineRange() {
    var rates = rdLogRead().filter(function (e) { return e.kind === 'baseline' && e.words > 0 && e.ms > 0; }).slice(0, 3)
      .map(function (e) { return R(BigInt(Math.round(e.words)) * 60000n, BigInt(Math.round(e.ms))); });
    if (!rates.length) return null;
    var s = rates.slice().sort(Rcmp);
    return { baseLo: Rtext(s[0]), baseHi: Rtext(s[s.length - 1]), n: rates.length };
  }
  (function () {
    var btnEl = document.getElementById('rdUseBase'), note = document.getElementById('rdBaseNote');
    function fill() {
      var r = rdBaselineRange();
      if (!r) { if (note) note.textContent = 'Your log has no readings marked as baselines yet.'; return false; }
      rdWrite({ baseLo: r.baseLo, baseHi: r.baseHi });
      if (note) note.textContent = 'Baseline range from your first ' + r.n + ' baseline reading' + (r.n === 1 ? '' : 's') + '.';
      return true;
    }
    if (btnEl) btnEl.addEventListener('click', fill);
    if (field('drInBaseLo') && field('drInBaseLo').value === '' && rdBaselineRange()) fill();
  })();
"""

ORDER_UI_JS = r"""
  /* The order of a compare: cfg AB, BA, or alternate by the parity of the
     log's length (read at load; nothing starts). B first moves its box up. */
  (function () {
    var o = DR_ORDER === 'alternate' ? (rdLogRead().length % 2 ? 'BA' : 'AB') : DR_ORDER;
    SLOTS.A.order = SLOTS.B.order = o;
    var a = document.getElementById('rdBoxA'), b = document.getElementById('rdBoxB'), note = document.getElementById('rdOrder');
    if (o === 'BA' && a && b && a.parentNode && a.parentNode === b.parentNode && a.parentNode.insertBefore) a.parentNode.insertBefore(b, a);
    if (note) note.textContent = (o === 'AB' ? 'Read A first, then B.' : 'Read B first, then A.')
      + (DR_ORDER === 'alternate' ? ' The order alternates from one comparison to the next, so neither condition always comes second.' : '');
  })();
"""


def F(key, label, kind, default=None):
    return (key, label, kind, default)


ATTENTION = {"label": "My attention left the text at some point", "key": "lapse"}


def one_question_note(n):
    """D.3.1: what one question is worth, for a passage of n questions."""
    pts = rc.Fraction(100, n)
    t = (str(pts.numerator) if pts.denominator == 1 else "%.1f" % float(pts) if (pts * 10).denominator == 1
         else "≈ %.1f" % float(pts))
    return "One question is %s points; a one-question difference is not a result." % t


def _kinds_ok(kit, side, p, qkinds):
    if not p.get("questions"):
        raise ValueError("%s: %s: passage %s has no questions; set questions off or use a passage that has them"
                         % (kit, side, p["id"]))
    if qkinds == "gist" and not any(q["kind"] == "gist" for q in p["questions"]):
        raise ValueError("%s: %s: the gist display asks gist questions and passage %s has none" % (kit, side, p["id"]))


def _side_cfg(kit, name, sc, passage, default_kind):
    """A drill side's settings, checked: display, questions, target, chunk, limit, kind."""
    if not isinstance(sc, dict):
        raise ValueError("%s: cfg[%r] must be a dict of that reading's settings" % (kit, name))
    allowed = {"display", "questions", "target", "chunk", "limit", "kind", "label", "suppress", "published"}
    extra = sorted(set(sc) - allowed)
    if extra:
        raise ValueError("%s: cfg[%r] has %s; a reading's settings are %s" % (kit, name, ", ".join(extra), ", ".join(sorted(allowed))))
    d = sc.get("display", "normal")
    if d not in DISPLAYS:
        raise ValueError("%s: %s display %r is not one of %s" % (kit, name, d, ", ".join(DISPLAYS)))
    if d == "phrases" and not passage.get("phrases"):
        raise ValueError("%s: %s uses the phrases display and passage %s is not phrase-marked" % (kit, name, passage["id"]))
    q = sc.get("questions", True)
    if not isinstance(q, bool):
        raise ValueError("%s: %s questions is True or False" % (kit, name))
    qkinds = "gist" if d == "gist" else "all"
    if q:
        _kinds_ok(kit, name, passage, qkinds)
    out = {"display": d, "questions": q, "qkinds": qkinds, "label": sc.get("label", name),
           "kind": rc.log_kind(kit + " " + name, sc.get("kind"), default_kind), "suppress": bool(sc.get("suppress", False))}
    t = rc.num(kit, sc, "target", None, lo=1, hi=100000)
    if d in TIMED and t is None:
        raise ValueError("%s: %s uses the %s display and needs a target (wpm), the starting value of its target box"
                         % (kit, name, d))
    out["target"] = t
    out["chunk"] = rc.num(kit, sc, "chunk", 1, lo=1, hi=5, whole=True)
    lim = rc.num(kit, sc, "limit", None, lo=5, hi=1800, whole=True)
    if d in ("gist", "preview") and lim is None:
        raise ValueError("%s: %s uses the %s display and needs a limit in seconds" % (kit, name, d))
    out["limit"] = None if lim is None else int(lim)
    pub = rc.num(kit, sc, "published", 183, lo=1, hi=1000, whole=True)
    out["published"] = int(pub)
    return out


def _side_fields(s, sc, passage, label, chars=False, kinds=False):
    """The text inputs one reading fills. s: the key suffix ('', 'A', '1'...)."""
    who = (" (%s)" % label) if label else ""
    f = [F("words" + s, "Words read" + who, "count", rc.word_count_passage(passage))]
    if chars:
        f.append(F("chars" + s, "Characters, spaces included" + who, "count", rc.passage_counts(passage)["chars"]))
    f.append(F("seconds" + s, "Seconds taken" + who, "pos"))
    if kinds:
        f += [F("gist" + s, "Gist questions right" + who, "nncount"), F("gistTotal" + s, "Gist questions asked" + who, "nncount"),
              F("detail" + s, "Detail questions right" + who, "nncount"),
              F("detailTotal" + s, "Detail questions asked" + who, "nncount")]
    else:
        nq = 0 if not sc["questions"] else None
        f += [F("correct" + s, "Questions right" + who, "nncount", nq), F("total" + s, "Questions asked" + who, "nncount", nq)]
    d = sc["display"]
    if d in TIMED:
        f.append(F("target" + s, "Target rate, wpm" + who, "pos", rc.ftext(sc["target"])))
    if d == "rsvp":
        f.append(F("chunk" + s, "Words per flash" + who, "count", rc.ftext(sc["chunk"])))
    if d == "phrases":
        f.append(F("phrases" + s, "Phrases in the passage" + who, "count", rc.phrase_count(passage)))
    if d == "gist":
        f.append(F("shown" + s, "Words the skim shows" + who, "nncount", rc.gist_words(passage)))
    return f


def _write_map(fields, s):
    """generic measurement name -> this view's input key, for every input the slot fills."""
    out = {}
    for key, *_ in fields:
        if s and key.endswith(s):
            base = key[: -len(s)]
        elif not s:
            base = key
        else:
            continue
        if base in ("words", "chars", "seconds", "correct", "total", "gist", "gistTotal", "detail", "detailTotal",
                    "shown", "phrases"):
            out[base] = key
    return out


def _slot_intro(sc, passage):
    d = sc["display"]
    base = {"normal": "Read at your usual pace.", "aloud": "Read this one aloud.",
            "pacer": "A highlight moves line by line at the target rate in the box below; read with it.",
            "mask": "A highlight moves line by line and the lines above it disappear.",
            "rsvp": "The passage is flashed a word at a time at the target rate.",
            "phrases": "The passage is shown a phrase at a time at the target rate.",
            "gist": "A skim: only headings and first sentences, for a fixed time.",
            "preview": "A preview of headings, the first and the last paragraph, then the whole passage."}[d]
    if d in ("rsvp", "phrases"):
        base += " " + rc.PHOTO_NOTE
    if sc["suppress"]:
        base += " While you read, repeat “one-two-three” under your breath, without stopping."
    q = (" Then %d questions, one at a time; the passage is hidden while you answer." % (
        len([x for x in passage.get("questions") or [] if sc["qkinds"] == "all" or x["kind"] == "gist"])) if sc["questions"] else
        " No questions follow.")
    return base + q + " Press Start when you are ready."


def _slot_markup(k, sc, passage, heading, flow="read"):
    extra = ""
    if flow == "sections":
        extra += rc.btn("rdNext" + k, "Next section", hidden=True)
    if sc["display"] == "aloud":
        extra += rc.btn("rdAlt" + k, "I can’t read aloud here")
    return rc.slot_html(k, heading, _slot_intro(sc, passage), extra)


def _drill(cfg, view, kit):
    lw = rc.num(kit, cfg, "lineWords", 12, lo=1, hi=40, whole=True)
    hold = rc.num(kit, cfg, "hold", "2/3", lo=0, hi=1)
    opts = {"lineWords": rc.ftext(lw), "_cfg_keys": ("passage", "passages", "lineWords")}
    fields, tiles, slots, main, js, extra_keys = [], [], {}, "", DRILL_JS, ()
    if view in ("single", "practice"):
        if view == "single":
            (p,) = rc.passages_of(cfg, kit, 1)
            pool = [p]
        elif "pool" not in cfg:
            pool = rc.passages_of(cfg, kit)
            if not pool:
                raise ValueError("%s: drill/practice needs cfg[\"pool\"], a list of passages" % kit)
            p = pool[0]
        sc_cfg = {k: cfg[k] for k in ("display", "questions", "target", "chunk", "limit", "kind", "suppress") if k in cfg}
        if view == "practice" and "pool" in cfg:
            if "passages" in cfg or "passage" in cfg:
                raise ValueError("%s: give the pool as cfg[\"pool\"] or cfg[\"passages\"], not both" % kit)
            pool = rc.passages_of({"passages": cfg["pool"]}, kit)
            p = pool[0]
        if view == "practice":
            sc_cfg.setdefault("target", 250)
            if sc_cfg.get("display", "normal") not in ("normal", "pacer"):
                raise ValueError("%s: drill/practice offers the normal and pacer displays only" % kit)
            sc_cfg["display"] = "pacer"   # the target box always shows; the reader turns the pacer on
        sc = _side_cfg(kit, "the reading", sc_cfg, p, "practice" if view == "practice" else "condition")
        if view == "practice":
            sc["display"] = "normal"
            for q in pool:
                _kinds_ok(kit, "pool", q, "all")
        opts["_cfg_keys"] += ("display", "questions", "target", "chunk", "limit", "kind", "suppress", "published")
        if view == "practice":
            opts["_cfg_keys"] += ("hold", "pool")
        fields = _side_fields("", dict(sc, display="pacer") if view == "practice" else sc, p, "", chars=(view == "single"))
        if view == "practice":
            for i, f in enumerate(fields):
                if f[0] in ("correct", "total"):
                    fields[i] = F(f[0], f[1], "nncount", 0)
            fields.append(F("pacerLog", "Your pacer practice: target/right/asked, oldest first", ("entries", 0, 200), []))
            fields.append(F("sinceTest", "Practice sessions since your last test reading", "nncount", 0))
        d = sc["display"]
        tiles = [("Words", "drWords"), ("Time", "drTime")]
        if d == "gist":
            tiles += [("Share of the words the skim shows", "drShown"), ("Gist questions right", "drComp"),
                      ("Gist answers a minute", "drGistPerMin")]
        else:
            tiles += [("Rate", "drWpm")] + ([("Rate in standard words (6 characters)", "drStdWpm")] if view == "single" else [])
            tiles += [("Comprehension", "drComp"), ("Effective rate", "drErr")]
            if d == "rsvp":
                tiles += [("Each flash is requested for", "drWordMs"), ("Each flash took, measured", "drWordMsSeen")]
            if d in ("pacer", "mask"):
                tiles.append(("Pacer time for a line of %s words" % rc.ftext(lw), "drPacerLineMs"))
            if d == "phrases":
                tiles.append(("Mean time per phrase", "drPhraseMs"))
        if view == "practice":
            tiles += [("Hold target: last three pacer runs at it all at %s or better" % rc.ftext(hold), "drHold"),
                      ("Next pacer target", "drNextTarget"), ("Next test reading", "drTestDue")]
            opts["hold"] = rc.ftext(hold)
        opts["sides"] = {"": {"display": d, "label": ""}}
        slots[""] = rc.slot("", None if view == "practice" else p, intro=_slot_intro(sc, p), kind=sc["kind"], mode="drill",
                            view=view, display=d, questions=sc["questions"], qkinds=sc["qkinds"], flow=view if view == "practice" else "read",
                            write=_write_map(fields, ""), target_key="target" if d in TIMED or view == "practice" else None,
                            chunk=int(sc["chunk"]), limit=sc["limit"], suppress=sc["suppress"], published=sc["published"],
                            tick=ATTENTION if view == "practice" else None)
        if view == "practice":
            main = ('      <div class="card card-pad" style="margin-top:12px;">\n'
                    '        <p class="small-copy" id="rdPool" style="margin:0 0 8px;"></p>\n'
                    '        <label class="small-copy"><input type="checkbox" id="rdPacer"> Read with the pacer at the target rate in the panel</label><br>\n'
                    '        <label class="small-copy"><input type="checkbox" id="rdTest"> This is a test reading (natural pace, no pacer)</label>\n'
                    '        <details style="margin-top:8px;"><summary class="small-copy">Or paste a text of your own</summary>\n'
                    '        <textarea id="rdPaste" rows="6" style="width:100%;box-sizing:border-box;" aria-label="Your own text"></textarea>\n'
                    '        <p class="small-copy">Paragraphs are separated by a blank line. Your own text has no questions, so its comprehension is not scored; it is logged as practice.</p></details>\n'
                    '      </div>\n')
            main += rc.slot_html("", "Practice reading", slots[""]["intro"])
            js += PRACTICE_JS
            opts["_pool"] = [q["id"] for q in pool]
        else:
            main = _slot_markup("", sc, p, "Timed reading: " + p["title"])
        passages = pool
    elif view == "compare":
        pa, pb = rc.passages_of(cfg, kit, 2)
        kinds = cfg.get("kinds", False)
        if not isinstance(kinds, bool):
            raise ValueError("%s: cfg[\"kinds\"] is True or False" % kit)
        ratio = cfg.get("ratioOf", "err")
        if ratio not in ("err", "wpm"):
            raise ValueError("%s: cfg[\"ratioOf\"] is \"err\" (effective rate) or \"wpm\" (rate)" % kit)
        sa = _side_cfg(kit, "a", cfg.get("a", {}), pa, "condition")
        sb = _side_cfg(kit, "b", cfg.get("b", {}), pb, "condition")
        sa["label"] = cfg.get("a", {}).get("label", "Reading A")
        sb["label"] = cfg.get("b", {}).get("label", "Reading B")
        fields = (_side_fields("A", sa, pa, "A", kinds=kinds) + _side_fields("B", sb, pb, "B", kinds=kinds)
                  + [F("baseLo", "Baseline range: lowest rate (empty if none)", "opt", ""),
                     F("baseHi", "Baseline range: highest rate (empty if none)", "opt", "")])
        tiles = [("Rate A", "drWpmA"), ("Rate B", "drWpmB"), ("Comprehension A", "drCompA"), ("Comprehension B", "drCompB")]
        if kinds:
            tiles += [("Gist A", "drGistA"), ("Detail A", "drDetailA"), ("Gist B", "drGistB"), ("Detail B", "drDetailB")]
        tiles += [("Effective rate A", "drErrA"), ("Effective rate B", "drErrB"), ("Effective rate, B − A", "drErrDiff"),
                  ("B / A, " + ("effective rate" if ratio == "err" else "rate"), "drRatio"),
                  ("Rate B against your baseline range", "drVerdictB")]
        ds = (sa["display"], sb["display"])
        if "pacer" in ds or "mask" in ds:
            tiles.append(("Pacer time for a line of %s words" % rc.ftext(lw), "drPacerLineMs"))
        if "rsvp" in ds:
            tiles += [("Each flash is requested for", "drWordMs"), ("Each flash took, measured", "drWordMsSeen")]
        if "phrases" in ds:
            tiles.append(("Mean time per phrase", "drPhraseMs"))
        opts.update(sides={"A": {"display": sa["display"], "label": sa["label"]}, "B": {"display": sb["display"], "label": sb["label"]}},
                    kinds=kinds, ratioOf=ratio)
        opts["_cfg_keys"] += ("a", "b", "kinds", "ratioOf", "order")
        order = cfg.get("order", "alternate")
        if order not in ("AB", "BA", "alternate"):
            raise ValueError("%s: cfg[\"order\"] is \"AB\", \"BA\" or \"alternate\"" % kit)
        for k, sc, p in (("A", sa, pa), ("B", sb, pb)):
            slots[k] = rc.slot(k, p, intro=_slot_intro(sc, p), kind=sc["kind"], mode="drill", view="compare",
                               display=sc["display"], questions=sc["questions"], qkinds=sc["qkinds"],
                               write=_write_map(fields, k), target_key=("target" + k) if sc["display"] in TIMED else None,
                               chunk=int(sc["chunk"]), limit=sc["limit"], suppress=sc["suppress"], published=sc["published"])
            main += _slot_markup(k, sc, p, "%s: %s" % (sc["label"], p["title"]))
        main = '      <p class="small-copy" id="rdOrder" style="margin:12px 0 0;"></p>\n' + main
        main += ('      <p class="small-copy" style="margin-top:8px;">' + rc.btn("rdUseBase", "Use my baseline range")
                 + ' <span id="rdBaseNote"></span></p>\n')
        extra_ui = BASELINE_UI_JS + "  var DR_ORDER = %s;\n" % rc.json.dumps(order) + ORDER_UI_JS
        note_q = [pa, pb]
        passages = [pa, pb]
    elif view == "ladder":
        plist = rc.passages_of(cfg, kit, 3)
        opts["hold"] = rc.ftext(hold)
        opts["_cfg_keys"] += ("display", "hold", "kind", "targets")
        disp = cfg.get("display", "pacer")
        if disp not in ("pacer", "mask", "normal"):
            raise ValueError("%s: a ladder runs the pacer (or mask, or normal), not %r" % (kit, disp))
        tgs = cfg.get("targets", [250, 300, 375])
        if not isinstance(tgs, list) or len(tgs) != 3:
            raise ValueError("%s: cfg[\"targets\"] is the three starting targets" % kit)
        for i, p in enumerate(plist, start=1):
            sc = _side_cfg(kit, "run %d" % i, {"display": disp, "target": tgs[i - 1], "kind": cfg.get("kind", "condition")},
                           p, "condition")
            fs = _side_fields(str(i), dict(sc, display="normal"), p, "run %d" % i)
            fs.insert(0, F("t%d" % i, "Target rate, wpm (run %d)" % i, "pos", rc.ftext(sc["target"])))
            fields += fs
            slots[str(i)] = rc.slot(str(i), p, intro=_slot_intro(sc, p), kind=sc["kind"], mode="drill", view="ladder",
                                    display=disp, write=_write_map(fs, str(i)), target_key="t%d" % i if disp != "normal" else None)
            main += _slot_markup(str(i), sc, p, "Run %d: %s" % (i, p["title"]))
            tiles += [("Rate, run %d" % i, "drWpm%d" % i), ("Effective rate, run %d" % i, "drErr%d" % i)]
        tiles += [("Fastest target holding %s" % rc.ftext(hold), "drBestTarget"), ("Its effective rate", "drBestErr"),
                  ("Highest effective rate of the three", "drTopErr")]
        opts["sides"] = {}
        passages = plist
        note_q = plist
    elif view == "repeat":
        pa, pb = rc.passages_of(cfg, kit, 2)
        qs = cfg.get("questions", [False, False, True, True])
        if not isinstance(qs, list) or len(qs) != 4 or not all(isinstance(x, bool) for x in qs):
            raise ValueError("%s: cfg[\"questions\"] lists, for each of the four readings, True or False" % kit)
        opts["_cfg_keys"] += ("questions", "kind")
        for i in range(1, 5):
            p = pa if i < 4 else pb
            sc = _side_cfg(kit, "reading %d" % i, {"questions": qs[i - 1], "kind": cfg.get("kind", "condition")}, p, "condition")
            fs = _side_fields(str(i), sc, p, "reading %d" % i)
            fields += fs
            slots[str(i)] = rc.slot(str(i), p, intro=_slot_intro(sc, p), kind=sc["kind"], mode="drill", view="repeat",
                                    questions=qs[i - 1], write=_write_map(fs, str(i)))
            main += _slot_markup(str(i), sc, p, ("Reading %d of the same passage: " % i if i < 4 else "A new passage: ") + p["title"])
            tiles.append(("Rate, reading %d" % i, "drWpm%d" % i))
        tiles += [("Gain on the repeated passage (3 − 1)", "drRepeatGain"), ("Gain on the new passage (4 − 1)", "drTransferGain")]
        opts["sides"] = {}
        passages = [pa, pb]
        note_q = [pa, pb]
    elif view == "sections":
        (p,) = rc.passages_of(cfg, kit, 1)
        s0, s1 = rc.section_starts(kit, p)
        sc = _side_cfg(kit, "the reading", {"questions": cfg.get("questions", True), "kind": cfg.get("kind", "condition")}, p,
                       "condition")
        opts["_cfg_keys"] += ("questions", "kind")
        part1, part2 = dict(p, paragraphs=p["paragraphs"][:s1]), dict(p, paragraphs=p["paragraphs"][s1:])
        nq = None if sc["questions"] else 0
        fields = [F("words1", "Words in section 1", "count", rc.word_count_passage(part1)),
                  F("seconds1", "Seconds on section 1", "pos"),
                  F("words2", "Words in section 2", "count", rc.word_count_passage(part2)),
                  F("seconds2", "Seconds on section 2", "pos"),
                  F("correct", "Questions right", "nncount", nq), F("total", "Questions asked", "nncount", nq)]
        tiles = [("Rate, section 1", "drRateS1"), ("Rate, section 2", "drRateS2"), ("Rate, whole passage", "drWpm"),
                 ("Comprehension", "drComp"), ("Effective rate", "drErr")]
        slots[""] = rc.slot("", p, intro="Read section 1, press Next section at its end, then read section 2 and press Done. "
                            + _slot_intro(sc, p), kind=sc["kind"], mode="drill", view="sections", questions=sc["questions"],
                            flow="sections", split=s1,
                            write={"words1": "words1", "words2": "words2", "seconds1": "seconds1", "seconds2": "seconds2",
                                   "correct": "correct", "total": "total"}, tick=ATTENTION)
        main = _slot_markup("", sc, p, "Timed reading in two sections: " + p["title"], flow="sections")
        opts["sides"] = {}
        passages = [p]
    else:
        raise ValueError("%s: unknown view %r" % (kit, view))
    title, sub = "Timed reading drill", "rate, comprehension and the effective rate, measured on your own reading"
    intro = ("Your measurement: press Start, read, press Done, answer the questions, press Score, and the boxes fill "
             "with what you did. Before you do, the boxes hold a worked example; the tiles compute from the boxes either way.")
    nq = sorted({len(q.get("questions") or []) for q in locals().get("note_q") or []} - {0})
    if nq:
        intro += " " + one_question_note(nq[-1])
    lab = rc.build_lab(cfg, kit=kit, prefix="dr", view=view, fields=fields, tiles=tiles, fn="drCompute", js=js,
                       opts=opts, title=title, subtitle=sub, panel_title="Your reading, in numbers", panel_intro=intro,
                       main_html=main, passages=passages, slots=slots,
                       ui_js=(locals().get("extra_ui") or "")
                       + ("  var RD_POOL = %s;\n" % rc.json.dumps(opts.get("_pool", [])) + PRACTICE_INIT_JS
                          if view == "practice" else ""))
    return lab


# ---------------------------------------------------------------------------
# eye
# ---------------------------------------------------------------------------

EYE_JS = r"""
  /* eye: the stated model. A word of cpw characters (space included) takes
     cpw / step forward fixations; regressions are a share reg of ALL
     fixations, each one a fixation that does not advance, so fixations per
     word = (cpw / step) / (1 - reg); each fixation costs fix + sac ms. */
  function rdFrac(r) {
    if (Rint(r)) return rdFig(r);
    var f = rdFig(r);
    return (Rsign(r) < 0 ? RD_MINUS : '') + Rtext(Rabs(r)) + (f.indexOf('≈') === 0 ? ' ' + f : ' = ' + f);
  }
  function eyBudget(cpw, step, reg, fix, sac) {
    var per = Rdiv(Rdiv(cpw, step), Rsub(R1, reg)), ms = Rmul(per, Radd(fix, sac));
    return { fix: per, ms: ms, wpm: Rdiv(R(60000n), ms) };
  }
  function eyNeededOf(target, cpw, fix, sac, reg) {
    return Rdiv(Rmul(Rmul(target, cpw), Radd(fix, sac)), Rmul(R(60000n), Rsub(R1, reg)));
  }
  function eyVerdictOf(need, ident, percep) {
    if (Rcmp(need, ident) <= 0) return 'at these settings, within the word-identification span';
    if (Rcmp(need, percep) <= 0) return 'at these settings, beyond the word-identification span but within the perceptual span';
    return 'at these settings, beyond the perceptual span';
  }
  function eyCompute(view, inst, opts) {
    var t = {}, said;
    if (view === 'budget') {
      var reg = opts.split ? Radd(inst.regNeed, inst.regRepair) : inst.reg;
      if (Rcmp(reg, R1) >= 0) return { refuse: 'The regression share must be less than 1: with every fixation going back, the eye never advances' };
      var b = eyBudget(inst.cpw, inst.step, reg, inst.fix, inst.sac);
      t.eyFixPerWord = rdFrac(b.fix) + ' fixations';
      t.eyMsPerWord = rdUnit(b.ms, 'ms');
      t.eyWpm = rdUnit(b.wpm, 'wpm');
      said = 'Fixations per word = (' + rdFig(inst.cpw) + ' / ' + rdFig(inst.step) + ') / (1 − ' + Rtext(reg) + ') = ' + rdFrac(b.fix)
        + '; each costs ' + rdFig(Radd(inst.fix, inst.sac)) + ' ms, so a word takes ' + t.eyMsPerWord + ' and 60,000 / that = ' + t.eyWpm
        + '. The model counts a regression as one fixation that does not advance, so it understates what a regression costs.';
      if (opts.split) {
        var c = eyBudget(inst.cpw, inst.step, inst.regRepair, inst.fix, inst.sac);
        t.eySaved = rdUnit(Rsub(c.wpm, b.wpm), 'wpm');
        said += ' Cutting only the needless regressions (share ' + Rtext(inst.regRepair) + ' left) gives ' + rdUnit(c.wpm, 'wpm') + ', ' + t.eySaved + ' more.';
      }
      return { tiles: t, status: said };
    }
    if (view === 'required') {
      if (Rcmp(inst.reg, R1) >= 0) return { refuse: 'The regression share must be less than 1' };
      var target = inst.target;
      if (opts.claim) {
        target = rdRate(inst.words, inst.seconds);
        t.eyClaimWpm = rdUnit(target, 'wpm');
        t.eyClaimErr = rdUnit(Rmul(target, inst.comp), 'wpm');
      }
      var need = eyNeededOf(target, inst.cpw, inst.fix, inst.sac, inst.reg);
      t.eyNeeded = rdUnit(need, 'characters');
      t.eyVerdict = eyVerdictOf(need, Rparse(opts.identify), Rparse(opts.perceptual));
      said = rdUnit(target, 'wpm') + ' × ' + rdFig(inst.cpw) + ' characters × ' + rdFig(Radd(inst.fix, inst.sac)) + ' ms / (60,000 × (1 − '
        + Rtext(inst.reg) + ')) = ' + t.eyNeeded + ' a forward fixation must advance: ' + t.eyVerdict
        + ' (word identification taken as ' + opts.identify + ' characters, the perceptual span as ' + opts.perceptual
        + ', after Rayner 1998).';
      return { tiles: t, status: said };
    }
    /* lines: f = cpl / step fixations a line, f - 1 forward saccades, one return sweep */
    if (Rcmp(inst.cpl, inst.step) < 0) return { refuse: 'A line must be at least one saccade long: characters per line below the step' };
    var f = Rdiv(inst.cpl, inst.step), msl = Radd(Radd(Rmul(f, inst.fix), Rmul(Rsub(f, R1), inst.sac)), inst.sweep);
    var total = Rmul(msl, inst.lines);
    t.eyFixPerLine = rdFrac(f) + ' fixations';
    t.eySweepShare = rdShare(Rinv(f));
    t.eyMsPerLine = rdUnit(msl, 'ms');
    t.eySweepTime = rdShare(Rdiv(inst.sweep, msl));
    t.eyTotal = rdUnit(Rdiv(total, R(1000n)), 's');
    said = rdFig(inst.cpl) + ' / ' + rdFig(inst.step) + ' = ' + rdFrac(f) + ' fixations a line, ' + rdFrac(Rsub(f, R1))
      + ' forward saccades and 1 return sweep, so ' + t.eySweepShare + ' of the eye movements are sweeps; a line takes ' + t.eyMsPerLine + '.';
    return { tiles: t, status: said };
  }
"""


def _eye(cfg, view, kit):
    opts = {"_cfg_keys": ()}
    if view == "budget":
        split = cfg.get("split", False)
        if not isinstance(split, bool):
            raise ValueError("%s: cfg[\"split\"] is True or False" % kit)
        opts.update(split=split, _cfg_keys=("split",))
        fields = [F("fix", "Fixation, ms", "pos"), F("sac", "Saccade, ms", "nn"),
                  F("step", "Characters per forward saccade", "pos")]
        fields += ([F("regNeed", "Needless regressions, share of fixations", "share"),
                    F("regRepair", "Repair regressions, share of fixations", "share")] if split
                   else [F("reg", "Regressions, share of fixations (below 1)", "share")])
        fields.append(F("cpw", "Characters per word, space included", "pos", 6))
        tiles = [("Fixations per word", "eyFixPerWord"), ("Time per word", "eyMsPerWord"), ("Rate the model allows", "eyWpm")]
        if split:
            tiles.append(("Gained by cutting needless regressions only", "eySaved"))
        intro = ("A stated model: fixations per word = (characters per word / characters per saccade) / (1 − regression share); "
                 "time per word = fixations × (fixation + saccade). A regression is counted as one more fixation that does not "
                 "advance, which understates its cost: a real regression also travels back and re-reads (Rayner 1998).")
        title = "The eye-movement budget"
    elif view == "required":
        claim = cfg.get("claim", False)
        if not isinstance(claim, bool):
            raise ValueError("%s: cfg[\"claim\"] is True or False" % kit)
        ident = rc.num(kit, cfg, "identify", 8, lo=1, hi=200)
        percep = rc.num(kit, cfg, "perceptual", 15, lo=1, hi=200)
        if percep < ident:
            raise ValueError("%s: the perceptual span cannot be narrower than the identification span" % kit)
        opts.update(claim=claim, identify=rc.ftext(ident), perceptual=rc.ftext(percep),
                    _cfg_keys=("claim", "identify", "perceptual"))
        fields = ([F("words", "Words the claim says were read", "pos"), F("seconds", "In this many seconds", "pos"),
                   F("comp", "Comprehension the claim allows (share)", "share", 1)] if claim
                  else [F("target", "Target rate, wpm", "pos")])
        fields += [F("fix", "Fixation, ms", "pos", 225), F("sac", "Saccade, ms", "nn", 30),
                   F("cpw", "Characters per word, space included", "pos", 6), F("reg", "Regressions, share of fixations", "share", 0)]
        tiles = ([("The claimed rate", "eyClaimWpm"), ("Effective rate at that comprehension", "eyClaimErr")] if claim else [])
        tiles += [("Characters a forward fixation must advance", "eyNeeded"), ("Against the spans", "eyVerdict")]
        intro = ("A stated model: characters per fixation = rate × characters per word × (fixation + saccade) / (60,000 × (1 − "
                 "regression share)), set against a word-identification span of %s characters and a perceptual span of %s "
                 "(Rayner 1998). It says what a claim would need, not whether a reader did it." % (rc.ftext(ident), rc.ftext(percep)))
        title = "The speed a claim needs"
    elif view == "lines":
        fields = [F("cpl", "Characters per line", "pos"), F("lines", "Lines", "count"), F("step", "Characters per forward saccade", "pos", 8),
                  F("fix", "Fixation, ms", "pos", 225), F("sac", "Saccade, ms", "nn", 30),
                  F("sweep", "Return sweep with its corrective fixation, ms", "nn")]
        tiles = [("Fixations per line", "eyFixPerLine"), ("Share of eye movements that are return sweeps", "eySweepShare"),
                 ("Time per line", "eyMsPerLine"), ("Share of the time in sweeps", "eySweepTime"), ("Time for all the lines", "eyTotal")]
        intro = ("A stated model: a line of characters-per-line / step fixations has one fewer forward saccade and one return "
                 "sweep; time per line = fixations × fixation + forward saccades × saccade + sweep.")
        title = "Lines and return sweeps"
    else:
        raise ValueError("%s: unknown view %r" % (kit, view))
    return rc.build_lab(cfg, kit=kit, prefix="ey", view=view, fields=fields, tiles=tiles, fn="eyCompute", js=EYE_JS, opts=opts,
                        title=title, subtitle="a stated model of fixations and saccades, computed exactly",
                        panel_title="The model's quantities", panel_intro=intro)


# ---------------------------------------------------------------------------
# flash
# ---------------------------------------------------------------------------

FLASH_JS = r"""
  /* flash/span: letters identified at each position of a brief flash,
     scored by position from the centre (-k..+k). This measures letter
     identification in an unreadable string, not the perceptual span in
     reading. flash/schulte: a 5x5 table time. */
  function flScore(targets, typed) {
    if (typed.length !== targets.length) return { refuse: 'Type one answer for each flashed string: ' + targets.length + ' flashed, ' + typed.length + ' typed' };
    var len = targets[0].length;
    if (len % 2 === 0 || len < 3) return { refuse: 'Flashed strings have an odd length of at least 3, so that one letter is at the centre' };
    for (var i = 0; i < targets.length; i++) {
      if (targets[i].length !== len) return { refuse: 'Every flashed string must have the same length (' + len + ')' };
      if (typed[i].length > len) return { refuse: 'Answer ' + (i + 1) + ' is longer than the flashed string' };
    }
    /* A typed '.' is a position that was not asked (partial report); any
       other character, or none, is an answer: right when it is the letter. */
    var k = (len - 1) / 2, hits = [], asked = [];
    for (var p = 0; p < len; p++) { hits.push(0); asked.push(0); }
    targets.forEach(function (t, i) {
      for (var p = 0; p < len; p++) {
        if (typed[i].charAt(p) === '.') continue;
        asked[p] += 1;
        if (typed[i].charAt(p) === t.charAt(p)) hits[p] += 1;
      }
    });
    return { k: k, n: targets.length, hits: hits, asked: asked };
  }
  function flAcc(sc, pos) { var a = sc.asked[pos + sc.k]; return a ? R(BigInt(sc.hits[pos + sc.k]), BigInt(a)) : null; }
  /* The outermost position on each side, among those asked, whose accuracy is at least 1/2. */
  function flSpanOf(sc) {
    var left = 0, right = 0, half = R(1n, 2n), a;
    for (var p = 1; p <= sc.k; p++) {
      a = flAcc(sc, -p); if (a && Rcmp(a, half) >= 0) left = p;
      a = flAcc(sc, p); if (a && Rcmp(a, half) >= 0) right = p;
    }
    return { left: left, right: right };
  }
  /* The Schulte table for a seed: the numbers 1..25 shuffled by Fisher-Yates
     driven by the stated LCG s -> (1103515245 s + 12345) mod 2^31, j = s mod (i + 1). */
  function flTable(seed) {
    var cells = [], s = BigInt(seed);
    for (var i = 1; i <= 25; i++) cells.push(i);
    for (var i2 = 24; i2 >= 1; i2--) {
      s = (1103515245n * s + 12345n) % 2147483648n;
      var j = Number(s % BigInt(i2 + 1)), tmp = cells[i2];
      cells[i2] = cells[j]; cells[j] = tmp;
    }
    return cells;
  }
  function flGridHtml(cells, live) {
    return '<div style="display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:4px;max-width:20rem;margin:0 auto;position:relative;">'
      + cells.map(function (c, i) {
        return '<button type="button" class="btn small" data-c="' + c + '"' + (live ? '' : ' disabled') + ' style="min-height:2.6rem;justify-content:center;'
          + (i === 12 ? 'outline:2px solid var(--cyan);' : '') + '">' + c + '</button>';
      }).join('') + '</div>';
  }
  function flCompute(view, inst, opts) {
    var t = {};
    if (view === 'span') {
      var sc = flScore(inst.targets, inst.typed);
      if (sc.refuse) return sc;
      var sp = flSpanOf(sc), rows = [], c = flAcc(sc, 0), edgeAsked = sc.asked[0] + sc.asked[2 * sc.k];
      t.flCentre = c ? rdShare(c) : 'not asked';
      t.flEdge = edgeAsked ? rdShare(R(BigInt(sc.hits[0] + sc.hits[2 * sc.k]), BigInt(edgeAsked))) : 'not asked';
      t.flSpan = 'left ' + sp.left + ', right ' + sp.right;
      for (var p = -sc.k; p <= sc.k; p++) {
        var acc = flAcc(sc, p);
        rows.push([(p > 0 ? '+' : p < 0 ? RD_MINUS : '') + Math.abs(p), sc.hits[p + sc.k] + ' of ' + sc.asked[p + sc.k], acc ? rdShare(acc) : 'not asked']);
      }
      return { tiles: t, status: sc.n + ' flashed strings of ' + (2 * sc.k + 1) + ' letters. Letters identified at the centre: ' + t.flCentre
        + '; at the outermost positions: ' + t.flEdge + '. Positions with at least half identified reach ' + t.flSpan
        + '. Random letters measure letter identification by position; reading words is a different task.',
        table: { caption: 'Letters identified, by position from the centre', head: ['position', 'identified of asked', 'share'], rows: rows } };
    }
    if (Rcmp(inst.seed, R(2147483648n)) >= 0) return { refuse: 'The seed is a whole number below 2,147,483,648' };
    t.flTime = rdUnit(inst.seconds, 's');
    t.flPerCell = rdUnit(Rdiv(inst.seconds, R(25n)), 's');
    t.flErrors = rdFig(inst.errors);
    return { tiles: t, status: '25 cells in ' + t.flTime + ' is ' + t.flTime.replace(/ s$/, '') + ' / 25 = ' + t.flPerCell + ' a cell, with '
      + t.flErrors + ' wrong clicks. A faster table shows a faster table; whether reading moves with it is for your log to show.',
      html: '<p class="small-copy" style="text-align:center;">The table for seed ' + rdFig(inst.seed) + ':</p>' + flGridHtml(flTable(String(inst.seed.n)), false) };
  }
"""

FLASH_SPAN_UI_JS = r"""
  /* The flash drill, partial report: a fixation mark, FL_LEN letters for
     FL_MS ms (requested), a mask, then FL_CUES cued positions, each answered
     by four letter buttons. Only on Start. The measured display time is printed. */
  (function () {
    var startB = document.getElementById('flStart'), stage = document.getElementById('flStage'), msg = document.getElementById('flMsg');
    if (!startB) return;
    var targets = [], typed = [], measured = [], running = false, K = (FL_LEN - 1) / 2;
    var LETTERS = 'BCDFGHJKLMNPQRSTVWXZ';
    function pick(n) { return Math.floor(Math.random() * n); }
    function randomString() { var s = ''; for (var i = 0; i < FL_LEN; i++) s += LETTERS.charAt(pick(LETTERS.length)); return s; }
    function cues() { var c = [], p; while (c.length < FL_CUES) { p = pick(FL_LEN); if (c.indexOf(p) < 0) c.push(p); } return c.sort(function (a, b) { return a - b; }); }
    function options(right) {
      var o = [right], l;
      while (o.length < 4) { l = LETTERS.charAt(pick(LETTERS.length)); if (o.indexOf(l) < 0) o.push(l); }
      for (var i = o.length - 1; i > 0; i--) { var j = pick(i + 1), t = o[i]; o[i] = o[j]; o[j] = t; }
      return o;
    }
    function posName(p) { var d = p - K; return d === 0 ? 'the centre' : (d < 0 ? RD_MINUS + (-d) + ' (left)' : '+' + d + ' (right)'); }
    function ask(s, cue, j, answer, n) {
      if (j >= cue.length) { typed.push(answer.join('')); trial(n + 1); return; }
      var p = cue[j], row = '';
      for (var i = 0; i < FL_LEN; i++) row += i === p ? '?' : (cue.indexOf(i) >= 0 ? '_' : '·');
      stage.innerHTML = '<div aria-hidden="true">' + row + '</div><div class="small-copy" style="font-family:inherit;letter-spacing:0;margin:6px 0;">Which letter was at position '
        + posName(p) + '? (' + (j + 1) + ' of ' + cue.length + ')</div><div style="display:flex;gap:6px;justify-content:center;flex-wrap:wrap;">'
        + options(s.charAt(p)).map(function (l) { return '<button type="button" class="btn small" data-l="' + l + '">' + l + '</button>'; }).join('')
        + ' <button type="button" class="btn small" data-l="-">not seen</button></div>';
      var bs = stage.getElementsByTagName('button');
      for (var b = 0; b < bs.length; b++) bs[b].addEventListener('click', function (e) {
        answer[p] = e.currentTarget.getAttribute('data-l'); ask(s, cue, j + 1, answer, n);
      });
      bs[0].focus();
    }
    function trial(n) {
      if (n >= FL_N) {
        running = false; stage.innerHTML = '';
        rdWrite({ targets: targets.join('; '), typed: typed.join('; ') });
        var m = measured.slice().sort(function (a, b) { return a - b; });
        msg.textContent = 'Done. Requested ' + FL_MS + ' ms; measured on this screen: ' + m[0] + ' to ' + m[m.length - 1]
          + ' ms. The display time is requested, not guaranteed.';
        rdLogAppend({ mode: 'flash', view: 'span', side: '', passage: '', display: 'flash', words: 0, ms: 0, correct: 0,
                      total: FL_N, kind: FL_KIND, extra: { len: FL_LEN, ms: FL_MS, cues: FL_CUES, measured: measured } }, msg);
        startB.style.display = '';
        return;
      }
      var s = randomString(), cue = cues(), answer = [];
      for (var i = 0; i < FL_LEN; i++) answer.push('.');
      targets.push(s);
      msg.textContent = 'String ' + (n + 1) + ' of ' + FL_N + ': look at the + .';
      stage.textContent = new Array(K + 1).join(' ') + '+' + new Array(K + 1).join(' ');
      setTimeout(function () {
        var t0 = performance.now();
        stage.textContent = s;
        setTimeout(function () {
          measured.push(Math.round(performance.now() - t0));
          stage.textContent = new Array(FL_LEN + 1).join('#');
          setTimeout(function () { msg.textContent = 'Answer for the marked positions only.'; ask(s, cue, 0, answer, n); }, 300);
        }, FL_MS);
      }, 700);
    }
    startB.addEventListener('click', function () {
      if (running) return;
      running = true; targets = []; typed = []; measured = [];
      startB.style.display = 'none';
      trial(0);
    });
  })();
"""

FLASH_SCHULTE_UI_JS = r"""
  /* The Schulte drill: a fresh random seed, a live table, click 1..25 in order. */
  (function () {
    var startB = document.getElementById('flStart'), stage = document.getElementById('flStage'), msg = document.getElementById('flMsg');
    if (!startB) return;
    startB.addEventListener('click', function () {
      var seed = Math.floor(Math.random() * 2147483647), next = 1, errors = 0, t0;
      stage.innerHTML = flGridHtml(flTable(String(seed)), true);
      msg.textContent = 'Keep your eyes on the outlined centre cell and click 1, 2, 3 ... 25 in order.';
      startB.style.display = 'none';
      t0 = performance.now();
      stage.addEventListener('click', function handler(e) {
        var b = e.target;
        if (!b || !b.getAttribute || !b.getAttribute('data-c')) return;
        if (+b.getAttribute('data-c') !== next) { errors += 1; return; }
        b.disabled = true; next += 1;
        if (next > 25) {
          var ms = Math.max(1, Math.round(performance.now() - t0));
          stage.removeEventListener('click', handler);
          stage.innerHTML = '';
          rdWrite({ seconds: rdMsText(ms), errors: errors, seed: seed });
          rdLogAppend({ mode: 'flash', view: 'schulte', side: '', passage: '', display: 'table', words: 0, ms: ms, correct: 25,
                        total: 25, kind: FL_KIND, extra: { errors: errors, seed: seed } }, msg);
          msg.textContent = 'Done in ' + rdUnit(Rparse(rdMsText(ms)), 's') + ' with ' + errors + ' wrong clicks. Logged.';
          startB.textContent = 'Another table'; startB.style.display = '';
        }
      });
    });
  })();
"""

FLASH_MSTEXT_JS = r"""
  function rdMsText(ms) {
    ms = Math.max(1, Math.round(ms));
    var w = Math.floor(ms / 1000), f = ms % 1000;
    return f ? w + '.' + String(f + 1000).slice(1).replace(/0+$/, '') : String(w);
  }
"""


def _flash(cfg, view, kit):
    kind = rc.log_kind(kit, cfg.get("kind"), "practice")
    if view == "span":
        ln = rc.num(kit, cfg, "len", 15, lo=3, hi=21, whole=True)
        if ln.numerator % 2 == 0:
            raise ValueError("%s: cfg[\"len\"] must be odd, so one letter sits at the centre" % kit)
        ms = rc.num(kit, cfg, "ms", 150, lo=17, hi=2000, whole=True)
        n = rc.num(kit, cfg, "n", 10, lo=1, hi=20, whole=True)
        cues = rc.num(kit, cfg, "cues", 3, lo=2, hi=3, whole=True)
        fields = [F("targets", "Flashed strings, separated by ;", ("strings", 1, 40, False)),
                  F("typed", "Answers by position, in the same order (. not asked, - asked and not seen)", ("strings", 1, 40, True))]
        tiles = [("Letters identified at the centre, %d ms flash" % ms, "flCentre"),
                 ("Letters identified at the outermost positions, %d ms flash" % ms, "flEdge"),
                 ("Positions with at least half identified", "flSpan")]
        cfgk = ("len", "ms", "n", "cues", "kind")

        def check(where, p, inst):
            t = [s for s in inst["targets"].split("; ")]
            y = [s for s in inst["typed"].split("; ")]
            if len(t) != len(y) or len({len(s) for s in t}) != 1 or len(t[0]) % 2 == 0 or any(len(a) > len(t[0]) for a in y):
                raise ValueError("%s: targets must share one odd length and typed must match them one for one" % where)
        ui = ("  var FL_LEN = %d, FL_MS = %d, FL_N = %d, FL_CUES = %d, FL_KIND = %s;\n" % (ln, ms, n, cues, rc.json.dumps(kind))
              + FLASH_SPAN_UI_JS)
        title = "Letters identified by position in a %d ms flash" % ms
        intro = ("Your measurement: a + marks where to look, then %d random letters are flashed for %d ms (requested; the "
                 "screen may show them a little longer, and the drill prints what it measured), then a mask. Then %d of the "
                 "positions are marked, one at a time, and you pick the letter that was there from four (or say you did not "
                 "see it). Letters are scored by their position from the centre, −%d to +%d. A flash this short is over before "
                 "the eyes could move: a saccade takes about 175 to 200 ms to start. Random letters measure letter "
                 "identification by position, not the perceptual span in reading, which is wider to the right. %s"
                 % (ln, ms, cues, (ln - 1) // 2, (ln - 1) // 2, rc.PHOTO_NOTE))
    elif view == "schulte":
        fields = [F("seconds", "Seconds for the table", "pos"), F("errors", "Wrong clicks", "nncount", 0),
                  F("seed", "Table seed", "nncount")]
        tiles = [("Time", "flTime"), ("Time per cell", "flPerCell"), ("Wrong clicks", "flErrors")]
        cfgk = ("kind",)
        check = None
        ui = "  var FL_KIND = %s;\n" % rc.json.dumps(kind) + FLASH_SCHULTE_UI_JS
        title = "A Schulte table"
        intro = ("Your measurement: 25 numbers in a 5×5 table, found in order with your eyes on the centre. A drill uses a "
                 "random table; a worked example uses its seed, with the stated generator, so it always shows the same table.")
    else:
        raise ValueError("%s: unknown view %r" % (kit, view))
    main = ('      <div class="card card-pad" style="margin-top:12px;">\n'
            '        <p class="small-copy" id="flMsg" aria-live="polite" style="margin:0 0 8px;">Press Start when you are ready.</p>\n'
            '        ' + rc.btn("flStart", "Start", primary=True) + '\n'
            '        <div id="flStage" style="margin-top:12px;min-height:3.2rem;text-align:center;font-family:monospace;'
            'font-size:clamp(1rem, 5vw, 1.6rem);letter-spacing:0.15em;overflow-wrap:anywhere;"></div>\n'
            '      </div>\n')
    lab = rc.build_lab(cfg, kit=kit, prefix="fl", view=view, fields=fields, tiles=tiles, fn="flCompute", js=FLASH_JS,
                       opts={"_cfg_keys": cfgk}, title=title, subtitle="a drill of the eyes, scored exactly",
                       panel_title="The drill, in numbers", panel_intro=intro, main_html=main, check=check,
                       ui_js=FLASH_MSTEXT_JS + ui)
    return lab


# ---------------------------------------------------------------------------
# scan
# ---------------------------------------------------------------------------

SCAN_JS = r"""
  /* scan: seconds per target found, words passed over per second. */
  function scCompute(view, inst) {
    var t = {};
    if (Rcmp(inst.found, inst.targets) > 0) return { refuse: 'More found than there were targets' };
    t.scFound = rdFig(inst.found) + ' of ' + rdFig(inst.targets);
    t.scPerTarget = Rzero(inst.found) ? 'none found' : rdUnit(Rdiv(inst.seconds, inst.found), 's');
    t.scWordsPerSec = rdUnit(Rdiv(inst.words, inst.seconds), 'words a second');
    if (view === 'find') t.scWrong = rdFig(inst.wrong);
    return { tiles: t, status: t.scFound + ' in ' + rdUnit(inst.seconds, 's') + ': ' + t.scPerTarget + ' per target found, over a text of '
      + rdFig(inst.words) + ' words, ' + t.scWordsPerSec + ' (' + rdUnit(Rdiv(Rmul(inst.words, R(60n)), inst.seconds), 'a minute') + ')'
      + '. Scanning is a search for a known form, not reading; its speed says nothing about reading rate.' };
  }
"""


def _scan(cfg, view, kit):
    (p,) = rc.passages_of(cfg, kit, 1)
    kind = rc.log_kind(kit, cfg.get("kind"), "other")
    words = rc.word_count_passage(p)
    if view == "find":
        if "targets" in cfg:
            targets = rc.resolve_targets(kit, p, cfg["targets"])
        elif "targets" in p:
            targets = rc.resolve_targets(kit, p, p["targets"])
        else:
            raise ValueError("%s: scan/find needs targets, in cfg[\"targets\"] or the passage's \"targets\"" % kit)
        lim = rc.num(kit, cfg, "limit", None, lo=10, hi=1800, whole=True)
        fields = [F("found", "Targets found", "nncount"), F("wrong", "Wrong clicks", "nncount", 0),
                  F("targets", "Targets", "count", len(targets)), F("seconds", "Seconds", "pos"), F("words", "Words in the text", "count", words)]
        tiles = [("Found", "scFound"), ("Seconds per target found", "scPerTarget"), ("Words passed over", "scWordsPerSec"),
                 ("Wrong clicks", "scWrong")]
        sl = rc.slot("", p, intro="Each prompt names something to find. Click the word that answers it (or Tab to it and press "
                     "Enter); a wrong click is counted and you keep looking. Press Start when you are ready.",
                     kind=kind, mode="scan", view="find", flow="find", questions=False, targets=targets,
                     limit=None if lim is None else int(lim),
                     write={"found": "found", "wrong": "wrong", "seconds": "seconds", "words": "words", "targets": "targets"})
        main = rc.slot_html("", "Scan: " + p["title"], sl["intro"], rc.btn("rdNext", "Skip this one", hidden=True))
        cfgk = ("passage", "targets", "limit", "kind")
    elif view == "inspect":
        lim = rc.num(kit, cfg, "limit", 300, lo=10, hi=1800, whole=True)
        if not p.get("questions"):
            raise ValueError("%s: scan/inspect asks the passage's questions, and %s has none" % (kit, p["id"]))
        fields = [F("found", "Questions answered right", "nncount"), F("targets", "Questions", "count", len(p["questions"])),
                  F("seconds", "Seconds of inspection", "pos"), F("words", "Words in the document", "count", words)]
        tiles = [("Answered", "scFound"), ("Seconds per right answer", "scPerTarget"), ("Words passed over", "scWordsPerSec")]
        sl = rc.slot("", p, intro="Inspect the document for up to %d seconds (it disappears then, or press Done), then answer "
                     "questions about what it is and where things are in it." % lim, kind=kind, mode="scan", view="inspect",
                     flow="inspect", limit=int(lim), write={"found": "found", "targets": "targets", "seconds": "seconds", "words": "words"})
        main = rc.slot_html("", "Inspect: " + p["title"], sl["intro"])
        cfgk = ("passage", "limit", "kind")
    else:
        raise ValueError("%s: unknown view %r" % (kit, view))
    return rc.build_lab(cfg, kit=kit, prefix="sc", view=view, fields=fields, tiles=tiles, fn="scCompute", js=SCAN_JS,
                        opts={"_cfg_keys": cfgk}, title="Scanning" if view == "find" else "Inspectional reading",
                        subtitle="a search for a known form, timed",
                        panel_title="The search, in numbers",
                        panel_intro="Your measurement: the boxes fill when the drill ends; before that they hold a worked example.",
                        main_html=main, passages=[p], slots={"": sl})


# ---------------------------------------------------------------------------
# entry point
# ---------------------------------------------------------------------------

VIEWS = {
    "drill": ("single", "compare", "ladder", "repeat", "sections", "practice"),
    "eye": ("budget", "required", "lines"),
    "flash": ("span", "schulte"),
    "scan": ("find", "inspect"),
    "triage": ("plan",),
    "text": ("readability", "coverage", "volume"),
    "recall": ("free", "delayed", "schedule"),
    "log": ("noise", "gears", "history", "plan", "profile"),
}
_HERE = {"drill": _drill, "eye": _eye, "flash": _flash, "scan": _scan}


def readkit_lab(cfg):
    """The Reading Faster kit. cfg["mode"] chooses the mode, cfg["view"] the view; unknown ones raise."""
    cfg = cfg or {}
    mode = cfg.get("mode")
    if mode not in VIEWS:
        raise ValueError("readkit_lab: unknown mode %r; the eight modes are %s" % (mode, ", ".join(VIEWS)))
    view = cfg.get("view", VIEWS[mode][0])
    if view not in VIEWS[mode]:
        raise ValueError("readkit/%s: unknown view %r; the views are %s" % (mode, view, ", ".join(VIEWS[mode])))
    kit = "%s/%s/%s" % (KIT, mode, view)
    if mode in _HERE:
        return _HERE[mode](cfg, view, kit)
    from . import readkit_b
    return readkit_b.readkit_b_lab(cfg, mode, view, kit)
