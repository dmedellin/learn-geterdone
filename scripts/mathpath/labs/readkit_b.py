"""readkit_b -- the Reading Faster kit's triage, text, recall and log modes.

Built by readkit.readkit_lab (imported only when one of these modes is asked
for). Same conventions as readkit.py: text inputs <prefix>In<Key>, tiles, one
pure <xx>Compute(view, inst, opts) per mode for scripts/mathcheck.js, and
browser-only UI code that does nothing until a button is clicked (except
reading the log at load, which starts nothing).

  triage  plan: read / skim / skip a stack of documents under a time budget
  text    readability (Flesch, Flesch-Kincaid, by the kit's counting rule),
          coverage (unknown words), volume (words and books a year)
  recall  free (free recall or a summary, scored by the reader's ticks),
          delayed (reread against retrieve, tested again days later),
          schedule (an expanding review schedule)
  log     noise, gears, history, plan, profile: the reader's own log
"""

from . import readkit_core as rc
from .readkit import F

# ---------------------------------------------------------------------------
# triage
# ---------------------------------------------------------------------------

TRIAGE_JS = r"""
  /* triage: time = words read / read rate + words skimmed / skim rate;
     value covered = sum(value x coverage) / sum(value), read = 1, skim = the
     skim coverage, skip = 0. */
  function trCompute(view, inst) {
    var mins = R0, cov = R0, all = R0, t = {}, rows = [];
    inst.items.forEach(function (it) {
      var m = R0, c = R0;
      if (it.choice === 'read') { m = Rdiv(it.words, inst.read); c = R1; }
      if (it.choice === 'skim') { m = Rdiv(it.words, inst.skim); c = inst.coverage; }
      mins = Radd(mins, m); cov = Radd(cov, Rmul(it.value, c)); all = Radd(all, it.value);
      rows.push([it.title, rdFig(it.words), rdFig(it.value), it.choice, rdUnit(m, 'min')]);
    });
    t.trMinutes = rdUnit(mins, 'min');
    t.trCovered = rdShare(Rdiv(cov, all));
    var spare = Rsub(inst.budget, mins);
    t.trFits = Rsign(spare) >= 0 ? 'fits, ' + rdUnit(spare, 'min') + ' to spare' : 'over the budget by ' + rdUnit(Rneg(spare), 'min');
    var html = '<div class="table-wrap"><table class="tt"><caption>Choose for each document</caption><tbody>'
      + inst.items.map(function (it, i) {
        return '<tr><td>' + rdEsc(it.title) + '</td><td>' + ['read', 'skim', 'skip'].map(function (c) {
          return '<button type="button" class="btn small' + (c === it.choice ? ' primary' : '') + '" data-i="' + i + '" data-c="' + c
            + '" aria-pressed="' + (c === it.choice) + '">' + c + '</button>';
        }).join(' ') + '</td></tr>';
      }).join('') + '</tbody></table></div>';
    return { tiles: t, html: html, status: 'The plan takes ' + t.trMinutes + ' against a budget of ' + rdUnit(inst.budget, 'min')
      + ' and covers ' + t.trCovered + ' of the value (a skim is taken to cover ' + rdShare(inst.coverage) + ' of a document\'s value).',
      table: { caption: 'The plan', head: ['document', 'words', 'value', 'choice', 'time'], rows: rows } };
  }
"""

TRIAGE_UI_JS = r"""
  /* The choice buttons rewrite the items box: the plan is always the box's text. */
  (function () {
    var ex = document.getElementById('trExtra');
    ex.addEventListener('click', function (e) {
      var b = e.target;
      if (!b || !b.getAttribute || b.getAttribute('data-c') === null) return;
      var f = SPEC.filter(function (s) { return s.key === 'items'; })[0], items;
      try { items = rdField(f, field(f.id).value); } catch (err) { return; }
      items[+b.getAttribute('data-i')].choice = b.getAttribute('data-c');
      rdWrite({ items: items.map(function (it) {
        return [it.title, Rtext(it.words), Rtext(it.value), it.choice].join(', ');
      }).join('; ') });
    });
  })();
"""


def _triage(cfg, view, kit):
    fields = [F("items", "Documents: title, words, value, read/skim/skip; separated by ;",
                ("rec", [("title", "name"), ("words", "count"), ("value", "pos"), ("choice", ("word", ["read", "skim", "skip"]))],
                 1, 12, False)),
              F("read", "Reading rate, wpm", "pos", 250), F("skim", "Skimming rate, wpm", "pos", 750),
              F("coverage", "Share of a document's value a skim covers", "share", "1/2"),
              F("budget", "Time budget, minutes", "pos")]
    tiles = [("Time the plan takes", "trMinutes"), ("Value covered", "trCovered"), ("Against the budget", "trFits")]
    return rc.build_lab(cfg, kit=kit, prefix="tr", view=view, fields=fields, tiles=tiles, fn="trCompute", js=TRIAGE_JS,
                        opts={"_cfg_keys": ()}, title="Triaging a reading list",
                        subtitle="what to read, what to skim, what to skip",
                        panel_title="The plan, in numbers",
                        panel_intro=("A stated model: a document read costs its words over your reading rate, one skimmed its "
                                     "words over your skimming rate, one skipped nothing; a skim is credited with a stated "
                                     "share of the document's value. Choose read, skim or skip for each document."),
                        ui_js=TRIAGE_UI_JS)


# ---------------------------------------------------------------------------
# text
# ---------------------------------------------------------------------------

