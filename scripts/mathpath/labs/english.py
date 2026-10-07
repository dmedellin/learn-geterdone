"""The English Subject's kit: one rule per mode, each scored on printed text.

WHAT THIS KIT PROVES. Nothing here is a table of answers. Every cell the reader
sees is produced in their browser by the rules the lesson states, applied to the
verb they typed, and `vbRuleTrace` names the rule that fired. A learner who is
handed a filled table learns twelve strings; a learner who watches the rules
fill it learns five rules and can fill the thirteenth themselves.

WHAT IT MEASURES, and why the residue is printed rather than counted away. The
forming rules are scored on the page against the attested forms of the printed
verb list: -s 99.85%, -ing 98.97%, -ed 98.67%. The words they miss are the
lesson -- busing, counselling, formatting, bred -- because a rule without its
exceptions is the thing textbooks already give.

THE REFUTED RULE. `rules` mode prints the -s rule against the variant that adds
f -> ves, which sounds right and scores WORSE (brief, golf, proof and roof are
verbs that take -s). The reader sees the comparison, not a claim about it.
"""

from .common import Lab, cfg_literal
from .algebra_core import RATIONAL_JS
from .english_core import ENGLISH_VERB_JS

MODES = ("table", "doubling", "svo", "adverbs", "questions",
         "irregular", "classes", "irrshare")


# ---------------------------------------------------------------------------
# table -- type a verb, watch the rules fill the twelve cells
# ---------------------------------------------------------------------------

_TABLE_PRESETS = [
    {"id": "walk", "label": "walk — nothing special happens",
     "verb": "walk",
     "expect": {"tbThird": "walks", "tbIng": "walking", "tbEd": "walked",
                "tbRule": "nothing special: just add the ending"}},
    {"id": "stop", "label": "stop — the last letter doubles",
     "verb": "stop",
     "expect": {"tbThird": "stops", "tbIng": "stopping", "tbEd": "stopped",
                "tbRule": "ends consonant-vowel-consonant, stressed: double it"}},
    {"id": "carry", "label": "carry — -y becomes -ies",
     "verb": "carry",
     "expect": {"tbThird": "carries", "tbIng": "carrying", "tbEd": "carried",
                "tbRule": "consonant then -y: -y becomes -ies"}},
    {"id": "hope", "label": "hope — the silent -e goes",
     "verb": "hope",
     "expect": {"tbThird": "hopes", "tbIng": "hoping", "tbEd": "hoped",
                "tbRule": "silent -e: drop it before -ing"}},
    {"id": "listen", "label": "listen — CVC, but the stress is early, so no doubling",
     "verb": "listen",
     "expect": {"tbThird": "listens", "tbIng": "listening", "tbEd": "listened",
                "tbRule": "nothing special: just add the ending"}},
    {"id": "go", "label": "go — irregular: looked up, not formed",
     "verb": "go",
     "expect": {"tbThird": "goes", "tbIng": "going", "tbEd": "went",
                "tbRule": "irregular: looked up, not formed"}},
]


def _expect(presets):
    return {p["id"]: p["expect"] for p in presets}


