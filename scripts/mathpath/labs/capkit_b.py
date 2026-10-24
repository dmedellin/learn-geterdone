"""capkit, second half: turnover, schemes, profit, prices, tendency, interest, rent, revenue.

docs/capital/PLAN.md section D.2; the conventions of D.0 there (and of
docs/philosophy/PLAN.md D.0, which it adopts) bind every mode. capkit.py
dispatches these eight modes here, as dekit dispatches to dekit_b, so two
engineers can build the seventeen modes without sharing a file. The entry
point is capkit_b_lab(cfg); MODES names the eight modes; an unknown mode or
view RAISES.

  turnover  (tu)  turnover time and turnovers a year, the three stages, fixed
                  capital's wear and moral depreciation, aggregate turnover,
                  the two classifications, the working period, capital I and
                  II and the capital set free, the annual rate of surplus
                  value, the merchant's turnovers
  schemes   (sc)  Volume II's two departments: sorting the product, the three
                  exchanges, fixed capital and hoards, the expanded scheme
  profit    (pr)  cost price, p' beside s', turnover, economy, price changes
  prices    (pp)  rates by sphere, the general rate and prices of production,
                  a general wage rise, the merchant's share and mark-up
  tendency  (te)  the rate of profit under a rising composition, what offsets
                  it, over-accumulation and devaluation
  interest  (in)  interest and profit of enterprise, the bounds, the price of
                  a claim on income, compound sums, usury
  rent      (rt)  the price of land, the waterfall, differential rent I and II,
                  absolute rent
  revenue   (rv)  c + v + s, the dogma's missing c, the trinity, classes

SHARED MACHINERY is capkit_core.py: the preset menu, the input boxes and their
parsing by field kind (capRead), money and percentage printing (capMoney,
capPct), the table, the banner and the wiring. Each mode here is a table of
fields, a table of views, and one pure JS function kbXxxx(view, inst, U, opts)
that the wiring calls with the parsed boxes: it checks the rules that span
fields (returning {refuse: sentence}) and computes every tile, the table and
the banner. Being pure, it is what scripts/mathcheck.js calls (section
"capkit_b (Volumes II and III modes)").

THE LESSON SUPPLIES THE INSTANCES, with D.2's field names. A few D.2 shapes are
turned into the shape a text box holds before capkit_core sees them (see
_normalise): I and II {c, v, s} become "4000, 1000, 1000"; agri and industry
{c, v} become "75, 25"; split {interest, rent} becomes two boxes; a soil's
list of outputs becomes one row per investment; a single c_step becomes a list
of one. Every other field is the box's text as capkit_core writes it.

VIEW IS NOT A CONTROL. cfg["view"] fixes which inputs and tiles the page
shows. There are no redraw-only selects in these eight modes.
schemes/expanded and tendency/law and counter carry the periods range (1 to
10), shipped from cfg["periods"] or from a preset's own "periods" (capkit_core
mode_lab), and a tendency step list must match the periods of its own preset;
rent/dr2 takes cfg["price_case"] (constant,
falling, rising, worst-soil), which is not a control: every preset is checked
against it at build time, and the banner says when a reader's edit leaves the
case.

NAMES. Module-level JavaScript names here begin kb, and a mode's helpers kb +
the mode's two letters (kbTuTime, kbScStep, ...). No tile id is a JS name.
Tile ids grepped against scripts/mathpath/labs/*.py on 2026-10-24: none of
tu*, sc*, pr*, pp*, te*, in*, rt*, rv* below is a module-level JS name of any
kit; ppPreset/prPreset/inPreset and friends exist as element ids on other
kits' pages only, and one page carries one lab.

EXACT. Every printed figure is a rational over BigInt (RATIONAL_JS). The one
non-exact figure is the percentage beside its fraction (capPct), and
interest/usury's table, which prints a long exact figure rounded behind ≈.
interest/compound prints a closed form and a count of digits where the exact
sum is too long to print.

DEVIATIONS FROM D.2, each the reading that keeps the arithmetic honest; the
full list, with reasons, is DEVIATIONS below.
"""

from fractions import Fraction

from . import capkit_core as cc
from .common import cfg_literal

KIT = "capkit"

DEVIATIONS = """
  * Fields D.2 does not list but a lesson in section C needs: turnover/time
    `capital` (the capital advanced, for tuAggregate); turnover/fixed
    `age_years` (tuRemaining is "after n years"); turnover/advance
    `new_outlay` (Chapter 31's change of scale: tuFreed then prints the
    capital released); prices `profit_rate` and `average` (Chapter 11 gives
    Marx's average rate and names the sphere of average composition; without
    `average` the whole of the spheres is the average capital); rent
    `industry` {c, v} (Chapter 45 compares agriculture with it); revenue
    `people` rows may give `source` (a named source of revenue) so that
    "landowners-split" can split rent finely; {name, wages, profit, rent}
    still works and the source is the kinds with a positive amount.
  * Rates are typed as fractions (1/5), as capkit_core reads them; a tile
    prints the percentage beside the fraction.
  * schemes tiles print Marx's notation bare (I(v + s) = 2,000 = IIc), as D.2's
    formats do; the banner names no unit. Every other money tile carries the
    lesson's money_unit, including ppTotals (values £422 = prices £422 ...).
  * section C says "years = 4" for schemes/expanded; D.0 names the key
    `periods`, which is what this kit reads.
  * prices/wage-rise: Marx's Chapter 11 low-composition figure. Exactly, 50c +
    62½v at 1/7 earns 225/14 = 16 1/14 and sells at 900/7 = 128 4/7 (= 128
    8/14); the Kerr text prints 16 1/12 and 128 7/12, 1/84 too much. The tile
    prints 900/7. The high-composition 116 4/7 (816/7) is exact.
  * tendency/law: Marx's Chapter 13 table raises c by 50, 100, 100, 100 at v =
    100, so c_step and capital_growth take a list (one figure per period) as
    well as one figure for every period. Each period: capital grows by
    capital_growth (c and v alike), then c_step is added to c, then c cheapens
    by c_cheapening, then s' rises by s_rate_step.
  * tendency/overaccumulation: absolute over-accumulation is modelled as D.2's
    figures read: the added capital sets no more labour in motion, so the mass
    of s is unchanged; devaluation removes a share of the swollen capital.
  * interest/usury: the whole surplus goes to the usurer each year and the
    interest it does not cover is added to the debt; years is the horizon
    (1 to 100); inYearsToRuin also prints "repaid in year n" when the surplus
    clears the debt.
  * interest/compound: years 0 to 5000; the tile prints the exact sum when it
    is at most 40 characters, else the closed form and the number of digits
    before the point.
  * rent/dr1 and dr2: the regulating investment is the least productive in use
    (`regulating: "auto"`), or a named one ("B" or "B1" for B's first dose,
    "B2" for its second). With `market_limit` the most productive investments
    are taken first until the market is supplied and the last taken
    regulates, which is how a price falls (A drops out) or rises. dr2 adds
    `former_price` (the regulating price before the change; empty: what the
    least productive first doses would set), because "rising" and "falling"
    are claims about a change and a new worse soil cannot be detected from
    the new instance alone. price_case "worst-soil" is Chapter 44's case: an
    additional dose regulates and the worst soil's first dose pays rent.
  * rent/waterfall prints rtSurplusProfit with Marx's mixed numbers (11½), the
    one tile in these modes that does, because D.2's format says so.
  * schemes/hoard: of Department I's accumulated surplus product, the
    `hoarders_share` is sold and hoarded with no purchase; the rest is bought
    with money hoarded before. scHoardGap = hoarders' sales − investors'
    purchases.
"""

# ---------------------------------------------------------------------------
# Shared JavaScript (on top of capkit_core's CAP_CORE_JS)
# ---------------------------------------------------------------------------

KB_COMMON_JS = r"""
  function kbFloor(r) {
    var q = r.n / r.d;
    return (r.n < 0n && q * r.d !== r.n) ? q - 1n : q;
  }
  function kbFig(r) { return capNumText(r); }
  function kbSigned(r) { return capSigned(r, capNumText); }
  var KB_GLYPH = { '1/2': '½', '1/4': '¼', '3/4': '¾' };
  /* A mixed number the way Marx prints one: 11½, 3¼, 2 1/3, ½. */
  function kbVulgar(r) {
    var neg = Rsign(r) < 0, a = Rabs(r), w = kbFloor(a), f = Rsub(a, R(w)), t;
    if (Rzero(f)) t = capGroup(String(w));
    else if (KB_GLYPH[Rtext(f)]) t = (w > 0n ? capGroup(String(w)) : '') + KB_GLYPH[Rtext(f)];
    else t = (w > 0n ? capGroup(String(w)) + ' ' : '') + Rtext(f);
    return (neg ? CAP_MINUS : '') + t;
  }
  function kbMoneyV(r, unit) {
    if (unit === 's') return capShillings(r);
    var neg = Rsign(r) < 0, t = kbVulgar(Rabs(r));
    return (neg ? CAP_MINUS : '') + (unit === '£' ? '£' + t : t + ' h');
  }
  /* The percentage alone, as capPct prints it: 66.67%. */
  function kbPctNum(r) { return capPct(r).split(' = ')[1]; }
  /* A rate inside a sentence or a longer tile, exact: 5%, 100/7%. */
  function kbPctShort(r) { return capNumText(Rmul(r, R(100n))) + '%'; }
  function kbWeeks(r) { return capCount(r, 'week', 'weeks'); }
  function kbYears(r) { return capCount(r, 'year', 'years'); }
  function kbTimes(r) { return capCount(r, 'time', 'times'); }
  function kbPlural(n, one, many) { return n + ' ' + (n === 1 ? one : many); }
  /* A long exact figure rounded for a table, behind ≈ (half away from zero). */
  function kbApprox(r, unit) {
    var t = Rdec(r, 2).replace('-', CAP_MINUS), dot = t.indexOf('.');
    t = dot < 0 ? capGroup(t) : capGroup(t.slice(0, dot)) + t.slice(dot);
    return '≈ ' + (unit === '£' ? '£' + t : unit === 's' ? t + 's' : t + ' h');
  }
  /* Run a mode's checks; a thrown sentence becomes the page's refusal. */
  function kbGuard(check, view, inst, opts) {
    try { return { o: check(view, inst, opts) }; } catch (err) { return { refuse: err.message }; }
  }
"""

# ---------------------------------------------------------------------------
# turnover (Volume II, Part Two; Volume III, Chapter 16)
# ---------------------------------------------------------------------------