TEXT_JS = r"""
  /* text: Flesch Reading Ease = 206.835 - 1.015 (words / sentences) - 84.6 (syllables / words);
     Flesch-Kincaid grade = 0.39 (words / sentences) + 11.8 (syllables / words) - 15.59.
     The constants are exact decimals, so the formulas are exact rationals. */
  function txFormulas(w, s, y) {
    var ws = Rdiv(w, s), yw = Rdiv(y, w);
    return { fre: Rsub(Rsub(Rparse('206.835'), Rmul(Rparse('1.015'), ws)), Rmul(Rparse('84.6'), yw)),
             grade: Rsub(Radd(Rmul(Rparse('0.39'), ws), Rmul(Rparse('11.8'), yw)), Rparse('15.59')) };
  }
  function txCompute(view, inst) {
    var t = {};
    if (view === 'readability') {
      var f = txFormulas(inst.words, inst.sentences, inst.syllables);
      t.txWords = rdFig(inst.words); t.txSentences = rdFig(inst.sentences);
      t.txSyllables = rdFig(inst.syllables) + ' (by the rule)';
      t.txFre = rdFig(f.fre); t.txGrade = rdFig(f.grade);
      return { tiles: t, status: '206.835 − 1.015 × ' + rdFig(Rdiv(inst.words, inst.sentences)) + ' − 84.6 × '
        + rdFig(Rdiv(inst.syllables, inst.words)) + ' = ' + t.txFre + ' reading ease; grade ' + t.txGrade
        + '. Syllables are counted by a rule, an approximation; the formulas see sentence and word length, not ideas.' };
    }
    if (view === 'coverage') {
      if (Rcmp(inst.unknown, inst.tokens) > 0) return { refuse: 'More unknown words than words in the text' };
      if (inst.total !== undefined && Rcmp(inst.correct, inst.total) > 0) return { refuse: 'More questions right than asked' };
      t.txCoverage = rdShare(Rdiv(Rsub(inst.tokens, inst.unknown), inst.tokens));
      t.txOneIn = Rzero(inst.unknown) ? 'no unknown words' : 'one unknown in every ' + rdFig(Rdiv(inst.tokens, inst.unknown)) + ' tokens';
      /* Timed: the rate while marking; with questions: comprehension afterwards. */
      if (inst.seconds !== undefined) t.txWpm = rdUnit(rdRate(inst.tokens, inst.seconds), 'wpm');
      if (inst.total !== undefined) t.txComp = Rzero(inst.total) ? 'no questions' : rdShare(Rdiv(inst.correct, inst.total));
      return { tiles: t, status: rdFig(inst.unknown) + ' unknown of ' + rdFig(inst.tokens) + ' words: coverage ' + t.txCoverage
        + ', one unknown word every ' + (Rzero(inst.unknown) ? '(none)' : rdFig(Rdiv(inst.tokens, inst.unknown))) + ' words. Hu and Nation put unassisted reading near 98%.'
        + (t.txWpm ? ' Read while marking at ' + t.txWpm + (t.txComp ? ', comprehension ' + t.txComp : '') + '.' : t.txComp ? ' Comprehension ' + t.txComp + '.' : '') };
    }
    var w = Rmul(Rmul(inst.minutes, inst.wpm), inst.days);
    t.txWordsYear = rdUnit(w, 'words');
    t.txBooksYear = rdUnit(Rdiv(w, inst.bookWords), 'books');
    return { tiles: t, status: rdFig(inst.minutes) + ' min × ' + rdFig(inst.wpm) + ' wpm × ' + rdFig(inst.days) + ' days = ' + t.txWordsYear
      + ', or ' + t.txBooksYear + ' of ' + rdFig(inst.bookWords) + ' words.' };
  }
"""

TEXT_READ_UI_JS = r"""
  /* A preset that names a bank passage is COUNTED here, by the rule, and the
     passage is shown; typed counts are used as they are. "Count my text"
     counts pasted text the same way. */
  function rdFill(inst) {
    var id = inst.__passage;
    var view = document.getElementById('txPassage');
    if (!id || !PASSAGES[id]) { if (view) view.innerHTML = ''; return inst; }
    var c = rdCounts(PASSAGES[id]);
    if (view) view.innerHTML = '<h4>' + rdEsc(PASSAGES[id].title) + '</h4>' + PASSAGES[id].paragraphs.map(function (p) {
      return rdHeading(p) ? '<h4>' + rdEsc(rdPlain(p)) + '</h4>' : '<p>' + rdEsc(rdPlain(p)) + '</p>';
    }).join('');
    return { words: c.words, sentences: c.sentences, syllables: c.syllables };
  }
  (function () {
    var b = document.getElementById('txCount');
    var first = PRESETS[presetS.value];
    if (first && first.__passage) rdWrite(rdFill(first));
    b.addEventListener('click', function () {
      var text = rdClean(document.getElementById('txOwn').value);
      if (text === '') return;
      var c = rdCounts({ paragraphs: text.split(/\n\s*\n/) });
      if (!c.words || !c.sentences) { statusEl.textContent = 'That text has no complete sentence to count.'; return; }
      document.getElementById('txPassage').innerHTML = '';
      rdWrite(c);
    });
  })();
"""


def _text(cfg, view, kit):
    opts = {"_cfg_keys": ()}
    slots, main, ui, passages, extra, check = None, "", "", [], (), None
    if view == "readability":
        passages = rc.passages_of(cfg, kit)
        ids = {p["id"]: p for p in passages}
        fields = [F("words", "Words (body paragraphs)", "count", 1), F("sentences", "Sentences", "count", 1),
                  F("syllables", "Syllables, by the rule", "count", 1)]
        tiles = [("Words", "txWords"), ("Sentences", "txSentences"), ("Syllables", "txSyllables"),
                 ("Flesch Reading Ease", "txFre"), ("Flesch–Kincaid grade", "txGrade")]
        extra = ("passage",)

        def check(where, p, inst):
            given = [k for k in ("words", "sentences", "syllables") if k in p]
            if "passage" in p:
                if p["passage"] not in ids:
                    raise ValueError("%s: passage %r is not one the cfg gives (%s)" % (where, p["passage"], ", ".join(ids) or "none"))
                if given:
                    raise ValueError("%s: a preset names a passage or gives counts, not both" % where)
                c = rc.passage_counts(ids[p["passage"]])
                if not c["sentences"]:
                    raise ValueError("%s: passage %s has no sentence by the rule" % (where, p["passage"]))
                inst.update(words=str(c["body_words"]), sentences=str(c["sentences"]), syllables=str(c["syllables"]))
            elif len(given) != 3:
                raise ValueError("%s: a preset names a passage, or gives words, sentences and syllables" % where)
        opts["_cfg_keys"] = ("passage", "passages")
        main = ('      <div id="txPassage" class="prose card card-pad" style="margin-top:12px;max-height:22rem;overflow-y:auto;"></div>\n'
                '      <details style="margin-top:12px;"><summary class="small-copy">Count a text of your own</summary>\n'
                '        <textarea id="txOwn" rows="6" style="width:100%;box-sizing:border-box;" aria-label="Text to count"></textarea>\n'
                '        ' + rc.btn("txCount", "Count my text") + '</details>\n')
        ui = TEXT_READ_UI_JS
        title, intro = "Readability by formula", ("A count over a text: words, sentences and syllables by the kit's stated rule "
                                                  "(vowel groups, minus a final silent e, at least one a word), an approximation; "
                                                  "then Flesch's two formulas.")
    elif view == "coverage":
        (p,) = rc.passages_of(cfg, kit, 1)
        opts["_cfg_keys"] = ("passage", "kind", "timed", "questions")
        timed, qs = cfg.get("timed", False), cfg.get("questions", False)
        if not isinstance(timed, bool) or not isinstance(qs, bool):
            raise ValueError("%s: cfg[\"timed\"] and cfg[\"questions\"] are True or False" % kit)
        if qs and not p.get("questions"):
            raise ValueError("%s: passage %s has no questions to ask" % (kit, p["id"]))
        fields = [F("tokens", "Words in the text", "count", rc.word_count_passage(p)), F("unknown", "Words you do not know", "nncount")]
        tiles = [("Coverage", "txCoverage"), ("Unknown words", "txOneIn")]
        write = {"tokens": "tokens", "unknown": "unknown"}
        if timed:
            fields.append(F("seconds", "Seconds, reading and marking", "pos"))
            tiles.append(("Rate while marking", "txWpm"))
            write["seconds"] = "seconds"
        if qs:
            fields += [F("correct", "Questions right", "nncount"), F("total", "Questions asked", "nncount", len(p["questions"]))]
            tiles.append(("Comprehension", "txComp"))
            write.update(correct="correct", total="total")
        slots = {"": rc.slot("", p, intro="Press Start, then mark every word you do not know (click it, or Tab to it and press "
                             "Enter). Press Count my marks when you reach the end. "
                             + ("The clock runs from Start to Count my marks, so read as you mark. " if timed else "Nothing is timed. ")
                             + ("Then the passage's questions, with the passage hidden." if qs else ""),
                             kind=rc.log_kind(kit, cfg.get("kind"), "other"), mode="text", view="coverage", flow="coverage",
                             questions=qs, write=write)}
        slots[""]["timed"] = timed
        main = rc.slot_html("", "Mark the unknown words: " + p["title"], slots[""]["intro"])
        passages = [p]
        title, intro = "Vocabulary coverage", "Your measurement: coverage = known words / all words, counted by the kit's word rule."
    elif view == "volume":
        fields = [F("minutes", "Minutes of reading a day", "nn"), F("wpm", "Rate, wpm", "pos"), F("days", "Days a year", "nn", 365),
                  F("bookWords", "Words in a book", "pos", 90000)]
        tiles = [("Words a year", "txWordsYear"), ("Books a year", "txBooksYear")]
        title, intro = "How much you read", "A stated model: words a year = minutes a day × rate × days."
    else:
        raise ValueError("%s: unknown view %r" % (kit, view))
    return rc.build_lab(cfg, kit=kit, prefix="tx", view=view, fields=fields, tiles=tiles, fn="txCompute", js=TEXT_JS, opts=opts,
                        title=title, subtitle="counted by a stated rule", panel_title="The counts and the formulas",
                        panel_intro=intro, main_html=main, passages=passages, slots=slots, ui_js=ui, extra_keys=extra,
                        check=check, needs_text=True)