def _table(cfg):
    markup = (
        '<div class="kpi-grid">'
        '<div class="kpi"><span class="kpi-label">he / she / it</span>'
        '<span class="kpi-value" id="tbThird">walks</span></div>'
        '<div class="kpi"><span class="kpi-label">-ing form</span>'
        '<span class="kpi-value" id="tbIng">walking</span></div>'
        '<div class="kpi"><span class="kpi-label">past form</span>'
        '<span class="kpi-value" id="tbEd">walked</span></div>'
        '<div class="kpi"><span class="kpi-label">rule that fired</span>'
        '<span class="kpi-value" id="tbRule">nothing special</span></div>'
        '</div>'
        '<div class="table-wrap"><table id="tbGrid"><thead><tr>'
        '<th>time</th><th>simple</th><th>progressive</th>'
        '<th>perfect</th><th>perfect progressive</th>'
        '</tr></thead><tbody id="tbBody"></tbody></table></div>'
    )
    controls = (
        '<label for="tbVerb">A verb</label> '
        '<input id="tbVerb" type="text" value="walk" size="14" /> '
        '<label for="tbPreset">or one that shows a rule</label> '
        '<select id="tbPreset">'
        + "".join('<option value="%s">%s</option>' % (p["id"], p["label"])
                  for p in _TABLE_PRESETS)
        + "</select>"
    )
    script = (
        RATIONAL_JS + ENGLISH_VERB_JS
        + cfg_literal("TB_PRESETS", _TABLE_PRESETS)
        + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  /* The irregular verbs the page knows, printed in the lesson beside the lab. */
  VB_IRREG = {
    go:   { third: 'goes',  ing: 'going',  past: 'went',  pp: 'gone' },
    be:   { third: 'is',    ing: 'being',  past: 'was',   pp: 'been' },
    have: { third: 'has',   ing: 'having', past: 'had',   pp: 'had' },
    make: { third: 'makes', ing: 'making', past: 'made',  pp: 'made' },
    take: { third: 'takes', ing: 'taking', past: 'took',  pp: 'taken' },
    see:  { third: 'sees',  ing: 'seeing', past: 'saw',   pp: 'seen' }
  };
  VB_FINAL_STRESS = { listen: false, open: false, happen: false, offer: false,
                      visit: false, enter: false, answer: false, travel: false };

  var draw = function (verb) {
    verb = (verb || '').toLowerCase().replace(/[^a-z]/g, '') || 'walk';
    el('tbThird').textContent = vbThird(verb);
    el('tbIng').textContent = vbIng(verb);
    el('tbEd').textContent = vbEd(verb);
    el('tbRule').textContent = vbRuleTrace(verb);
    var cells = vbTable(verb, true), rows = {}, i, t;
    for (i = 0; i < cells.length; i++) {
      (rows[cells[i].time] = rows[cells[i].time] || {})[cells[i].aspect] = cells[i].form;
    }
    var html = '', times = ['present', 'past', 'future'],
        asp = ['simple', 'progressive', 'perfect', 'perfect progressive'];
    for (i = 0; i < times.length; i++) {
      html += '<tr><th scope="row">' + times[i] + '</th>';
      for (t = 0; t < asp.length; t++) {
        html += '<td>' + (rows[times[i]][asp[t]] || '') + '</td>';
      }
      html += '</tr>';
    }
    el('tbBody').innerHTML = html;
  };

  /* labcheck calls this after setting a control, and refuses the page without
     it: a lab whose figures cannot be re-driven from outside cannot be pinned. */
  window.redrawLab = function () { draw(el('tbVerb').value); };

  el('tbVerb').addEventListener('input', function () { draw(this.value); });
  el('tbPreset').addEventListener('change', function () {
    var i;
    for (i = 0; i < TB_PRESETS.length; i++) {
      if (TB_PRESETS[i].id === this.value) {
        el('tbVerb').value = TB_PRESETS[i].verb;
        draw(TB_PRESETS[i].verb);
        return;
      }
    }
  });
  draw('walk');
}());
"""
    )
    return Lab(
        title="Twelve cells, five rules, and the verb you typed",
        subtitle="Every cell is formed on the page by the rule named beside it",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type any verb and watch the table fill"),
        panel_intro=cfg.get(
            "panel_intro",
            "Nothing here is looked up except the verbs marked irregular. The "
            "three forms at the top are made by the rules this lesson states, "
            "and the box beside them names the rule that fired, so you can "
            "check the answer against the reason for it.",
        ),
        script=script,
        expect={"tbPreset": _expect(_TABLE_PRESETS)},
    )




# ---------------------------------------------------------------------------
# doubling -- the rule that needs the sound, and what it costs without it
# ---------------------------------------------------------------------------

# The 232 verbs of the NGSL that END consonant-vowel-consonant, which are the
# only verbs the doubling rule can touch. Printed on the page, because a hit
# rate the reader cannot recount is a hit rate they have to take on trust.
# Each row: base, 1 if the stress falls on the last part, 1 if it doubles,
# and the form the word list actually records.
DOUBLING_VERBS = [["abandon",0,0,"abandoning"],["admit",1,1,"admitting"],["alter",0,0,"altering"],["anger",0,0,"angering"],["answer",0,0,"answering"],["author",0,0,"authoring"],["bag",1,1,"bagging"],["ban",1,1,"banning"],["bar",1,1,"barring"],["bed",1,1,"bedding"],["begin",1,1,"beginning"],["benefit",0,1,"benefitting"],["bet",1,1,"betting"],["bin",1,1,"binning"],["bit",1,1,"bitting"],["blog",1,1,"blogging"],["border",0,0,"bordering"],["bother",0,0,"bothering"],["bottom",0,0,"bottoming"],["budget",0,0,"budgeting"],["burden",0,0,"burdening"],["bus",1,0,"busing"],["button",0,0,"buttoning"],["can",1,1,"canning"],["cancel",0,1,"cancelling"],["cap",1,1,"capping"],["carpet",0,0,"carpeting"],["catalog",0,0,"cataloging"],["center",0,0,"centering"],["chamber",0,0,"chambering"],["channel",0,1,"channelling"],["chat",1,1,"chatting"],["chicken",0,0,"chickening"],["chip",1,1,"chipping"],["club",1,1,"clubbing"],["cluster",0,0,"clustering"],["color",0,0,"coloring"],["commit",1,1,"committing"],["consider",0,0,"considering"],["control",1,1,"controlling"],["corner",0,0,"cornering"],["council",0,1,"councilling"],["counsel",0,1,"counselling"],["counter",0,0,"countering"],["cover",0,0,"covering"],["credit",0,0,"crediting"],["crop",1,1,"cropping"],["cup",1,1,"cupping"],["cut",1,1,"cutting"],["deliver",0,0,"delivering"],["deposit",0,0,"depositing"],["develop",0,0,"developing"],["dialog",0,0,"dialoging"],["differ",0,0,"differing"],["dig",1,1,"digging"],["discover",0,0,"discovering"],["disorder",0,0,"disordering"],["doctor",0,0,"doctoring"],["dog",1,1,"dogging"],["drag",1,1,"dragging"],["drop",1,1,"dropping"],["drug",1,1,"drugging"],["edit",0,0,"editing"],["encounter",0,0,"encountering"],["enter",0,0,"entering"],["exhibit",0,0,"exhibiting"],["factor",0,0,"factoring"],["fan",1,1,"fanning"],["father",0,0,"fathering"],["favor",0,0,"favoring"],["filter",0,0,"filtering"],["finger",0,0,"fingering"],["fit",1,1,"fitting"],["flag",1,1,"flagging"],["flat",1,1,"flatting"],["flower",0,0,"flowering"],["focus",0,1,"focussing"],["format",0,1,"formatting"],["frighten",0,0,"frightening"],["further",0,0,"furthering"],["gap",1,1,"gapping"],["garden",0,0,"gardening"],["gas",1,1,"gassing"],["gather",0,0,"gathering"],["grab",1,1,"grabbing"],["grin",1,1,"grinning"],["gun",1,1,"gunning"],["happen",0,0,"happening"],["harbor",0,0,"harboring"],["hat",1,1,"hatting"],["hit",1,1,"hitting"],["honor",0,0,"honoring"],["hot",1,1,"hotting"],["humor",0,0,"humoring"],["hunger",0,0,"hungering"],["input",0,1,"inputting"],["interpret",0,0,"interpreting"],["iron",0,0,"ironing"],["journal",0,0,"journaling"],["kid",1,1,"kidding"],["label",0,1,"labelling"],["labor",0,0,"laboring"],["layer",0,0,"layering"],["leather",0,0,"leathering"],["leg",1,1,"legging"],["let",1,1,"letting"],["letter",0,0,"lettering"],["level",0,1,"levelling"],["limit",0,0,"limiting"],["lip",1,1,"lipping"],["listen",0,0,"listening"],["log",1,1,"logging"],["major",0,0,"majoring"],["man",1,1,"manning"],["map",1,1,"mapping"],["market",0,0,"marketing"],["master",0,0,"mastering"],["matter",0,0,"mattering"],["member",0,0,"membering"],["metal",0,1,"metalling"],["meter",0,0,"metering"],["minister",0,0,"ministering"],["mirror",0,0,"mirroring"],["model",0,1,"modelling"],["monitor",0,0,"monitoring"],["mother",0,0,"mothering"],["motor",0,0,"motoring"],["murder",0,0,"murdering"],["neighbor",0,0,"neighboring"],["net",1,1,"netting"],["number",0,0,"numbering"],["occur",1,1,"occurring"],["offer",0,1,"offerring"],["officer",0,0,"officering"],["open",0,0,"opening"],["order",0,0,"ordering"],["output",0,1,"outputting"],["panel",0,1,"panelling"],["panic",0,0,"panicking"],["paper",0,0,"papering"],["parallel",0,0,"paralleling"],["partner",0,0,"partnering"],["pen",1,1,"penning"],["permit",1,1,"permitting"],["pig",1,1,"pigging"],["pilot",0,0,"piloting"],["plan",1,1,"planning"],["plot",1,1,"plotting"],["pocket",0,0,"pocketing"],["pop",1,1,"popping"],["pot",1,1,"potting"],["power",0,0,"powering"],["prefer",1,1,"preferring"],["prison",0,0,"prisoning"],["profit",0,0,"profiting"],["program",0,1,"programming"],["put",1,1,"putting"],["quarter",0,0,"quartering"],["rat",1,1,"ratting"],["reason",0,0,"reasoning"],["reckon",0,0,"reckoning"],["recover",0,0,"recovering"],["red",1,1,"redding"],["refer",1,1,"referring"],["register",0,0,"registering"],["regret",1,1,"regretting"],["remember",0,0,"remembering"],["rid",1,1,"ridding"],["rival",0,1,"rivalling"],["scan",1,1,"scanning"],["season",0,0,"seasoning"],["set",1,1,"setting"],["shelter",0,0,"sheltering"],["ship",1,1,"shipping"],["shop",1,1,"shopping"],["shoulder",0,0,"shouldering"],["shower",0,0,"showering"],["shut",1,1,"shutting"],["signal",0,1,"signalling"],["silver",0,0,"silvering"],["skin",1,1,"skinning"],["slip",1,1,"slipping"],["snap",1,1,"snapping"],["son",1,1,"sonning"],["spirit",0,0,"spiriting"],["split",1,1,"splitting"],["sponsor",0,0,"sponsoring"],["spot",1,1,"spotting"],["star",1,1,"starring"],["stem",1,1,"stemming"],["step",1,1,"stepping"],["stir",1,1,"stirring"],["stop",1,1,"stopping"],["strengthen",0,0,"strengthening"],["strip",1,1,"stripping"],["submit",1,1,"submitting"],["suffer",0,1,"sufferring"],["sum",1,1,"summing"],["summer",0,0,"summering"],["sun",1,1,"sunning"],["swim",1,1,"swimming"],["tap",1,1,"tapping"],["target",0,0,"targeting"],["tender",0,0,"tendering"],["thin",1,1,"thinning"],["threaten",0,0,"threatening"],["ticket",0,0,"ticketing"],["tip",1,1,"tipping"],["top",1,1,"topping"],["total",0,1,"totalling"],["tower",0,0,"towering"],["traffic",0,0,"trafficking"],["transfer",1,1,"transferring"],["trap",1,1,"trapping"],["travel",0,1,"travelling"],["trigger",0,0,"triggering"],["trip",1,1,"tripping"],["twin",1,1,"twinning"],["upset",1,1,"upsetting"],["visit",0,0,"visiting"],["wander",0,0,"wandering"],["war",1,1,"warring"],["water",0,0,"watering"],["weather",0,0,"weathering"],["web",1,1,"webbing"],["wed",1,1,"wedding"],["wet",1,1,"wetting"],["whisper",0,0,"whispering"],["win",1,1,"winning"],["winter",0,0,"wintering"],["wonder",0,0,"wondering"],["wrap",1,1,"wrapping"]]

_DB_PRESETS = [
    {"id": "stress", "label": "double when the last part is the strong part",
     "rule": "stress",
     "expect": {"dbScore": "210 of 232", "dbPct": "90.5%", "dbWrong": "22"}},
    {"id": "always", "label": "double every one of them",
     "rule": "always",
     "expect": {"dbScore": "117 of 232", "dbPct": "50.4%", "dbWrong": "115"}},
    {"id": "never", "label": "never double",
     "rule": "never",
     "expect": {"dbScore": "115 of 232", "dbPct": "49.6%", "dbWrong": "117"}},
]


def _doubling(cfg):
    markup = (
        '<div class="kpi-grid">'
        '<div class="kpi"><span class="kpi-label">right</span>'
        '<span class="kpi-value" id="dbScore">210 of 232</span></div>'
        '<div class="kpi"><span class="kpi-label">share</span>'
        '<span class="kpi-value" id="dbPct">90.5%</span></div>'
        '<div class="kpi"><span class="kpi-label">wrong</span>'
        '<span class="kpi-value" id="dbWrong">22</span></div>'
        '<div class="kpi"><span class="kpi-label">of those, ending in -l</span>'
        '<span class="kpi-value" id="dbEl">13</span></div>'
        '</div>'
        '<div class="table-wrap"><table id="dbTable"><thead><tr>'
        '<th>verb</th><th>strong part last?</th><th>rule says</th>'
        '<th>word list says</th><th></th></tr></thead>'
        '<tbody id="dbBody"></tbody></table></div>'
    )
    controls = (
        '<label for="dbPreset">The rule to score</label> '
        '<select id="dbPreset">'
        + "".join('<option value="%s">%s</option>' % (p["id"], p["label"])
                  for p in _DB_PRESETS)
        + "</select> "
        '<label for="dbShow">Show</label> '
        '<select id="dbShow">'
        '<option value="wrong">only the ones it gets wrong</option>'
        '<option value="all">every verb</option>'
        '</select>'
    )
    script = (
        cfg_literal("DB_VERBS", DOUBLING_VERBS)
        + cfg_literal("DB_PRESETS", _DB_PRESETS)
        + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var rule = 'stress', show = 'wrong';

  var predicts = function (row) {
    if (rule === 'always') return 1;
    if (rule === 'never') return 0;
    return row[1];                       /* the stress flag */
  };

  var draw = function () {
    var right = 0, wrong = [], i, row;
    for (i = 0; i < DB_VERBS.length; i++) {
      row = DB_VERBS[i];
      if (predicts(row) === row[2]) right++; else wrong.push(row);
    }
    var n = DB_VERBS.length;
    el('dbScore').textContent = right + ' of ' + n;
    /* One decimal place, worked in whole numbers so the printed figure is
       exactly what the division gives and not a floating-point artefact. */
    var tenths = Math.round(right * 1000 / n);
    el('dbPct').textContent = Math.floor(tenths / 10) + '.' + (tenths % 10) + '%';
    el('dbWrong').textContent = String(wrong.length);
    var el_count = 0;
    for (i = 0; i < wrong.length; i++) if (/l$/.test(wrong[i][0])) el_count++;
    el('dbEl').textContent = String(el_count);

    var rowsToShow = show === 'all' ? DB_VERBS : wrong, html = '';
    for (i = 0; i < rowsToShow.length && i < 240; i++) {
      row = rowsToShow[i];
      var says = predicts(row) ? row[0] + row[0].charAt(row[0].length - 1) + 'ing'
                               : row[0] + 'ing';
      html += '<tr><td>' + row[0] + '</td><td>' + (row[1] ? 'yes' : 'no')
            + '</td><td>' + says + '</td><td>' + row[3] + '</td><td>'
            + (says === row[3] ? '' : 'no') + '</td></tr>';
    }
    el('dbBody').innerHTML = html;
  };

  window.redrawLab = draw;
  el('dbPreset').addEventListener('change', function () { rule = this.value; draw(); });
  el('dbShow').addEventListener('change', function () { show = this.value; draw(); });
  draw();
}());
"""
    )
    return Lab(
        title="The doubling rule, scored three ways on the same 232 verbs",
        subtitle="Switch the stress condition off and watch the rule fall to a coin toss",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Score the rule yourself"),
        panel_intro=cfg.get(
            "panel_intro",
            "These are every verb in the word list that ends consonant, vowel, "
            "consonant -- the only verbs the doubling rule can touch. The table "
            "is scored in your browser against the forms the word list records, "
            "and you can read every row.",
        ),
        script=script,
        expect={"dbPreset": _expect(_DB_PRESETS)},
    )