TURNOVER_JS = r"""
  /* Turnover time u = production time + circulation time; n = U/u, with U
     the year in weeks (Volume II, Chapter 7). */
  function kbTuTime(production, circulation, year) {
    var u = Radd(production, circulation);
    return { u: u, n: Rdiv(year, u) };
  }
  /* Fixed capital at a given age (Chapter 8): each item transfers value/life
     a year, plus its repairs; once a cheaper machine of the same kind has
     appeared, the old one is worth what its replacement would cost, worn to
     the same age (moral depreciation). lost = value destroyed that way. */
  function kbTuFixed(items, age) {
    var wear = R0, left = R0, lost = R0;
    items.forEach(function (it) {
      var moral = it.replacement !== null && Rcmp(age, it.appears) >= 0;
      var base = moral ? it.replacement : it.value;
      var used = Rcmp(age, it.life) > 0 ? it.life : age;
      var share = Rdiv(Rsub(it.life, used), it.life);
      wear = Radd(wear, Radd(Rdiv(base, it.life), it.repairs));
      left = Radd(left, Rmul(base, share));
      if (moral) lost = Radd(lost, Rmul(Rsub(it.value, it.replacement), share));
    });
    return { wear: wear, left: left, lost: lost };
  }
  /* Aggregate turnover (Chapter 9): the year's wear of the fixed parts plus
     the circulating part times its turnovers, against the capital advanced. */
  function kbTuAggregate(items, circulating, turns) {
    var wear = R0, fixed = R0;
    items.forEach(function (it) { wear = Radd(wear, Rdiv(it.value, it.life)); fixed = Radd(fixed, it.value); });
    var turned = Radd(wear, Rmul(circulating, turns)), advanced = Radd(fixed, circulating);
    return { wear: wear, turned: turned, advanced: advanced, average: Rdiv(turned, advanced) };
  }
  /* The same items by both classifications (Chapters 10-11), per capital in
     input order; s at the rate of surplus value on the variable items only. */
  function kbTuClassify(items, sRate) {
    var groups = [], at = {};
    items.forEach(function (it) {
      var key = it.capital || '';
      if (at[key] === undefined) {
        at[key] = groups.length;
        groups.push({ name: key, fixed: R0, circulating: R0, constant: R0, variable: R0 });
      }
      var g = groups[at[key]];
      if (it.fixed) g.fixed = Radd(g.fixed, it.value); else g.circulating = Radd(g.circulating, it.value);
      if (it.variable) g.variable = Radd(g.variable, it.value); else g.constant = Radd(g.constant, it.value);
    });
    groups.forEach(function (g) { g.s = Rmul(sRate, g.variable); });
    return groups;
  }
  /* Capital I covers the working period, capital II the circulation period
     (Chapter 15). The capital set free at the close of each working period,
     from the second turnover on, is the chapter's rule in §4: capital II when
     the working period is the longer; nothing when the two are equal or the
     circulation period is a whole multiple of the working period; otherwise
     the excess of circulation over the largest multiple of working periods. */
  function kbTuAdvance(working, circulation, outlay) {
    var capI = Rmul(working, outlay), capII = Rmul(circulation, outlay), freedWeeks;
    var c = Rcmp(working, circulation);
    if (c > 0) freedWeeks = circulation;
    else if (c === 0) freedWeeks = R0;
    else freedWeeks = Rsub(circulation, Rmul(working, R(kbFloor(Rdiv(circulation, working)))));
    return { capI: capI, capII: capII, total: Radd(capI, capII), freed: Rmul(freedWeeks, outlay) };
  }
  /* A change of scale (Chapter 31's case): the whole turnover's advance at the
     old weekly outlay less at the new; positive = released. */
  function kbTuRescale(working, circulation, outlay, newOutlay) {
    return Rmul(Radd(working, circulation), Rsub(outlay, newOutlay));
  }
  /* The annual rate of surplus value s'·n and the year's mass s'·v·n (Chapter 16). */
  function kbTuAnnual(variable, sRate, u, year) {
    var n = Rdiv(year, u);
    return { n: n, rate: Rmul(sRate, n), mass: Rmul(Rmul(sRate, variable), n) };
  }
  function kbTuCheck(view, x) {
    var o = {};
    if (view === 'time') {
      o.production = x.production_weeks; o.circulation = x.circulation_weeks; o.year = x.year_weeks;
      o.working = x.working_weeks === null ? x.production_weeks : x.working_weeks;
      if (Rcmp(o.working, o.production) > 0) {
        throw new Error('The working time (' + kbWeeks(o.working) + ') is longer than the production period ('
          + kbWeeks(o.production) + ') it is part of');
      }
      o.capital = x.capital;
    } else if (view === 'phases') {
      o.stages = x.stage_weeks; o.year = x.year_weeks;
      if (Rzero(capSum(o.stages))) throw new Error('The three stages add up to no time at all');
    } else if (view === 'fixed' || view === 'aggregate') {
      o.items = x.fixed.map(function (it) {
        if ((it.replacement_value === null) !== (it.appears_year === null)) {
          throw new Error(it.name + ' needs both a replacement value and the year it appears, or neither');
        }
        return { name: it.name, value: it.value, life: it.life_years, repairs: it.repairs_per_year || R0,
                 replacement: it.replacement_value, appears: it.appears_year };
      });
      if (view === 'fixed') o.age = x.age_years;
      else {
        o.circulating = x.circulating; o.turns = x.circ_turnovers;
        if (Rzero(Radd(capSum(o.items.map(function (it) { return it.value; })), o.circulating))) {
          throw new Error('No capital is advanced at all');
        }
      }
    } else if (view === 'classify') {
      o.items = x.items.map(function (it) {
        if (it.fixed && it.variable) {
          throw new Error(it.name + ' is marked fixed and variable; wages are paid out and return within each '
            + 'turnover, so variable capital is always circulating');
        }
        return it;
      });
      o.sRate = x.s_rate;
    } else if (view === 'working') {
      o.working = x.working_weeks; o.outlay = x.weekly_outlay;
    } else if (view === 'advance') {
      o.working = x.working_weeks; o.circulation = x.circulation_weeks; o.outlay = x.weekly_outlay;
      o.newOutlay = x.new_outlay; o.year = x.year_weeks;
    } else if (view === 'annual') {
      o.variable = x.variable; o.sRate = x.s_rate; o.working = x.working_weeks;
      o.circulation = x.circulation_weeks; o.year = x.year_weeks;
    } else {
      o.capital = x.merchant_capital; o.turns = x.merchant_turnovers;
    }
    return o;
  }
  function kbTuShow(view, o, unit) {
    var m = function (r) { return capMoney(r, unit); }, t = {}, said, table = null;
    var turnsText = function (n, year) { return kbFig(n) + ' a year (a ' + kbFig(year) + '-week year)'; };
    if (view === 'time') {
      var tm = kbTuTime(o.production, o.circulation, o.year);
      t.tuTurnover = kbWeeks(tm.u);
      t.tuTurnovers = turnsText(tm.n, o.year);
      t.tuWorkingShare = capPct(Rdiv(o.working, o.production));
      t.tuCirculationShare = capPct(Rdiv(o.circulation, tm.u));
      t.tuAggregate = o.capital === null ? CAP_DASH
        : m(Rmul(o.capital, tm.n)) + ' turned over on ' + m(o.capital) + ' advanced';
      said = 'A production period of ' + kbWeeks(o.production) + ' (' + kbWeeks(o.working) + ' of it working time) and '
        + kbWeeks(o.circulation) + ' of circulation make a turnover of ' + kbWeeks(tm.u) + ', so the capital turns over '
        + kbTimes(tm.n) + ' in a year of ' + kbWeeks(o.year) + '.'
        + (o.capital === null ? '' : ' The ' + m(o.capital) + ' advanced turns over ' + m(Rmul(o.capital, tm.n))
          + ' of value in the year and is still ' + m(o.capital) + ' of capital.');
    } else if (view === 'phases') {
      var u = capSum(o.stages), pt = kbTuTime(u, R0, o.year);
      t.tuTurnover = kbWeeks(u);
      t.tuTurnovers = turnsText(pt.n, o.year);
      t.tuMoney = capPct(Rdiv(o.stages[0], u));
      t.tuProductive = capPct(Rdiv(o.stages[1], u));
      t.tuCommodity = capPct(Rdiv(o.stages[2], u));
      said = 'The capital spends ' + kbWeeks(o.stages[0]) + ' as money capital, ' + kbWeeks(o.stages[1])
        + ' as productive capital and ' + kbWeeks(o.stages[2]) + ' as commodity capital: one circuit of '
        + kbWeeks(u) + ', ' + kbFig(pt.n) + ' circuits in a year of ' + kbWeeks(o.year) + '.';
    } else if (view === 'fixed') {
      var fx = kbTuFixed(o.items, o.age);
      t.tuWear = m(fx.wear) + ' a year';
      t.tuRemaining = m(fx.left) + ' after ' + kbYears(o.age);
      table = { caption: 'Each item of fixed capital after ' + kbYears(o.age),
        head: ['item', 'value', 'life', 'wear a year', 'value left'],
        rows: o.items.map(function (it) {
          var one = kbTuFixed([it], o.age);
          return [it.name, m(it.value), kbYears(it.life), m(one.wear), m(one.left)];
        }) };
      said = 'Fixed capital passes its value to the product piecemeal: ' + m(fx.wear) + ' a year in all, repairs included, '
        + 'and after ' + kbYears(o.age) + ' ' + m(fx.left) + ' is still locked in it.'
        + (Rzero(fx.lost) ? '' : ' A cheaper machine of the same kind has appeared, so ' + m(fx.lost)
          + ' of the old value is lost without any wear at all.');
    } else if (view === 'aggregate') {
      var ag = kbTuAggregate(o.items, o.circulating, o.turns);
      t.tuAggregate = m(ag.turned) + ' a year on ' + m(ag.advanced) + ' advanced';
      t.tuAverage = kbFig(ag.average) + ' turnovers a year';
      t.tuWear = m(ag.wear) + ' a year';
      said = 'The fixed parts transfer ' + m(ag.wear) + ' a year by wear; the circulating ' + m(o.circulating)
        + ' turns over ' + kbTimes(o.turns) + ', ' + m(Rmul(o.circulating, o.turns)) + '. Together ' + m(ag.turned)
        + ' is turned over on ' + m(ag.advanced) + ' advanced: ' + kbFig(ag.average) + ' turnovers a year, so the whole capital '
        + (Rzero(ag.turned) ? 'never turns over.' : 'turns over once in ' + kbYears(Rinv(ag.average)) + '.');
    } else if (view === 'classify') {
      var gs = kbTuClassify(o.items, o.sRate), many = gs.length > 1;
      var each = function (fn) { return gs.map(function (g) { return (many ? g.name + ': ' : '') + fn(g); }).join('; '); };
      t.tuFixed = each(function (g) { return 'fixed ' + m(g.fixed) + ', circulating ' + m(g.circulating); });
      t.tuVariable = each(function (g) { return 'constant ' + m(g.constant) + ', variable ' + m(g.variable); });
      t.tuS = gs.map(function (g) { return (many ? g.name + ' ' : '') + m(g.s); }).join(', ');
      table = { caption: 'Each item under both classifications',
        head: ['item', 'value', 'fixed or circulating', 'constant or variable'].concat(many ? ['capital'] : []),
        rows: o.items.map(function (it) {
          return [it.name, m(it.value), it.fixed ? 'fixed' : 'circulating', it.variable ? 'variable' : 'constant']
            .concat(many ? [it.capital] : []);
        }) };
      said = 'The same items sorted twice. Fixed against circulating is a difference in how value returns; constant against '
        + 'variable is a difference in whether new value is created. At ' + kbPctShort(o.sRate) + ' only the variable items '
        + 'yield surplus value: ' + t.tuS + '.';
    } else if (view === 'working') {
      var tied = Rmul(o.working, o.outlay);
      t.tuAdvance = m(tied);
      said = m(o.outlay) + ' a week for a working period of ' + kbWeeks(o.working) + ' ties up ' + m(tied)
        + ' before the product can be sold at all.';
    } else if (view === 'advance') {
      var ad = kbTuAdvance(o.working, o.circulation, o.outlay), turns = Rdiv(o.year, Radd(o.working, o.circulation));
      t.tuAdvance = m(ad.total) + ' = I ' + m(ad.capI) + ' + II ' + m(ad.capII);
      t.tuTurnovers = turnsText(turns, o.year);
      said = 'Capital I, ' + m(ad.capI) + ', covers the working period of ' + kbWeeks(o.working) + '; to keep working while the '
        + 'product circulates for ' + kbWeeks(o.circulation) + ' takes capital II, ' + m(ad.capII) + '. ';
      if (o.newOutlay === null) {
        t.tuFreed = m(ad.freed) + ' each working period';
        said += Rzero(ad.freed)
          ? 'The capitals relieve one another exactly, and none is set free.'
          : 'From the second turnover on, ' + m(ad.freed) + ' is set free at the close of each working period.';
      } else {
        var rel = kbTuRescale(o.working, o.circulation, o.outlay, o.newOutlay);
        t.tuFreed = Rsign(rel) >= 0 ? m(rel) + ' released' : m(Rneg(rel)) + ' more tied up';
        said += 'Moving from ' + m(o.outlay) + ' to ' + m(o.newOutlay) + ' a week '
          + (Rsign(rel) >= 0 ? 'releases ' + m(rel) + ' of circulating capital, which nobody saved.'
            : 'ties up ' + m(Rneg(rel)) + ' more.');
      }
    } else if (view === 'annual') {
      var u2 = Radd(o.working, o.circulation), an = kbTuAnnual(o.variable, o.sRate, u2, o.year);
      t.tuTurnover = kbWeeks(u2);
      t.tuTurnovers = turnsText(an.n, o.year);
      t.tuAnnualRate = capPct(an.rate);
      t.tuMassS = m(an.mass) + ' a year';
      said = m(o.variable) + ' of variable capital, exploited at ' + kbPctShort(o.sRate) + ' and turned over ' + kbTimes(an.n)
        + ' a year, yields ' + m(an.mass) + ' of surplus value: an annual rate of ' + kbPctNum(an.rate)
        + ' on the variable capital advanced. The rate in each turnover is still ' + kbPctNum(o.sRate) + '.';
    } else {
      var fr = Rmul(o.capital, o.turns);
      t.tuFreed = m(fr);
      said = 'A merchant\'s capital of ' + m(o.capital) + ' turned over ' + kbTimes(o.turns) + ' a year buys '
        + m(fr) + ' of commodities from the industrialists, who would otherwise hold that much capital in commodity form.';
    }
    return { tiles: t, status: said, table: table };
  }
  function kbTurnover(view, inst, U, opts) {
    var g = kbGuard(kbTuCheck, view, inst, opts);
    return g.refuse ? g : kbTuShow(view, g.o, U.money);
  }
"""

# ---------------------------------------------------------------------------
# schemes (Volume II, Part Three)
# ---------------------------------------------------------------------------