# ---------------------------------------------------------------------------
# recall
# ---------------------------------------------------------------------------

RECALL_JS = r"""
  /* recall: the reader ticks the idea units; the kit never scores a free recall. */
  function reCompute(view, inst) {
    var t = {};
    if (view === 'free') {
      if (Rcmp(inst.recalled, inst.units) > 0) return { refuse: 'More idea units ticked than the passage has' };
      var share = Rdiv(inst.recalled, inst.units), wpm = rdRate(inst.words, inst.seconds);
      t.reRecall = rdShare(share);
      t.reRate = rdUnit(Rmul(wpm, share), 'wpm');
      t.reWordsPerUnit = Rzero(inst.recalled) ? 'no units recalled' : rdUnit(Rdiv(inst.summaryWords, inst.recalled), 'words');
      if (inst.total !== undefined) {
        if (Rcmp(inst.correct, inst.total) > 0) return { refuse: 'More questions right than asked' };
        t.reComp = Rzero(inst.total) ? 'no questions' : rdShare(Rdiv(inst.correct, inst.total));
      }
      return { tiles: t, status: rdFig(inst.recalled) + ' of ' + rdFig(inst.units) + ' idea units: ' + t.reRecall + '. Rate ' + rdUnit(wpm, 'wpm')
        + ' × ' + Rtext(share) + ' = ' + t.reRate + ' of recalled reading; ' + rdFig(inst.summaryWords) + ' words written.'
        + (t.reComp ? ' The questions afterwards: ' + t.reComp + '.' : '') };
    }
    if (view === 'delayed') {
      if (Rcmp(inst.delA, inst.total) > 0 || Rcmp(inst.delB, inst.total) > 0) return { refuse: 'More right than asked on the delayed test' };
      if (Rcmp(inst.recalled, inst.units) > 0) return { refuse: 'More idea units ticked than the passage has' };
      var ka = Rdiv(inst.delA, inst.total), kb = Rdiv(inst.delB, inst.total);
      t.reDelayedA = rdShare(ka);
      t.reDelayedB = rdShare(kb);
      t.reDelayedDiff = rdSigned(Rmul(Rsub(kb, ka), R(100n)), 'points');
      t.reRecallB = rdShare(Rdiv(inst.recalled, inst.units));
      return { tiles: t, status: 'On the delayed test the passage read twice scored ' + t.reDelayedA + ' and the passage read once and recalled '
        + t.reDelayedB + ', a difference of ' + t.reDelayedDiff + '; at the time, its free recall held ' + t.reRecallB + ' of its idea units.'
        + (Rcmp(inst.total, R(6n)) <= 0 ? ' With ' + rdFig(inst.total) + ' questions a side, one question is ' + rdFig(Rdiv(R(100n), inst.total)).replace('≈ ', '≈ ') + ' points; a one-question difference is not a result.' : '') };
    }
    if (Rcmp(inst.reviews, R(12n)) > 0) return { refuse: 'This lab plans at most 12 reviews' };
    var days = [], day = R0, n = Number(inst.reviews.n);
    for (var k = 0; k < n; k++) { day = Radd(day, Rmul(inst.first, Rpow(inst.mult, k))); days.push(day); }
    t.reDays = days.map(rdFig).join(', ');
    t.reLastDay = 'day ' + rdFig(day);
    t.reMinutes = rdUnit(Rmul(inst.reviews, inst.minutes), 'min');
    return { tiles: t, status: 'Gaps of ' + rdFig(inst.first) + ' day' + (Requ(inst.first, R1) ? '' : 's') + ' multiplied by ' + rdFig(inst.mult)
      + ' each time put the reviews on days ' + t.reDays + ', ' + t.reMinutes + ' in all.' };
  }
"""

DELAYED_UI_JS = r"""
  /* The delayed test: offered when both conditions are logged for this lesson
     and their due date has passed. The questions of both passages, no passage shown. */
  function reDelayedShow() {
    var box = document.getElementById('reDelayed');
    function lessonId() { return LESSON || String((window.location && window.location.pathname) || '').split('/').filter(Boolean).pop() || ''; }
    var here = lessonId(), list = rdLogRead(), mine = list.filter(function (e) { return e.lesson === here && e.view === 'delayed'; });
    var a = mine.filter(function (e) { return e.side === 'A'; }).pop(), b = mine.filter(function (e) { return e.side === 'B'; }).pop();
    if (!a || !b) return;
    var done = list.some(function (e) { return e.view === 'delayed-test' && e.lesson === here && e.at > a.at && e.at > b.at; });
    if (done) return;
    var due = Date.parse(a.due) > Date.parse(b.due) ? a.due : b.due;
    box.style.display = '';
    if (Date.parse(due) > Date.now()) { box.textContent = 'Both conditions are logged. The delayed test is due on ' + due.slice(0, 10) + '.'; return; }
    box.innerHTML = 'Your delayed test is due. ' + '<button class="btn small primary" type="button">Take the delayed test</button><div style="margin-top:8px;"></div>';
    box.getElementsByTagName('button')[0].addEventListener('click', function () {
      var work = box.getElementsByTagName('div')[0], qa = PASSAGES[RE_A].questions, qb = PASSAGES[RE_B].questions;
      rdAsk(work, qa.concat(qb), function (answers) {
        var ta = rdTally(qa, answers.slice(0, qa.length)), tb = rdTally(qb, answers.slice(qa.length));
        var v = { delA: ta.correct, delB: tb.correct, total: qa.length };
        /* B's recall at the time, from its log entry, so every box is the reader's own. */
        if (b.extra && b.extra.units > 0) { v.units = b.extra.units; v.recalled = b.extra.recalled; }
        rdWrite(v);
        rdLogAppend({ mode: 'recall', view: 'delayed-test', side: '', passage: RE_A + '+' + RE_B, display: 'none', words: 0, ms: 0,
                      correct: ta.correct + tb.correct, total: qa.length + qb.length, kind: a.kind,
                      extra: { delA: ta.correct, delB: tb.correct } }, box);
        work.innerHTML = rdReview(qa.concat(qb), answers);
      });
    });
  }
  /* At load, and after each side is logged, so "due on" shows without a reload. */
  function rdAfterScore() { reDelayedShow(); }
  reDelayedShow();
"""