def _data(name):
    """Read a printed dataset from content/english/data/.

    The data lives beside the content it belongs to rather than inside this
    module: it is the text the page prints, not code, and a reviewer should be
    able to read it without opening a lab kit.
    """
    import json
    import pathlib
    here = pathlib.Path(__file__).resolve()
    root = here.parent.parent.parent.parent          # scripts/mathpath/labs -> repo
    return json.loads((root / "content" / "english" / "data" / name).read_text())


# ---------------------------------------------------------------------------
# The word-order modes. One scanner, three rules, three printed datasets.
#
# Every figure these labs show is computed in the browser over text printed on
# the same page, scored against a lexicon printed with it. A dataset is never
# scored against another page's word list -- an early version scored a
# whole-novel concordance against a 141-word passage lexicon and reported 45%
# of its rows as "outside the lexicon", which measured the lexicon, not English.
# ---------------------------------------------------------------------------

WORDORDER_DATA = _data("wordorder_passage.json")
ADVERB_DATA = _data("adverb_concordance.json")
QUESTION_DATA = _data("question_concordance.json")

SCAN_JS = r"""
var wordsOf = function (s) { return s.match(/[A-Za-z][A-Za-z']*/g) || []; };
var lower = function (a) {
  var o = [], i;
  for (i = 0; i < a.length; i++) o.push(a[i].toLowerCase());
  return o;
};
var inSet = function (set, w) { return Object.prototype.hasOwnProperty.call(set, w); };
var setOf = function (list) {
  var o = {}, i;
  for (i = 0; i < list.length; i++) o[list[i]] = true;
  return o;
};
/* A share printed to one decimal place, worked in whole numbers so the figure
   on the page is exactly the division and not a floating-point artefact. */
var share1 = function (hit, total) {
  if (!total) return '0.0%';
  var t = Math.round(hit * 1000 / total);
  return Math.floor(t / 10) + '.' + (t % 10) + '%';
};
"""