SCHEMES_JS = r"""
  function kbScTotal(d) { return Radd(Radd(d.c, d.v), d.s); }
  function kbScText(d) { return kbFig(d.c) + 'c + ' + kbFig(d.v) + 'v + ' + kbFig(d.s) + 's'; }
  /* Simple reproduction (Chapter 20): I(v + s) against IIc. gap > 0 leaves
     Department I's means of production without a buyer; gap < 0 leaves
     Department II's means of consumption unsold. */
  function kbScSimple(I, II) {
    var ivs = Radd(I.v, I.s);
    return { ivs: ivs, iic: II.c, gap: Rsub(ivs, II.c), exchanged: capMin(ivs, II.c), withinI: I.c,
             withinII: Radd(II.v, II.s) };
  }
  function kbScBalanceText(sim) {
    return Rzero(sim.gap) ? 'I(v + s) = ' + kbFig(sim.ivs) + ' = IIc'
      : 'I(v + s) = ' + kbFig(sim.ivs) + ', IIc = ' + kbFig(sim.iic) + ': gap ' + kbSigned(sim.gap);
  }
  /* Chapter 20, §11: renewals in kind less the wear hoarded in money. */
  function kbScFixedGap(wear, renewals) { return Rsub(renewals, wear); }
  /* Chapter 21, §1: of Department I's accumulated surplus product, the share
     whose owners sell and hoard is offered with no purchase against it; the
     rest is bought with money hoarded before. gap > 0 is product unsold. */
  function kbScHoardGap(s, accShare, hoarders) {
    var acc = Rmul(accShare, s);
    return Rsub(Rmul(hoarders, acc), Rmul(Rsub(R1, hoarders), acc));
  }
  /* One period of Marx's first example (Chapter 21, §3). Department I
     accumulates its share of s at composition kI; Department II accumulates
     exactly what makes I(v + Δv + s/x) = II(c + Δc), at composition kII.
     Each department keeps the rate of surplus value it starts with. */
  function kbScStep(I, II, share, kI, kII) {
    var accI = Rmul(share, I.s), dvI = Rdiv(accI, Radd(kI, R1)), dcI = Rsub(accI, dvI);
    var consI = Rsub(I.s, accI), dcII = Rsub(Radd(Radd(I.v, dvI), consI), II.c);
    if (Rsign(dcII) < 0) return { refused: 'shrink', dcII: dcII };
    var dvII = Rdiv(dcII, kII), accII = Radd(dcII, dvII);
    if (Rcmp(accII, II.s) > 0) return { refused: 'short', accII: accII };
    var nI = { c: Radd(I.c, dcI), v: Radd(I.v, dvI) }, nII = { c: Radd(II.c, dcII), v: Radd(II.v, dvII) };
    nI.s = Rmul(Rdiv(I.s, I.v), nI.v); nII.s = Rmul(Rdiv(II.s, II.v), nII.v);
    return { I: nI, II: nII, accI: accI, dcI: dcI, dvI: dvI, dcII: dcII, dvII: dvII, accII: accII };
  }
  function kbScRun(I, II, share, kI, kII, periods) {
    var rows = [{ I: I, II: II }], refused = null;
    for (var p = 1; p <= periods; p += 1) {
      var st = kbScStep(rows[p - 1].I, rows[p - 1].II, share, kI, kII);
      if (st.refused) { refused = { period: p, step: st }; break; }
      rows[p - 1].step = st;
      rows.push({ I: st.I, II: st.II });
    }
    return { rows: rows, refused: refused };
  }
  function kbScDept(xs) { return { c: xs[0], v: xs[1], s: xs[2] }; }
  function kbScCheck(view, x, opts) {
    var o = {};
    if (view === 'sort') {
      o.products = x.products;
      var valued = o.products.filter(function (p) { return p.value !== null; }).length;
      if (valued && valued !== o.products.length) throw new Error('Give every product a value, or none');
      return o;
    }
    o.I = kbScDept(x.I);
    if (view === 'hoard') { o.share = x.I_accumulate_share; o.hoarders = x.hoarders_share; return o; }
    o.II = kbScDept(x.II);
    if (view === 'fixed') { o.wear = x.wear_set_aside; o.renewals = x.renewals; }
    if (view === 'expanded') {
      if (Rzero(o.I.v) || Rzero(o.II.v)) throw new Error('Each department needs some v for its rate of surplus value');
      o.share = x.I_accumulate_share;
      o.kI = x.composition_I === null ? Rdiv(o.I.c, o.I.v) : x.composition_I;
      o.kII = x.composition_II === null ? Rdiv(o.II.c, o.II.v) : x.composition_II;
      if (Rzero(o.kII)) throw new Error('Department II\'s composition c/v must be more than 0 for II to balance by adding c');
      o.periods = opts.periods;
    }
    return o;
  }
  function kbScShow(view, o) {
    var t = {}, said, table = null;
    var dept = function (d) { return kbScText(d) + ' = ' + kbFig(kbScTotal(d)); };
    if (view === 'sort') {
      var list = function (k) {
        var ps = o.products.filter(function (p) { return p.use === k; });
        if (!ps.length) return 'none';
        var names = ps.map(function (p) { return p.name; }).join(', ');
        return ps[0].value === null ? names : kbFig(capSum(ps.map(function (p) { return p.value; }))) + ': ' + names;
      };
      t.scDeptI = list('production'); t.scDeptII = list('consumption');
      said = 'Each product is sorted by its use, not by what it is: means of production go to Department I, '
        + 'means of consumption to Department II.';
      return { tiles: t, status: said, table: null };
    }
    if (view === 'hoard') {
      var gap = kbScHoardGap(o.I.s, o.share, o.hoarders), acc = Rmul(o.share, o.I.s);
      t.scHoardGap = Rzero(gap) ? '0: hoarders\' sales = investors\' purchases'
        : (Rsign(gap) > 0 ? '+' + kbFig(gap) + ': ' + kbFig(gap) + ' of surplus product unsold'
          : kbFig(gap) + ': ' + kbFig(Rneg(gap)) + ' of demand without a product');
      said = 'Department I accumulates ' + kbFig(acc) + ' of its ' + kbFig(o.I.s) + 's. Those who hoard this year ('
        + kbPctShort(o.hoarders) + ') sell ' + kbFig(Rmul(o.hoarders, acc)) + ' and buy nothing; those who invest buy '
        + kbFig(Rmul(Rsub(R1, o.hoarders), acc)) + ' with money hoarded before. Sales and purchases of the surplus '
        + 'product balance only when the two are equal.';
      return { tiles: t, status: said, table: null };
    }
    var sim = kbScSimple(o.I, o.II);
    t.scDeptI = dept(o.I); t.scDeptII = dept(o.II);
    t.scBalance = kbScBalanceText(sim);
    if (view === 'simple') {
      t.scIExchange = kbFig(sim.exchanged) + ' each way' + (Rzero(sim.gap) ? ''
        : '; ' + kbFig(Rabs(sim.gap)) + ' of Department ' + (Rsign(sim.gap) > 0 ? 'I' : 'II') + '\'s product unsold');
      t.scWithinI = kbFig(sim.withinI);
      table = { caption: 'The three great exchanges', head: ['exchange', 'value'],
        rows: [['IIv + IIs, within Department II', kbFig(sim.withinII)],
               ['I(v + s) for IIc, between the departments', kbFig(sim.exchanged) + ' each way'],
               ['Ic, within Department I', kbFig(sim.withinI)]] };
      said = (Rzero(sim.gap) ? 'The scheme reproduces itself: ' : 'The scheme does not close: ') + t.scBalance + '. Of the '
        + kbFig(Radd(kbScTotal(o.I), kbScTotal(o.II))) + ' of annual product, ' + kbFig(sim.withinI)
        + ' (Ic) is means of production exchanged within Department I and is never anyone\'s revenue.';
    } else if (view === 'fixed') {
      var fg = kbScFixedGap(o.wear, o.renewals);
      t.scFixedGap = Rzero(fg) ? '0: renewals = wear hoarded'
        : (Rsign(fg) < 0 ? kbFig(fg) + ': ' + kbFig(Rneg(fg)) + ' of Department I\'s product unsold'
          : '+' + kbFig(fg) + ': Department I ' + kbFig(fg) + ' short');
      said = 'Department II sets aside ' + kbFig(o.wear) + ' of wear in money and renews ' + kbFig(o.renewals)
        + ' of fixed capital in kind. ' + (Rzero(fg) ? 'The two match, and Department I\'s product finds its buyers.'
          : Rsign(fg) < 0 ? 'The money hoarded is not spent, so ' + kbFig(Rneg(fg))
            + ' of Department I\'s product has no buyer, on an unchanged scale of reproduction.'
            : 'Renewals exceed the hoard, so Department I is ' + kbFig(fg) + ' short of the means of production demanded.');
    } else {
      var run = kbScRun(o.I, o.II, o.share, o.kI, o.kII, o.periods), rows = run.rows, last = rows[rows.length - 1];
      var start = Radd(kbScTotal(o.I), kbScTotal(o.II)), end = Radd(kbScTotal(last.I), kbScTotal(last.II));
      var cv = function (d) { return kbFig(d.c) + 'c + ' + kbFig(d.v) + 'v'; };
      t.scYear2 = rows.length > 1 ? 'I ' + cv(rows[1].I) + '; II ' + cv(rows[1].II) : 'refused in period 1';
      t.scGrowth = run.refused ? 'refused in period ' + run.refused.period
        : kbFig(start) + ' to ' + kbFig(end) + ': ' + capPct(Rsub(Rdiv(end, start), R1));
      table = { caption: 'The expanded scheme, period by period',
        head: ['period', 'Department I', 'Department II', 'product', 'I accumulates', 'II accumulates'],
        rows: rows.map(function (r, i) {
          return [String(i + 1), kbScText(r.I), kbScText(r.II), kbFig(Radd(kbScTotal(r.I), kbScTotal(r.II))),
                  r.step ? kbFig(r.step.accI) : CAP_DASH, r.step ? kbFig(r.step.accII) : CAP_DASH];
        }) };
      said = 'Department I accumulates ' + kbPctShort(o.share) + ' of its s at c/v = ' + kbFig(o.kI)
        + '; Department II accumulates exactly what balances I(v + Δv + s/x) = II(c + Δc), at c/v = ' + kbFig(o.kII) + '.';
      if (run.refused) {
        var st = run.refused.step;
        said += ' Period ' + run.refused.period + ' is refused: ' + (st.refused === 'short'
          ? 'balance needs Department II to accumulate ' + kbFig(st.accII) + ', more than its s of '
            + kbFig(last.II.s) + '.'
          : 'balance would need Department II to cut its constant capital by ' + kbFig(Rneg(st.dcII)) + '.');
      } else {
        said += ' Over ' + kbPlural(o.periods, 'period', 'periods') + ' the annual product grows from ' + kbFig(start)
          + ' to ' + kbFig(end) + '.';
      }
    }
    return { tiles: t, status: said, table: table };
  }
  function kbSchemes(view, inst, U, opts) {
    var g = kbGuard(kbScCheck, view, inst, opts);
    return g.refuse ? g : kbScShow(view, g.o);
  }
"""

# ---------------------------------------------------------------------------
# profit (Volume III, Part One)
# ---------------------------------------------------------------------------

PROFIT_JS = r"""
  function kbPrCost(c, v) { return Radd(c, v); }
  function kbPrRate(s, c, v) { return Rdiv(s, Radd(c, v)); }
  /* Engels' Chapter 4: s per turnover times n, over the whole capital advanced. */
  function kbPrAnnual(s, n, c, v) { return Rdiv(Rmul(s, n), Radd(c, v)); }
  /* Chapter 6: c changes by dc; the selling price follows by the share passed on. */
  function kbPrPriceChange(c, v, s, dc, passed) {
    var cost = Radd(Radd(c, dc), v), price = Radd(Radd(Radd(c, v), s), Rmul(dc, passed));
    var profit = Rsub(price, cost);
    return { cost: cost, price: price, profit: profit, rate: Rdiv(profit, cost) };
  }
  function kbPrCheck(view, x) {
    var o = { c: x.c, v: x.v, s: x.s, price: x.sale_price === undefined ? null : x.sale_price,
              n: x.turnovers, dc: x.c_change, passed: x.price_passed_on };
    if (o.dc !== undefined && Rsign(Radd(o.c, o.dc)) < 0) {
      throw new Error('c cannot fall below 0, and ' + kbFig(o.c) + ' ' + kbSigned(o.dc) + ' does');
    }
    return o;
  }
  function kbPrShow(view, o, unit) {
    var m = function (r) { return capMoney(r, unit); }, t = {}, said;
    var value = Radd(Radd(o.c, o.v), o.s), cost = kbPrCost(o.c, o.v);
    if (view === 'cost' || view === 'books') {
      var price = o.price === null ? value : o.price, profit = Rsub(price, cost);
      t.prCost = m(cost); t.prProfit = m(profit);
      if (view === 'books') t.prRate = capPct(Rdiv(profit, cost));
      said = 'Cost price k = c + v = ' + m(cost) + '; the value is ' + m(value) + '. Sold at ' + m(price) + ', the profit is '
        + m(profit) + (Rcmp(price, value) < 0 ? ', ' + m(Rsub(value, price)) + ' below value'
          : Rcmp(price, value) > 0 ? ', ' + m(Rsub(price, value)) + ' above value' : ', at value') + '.'
        + (view === 'books' ? ' The books call ' + m(profit) + ' a return on the ' + m(cost)
          + ' laid out; the analysis calls the ' + m(o.s) + ' surplus value produced by ' + m(o.v) + ' of variable capital.' : '');
    } else if (view === 'rate' || view === 'relation') {
      t.prRate = capPct(kbPrRate(o.s, o.c, o.v)); t.prSRate = capPct(Rdiv(o.s, o.v));
      said = 'The same ' + m(o.s) + ' of surplus value measured two ways: against v it is s′ = ' + kbPctNum(Rdiv(o.s, o.v))
        + '; against the whole capital c + v = ' + m(cost) + ' it is p′ = ' + kbPctNum(kbPrRate(o.s, o.c, o.v))
        + '. p′ = s′·v/C, with c/v = ' + kbFig(Rdiv(o.c, o.v)) + '.';
    } else if (view === 'turnover') {
      var annual = kbPrAnnual(o.s, o.n, o.c, o.v);
      t.prAnnual = capPct(annual); t.prRate = capPct(kbPrRate(o.s, o.c, o.v)); t.prSRate = capPct(Rdiv(o.s, o.v));
      said = 'v = ' + m(o.v) + ' turned over ' + kbTimes(o.n) + ' a year at s′ = ' + kbPctNum(Rdiv(o.s, o.v)) + ' yields '
        + m(Rmul(o.s, o.n)) + ' of surplus value on C = ' + m(cost) + ': an annual rate of profit of ' + kbPctNum(annual) + '.';
    } else if (view === 'economy') {
      var ec = Radd(Radd(o.c, o.dc), o.v), er = Rdiv(o.s, ec);
      t.prRate = capPct(er); t.prCost = m(ec);
      said = 'Changing c by ' + kbSigned(o.dc) + ' with v and s unchanged moves p′ from ' + kbPctNum(kbPrRate(o.s, o.c, o.v))
        + ' to ' + kbPctNum(er) + '.';
    } else {
      var pc = kbPrPriceChange(o.c, o.v, o.s, o.dc, o.passed);
      t.prRate = capPct(pc.rate); t.prCost = m(pc.cost); t.prProfit = m(pc.profit);
      said = 'c changes by ' + kbSigned(o.dc) + ' and ' + kbPctShort(o.passed) + ' of the change is passed on, so the product sells at '
        + m(pc.price) + ' against a cost price of ' + m(pc.cost) + ': profit ' + m(pc.profit) + ', p′ ' + kbPctNum(pc.rate) + '.';
    }
    return { tiles: t, status: said, table: null };
  }
  function kbProfit(view, inst, U, opts) {
    var g = kbGuard(kbPrCheck, view, inst, opts);
    return g.refuse ? g : kbPrShow(view, g.o, U.money);
  }
"""

# ---------------------------------------------------------------------------
# prices (Volume III, Part Two; Chapters 17-19)
# ---------------------------------------------------------------------------

