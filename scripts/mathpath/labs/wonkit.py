"""wonkit -- the lab kit of The Wealth of Nations, Read Along (family A, Book I).

Specified in docs/wealth-of-nations/PLAN.md sections 0 and D (D.1 is this
module's table); the report an author configures a lesson from is
docs/wealth-of-nations/kit-report-a.md. The seam shared with family B is
wonkit_core.py, and every view here is built through `wonkit_core.mode_lab`.

Family A (this module), Book I:

  division   (wdv)  supply, pins, exchange, market
  money      (wmo)  barter, coin
  price      (wpr)  real, parts, market
  wages      (wwg)  subsistence, fund, growth
  advantage  (wad)  net, lottery, profit
  rent       (wre)  residual, tenure, silver
  interest   (wit)  purchase, profit

Family B (wonkit_b.py) exposes MODES; `wonkit_lab` dispatches any mode not
listed above through `wonkit_b.MODES`, imported lazily so this module imports
before wonkit_b.py exists.

THE BUILDER SIGNATURE. `builder(cfg) -> common.Lab`; every builder is
`lambda cfg: mode_lab(cfg, <mode>, <SPEC>)`. The first view is the default.
A page ships RATIONAL_JS, EA_CORE_JS, AKT_CORE_JS, WNK_CORE_JS, its mode's
base block and its own view's block -- never another view's or mode's.

UNITS. Lesson-level cfg keys, read by each view's `options` hook and handed to
the compute function as opts: `money_unit` (default `£`) wherever a view prints
money, `qty_unit`, `measure_unit` and `period` where D.1 names them. No £sd
cell kind is defined: every money amount is typed in the one unit the lesson
names (pence as `d`, shillings as `s`), see the report.

EXACTNESS. Every figure is a count or an exact BigInt rational; money and
quantities that are not exact at two places are shown to two places with ≈.
Nothing typed is evaluated as script.
"""

import importlib
import re

from .wonkit_core import alist, arec, ea, mode_lab, num_text, rat

_N = ea.NAME
LIMIT = ea.LIMIT

# ---------------------------------------------------------------------------
# Shared printers of family A. One template, shipped in each mode's base block
# with %P% replaced by the mode's prefix (so every name begins with it).
# ---------------------------------------------------------------------------

WNA_JS = r"""
  /* family A's printers (kit-report-a.md, "Printers"); %P% is the mode prefix. */
  function %P%Unit(r, w) { return eaNum(r) + ' ' + (Requ(Rabs(r), R1) && /^[A-Za-z]+s$/.test(w) ? w.slice(0, -1) : w); }
  function %P%Two(r) { return Rint(r) ? eaInt(r.n) : (eaExactAt(r, 2) ? '' : '≈ ') + eaFixed(r, 2); }
  function %P%Money(r, u, signed) {
    var a = Rabs(r), ex = Rint(a) || eaExactAt(a, 2), t = Rint(a) ? eaInt(a.n) : eaFixed(a, 2);
    var sign = r.n < 0n ? EA_MINUS : (signed && r.n > 0n ? '+' : '');
    var body = /^[£$€]$/.test(u) ? u + t : t + (u === 's' || u === 'd' ? '' : ' ') + u;
    return (ex ? '' : '≈ ') + sign + body;
  }
  function %P%Rate(p) { return (eaExactAt(p, 2) ? aktDec(p) : eaNum(p)) + '%'; }
  function %P%Ch(r) {
    var t = eaPct(r);
    if (r.n <= 0n) return t;
    return /^[=≈]/.test(t) ? t.replace(/^([=≈] )/, '$1+') : '+' + t.replace(/ ([=≈]) /, ' $1 +');
  }
  function %P%Sg(r) { return (r.n > 0n ? '+' : '') + eaNum(r); }
  function %P%X(r) { return eaNum(r) + '×'; }
  function %P%Way(r) { return r.n > 0n ? 'rose' : (r.n < 0n ? 'fell' : 'held'); }
"""


def _js(prefix, base):
    return WNA_JS.replace("%P%", prefix) + base


_UNIT_WORD = re.compile(r"^[A-Za-z£$€](?:[A-Za-z£$€ .-]{0,22}[A-Za-z.])?$")
_UNIT_DEFAULTS = {"money_unit": "£", "measure_unit": "days of labour", "period": "week"}


def _units(**defaults):
    """An options hook taking the lesson-level unit keys named, with their defaults."""
    def options(cfg, kit, tiles):
        fixed = {}
        for key, default in defaults.items():
            v = cfg.get(key, default)
            if not isinstance(v, str) or not _UNIT_WORD.match(v) or "  " in v:
                raise ValueError("%s: cfg[%r] should be a short plain word or symbol (letters, spaces, dots, hyphens, "
                                 "£ $ €; at most 24 characters), not %r" % (kit, key, v))
            fixed[key] = v
        return fixed, sorted(defaults), tiles
    return options


def _money(**more):
    return _units(money_unit="£", **more)


def _n(fr):
    return num_text(fr)


# ---------------------------------------------------------------------------
# division (wdv): produce per head, the pin factory, exchange, the market
# ---------------------------------------------------------------------------

WDV_JS = r"""
  var WDV_VIEW = {};
  function wdvCompute(view, inst, opts) { return eaRun(WDV_VIEW[view], inst, opts); }
"""

WDV_VIEW_JS = {}

WDV_VIEW_JS["supply"] = r"""
  WDV_VIEW.supply = function (inst, o) {
    var u = o.qty_unit;
    inst.nations.forEach(function (x, i) {
      if (Rcmp(x.workers, x.population) > 0) eaRefuse('Nations, record ' + (i + 1) + ' (' + x.nation + '): ' + eaNum(x.workers) + ' at work is more than the population of ' + eaNum(x.population));
    });
    var N = inst.nations.map(function (x) {
      var prod = Rmul(x.workers, x.output);
      return { name: x.nation, pop: x.population, work: x.workers, share: Rdiv(x.workers, x.population), prod: prod, head: Rdiv(prod, x.population) };
    });
    var list = function (f) { return N.map(function (x) { return x.name + ' ' + f(x); }).join('; '); };
    var s = N.slice().sort(function (a, b) { return Rcmp(b.head, a.head); });
    var tops = N.filter(function (x) { return Requ(x.head, s[0].head); }), best, ratio, say;
    var head = function (x) { return wdvUnit(x.head, u) + ' a head'; };
    if (N.length === 1) {
      best = N[0].name + ', ' + head(N[0]) + ' (one nation only)'; ratio = 'one nation only';
      say = N[0].name + ': ' + head(N[0]) + ', with ' + eaPct(N[0].share) + ' of its people at work';
    } else {
      if (Rzero(s[0].head)) best = 'no nation produces anything';
      else if (tops.length > 1) best = tops.map(function (x) { return x.name; }).join(' and ') + ' tie at ' + head(s[0]);
      else best = s[0].name + ', ' + head(s[0]);
      if (Rzero(s[1].head)) ratio = Rzero(s[0].head) ? 'every nation produces nothing a head' : 'no finite ratio: ' + s[1].name + ' produces nothing a head';
      else ratio = wdvX(Rdiv(s[0].head, s[1].head)) + ' (' + s[0].name + ' over ' + s[1].name + ')';
      say = tops.length > 1 ? best : s[0].name + ' is the better supplied: ' + head(s[0]) + ' against ' + wdvUnit(s[1].head, u) + ' for ' + s[1].name;
    }
    return {
      tiles: {
        wdvShare: list(function (x) { return eaPct(x.share); }),
        wdvProduce: list(function (x) { return wdvUnit(x.prod, u); }),
        wdvPerHead: list(function (x) { return wdvUnit(x.head, u); }),
        wdvBest: best, wdvRatio: ratio
      },
      status: wnkStatus(say),
      table: { caption: 'Each nation: the share at useful labour, the annual produce and the produce per head (' + u + ')',
               head: ['nation', 'population', 'at work', 'share at work', 'annual produce', 'per head'],
               rows: N.map(function (x) { return [x.name, eaNum(x.pop), eaNum(x.work), eaPct(x.share), eaNum(x.prod), eaNum(x.head)]; }) }
    };
  };
"""

WDV_VIEW_JS["pins"] = r"""
  WDV_VIEW.pins = function (inst, o) {
    var u = o.qty_unit, n = inst.workers, per = Rdiv(inst.together, n), solo = Rmul(n, inst.alone);
    var mult = Rzero(inst.alone) ? 'no finite multiple: alone, a worker makes none' : wdvX(Rdiv(per, inst.alone));
    var extra = Rsub(inst.together, solo);
    return {
      tiles: {
        wdvPerWorker: wdvUnit(per, u) + ' a day',
        wdvAloneTeam: wdvUnit(solo, u) + ' a day',
        wdvMultiple: mult,
        wdvExtra: (extra.n > 0n ? '+' : '') + wdvUnit(extra, u) + ' a day',
        wdvOpsEach: wdvUnit(Rdiv(inst.operations, n), 'operations') + ' a worker'
      },
      status: wnkStatus('Dividing ' + eaPlural(inst.operations.n, 'operation', 'operations') + ' among ' + eaPlural(n.n, 'worker', 'workers')
        + ', each makes ' + wdvUnit(per, u) + ' a day against ' + wdvUnit(inst.alone, u) + ' alone'
        + (Rzero(inst.alone) ? ', so no multiple is finite' : ', ' + wdvX(Rdiv(per, inst.alone)) + ' as many')),
      table: { caption: 'The team a day, divided and alone (' + u + ')', head: ['', 'the team', 'a worker'],
               rows: [['divided', eaNum(inst.together), eaNum(per)], ['each alone', eaNum(solo), eaNum(inst.alone)], ['difference', wdvSg(extra), wdvSg(Rsub(per, inst.alone))]] }
    };
  };
"""