_SVO_PRESETS = [
    {"id": "subject", "label": "subject pronouns: I, he, she, we, they",
     "kind": "subject",
     # Verified against an independent count, not copied from what the page
     # printed: 72 of 80 hold, one is the quotation-tag inversion, five have a
     # modifier between. Pinning whatever the lab says would make this vacuous.
     "expect": {"soHit": "72 of 80", "soPct": "90.0%", "soBroken": "1"}},
    {"id": "object", "label": "object pronouns: me, him, us, them",
     "kind": "object",
     "expect": {"soHit": "16 of 18", "soPct": "88.9%", "soBroken": "0"}},
]


def _svo(cfg):
    markup = (
        '<div class="kpi-grid">'
        '<div class="kpi"><span class="kpi-label">rule holds</span>'
        '<span class="kpi-value" id="soHit">72 of 80</span></div>'
        '<div class="kpi"><span class="kpi-label">share</span>'
        '<span class="kpi-value" id="soPct">90.0%</span></div>'
        '<div class="kpi"><span class="kpi-label">word order broken</span>'
        '<span class="kpi-value" id="soBroken">0</span></div>'
        '<div class="kpi"><span class="kpi-label">a modifier comes between</span>'
        '<span class="kpi-value" id="soMod">0</span></div>'
        '</div>'
        '<div class="table-wrap"><table id="soTable"><thead><tr>'
        '<th>pronoun</th><th>next word</th><th>what the rule says</th>'
        '</tr></thead><tbody id="soBody"></tbody></table></div>'
        '<div class="mathblock" id="soPassage" style="font-size:0.8rem;"></div>'
    )
    controls = (
        '<label for="soPreset">Which pronouns</label> '
        '<select id="soPreset">'
        + "".join('<option value="%s">%s</option>' % (p["id"], p["label"])
                  for p in _SVO_PRESETS)
        + '</select> '
        '<label for="soShow">Show</label> '
        '<select id="soShow">'
        '<option value="residue">only the ones the rule does not cover</option>'
        '<option value="all">every one</option>'
        '</select>'
    )
    script = SCAN_JS + cfg_literal("SO_DATA", WORDORDER_DATA) + cfg_literal("SO_PRESETS", _SVO_PRESETS) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var verbs = setOf(SO_DATA.verbs), aux = setOf(SO_DATA.aux);
  var SUBJ = setOf(['i', 'he', 'she', 'we', 'they']);
  var OBJ = setOf(['me', 'him', 'us', 'them']);
  var PREP = setOf(['of','to','in','for','on','with','at','by','from','about','into','over',
                    'after','under','between','through','against','before','without','upon']);
  var MOD = setOf(['all','both','who','that','first','as','when','also','which','never',
                   'always','only','then','still','soon','too','indeed','certainly','really',
                   'quite','almost','hardly','scarcely']);
  var REPORT = setOf(['said','cried','replied','returned','added','observed','asked',
                      'answered','exclaimed','thought','repeated','rejoined']);
  var kind = 'subject', show = 'residue';

  var scan = function () {
    var w = wordsOf(SO_DATA.passage), lw = lower(w), rows = [], i;
    var hit = 0, broken = 0, mod = 0;
    for (i = 0; i < lw.length; i++) {
      var isTarget = kind === 'subject' ? inSet(SUBJ, lw[i]) : inSet(OBJ, lw[i]);
      if (!isTarget) continue;
      var verdict, nxt = i + 1 < lw.length ? lw[i + 1] : '';
      var prev = i ? lw[i - 1] : '';
      if (kind === 'subject') {
        if (inSet(verbs, nxt) || inSet(aux, nxt)) { verdict = 'holds'; hit++; }
        else if (inSet(REPORT, prev)) { verdict = 'inverted, a quotation tag'; broken++; }
        else if (inSet(MOD, nxt)) { verdict = 'a modifier comes between'; mod++; }
        else verdict = 'next word not in the printed list';
      } else {
        if (inSet(verbs, prev) || inSet(aux, prev) || inSet(PREP, prev)) { verdict = 'holds'; hit++; }
        else if (inSet(MOD, prev)) { verdict = 'a modifier comes between'; mod++; }
        else verdict = 'word before it not in the printed list';
      }
      rows.push([w[i], kind === 'subject' ? (nxt || '—') : (prev || '—'), verdict]);
    }
    el('soHit').textContent = hit + ' of ' + rows.length;
    el('soPct').textContent = share1(hit, rows.length);
    el('soBroken').textContent = String(broken);
    el('soMod').textContent = String(mod);
    var html = '', shown = 0;
    for (i = 0; i < rows.length; i++) {
      if (show === 'residue' && rows[i][2] === 'holds') continue;
      if (shown++ > 120) break;
      html += '<tr><td>' + rows[i][0] + '</td><td>' + rows[i][1]
            + '</td><td>' + rows[i][2] + '</td></tr>';
    }
    el('soBody').innerHTML = html;
    el('soPassage').textContent = SO_DATA.passage;
  };
  window.redrawLab = scan;
  el('soPreset').addEventListener('change', function () { kind = this.value === 'object' ? 'object' : 'subject'; scan(); });
  el('soShow').addEventListener('change', function () { show = this.value; scan(); });
  scan();
}());
"""
    return Lab(
        title="The rule scored on a page you can read",
        subtitle="Every pronoun in the passage below, and the word that follows it",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "Score the rule on printed text"),
        panel_intro=cfg.get("panel_intro",
            "The passage is printed under the table and the list of verb forms it "
            "contains is printed with it. The scan runs in your browser over that "
            "text, so you can check any row by eye."),
        script=script,
        expect={"soPreset": _expect(_SVO_PRESETS)},
    )


_ADV_PRESETS = [
    {"id": "mid", "label": "the adverb sits in the middle",
     "expect": {"avHit": "85 of 120", "avPct": "70.8%"}},
]


def _adverbs(cfg):
    markup = (
        '<div class="kpi-grid">'
        '<div class="kpi"><span class="kpi-label">rule holds</span>'
        '<span class="kpi-value" id="avHit">85 of 120</span></div>'
        '<div class="kpi"><span class="kpi-label">share</span>'
        '<span class="kpi-value" id="avPct">70.8%</span></div>'
        '<div class="kpi"><span class="kpi-label">a preposition follows</span>'
        '<span class="kpi-value" id="avPrep">6</span></div>'
        '<div class="kpi"><span class="kpi-label">something else between</span>'
        '<span class="kpi-value" id="avOther">29</span></div>'
        '</div>'
        '<div class="table-wrap"><table id="avTable"><thead><tr>'
        '<th>adverb</th><th>the line it came from</th><th>verdict</th>'
        '</tr></thead><tbody id="avBody"></tbody></table></div>'
    )
    controls = (
        '<label for="avWord">Which adverb</label> '
        '<select id="avWord"><option value="">all of them</option>'
        + "".join('<option value="%s">%s</option>' % (a, a) for a in ADVERB_DATA["adverbs"])
        + '</select> '
        '<label for="avPreset">Rule</label> '
        '<select id="avPreset">'
        + "".join('<option value="%s">%s</option>' % (p["id"], p["label"]) for p in _ADV_PRESETS)
        + '</select>'
    )
    script = SCAN_JS + cfg_literal("AV_DATA", ADVERB_DATA) + cfg_literal("AV_PRESETS", _ADV_PRESETS) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var verbs = setOf(AV_DATA.verbs), aux = setOf(AV_DATA.aux);
  var BE = setOf(['is', 'are', 'was', 'were', 'am', 'be', 'been']);
  var PREP = setOf(['in', 'at', 'on', 'of', 'to', 'for', 'with']);
  var only = '';

  var scan = function () {
    var hit = 0, prep = 0, other = 0, rows = [], i;
    for (i = 0; i < AV_DATA.rows.length; i++) {
      var adv = AV_DATA.rows[i][0], ctx = AV_DATA.rows[i][1];
      if (only && adv !== only) continue;
      var lw = lower(wordsOf(ctx)), at = lw.indexOf(adv), verdict;
      var prev = at > 0 ? lw[at - 1] : '', nxt = at >= 0 && at + 1 < lw.length ? lw[at + 1] : '';
      if (at < 0) verdict = 'not found';
      else if (inSet(aux, prev) || inSet(BE, prev) || inSet(verbs, nxt) || inSet(aux, nxt)) {
        verdict = 'in the middle'; hit++;
      } else if (inSet(PREP, nxt)) { verdict = 'a preposition follows'; prep++; }
      else { verdict = 'something else between'; other++; }
      rows.push([adv, ctx, verdict]);
    }
    el('avHit').textContent = hit + ' of ' + rows.length;
    el('avPct').textContent = share1(hit, rows.length);
    el('avPrep').textContent = String(prep);
    el('avOther').textContent = String(other);
    var html = '';
    for (i = 0; i < rows.length && i < 130; i++) {
      html += '<tr><td>' + rows[i][0] + '</td><td>' + rows[i][1]
            + '</td><td>' + rows[i][2] + '</td></tr>';
    }
    el('avBody').innerHTML = html;
  };
  window.redrawLab = scan;
  el('avWord').addEventListener('change', function () { only = this.value; scan(); });
  el('avPreset').addEventListener('change', function () { scan(); });
  scan();
}());
"""
    return Lab(
        title="One hundred and twenty lines, and where the adverb sits in each",
        subtitle="Every line the figure is computed from is printed in the table",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "Where the adverb goes, counted"),
        panel_intro=cfg.get("panel_intro",
            "Each row is a line taken from the book around one adverb. The rule is "
            "scored in your browser against the verb forms printed with the lines, "
            "and you can read every row and disagree with any of them."),
        script=script,
        expect={"avPreset": _expect(_ADV_PRESETS)},
    )