PRICES_JS = r"""
  function kbPpCv(x) { return kbFig(x.c) + 'c + ' + kbFig(x.v) + 'v'; }
  /* A sphere: {name, c, v, used, s}. Its rate of profit at value, s/(c + v). */
  function kbPpRates(spheres) {
    return spheres.map(function (x) { return Rdiv(x.s, Radd(x.c, x.v)); });
  }
  /* Chapter 9, inputs at value: the general rate is total s over total
     capital; each sphere's price of production is its cost price (used-up c
     + v) plus the general rate on its capital. Premiums (Chapter 12) are
     extra rates for named spheres paid out of the same total: the base rate
     falls so that total profit still equals total s. */
  function kbPpProduction(spheres, premiums) {
    var K = R0, S = R0, P = R0;
    spheres.forEach(function (x, i) {
      var k = Radd(x.c, x.v);
      K = Radd(K, k); S = Radd(S, x.s); P = Radd(P, Rmul(premiums[i], k));
    });
    var base = Rdiv(Rsub(S, P), K), prices = [], values = [], profits = [];
    spheres.forEach(function (x, i) {
      var profit = Rmul(Radd(base, premiums[i]), Radd(x.c, x.v)), cost = Radd(x.used, x.v);
      profits.push(profit); prices.push(Radd(cost, profit)); values.push(Radd(cost, x.s));
    });
    return { rate: base, prices: prices, values: values, profits: profits, S: S, K: K,
             totalPrice: capSum(prices), totalValue: capSum(values), totalProfit: capSum(profits) };
  }
  /* Chapter 11: the money wage rises by w; the extra wages come out of
     surplus value; the new general rate is the average capital's reduced
     profit over its enlarged advance, (r·(c + v) − w·v) / (c + v·(1 + w)).
     Marx: 15 on 105 is 1/7. */
  function kbPpNewRate(avg, rate, w) {
    var k = Radd(avg.c, avg.v), extra = Rmul(w, avg.v);
    return Rdiv(Rsub(Rmul(rate, k), extra), Radd(k, extra));
  }
  function kbPpWageRise(spheres, avg, rate, w) {
    var r2 = kbPpNewRate(avg, rate, w);
    var before = spheres.map(function (x) { return Radd(Radd(x.used, x.v), Rmul(rate, Radd(x.c, x.v))); });
    var after = spheres.map(function (x) {
      var v2 = Rmul(x.v, Radd(R1, w));
      return Radd(Radd(x.used, v2), Rmul(r2, Radd(x.c, v2)));
    });
    return { rate: r2, before: before, after: after };
  }
  /* Chapter 17: merchant's capital M (and its own circulation costs) shares
     in the averaging; the industrialist sells at cost price + the rate on his
     capital, the merchant adds his costs and the rate on M + costs. */
  function kbPpMerchant(spheres, M, costs) {
    var K = R0, S = R0, k = R0;
    spheres.forEach(function (x) { K = Radd(K, Radd(x.c, x.v)); S = Radd(S, x.s); k = Radd(k, Radd(x.used, x.v)); });
    var rate = Rdiv(S, Radd(Radd(K, M), costs));
    var industrial = Radd(k, Rmul(rate, K)), mprofit = Rmul(rate, Radd(M, costs));
    return { rate: rate, industrial: industrial, merchant: Radd(Radd(industrial, costs), mprofit), mprofit: mprofit,
             value: Radd(k, S), S: S };
  }
  /* Chapter 18: the year's rate spread over the merchant's turnovers. */
  function kbPpMarkup(rate, turns) { return Rdiv(rate, turns); }
  function kbPpCheck(view, x) {
    var o = {};
    if (view === 'merchant-turnover') {
      o.rate = x.profit_rate; o.turns = x.merchant_turnovers; o.M = x.merchant_capital;
      return o;
    }
    o.spheres = x.spheres.map(function (r) {
      var sp = { name: r.name, c: r.c, v: r.v, used: r.c_used === null ? r.c : r.c_used };
      if (Rzero(Radd(sp.c, sp.v))) throw new Error(sp.name + ' has no capital at all');
      if (Rcmp(sp.used, sp.c) > 0) {
        throw new Error('The used-up c of ' + sp.name + ' (' + kbFig(sp.used) + ') is more than its c (' + kbFig(sp.c) + ')');
      }
      if (view !== 'wage-rise') {
        var e = r.s_rate !== null ? r.s_rate : x.s_rate;
        if (e === null) throw new Error(sp.name + ' has no rate of surplus value, and none is given for all the spheres');
        sp.s = Rmul(e, sp.v);
      }
      return sp;
    });
    var names = o.spheres.map(function (sp) { return sp.name; });
    if (view === 'production') {
      o.premiums = o.spheres.map(function () { return R0; });
      x.premiums.forEach(function (p) {
        var i = names.indexOf(p.sphere);
        if (i < 0) throw new Error('A premium names "' + p.sphere + '", which is not one of the spheres');
        o.premiums[i] = p.rate;
      });
    } else if (view === 'wage-rise') {
      o.rate = x.profit_rate; o.w = x.wage_rise;
      if (Rcmp(o.w, R(-1n)) <= 0) throw new Error('Wages cannot fall by 100% or more');
      if (x.average === '') {
        o.avg = { name: '', c: capSum(o.spheres.map(function (sp) { return sp.c; })),
                  v: capSum(o.spheres.map(function (sp) { return sp.v; })) };
      } else {
        var i = names.indexOf(x.average);
        if (i < 0) throw new Error('The average capital is named "' + x.average + '", which is not one of the spheres');
        o.avg = o.spheres[i];
      }
      if (Rsign(kbPpNewRate(o.avg, o.rate, o.w)) < 0) {
        throw new Error('A wage rise of ' + kbPctShort(o.w) + ' takes more than the average capital\'s whole profit');
      }
    } else if (view === 'merchant') {
      o.M = x.merchant_capital; o.costs = x.merchant_costs === null ? R0 : x.merchant_costs;
    }
    return o;
  }
  function kbPpShow(view, o, unit) {
    var m = function (r) { return capMoney(r, unit); }, t = {}, said, table = null;
    if (view === 'rates') {
      var rates = kbPpRates(o.spheres);
      t.ppRates = rates.map(capPct).join(', ');
      table = { caption: 'Each sphere at value', head: ['sphere', 'capital', 's', 'value', 'rate of profit'],
        rows: o.spheres.map(function (x, i) {
          return [x.name, kbPpCv(x), m(x.s), m(Radd(Radd(x.used, x.v), x.s)), kbPctNum(rates[i])];
        }) };
      said = 'Sold at their values, capitals of different composition make different rates of profit: '
        + o.spheres.map(function (x, i) { return x.name + ' ' + kbPctNum(rates[i]); }).join(', ') + '.';
    } else if (view === 'production') {
      var pp = kbPpProduction(o.spheres, o.premiums);
      t.ppAverage = capPct(pp.rate);
      t.ppPrices = pp.prices.map(m).join(', ');
      t.ppTotals = 'values ' + m(pp.totalValue) + ' = prices ' + m(pp.totalPrice) + '; s ' + m(pp.S) + ' = profit ' + m(pp.totalProfit);
      table = { caption: 'Values and prices of production',
        head: ['sphere', 'capital', 'used-up c', 's', 'value', 'cost price', 'profit', 'price of production', 'price − value'],
        rows: o.spheres.map(function (x, i) {
          return [x.name, kbPpCv(x), m(x.used), m(x.s), m(pp.values[i]), m(Radd(x.used, x.v)), m(pp.profits[i]),
                  m(pp.prices[i]), capSigned(Rsub(pp.prices[i], pp.values[i]), m)];
        }) };
      var anyPrem = o.premiums.some(function (p) { return !Rzero(p); });
      said = 'Total surplus value ' + m(pp.S) + ' over a total capital of ' + m(pp.K) + ' gives a general rate of '
        + kbPctNum(pp.rate) + (anyPrem ? ' after the premiums, which are paid out of the same total' : '')
        + '. Each sphere sells at its cost price plus that rate on its capital; prices depart from values sphere by sphere, '
        + 'and the totals agree.';
    } else if (view === 'wage-rise') {
      var wr = kbPpWageRise(o.spheres, o.avg, o.rate, o.w);
      t.ppAverage = capPct(wr.rate);
      t.ppPrices = wr.after.map(m).join(', ');
      var dir = function (i) { var c = Rcmp(wr.after[i], wr.before[i]); return c > 0 ? 'rises' : c < 0 ? 'falls' : 'unchanged'; };
      table = { caption: 'Prices of production before and after the wage rise',
        head: ['sphere', 'capital', 'before', 'after', 'direction'],
        rows: o.spheres.map(function (x, i) { return [x.name, kbPpCv(x), m(wr.before[i]), m(wr.after[i]), dir(i)]; }) };
      said = 'Money wages rise by ' + kbPctShort(o.w) + ' and the extra wages come out of surplus value. The average capital ('
        + (o.avg.name || 'all the spheres together') + ', ' + kbPpCv(o.avg) + ') now makes '
        + m(Rsub(Rmul(o.rate, Radd(o.avg.c, o.avg.v)), Rmul(o.w, o.avg.v))) + ' on '
        + m(Radd(Radd(o.avg.c, o.avg.v), Rmul(o.w, o.avg.v))) + ', so the general rate goes from ' + kbPctNum(o.rate) + ' to '
        + kbPctNum(wr.rate) + ', reckoned over the capital advanced after the rise. Prices: '
        + o.spheres.map(function (x, i) { return x.name + ' ' + dir(i); }).join(', ') + '.';
    } else if (view === 'merchant') {
      var mp = kbPpMerchant(o.spheres, o.M, o.costs);
      t.ppAverage = capPct(mp.rate);
      t.ppMerchantPrice = 'industrial ' + m(mp.industrial) + '; merchant ' + m(mp.merchant);
      said = 'Surplus value of ' + m(mp.S) + ' is averaged over the industrial capital and the merchant\'s ' + m(o.M)
        + (Rzero(o.costs) ? '' : ' plus ' + m(o.costs) + ' of circulation costs') + ': ' + kbPctNum(mp.rate)
        + '. The industrialists sell at ' + m(mp.industrial) + ', the merchant at ' + m(mp.merchant) + ', drawing ' + m(mp.mprofit)
        + ' of profit; the merchant\'s price is the value, ' + m(mp.value) + (Rzero(o.costs) ? '.' : ', plus the costs.');
    } else {
      var mk = kbPpMarkup(o.rate, o.turns);
      t.ppMarkup = capPct(mk);
      t.ppMerchantPrice = 'buys at ' + m(o.M) + ', sells at ' + m(Rmul(o.M, Radd(R1, mk)));
      said = 'At ' + kbPctNum(o.rate) + ' a year and ' + kbFig(o.turns) + ' turnovers, the merchant adds ' + kbPctNum(mk)
        + ' each time: a faster turnover lowers the mark-up on each sale, not the rate on the capital.';
    }
    return { tiles: t, status: said, table: table };
  }
  function kbPrices(view, inst, U, opts) {
    var g = kbGuard(kbPpCheck, view, inst, opts);
    return g.refuse ? g : kbPpShow(view, g.o, U.money);
  }
"""

# ---------------------------------------------------------------------------
# tendency (Volume III, Part Three)
# ---------------------------------------------------------------------------

TENDENCY_JS = r"""
  /* A step list: empty = 0 every period; one figure = every period; else one per period. */
  function kbTeAt(steps, i) { return steps.length === 0 ? R0 : (steps.length === 1 ? steps[0] : steps[i]); }
  /* The rate of profit period by period. Each period, in this order: the
     whole capital grows by capital_growth (c and v alike); c_step is added to
     c; c cheapens by c_cheapening; s' rises by s_rate_step. */
  function kbTePath(c, v, e, cSteps, growth, eSteps, cheap, periods) {
    var rows = [{ c: c, v: v, e: e }];
    for (var i = 0; i < periods; i += 1) {
      var g = Radd(R1, kbTeAt(growth, i)), p = rows[i];
      var nc = Rmul(Radd(Rmul(p.c, g), kbTeAt(cSteps, i)), Rsub(R1, kbTeAt(cheap, i)));
      rows.push({ c: nc, v: Rmul(p.v, g), e: Radd(p.e, kbTeAt(eSteps, i)) });
    }
    rows.forEach(function (r) { r.s = Rmul(r.e, r.v); r.rate = Rdiv(r.s, Radd(r.c, r.v)); });
    return rows;
  }
  /* Chapter 15, absolute over-accumulation: the added capital sets no more
     labour in motion, so the mass of surplus value stays; devaluation removes
     a share of the swollen capital and the same mass is reckoned on less. */
  function kbTeOver(c, v, e, added, devalued) {
    var s = Rmul(e, v), k = Radd(c, v), k2 = Radd(k, added), k3 = Rmul(k2, Rsub(R1, devalued));
    return { s: s, before: Rdiv(s, k), after: Rdiv(s, k2), restored: Rdiv(s, k3), k: k, k2: k2, k3: k3 };
  }
  function kbTeCheck(view, x, opts) {
    var o = { c: x.c, v: x.v, e: x.s_rate };
    if (view === 'overaccumulation') {
      o.added = x.added_capital; o.devalued = x.devalued_share;
      if (Requ(o.devalued, R1)) throw new Error('Devaluing the whole capital leaves nothing to reckon a rate on');
      return o;
    }
    o.periods = opts.periods;
    var steps = function (list, what) {
      if (list.length > 1 && list.length !== o.periods) {
        throw new Error(what + ' lists ' + list.length + ' figures for ' + kbPlural(o.periods, 'period', 'periods')
          + '; give one figure for every period, or one per period');
      }
      return list;
    };
    o.cSteps = steps(x.c_step, 'The rise in c');
    o.growth = steps(x.capital_growth, 'The growth of capital');
    o.growth.forEach(function (g) { if (Rcmp(g, R(-1n)) <= 0) throw new Error('Capital cannot shrink by 100% or more in a period'); });
    o.eSteps = view === 'counter' ? steps(x.s_rate_step, 'The rise in s′') : [];
    o.cheap = view === 'counter' ? steps(x.c_cheapening, 'The cheapening of c') : [];
    o.cheap.forEach(function (ch) { if (Requ(ch, R1)) throw new Error('c cannot cheapen to nothing'); });
    kbTePath(o.c, o.v, o.e, o.cSteps, o.growth, o.eSteps, o.cheap, o.periods).forEach(function (r, i) {
      if (Rsign(r.c) < 0) throw new Error('c falls below 0 in period ' + i);
      if (Rsign(r.e) < 0) throw new Error('s′ falls below 0 in period ' + i);
    });
    return o;
  }
  function kbTeShow(view, o, unit) {
    var m = function (r) { return capMoney(r, unit); }, t = {}, said, table;
    if (view === 'overaccumulation') {
      var ov = kbTeOver(o.c, o.v, o.e, o.added, o.devalued), fin = Rzero(o.devalued) ? ov.after : ov.restored;
      t.teRate = capPct(fin); t.teMass = m(ov.s);
      table = { caption: 'The same mass of surplus value on a changing capital', head: ['capital', 'surplus value', 'rate of profit'],
        rows: [[m(ov.k), m(ov.s), kbPctNum(ov.before)], [m(ov.k2) + ' after the addition', m(ov.s), kbPctNum(ov.after)]]
          .concat(Rzero(o.devalued) ? [] : [[m(ov.k3) + ' after devaluation', m(ov.s), kbPctNum(ov.restored)]]) };
      said = 'A capital of ' + m(ov.k) + ' yields ' + m(ov.s) + '. The added ' + m(o.added) + ' sets no more labour in motion, so the '
        + 'mass stays at ' + m(ov.s) + ' and p′ goes from ' + kbPctNum(ov.before) + ' to ' + kbPctNum(ov.after) + '.'
        + (Rzero(o.devalued) ? '' : ' Devaluing ' + kbPctShort(o.devalued) + ' of the capital leaves ' + m(ov.k3)
          + ', and the same mass is ' + kbPctNum(ov.restored) + ' of it.');
      return { tiles: t, status: said, table: table };
    }
    var rows = kbTePath(o.c, o.v, o.e, o.cSteps, o.growth, o.eSteps, o.cheap, o.periods), last = rows[rows.length - 1];
    t.teRate = capPct(last.rate); t.teMass = m(last.s);
    table = { caption: 'The rate of profit, period by period', head: ['period', 'c', 'v', 's', 'c/v', 's′', 'p′'],
      rows: rows.map(function (r, i) {
        return [String(i), m(r.c), m(r.v), m(r.s), kbFig(Rdiv(r.c, r.v)), kbPctNum(r.e), kbPctNum(r.rate)];
      }) };
    said = 'From ' + kbFig(o.c) + 'c + ' + kbFig(o.v) + 'v at s′ = ' + kbPctNum(o.e) + ', p′ goes from ' + kbPctNum(rows[0].rate)
      + ' to ' + kbPctNum(last.rate) + ' over ' + kbPlural(o.periods, 'period', 'periods') + ', while the mass of profit goes from '
      + m(rows[0].s) + ' to ' + m(last.s) + '.';
    if (view === 'counter') {
      var bare = kbTePath(o.c, o.v, o.e, o.cSteps, o.growth, [], [], o.periods), bl = bare[bare.length - 1];
      var fall = Rmul(Rsub(rows[0].rate, bl.rate), R(100n)), off = Rmul(Rsub(last.rate, bl.rate), R(100n));
      t.teOffset = Rsign(fall) > 0 ? kbFig(off) + ' of ' + kbFig(fall) + ' points' : 'no fall to offset';
      said += ' Without the counteracting influences it would end at ' + kbPctNum(bl.rate) + '; they offset '
        + (Rsign(fall) > 0 ? kbFig(off) + ' of the ' + kbFig(fall) + ' percentage points of that fall.' : 'nothing, because there is no fall.');
    }
    return { tiles: t, status: said, table: table };
  }
  function kbTendency(view, inst, U, opts) {
    var g = kbGuard(kbTeCheck, view, inst, opts);
    return g.refuse ? g : kbTeShow(view, g.o, U.money);
  }
"""