WDV_VIEW_JS["exchange"] = r"""
  WDV_VIEW.exchange = function (inst) {
    var g = inst.goods, P = inst.producers, a = P[0], b = P[1];
    var ra = Rdiv(a.a, a.b), rb = Rdiv(b.a, b.b);
    if (Requ(ra, rb)) eaRefuse('The two producers have the same relative cost (' + eaNum(ra) + ' hours of ' + g[0] + ' for an hour of ' + g[1] + '), so neither has the lower cost of either good and the relative-cost rule names no division');
    var q = P.map(function (p) { return Rdiv(p.hours, Radd(p.a, p.b)); }), self = Radd(q[0], q[1]);
    var m0 = Rcmp(ra, rb) < 0 ? 0 : 1, m1 = 1 - m0;
    var s0 = Rdiv(P[m0].hours, P[m0].a), s1 = Rdiv(P[m1].hours, P[m1].b);
    var gain0 = Rsub(s0, self), gain1 = Rsub(s1, self);
    var better = function (k) { var c = Rcmp(a[k], b[k]); return c === 0 ? null : (c < 0 ? a.producer : b.producer); };
    var bA = better('a'), bB = better('b'), kase;
    if (bA && bB && bA !== bB) kase = 'each is better at one good: ' + bA + ' at ' + g[0] + ', ' + bB + ' at ' + g[1] + ' (Smith’s case)';
    else kase = 'not Smith’s case: ' + (bA ? bA + ' is better at ' + g[0] : 'neither is better at ' + g[0]) + ' and ' + (bB ? (bB === bA ? 'also' : bB + ' is better') + ' at ' + g[1] : 'neither at ' + g[1]) + '; only the relative-cost rule divides the work';
    return {
      tiles: {
        wdvSelfEach: P.map(function (p, i) { return p.producer + ' ' + eaNum(q[i]) + ' of each'; }).join('; '),
        wdvSelfTotal: g[0] + ' ' + eaNum(self) + '; ' + g[1] + ' ' + eaNum(self),
        wdvWho: P[m0].producer + ' makes ' + g[0] + ' (relative cost ' + eaNum(m0 === 0 ? ra : rb) + ' against ' + eaNum(m0 === 0 ? rb : ra) + '); ' + P[m1].producer + ' makes ' + g[1],
        wdvSpecTotal: g[0] + ' ' + eaNum(s0) + '; ' + g[1] + ' ' + eaNum(s1),
        wdvGain: g[0] + ' ' + wdvSg(gain0) + '; ' + g[1] + ' ' + wdvSg(gain1),
        wdvCase: kase
      },
      status: wnkStatus('Specialised, ' + P[m0].producer + ' makes ' + g[0] + ' and ' + P[m1].producer + ' makes ' + g[1] + ': '
        + g[0] + ' ' + wdvSg(gain0) + ' and ' + g[1] + ' ' + wdvSg(gain1) + ' against each making equal quantities of both'),
      table: { caption: 'Each producer: hours a unit, relative cost, and the output each way',
               head: ['producer', 'hours', 'hours a unit of ' + g[0], 'hours a unit of ' + g[1], 'relative cost', 'self-sufficient (each good)', 'specialised'],
               rows: P.map(function (p, i) { return [p.producer, eaNum(p.hours), eaNum(p.a), eaNum(p.b), eaNum(i === 0 ? ra : rb), eaNum(q[i]), i === m0 ? eaNum(s0) + ' ' + g[0] : eaNum(s1) + ' ' + g[1]]; }) }
    };
  };
"""

WDV_VIEW_JS["market"] = r"""
  WDV_VIEW.market = function (inst, o) {
    var u = o.qty_unit, out = inst.output, L = inst.places;
    var keep = L.map(function (p) { return eaFloor(Rdiv(p.demand, out)); });
    var live = L.filter(function (p, i) { return keep[i] > 0n; }).map(function (p) { return p.place; });
    var list = function (f) { return L.map(function (p, i) { return p.place + ' ' + f(p, i); }).join('; '); };
    var where = live.length === 0 ? 'none of ' + eaPlural(L.length, 'place', 'places') : eaInt(live.length) + ' of ' + eaPlural(L.length, 'place', 'places') + ': ' + live.join(', ');
    return {
      tiles: {
        wdvKeeps: list(function (p, i) { return eaInt(keep[i]); }),
        wdvYearShare: list(function (p) { return eaPct(Rdiv(p.demand, out)); }),
        wdvLive: where,
        wdvPerDay: wdvUnit(Rdiv(out, inst.days), u) + ' a day'
      },
      status: wnkStatus('One specialist makes ' + wdvUnit(out, u) + ' a year; a full-time trade can live in ' + where),
      table: { caption: 'Each place: its demand a year against one specialist’s year (' + u + ')',
               head: ['place', 'demand a year', 'specialists kept', 'share of one specialist’s year', 'a full-time trade'],
               rows: L.map(function (p, i) { return [p.place, eaNum(p.demand), eaInt(keep[i]), eaPct(Rdiv(p.demand, out)), keep[i] > 0n ? 'yes' : 'no']; }) }
    };
  };
"""


def _check_supply(inst, fixed):
    for i, x in enumerate(inst["nations"]):
        if x["workers"] > x["population"]:
            raise ValueError("Nations, record %d (%s): %s at work is more than the population of %s"
                             % (i + 1, x["nation"], _n(x["workers"]), _n(x["population"])))


def _check_exchange(inst, fixed):
    a, b = inst["producers"]
    ra, rb = a["a"] / a["b"], b["a"] / b["b"]
    if ra == rb:
        g = inst["goods"]
        raise ValueError("The two producers have the same relative cost (%s hours of %s for an hour of %s), so neither "
                         "has the lower cost of either good and the relative-cost rule names no division"
                         % (_n(ra), g[0], g[1]))


DIVISION = {
    "prefix": "wdv", "fn": "wdvCompute", "title": "The division of labour", "js": _js("wdv", WDV_JS),
    "views": {
        "supply": {
            "fields": [("nations", arec("Nations (nation, population, workers at useful labour, output per worker a year)",
                                        [("nation", _N), ("population", ea.whole(1, LIMIT)), ("workers", ea.whole(0, LIMIT)),
                                         ("output", rat(lo=0))], unique=True, rows=3, lo=1, hi=12), None)],
            "tiles": [("Share of the people at useful labour", "wdvShare"), ("Annual produce", "wdvProduce"),
                      ("Produce per head", "wdvPerHead"), ("Better supplied per head", "wdvBest"),
                      ("Best per head over the next", "wdvRatio")],
            "check": _check_supply, "options": _units(qty_unit="units"),
            "subtitle": "produce per head from the share at work and the output of each",
            "rules": "A nation's annual produce is its workers times the output of each a year; produce per head "
                     "divides it by the whole population, workers or not. Smith gives the rule (Introduction): "
                     "supply per head depends on the skill of the labour and the proportion of people usefully "
                     "employed. The share at work is workers over population, exact. Nations are listed in the order "
                     "given; the better supplied is the highest produce per head (equal ones tie), and the ratio is "
                     "the highest per head over the next highest (the earlier given wins a tie for second place).",
            "js": WDV_VIEW_JS["supply"],
        },
        "pins": {
            "fields": [("workers", ea.field("Workers in the team", ea.whole(1, 10000)), "10"),
                       ("operations", ea.field("Distinct operations", ea.whole(1, 10000)), "18"),
                       ("together", ea.field("The team's output a day, divided", rat(gt=0)), "48000"),
                       ("alone", ea.field("One worker's output a day alone (0 for none)", rat(lo=0)), "20")],
            "tiles": [("Output per worker, divided", "wdvPerWorker"), ("The team's output if each worked alone", "wdvAloneTeam"),
                      ("Multiple (per worker divided over alone)", "wdvMultiple"), ("Extra output of the team a day", "wdvExtra"),
                      ("Operations per worker", "wdvOpsEach")],
            "check": None, "options": _units(qty_unit="pins"),
            "subtitle": "output per worker when the operations are divided",
            "rules": "Output per worker divided is the team's output over its workers; the team alone is the workers "
                     "times one worker's output alone; the multiple is per worker divided over alone, and when alone "
                     "is 0 no multiple is finite (Smith: perhaps not one). The extra output is the team's divided "
                     "output less its output alone. Operations per worker is the operations over the workers, exact. "
                     "Smith gives the figures of I.1 (ten workers, eighteen operations, upwards of 48,000 pins a day, "
                     "certainly not twenty alone); the lab takes the figures typed and says nothing of which of his "
                     "three causes accounts for the multiple.",
            "js": WDV_VIEW_JS["pins"],
        },
        "exchange": {
            "fields": [("goods", alist("The two goods (two names)", _N, lo=2, hi=2, things="goods"), None),
                       ("producers", arec("Producers (producer, hours available, hours a unit of the first good, hours a "
                                          "unit of the second)", [("producer", _N), ("hours", rat(gt=0)), ("a", rat(gt=0)),
                                                                  ("b", rat(gt=0))], unique=True, rows=2, lo=2, hi=2), None)],
            "tiles": [("Self-sufficient: each makes equal quantities of both", "wdvSelfEach"),
                      ("Self-sufficient totals", "wdvSelfTotal"), ("Specialised: who makes what", "wdvWho"),
                      ("Specialised totals", "wdvSpecTotal"), ("Gain in each good", "wdvGain"),
                      ("Who is better at what", "wdvCase")],
            "check": _check_exchange, "options": None,
            "subtitle": "two producers' output, self-sufficient and specialised",
            "rules": "Self-sufficient, each producer splits the hours to make equal quantities of both goods: "
                     "hours over (hours a unit of the first + hours a unit of the second). Specialised, each makes only "
                     "one good with all the hours: the producer whose relative cost of the first good (its hours a "
                     "unit over the second's) is the lower makes the first, the other makes the second. That "
                     "relative-cost rule is Ricardo's (1817), not Smith's; it agrees with Smith's case, where each "
                     "producer is better (fewer hours a unit) at one good, and it still divides the work when one "
                     "producer is better at both. Equal relative costs are refused: the rule then names no division. "
                     "A gain is specialised less self-sufficient, signed; it may be negative in one good. Every "
                     "figure is exact.",
            "js": WDV_VIEW_JS["exchange"],
        },
        "market": {
            "fields": [("places", arec("Places (place, demand a year)", [("place", _N), ("demand", rat(lo=0))],
                                       unique=True, rows=3, lo=1, hi=12), None),
                       ("output", ea.field("One specialist's output a year", rat(gt=0)), None),
                       ("days", ea.field("Working days a year", ea.whole(1, 366)), "300")],
            "tiles": [("Specialists the demand keeps", "wdvKeeps"), ("Share of one specialist's year", "wdvYearShare"),
                      ("Where a full-time trade can live", "wdvLive"), ("One specialist's output a day", "wdvPerDay")],
            "check": None, "options": _units(qty_unit="units"),
            "subtitle": "how many specialists a market of a given size can keep",
            "rules": "The specialists a place keeps is its demand a year over one specialist's output a year, rounded "
                     "down to a whole number (the lab's rule: a part of a year's work does not keep a person at the "
                     "trade). The share is the same quotient, exact, and may pass 100%. A full-time trade can live "
                     "where it keeps at least one specialist; Smith's rule (I.3) is that the division of labour is "
                     "limited by the extent of the market. Output a day is the output a year over the working days. "
                     "Places are listed in the order given.",
            "js": WDV_VIEW_JS["market"],
        },
    },
}

# ---------------------------------------------------------------------------
# money (wmo): barter and a common measure, coin and its silver
# ---------------------------------------------------------------------------

WMO_JS = r"""
  var WMO_VIEW = {};
  function wmoCompute(view, inst, opts) { return eaRun(WMO_VIEW[view], inst, opts); }
  /* whole pence as pounds, shillings and pence: 744 -> £3 2s; otherwise the pence */
  function wmoLsd(r) {
    if (!Rint(r) || r.n <= 0n) return eaNum(r) + 'd';
    var n = r.n, l = n / 240n, s = (n % 240n) / 12n, d = n % 12n, out = [];
    if (l) out.push('£' + eaInt(l));
    if (s) out.push(String(s) + 's');
    if (d) out.push(String(d) + 'd');
    return eaNum(r) + 'd (' + out.join(' ') + ')';
  }
"""

WMO_VIEW_JS = {}