def _recall(cfg, view, kit):
    opts = {"_cfg_keys": ()}
    slots, main, ui, passages = None, "", "", []
    if view == "free":
        (p,) = rc.passages_of(cfg, kit, 1, need=("ideas",))
        summary = cfg.get("summary", False)
        if not isinstance(summary, bool):
            raise ValueError("%s: cfg[\"summary\"] is True or False" % kit)
        qs = cfg.get("questions", False)
        if not isinstance(qs, bool) or (qs and not p.get("questions")):
            raise ValueError("%s: cfg[\"questions\"] is True or False, and True needs a passage with questions" % kit)
        opts["_cfg_keys"] = ("passage", "summary", "kind", "questions")
        fields = [F("units", "Idea units in the passage", "count", len(p["ideas"])), F("recalled", "Idea units you ticked", "nncount"),
                  F("words", "Words read", "count", rc.word_count_passage(p)), F("seconds", "Seconds reading", "pos"),
                  F("summaryWords", "Words you wrote", "nncount", 0)]
        tiles = [("Idea units recalled", "reRecall"), ("Rate × recall", "reRate"), ("Words written per unit recalled", "reWordsPerUnit")]
        if qs:
            fields += [F("correct", "Questions right, after the recall", "nncount"),
                       F("total", "Questions asked", "nncount", len(p["questions"]))]
            tiles.append(("Questions right, after the recall", "reComp"))
        slots = {"": rc.slot("", p, intro=("Read at your usual pace and press Done. Then " + ("write a three-sentence summary"
                             if summary else "write everything you remember") + " with the passage hidden, and tick the idea "
                             "units your writing contains. You are the judge; the kit does not score your writing."
                             + (" Then the passage's questions, one at a time." if qs else "")),
                             kind=rc.log_kind(kit, cfg.get("kind"), "condition"), mode="recall", view="free", flow="recall",
                             summary=summary, questions=qs,
                             write=dict({"units": "units", "recalled": "recalled", "words": "words", "seconds": "seconds",
                                         "summaryWords": "summaryWords"}, **({"correct": "correct", "total": "total"} if qs else {})))}
        main = rc.slot_html("", "Read, then recall: " + p["title"], slots[""]["intro"])
        passages = [p]
        title = "Free recall" if not summary else "A summary in your own words"
    elif view == "delayed":
        pa, pb = rc.passages_of(cfg, kit, 2, need=("questions",))
        if not pb.get("ideas"):
            raise ValueError("%s: passage %s (the retrieve condition) needs its idea units" % (kit, pb["id"]))
        if len(pa["questions"]) != len(pb["questions"]):
            raise ValueError("%s: the two passages must carry the same number of questions" % kit)
        days = int(rc.num(kit, cfg, "days", 2, lo=1, hi=60, whole=True))
        kind = rc.log_kind(kit, cfg.get("kind"), "condition")
        opts["_cfg_keys"] = ("passages", "days", "kind")
        fields = [F("delA", "Right on the delayed test, read twice", "nncount"), F("delB", "Right on the delayed test, recalled", "nncount"),
                  F("total", "Questions on each delayed test", "count", len(pa["questions"])),
                  F("units", "Idea units (recalled passage)", "count", len(pb["ideas"])),
                  F("recalled", "Idea units ticked at the time", "nncount")]
        tiles = [("Delayed score, read twice", "reDelayedA"), ("Delayed score, read once and recalled", "reDelayedB"),
                 ("Recalled minus read twice", "reDelayedDiff"), ("Recall at the time (recalled passage)", "reRecallB")]
        slots = {"A": rc.slot("A", pa, intro="Condition 1: read this passage twice through. There is no test now.", kind=kind,
                              mode="recall", view="delayed", flow="reread", questions=False, days=days),
                 "B": rc.slot("B", pb, intro="Condition 2: read this passage once, then write what you remember and tick the "
                              "idea units.", kind=kind, mode="recall", view="delayed", flow="recall", days=days, questions=False,
                              write={"units": "units", "recalled": "recalled"})}
        main = ('      <div class="status-banner" id="reDelayed" style="display:none;margin-top:12px;"></div>\n'
                + rc.slot_html("A", "Read twice: " + pa["title"], slots["A"]["intro"])
                + rc.slot_html("B", "Read once, then recall: " + pb["title"], slots["B"]["intro"]))
        ui = "  var RE_A = %s, RE_B = %s;\n" % (rc.json.dumps(pa["id"]), rc.json.dumps(pb["id"])) + DELAYED_UI_JS
        passages = [pa, pb]
        title = "Retrieval against rereading"
    elif view == "schedule":
        fields = [F("first", "First gap, days", "pos", 1), F("mult", "Each gap is the last one times", "nn", 2),
                  F("reviews", "Reviews", "count", 5), F("minutes", "Minutes per review", "nn", 10)]
        tiles = [("Review days", "reDays"), ("Last review", "reLastDay"), ("Minutes in all", "reMinutes")]
        title = "A review schedule"
    else:
        raise ValueError("%s: unknown view %r" % (kit, view))
    return rc.build_lab(cfg, kit=kit, prefix="re", view=view, fields=fields, tiles=tiles, fn="reCompute", js=RECALL_JS,
                        opts=opts, title=title, subtitle="what is kept, measured by you",
                        panel_title="What you kept, in numbers",
                        panel_intro=("Your measurement where there is a drill, scored by your own ticks; a stated schedule "
                                     "otherwise. Before a drill, the boxes hold a worked example."),
                        main_html=main, passages=passages, slots=slots, ui_js=ui)


# ---------------------------------------------------------------------------
# log
# ---------------------------------------------------------------------------