# ---------------------------------------------------------------------------
# interest (Volume III, Part Five)
# ---------------------------------------------------------------------------

INTEREST_JS = r"""
  /* Chapters 21-23: profit at the general rate on the capital employed;
     interest at the rate on the capital borrowed; profit of enterprise is
     the rest, after any hired manager's salary. */
  function kbInSplit(capital, rate, i, principal, salary) {
    var profit = Rmul(capital, rate), interest = Rmul(principal, i);
    return { profit: profit, interest: interest, enterprise: Rsub(Rsub(profit, interest), salary) };
  }
  /* Chapter 22: 0 < i < p' is the normal range; outside it is not an error. */
  function kbInBound(i, rate) { return Rsign(i) > 0 && Rcmp(i, rate) < 0; }
  /* Chapter 29: capitalisation, income / rate. */
  function kbInPrice(income, i) { return Rdiv(income, i); }
  /* Chapter 24: principal × (1 + rate)^years, exact over BigInt. */
  function kbInCompound(principal, rate, years) { return Rmul(principal, Rpow(Radd(R1, rate), years)); }
  /* Decimal digits before the point. */
  function kbInDigits(r) { return String(kbFloor(Rabs(r))).length; }
  /* Chapter 36: the whole surplus goes to the usurer each year; interest not
     covered by it is added to the debt and bears interest in turn. */
  function kbInUsury(debt, i, surplus, holding, years) {
    var rows = [], d = debt, ruin = null, repaid = null;
    for (var y = 1; y <= years; y += 1) {
      var interest = Rmul(d, i), next = Rsub(Radd(d, interest), surplus);
      if (Rsign(next) <= 0) { rows.push({ year: y, interest: interest, debt: R0 }); repaid = y; break; }
      rows.push({ year: y, interest: interest, debt: next });
      d = next;
      if (ruin === null && Rcmp(d, holding) > 0) ruin = y;
    }
    return { rows: rows, ruin: ruin, repaid: repaid };
  }
  /* A sum that may be enormous: exact when it is short, otherwise its closed
     form and the number of digits before the point. */
  function kbInSum(principal, rate, years, value, unit) {
    var form = capMoney(principal, unit) + ' × (' + Rtext(Radd(R1, rate)) + ')^' + years, digits = kbInDigits(value);
    var name = unit === 's' ? 'shillings' : unit === '£' ? 'pounds' : 'hours';
    if (Rtext(value).length <= 40) return form + ' = ' + capMoney(value, unit);
    return form + ': ' + kbPlural(digits, 'digit', 'digits') + ' before the point, in ' + name;
  }
  function kbInCheck(view, x) {
    var o = {};
    Object.keys(x).forEach(function (k) { o[k] = x[k]; });
    if (view === 'split' || view === 'bounds') {
      if (o.principal === null) o.principal = o.capital;
      if (o.manager_salary === null) o.manager_salary = R0;
    } else if (view === 'compound') {
      o.years = Number(o.years.n);
      if (o.years > 5000) throw new Error('This lab compounds for at most 5,000 years');
      [o.interest_rate, o.real_growth].forEach(function (r) {
        if (String(r.n).length + String(r.d).length > 12) throw new Error('Give each rate with at most 12 digits in all');
      });
    } else if (view === 'usury') {
      o.years = Number(o.years.n);
      if (o.years > 100) throw new Error('This lab follows a debt for at most 100 years');
      if (String(o.interest_rate.d).length > 4) throw new Error('Give the usurer\'s rate with a denominator of at most four digits');
    }
    return o;
  }
  function kbInShow(view, o, unit) {
    var m = function (r) { return capMoney(r, unit); }, t = {}, said, table = null;
    if (view === 'split' || view === 'bounds') {
      var sp = kbInSplit(o.capital, o.profit_rate, o.interest_rate, o.principal, o.manager_salary);
      t.inInterest = m(sp.interest); t.inEnterprise = m(sp.enterprise);
      said = m(o.capital) + ' at the average rate of ' + kbPctShort(o.profit_rate) + ' makes ' + m(sp.profit) + '; '
        + m(sp.interest) + ' goes to the lender as interest' + (Requ(o.principal, o.capital) ? '' : ' on the ' + m(o.principal) + ' borrowed')
        + (Rzero(o.manager_salary) ? '' : ', ' + m(o.manager_salary) + ' to a hired manager') + ', and ' + m(sp.enterprise)
        + ' stays as profit of enterprise.';
      if (view === 'bounds') {
        var inside = kbInBound(o.interest_rate, o.profit_rate);
        t.inBound = inside ? '0 < ' + kbPctShort(o.interest_rate) + ' < ' + kbPctShort(o.profit_rate)
          : 'breached: ' + (Rsign(o.interest_rate) <= 0 ? kbPctShort(o.interest_rate) + ' ≤ 0'
            : kbPctShort(o.interest_rate) + ' ≥ ' + kbPctShort(o.profit_rate));
        said += inside ? ' The rate of interest lies between 0 and the rate of profit; nothing in the chapter fixes where.'
          : ' The rate of interest is outside 0 < i < p′, so the interest is not paid out of this profit.';
      }
    } else if (view === 'capitalise') {
      var price = kbInPrice(o.income, o.interest_rate);
      t.inPrice = m(price);
      said = 'A claim to ' + m(o.income) + ' a year, capitalised at ' + kbPctShort(o.interest_rate) + ', is priced at ' + m(price)
        + '. Nothing stands behind the figure but the income and the rate.';
    } else if (view === 'compound') {
      var cs = kbInCompound(o.principal, o.interest_rate, o.years), rs = kbInCompound(o.principal, o.real_growth, o.years);
      t.inCompound = kbInSum(o.principal, o.interest_rate, o.years, cs, unit);
      t.inReal = kbInSum(o.principal, o.real_growth, o.years, rs, unit);
      var c = Rcmp(cs, rs);
      said = 'Over ' + kbPlural(o.years, 'year', 'years') + ', ' + m(o.principal) + ' at ' + kbPctShort(o.interest_rate)
        + ' compound has ' + kbPlural(kbInDigits(cs), 'digit', 'digits') + ' before the point; growing with the product at '
        + kbPctShort(o.real_growth) + ' it has ' + kbPlural(kbInDigits(rs), 'digit', 'digits') + '. '
        + (c > 0 ? 'The compound sum outgrows the real growth.' : c < 0 ? 'The real growth is the larger.' : 'They are equal.');
    } else {
      var us = kbInUsury(o.debt, o.interest_rate, o.surplus, o.holding_value, o.years);
      t.inInterest = m(Rmul(o.debt, o.interest_rate)) + ' in year 1';
      t.inYearsToRuin = us.ruin !== null ? 'year ' + us.ruin
        : (us.repaid !== null ? 'repaid in year ' + us.repaid : 'never within ' + kbPlural(o.years, 'year', 'years'));
      var cell = function (r) { var s = m(r); return s.length <= 24 ? s : kbApprox(r, unit); };
      table = { caption: 'The debt year by year (≈ marks an exact figure rounded to two decimals)',
        head: ['year', 'interest', 'debt at the year\'s end'],
        rows: us.rows.map(function (r) { return [String(r.year), cell(r.interest), cell(r.debt)]; }) };
      said = 'The usurer takes the whole surplus of ' + m(o.surplus) + ' each year; interest at ' + kbPctShort(o.interest_rate)
        + ' that it does not cover is added to the debt and bears interest in turn. '
        + (us.ruin !== null ? 'In year ' + us.ruin + ' the debt passes the holding\'s value of ' + m(o.holding_value) + '.'
          : us.repaid !== null ? 'The debt is paid off in year ' + us.repaid + '.'
            : 'Within ' + kbPlural(o.years, 'year', 'years') + ' the debt never passes the holding\'s ' + m(o.holding_value) + '.');
    }
    return { tiles: t, status: said, table: table };
  }
  function kbInterest(view, inst, U, opts) {
    var g = kbGuard(kbInCheck, view, inst, opts);
    return g.refuse ? g : kbInShow(view, g.o, U.money);
  }
"""

# ---------------------------------------------------------------------------
# rent (Volume III, Part Six)
# ---------------------------------------------------------------------------