WMO_VIEW_JS["barter"] = r"""
  WMO_VIEW.barter = function (inst) {
    var G = inst.goods, n = BigInt(G.length), T = inst.traders;
    T.forEach(function (t, i) {
      var w = 'Traders, record ' + (i + 1) + ' (' + t.trader + ')';
      if (G.indexOf(t.has) < 0) eaRefuse(w + ': ' + t.has + ' is not one of the goods');
      if (G.indexOf(t.wants) < 0) eaRefuse(w + ': ' + t.wants + ' is not one of the goods');
      if (t.has === t.wants) eaRefuse(w + ' has and wants the same good, ' + t.has);
    });
    var without = n * (n - 1n) / 2n, wth = n - 1n, pairs = [], inPair = {};
    T.forEach(function (x, i) {
      T.forEach(function (y, j) {
        if (j > i && x.has === y.wants && y.has === x.wants) { pairs.push(x.trader + '–' + y.trader); inPair[x.trader] = true; inPair[y.trader] = true; }
      });
    });
    var wanted = function (x) { return T.some(function (y) { return y !== x && y.wants === x.has; }); };
    var viaMoney = T.filter(function (x) { return !inPair[x.trader] && wanted(x); }).map(function (x) { return x.trader; });
    var noBuyer = T.filter(function (x) { return !wanted(x); }).map(function (x) { return x.trader; });
    var none = 'no traders given';
    return {
      tiles: {
        wmoWithout: eaPlural(without, 'ratio', 'ratios'), wmoWith: eaPlural(wth, 'price', 'prices'),
        wmoFewer: eaPlural(without - wth, 'quotation', 'quotations') + ' fewer',
        wmoDirect: T.length ? aktListed(pairs.length, pairs) : none,
        wmoViaMoney: T.length ? aktListed(viaMoney.length, viaMoney) : none,
        wmoNoBuyer: T.length ? aktListed(noBuyer.length, noBuyer) : none
      },
      status: wnkStatus(eaPlural(n, 'good', 'goods') + ' need ' + eaPlural(without, 'exchange ratio', 'exchange ratios') + ' without money and '
        + eaPlural(wth, 'price', 'prices') + ' in a common measure' + (T.length ? '; ' + eaPlural(pairs.length, 'pair of traders', 'pairs of traders') + ' can trade directly' : '')),
      table: T.length ? { caption: 'Each trader: what they have, what they want, and how they can trade',
                          head: ['trader', 'has', 'wants', 'someone wants theirs', 'trades directly'],
                          rows: T.map(function (x) { return [x.trader, x.has, x.wants, wanted(x) ? 'yes' : 'no', inPair[x.trader] ? 'yes' : 'no']; }) } : null
    };
  };
"""

WMO_VIEW_JS["coin"] = r"""
  WMO_VIEW.coin = function (inst) {
    var P = inst.periods, f = P[0], c1 = f.coined, sum = inst.sum, has = sum !== '-', last = P[P.length - 1];
    var list = function (g) { return P.map(function (p) { return p.period + ' ' + g(p); }).join('; '); };
    var lost = function (p) { return Rsub(R1, Rdiv(c1, p.coined)); };
    var later = P.slice(1);
    var lossText = function (p) {
      var l = lost(p);
      if (Rzero(l)) return p.period + ' no loss';
      if (l.n < 0n) return p.period + ' gains ' + eaPct(Rneg(l)) + ' more silver';
      return p.period + ' ' + eaPct(l) + ' of the silver';
    };
    return {
      tiles: {
        wmoSilver: list(function (p) { return eaPct(Rdiv(c1, p.coined)); }),
        wmoPound: list(function (p) { return wmoLsd(Rdiv(Rmul(R(240n), p.coined), c1)); }),
        wmoSumSilver: has ? list(function (p) { return wmoUnit(Rdiv(sum, p.coined), 'lb') + ' silver'; }) : 'no sum given',
        wmoLoss: later.length ? later.map(lossText).join('; ') : 'one period only',
        wmoLossSum: !has ? 'no sum given' : (later.length ? later.map(function (p) { var x = Rmul(sum, lost(p)); return p.period + ' ' + (Rzero(x) ? 'no loss' : (x.n > 0n ? eaNum(x) + 'd lost' : eaNum(Rneg(x)) + 'd gained')) + ', in ' + f.period + '’s pence'; }).join('; ') : 'one period only')
      },
      status: wnkStatus(later.length ? 'From ' + f.period + ' to ' + last.period + ' a penny comes to hold ' + eaPct(Rdiv(c1, last.coined)) + ' of its silver, and '
        + f.period + '’s pound is ' + wmoLsd(Rdiv(Rmul(R(240n), last.coined), c1)) + ' in ' + last.period + '’s pence' : f.period + ': ' + eaNum(c1) + ' pence to a pound weight of silver'),
      table: { caption: 'Each period: pence coined from a pound weight of silver, and the silver in a penny',
               head: ['period', 'pence coined', 'silver in a penny (lb)', 'against ' + f.period].concat(has ? ['silver in the sum (lb)'] : []),
               rows: P.map(function (p) { return [p.period, eaNum(p.coined), eaFrac(Rinv(p.coined)), eaPct(Rdiv(c1, p.coined))].concat(has ? [eaNum(Rdiv(sum, p.coined))] : []); }) }
    };
  };
"""


def _check_barter(inst, fixed):
    goods = inst["goods"]
    for i, t in enumerate(inst["traders"]):
        w = "Traders, record %d (%s)" % (i + 1, t["trader"])
        if t["has"] not in goods:
            raise ValueError("%s: %s is not one of the goods" % (w, t["has"]))
        if t["wants"] not in goods:
            raise ValueError("%s: %s is not one of the goods" % (w, t["wants"]))
        if t["has"] == t["wants"]:
            raise ValueError("%s has and wants the same good, %s" % (w, t["has"]))


MONEY = {
    "prefix": "wmo", "fn": "wmoCompute", "title": "Money", "js": _js("wmo", WMO_JS),
    "views": {
        "barter": {
            "fields": [("goods", alist("Goods (2 to 12 names)", _N, lo=2, hi=12, things="goods"), None),
                       ("traders", arec("Traders (trader, has, wants; empty for none)",
                                        [("trader", _N), ("has", _N), ("wants", _N)], unique=True, rows=3, lo=0, hi=12), "")],
            "tiles": [("Ratios to quote without money", "wmoWithout"), ("Prices to quote in a common measure", "wmoWith"),
                      ("Quotations saved", "wmoFewer"), ("Pairs who can trade directly", "wmoDirect"),
                      ("Traders who can trade only through a money", "wmoViaMoney"),
                      ("Traders whose good no other trader wants", "wmoNoBuyer")],
            "check": _check_barter, "options": None,
            "subtitle": "exchange ratios without money and with a common measure",
            "rules": "Without money every pair of n goods needs its own ratio, n(n − 1)/2; with a common measure each "
                     "good needs one price, n − 1 (the measure itself needs none). Two traders can trade directly when "
                     "each has what the other wants (Smith's want of a double coincidence, I.4). A trader can trade only "
                     "through a money when another trader wants their good but no direct pair includes them; a trader "
                     "whose good no other trader wants has no buyer among those listed. The trader lists are the "
                     "lab's reading of Smith's butcher, brewer and baker. Traders are listed in the order given.",
            "js": WMO_VIEW_JS["barter"],
        },
        "coin": {
            "fields": [("periods", arec("Periods (period, pence coined from a pound weight of silver)",
                                        [("period", _N), ("coined", rat(gt=0))], unique=True, rows=3, lo=1, hi=12), None),
                       ("sum", ea.field("A fixed sum in pence (- for none)", rat(gt=0, dash=True)), "-")],
            "tiles": [("Silver in a penny, against the first period", "wmoSilver"),
                      ("The first period's pound (240 of its pence) in each period's pence", "wmoPound"),
                      ("Silver in the fixed sum", "wmoSumSilver"),
                      ("Silver a creditor loses when paid the same sum, against the first period", "wmoLoss"),
                      ("The creditor's loss in the first period's pence", "wmoLossSum")],
            "check": None, "options": None,
            "subtitle": "the silver in a penny as the pound is debased",
            "rules": "A penny holds 1/coined of a pound weight of silver, so against the first period it holds "
                     "(first coined)/(this coined). The first period's pound is 240 of its pence; its silver, in a "
                     "later period's pence, is 240 × (this coined)/(first coined), shown also in pounds, shillings and "
                     "pence when whole. A fixed sum holds sum/coined pounds weight of silver. A creditor owed the sum "
                     "in the first period's coin and paid the same sum later loses 1 − (first coined)/(later coined) "
                     "of the silver (a gain when fewer pence are coined later); the loss in the first period's pence "
                     "is the sum times that share. Smith gives the rule (I.4, I.5) and figures such as 240 and 744 "
                     "pence from the pound weight. Periods are compared with the first given.",
            "js": WMO_VIEW_JS["coin"],
        },
    },
}

# ---------------------------------------------------------------------------
# price (wpr): real and nominal price, the component parts, market price
# ---------------------------------------------------------------------------

WPR_JS = r"""
  var WPR_VIEW = {};
  function wprCompute(view, inst, opts) { return eaRun(WPR_VIEW[view], inst, opts); }
"""

WPR_VIEW_JS = {}

WPR_VIEW_JS["real"] = r"""
  WPR_VIEW.real = function (inst, o) {
    var Y = inst.years, mu = o.measure_unit, m = o.money_unit, f = Y[0], l = Y[Y.length - 1];
    var real = function (y) { return Rdiv(y.price, y.measure); };
    var chMoney = Rdiv(Rsub(l.price, f.price), f.price), chReal = Rdiv(Rsub(real(l), real(f)), real(f));
    var wm = wprWay(chMoney), wr = wprWay(chReal);
    var way = wm === wr ? 'the same way: both ' + wm : 'not the same way: the money price ' + wm + ' and the real price ' + wr;
    return {
      tiles: {
        wprReal: Y.map(function (y) { return y.year + ' ' + wprUnit(real(y), mu); }).join('; '),
        wprMoneyCh: f.year + ' → ' + l.year + ': ' + wprCh(chMoney),
        wprRealCh: f.year + ' → ' + l.year + ': ' + wprCh(chReal),
        wprWay: way
      },
      status: wnkStatus('From ' + f.year + ' to ' + l.year + ' the money price ' + wm + ' (' + wprCh(chMoney) + ') and the real price, in ' + mu + ', ' + wr + ' (' + wprCh(chReal) + ')'),
      table: { caption: 'Each year: the money price, the money price of the measure, and the real price in ' + mu,
               head: ['year', 'money price', 'price of the measure', 'real price (' + mu + ')'],
               rows: Y.map(function (y) { return [y.year, wprMoney(y.price, m), wprMoney(y.measure, m), eaNum(real(y))]; }) }
    };
  };
"""