LOG_JS = r"""
  /* log: the reader's numbers. History, noise and profile use readings
     logged as "baseline" or "test" only, of standard text (rdStandard). */
  /* n: the number of baseline readings the range comes from. */
  function lgRangeVerdict(x, lo, hi, n) {
    if (Rcmp(x, hi) > 0) return rdOnce(n);
    if (Rcmp(x, lo) < 0) return 'below the baseline range';
    return 'inside the baseline range';
  }
  function lgMinMax(v) { var s = v.slice().sort(Rcmp); return { lo: s[0], hi: s[s.length - 1] }; }
  function lgErr(e) { return Rmul(e.wpm, Rdiv(e.correct, e.total)); }
  /* The three tiers (PLAN D.3.3): with three tests or more, the median of the
     last three against the range of n baselines; else (or when that median is
     inside) the latest test, which above the range is "once". */
  function lgTiers(tests, lo, hi, n) {
    var last = tests[tests.length - 1];
    if (tests.length >= 3) {
      var med = rdMedian(tests.slice(-3));
      if (Rcmp(med, hi) > 0) return 'above the baseline range on the median of the last three tests';
      if (Rcmp(med, lo) < 0) return 'below the baseline range on the median of the last three tests';
      return Rcmp(last, hi) > 0 ? rdOnce(n) : 'inside the baseline range';
    }
    return lgRangeVerdict(last, lo, hi, n);
  }
  /* History: the first nb sessions are the baselines (all of them, three at
     least), the rest tests. */
  function lgHistoryVerdict(errs, nb) {
    if (nb < 3) return rdNeedBase(nb);
    if (errs.length <= nb) return 'needs a reading after the ' + (RD_NW[nb] || nb) + ' baselines';
    var base = lgMinMax(errs.slice(0, nb));
    return lgTiers(errs.slice(nb), base.lo, base.hi, nb);
  }
  /* The chart: baseline and test sessions as the line; practice sessions,
     when given, as a lighter dashed series spread over the same width. */
  function lgChart(errs, practice) {
    var W = 320, H = 120, P = 24, max = R1;
    errs.concat(practice).forEach(function (e) { if (Rcmp(e, max) > 0) max = e; });
    var mx = Rnum(max);
    function pts(v) {
      var n = v.length;
      return v.map(function (e, i) {
        var x = P + (n === 1 ? 0 : i * (W - 2 * P) / (n - 1)), y = H - P - Rnum(e) / mx * (H - 2 * P);
        return x.toFixed(1) + ',' + y.toFixed(1);
      });
    }
    var a = pts(errs), b = pts(practice);
    return '<svg viewBox="0 0 ' + W + ' ' + H + '" width="100%" role="img" aria-label="Effective rate by session" style="max-width:32rem;display:block;">'
      + '<line x1="' + P + '" y1="' + (H - P) + '" x2="' + (W - P) + '" y2="' + (H - P) + '" stroke="currentColor" stroke-opacity="0.3"/>'
      + (b.length ? '<polyline fill="none" stroke="currentColor" stroke-opacity="0.35" stroke-dasharray="4 3" stroke-width="1.5" points="' + b.join(' ') + '"/>'
        + b.map(function (p) { var c = p.split(','); return '<circle cx="' + c[0] + '" cy="' + c[1] + '" r="2" fill="currentColor" fill-opacity="0.35"/>'; }).join('') : '')
      + (a.length ? '<polyline fill="none" stroke="var(--cyan)" stroke-width="2" points="' + a.join(' ') + '"/>'
        + a.map(function (p) { var c = p.split(','); return '<circle cx="' + c[0] + '" cy="' + c[1] + '" r="3" fill="var(--cyan)"/>'; }).join('') : '')
      + '<text x="' + P + '" y="14" font-size="11" fill="currentColor">effective rate, wpm: baselines and tests'
      + (b.length ? '; practice lighter' : '') + '</text></svg>';
  }
  function lgNearestOf(wpm, gears) {
    var top = gears[0], best = null;
    gears.forEach(function (g) { if (Rcmp(g.wpm, top.wpm) > 0) top = g; });
    if (Rcmp(wpm, top.wpm) > 0) return null;
    gears.forEach(function (g) {
      if (best === null) { best = g; return; }
      var d = Rcmp(Rabs(Rsub(wpm, g.wpm)), Rabs(Rsub(wpm, best.wpm)));
      if (d < 0 || (d === 0 && Rcmp(g.wpm, best.wpm) < 0)) best = g;
    });
    return best;
  }
  function lgCompute(view, inst, opts) {
    var t = {};
    if (view === 'noise') {
      var mm = lgMinMax(inst.base), range = Rsub(mm.hi, mm.lo), mean = Rdiv(rdSum(inst.base), R(BigInt(inst.base.length)));
      var later = inst.tests[inst.tests.length - 1], recent = inst.tests.slice(-3);
      t.lgMean = rdUnit(mean, 'wpm'); t.lgRange = rdUnit(range, 'wpm');
      t.lgTestMedian = rdUnit(rdMedian(recent), 'wpm') + (recent.length < 3 ? ' (of ' + recent.length + ')' : '');
      t.lgVerdict = lgTiers(inst.tests, mm.lo, mm.hi, inst.base.length);
      var off = Rcmp(later, mm.hi) > 0 ? Rsub(later, mm.hi) : (Rcmp(later, mm.lo) < 0 ? Rsub(mm.lo, later) : null);
      t.lgBeyond = off === null ? 'inside' : rdUnit(off, 'wpm') + (Rcmp(later, mm.hi) > 0 ? ' above the top' : ' below the bottom')
        + (Rzero(range) ? '' : ' (' + rdFig(Rdiv(off, range)) + ' ranges)');
      return { tiles: t, status: inst.base.length + ' baseline rates from ' + rdUnit(mm.lo, 'wpm') + ' to ' + rdUnit(mm.hi, 'wpm')
        + ': a spread of ' + t.lgRange + ' with nothing changed. ' + inst.tests.length + ' test reading' + (inst.tests.length === 1 ? '' : 's')
        + ', the latest ' + rdUnit(later, 'wpm') + ': ' + t.lgVerdict + '.' };
    }
    if (view === 'gears') {
      /* The gears are in standard-length words, the average in words (D.3.15). */
      var std = (inst.stdwpm === undefined || inst.stdwpm === null) ? null : inst.stdwpm, gw = std || inst.wpm;
      var g = lgNearestOf(gw, opts.gears.map(function (x) { return { name: x.name, wpm: Rparse(x.wpm) }; }));
      t.lgNearest = g ? g.name + ', ' + rdUnit(g.wpm, 'standard wpm') : 'above every gear';
      t.lgVsAverage = rdShare(Rdiv(inst.wpm, Rparse(opts.average)));
      return { tiles: t, status: rdUnit(inst.wpm, 'wpm') + ' is ' + t.lgVsAverage + ' of the ' + opts.average + ' wpm average for silent reading of '
        + 'nonfiction (Brysbaert 2019, in words); the nearest of Carver\'s gears (in standard-length words) to '
        + (std ? rdUnit(std, 'standard wpm') : rdUnit(inst.wpm, 'wpm') + ' (no standard-word rate given, so the rate in words stands in)')
        + ' is ' + t.lgNearest + '.' };
    }
    if (view === 'history') {
      var errs = inst.entries.map(lgErr), n = errs.length, nb = Number(inst.baseN.n), out;
      if (nb > n) return { refuse: 'There are ' + n + ' sessions, so ' + nb + ' of them cannot be baselines' };
      t.lgSessions = String(n);
      t.lgBaseMedian = nb ? rdUnit(rdMedian(errs.slice(0, nb)), 'wpm') : 'no baselines';
      t.lgRecentMedian = n - nb >= 3 ? rdUnit(rdMedian(errs.slice(-3)), 'wpm') : 'after ' + (Math.max(nb, 3) + 3) + ' sessions';
      t.lgLatestErr = n ? rdUnit(errs[n - 1], 'wpm') : 'no sessions';
      t.lgVerdict = lgHistoryVerdict(errs, nb);
      out = { tiles: t, status: n + ' sessions with questions, the first ' + nb + ' of them baselines. Baseline median ' + t.lgBaseMedian
        + '; recent median (last three tests) ' + t.lgRecentMedian + '; ' + t.lgVerdict + '.' };
      var prac = (inst.practice || []).map(lgErr);
      if (n || prac.length) {
        out.svg = lgChart(errs, prac);
      }
      if (n) {
        out.table = { caption: 'Sessions (baseline and test readings)', head: ['session', 'rate', 'right', 'effective rate'],
          rows: inst.entries.map(function (e, i) { return [String(i + 1), rdUnit(e.wpm, 'wpm'), rdFig(e.correct) + ' of ' + rdFig(e.total), rdUnit(errs[i], 'wpm')]; }) };
      }
      return out;
    }
    if (view === 'plan') {
      var mins = R0, test = R0, found = false;
      inst.rows.forEach(function (r) { var m = Rmul(r.sessions, r.minutes); mins = Radd(mins, m); if (r.drill === inst.test) { test = Radd(test, m); found = true; } });
      if (Rzero(mins)) return { refuse: 'The plan has no minutes in it' };
      t.lgWeekMinutes = rdUnit(mins, 'min');
      t.lgTestShare = found ? rdShare(Rdiv(test, mins)) : 'no test in the week';
      var spare = Rsub(inst.budget, mins);
      t.lgFits = Rsign(spare) >= 0 ? 'fits, ' + rdUnit(spare, 'min') + ' to spare' : 'over the budget by ' + rdUnit(Rneg(spare), 'min');
      return { tiles: t, status: 'The week is ' + t.lgWeekMinutes + '; the test reading ("' + inst.test + '") is ' + t.lgTestShare + ' of it.',
        table: { caption: 'The week', head: ['drill', 'sessions', 'minutes each', 'minutes'],
          rows: inst.rows.map(function (r) { return [r.drill, rdFig(r.sessions), rdFig(r.minutes), rdFig(Rmul(r.sessions, r.minutes))]; }) } };
    }
    /* profile */
    var lo = inst.baseLo, hi = inst.baseHi;
    if ((lo === null) !== (hi === null)) return { refuse: 'Give both ends of the baseline range, or neither' };
    if (lo !== null && Rcmp(lo, hi) > 0) return { refuse: 'The baseline range runs from the lower rate to the higher one' };
    t.lgErrThen = rdUnit(inst.errThen, 'wpm'); t.lgErrNow = rdUnit(inst.errNow, 'wpm');
    var nb = Number(inst.baseN.n);
    /* With the recent tests given, the tier rule on them; else the one reading now. */
    t.lgVerdict = lo === null ? 'no baseline range given' : nb < 3 ? rdNeedBase(nb)
      : inst.tests.length ? lgTiers(inst.tests, lo, hi, nb) : lgRangeVerdict(inst.errNow, lo, hi, nb);
    t.lgGist = rdShare(inst.gistThen) + ' → ' + rdShare(inst.gistNow);
    t.lgScan = rdUnit(inst.scanThen, 's') + ' → ' + rdUnit(inst.scanNow, 's');
    t.lgRecall = rdShare(inst.recallThen) + ' → ' + rdShare(inst.recallNow);
    return { tiles: t, status: 'Effective rate ' + t.lgErrThen + ' then, ' + t.lgErrNow + ' now: ' + t.lgVerdict + '. A reader is a profile, not one number.' };
  }
"""