RENT_JS = r"""
  /* Chapter 37: the price of land is rent capitalised at the rate of interest. */
  function kbRtPrice(rent, i) { return Rdiv(rent, i); }
  /* Chapter 38: the steam user's cost plus the average profit regulates the
     price. Marx's surplus profit is the water user's profit less the steam
     user's; against its own individual price of production it is the price
     less that. */
  function kbRtWaterfall(steam, water, rate) {
    var price = Rmul(steam, Radd(R1, rate)), own = Rmul(water, Radd(R1, rate));
    return { price: price, own: own, marx: Rsub(Rsub(price, water), Rsub(price, steam)), againstOwn: Rsub(price, own) };
  }
  /* Rows {soil, capital, output}, one per investment, grouped into soils in
     first-appearance order; each investment's individual price of
     production per unit. */
  function kbRtInvestments(rows, rate) {
    var soils = [], at = {}, invs = [];
    rows.forEach(function (r) {
      if (at[r.soil] === undefined) { at[r.soil] = soils.length; soils.push({ name: r.soil, n: 0 }); }
      var sl = soils[at[r.soil]];
      sl.n += 1;
      invs.push({ soil: at[r.soil], k: sl.n, capital: r.capital, output: r.output,
                  ppu: Rdiv(Rmul(r.capital, Radd(R1, rate)), r.output) });
    });
    return { soils: soils, invs: invs };
  }
  /* Which investments are in use and which regulates. Without a market limit
     every investment is in use and the least productive regulates (ties: the
     first listed). With a limit, the most productive are taken first until
     the market is supplied, and the last one taken regulates. A named
     regulator ("B" or "B1" for B's first dose, "B2" for its second) overrides. */
  function kbRtRegulate(invs, soils, regulating, limit) {
    var use = invs.map(function () { return limit === null; }), reg = -1;
    if (limit !== null) {
      var order = invs.map(function (x, i) { return i; }).sort(function (a, b) {
        var c = Rcmp(invs[a].ppu, invs[b].ppu); return c !== 0 ? c : a - b;
      });
      var got = R0;
      for (var j = 0; j < order.length && Rcmp(got, limit) < 0; j += 1) {
        use[order[j]] = true; got = Radd(got, invs[order[j]].output); reg = order[j];
      }
      if (Rcmp(got, limit) < 0) return { error: 'The soils listed supply only ' + kbFig(got) + ' against a market of ' + kbFig(limit) };
    } else {
      invs.forEach(function (x, i) { if (reg < 0 || Rcmp(x.ppu, invs[reg].ppu) > 0) reg = i; });
    }
    if (regulating !== '' && regulating !== 'auto') {
      var hit = -1;
      invs.forEach(function (x, i) {
        var id = soils[x.soil].name;
        if (regulating === id + x.k || (x.k === 1 && regulating === id)) hit = i;
      });
      if (hit < 0) return { error: 'The regulating investment "' + regulating + '" is not one of the investments listed' };
      if (!use[hit]) return { error: 'The regulating investment "' + regulating + '" is not in use' };
      reg = hit;
    }
    return { use: use, reg: reg, price: invs[reg].ppu };
  }
  /* Rent on each soil: over its investments in use, output × price less the
     capital and the average profit on it. */
  function kbRtRents(soils, invs, use, price, rate) {
    var rents = soils.map(function () { return R0; });
    invs.forEach(function (x, i) {
      if (use[i]) rents[x.soil] = Radd(rents[x.soil], Rsub(Rmul(x.output, price), Rmul(x.capital, Radd(R1, rate))));
    });
    return { rents: rents, total: capSum(rents) };
  }
  /* Which of Chapters 41-44's cases an instance is. The price moves against
     the former price (default: what the least productive first doses would
     set, differential rent I on every soil listed); "worst-soil" is Chapter
     44's case, a regulating additional dose under which the worst soil's
     first dose, in use, earns a surplus profit. */
  function kbRtCase(invs, reg, use, price, former) {
    var worst = -1;
    invs.forEach(function (x, i) { if (x.k === 1 && (worst < 0 || Rcmp(x.ppu, invs[worst].ppu) > 0)) worst = i; });
    var c = Rcmp(price, former === null ? invs[worst].ppu : former);
    return { move: c === 0 ? 'constant' : (c < 0 ? 'falling' : 'rising'),
             worstSoil: invs[reg].k > 1 && use[worst] && Rcmp(invs[worst].ppu, price) < 0 };
  }
  /* Chapter 45: agricultural value against the price of production
     equalised over agriculture and industry; absolute rent is at most the
     difference, and at most what the market limit allows. */
  function kbRtAbsolute(agri, ind, e, limit) {
    var ka = Radd(agri.c, agri.v), ki = Radd(ind.c, ind.v);
    var rate = Rdiv(Rmul(e, Radd(agri.v, ind.v)), Radd(ka, ki));
    var value = Radd(ka, Rmul(e, agri.v)), price = Rmul(ka, Radd(R1, rate));
    var cap = limit === null ? value : capMin(value, limit), abs = Rsub(cap, price);
    return { rate: rate, value: value, price: price, absolute: Rsign(abs) > 0 ? abs : R0 };
  }
  function kbRtCheck(view, x) {
    var o = {};
    if (view === 'price') {
      o.rent = x.rent; o.i = x.interest_rate; o.improvement = x.improvement_interest === null ? R0 : x.improvement_interest;
      if (Rcmp(o.improvement, o.rent) > 0) throw new Error('The interest on improvements is more than the whole payment');
    } else if (view === 'waterfall') {
      o.steam = x.cost_steam; o.water = x.cost_water; o.rate = x.profit_rate;
    } else if (view === 'dr1' || view === 'dr2') {
      o.rate = x.profit_rate;
      var g = kbRtInvestments(x.soils, o.rate);
      o.soils = g.soils; o.invs = g.invs;
      if (o.soils.length > 6) throw new Error('This lab takes at most 6 soils, and there are ' + o.soils.length);
      o.soils.forEach(function (sl) {
        if (view === 'dr1' && sl.n > 1) throw new Error('Differential rent I takes one investment per soil, and ' + sl.name + ' has ' + sl.n);
        if (sl.n > 6) throw new Error(sl.name + ' has ' + sl.n + ' investments; this lab takes at most 6 a soil');
      });
      o.reg = kbRtRegulate(o.invs, o.soils, x.regulating, x.market_limit);
      if (o.reg.error) throw new Error(o.reg.error);
      o.former = x.former_price === undefined ? null : x.former_price;
    } else {
      o.agri = { c: x.agri[0], v: x.agri[1] }; o.ind = { c: x.industry[0], v: x.industry[1] };
      if (Rzero(Radd(o.agri.c, o.agri.v))) throw new Error('Agriculture has no capital at all');
      o.e = x.s_rate; o.limit = x.market_limit;
    }
    return o;
  }
  function kbRtShow(view, o, unit, qty, priceCase) {
    var m = function (r) { return capMoney(r, unit); }, t = {}, said, table = null;
    if (view === 'price') {
      var lp = kbRtPrice(o.rent, o.i), tr = Rsub(o.rent, o.improvement);
      t.rtPrice = m(lp); t.rtTrueRent = m(tr);
      said = 'A yearly payment of ' + m(o.rent) + ' capitalised at ' + kbPctShort(o.i) + ' is a price of ' + m(lp) + '.'
        + (Rzero(o.improvement) ? ' All of it is ground rent proper.'
          : ' Of the payment, ' + m(o.improvement) + ' is interest on capital sunk in the land, so the true rent is ' + m(tr)
            + ' and the land as such is priced at ' + m(kbRtPrice(tr, o.i)) + '.');
    } else if (view === 'waterfall') {
      var wf = kbRtWaterfall(o.steam, o.water, o.rate);
      t.rtPrice = m(wf.price);
      t.rtSurplusProfit = kbMoneyV(wf.marx, unit) + ' against the steam user\'s profit; '
        + kbMoneyV(wf.againstOwn, unit) + ' against its own price of production';
      said = 'The steam-driven factories regulate the price: ' + m(o.steam) + ' plus ' + kbPctShort(o.rate) + ' is ' + m(wf.price)
        + '. The water-driven factory, at a cost of ' + m(o.water) + ', makes ' + m(Rsub(wf.price, o.water)) + ' against the steam user\'s '
        + m(Rsub(wf.price, o.steam)) + ': a surplus profit of ' + kbMoneyV(wf.marx, unit) + ', Marx\'s figure. Against its own '
        + 'individual price of production, ' + kbMoneyV(wf.own, unit) + ', it is ' + kbMoneyV(wf.againstOwn, unit) + '.';
    } else if (view === 'dr1' || view === 'dr2') {
      var rg = o.reg, rr = kbRtRents(o.soils, o.invs, rg.use, rg.price, o.rate), per = ' a ' + (qty || 'unit');
      var ri = o.invs[rg.reg], regName = o.soils[ri.soil].name + (o.soils[ri.soil].n > 1 ? ' (investment ' + ri.k + ')' : '');
      t.rtPrice = m(rg.price) + per;
      t.rtRents = rr.rents.map(m).join(', ');
      t.rtTotal = m(rr.total);
      table = { caption: 'Each investment at the regulating price of ' + m(rg.price) + per,
        head: ['soil', 'investment', 'capital', 'output', 'price of production' + per, 'surplus profit'],
        rows: o.invs.map(function (x, i) {
          return [o.soils[x.soil].name, String(x.k), m(x.capital), capQty(x.output, qty), m(x.ppu),
                  rg.use[i] ? m(Rsub(Rmul(x.output, rg.price), Rmul(x.capital, Radd(R1, o.rate)))) : 'not in use'];
        }) };
      said = 'The price is regulated by the least productive investment in use, ' + regName + ', at ' + m(rg.price) + per
        + '. Each soil pays as rent the surplus profit its investments make at that price: ' + m(rr.total) + ' in all.';
      if (view === 'dr2') {
        var kc = kbRtCase(o.invs, rg.reg, rg.use, rg.price, o.former);
        var from = o.former === null ? 'the price the first investments alone would set' : 'the former ' + m(o.former) + per;
        said += ' Against ' + from + ', the price of production is ' + (kc.move === 'constant' ? 'constant'
          : kc.move === 'falling' ? 'falling' : 'rising') + (kc.worstSoil ? ', and the worst soil pays rent too' : '') + '.';
        if (priceCase && (priceCase === 'worst-soil' ? !kc.worstSoil : kc.move !== priceCase)) {
          said += ' These figures have left the ' + priceCase + ' case this lesson reads.';
        }
      }
      if (rr.rents.some(function (r) { return Rsign(r) < 0; })) said += ' A negative figure is a soil that cannot be farmed at this price.';
    } else {
      var ab = kbRtAbsolute(o.agri, o.ind, o.e, o.limit);
      t.rtPrice = m(ab.price);
      t.rtAbsolute = 'up to ' + m(ab.absolute);
      said = 'At s′ = ' + kbPctShort(o.e) + ', agriculture (' + kbPpCvR(o.agri) + ') produces a value of ' + m(ab.value)
        + '; equalised with industry (' + kbPpCvR(o.ind) + ') at ' + kbPctNum(ab.rate) + ', its price of production is ' + m(ab.price)
        + '. Landed property can hold the price up to the value' + (o.limit === null ? '' : ' or the market limit of ' + m(o.limit))
        + ', so absolute rent is at most ' + m(ab.absolute) + ', with no price above value.';
    }
    return { tiles: t, status: said, table: table };
  }
  function kbPpCvR(x) { return kbFig(x.c) + 'c + ' + kbFig(x.v) + 'v'; }
  function kbRent(view, inst, U, opts) {
    var g = kbGuard(kbRtCheck, view, inst, opts);
    return g.refuse ? g : kbRtShow(view, g.o, U.money, U.qty, typeof KB_RT_CASE === 'string' ? KB_RT_CASE : '');
  }
"""

# ---------------------------------------------------------------------------
# revenue (Volume II, Chapter 19; Volume III, Part Seven)
# ---------------------------------------------------------------------------

REVENUE_JS = r"""
  /* Chapter 48: the value product v + s resolved into wages, rent, interest
     and profit of enterprise (rent and interest as shares of s). */
  function kbRvTrinity(c, v, s, iShare, rShare) {
    var rent = Rmul(s, rShare), interest = Rmul(s, iShare);
    return { total: Radd(Radd(c, v), s), wages: v, rent: rent, interest: interest,
             enterprise: Rsub(Rsub(s, rent), interest) };
  }
  /* Chapter 50: with the value product fixed, a wage change comes out of s;
     rent and interest keep their shares of the new s. */
  function kbRvAddedUp(c, v, s, iShare, rShare, dw) {
    return kbRvTrinity(c, Radd(v, dw), Rsub(s, dw), iShare, rShare);
  }
  /* Chapter 52: the distinct sources of revenue, in first-appearance order. */
  function kbRvClasses(people) {
    var out = [];
    people.forEach(function (p) { if (out.indexOf(p.source) < 0) out.push(p.source); });
    return out;
  }
  function kbRvCheck(view, x) {
    var o = {};
    Object.keys(x).forEach(function (k) { o[k] = x[k]; });
    if (view === 'trinity' || view === 'added-up') {
      if (Rcmp(Radd(o.split_interest, o.split_rent), R1) > 0) throw new Error('Interest and rent together take more than the whole of s');
      if (view === 'added-up') {
        if (Rsign(Radd(o.v, o.wage_change)) < 0) throw new Error('Wages cannot fall below 0');
        if (Rcmp(o.wage_change, o.s) > 0) {
          throw new Error('A wage rise of ' + kbFig(o.wage_change) + ' is more than the whole of s, ' + kbFig(o.s));
        }
      }
    }
    return o;
  }
  function kbRvShow(view, o, unit) {
    var m = function (r) { return capMoney(r, unit); }, t = {}, said;
    if (view === 'classes') {
      var cl = kbRvClasses(o.people);
      t.rvClassCount = kbPlural(cl.length, 'group', 'groups') + ': ' + cl.join(', ');
      said = 'Grouped by source of revenue, ' + kbPlural(o.people.length, 'person makes', 'people make') + ' '
        + kbPlural(cl.length, 'group', 'groups') + '. Split the sources more finely and the count grows with them.';
      return { tiles: t, status: said, table: null };
    }
    var tot = Radd(Radd(o.c, o.v), o.s), vp = Radd(o.v, o.s);
    t.rvTotal = m(tot);
    if (view === 'dogma') {
      t.rvSmith = 'v + s = ' + m(vp) + '; c = ' + m(o.c) + ' missing';
      said = 'The annual product is worth c + v + s = ' + m(tot) + '. Resolving its price into incomes alone, v + s, accounts for '
        + m(vp) + ' and loses the ' + m(o.c) + ' of means of production that must be replaced.';
      return { tiles: t, status: said, table: null };
    }
    var tr = view === 'trinity' ? kbRvTrinity(o.c, o.v, o.s, o.split_interest, o.split_rent)
      : kbRvAddedUp(o.c, o.v, o.s, o.split_interest, o.split_rent, o.wage_change);
    t.rvWages = m(tr.wages); t.rvRent = m(tr.rent); t.rvInterest = m(tr.interest); t.rvProfitShare = m(tr.enterprise);
    said = 'The value product of ' + m(vp) + ' resolves into wages ' + m(tr.wages) + ', rent ' + m(tr.rent) + ', interest '
      + m(tr.interest) + ' and profit of enterprise ' + m(tr.enterprise) + '.';
    if (view === 'added-up') {
      var old = kbRvTrinity(o.c, o.v, o.s, o.split_interest, o.split_rent);
      said += ' Wages change by ' + capSigned(o.wage_change, m) + ' and the other three by ' + capSigned(Rneg(o.wage_change), m)
        + ' together (profit of enterprise was ' + m(old.enterprise) + '). Added up as if each part were fixed in advance, they would make '
        + m(Radd(vp, o.wage_change)) + ', not the ' + m(vp) + ' that the year\'s labour produced.';
    }
    return { tiles: t, status: said, table: null };
  }
  function kbRevenue(view, inst, U, opts) {
    var g = kbGuard(kbRvCheck, view, inst, opts);
    return g.refuse ? g : kbRvShow(view, g.o, U.money);
  }
"""

# ---------------------------------------------------------------------------
# Fields, views and tiles. A field is (key, box label, capkit_core kind,
# default); a default of None means the preset must give it.
# ---------------------------------------------------------------------------

_FIXED_SUB = [("name", "name"), ("value", "nn"), ("life_years", "pos"), ("repairs_per_year", "opt"),
              ("replacement_value", "opt"), ("appears_year", "opt")]
_ITEM_SUB = [("name", "name"), ("value", "nn"), ("fixed", "yesno"), ("variable", "yesno"), ("capital", "label")]
_PRODUCT_SUB = [("name", "name"), ("use", ("word", ["production", "consumption"])), ("value", "opt")]
_SPHERE_SUB = [("name", "name"), ("c", "nn"), ("v", "nn"), ("c_used", "opt"), ("s_rate", "opt")]
_PREMIUM_SUB = [("sphere", "name"), ("rate", "num")]
_SOIL_SUB = [("soil", "name"), ("capital", "pos"), ("output", "pos")]
_PERSON_SUB = [("name", "name"), ("source", "name")]

_YEAR = ("year_weeks", "Weeks in the year", "pos", 52)
_FIXED = ("fixed", "Fixed capital: name, value, life in years, repairs a year, a cheaper replacement's value, "
          "the year it appears; entries separated by ;", ("rec", _FIXED_SUB, 1, 12, True), None)
_DEPT = lambda key: (key, "Department %s: c, v, s" % key, ("nums", "nn", 3, 3), None)
_SPHERES = ("spheres", "Spheres: name, c, v, used-up c (empty: all of c), its own s/v (empty: the common one); "
            "separated by ;", ("rec", _SPHERE_SUB, 1, 6, True), None)
_SOILS = ("soils", "Investments: soil, capital, output; one entry per investment, separated by ;",
          ("rec", _SOIL_SUB, 1, 36, False), None)
_CVS = [("c", "c", "nn", None), ("v", "v", "pos", None), ("s", "s", "nn", None)]
_CVS0 = [("c", "c", "nn", None), ("v", "v", "nn", None), ("s", "s", "nn", None)]