_Q_PRESETS = [
    {"id": "aux", "label": "a question starts with an auxiliary, or a wh-word then one",
     "expect": {"quHit": "48 of 90", "quPct": "53.3%"}},
]


def _questions(cfg):
    markup = (
        '<div class="kpi-grid">'
        '<div class="kpi"><span class="kpi-label">rule holds</span>'
        '<span class="kpi-value" id="quHit">48 of 90</span></div>'
        '<div class="kpi"><span class="kpi-label">share</span>'
        '<span class="kpi-value" id="quPct">53.3%</span></div>'
        '<div class="kpi"><span class="kpi-label">starts with a joining word</span>'
        '<span class="kpi-value" id="quConn">13</span></div>'
        '<div class="kpi"><span class="kpi-label">something else</span>'
        '<span class="kpi-value" id="quOther">21</span></div>'
        '</div>'
        '<div class="table-wrap"><table id="quTable"><thead><tr>'
        '<th>question</th><th>verdict</th></tr></thead>'
        '<tbody id="quBody"></tbody></table></div>'
    )
    controls = (
        '<label for="quPreset">Rule</label> '
        '<select id="quPreset">'
        + "".join('<option value="%s">%s</option>' % (p["id"], p["label"]) for p in _Q_PRESETS)
        + '</select> '
        '<label for="quShow">Show</label> '
        '<select id="quShow">'
        '<option value="residue">only the ones it fails</option>'
        '<option value="all">every question</option>'
        '</select>'
    )
    script = SCAN_JS + cfg_literal("QU_DATA", QUESTION_DATA) + cfg_literal("QU_PRESETS", _Q_PRESETS) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var AUX = setOf(['is','are','was','were','be','am','have','has','had','do','does','did',
                   'will','would','shall','should','can','could','may','might','must','cannot']);
  var WH = setOf(['what','where','when','why','who','whom','whose','how','which']);
  var CONN = setOf(['and','but','or','so','yet','for','then']);
  var FILLER = setOf(['pray','oh','well','my','dear']);
  var show = 'residue';

  var scan = function () {
    var hit = 0, conn = 0, other = 0, rows = [], i;
    for (i = 0; i < QU_DATA.questions.length; i++) {
      var q = QU_DATA.questions[i], lw = lower(wordsOf(q)), verdict;
      if (!lw.length) continue;
      if (inSet(AUX, lw[0])) { verdict = 'holds'; hit++; }
      else if (inSet(WH, lw[0]) && lw.length > 1 && inSet(AUX, lw[1])) { verdict = 'holds'; hit++; }
      else if (inSet(WH, lw[0])) verdict = 'a wh-word with no auxiliary after it';
      else if (inSet(CONN, lw[0])) { verdict = 'starts with a joining word'; conn++; }
      else if (inSet(FILLER, lw[0])) verdict = 'starts with an address';
      else { verdict = 'something else'; other++; }
      rows.push([q, verdict]);
    }
    el('quHit').textContent = hit + ' of ' + rows.length;
    el('quPct').textContent = share1(hit, rows.length);
    el('quConn').textContent = String(conn);
    el('quOther').textContent = String(other);
    var html = '';
    for (i = 0; i < rows.length; i++) {
      if (show === 'residue' && rows[i][1] === 'holds') continue;
      html += '<tr><td>' + rows[i][0] + '</td><td>' + rows[i][1] + '</td></tr>';
    }
    el('quBody').innerHTML = html;
  };
  window.redrawLab = scan;
  el('quPreset').addEventListener('change', function () { scan(); });
  el('quShow').addEventListener('change', function () { show = this.value; scan(); });
  scan();
}());
"""
    return Lab(
        title="Ninety real questions, and a rule that does not cover them",
        subtitle="The rule is stated, scored, and shown to fail -- which is the lesson",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "A rule that does not work, and why that is printed"),
        panel_intro=cfg.get("panel_intro",
            "These are real questions from the book. The rule is scored against "
            "them in your browser. It covers about half, and the half it misses is "
            "printed so you can see what questions actually look like."),
        script=script,
        expect={"quPreset": _expect(_Q_PRESETS)},
    )




# ---------------------------------------------------------------------------
# The irregular-verb modes. One printed list, three views of it.
# ---------------------------------------------------------------------------

IRREGULAR_DATA = _data("irregular_verbs.json")

_IR_PRESETS = [
    {"id": "all", "label": "every verb on the list", "cls": "",
     "expect": {"irCount": "133", "irClasses": "7", "irBiggest": "60"}},
    {"id": "past_eq_pp", "label": "past and participle are the same word", "cls": "past_eq_pp",
     "expect": {"irCount": "60", "irClasses": "7", "irBiggest": "60"}},
    {"id": "all_same", "label": "all three forms the same", "cls": "all_same",
     "expect": {"irCount": "21", "irClasses": "7", "irBiggest": "60"}},
    {"id": "all_diff_n", "label": "all three differ, participle ends in -n", "cls": "all_diff_n",
     "expect": {"irCount": "37", "irClasses": "7", "irBiggest": "60"}},
    {"id": "all_diff_other", "label": "all three differ, participle does not end in -n",
     "cls": "all_diff_other",
     "expect": {"irCount": "9", "irClasses": "7", "irBiggest": "60"}},
]


def _irregular_view(cfg, title, subtitle, panel_title, panel_intro):
    markup = (
        '<div class="kpi-grid">'
        '<div class="kpi"><span class="kpi-label">verbs shown</span>'
        '<span class="kpi-value" id="irCount">133</span></div>'
        '<div class="kpi"><span class="kpi-label">patterns in all</span>'
        '<span class="kpi-value" id="irClasses">7</span></div>'
        '<div class="kpi"><span class="kpi-label">largest pattern</span>'
        '<span class="kpi-value" id="irBiggest">60</span></div>'
        '<div class="kpi"><span class="kpi-label">share of the list</span>'
        '<span class="kpi-value" id="irPct">100.0%</span></div>'
        '</div>'
        '<div id="irRule" class="mathblock"></div>'
        '<div class="table-wrap"><table id="irTable"><thead><tr>'
        '<th>base</th><th>past</th><th>after <em>have</em></th><th>pattern</th>'
        '</tr></thead><tbody id="irBody"></tbody></table></div>'
    )
    controls = (
        '<label for="irPreset">Which verbs</label> <select id="irPreset">'
        + "".join('<option value="{}">{}</option>'.format(p["id"], p["label"])
                  for p in _IR_PRESETS)
        + "</select>"
    )
    script = SCAN_JS + cfg_literal("IR_DATA", IRREGULAR_DATA) + cfg_literal("IR_PRESETS", _IR_PRESETS) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var cls = '';

  var draw = function () {
    var rows = [], i, v, classes = {}, biggest = 0;
    for (i = 0; i < IR_DATA.verbs.length; i++) {
      v = IR_DATA.verbs[i];
      classes[v.class] = (classes[v.class] || 0) + 1;
      if (!cls || v.class === cls) rows.push(v);
    }
    var names = Object.keys(classes), k;
    for (k = 0; k < names.length; k++) {
      if (classes[names[k]] > biggest) biggest = classes[names[k]];
    }
    el('irCount').textContent = String(rows.length);
    el('irClasses').textContent = String(names.length);
    el('irBiggest').textContent = String(biggest);
    el('irPct').textContent = share1(rows.length, IR_DATA.verbs.length);
    el('irRule').textContent = cls && IR_DATA.classes[cls]
      ? IR_DATA.classes[cls].rule
      : 'Every verb on the list, in every pattern.';
    var html = '';
    for (i = 0; i < rows.length; i++) {
      html += '<tr><td>' + rows[i].base + '</td><td>' + rows[i].past
            + '</td><td>' + rows[i].pp + '</td><td>' + rows[i].class + '</td></tr>';
    }
    el('irBody').innerHTML = html;
  };
  window.redrawLab = draw;
  el('irPreset').addEventListener('change', function () {
    var i;
    for (i = 0; i < IR_PRESETS.length; i++) {
      if (IR_PRESETS[i].id === this.value) { cls = IR_PRESETS[i].cls; draw(); return; }
    }
  });
  draw();
}());
"""
    return Lab(
        title=title, subtitle=subtitle, markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", panel_title),
        panel_intro=cfg.get("panel_intro", panel_intro),
        script=script, expect={"irPreset": _expect(_IR_PRESETS)},
    )