LOG_FILL_JS = r"""
  /* Reading the log (at load, and on the buttons). Only "baseline" and "test"
     readings of standard text with questions count; every other entry is listed, greyed. */
  function lgCounted(e) { return (e.kind === 'baseline' || e.kind === 'test') && e.total > 0 && rdIsReading(e) && rdStandard(e); }
  function lgRate(e) { return rdEntryRate(e, false); }
  function lgLogTable(list) {
    var el = document.getElementById('lgLog');
    if (!el) return;
    if (!list.length) { el.innerHTML = '<p class="small-copy">Your log is empty: the boxes hold an example log. Do a drill and it appears here.</p>'; return; }
    el.innerHTML = '<div class="table-wrap"><table class="tt"><caption>Your log (only baseline and test readings of standard passages, with questions, are counted)</caption>'
      + '<thead><tr><th>date</th><th>lesson</th><th>kind</th><th>what</th><th>rate</th><th>right</th></tr></thead><tbody>'
      + list.map(function (e) {
        var rate = e.words > 0 && e.ms > 0 ? rdUnit(lgRate(e), 'wpm') : '';
        return '<tr' + (lgCounted(e) ? '' : ' style="opacity:0.55"') + '><td>' + rdEsc(String(e.at || '').slice(0, 10)) + '</td><td>'
          + rdEsc(e.lesson || '') + '</td><td>' + rdEsc(e.kind || '') + '</td><td>' + rdEsc((e.view || '') + (e.view === 'note' && e.extra ? ': ' + e.extra.text : '') + (rdStandard(e) ? '' : ', ' + e.band + ' passage'))
          + '</td><td>' + rate + '</td><td>' + (e.total ? e.correct + ' of ' + e.total : '') + '</td></tr>';
      }).join('') + '</tbody></table></div>';
  }
  /* rate/right/asked, the rate a decimal of at most two places ("251.07/5/6"). */
  function lgEntriesText(list) {
    return list.map(function (e) { return rdDec(lgRate(e)) + '/' + e.correct + '/' + e.total; }).join(', ');
  }
"""