WPR_VIEW_JS["parts"] = r"""
  function wprRun(st, wf, pts) {
    var p = R0, W = R0, Rn = R0, Pr = R0, after = [], adv = [];
    st.forEach(function (s) {
      var w = Rmul(s.wages, wf), a = Radd(Radd(p, w), s.rent), pr = Rmul(a, Rdiv(Radd(s.rate, pts), R(100n)));
      W = Radd(W, w); Rn = Radd(Rn, s.rent); Pr = Radd(Pr, pr); p = Radd(a, pr); after.push(p); adv.push(a);
    });
    return { p: p, W: W, Rn: Rn, Pr: Pr, after: after, adv: adv };
  }
  WPR_VIEW.parts = function (inst, o) {
    var m = o.money_unit, st = inst.stages, wr = inst.wage_rise, pr = inst.profit_rise;
    var wf = Radd(R1, Rdiv(wr, R(100n))), base = wprRun(st, R1, R0);
    if (Rzero(base.p)) eaRefuse('Every stage’s wages and rent are 0, so there is no price to resolve');
    var M = function (r) { return wprMoney(r, m); }, S = function (r) { return wprMoney(r, m, true); };
    var rise = function (r, extra) { var d = Rsub(r.p, base.p); return M(base.p) + ' → ' + M(r.p) + ': ' + S(d) + ' (' + wprCh(Rdiv(d, base.p)) + ')' + extra; };
    var rW = Rzero(wr) ? null : wprRun(st, wf, R0), rP = Rzero(pr) ? null : wprRun(st, R1, pr), rB = rW && rP ? wprRun(st, wf, pr) : null;
    var direct = Rmul(eaSum(base.adv), Rdiv(pr, R(100n)));
    var say = 'The final price is ' + M(base.p) + ': wages ' + eaPct(Rdiv(base.W, base.p)) + ', rent ' + eaPct(Rdiv(base.Rn, base.p)) + ', profit ' + eaPct(Rdiv(base.Pr, base.p));
    if (rW) say += '; a wage rise of ' + wprRate(wr) + ' adds ' + M(Rsub(rW.p, base.p));
    if (rP) say += (rW ? ' and ' : '; ') + 'a profit rise of ' + aktDec(pr) + ' points adds ' + M(Rsub(rP.p, base.p));
    return {
      tiles: {
        wprStages: st.map(function (s, i) { return s.stage + ' ' + M(base.after[i]); }).join('; '),
        wprFinal: M(base.p),
        wprResolved: 'wages ' + M(base.W) + ', rent ' + M(base.Rn) + ', profit ' + M(base.Pr),
        wprShares: 'wages ' + eaPct(Rdiv(base.W, base.p)) + '; rent ' + eaPct(Rdiv(base.Rn, base.p)) + '; profit ' + eaPct(Rdiv(base.Pr, base.p)),
        wprWageRise: rW ? rise(rW, '; wages paid ' + S(Rsub(rW.W, base.W))) : 'no wage rise given',
        wprProfitRise: rP ? rise(rP, '; profit on the old advances ' + S(direct)) : 'no profit rise given',
        wprBothRise: rB ? rise(rB, '') : 'give both rises to combine them'
      },
      status: wnkStatus(say),
      table: { caption: 'Each stage: what is advanced (the last price, wages and rent), the profit on it, and the price after',
               head: ['stage', 'wages', 'rent', 'profit rate', 'advanced', 'profit', 'price after'].concat(rW ? ['after the wage rise'] : []).concat(rP ? ['after the profit rise'] : []),
               rows: st.map(function (s, i) {
                 return [s.stage, M(s.wages), M(s.rent), wprRate(s.rate), M(base.adv[i]), M(Rsub(base.after[i], base.adv[i])), M(base.after[i])]
                   .concat(rW ? [M(rW.after[i])] : []).concat(rP ? [M(rP.after[i])] : []);
               }) }
    };
  };
"""

WPR_VIEW_JS["market"] = r"""
  WPR_VIEW.market = function (inst, o) {
    var m = o.money_unit, u = o.qty_unit, nat = inst.natural, eff = inst.effectual, br = inst.brought;
    var B = inst.buyers.slice().sort(function (a, b) { return Rcmp(a.price, b.price); });
    inst.buyers.forEach(function (x, i) {
      inst.buyers.forEach(function (y, j) { if (j < i && Requ(x.price, y.price)) eaRefuse('Buyers, record ' + (i + 1) + ': the price ' + eaNum(x.price) + ' is listed twice'); });
    });
    B.forEach(function (x, k) {
      if (k > 0 && Rcmp(x.quantity, B[k - 1].quantity) > 0) eaRefuse('Buyers: at the price ' + eaNum(x.price) + ' buyers take ' + eaNum(x.quantity) + ', more than the ' + eaNum(B[k - 1].quantity) + ' they take at the lower price ' + eaNum(B[k - 1].price) + '; quantities must not increase as the price rises');
    });
    var c = Rcmp(br, eff), pos, gap, mp = null, mtxt, ug, tg;
    if (c < 0) { pos = 'above the natural price: less is brought (' + eaNum(br) + ') than the effectual demand (' + eaNum(eff) + ')'; gap = 'shortfall of ' + wprUnit(Rsub(eff, br), u); }
    else if (c > 0) { pos = 'below the natural price: more is brought (' + eaNum(br) + ') than the effectual demand (' + eaNum(eff) + ')'; gap = 'excess of ' + wprUnit(Rsub(br, eff), u); }
    else { pos = 'at the natural price: the quantity brought equals the effectual demand (' + eaNum(eff) + ')'; gap = 'none'; }
    if (B.length === 0) { mtxt = 'no schedule given'; ug = mtxt; tg = mtxt; }
    else {
      B.forEach(function (x) { if (Rcmp(x.quantity, br) >= 0) mp = x.price; });
      if (mp === null) { mtxt = 'no listed price: at every listed price buyers take less than the ' + eaNum(br) + ' brought'; ug = 'no market price'; tg = ug; }
      else {
        var d = Rsub(mp, nat);
        mtxt = wprMoney(mp, m) + ' a unit';
        ug = wprMoney(d, m, true) + ' a unit ' + (d.n > 0n ? 'above' : (d.n < 0n ? 'below' : 'at')) + ' the natural price';
        tg = wprMoney(Rmul(d, br), m, true) + ' over the ' + wprUnit(br, u) + ' brought';
      }
    }
    return {
      tiles: { wprPosition: pos, wprGap: gap, wprMarketPrice: mtxt, wprUnitGap: ug, wprAllGap: tg },
      status: wnkStatus('With ' + wprUnit(br, u) + ' brought against an effectual demand of ' + eaNum(eff) + ', the price is ' + pos.split(':')[0]
        + (mp !== null ? '; the schedule clears at ' + wprMoney(mp, m) + ' against a natural price of ' + wprMoney(nat, m) : '')),
      table: B.length ? { caption: 'The buyers’ schedule, lowest price first, against the quantity brought',
                          head: ['price', 'buyers take', 'takes at least the quantity brought'],
                          rows: B.map(function (x) { return [wprMoney(x.price, m), eaNum(x.quantity), Rcmp(x.quantity, br) >= 0 ? 'yes' : 'no']; }) } : null
    };
  };
"""


def _check_parts(inst, fixed):
    if all(s["wages"] == 0 and s["rent"] == 0 for s in inst["stages"]):
        raise ValueError("Every stage’s wages and rent are 0, so there is no price to resolve")


def _check_market(inst, fixed):
    buyers = inst["buyers"]
    for i, x in enumerate(buyers):
        if any(y["price"] == x["price"] for y in buyers[:i]):
            raise ValueError("Buyers, record %d: the price %s is listed twice" % (i + 1, _n(x["price"])))
    s = sorted(buyers, key=lambda x: x["price"])
    for k in range(1, len(s)):
        if s[k]["quantity"] > s[k - 1]["quantity"]:
            raise ValueError("Buyers: at the price %s buyers take %s, more than the %s they take at the lower price %s; "
                             "quantities must not increase as the price rises"
                             % (_n(s[k]["price"]), _n(s[k]["quantity"]), _n(s[k - 1]["quantity"]), _n(s[k - 1]["price"])))


PRICE = {
    "prefix": "wpr", "fn": "wprCompute", "title": "Price", "js": _js("wpr", WPR_JS),
    "views": {
        "real": {
            "fields": [("years", arec("Years (year, money price of the good, money price of the measure)",
                                      [("year", _N), ("price", rat(gt=0)), ("measure", rat(gt=0))],
                                      unique=True, rows=3, lo=2, hi=12), None)],
            "tiles": [("Real price each year, in the measure", "wprReal"), ("Change in the money price", "wprMoneyCh"),
                      ("Change in the real price", "wprRealCh"), ("Did they move the same way?", "wprWay")],
            "check": None, "options": _money(measure_unit="days of labour"),
            "subtitle": "a price in money against a price in labour or in corn",
            "rules": "The real price in a year is the money price of the good over the money price of the measure (a "
                     "day's labour, or a quarter of corn): how much of the measure the good commands. Smith gives the "
                     "rule (I.5): labour is the real measure, money the nominal one. A change is last less first over "
                     "first, exact, signed; first and last are the first and last years given, in the order given. "
                     "Each moved the same way when both rose, both fell or both held.",
            "js": WPR_VIEW_JS["real"],
        },
        "parts": {
            "fields": [("stages", arec("Stages (stage, wages paid, rent paid, profit rate % on everything advanced)",
                                       [("stage", _N), ("wages", rat(lo=0)), ("rent", rat(lo=0)), ("rate", rat(lo=0, hi=1000))],
                                       unique=True, rows=3, lo=1, hi=12), None),
                       ("wage_rise", ea.field("A rise of wages, % (0 for none)", rat(lo=0, hi=1000)), "0"),
                       ("profit_rise", ea.field("A rise of profit, points added to every rate (0 for none)", rat(lo=0, hi=1000)), "0")],
            "tiles": [("Price after each stage", "wprStages"), ("Final price", "wprFinal"),
                      ("Resolved into wages, rent and profit", "wprResolved"), ("Shares of the final price", "wprShares"),
                      ("With the wage rise", "wprWageRise"), ("With the profit rise", "wprProfitRise"),
                      ("With both rises", "wprBothRise")],
            "check": _check_parts, "options": _money(),
            "subtitle": "a price resolved into wages, profit and rent through the stages of production",
            "rules": "At each stage the undertaker advances the price of what the last stage sold, the wages and the "
                     "rent, and takes the profit rate on all of it: price after = (previous price + wages + rent) × "
                     "(1 + rate/100), starting from nothing. The final price is then exactly the sum of all the wages, "
                     "rents and profits paid at every stage (Smith, I.6: every price resolves into the three). A wage "
                     "rise multiplies every stage's wages by (1 + rise/100); a profit rise adds its points to every "
                     "stage's rate. Each is worked through all the stages again. A wage rise adds the extra wages and "
                     "the profit charged on them; a profit rise is charged on prices that already carry profit, so it "
                     "compounds: compare the price's rise with the profit on the old advances (Smith, I.9: like "
                     "compound interest against simple). Stages run in the order given.",
            "js": WPR_VIEW_JS["parts"],
        },
        "market": {
            "fields": [("natural", ea.field("Natural price a unit", rat(gt=0)), None),
                       ("effectual", ea.field("Effectual demand (units at the natural price)", rat(gt=0)), None),
                       ("brought", ea.field("Units brought to market", rat(lo=0)), None),
                       ("buyers", arec("Buyers' schedule (price, quantity buyers take at it; empty for none)",
                                       [("price", rat(gt=0)), ("quantity", rat(lo=0))], rows=3, lo=0, hi=12), "")],
            "tiles": [("Market price against the natural price", "wprPosition"), ("Shortfall or excess", "wprGap"),
                      ("Market price from the schedule", "wprMarketPrice"), ("Its gap to the natural price", "wprUnitGap"),
                      ("The gap over the quantity brought", "wprAllGap")],
            "check": _check_market, "options": _money(qty_unit="units"),
            "subtitle": "the market price against the natural price",
            "rules": "Smith's rule (I.7): when less is brought to market than the effectual demand the market price "
                     "rises above the natural price, when more it sinks below, and when the two are equal it is the "
                     "natural price; the lab says which, from brought against effectual. The schedule is the lesson's, "
                     "never Smith's: buyers' quantities must not increase as the price rises (a price listed twice is "
                     "refused). The market price is the highest listed price at which buyers take at least the "
                     "quantity brought (the lab's rule, not Smith's); when none does, there is no market price on the "
                     "schedule. Its gap is the market price less the natural price, a unit and over the quantity "
                     "brought.",
            "js": WPR_VIEW_JS["market"],
        },
    },
}