VIEWS = {
    "turnover": {
        "time": ([("production_weeks", "Production period, weeks", "pos", None),
                  ("working_weeks", "Working time within it, weeks (empty: all of it)", "opt", ""),
                  ("circulation_weeks", "Circulation period, weeks", "nn", None), _YEAR,
                  ("capital", "Capital advanced (empty: none stated)", "opt", "")],
                 [("Turnover time", "tuTurnover"), ("Turnovers a year", "tuTurnovers"),
                  ("Working time / production period", "tuWorkingShare"),
                  ("Circulation / turnover", "tuCirculationShare"), ("Value turned over", "tuAggregate")], False),
        "phases": ([("stage_weeks", "Weeks as money, productive and commodity capital", ("nums", "nn", 3, 3), None),
                    _YEAR],
                   [("One circuit", "tuTurnover"), ("Circuits a year", "tuTurnovers"), ("Money stage", "tuMoney"),
                    ("Productive stage", "tuProductive"), ("Commodity stage", "tuCommodity")], False),
        "fixed": ([_FIXED, ("age_years", "Years in use", "nn", None)],
                  [("Value transferred a year", "tuWear"), ("Value still locked in", "tuRemaining")], False),
        "aggregate": ([_FIXED, ("circulating", "Circulating capital", "nn", None),
                       ("circ_turnovers", "Its turnovers a year", "nn", None)],
                      [("Turned over in a year", "tuAggregate"), ("Turnovers of the whole capital", "tuAverage"),
                       ("Wear of the fixed capital", "tuWear")], False),
        "classify": ([("items", "Items: name, value, fixed (yes or no), variable (yes or no), capital (optional); "
                       "separated by ;", ("rec", _ITEM_SUB, 1, 12, True), None),
                      ("s_rate", "Rate of surplus value s/v", "nn", None)],
                     [("Fixed and circulating", "tuFixed"), ("Constant and variable", "tuVariable"),
                      ("Surplus value", "tuS")], False),
        "working": ([("working_weeks", "Working period, weeks", "pos", None),
                     ("weekly_outlay", "Outlay a week", "nn", None)],
                    [("Tied up before any sale", "tuAdvance")], False),
        "advance": ([("working_weeks", "Working period, weeks", "pos", None),
                     ("circulation_weeks", "Circulation period, weeks", "nn", None),
                     ("weekly_outlay", "Outlay a week", "nn", None),
                     ("new_outlay", "New outlay a week, after a change of scale (empty: none)", "opt", ""), _YEAR],
                    [("Capital advanced", "tuAdvance"), ("Capital set free", "tuFreed"),
                     ("Turnovers a year", "tuTurnovers")], False),
        "annual": ([("variable", "Variable capital advanced", "nn", None),
                    ("s_rate", "Rate of surplus value s/v", "nn", None),
                    ("working_weeks", "Working period, weeks", "pos", None),
                    ("circulation_weeks", "Circulation period, weeks", "nn", None), _YEAR],
                   [("Turnover time", "tuTurnover"), ("Turnovers a year", "tuTurnovers"),
                    ("Annual rate of surplus value", "tuAnnualRate"), ("Surplus value a year", "tuMassS")], False),
        "merchant": ([("merchant_capital", "Merchant's capital", "nn", None),
                      ("merchant_turnovers", "Its turnovers a year", "nn", None)],
                     [("Commodity capital taken off the industrialists' hands", "tuFreed")], False),
    },
    "schemes": {
        "sort": ([("products", "Products: name, production or consumption, value (optional); separated by ;",
                   ("rec", _PRODUCT_SUB, 1, 12, True), None)],
                 [("Department I: means of production", "scDeptI"),
                  ("Department II: means of consumption", "scDeptII")], False),
        "simple": ([_DEPT("I"), _DEPT("II")],
                   [("Department I", "scDeptI"), ("Department II", "scDeptII"), ("Balance", "scBalance"),
                    ("Exchange between the departments", "scIExchange"), ("Ic, within Department I", "scWithinI")],
                   False),
        "fixed": ([_DEPT("I"), _DEPT("II"), ("wear_set_aside", "Wear Department II hoards in money", "nn", None),
                   ("renewals", "Fixed capital Department II renews in kind", "nn", None)],
                  [("Balance", "scBalance"), ("Renewals less wear hoarded", "scFixedGap")], False),
        "hoard": ([_DEPT("I"), ("I_accumulate_share", "Share of s Department I accumulates", "share", None),
                   ("hoarders_share", "Share of it whose owners hoard this year", "share", None)],
                  [("Hoarders' sales less investors' purchases", "scHoardGap")], False),
        "expanded": ([_DEPT("I"), _DEPT("II"),
                      ("I_accumulate_share", "Share of s Department I accumulates", "share", None),
                      ("composition_I", "c/v of Department I's added capital (empty: its own)", "opt", ""),
                      ("composition_II", "c/v of Department II's added capital (empty: its own)", "opt", "")],
                     [("Department I at the start", "scDeptI"), ("Department II at the start", "scDeptII"),
                      ("Balance at the start", "scBalance"), ("After the first period", "scYear2"),
                      ("Growth of the annual product", "scGrowth")], True),
    },
    "profit": {
        "cost": (_CVS + [("sale_price", "Selling price (empty: at value)", "opt", "")],
                 [("Cost price", "prCost"), ("Profit", "prProfit")], False),
        "rate": (_CVS, [("Rate of profit s/(c + v)", "prRate"), ("Rate of surplus value s/v", "prSRate")], False),
        "relation": (_CVS, [("Rate of profit s/(c + v)", "prRate"), ("Rate of surplus value s/v", "prSRate")], False),
        "turnover": (_CVS + [("turnovers", "Turnovers of v a year", "pos", None)],
                     [("Annual rate of profit", "prAnnual"), ("Rate of profit per turnover", "prRate"),
                      ("Rate of surplus value", "prSRate")], False),
        "economy": (_CVS + [("c_change", "Change in c", "num", None)],
                    [("Rate of profit after the change", "prRate"), ("Cost price after the change", "prCost")], False),
        "price": (_CVS + [("c_change", "Change in the price of c", "num", None),
                          ("price_passed_on", "Share of it passed on in the selling price", "share", 0)],
                  [("Rate of profit", "prRate"), ("Profit", "prProfit"), ("Cost price", "prCost")], False),
        "books": (_CVS + [("sale_price", "Selling price (empty: at value)", "opt", "")],
                  [("Profit", "prProfit"), ("Rate of profit on cost", "prRate"), ("Cost price", "prCost")], False),
    },
    "prices": {
        "rates": ([_SPHERES, ("s_rate", "Rate of surplus value s/v for every sphere", "opt", "")],
                  [("Rates of profit at value", "ppRates")], False),
        "production": ([_SPHERES, ("s_rate", "Rate of surplus value s/v for every sphere", "opt", ""),
                        ("premiums", "Premiums: sphere, extra rate; separated by ; (empty: none)",
                         ("rec", _PREMIUM_SUB, 0, 6, True), [])],
                       [("General rate of profit", "ppAverage"), ("Prices of production", "ppPrices"),
                        ("Totals", "ppTotals")], False),
        "wage-rise": ([_SPHERES, ("profit_rate", "General rate of profit before the rise", "nn", None),
                       ("wage_rise", "Rise in money wages", "num", None),
                       ("average", "Sphere of average composition (empty: all together)", "label", "")],
                      [("New general rate", "ppAverage"), ("New prices of production", "ppPrices")], False),
        "merchant": ([_SPHERES, ("s_rate", "Rate of surplus value s/v for every sphere", "opt", ""),
                      ("merchant_capital", "Merchant's capital", "nn", None),
                      ("merchant_costs", "Merchant's circulation costs (empty: none)", "opt", "")],
                     [("General rate of profit", "ppAverage"), ("Selling prices", "ppMerchantPrice")], False),
        "merchant-turnover": ([("profit_rate", "General rate of profit a year", "nn", None),
                               ("merchant_turnovers", "Merchant's turnovers a year", "pos", None),
                               ("merchant_capital", "Capital laid out on each turnover", "nn", None)],
                              [("Mark-up on each turnover", "ppMarkup"), ("Each turnover", "ppMerchantPrice")], False),
    },
    "tendency": {
        "law": ([("c", "c at the start", "nn", None), ("v", "v at the start", "pos", None),
                 ("s_rate", "Rate of surplus value s/v", "nn", None),
                 ("c_step", "Added to c each period: one figure, or one per period", ("nums", "num", 0, 10), []),
                 ("capital_growth", "Growth of the whole capital each period (empty: none)", ("nums", "num", 0, 10), [])],
                [("Rate of profit, last period", "teRate"), ("Mass of profit, last period", "teMass")], True),
        "counter": ([("c", "c at the start", "nn", None), ("v", "v at the start", "pos", None),
                     ("s_rate", "Rate of surplus value s/v", "nn", None),
                     ("c_step", "Added to c each period: one figure, or one per period", ("nums", "num", 0, 10), []),
                     ("capital_growth", "Growth of the whole capital each period (empty: none)",
                      ("nums", "num", 0, 10), []),
                     ("s_rate_step", "Rise in s/v each period (empty: none)", ("nums", "num", 0, 10), []),
                     ("c_cheapening", "Share by which c cheapens each period (empty: none)",
                      ("nums", "share", 0, 10), [])],
                    [("Rate of profit, last period", "teRate"), ("Mass of profit, last period", "teMass"),
                     ("Fall offset", "teOffset")], True),
        "overaccumulation": ([("c", "c", "nn", None), ("v", "v", "pos", None),
                              ("s_rate", "Rate of surplus value s/v", "nn", None),
                              ("added_capital", "Capital added, setting no more labour in motion", "nn", None),
                              ("devalued_share", "Share of the capital then devalued", "share", 0)],
                             [("Rate of profit", "teRate"), ("Mass of profit", "teMass")], False),
    },
    "interest": {
        "split": ([("capital", "Capital employed", "nn", None), ("profit_rate", "Average rate of profit", "num", None),
                   ("interest_rate", "Rate of interest", "num", None),
                   ("principal", "Capital borrowed (empty: all of it)", "opt", ""),
                   ("manager_salary", "Hired manager's salary (empty: none)", "opt", "")],
                  [("Interest", "inInterest"), ("Profit of enterprise", "inEnterprise")], False),
        "bounds": ([("capital", "Capital employed", "nn", None), ("profit_rate", "Average rate of profit", "num", None),
                    ("interest_rate", "Rate of interest", "num", None),
                    ("principal", "Capital borrowed (empty: all of it)", "opt", ""),
                    ("manager_salary", "Hired manager's salary (empty: none)", "opt", "")],
                   [("Interest", "inInterest"), ("Profit of enterprise", "inEnterprise"), ("0 < i < p′", "inBound")],
                   False),
        "capitalise": ([("income", "Income a year", "nn", None), ("interest_rate", "Rate of interest", "pos", None)],
                       [("Price of the claim", "inPrice")], False),
        "compound": ([("principal", "Sum put out", "pos", None), ("interest_rate", "Rate of interest", "nn", None),
                      ("years", "Years", "nncount", None),
                      ("real_growth", "Real growth of the product a year", "nn", None)],
                     [("At compound interest", "inCompound"), ("Growing with the product", "inReal")], False),
        "usury": ([("debt", "Debt", "nn", None), ("interest_rate", "Usurer's rate", "nn", None),
                   ("surplus", "Surplus the producer can pay a year", "nn", None),
                   ("holding_value", "Value of the holding", "pos", None), ("years", "Years followed", "count", None)],
                  [("Interest", "inInterest"), ("The debt passes the holding", "inYearsToRuin")], False),
    },
    "rent": {
        "price": ([("rent", "Payment a year", "nn", None), ("interest_rate", "Rate of interest", "pos", None),
                   ("improvement_interest", "Part that is interest on capital sunk in the land (empty: none)", "opt", "")],
                  [("Price of the land", "rtPrice"), ("True ground rent", "rtTrueRent")], False),
        "waterfall": ([("cost_steam", "Cost price with steam", "pos", None),
                       ("cost_water", "Cost price with the waterfall", "nn", None),
                       ("profit_rate", "Average rate of profit", "nn", None)],
                      [("Regulating price of production", "rtPrice"), ("Surplus profit", "rtSurplusProfit")], False),
        "dr1": ([_SOILS, ("profit_rate", "Average rate of profit", "nn", None),
                 ("regulating", "Regulating investment (auto: the least productive in use)", "label", "auto"),
                 ("market_limit", "Quantity the market takes (empty: all)", "opt", "")],
                [("Regulating price", "rtPrice"), ("Rent on each soil", "rtRents"), ("Total rent", "rtTotal")], False),
        "dr2": ([_SOILS, ("profit_rate", "Average rate of profit", "nn", None),
                 ("regulating", "Regulating investment (auto: the least productive in use)", "label", "auto"),
                 ("market_limit", "Quantity the market takes (empty: all)", "opt", ""),
                 ("former_price", "Former price (empty: what the first investments alone set)", "opt", "")],
                [("Regulating price", "rtPrice"), ("Rent on each soil", "rtRents"), ("Total rent", "rtTotal")], False),
        "absolute": ([("agri", "Agriculture: c, v", ("nums", "nn", 2, 2), None),
                      ("industry", "Industry: c, v", ("nums", "nn", 2, 2), None),
                      ("s_rate", "Rate of surplus value s/v", "nn", None),
                      ("market_limit", "Highest price the market bears (empty: none)", "opt", "")],
                     [("Agriculture's price of production", "rtPrice"), ("Absolute rent", "rtAbsolute")], False),
    },
    "revenue": {
        "trinity": (_CVS0 + [("split_interest", "Interest's share of s", "share", None),
                             ("split_rent", "Rent's share of s", "share", None)],
                    [("Annual product c + v + s", "rvTotal"), ("Wages", "rvWages"), ("Rent", "rvRent"),
                     ("Interest", "rvInterest"), ("Profit of enterprise", "rvProfitShare")], False),
        "dogma": (_CVS0, [("Annual product c + v + s", "rvTotal"), ("The dogma's total", "rvSmith")], False),
        "added-up": (_CVS0 + [("split_interest", "Interest's share of s", "share", None),
                              ("split_rent", "Rent's share of s", "share", None),
                              ("wage_change", "Change in wages", "num", None)],
                     [("Wages", "rvWages"), ("Rent", "rvRent"), ("Interest", "rvInterest"),
                      ("Profit of enterprise", "rvProfitShare")], False),
        "classes": ([("people", "People: name, source of revenue; separated by ;", ("rec", _PERSON_SUB, 1, 12, True),
                      None)],
                    [("Groups by source of revenue", "rvClassCount")], False),
    },
}