LOG_HISTORY_UI_JS = r"""
  var lgAfter = null;
  function rdAfterScore() { if (lgAfter) lgAfter(); }
  (function () {
    var list = rdLogRead(), msg = document.getElementById('lgMsg');
    lgLogTable(list);
    /* Every baseline first (all of them), then the tests, oldest first; practice apart. */
    function mine(l) {
      var c = l.filter(lgCounted), b = c.filter(function (e) { return e.kind === 'baseline'; }).slice(0, 200);
      var t = c.filter(function (e) { return e.kind === 'test'; }), p = l.filter(function (e) { return e.kind === 'practice' && e.total > 0 && rdIsReading(e); });
      return c.length ? { entries: lgEntriesText(b.concat(t.slice(Math.max(0, t.length - 200 + b.length)))), baseN: b.length,
                          practice: lgEntriesText(p.slice(-200)) } : null;
    }
    if (mine(list)) { rdWrite(mine(list)); msg.textContent = 'The boxes hold your own log.'; }
    function fill(quiet) {
      var l = rdLogRead(), v = mine(l);
      lgLogTable(l);
      if (!v) { if (!quiet) msg.textContent = 'Your log has no baseline or test readings with questions yet.'; return; }
      rdWrite(v); msg.textContent = 'The boxes hold your own log.';
    }
    document.getElementById('lgMine').addEventListener('click', function () { fill(false); });
    /* A warm-up scored on this page is in the log at once: read it again. */
    lgAfter = function () { fill(true); };
    document.getElementById('lgNoteAdd').addEventListener('click', function () {
      var box = document.getElementById('lgNote'), text = rdClean(box.value);
      if (text === '') return;
      rdLogAppend({ mode: 'log', view: 'note', side: '', passage: '', display: '', words: 0, ms: 0, correct: 0, total: 0, kind: 'other',
                    extra: { text: text.slice(0, 500) } }, msg);
      box.value = ''; lgLogTable(rdLogRead()); msg.textContent = 'Note added.';
    });
    document.getElementById('lgExport').addEventListener('click', function () {
      var out = document.getElementById('lgCsv'), head = ['at', 'lesson', 'kind', 'mode', 'view', 'passage', 'display', 'words', 'ms', 'correct', 'total', 'note'];
      out.value = head.join(',') + '\n' + rdLogRead().map(function (e) {
        return [e.at, e.lesson, e.kind, e.mode, e.view, e.passage, e.display, e.words, e.ms, e.correct, e.total,
                e.extra && e.extra.text ? e.extra.text : ''].map(function (v) {
          var s = v === undefined || v === null ? '' : String(v);
          return /[",\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s;
        }).join(',');
      }).join('\n');
      out.style.display = '';
    });
    var ask = document.getElementById('lgClearAsk'), yes = document.getElementById('lgClearYes'), no = document.getElementById('lgClearNo');
    ask.addEventListener('click', function () { yes.style.display = ''; no.style.display = ''; msg.textContent = 'Clear every entry of your reading log? This cannot be undone.'; });
    no.addEventListener('click', function () { yes.style.display = 'none'; no.style.display = 'none'; msg.textContent = 'Kept.'; });
    yes.addEventListener('click', function () {
      try { window.localStorage.removeItem(RD_LOG_KEY); } catch (err) { /* nothing to clear */ }
      yes.style.display = 'none'; no.style.display = 'none'; lgLogTable([]); msg.textContent = 'Your log is cleared.';
    });
  })();
"""

LOG_NOISE_UI_JS = r"""
  (function () {
    var msg = document.getElementById('lgMsg');
    document.getElementById('lgMine').addEventListener('click', function () {
      var c = rdLogRead().filter(lgCounted), base = c.filter(function (e) { return e.kind === 'baseline'; }).slice(-20);
      var tests = c.filter(function (e) { return e.kind === 'test'; });
      if (base.length < 2) { msg.textContent = 'Your log needs at least two baseline readings with questions.'; return; }
      var v = { base: base.map(function (e) { return rdDec(lgRate(e)); }).join(', ') };
      if (tests.length) v.tests = tests.slice(-20).map(function (e) { return rdDec(lgRate(e)); }).join(', ');
      rdWrite(v);
      msg.textContent = 'Your baselines' + (tests.length ? ' and your test readings.' : '; type a test rate to compare.');
    });
  })();
"""

LOG_GEARS_UI_JS = r"""
  (function () {
    var msg = document.getElementById('lgMsg');
    document.getElementById('lgMine').addEventListener('click', function () {
      var base = rdLogRead().filter(function (e) { return e.kind === 'baseline' && rdIsReading(e) && rdStandard(e); });
      if (!base.length) { msg.textContent = 'Your log has no baseline readings yet.'; return; }
      var v = { wpm: rdDec(rdMedian(base.map(lgRate))), stdwpm: '' };
      if (base.every(function (e) { return e.chars > 0; })) v.stdwpm = rdDec(rdMedian(base.map(function (e) {
        return R(BigInt(Math.round(e.chars)) * 10000n, BigInt(Math.round(e.ms)));
      })));
      rdWrite(v);
      msg.textContent = 'The median of your ' + base.length + ' baseline reading' + (base.length === 1 ? '' : 's') + '.';
    });
  })();
"""

LOG_PLAN_UI_JS = r"""
  (function () {
    var msg = document.getElementById('lgMsg');
    document.getElementById('lgMine').addEventListener('click', function () {
      var rows = SPEC.filter(function (s) { return s.key === 'rows'; })[0];
      rdLogAppend({ mode: 'log', view: 'plan', side: '', passage: '', display: '', words: 0, ms: 0, correct: 0, total: 0, kind: 'other',
                    extra: { text: field(rows.id).value } }, msg);
      msg.textContent = 'This week\'s plan is in your log.';
    });
  })();
"""

LOG_PROFILE_UI_JS = r"""
  (function () {
    var msg = document.getElementById('lgMsg');
    document.getElementById('lgMine').addEventListener('click', function () {
      var c = rdLogRead().filter(function (e) { return e.kind === 'baseline' || e.kind === 'test'; }), v = {};
      /* Readings (drills and warm-ups, not skims) with questions, as effective rates: every baseline, every test. */
      var base = rdKindRates('baseline', true, c), tests = rdKindRates('test', true, c);
      if (base.length) { var mm = lgMinMax(base); v.errThen = rdDec(rdMedian(base)); v.baseLo = rdDec(mm.lo); v.baseHi = rdDec(mm.hi); v.baseN = base.length; }
      if (tests.length) { v.errNow = rdDec(tests[tests.length - 1]); v.tests = tests.slice(-20).map(rdDec).join(', '); }
      function ends(list, f) { if (list.length) { return [f(list[0]), f(list[list.length - 1])]; } return null; }
      var g = ends(c.filter(function (e) { return e.display === 'gist' && e.extra && e.extra.gistTotal > 0; }), function (e) { return e.extra.gist + '/' + e.extra.gistTotal; });
      if (g) { v.gistThen = g[0]; v.gistNow = g[1]; }
      var s = ends(c.filter(function (e) { return e.mode === 'scan' && e.view === 'find' && e.correct > 0 && e.ms > 0; }), function (e) { return Rtext(R(BigInt(Math.round(e.ms)), BigInt(e.correct) * 1000n)); });
      if (s) { v.scanThen = s[0]; v.scanNow = s[1]; }
      var r = ends(c.filter(function (e) { return e.mode === 'recall' && e.view === 'free' && e.extra && e.extra.units > 0 && !e.extra.summary; }), function (e) { return e.extra.recalled + '/' + e.extra.units; });
      if (r) { v.recallThen = r[0]; v.recallNow = r[1]; }
      if (!Object.keys(v).length) { msg.textContent = 'Your log has no baseline or test readings yet.'; return; }
      rdWrite(v);
      msg.textContent = 'Filled from your baseline and test readings; boxes your log cannot fill keep the example.';
    });
  })();
"""