# ---------------------------------------------------------------------------
# wages (wwg): subsistence, the funds for maintaining labour, population
# ---------------------------------------------------------------------------

WWG_JS = r"""
  var WWG_VIEW = {};
  function wwgCompute(view, inst, opts) { return eaRun(WWG_VIEW[view], inst, opts); }
  function wwgAgainst(wage, need, M) {
    var d = Rsub(wage, need);
    return d.n > 0n ? 'covers it, with ' + M(d) + ' over' : (d.n < 0n ? 'falls short by ' + M(Rneg(d)) : 'exactly covers it');
  }
"""

WWG_VIEW_JS = {}

WWG_VIEW_JS["subsistence"] = r"""
  WWG_VIEW.subsistence = function (inst, o) {
    var m = o.money_unit, per = ' a ' + o.period, M = function (r) { return wwgMoney(r, m); };
    var fam = eaSum(inst.items.map(function (x) { return x.cost; })), mt = inst.maintenance, has = mt !== '-';
    var min = has ? Rmul(mt, inst.multiple) : null;
    return {
      tiles: {
        wwgFamily: M(fam) + per, wwgCover: wwgAgainst(inst.wage, fam, M),
        wwgMinimum: has ? M(min) + per + ' (' + eaNum(inst.multiple) + ' × ' + M(mt) + ')' : 'no maintenance given',
        wwgCoverMin: has ? wwgAgainst(inst.wage, min, M) : 'no maintenance given'
      },
      status: wnkStatus('A wage of ' + M(inst.wage) + per + ' against a family’s needs of ' + M(fam) + ': it ' + wwgAgainst(inst.wage, fam, M)
        + (has ? '; against ' + eaNum(inst.multiple) + ' × the worker’s own maintenance, it ' + wwgAgainst(inst.wage, min, M) : '')),
      table: { caption: 'The family’s needs' + per, head: ['item', 'cost'],
               rows: inst.items.map(function (x) { return [x.item, M(x.cost)]; }).concat([['total', M(fam)]]) }
    };
  };
"""

WWG_VIEW_JS["fund"] = r"""
  WWG_VIEW.fund = function (inst, o) {
    var m = o.money_unit, M = function (r) { return wwgMoney(r, m); };
    var gf = Radd(R1, Rdiv(inst.fund_growth, R(100n))), gw = Radd(R1, Rdiv(inst.worker_growth, R(100n))), Y = eaWhole(inst.years);
    var F = inst.fund, N = inst.workers, rows = [], t;
    for (t = 0; t <= Y; t += 1) {
      rows.push([String(t), M(F), wwgTwo(N), M(Rdiv(F, N))]);
      if (t < Y) { F = Rmul(F, gf); N = Rmul(N, gw); }
    }
    var w0 = Rdiv(inst.fund, inst.workers), w1 = Rdiv(F, N), k = Rdiv(gf, gw), c = Rcmp(k, R1);
    var trend = c > 0 ? 'rises every year: the fund grows faster than the workers' : (c < 0 ? 'falls every year: the workers grow faster than the fund' : 'holds: the fund and the workers grow at the same rate');
    return {
      tiles: {
        wwgWageFirst: M(w0) + ' a worker', wwgWageLast: M(w1) + ' a worker (year ' + Y + ')',
        wwgTrend: 'the wage ' + trend, wwgFactor: eaNum(k) + ' a year',
        wwgFundLast: M(F), wwgWorkersLast: wwgTwo(N)
      },
      status: wnkStatus(Y === 0 ? 'In year 0 the wage is ' + M(w0) + ' a worker; at these rates it ' + trend.split(':')[0].replace(' every year', ' each year')
        : 'Over ' + eaPlural(BigInt(Y), 'year', 'years') + ' the wage goes from ' + M(w0) + ' to ' + M(w1) + ' a worker: it ' + trend.split(':')[0]),
      table: { caption: 'Each year: the fund, the workers (a rate of population, not rounded) and the wage = fund / workers',
               head: ['year', 'fund', 'workers', 'wage'], rows: rows }
    };
  };
"""

WWG_VIEW_JS["growth"] = r"""
  WWG_VIEW.growth = function (inst) {
    var y = inst.years.n, d = inst.doubling.n, d2 = inst.doubling2.n;
    if (y % d !== 0n) eaRefuse('The years (' + eaInt(y) + ') are not a whole number of doublings of ' + eaInt(d) + ' years; a part of a doubling needs a root, which the lab does not take');
    if (d2 > 0n && y % d2 !== 0n) eaRefuse('The years (' + eaInt(y) + ') are not a whole number of doublings of ' + eaInt(d2) + ' years (the second doubling time); a part of a doubling needs a root, which the lab does not take');
    var k = y / d, f = R(2n ** k), after = Rmul(inst.population, f), cmp = 'no second doubling time given';
    if (d2 > 0n) {
      var k2 = y / d2, f2 = R(2n ** k2);
      cmp = 'in ' + eaPlural(y, 'year', 'years') + ': every ' + eaInt(d) + ' years ' + wwgX(f) + ', every ' + eaInt(d2) + ' years ' + wwgX(f2)
        + ' (' + eaNum(Rmul(inst.population, f2)) + '); the second ends ' + wwgX(Rdiv(f2, f)) + ' the first';
    }
    return {
      tiles: { wwgDoublings: eaInt(k), wwgAfter: eaNum(after), wwgTimes: wwgX(f), wwgCompare: cmp },
      status: wnkStatus('Doubling every ' + eaPlural(d, 'year', 'years') + ', a population of ' + eaNum(inst.population) + ' doubles ' + eaPlural(k, 'time', 'times') + ' in ' + eaPlural(y, 'year', 'years') + ' and ends at ' + eaNum(after)),
      table: null
    };
  };
"""


def _check_growth(inst, fixed):
    y, d, d2 = int(inst["years"]), int(inst["doubling"]), int(inst["doubling2"])
    if y % d:
        raise ValueError("The years (%s) are not a whole number of doublings of %s years; a part of a doubling needs a "
                         "root, which the lab does not take" % (ea.grp(y), ea.grp(d)))
    if d2 and y % d2:
        raise ValueError("The years (%s) are not a whole number of doublings of %s years (the second doubling time); a "
                         "part of a doubling needs a root, which the lab does not take" % (ea.grp(y), ea.grp(d2)))


WAGES = {
    "prefix": "wwg", "fn": "wwgCompute", "title": "Wages", "js": _js("wwg", WWG_JS),
    "views": {
        "subsistence": {
            "fields": [("items", arec("A family's needs (item, cost each period)", [("item", _N), ("cost", rat(lo=0))],
                                      unique=True, rows=4, lo=1, hi=12), None),
                       ("wage", ea.field("The wage each period", rat(lo=0)), None),
                       ("maintenance", ea.field("The worker's own maintenance each period (- for none)", rat(gt=0, dash=True)), "-"),
                       ("multiple", ea.field("Multiple of the worker's own maintenance", rat(gt=0, hi=100)), "2")],
            "tiles": [("Family subsistence", "wwgFamily"), ("The wage against it", "wwgCover"),
                      ("Maintenance × multiple", "wwgMinimum"), ("The wage against that minimum", "wwgCoverMin")],
            "check": None, "options": _money(period="week"),
            "subtitle": "a family's subsistence against a wage",
            "rules": "The family's subsistence is the sum of its needs each period. The wage covers it when it is at "
                     "least the sum; the lab says by how much it is over or short. With the worker's own maintenance, "
                     "the minimum is that maintenance times the multiple: Smith (I.8) reports Cantillon's double the "
                     "labourer's own maintenance, so that two working parents can bring up two children; the multiple "
                     "is the lesson's to state. The needs and the wage are the lesson's figures.",
            "js": WWG_VIEW_JS["subsistence"],
        },
        "fund": {
            "fields": [("fund", ea.field("Funds destined for maintaining labour, a year", rat(gt=0)), None),
                       ("workers", ea.field("Workers", rat(gt=0)), None),
                       ("fund_growth", ea.field("Growth of the fund, % a year (may be negative)", rat(gt=-100, hi=1000)), "0"),
                       ("worker_growth", ea.field("Growth of the workers, % a year (may be negative)", rat(gt=-100, hi=1000)), "0"),
                       ("years", ea.field("Years", ea.whole(0, 50)), "10")],
            "tiles": [("Wage in the first year", "wwgWageFirst"), ("Wage in the last year", "wwgWageLast"),
                      ("Does the wage rise, hold or fall?", "wwgTrend"), ("The wage's factor each year", "wwgFactor"),
                      ("The fund in the last year", "wwgFundLast"), ("Workers in the last year", "wwgWorkersLast")],
            "check": None, "options": _money(),
            "subtitle": "the wage when the fund and the workers grow at stated rates",
            "rules": "Each year the fund is multiplied by (1 + its growth/100) and the workers by (1 + theirs/100), "
                     "exactly, by repeated multiplication; the wage is the fund over the workers. The workers are not "
                     "rounded: they stand for a rate of population, not a head count. The wage's factor each year is "
                     "(1 + fund growth/100)/(1 + worker growth/100), so the wage rises when the fund grows faster than "
                     "the workers, whatever the fund's size: Smith's rule (I.8) that wages follow the increase of the "
                     "funds, not their greatness. Year 0 is the first year. Money and workers not exact at two places "
                     "are shown to two with ≈.",
            "js": WWG_VIEW_JS["fund"],
        },
        "growth": {
            "fields": [("population", ea.field("Population", ea.whole(1, LIMIT)), None),
                       ("doubling", ea.field("Doubling time, years", ea.whole(1, 200)), "25"),
                       ("years", ea.field("Years (a whole number of doublings)", ea.whole(0, 200)), "100"),
                       ("doubling2", ea.field("A second doubling time to compare, years (0 for none)", ea.whole(0, 200)), "0")],
            "tiles": [("Doublings", "wwgDoublings"), ("Population after", "wwgAfter"), ("The factor", "wwgTimes"),
                      ("The two doubling times compared", "wwgCompare")],
            "check": _check_growth, "options": None,
            "subtitle": "population doubling in a stated number of years",
            "rules": "Doublings are the years over the doubling time; the population after is the population times 2 "
                     "to that power, exactly. The years must be a whole number of doublings (of both doubling times "
                     "when two are given): a part of a doubling needs a root, which the lab does not take, and it "
                     "refuses with that reason. Smith (I.8) reports doubling in twenty or five-and-twenty years in "
                     "the North American colonies; the population is the lesson's. With a second doubling time the "
                     "two factors and the ratio of the second to the first are shown.",
            "js": WWG_VIEW_JS["growth"],
        },
    },
}