def _irregular(cfg):
    return _irregular_view(
        cfg,
        "Every irregular verb the course covers, with its three forms",
        "133 verbs, and the pattern each one follows",
        "The whole list, and how it divides",
        "Every verb here is printed with its three forms. Choose a pattern and "
        "the list narrows to the verbs that follow it, with the rule that "
        "defines it printed above the table.",
    )


def _classes(cfg):
    return _irregular_view(
        cfg,
        "Six patterns, and the rule that decides each one",
        "The rules work on the letters, not on the sound",
        "Pick a pattern and read its rule",
        "Each pattern is a rule about the three written forms. Choosing one "
        "prints its rule and the verbs it holds, so you can check the rule "
        "against every verb it claims.",
    )


_SH_PRESETS = [
    {"id": "with", "label": "count be, have and do as irregular verbs", "big": 1,
     "expect": {"shCount": "106", "shPct": "11.2%"}},
    {"id": "without", "label": "leave be, have and do out", "big": 0,
     "expect": {"shCount": "52", "shPct": "5.5%"}},
]


def _irrshare(cfg):
    markup = (
        '<div class="kpi-grid">'
        '<div class="kpi"><span class="kpi-label">irregular forms found</span>'
        '<span class="kpi-value" id="shCount">106</span></div>'
        '<div class="kpi"><span class="kpi-label">share of the passage</span>'
        '<span class="kpi-value" id="shPct">11.2%</span></div>'
        '<div class="kpi"><span class="kpi-label">be, have and do alone</span>'
        '<span class="kpi-value" id="shBig">54</span></div>'
        '<div class="kpi"><span class="kpi-label">their share of the irregulars</span>'
        '<span class="kpi-value" id="shBigPct">50.9%</span></div>'
        '</div>'
        '<div class="table-wrap"><table id="shTable"><thead><tr>'
        '<th>verb</th><th>times it appears</th></tr></thead>'
        '<tbody id="shBody"></tbody></table></div>'
        '<div class="mathblock" id="shPassage" style="font-size:0.8rem;"></div>'
    )
    controls = (
        '<label for="shPreset">How to count</label> <select id="shPreset">'
        + "".join('<option value="{}">{}</option>'.format(p["id"], p["label"])
                  for p in _SH_PRESETS)
        + "</select>"
    )
    script = (SCAN_JS + cfg_literal("SH_IRR", IRREGULAR_DATA)
              + cfg_literal("SH_TEXT", _data("wordorder_passage.json"))
              + cfg_literal("SH_PRESETS", _SH_PRESETS) + r"""
(function () {
  var el = function (id) { return document.getElementById(id); };
  var BIG = setOf(['be', 'have', 'do']);
  var withBig = true;

  var form2base = {};
  (function () {
    var i, v, b;
    for (i = 0; i < SH_IRR.verbs.length; i++) {
      v = SH_IRR.verbs[i]; b = v.base;
      form2base[b] = b;
      if (v.past) form2base[v.past] = b;
      if (v.pp) form2base[v.pp] = b;
      form2base[b + 's'] = b;
      form2base[b + 'ing'] = b;
    }
  }());

  var draw = function () {
    var toks = lower(wordsOf(SH_TEXT.passage)), counts = {}, total = 0, big = 0, i, base;
    for (i = 0; i < toks.length; i++) {
      if (!inSet(form2base, toks[i])) continue;
      base = form2base[toks[i]];
      if (inSet(BIG, base)) { big++; if (!withBig) continue; }
      counts[base] = (counts[base] || 0) + 1;
      total++;
    }
    el('shCount').textContent = String(total);
    el('shPct').textContent = share1(total, toks.length);
    el('shBig').textContent = String(big);
    /* be/have/do as a share of the irregulars WITH them counted, always: the
       point of the tile is what they contribute, so the denominator must not
       move when the menu does. */
    el('shBigPct').textContent = share1(big, withBig ? total : total + big);
    var names = Object.keys(counts);
    names.sort(function (a, b) { return counts[b] - counts[a]; });
    var html = '';
    for (i = 0; i < names.length; i++) {
      html += '<tr><td>' + names[i] + '</td><td>' + counts[names[i]] + '</td></tr>';
    }
    el('shBody').innerHTML = html;
    el('shPassage').textContent = SH_TEXT.passage;
  };
  window.redrawLab = draw;
  el('shPreset').addEventListener('change', function () {
    withBig = this.value === 'with'; draw();
  });
  draw();
}());
""")
    return Lab(
        title="How much of a real page is an irregular verb",
        subtitle="Counted on the passage below, with and without be, have and do",
        markup=markup, controls=controls,
        panel_title=cfg.get("panel_title", "Count them yourself"),
        panel_intro=cfg.get("panel_intro",
            "The passage is printed under the table. Every word in it is checked "
            "against the printed list of irregular verbs, and the menu decides "
            "whether be, have and do are counted. Watch what happens when they "
            "are not."),
        script=script, expect={"shPreset": _expect(_SH_PRESETS)},
    )


_MODES = {"table": _table, "doubling": _doubling,
          "svo": _svo, "adverbs": _adverbs, "questions": _questions,
          "irregular": _irregular, "classes": _classes, "irrshare": _irrshare}


def english_lab(cfg):
    """The tense course's kit. `cfg["mode"]` chooses the lesson; unknown raises."""
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "english_lab: unknown mode %r; this kit serves %s"
            % (mode, ", ".join(sorted(_MODES)))
        )
    return _MODES[mode](cfg or {})


__all__ = ["english_lab", "MODES"]