DEFAULT_GEARS = [("scanning", 600), ("skimming", 450), ("rauding", 300), ("learning", 200), ("memorising", 138)]


def _log_controls(button, extra=""):
    return ('      <div class="card card-pad" style="margin-top:12px;">\n'
            '        <p class="small-copy" id="lgMsg" aria-live="polite" style="margin:0 0 8px;">The boxes hold a worked example.</p>\n'
            '        ' + rc.btn("lgMine", button) + '\n' + extra + '      </div>\n')


def _log(cfg, view, kit):
    opts = {"_cfg_keys": ()}
    ui = LOG_FILL_JS
    if view == "noise":
        fields = [F("base", "Baseline rates, wpm, separated by commas", ("nums", "pos", 2, 20)),
                  F("tests", "Test rates, wpm, oldest first, separated by commas", ("nums", "pos", 1, 20))]
        tiles = [("Baseline mean", "lgMean"), ("Baseline range", "lgRange"), ("Median of the last three tests", "lgTestMedian"),
                 ("Verdict", "lgVerdict"), ("Latest test, how far outside", "lgBeyond")]
        main = _log_controls("Use my baselines")
        ui += LOG_NOISE_UI_JS
        title = "How much one reading varies"
    elif view == "gears":
        gears = cfg.get("gears", DEFAULT_GEARS)
        if not isinstance(gears, list) or not 1 <= len(gears) <= 8:
            raise ValueError("%s: cfg[\"gears\"] is a list of (name, wpm) pairs" % kit)
        gl = []
        for g in gears:
            if not (isinstance(g, (list, tuple)) and len(g) == 2 and isinstance(g[0], str) and g[0].strip()):
                raise ValueError("%s: each gear is (name, wpm), not %r" % (kit, g))
            gl.append({"name": g[0], "wpm": rc.ftext(rc.num(kit, {"g": g[1]}, "g", None, lo=1))})
        avg = rc.num(kit, cfg, "average", 238, lo=1)
        opts.update(gears=gl, average=rc.ftext(avg), _cfg_keys=("gears", "average"))
        fields = [F("wpm", "A reading rate, wpm (words)", "pos"),
                  F("stdwpm", "The same reading in standard words (6 characters) a minute; empty if not known", "opt", "")]
        tiles = [("Nearest gear", "lgNearest"), ("Against the average of %s wpm" % rc.ftext(avg), "lgVsAverage")]
        main = _log_controls("Use my baseline median")
        ui += LOG_GEARS_UI_JS
        title = "Typical rates and reading gears"
    elif view == "history":
        fields = [F("entries", "Sessions: rate/right/asked, baselines first, then tests, oldest first", ("entries", 0, 200)),
                  F("baseN", "How many of the sessions are baselines (the first ones)", "nncount", 3),
                  F("practice", "Practice readings (drawn lighter): rate/right/asked", ("entries", 0, 200), [])]
        tiles = [("Sessions", "lgSessions"), ("Baseline median", "lgBaseMedian"),
                 ("Recent median (last three tests)", "lgRecentMedian"), ("Latest effective rate", "lgLatestErr"), ("Verdict", "lgVerdict")]
        main = _log_controls("Show my log", (
            '        ' + rc.btn("lgExport", "Export as text") + ' ' + rc.btn("lgClearAsk", "Clear my log") + ' '
            + rc.btn("lgClearYes", "Yes, clear it", hidden=True) + ' ' + rc.btn("lgClearNo", "Keep it", hidden=True) + '\n'
            '        <textarea id="lgCsv" readonly rows="6" style="display:none;width:100%;box-sizing:border-box;margin-top:8px;" aria-label="Your log as CSV text"></textarea>\n'
            '        <div style="margin-top:8px;"><textarea id="lgNote" rows="2" style="width:100%;box-sizing:border-box;" aria-label="A note for your log"></textarea> '
            + rc.btn("lgNoteAdd", "Add note") + '</div>\n'
            '        <div id="lgLog" style="margin-top:8px;"></div>\n'))
        ui += LOG_HISTORY_UI_JS
        title = "Your practice log"
    elif view == "plan":
        fields = [F("rows", "The week: drill, sessions, minutes each; separated by ;",
                    ("rec", [("drill", "name"), ("sessions", "nncount"), ("minutes", "nn")], 1, 10, False)),
                  F("test", "The drill that is the test reading", "name", "test reading"),
                  F("budget", "Minutes you have in the week", "pos")]
        tiles = [("Minutes in the week", "lgWeekMinutes"), ("Share that is the test", "lgTestShare"), ("Against your time", "lgFits")]
        main = _log_controls("Save this plan to my log")
        ui += LOG_PLAN_UI_JS
        title = "A practice week"
    elif view == "profile":
        fields = [F("errThen", "Effective rate, first", "pos"), F("errNow", "Effective rate, now", "pos"),
                  F("baseLo", "Baseline range of effective rates: lowest", "opt", ""),
                  F("baseHi", "Baseline range of effective rates: highest", "opt", ""),
                  F("baseN", "Baseline readings in the range", "nncount", 3),
                  F("tests", "Your test effective rates, oldest first (empty: the one rate now)", ("nums", "pos", 0, 20), []),
                  F("gistThen", "Skim gist score, first (share)", "share"), F("gistNow", "Skim gist score, now (share)", "share"),
                  F("scanThen", "Scan seconds per target, first", "pos"), F("scanNow", "Scan seconds per target, now", "pos"),
                  F("recallThen", "Free recall share, first", "share"), F("recallNow", "Free recall share, now", "share")]
        tiles = [("Effective rate, first", "lgErrThen"), ("Effective rate, now", "lgErrNow"), ("Verdict", "lgVerdict"),
                 ("Skim gist", "lgGist"), ("Scan time per target", "lgScan"), ("Free recall", "lgRecall")]
        main = _log_controls("Fill from my log")
        ui += LOG_PROFILE_UI_JS
        title = "Your profile, then and now"
    else:
        raise ValueError("%s: unknown view %r" % (kit, view))
    return rc.build_lab(cfg, kit=kit, prefix="lg", view=view, fields=fields, tiles=tiles, fn="lgCompute", js=LOG_JS, opts=opts,
                        title=title, subtitle="your own numbers, compared with themselves",
                        panel_title="Your log, in numbers",
                        panel_intro=("Your measurement, from your log (only readings logged as baseline or test count), or a "
                                     "worked example until you have one. Nothing leaves your browser."),
                        main_html=main, ui_js=ui)


_MODES = {"triage": _triage, "text": _text, "recall": _recall, "log": _log}


def readkit_b_lab(cfg, mode, view, kit):
    return _MODES[mode](cfg, view, kit)