# ---------------------------------------------------------------------------
# advantage (wad): net advantages, the lottery of a profession, profit
# ---------------------------------------------------------------------------

WAD_JS = r"""
  var WAD_VIEW = {};
  function wadCompute(view, inst, opts) { return eaRun(WAD_VIEW[view], inst, opts); }
"""

WAD_VIEW_JS = {}

WAD_VIEW_JS["net"] = r"""
  WAD_VIEW.net = function (inst, o) {
    var m = o.money_unit, M = function (r) { return wadMoney(r, m); }, E = inst.employments, pf = Rdiv(inst.profit, R(100n));
    var names = E.map(function (e) { return e.employment; });
    inst.limit.forEach(function (l, i) {
      if (names.indexOf(l.employment) < 0) eaRefuse('Limits, record ' + (i + 1) + ': ' + l.employment + ' is not one of the employments');
    });
    var cap = {};
    inst.limit.forEach(function (l) { cap[l.employment] = l; });
    var row = function (e, wage) {
      var yr = Rmul(wage, e.days), learn = Radd(Rdiv(e.learning, e.years), Rmul(e.learning, pf));
      return { name: e.employment, wage: wage, yr: yr, learn: learn, net: Radd(Rsub(yr, learn), e.other) };
    };
    var rank = function (L) {
      var s = L.slice().sort(function (a, b) { return Rcmp(b.net, a.net); }), out = s[0].name, k;
      for (k = 1; k < s.length; k += 1) out += (Requ(s[k].net, s[k - 1].net) ? ' = ' : ' > ') + s[k].name;
      return { text: out, top: s[0], bottom: s[s.length - 1] };
    };
    var A = E.map(function (e) { return row(e, e.wage); });
    var B = E.map(function (e) { return cap[e.employment] ? row(e, Rmul(e.wage, Radd(R1, Rdiv(cap[e.employment].pay_rise, R(100n))))) : row(e, e.wage); });
    var list = function (L, f) { return L.map(function (x) { return x.name + ' ' + f(x); }).join('; '); };
    var r = rank(A), d = Rsub(r.top.net, r.bottom.net), hasCap = inst.limit.length > 0;
    var spread = A.length === 1 ? 'one employment only' : (Rzero(d) ? M(d) + ': every employment nets the same' : M(d) + ' (' + r.top.name + ' over ' + r.bottom.name + ')');
    return {
      tiles: {
        wadAnnual: list(A, function (x) { return M(x.yr); }), wadLearnYear: list(A, function (x) { return M(x.learn); }),
        wadNet: list(A, function (x) { return M(x.net); }), wadRank: r.text, wadSpread: spread,
        wadLimited: hasCap ? inst.limit.map(function (l) { var i = names.indexOf(l.employment); return l.employment + ' (entry capped at ' + eaNum(l.entrants) + '): wage ' + M(A[i].wage) + ' → ' + M(B[i].wage) + ' a day, net ' + M(A[i].net) + ' → ' + M(B[i].net); }).join('; ') : 'no limit given',
        wadRankAfter: hasCap ? rank(B).text : 'no limit given'
      },
      status: wnkStatus('Net advantage a year: ' + list(A, function (x) { return M(x.net); }) + (A.length > 1 ? '; the spread is ' + spread : '')),
      table: { caption: 'Each employment a year: the money wage, the cost of learning replaced, the other advantages, and the net',
               head: ['employment', 'wage a day', 'days', 'money wage a year', 'learning replaced a year', 'other', 'net advantage'].concat(hasCap ? ['net with the limit'] : []),
               rows: E.map(function (e, i) { return [e.employment, M(e.wage), eaNum(e.days), M(A[i].yr), M(A[i].learn), M(e.other, true), M(A[i].net)].concat(hasCap ? [M(B[i].net)] : []); }) }
    };
  };
"""

WAD_VIEW_JS["lottery"] = r"""
  WAD_VIEW.lottery = function (inst, o) {
    var m = o.money_unit, M = function (r) { return wadMoney(r, m); }, n = inst.entrants, s = inst.succeed;
    if (Rcmp(s, n) > 0) eaRefuse('The successful (' + eaNum(s) + ') cannot be more than the entrants (' + eaNum(n) + ')');
    var prizes = Rmul(Rmul(s, inst.prize), inst.years), cost = Rmul(n, inst.cost), d = Rsub(prizes, cost), fair;
    if (Rzero(cost)) fair = Rzero(prizes) ? 'fair: no prizes and no cost' : 'over: the tickets cost nothing';
    else if (Rzero(d)) fair = 'fair: the prizes exactly repay the tickets';
    else fair = (d.n < 0n ? 'short by ' + M(Rneg(d)) : 'over by ' + M(d)) + ': the prizes repay ' + eaPct(Rdiv(prizes, cost)) + ' of the tickets';
    var need = Rzero(s) ? 'no prize can repay the tickets: no one succeeds' : M(Rdiv(cost, Rmul(s, inst.years))) + ' a year (against ' + M(inst.prize) + ')';
    return {
      tiles: {
        wadChance: eaPct(Rdiv(s, n)), wadPrizes: M(prizes), wadTickets: M(cost),
        wadExpected: M(Rdiv(prizes, n)) + ' an entrant (against ' + M(inst.cost) + ' a ticket)', wadFair: fair, wadNeeded: need
      },
      status: wnkStatus(eaNum(s) + ' in ' + eaNum(n) + ' succeed: the prizes come to ' + M(prizes) + ' against ' + M(cost) + ' of tickets, ' + fair.split(':')[0]),
      table: null
    };
  };
"""

WAD_VIEW_JS["profit"] = r"""
  WAD_VIEW.profit = function (inst, o) {
    var m = o.money_unit, M = function (r) { return wadMoney(r, m, true); }, st = inst.stock === '-' ? inst.cost : inst.stock;
    var ap = Rsub(inst.sales, inst.cost), tr = Rsub(ap, inst.wages);
    return {
      tiles: {
        wadApparent: M(ap), wadApparentRate: wadCh(Rdiv(ap, st)) + ' on ' + wadMoney(st, m),
        wadTrue: M(tr), wadTrueRate: wadCh(Rdiv(tr, st)) + ' on ' + wadMoney(st, m),
        wadWageShare: ap.n > 0n ? eaPct(Rdiv(inst.wages, ap)) : 'no apparent profit to divide'
      },
      status: wnkStatus('The apparent profit is ' + M(ap) + ', ' + wadCh(Rdiv(ap, st)) + ' on the stock; less the wages of the trader’s labour, ' + M(tr) + ', ' + wadCh(Rdiv(tr, st))),
      table: null
    };
  };
"""


def _check_net(inst, fixed):
    names = [e["employment"] for e in inst["employments"]]
    for i, l in enumerate(inst["limit"]):
        if l["employment"] not in names:
            raise ValueError("Limits, record %d: %s is not one of the employments" % (i + 1, l["employment"]))


def _check_lottery(inst, fixed):
    if inst["succeed"] > inst["entrants"]:
        raise ValueError("The successful (%s) cannot be more than the entrants (%s)" % (_n(inst["succeed"]), _n(inst["entrants"])))


ADVANTAGE = {
    "prefix": "wad", "fn": "wadCompute", "title": "Advantages of employments", "js": _js("wad", WAD_JS),
    "views": {
        "net": {
            "fields": [("employments", arec("Employments (employment, wage a day, days a year, cost of learning, working "
                                            "years to replace it, other advantages a year, signed)",
                                            [("employment", _N), ("wage", rat(lo=0)), ("days", rat(lo=0, hi=366)),
                                             ("learning", rat(lo=0)), ("years", rat(gt=0, hi=100)), ("other", rat(lo=-LIMIT))],
                                            unique=True, rows=3, lo=1, hi=12), None),
                       ("profit", ea.field("Ordinary profit the cost of learning must also earn, % a year", rat(lo=0, hi=100)), "0"),
                       ("limit", arec("Limits on entry (employment, entrants allowed, pay rise %; empty for none)",
                                      [("employment", _N), ("entrants", ea.whole(0, LIMIT)), ("pay_rise", rat(lo=0, hi=1000))],
                                      unique=True, rows=2, lo=0, hi=12), "")],
            "tiles": [("Money wage a year", "wadAnnual"), ("Cost of learning replaced a year", "wadLearnYear"),
                      ("Net advantage a year", "wadNet"), ("Ranking, highest first", "wadRank"),
                      ("Spread, highest less lowest", "wadSpread"), ("With the limits on entry", "wadLimited"),
                      ("Ranking with the limits", "wadRankAfter")],
            "check": _check_net, "options": _money(),
            "subtitle": "the whole advantages and disadvantages of employments",
            "rules": "The money wage a year is the wage a day times the days worked. The cost of learning is "
                     "replaced over the working years with the ordinary profit on it each year: learning/years + "
                     "learning × profit/100 (the lab's simple rule; Smith, I.10, asks that it be replaced 'with at "
                     "least the ordinary profits'). Other advantages are the lesson's money value a year for "
                     "agreeableness, constancy, trust or risk, signed (a disadvantage is negative): Smith names the "
                     "circumstances, the lab does not price them. Net advantage = money wage − learning replaced + "
                     "other. Ranking is by net advantage, highest first; = marks a tie, which keeps the order given. "
                     "A limit on entry is the lesson's: the capped employment's wage rises by its pay rise % and its "
                     "net is worked again; the entrants allowed are shown, not used, since the lab does not derive "
                     "the pay rise from them.",
            "js": WAD_VIEW_JS["net"],
        },
        "lottery": {
            "fields": [("entrants", ea.field("Entrants to the profession", ea.whole(1, LIMIT)), "20"),
                       ("succeed", ea.field("How many succeed", ea.whole(0, LIMIT)), "1"),
                       ("prize", ea.field("Income a year of one who succeeds", rat(lo=0)), None),
                       ("years", ea.field("Working years", rat(gt=0, hi=100)), None),
                       ("cost", ea.field("Each entrant's cost of education", rat(lo=0)), None)],
            "tiles": [("Chance of success", "wadChance"), ("Total prizes", "wadPrizes"), ("Total cost of the tickets", "wadTickets"),
                      ("Expected prize per entrant", "wadExpected"), ("Prizes against the tickets", "wadFair"),
                      ("Prize a year that would repay the tickets", "wadNeeded")],
            "check": _check_lottery, "options": _money(),
            "subtitle": "a profession as a lottery, its prizes against its tickets",
            "rules": "The chance is the successful over the entrants. Total prizes = successful × income a year × "
                     "working years; total cost = entrants × cost of education; the expected prize is the total prizes "
                     "over the entrants. The prizes are fair when they equal the cost, short or over otherwise. The "
                     "prize that would repay the tickets is the total cost over (successful × working years). The lab "
                     "adds no interest and no discounting, and counts no income for those who fail (its rules, not "
                     "Smith's). Smith (I.10) says perhaps one in twenty succeeds in the law; the other figures are "
                     "the lesson's.",
            "js": WAD_VIEW_JS["lottery"],
        },
        "profit": {
            "fields": [("sales", ea.field("Sales a year", rat(lo=0)), None),
                       ("cost", ea.field("Cost of the goods sold (stock laid out)", rat(gt=0)), None),
                       ("wages", ea.field("What the trader's own labour would earn as wages a year", rat(lo=0)), None),
                       ("stock", ea.field("Capital employed if not the cost (- for the cost)", rat(gt=0, dash=True)), "-")],
            "tiles": [("Apparent profit", "wadApparent"), ("Its rate on the stock", "wadApparentRate"),
                      ("True profit, after the wages of the trader's labour", "wadTrue"), ("Its rate", "wadTrueRate"),
                      ("Share of the apparent profit that is wages", "wadWageShare")],
            "check": None, "options": _money(),
            "subtitle": "the apothecary's profit split into wages and profit",
            "rules": "Apparent profit = sales − cost, and its rate is over the stock (the cost unless another capital "
                     "is given). True profit takes off the wages the trader's own labour would earn; its rate is over "
                     "the same stock. The share that is wages is the wages over the apparent profit (it passes 100% "
                     "when the true profit is negative). Smith (I.10) reads the apothecary's 'thousand per cent' as "
                     "mostly the reasonable wages of his labour; the wages figure is the lesson's.",
            "js": WAD_VIEW_JS["profit"],
        },
    },
}