_MODE_META = {
    # mode: (prefix, JS block, JS function, title, subtitle, panel title, panel intro)
    "turnover": ("tu", TURNOVER_JS, "kbTurnover", "The turnover of capital",
                 "working, production and circulation time, and what they cost in capital",
                 "Change the periods or the capital",
                 "Every figure is computed from the weeks and sums as typed, exactly. The year's length is printed "
                 "with every count of turnovers."),
    "schemes": ("sc", SCHEMES_JS, "kbSchemes", "The two departments",
                "Department I makes means of production, Department II means of consumption",
                "Change the departments' c, v and s",
                "Each department is typed as c, v, s. Balance and growth are computed exactly; a period that "
                "cannot balance is refused, and the banner says why."),
    "profit": ("pr", PROFIT_JS, "kbProfit", "Cost price and the rate of profit",
               "the same c, v and s, measured against the whole capital",
               "Change c, v, s or the change in them", "Every rate is the exact fraction, with its percentage."),
    "prices": ("pp", PRICES_JS, "kbPrices", "Prices of production",
               "values transformed sphere by sphere, inputs at value, as Volume III, Chapter 9 does it",
               "Change the spheres or the rates",
               "A sphere is typed as name, c, v, used-up c, its own s/v; the general rate and every price are exact."),
    "tendency": ("te", TENDENCY_JS, "kbTendency", "The rate of profit over time",
                 "a rising composition, and what works against its effect",
                 "Change the capital, the steps or the periods",
                 "Each period is computed from the one before, exactly; at most 10 periods."),
    "interest": ("in", INTEREST_JS, "kbInterest", "Interest and its forms",
                 "a share of profit, a price for a claim, a sum that compounds",
                 "Change the capital, the rates or the years",
                 "Every sum is exact; one too long to print is given as its formula and its number of digits."),
    "rent": ("rt", RENT_JS, "kbRent", "Ground rent", "surplus profit fixed on land, and land priced at the rate of interest",
             "Change the soils, the investments or the rates",
             "Each investment is typed as soil, capital, output. The regulating price and every rent are exact."),
    "revenue": ("rv", REVENUE_JS, "kbRevenue", "Revenues and their sources",
                "one annual product, and the incomes it is divided into",
                "Change the product's parts or how s is divided",
                "Every figure is exact. Wages, rent, interest and profit of enterprise always add up to v + s."),
}

MODES = tuple(VIEWS)
PRICE_CASES = ("constant", "falling", "rising", "worst-soil")

# ---------------------------------------------------------------------------
# Lesson data -> box data, and the build-time checks
# ---------------------------------------------------------------------------


def _f(where, value, what):
    return cc.q(where, value, what)[0]


def _dict_to(where, key, value, parts):
    """{c, v, s} (or {c, v}) -> [c, v, s]; a list of the right length passes through."""
    if isinstance(value, dict):
        if set(value) != set(parts):
            raise ValueError("%s: %s should be {%s}, not %r" % (where, key, ", ".join(parts), value))
        return [value[k] for k in parts]
    if isinstance(value, (list, tuple)) and len(value) == len(parts):
        return list(value)
    raise ValueError("%s: %s should be {%s}, not %r" % (where, key, ", ".join(parts), value))


def _fill(rows, where, key, sub):
    """Records with every optional key present, as capkit_core writes them."""
    if not isinstance(rows, (list, tuple)):
        raise ValueError("%s: %s should be a list of records" % (where, key))
    out = []
    for r in rows:
        if not isinstance(r, dict):
            raise ValueError("%s: each entry of %s should be a record, not %r" % (where, key, r))
        r = dict(r)
        for k, kind in sub:
            if k not in r and kind in ("opt", "label"):
                r[k] = ""
        out.append(r)
    return out


def _normalise(mode, view, p, where):
    """D.2's shapes -> the boxes' shapes (see the module docstring)."""
    p = dict(p)
    if mode == "schemes":
        for key in ("I", "II"):
            if key in p:
                p[key] = _dict_to(where, key, p[key], ("c", "v", "s"))
        if "products" in p:
            p["products"] = _fill(p["products"], where, "products", _PRODUCT_SUB)
    elif mode == "turnover":
        if "fixed" in p:
            p["fixed"] = _fill(p["fixed"], where, "fixed", _FIXED_SUB)
        if "items" in p:
            p["items"] = _fill(p["items"], where, "items", _ITEM_SUB)
    elif mode == "prices":
        if "spheres" in p:
            p["spheres"] = _fill(p["spheres"], where, "spheres", _SPHERE_SUB)
    elif mode == "tendency":
        for key in ("c_step", "capital_growth", "s_rate_step", "c_cheapening"):
            if key in p and not isinstance(p[key], (list, tuple)):
                p[key] = [] if p[key] in (None, "") else [p[key]]
    elif mode == "rent":
        for key in ("agri", "industry"):
            if key in p:
                p[key] = _dict_to(where, key, p[key], ("c", "v"))
        if "soils" in p:
            soils, rows = p["soils"], []
            if not isinstance(soils, (list, tuple)):
                raise ValueError("%s: soils should be a list of {name, capital, outputs}" % where)
            for s in soils:
                if not isinstance(s, dict) or set(s) != {"name", "capital", "outputs"} \
                        or not isinstance(s["outputs"], (list, tuple)) or not s["outputs"]:
                    raise ValueError("%s: each soil should be {name, capital, outputs: [output of each investment]}, "
                                     "not %r" % (where, s))
                rows.extend({"soil": s["name"], "capital": s["capital"], "output": q} for q in s["outputs"])
            p["soils"] = rows
    elif mode == "revenue":
        if "split" in p:
            sp = p.pop("split")
            if not isinstance(sp, dict) or set(sp) != {"interest", "rent"}:
                raise ValueError("%s: split should be {interest, rent}, shares of s, not %r" % (where, sp))
            p["split_interest"], p["split_rent"] = sp["interest"], sp["rent"]
        if "people" in p:
            people = []
            for r in p["people"] if isinstance(p["people"], (list, tuple)) else [None]:
                if isinstance(r, dict) and set(r) == {"name", "source"}:
                    people.append(r)
                elif isinstance(r, dict) and "name" in r and set(r) <= {"name", "wages", "profit", "rent"}:
                    kinds = [k for k in ("wages", "profit", "rent") if r.get(k) and _f(where, r[k], k) > 0]
                    if not kinds:
                        raise ValueError("%s: %s has no revenue" % (where, r["name"]))
                    people.append({"name": r["name"], "source": " and ".join(kinds)})
                else:
                    raise ValueError("%s: each person is {name, source} or {name, wages, profit, rent}, not %r"
                                     % (where, r))
            p["people"] = people
    return p


def _rt_regulate(rows, rate, regulating, limit, former=None):
    """The Python twin of kbRtRegulate and kbRtCase, for build-time checks:
    (price, its move against the former price, whether the worst soil pays)."""
    invs, count = [], {}
    for r in rows:
        count[r["soil"]] = count.get(r["soil"], 0) + 1
        cap, out = r["capital"], r["output"]
        invs.append((r["soil"], count[r["soil"]], cap, out, cap * (1 + rate) / out))
    use = [limit is None] * len(invs)
    if limit is not None:
        got, reg = Fraction(0), -1
        for i in sorted(range(len(invs)), key=lambda i: (invs[i][4], i)):
            if got >= limit:
                break
            use[i], got, reg = True, got + invs[i][3], i
        if got < limit:
            raise ValueError("the soils supply only %s against a market of %s" % (got, limit))
    else:
        reg = max(range(len(invs)), key=lambda i: (invs[i][4], -i))
    if regulating not in ("", "auto"):
        hits = [i for i, x in enumerate(invs) if regulating == "%s%d" % (x[0], x[1])
                or (x[1] == 1 and regulating == x[0])]
        if not hits or not use[hits[0]]:
            raise ValueError("the regulating investment %r is not an investment in use" % regulating)
        reg = hits[0]
    price = invs[reg][4]
    firsts = [i for i, x in enumerate(invs) if x[1] == 1]
    worst = max(firsts, key=lambda i: (invs[i][4], -i))
    base = invs[worst][4] if former is None else former
    move = "constant" if price == base else ("falling" if price < base else "rising")
    return price, move, invs[reg][1] > 1 and use[worst] and invs[worst][4] < price


def _checker(mode, view, cfg, n_periods):
    """check(where, preset) for capkit_core.presets: the rules that span fields."""
    def check(where, p):
        g = lambda k, what=None: _f(where, p[k], what or k)
        if mode == "turnover" and view == "time" and p.get("working_weeks") not in (None, ""):
            if g("working_weeks") > g("production_weeks"):
                raise ValueError("%s: working_weeks is longer than production_weeks" % where)
        if mode == "turnover" and view in ("fixed", "aggregate"):
            for it in p["fixed"]:
                if (it.get("replacement_value") in (None, "")) != (it.get("appears_year") in (None, "")):
                    raise ValueError("%s: %s needs both replacement_value and appears_year, or neither"
                                     % (where, it.get("name")))
        if mode == "turnover" and view == "classify":
            for it in p["items"]:
                if it.get("fixed") is True and it.get("variable") is True:
                    raise ValueError("%s: %s is fixed and variable; variable capital is always circulating"
                                     % (where, it.get("name")))
        if mode == "prices" and view != "merchant-turnover":
            names = [s.get("name") for s in p["spheres"]]
            for s in p["spheres"]:
                if s.get("c_used") not in (None, "") and _f(where, s["c_used"], "c_used") > _f(where, s["c"], "c"):
                    raise ValueError("%s: the used-up c of %s is more than its c" % (where, s.get("name")))
                if view != "wage-rise" and s.get("s_rate") in (None, "") and p.get("s_rate") in (None, ""):
                    raise ValueError("%s: %s has no s_rate and none is given for all spheres" % (where, s.get("name")))
            for pr in p.get("premiums") or []:
                if pr.get("sphere") not in names:
                    raise ValueError("%s: a premium names %r, which is not a sphere" % (where, pr.get("sphere")))
            if view == "wage-rise" and p.get("average") not in (None, "") and p["average"] not in names:
                raise ValueError("%s: average names %r, which is not a sphere" % (where, p["average"]))
        if mode == "tendency" and view in ("law", "counter"):
            for k in ("c_step", "capital_growth", "s_rate_step", "c_cheapening"):
                n, runs = len(p.get(k) or []), p.get("periods", n_periods)
                if n > 1 and n != runs:
                    raise ValueError("%s: %s lists %d figures and the %s ships %d periods"
                                     % (where, k, n, "preset" if "periods" in p else "lesson", runs))
        if mode == "rent" and view in ("dr1", "dr2"):
            rows = [{"soil": r["soil"], "capital": _f(where, r["capital"], "capital"),
                     "output": _f(where, r["output"], "output")} for r in p["soils"]]
            soils = [r["soil"] for r in rows]
            if view == "dr1" and len(set(soils)) != len(soils):
                raise ValueError("%s: differential rent I takes one investment per soil" % where)
            if len(set(soils)) > 6:
                raise ValueError("%s: at most 6 soils" % where)
            lim, former = p.get("market_limit"), p.get("former_price")
            try:
                _price, move, worst_pays = _rt_regulate(
                    rows, _f(where, p["profit_rate"], "profit_rate"), str(p.get("regulating", "auto")).strip(),
                    None if lim in (None, "") else _f(where, lim, "market_limit"),
                    None if former in (None, "") else _f(where, former, "former_price"))
            except ValueError as err:
                raise ValueError("%s: %s" % (where, err))
            want = cfg.get("price_case")
            if view == "dr2" and want is not None and (not worst_pays if want == "worst-soil" else move != want):
                raise ValueError("%s: this instance's price is %s%s, and the lesson's price_case is %s"
                                 % (where, move, " with rent on the worst soil" if worst_pays else "", want))
        if mode == "revenue" and view in ("trinity", "added-up"):
            if g("split_interest") + g("split_rent") > 1:
                raise ValueError("%s: interest and rent take more than the whole of s" % where)
    return check


def _build(cfg, mode):
    views = VIEWS[mode]
    kit = "%s/%s" % (KIT, mode)
    view = cc.pick_view(cfg, kit, list(views))
    kit = "%s/%s/%s" % (KIT, mode, view)
    fields, tiles, iterates = views[view]
    money, qty = cc.units(cfg, kit, cc.MONEY_UNITS, "£")
    n_periods = cc.periods(cfg, kit, 4) if iterates else None
    if not iterates and "periods" in cfg:
        raise ValueError("%s: this view does not iterate, so cfg['periods'] means nothing here" % kit)
    for key in ("stage", "hold", "test"):
        if key in cfg:
            raise ValueError("%s: cfg sets %s, which this view has no control for" % (kit, key))
    extra_js = ""
    if mode == "rent" and view == "dr2":
        case = cfg.get("price_case")
        if case is not None and case not in PRICE_CASES:
            raise ValueError("%s: cfg['price_case'] is %r; it is one of %s" % (kit, case, ", ".join(PRICE_CASES)))
        extra_js = cfg_literal("KB_RT_CASE", case or "")
    elif "price_case" in cfg:
        raise ValueError("%s: price_case belongs to rent/dr2 only" % kit)
    presets = cfg.get("presets")
    if not isinstance(presets, list) or not presets:
        raise ValueError("%s: cfg['presets'] must be a non-empty list of instances" % kit)
    cfg2 = dict(cfg)
    cfg2["presets"] = [_normalise(mode, view, p, "%s preset %r" % (kit, p.get("id")))
                       if isinstance(p, dict) else p for p in presets]
    prefix, js, fn, title, subtitle, panel_title, panel_intro = _MODE_META[mode]
    return cc.mode_lab(cfg2, kit=kit, prefix=prefix, view=view, fields=list(fields), tiles=list(tiles),
                       mode_js=KB_COMMON_JS + js, fn=fn, money=money, qty=qty, title=title, subtitle=subtitle,
                       panel_title=panel_title, panel_intro=panel_intro, n_periods=n_periods,
                       check=_checker(mode, view, cfg, n_periods), extra_js=extra_js)


def capkit_b_lab(cfg):
    """The Capital kit's Volume II and III modes. cfg["mode"] chooses the mode and
    cfg["view"] the view; an unknown mode or view raises, as markov_lab does: a
    kit that fell back to a default would render another lesson's lab under the
    right title."""
    cfg = cfg or {}
    mode = cfg.get("mode")
    if mode not in VIEWS:
        raise ValueError("capkit_b_lab: unknown mode %r; the eight modes here are %s" % (mode, ", ".join(MODES)))
    return _build(cfg, mode)


__all__ = ["MODES", "VIEWS", "DEVIATIONS", "capkit_b_lab"]