# ---------------------------------------------------------------------------
# rent (wre): rent as a residual, tenure and improvement, the price of corn
# ---------------------------------------------------------------------------

WRE_JS = r"""
  var WRE_VIEW = {};
  function wreCompute(view, inst, opts) { return eaRun(WRE_VIEW[view], inst, opts); }
"""

WRE_VIEW_JS = {}

WRE_VIEW_JS["residual"] = r"""
  WRE_VIEW.residual = function (inst, o) {
    var m = o.money_unit, M = function (r) { return wreMoney(r, m); }, L = inst.lands, g = Radd(R1, Rdiv(inst.rate, R(100n)));
    var p2 = inst.price2, has2 = p2 !== '-';
    var cost = function (x) { return Rmul(Radd(x.wages, x.stock), g); };
    var rent = function (x, p) { return Rsub(Rmul(x.output, p), cost(x)); };
    var rtext = function (r) { return r.n > 0n ? M(r) : (r.n < 0n ? 'no rent (a loss of ' + M(Rneg(r)) + ')' : 'no rent (nothing left)'); };
    var list = function (f) { return L.map(function (x) { return x.land + ' ' + f(x); }).join('; '); };
    var total = function (p) { return eaSum(L.map(function (x) { var r = rent(x, p); return r.n > 0n ? r : R0; })); };
    var none = L.filter(function (x) { return rent(x, inst.price).n <= 0n; }).map(function (x) { return x.land; });
    return {
      tiles: {
        wreValue: list(function (x) { return M(Rmul(x.output, inst.price)); }),
        wreCosts: list(function (x) { return M(cost(x)); }),
        wreRent: list(function (x) { return rtext(rent(x, inst.price)); }),
        wreTotal: M(total(inst.price)), wreNoRent: aktListed(none.length, none),
        wreLowest: list(function (x) { return M(Rdiv(cost(x), x.output)) + ' a unit'; }),
        wreRent2: has2 ? list(function (x) { return rtext(rent(x, p2)); }) : 'no second price given',
        wreTotal2: has2 ? M(total(p2)) + ' at ' + M(p2) + ' a unit' : 'no second price given'
      },
      status: wnkStatus('At ' + M(inst.price) + ' a unit the lands pay ' + M(total(inst.price)) + ' of rent in all; ' + (none.length ? eaPlural(none.length, 'land yields', 'lands yield') + ' none (' + none.join(', ') + ')' : 'every land yields some')),
      table: { caption: 'Each land a year: the produce’s value, wages and stock with ordinary profit, and the rent left',
               head: ['land', 'output', 'value', 'wages + stock + profit', 'rent', 'lowest price for rent'].concat(has2 ? ['rent at the second price'] : []),
               rows: L.map(function (x) { return [x.land, eaNum(x.output), M(Rmul(x.output, inst.price)), M(cost(x)), rtext(rent(x, inst.price)), M(Rdiv(cost(x), x.output))].concat(has2 ? [rtext(rent(x, p2))] : []); }) }
    };
  };
"""

WRE_VIEW_JS["tenure"] = r"""
  WRE_VIEW.tenure = function (inst, o) {
    var m = o.money_unit, M = function (r) { return wreMoney(r, m, true); }, T = inst.tenures;
    var whole = Rmul(inst.added, inst.years), net = Rsub(whole, inst.cost);
    var gain = function (t) { return Rsub(Rmul(t.share, whole), Rmul(t.bears, inst.cost)); };
    var lord = function (t) { return Rsub(Rmul(Rsub(R1, t.share), whole), Rmul(Rsub(R1, t.bears), inst.cost)); };
    var yes = T.filter(function (t) { return gain(t).n > 0n; }).map(function (t) { return t.tenure; });
    var list = function (f) { return T.map(function (t) { return t.tenure + ' ' + f(t); }).join('; '); };
    return {
      tiles: {
        wreWhole: M(net) + ' (' + wreMoney(whole, m) + ' added over ' + wreUnit(inst.years, 'years') + ', less ' + wreMoney(inst.cost, m) + ')',
        wreGain: list(function (t) { return M(gain(t)); }),
        wreImproves: aktListed(yes.length, yes),
        wreLandlord: list(function (t) { return M(lord(t)); })
      },
      status: wnkStatus('The improvement is worth ' + M(net) + ' to occupier and landlord together; the occupier makes it under ' + (yes.length ? yes.join(', ') : 'no tenure listed')),
      table: { caption: 'Each tenure: the occupier’s share of the added produce and of the cost, and each party’s gain over the years',
               head: ['tenure', 'occupier keeps', 'occupier pays', 'occupier’s gain', 'improves', 'landlord’s part'],
               rows: T.map(function (t) { return [t.tenure, eaPct(t.share), eaPct(t.bears), M(gain(t)), gain(t).n > 0n ? 'yes' : 'no', M(lord(t))]; }) }
    };
  };
"""

WRE_VIEW_JS["silver"] = r"""
  WRE_VIEW.silver = function (inst, o) {
    var m = o.money_unit, M = function (r) { return wreMoney(r, m); }, P = inst.periods, X = inst.prices;
    var stats = P.map(function (p, i) {
      var w = 'Periods, record ' + (i + 1) + ' (' + p.period + ')';
      if (Rcmp(p.from, p.to) > 0) eaRefuse(w + ': from ' + String(p.from.n) + ' is after to ' + String(p.to.n));
      var ys = X.filter(function (x) { return Rcmp(x.year, p.from) >= 0 && Rcmp(x.year, p.to) <= 0; });
      if (!ys.length) eaRefuse(w + ': no year from ' + String(p.from.n) + ' to ' + String(p.to.n) + ' is listed in the prices');
      return { name: p.period, n: ys.length, avg: Rdiv(eaSum(ys.map(function (x) { return x.price; })), R(BigInt(ys.length))) };
    });
    var a1 = stats[0].avg, list = function (f) { return stats.map(function (s) { return s.name + ' ' + f(s); }).join('; '); };
    var last = stats[stats.length - 1];
    return {
      tiles: {
        wreYears: list(function (s) { return eaPlural(s.n, 'year', 'years'); }),
        wreAverage: list(function (s) { return M(s.avg); }),
        wreRatio: list(function (s) { return wreX(Rdiv(s.avg, a1)); }),
        wreCorn: list(function (s) { return wreUnit(Rinv(s.avg), 'quarters') + ' for ' + M(R1); })
      },
      status: wnkStatus(stats.length > 1 ? 'The average price of a quarter goes from ' + M(a1) + ' in ' + stats[0].name + ' to ' + M(last.avg) + ' in ' + last.name + ', ' + wreX(Rdiv(last.avg, a1)) : 'The average price of a quarter in ' + stats[0].name + ' is ' + M(a1)),
      table: { caption: 'Each period: the years listed in it and the average price of a quarter of wheat',
               head: ['period', 'from', 'to', 'years listed', 'average price', 'against ' + stats[0].name, 'quarters for ' + M(R1)],
               rows: P.map(function (p, i) { var s = stats[i]; return [s.name, String(p.from.n), String(p.to.n), String(s.n), M(s.avg), wreX(Rdiv(s.avg, a1)), eaNum(Rinv(s.avg))]; }) }
    };
  };
"""


def _check_silver(inst, fixed):
    years = [x["year"] for x in inst["prices"]]
    for i, p in enumerate(inst["periods"]):
        w = "Periods, record %d (%s)" % (i + 1, p["period"])
        if p["from"] > p["to"]:
            raise ValueError("%s: from %s is after to %s" % (w, str(int(p["from"])), str(int(p["to"]))))
        if not any(p["from"] <= y <= p["to"] for y in years):
            raise ValueError("%s: no year from %s to %s is listed in the prices"
                             % (w, str(int(p["from"])), str(int(p["to"]))))


_SHARE = rat(lo=0, hi=1)

RENT = {
    "prefix": "wre", "fn": "wreCompute", "title": "The rent of land", "js": _js("wre", WRE_JS),
    "views": {
        "residual": {
            "fields": [("lands", arec("Lands (land, units produced a year, wages paid, other stock advanced)",
                                      [("land", _N), ("output", rat(gt=0)), ("wages", rat(lo=0)), ("stock", rat(lo=0))],
                                      unique=True, rows=3, lo=1, hi=12), None),
                       ("price", ea.field("Price of a unit of the produce", rat(gt=0)), None),
                       ("rate", ea.field("Ordinary profit, % on wages and stock", rat(lo=0, hi=1000)), "10"),
                       ("price2", ea.field("A second price to compare (- for none)", rat(gt=0, dash=True)), "-")],
            "tiles": [("Value of the produce", "wreValue"), ("Wages and stock with ordinary profit", "wreCosts"),
                      ("Rent left", "wreRent"), ("Total rent", "wreTotal"), ("Lands yielding no rent", "wreNoRent"),
                      ("Lowest price that affords rent", "wreLowest"), ("Rent at the second price", "wreRent2"),
                      ("Total rent at the second price", "wreTotal2")],
            "check": None, "options": _money(),
            "subtitle": "rent as what is left after wages and ordinary profit",
            "rules": "A land's produce is worth its output times the price. Smith's rule (I.11): rent is what is "
                     "left after the wages and the stock advanced are replaced with the ordinary profit, (wages + "
                     "stock) × (1 + rate/100). When nothing or less than nothing is left the land yields no rent, and "
                     "the lab shows the loss; total rent adds only the rents above 0 (the lab's rule: a land that "
                     "cannot pay is not counted as paying a negative rent). The lowest price that affords rent is "
                     "(wages + stock) × (1 + rate/100) over the output: any price above it leaves a rent. Lands are "
                     "listed in the order given.",
            "js": WRE_VIEW_JS["residual"],
        },
        "tenure": {
            "fields": [("cost", ea.field("The improvement's cost", rat(lo=0)), None),
                       ("added", ea.field("Value of the produce it adds a year", rat(lo=0)), None),
                       ("years", ea.field("Years the improver gets the benefit", rat(gt=0, hi=200)), None),
                       ("tenures", arec("Tenures (tenure, share of the added produce the occupier keeps, share of the "
                                        "cost the occupier pays; each from 0 to 1)",
                                        [("tenure", _N), ("share", _SHARE), ("bears", _SHARE)], unique=True, rows=3,
                                        lo=1, hi=12), None)],
            "tiles": [("The improvement's whole gain", "wreWhole"), ("The occupier's gain under each tenure", "wreGain"),
                      ("Tenures under which the occupier improves", "wreImproves"), ("The landlord's part", "wreLandlord")],
            "check": None, "options": _money(),
            "subtitle": "whether the occupier gains from an improvement under each tenure",
            "rules": "Over the years the improvement adds its yearly produce times the years. The occupier keeps "
                     "the share of that and pays the share of the cost: gain = share × added × years − bears × cost. "
                     "The occupier improves when the gain is above 0 (the lab's rule; Smith, III.2, argues that a "
                     "tenant who keeps only part of the produce, or whose lease is short, has little interest in "
                     "improving). The landlord's part is the rest of the produce less the rest of the cost. Shares "
                     "are fractions from 0 to 1 (1/2 for a metayer). No interest or discounting is applied.",
            "js": WRE_VIEW_JS["tenure"],
        },
        "silver": {
            "fields": [("prices", arec("Prices (year, price of a quarter of wheat)", [("year", ea.whole(1, 3000)), ("price", rat(gt=0))],
                                       unique=True, rows=4, lo=1, hi=60), None),
                       ("periods", arec("Periods (period, from year, to year)",
                                        [("period", _N), ("from", ea.whole(1, 3000)), ("to", ea.whole(1, 3000))],
                                        unique=True, rows=3, lo=1, hi=12), None)],
            "tiles": [("Years listed in each period", "wreYears"), ("Average price of a quarter", "wreAverage"),
                      ("Average against the first period", "wreRatio"), ("The value of silver in corn", "wreCorn")],
            "check": _check_silver, "options": _money(),
            "subtitle": "the price of corn in silver, averaged by period",
            "rules": "A period's average is the mean of the prices of the years listed from its first year to its "
                     "last, inclusive, exact (shown to two places with ≈ when not exact); a year not listed is not "
                     "counted, and a period with no year listed is refused. Periods may overlap. The ratio is each "
                     "average over the first period's. The value of silver in corn is the quarters one unit of money "
                     "buys at the average, 1/average. Smith averages Windsor market prices this way in the Digression "
                     "(I.11); the lab takes the prices typed and says nothing of the price in any year not listed. Up "
                     "to 60 prices.",
            "js": WRE_VIEW_JS["silver"],
        },
    },
}

# ---------------------------------------------------------------------------
# interest (wit): years' purchase, profit from interest
# ---------------------------------------------------------------------------

WIT_JS = r"""
  var WIT_VIEW = {};
  function witCompute(view, inst, opts) { return eaRun(WIT_VIEW[view], inst, opts); }
"""

WIT_VIEW_JS = {}

WIT_VIEW_JS["purchase"] = r"""
  WIT_VIEW.purchase = function (inst, o) {
    var m = o.money_unit, M = function (r) { return witMoney(r, m); }, H = R(100n);
    var yp = Rdiv(H, inst.rate), price = Rmul(inst.rent, yp), r2 = inst.rate2, y = inst['yield'], none = 'no second rate given';
    var yp2 = r2 === '-' ? null : Rdiv(H, r2), price2 = yp2 ? Rmul(inst.rent, yp2) : null, fetch;
    if (y === '-') fetch = 'no present yield given';
    else if (Rzero(y)) fetch = M(price) + ', but it yields nothing now: no number of years of its yield equals the price';
    else fetch = M(price) + ', ' + eaNum(Rdiv(price, y)) + ' years of its present yield of ' + M(y);
    return {
      tiles: {
        witYp: eaNum(yp) + ' years’ purchase at ' + witRate(inst.rate), witPrice: M(price),
        witYp2: yp2 ? eaNum(yp2) + ' years’ purchase at ' + witRate(r2) : none,
        witPrice2: yp2 ? M(price2) + ' (' + witMoney(Rsub(price2, price), m, true) + ', ' + witCh(Rdiv(Rsub(price2, price), price)) + ')' : none,
        witFetches: fetch
      },
      status: wnkStatus('At ' + witRate(inst.rate) + ' a rent of ' + M(inst.rent) + ' sells for ' + eaNum(yp) + ' years’ purchase, ' + M(price)
        + (yp2 ? '; at ' + witRate(r2) + ', ' + eaNum(yp2) + ' years’ purchase, ' + M(price2) : '')),
      table: null
    };
  };
"""

WIT_VIEW_JS["profit"] = r"""
  WIT_VIEW.profit = function (inst) {
    var R2 = inst.rows, T = R(2n);
    var mult = function (x) { return x.rest.length && x.rest[0] !== '-' ? x.rest[0] : T; };
    R2.forEach(function (x, i) {
      if (x.rest.length && x.rest[0] !== '-' && Rzero(x.rest[0])) eaRefuse('Rows, record ' + (i + 1) + ' (' + x.period + '): a multiple of 0 makes profit nothing; give a multiple above 0, or - for 2');
    });
    var implied = function (x) { return Rmul(x.interest, mult(x)); };
    var list = function (f) { return R2.map(function (x) { return x.period + ' ' + f(x); }).join('; '); };
    var stated = R2.filter(function (x) { return x.rest.length > 1 && x.rest[1] !== '-'; });
    var f = R2[0], l = R2[R2.length - 1], fall;
    if (R2.length === 1) fall = 'one period only';
    else fall = 'interest ' + witRate(f.interest) + ' → ' + witRate(l.interest) + ' (' + aktPp(Rdiv(Rsub(l.interest, f.interest), R(100n))) + '); implied profit '
      + witRate(implied(f)) + ' → ' + witRate(implied(l)) + ' (' + aktPp(Rdiv(Rsub(implied(l), implied(f)), R(100n))) + ')';
    return {
      tiles: {
        witImplied: list(function (x) { return witRate(x.interest) + ' × ' + eaNum(mult(x)) + ' = ' + witRate(implied(x)); }),
        witLeft: stated.length ? stated.map(function (x) { var d = Rsub(x.rest[1], x.interest); return x.period + ' ' + witRate(x.rest[1]) + ' − ' + witRate(x.interest) + ' = ' + witRate(d); }).join('; ') : 'no profit stated',
        witFall: fall
      },
      status: wnkStatus(R2.length === 1 ? f.period + ': interest ' + witRate(f.interest) + ' implies an ordinary profit of ' + witRate(implied(f)) : 'From ' + f.period + ' to ' + l.period + ' ' + fall),
      table: { caption: 'Each period: the market rate of interest, the multiple, the implied ordinary profit, and what a stated profit leaves after interest',
               head: ['period', 'interest', 'multiple', 'implied profit', 'stated profit', 'left after interest'],
               rows: R2.map(function (x) { var s = x.rest.length > 1 && x.rest[1] !== '-'; return [x.period, witRate(x.interest), eaNum(mult(x)), witRate(implied(x)), s ? witRate(x.rest[1]) : '—', s ? witRate(Rsub(x.rest[1], x.interest)) : '—']; }) }
    };
  };
"""


def _check_wit_profit(inst, fixed):
    for i, x in enumerate(inst["rows"]):
        if x["rest"] and x["rest"][0] != "-" and x["rest"][0] == 0:
            raise ValueError("Rows, record %d (%s): a multiple of 0 makes profit nothing; give a multiple above 0, or - "
                             "for 2" % (i + 1, x["period"]))


INTEREST = {
    "prefix": "wit", "fn": "witCompute", "title": "Interest", "js": _js("wit", WIT_JS),
    "views": {
        "purchase": {
            "fields": [("rent", ea.field("Rent a year (or any yearly revenue sold)", rat(gt=0)), None),
                       ("rate", ea.field("Rate of interest, %", rat(gt=0, hi=100)), None),
                       ("rate2", ea.field("A second rate to compare, % (- for none)", rat(gt=0, hi=100, dash=True)), "-"),
                       ("yield", ea.field("What the asset yields its present owner a year (- for none)", rat(lo=0, dash=True)), "-")],
            "tiles": [("Years' purchase", "witYp"), ("Price", "witPrice"), ("Years' purchase at the second rate", "witYp2"),
                      ("Price at the second rate", "witPrice2"), ("What it fetches against what it yields", "witFetches")],
            "check": None, "options": _money(),
            "subtitle": "the price of land in years' purchase",
            "rules": "Years' purchase = 100 / the rate of interest: the number of years' rent the price equals, so "
                     "that the rent is the interest on the price. Price = rent × years' purchase. Smith (II.4) gives "
                     "the rule that the price of land rises as interest falls. With a second rate both are shown and "
                     "the change in price. With a present yield (the crown lands of V.2, which yield their owner less "
                     "than the rent a private owner would draw), the price over that yield is the number of years of "
                     "the present yield the sale fetches.",
            "js": WIT_VIEW_JS["purchase"],
        },
        "profit": {
            "fields": [("rows", arec("Periods (period, market rate of interest %, then the multiple and a stated profit "
                                     "rate %, each optional; - for none)",
                                     [("period", _N), ("interest", rat(gt=0, hi=100))], rat(lo=0, hi=1000, dash=True),
                                     "value", 0, 2, unique=True, rows=4, lo=1, hi=12), None)],
            "tiles": [("Implied ordinary profit (interest × multiple)", "witImplied"),
                      ("A stated profit less interest", "witLeft"), ("First to last", "witFall")],
            "check": _check_wit_profit, "options": None,
            "subtitle": "interest as the index of profit",
            "rules": "Smith (I.9) takes the market rate of interest as the index of the ordinary rate of profit, and "
                     "double interest as a 'reasonable, moderate' profit. The implied profit is interest × the "
                     "multiple (2 when none is given or it is -). A stated profit less the interest is what is left "
                     "to the borrower for the risk and trouble of employing the stock. The fall compares the first "
                     "and last periods given, in percentage points.",
            "js": WIT_VIEW_JS["profit"],
        },
    },
}

# ---------------------------------------------------------------------------
# The entry point
# ---------------------------------------------------------------------------

SPECS = {"division": DIVISION, "money": MONEY, "price": PRICE, "wages": WAGES, "advantage": ADVANTAGE,
         "rent": RENT, "interest": INTEREST}
for _spec in SPECS.values():
    for _v in _spec["views"].values():
        if _v.get("options") is None:
            _v.pop("options", None)
MODES_A = tuple(SPECS)


def _family_b():
    """wonkit_b.MODES, imported on first use; {} while wonkit_b.py does not exist."""
    try:
        wonkit_b = importlib.import_module(".wonkit_b", __package__)
    except ModuleNotFoundError as exc:
        if exc.name and exc.name.endswith("wonkit_b"):
            return {}
        raise
    return wonkit_b.MODES


def wonkit_lab(cfg):
    """The Wealth of Nations kit: cfg["mode"] chooses the mode, cfg["view"] the view."""
    cfg = cfg or {}
    mode = cfg.get("mode")
    if mode in SPECS:
        return mode_lab(cfg, mode, SPECS[mode])
    family_b = _family_b()
    if mode in family_b:
        return family_b[mode](cfg)
    raise ValueError("wonkit_lab: unknown mode %r; the modes are %s"
                     % (mode, ", ".join(MODES_A + tuple(m for m in family_b if m not in SPECS))))


__all__ = ["wonkit_lab", "SPECS", "MODES_A", "WNA_JS"]
