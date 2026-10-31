"""itakit -- the lab kit of Introduction to Algorithms, Read Along.

Specified in docs/intro-algorithms/PLAN.md section D; the report an author
configures a lesson from is docs/intro-algorithms/kit-report.md, and the seam
between this module and itakit_b.py is docs/intro-algorithms/kit-contract.md.
Built on eakit_core (imported as `ea`, unchanged): its field parser, printers,
preset table, markup and wiring.

Family A (this module), numeric and analytic:

  growth      (gri)  race, bounds
  sorting     (sti)  insertion, cost, merge
  recurrence  (rci)  master, tree
  maxsub      (msi)  compare
  hiring      (hri)  order
  workspan    (wsi)  dag, recurrence
  lup         (lui)  decompose
  fft         (fti)  multiply

Family B (itakit_b.py): rod, lcs, obst, amortized, rbtree, btree, fibheap,
veb, bfs. `itakit_lab` dispatches them through `itakit_b.MODES`.

THE BUILDER SIGNATURE (both families). A mode is built by
`builder(cfg) -> common.Lab`, where cfg is the lesson's lab cfg as written
(cfg["mode"] names the mode). Every builder in this kit is
`lambda cfg: mode_lab(cfg, <mode>, <SPEC>)`, and `mode_lab` takes a spec dict:

  {"prefix": "gri", "fn": "griCompute", "title": "...", "js": GRI_JS,
   "views": {view: {"fields": [(key, field_spec, default)], "tiles": [(label, id)],
                    "check": check(parsed, fixed) | None, "subtitle": "...",
                    "rules": "...", "js": GRI_VIEW_JS[view],
                    "options": options(cfg, kit, tiles) -> (fixed, keys, tiles) | absent,
                    "family": 1 | 2 (default 1)}}}

The first view is the default. A page ships RATIONAL_JS, EA_CORE_JS,
ITA_CORE_JS, its mode's base block and its own view's block -- never the other
views or modes (page weight).

IDS. The PLAN's two-letter prefixes are taken by other kits (grCompute,
hrPreset, ftStatus exist), so every id, JS function and JS variable here uses
the PLAN prefix followed by "i": gri, sti, rci, msi, hri, wsi, lui, fti (and
family B rdi, lci, obi, ami, rbi, bti, fhi, vbi, bfi). The shared helpers
begin ita / ITA_. Grepped against scripts/mathpath/labs/*.py on 2026-10-31:
none of these prefixes is used by another kit.

EXACTNESS. Every figure is an exact BigInt rational, except: lg n of a number
that is not a power of 2 is irrational, so a time or value containing lg n is
printed rounded with "≈" while every COMPARISON involving lg n is decided
exactly (itaLgCmp brackets lg n by repeated squaring on integers until the
bracket excludes the other side); n^(log_b a) is printed with an approximate
exponent when log_b a is irrational, while the master-method case is decided
on integers; and the FFT works in floating point, says so, rounds its product
to integers and compares it with the exact schoolbook product.
"""

import math
import re
from fractions import Fraction

from . import eakit_core as ea

KIT = "itakit"

# ---------------------------------------------------------------------------
# Shared JavaScript, on every itakit page (both families)
# ---------------------------------------------------------------------------

ITA_CORE_JS = r"""
  /* itakit's shared helpers (docs/intro-algorithms/kit-contract.md). */
  function itaQ(r) { return Rint(r) ? eaInt(r.n) : eaInt(r.n) + '/' + eaInt(r.d); }
  function itaList(a) {
    return a.map(function (x) { return typeof x === 'object' ? itaQ(x) : eaInt(x); }).join(', ');
  }
  function itaApprox(r, places) { return '≈ ' + eaFixed(r, places); }
  function itaBitLen(n) { return n.toString(2).length; }
  /* lg n for a BigInt n >= 1: {exact} when n is a power of 2, else a bracket
     {lo, hi} of width 2^-k from k binary digits found by squaring n / 2^m on
     integers with outward rounding, so the bracket always holds lg n. */
  function itaLg(n, bits) {
    n = BigInt(n); bits = bits || 64;
    var m = BigInt(itaBitLen(n) - 1);
    if (n === (1n << m)) return { exact: R(m) };
    var P = BigInt(bits + 24), two = 2n << P;
    var lo = (n << P) >> m, hi = lo + 1n, digits = 0n, k = 0n;
    for (var i = 0; i < bits; i += 1) {
      lo = (lo * lo) >> P; hi = ((hi * hi) >> P) + 1n;
      if (lo >= two) { digits = digits * 2n + 1n; lo >>= 1n; hi = (hi >> 1n) + 1n; }
      else if (hi < two) { digits = digits * 2n; }
      else break;
      k += 1n;
    }
    var scale = 1n << k;
    return { lo: R(m * scale + digits, scale), hi: R(m * scale + digits + 1n, scale) };
  }
  /* The sign of lg n - x, exactly, for BigInt n >= 1 and a rational x. */
  function itaLgCmp(n, x) {
    n = BigInt(n);
    var m = BigInt(itaBitLen(n) - 1);
    if (n === (1n << m)) return Rcmp(R(m), x);
    if (Rcmp(x, R(m)) <= 0) return 1;
    if (Rcmp(x, R(m + 1n)) >= 0) return -1;
    var widths = [64, 256, 1024];
    for (var i = 0; i < widths.length; i += 1) {
      var b = itaLg(n, widths[i]);
      if (Rcmp(x, b.lo) <= 0) return 1;
      if (Rcmp(x, b.hi) >= 0) return -1;
    }
    eaRefuse('lg ' + eaInt(n) + ' and ' + itaQ(x) + ' agree to 1,024 binary places, too close for this lab to compare');
  }
  /* lg n as one rational: exact, or the middle of a 2^-64 bracket. */
  function itaLgMid(n) { var b = itaLg(n, 64); return b.exact || Rdiv(Radd(b.lo, b.hi), R(2n)); }
"""

# ---------------------------------------------------------------------------
# growth (gri): two programs racing, and checking a claimed witness
# ---------------------------------------------------------------------------

RACE_FNS = ("lg n", "n", "n lg n", "n^2", "n^3", "2^n")
BOUND_FNS = ("1", "lg* n", "lg n", "n", "n lg n", "n^2", "n^3", "F(n)", "2^n", "n!")
BIG_FNS = ("F(n)", "2^n", "n!")
RACE_CAP = 10 ** 15         # the crossover search stops here (4,096 when 2^n races)
EXP_CAP = 4096
WINDOW = 10000              # bounds: every n in [n0, n0 + 10,000]
BIG_N0 = 1000               # bounds: n0 at most 1,000 when F(n), 2^n or n! appears

GRI_JS = r"""
  var GRI_VIEW = {};
  function griCompute(view, inst, opts) { return eaRun(GRI_VIEW[view], inst, opts); }
  /* Rank of each menu function by order of growth: each is o() of the next. */
  var GRI_RANK = { '1': 0, 'lg* n': 1, 'lg n': 2, 'n': 3, 'n lg n': 4, 'n^2': 5, 'n^3': 6, 'F(n)': 7, '2^n': 8, 'n!': 9 };
  /* lg* n = the least i with lg applied i times <= 1: n <= 1, 2, 4, 16, 65,536. */
  function griLgStar(n) {
    var t = [1n, 2n, 4n, 16n, 65536n], i;
    for (i = 0; i < t.length; i += 1) if (n <= t[i]) return BigInt(i);
    return 5n;
  }
  /* A menu function at the BigInt n as {p, q}: the value is p + q lg n.
     st carries n! and F(n) for the bounds walk. */
  function griAt(fn, n, st) {
    var z = { p: R0, q: R0 };
    switch (fn) {
      case '1': z.p = R1; break;
      case 'lg* n': z.p = R(griLgStar(n)); break;
      case 'lg n': z.q = R1; break;
      case 'n': z.p = R(n); break;
      case 'n lg n': z.q = R(n); break;
      case 'n^2': z.p = R(n * n); break;
      case 'n^3': z.p = R(n * n * n); break;
      case '2^n': z.p = R(1n << n); break;
      case 'n!': z.p = R(st.fact); break;
      case 'F(n)': z.p = R(st.fib); break;
    }
    return z;
  }
  function griLin(a, b, kb) { return { p: Radd(a.p, Rmul(kb, b.p)), q: Radd(a.q, Rmul(kb, b.q)) }; }
  function griScale(a, k) { return { p: Rmul(a.p, k), q: Rmul(a.q, k) }; }
  /* The sign of p + q lg n, exactly. */
  function griSign(v, n) {
    if (Rsign(v.q) === 0) return Rsign(v.p);
    var c = itaLgCmp(n, Rdiv(Rneg(v.p), v.q));
    return Rsign(v.q) > 0 ? c : -c;
  }
  /* The value p + q lg n as one rational, and whether it is exact. */
  function griValue(v, n) {
    if (Rsign(v.q) === 0) return { r: v.p, exact: true };
    var b = itaLg(n, 64);
    if (b.exact) return { r: Radd(v.p, Rmul(v.q, b.exact)), exact: true };
    return { r: Radd(v.p, Rmul(v.q, itaLgMid(n))), exact: false };
  }
  /* A value for a tile: exact whole numbers grouped, exact fractions as eaNum,
     an approximation with "≈" and two places; tiny or huge in powers of ten. */
  function griShow(x) {
    var r = x.r, a = Rabs(r);
    if (Rsign(r) !== 0 && (Rcmp(a, R(1n, 100n)) < 0 || eaBig(r))) return (x.exact && !eaBig(r) ? itaQ(r) + ' ' : '') + eaSci(r);
    if (x.exact) return eaNum(r);
    return itaApprox(r, 2);
  }
  function griFormula(c, fn) { return (Requ(c, R1) ? '' : itaQ(c) + ' ') + fn; }
"""

GRI_VIEW_JS = {}

GRI_VIEW_JS["race"] = r"""
  GRI_VIEW.race = function (inst) {
    var A = { name: 'A', fn: inst.fnA, k: Rdiv(inst.costA, inst.speedA), c: inst.costA },
        B = { name: 'B', fn: inst.fnB, k: Rdiv(inst.costB, inst.speedB), c: inst.costB }, n = inst.n.n;
    [A, B].forEach(function (X) {
      if (X.fn === '2^n' && n > 4096n) eaRefuse('Program ' + X.name + ' costs 2^n, and 2^n seconds past n = 4,096 is too large to print; choose n of at most 4,096');
    });
    var time = function (X, m) { return griScale(griAt(X.fn, m), X.k); };
    var diff = function (X, Y, m) { return griSign(griLin(time(X, m), time(Y, m), R(-1n)), m); };
    var tA = griValue(time(A, n), n), tB = griValue(time(B, n), n), cross, rows = [];
    [1n, 10n, 100n, 1000n, 10000n, 100000n, 1000000n, 10000000n].forEach(function (k) {
      if ((A.fn === '2^n' || B.fn === '2^n') && k > 4096n) return;
      var a = griValue(time(A, k), k), b = griValue(time(B, k), k), d = diff(A, B, k);
      rows.push([eaInt(k), griShow(a) + ' s', griShow(b) + ' s', d < 0 ? 'A' : (d > 0 ? 'B' : 'neither')]);
    });
    if (GRI_RANK[A.fn] === GRI_RANK[B.fn]) {
      var q = Rdiv(A.k, B.k), qa = Rcmp(q, R1) >= 0;
      /* State the ratio from the slower program, so it is never a figure under 1
         that rounds to 0.0×. */
      cross = 'never: the same order of growth, so ' + (qa ? 'A' : 'B') + ' always takes '
        + eaTimes(qa ? q : Rdiv(R1, q)) + ' ' + (qa ? 'B' : 'A') + '\'s time';
    } else {
      var S = GRI_RANK[A.fn] < GRI_RANK[B.fn] ? A : B, F = S === A ? B : A;
      var cap = (A.fn === '2^n' || B.fn === '2^n') ? 4096n : 1000000000000000n;
      var last = 0n, m, N = null;
      for (m = 1n; m <= 64n; m += 1n) if (diff(S, F, m) >= 0) last = m;
      if (diff(S, F, 64n) < 0) N = last + 1n;
      else if (diff(S, F, cap) >= 0) N = null;
      else {
        var lo = 64n, hi = cap;
        while (hi - lo > 1n) { m = (lo + hi) / 2n; if (diff(S, F, m) >= 0) lo = m; else hi = m; }
        N = hi;
      }
      cross = N === null ? 'beyond n = ' + eaInt(cap) + ', where the search stops'
        : 'n = ' + eaInt(N) + ': from there on ' + S.name + ' (' + S.fn + ') is always faster';
    }
    var d0 = diff(A, B, n), faster;
    if (d0 === 0) faster = 'neither: the same time';
    else {
      var W = d0 < 0 ? A : B, L = d0 < 0 ? B : A, w = W === A ? tA : tB, l = W === A ? tB : tA;
      var ratio = Rsign(w.r) === 0 ? null : Rdiv(l.r, w.r);
      faster = W.name + (ratio === null ? '' : ', ' + (w.exact && l.exact ? eaTimes(ratio) : '≈ ' + eaFixed(ratio, 1) + '×') + ' faster');
    }
    return {
      tiles: { griCross: cross, griTimeA: griShow(tA) + ' s', griTimeB: griShow(tB) + ' s', griFaster: faster },
      status: 'A runs ' + griFormula(A.c, A.fn) + ' instructions at ' + eaNum(inst.speedA)
        + ' a second; B runs ' + griFormula(B.c, B.fn) + ' at ' + eaNum(inst.speedB) + ' a second. A time with lg n in it is rounded (lg n is irrational unless n is a power of 2); which program is faster is decided exactly. '
        + 'The crossover is a count over these two formulas, not a measurement of a machine.',
      table: { caption: 'Time of each program at powers of ten', head: ['n', 'A (seconds)', 'B (seconds)', 'faster'], rows: rows }
    };
  };
"""

GRI_VIEW_JS["bounds"] = r"""
  var GRI_REL = { O: 'O', Omega: 'Ω', Theta: 'Θ' };
  function griSum(terms, n, st) {
    var v = { p: R0, q: R0 };
    terms.forEach(function (t) { v = griLin(v, griAt(t.fn, n, st), t.coef); });
    return v;
  }
  function griText(terms) {
    return terms.map(function (t, i) {
      var neg = Rsign(t.coef) < 0, c = Rabs(t.coef);
      var body = (Requ(c, R1) && t.fn !== '1') ? t.fn : (t.fn === '1' ? itaQ(c) : itaQ(c) + ' ' + t.fn);
      return (i === 0 ? (neg ? EA_MINUS : '') : (neg ? ' ' + EA_MINUS + ' ' : ' + ')) + body;
    }).join('');
  }
  /* The leading term: the highest-ranked function with a nonzero total coefficient. */
  function griLead(terms) {
    var by = {};
    terms.forEach(function (t) { by[t.fn] = Radd(by[t.fn] || R0, t.coef); });
    var best = null;
    Object.keys(by).forEach(function (fn) {
      if (Rsign(by[fn]) !== 0 && (best === null || GRI_RANK[fn] > GRI_RANK[best.fn])) best = { fn: fn, coef: by[fn] };
    });
    return best;
  }
  GRI_VIEW.bounds = function (inst) {
    var big = inst.f.concat(inst.g).some(function (t) { return t.fn === 'F(n)' || t.fn === '2^n' || t.fn === 'n!'; });
    var n0 = inst.n0.n, last = n0 + 10000n, rel = inst.relation, c1 = inst.c1, c2 = inst.c2;
    if (big && n0 > 1000n) eaRefuse('With F(n), 2^n or n! in f or g, n₀ is at most 1,000 (the check runs to n₀ + 10,000)');
    var st = { fact: 1n, fib: 0n }, fb = 1n, n, k;
    for (k = 2n; k <= n0; k += 1n) st.fact *= k;
    for (k = 0n; k < n0; k += 1n) { var t = st.fib + fb; st.fib = fb; fb = t; }
    var fail = null, first = null, checks = 0n;
    for (n = n0; n <= last; n += 1n) {
      if (n > n0) { st.fact *= n; var t2 = st.fib + fb; st.fib = fb; fb = t2; }
      var f = griSum(inst.f, n, st), g = griSum(inst.g, n, st), lowG = griScale(g, c1), highG = griScale(g, c2), why = null;
      if (first === null) first = { f: griValue(f, n), lo: griValue(lowG, n), hi: griValue(highG, n) };
      checks += 1n;
      if (rel === 'O') {
        if (griSign(f, n) < 0) why = 'f(n) < 0';
        else if (griSign(griLin(highG, f, R(-1n)), n) < 0) why = 'f(n) > c₂·g(n)';
      } else {
        if (griSign(lowG, n) < 0) why = 'c₁·g(n) < 0';
        else if (griSign(griLin(f, lowG, R(-1n)), n) < 0) why = 'f(n) < c₁·g(n)';
        else if (rel === 'Theta' && griSign(griLin(highG, f, R(-1n)), n) < 0) why = 'f(n) > c₂·g(n)';
      }
      if (why) {
        fail = { n: n, why: why, f: griValue(f, n), lo: griValue(lowG, n), hi: griValue(highG, n) };
        break;
      }
    }
    var shown = rel === 'O' ? ['f', 'hi'] : (rel === 'Omega' ? ['f', 'lo'] : ['f', 'lo', 'hi']);
    var name = { f: 'f', lo: 'c₁g', hi: 'c₂g' };
    var at = function (x, m) { return shown.map(function (s) { return name[s] + '(' + eaInt(m) + ') = ' + griShow(x[s]); }).join(', '); };
    var lf = griLead(inst.f), lg = griLead(inst.g), order, truth;
    if (!lf || Rsign(lf.coef) < 0) { order = 'f is eventually negative or zero'; truth = 'false: no witness exists'; }
    else if (!lg || Rsign(lg.coef) < 0) { order = 'g is eventually negative or zero'; truth = 'false: no witness exists'; }
    else {
      var d = GRI_RANK[lf.fn] - GRI_RANK[lg.fn];
      order = d === 0 ? 'f = Θ(g): both lead with ' + lf.fn : (d < 0 ? 'f = o(g): ' + lf.fn + ' grows slower than ' + lg.fn
        : 'f = ω(g): ' + lf.fn + ' grows faster than ' + lg.fn);
      var ok = rel === 'O' ? d <= 0 : (rel === 'Omega' ? d >= 0 : d === 0);
      truth = ok ? 'true: some c and n₀ work' : 'false: no c and n₀ work';
    }
    var claim = 'f(n) = ' + GRI_REL[rel] + '(g(n))';
    return {
      tiles: {
        griHolds: fail ? 'no' : 'yes, at all ' + eaInt(checks) + ' values of n from ' + eaInt(n0) + ' to ' + eaInt(last),
        griFirstFail: fail ? 'n = ' + eaInt(fail.n) + ': ' + fail.why : 'none from ' + eaInt(n0) + ' to ' + eaInt(last),
        griAtN0: at(first, n0),
        griOrder: order,
        griClaim: truth
      },
      status: 'Claim: ' + claim + ' with f(n) = ' + griText(inst.f) + ' and g(n) = ' + griText(inst.g)
        + (rel === 'O' ? ', c₂ = ' : (rel === 'Omega' ? ', c₁ = ' : ', c₁ = ' + itaQ(c1) + ', c₂ = ')) + itaQ(rel === 'Omega' ? c1 : c2)
        + ', n₀ = ' + eaInt(n0) + '. ' + (fail ? 'The witness fails at n = ' + eaInt(fail.n) + ' (' + at(fail, fail.n) + '). '
          : 'The witness holds at every n the lab tried; that is evidence about ' + eaInt(checks) + ' values of n, and only a proof covers every n ≥ n₀. ')
        + 'Every inequality is decided exactly, lg n included; a value with lg n in it prints rounded.',
      table: null
    };
  };
"""


def _menu_term(what):
    return ea.rec(what, [("coef", ea.num(lo=-ea.LIMIT)), ("fn", ea.word(*BOUND_FNS))], rows=2, hi=4)


def _check_race(inst, fixed):
    for side in ("A", "B"):
        if inst["fn" + side] == "2^n" and inst["n"] > EXP_CAP:
            raise ValueError("Program %s costs 2^n, and 2^n seconds past n = 4,096 is too large to print; "
                             "choose n of at most 4,096" % side)


def _check_bounds(inst, fixed):
    big = any(t["fn"] in BIG_FNS for t in inst["f"] + inst["g"])
    if big and inst["n0"] > BIG_N0:
        raise ValueError("With F(n), 2^n or n! in f or g, n₀ is at most 1,000 (the check runs to n₀ + 10,000)")


# ---------------------------------------------------------------------------
# sorting (sti): insertion sort pass by pass, its cost, merge sort by level
# ---------------------------------------------------------------------------

STI_JS = r"""
  var STI_VIEW = {};
  function stiCompute(view, inst, opts) { return eaRun(STI_VIEW[view], inst, opts); }
  /* INSERTION-SORT on a copy, one record a pass j = 2..n (one-based). A key
     comparison is a test A[i] > key; the loop stops without one when i
     reaches 0. t_j is the number of times the while test runs: shifts + 1. */
  function stiInsertion(list) {
    var A = list.map(function (r) { return r.n; }), passes = [], n = A.length, j;
    var sorted = function (a) { return a.slice().sort(function (x, y) { return x < y ? -1 : (x > y ? 1 : 0); }); };
    var same = function (a, b) { return a.length === b.length && a.every(function (x, i) { return x === b[i]; }); };
    var checks = 0, held = 0;
    for (j = 1; j <= n; j += 1) {
      checks += 1;
      if (same(A.slice(0, j), sorted(list.slice(0, j).map(function (r) { return r.n; })))) held += 1;
      if (j === n) break;
      var key = A[j], i = j - 1, comps = 0, shifts = 0, before = A.slice(0, j);
      while (i >= 0) {
        comps += 1;
        if (A[i] > key) { A[i + 1] = A[i]; i -= 1; shifts += 1; } else break;
      }
      A[i + 1] = key;
      passes.push({ j: j + 1, key: key, before: before, comps: comps, shifts: shifts, t: shifts + 1, after: A.slice() });
    }
    var sum = function (k) { return passes.reduce(function (s, p) { return s + p[k]; }, 0); };
    return { passes: passes, n: n, A: A, checks: checks, held: held, comps: sum('comps'), shifts: sum('shifts'), sumT: sum('t') };
  }
"""

STI_VIEW_JS = {}

STI_VIEW_JS["insertion"] = r"""
  STI_VIEW.insertion = function (inst) {
    var s = stiInsertion(inst.list), n = s.n;
    return {
      tiles: {
        stiComparisons: eaInt(s.comps), stiShifts: eaInt(s.shifts),
        stiInvariant: (s.held === s.checks ? 'holds at all ' : 'fails at ' + (s.checks - s.held) + ' of ') + eaInt(s.checks)
          + ' checks, j = 2 to ' + eaInt(n + 1),
        stiSorted: itaList(s.A)
      },
      status: 'The invariant, checked at the start of each pass and at the end: A[1..j − 1] holds the elements first in A[1..j − 1], in sorted order. '
        + 'At j = 2 that is initialisation, at each later j maintenance, and at j = n + 1 = ' + eaInt(n + 1) + ' termination: the whole array sorted. '
        + 'Checking it on this array is evidence; the proof is the argument for every array.',
      table: { caption: 'Each pass of INSERTION-SORT', head: ['j', 'key', 'A[1..j − 1] before', 'comparisons', 'shifts', 'array after'],
        rows: s.passes.map(function (p) { return [String(p.j), eaInt(p.key), itaList(p.before), String(p.comps), String(p.shifts), itaList(p.after)]; }) }
    };
  };
"""

STI_VIEW_JS["cost"] = r"""
  STI_VIEW.cost = function (inst) {
    var s = stiInsertion(inst.list), n = BigInt(s.n), sumT = BigInt(s.sumT), inner = sumT - (n - 1n);
    var lines = n + 3n * (n - 1n) + sumT + 2n * inner;
    var best = 5n * n - 4n, worst = (3n * n * n + 7n * n - 8n) / 2n;
    return {
      tiles: {
        stiTj: s.passes.length ? s.passes.map(function (p) { return String(p.t); }).join(', ') : 'none (n = 1)',
        stiSumTj: eaInt(sumT), stiComparisons: eaInt(s.comps), stiShifts: eaInt(s.shifts),
        stiBest: 'n − 1 = ' + eaInt(n - 1n), stiWorst: 'n(n − 1)/2 = ' + eaInt(n * (n - 1n) / 2n),
        stiLines: eaInt(lines) + ' (best 5n − 4 = ' + eaInt(best) + ', worst (3n² + 7n − 8)/2 = ' + eaInt(worst) + ')'
      },
      status: 'The comparisons lie between the best case n − 1 (already sorted) and the worst case n(n − 1)/2 (reverse sorted); '
        + 'the shifts equal the inversions of the array. Lines executed: line 1 runs n times, lines 2, 4 and 8 n − 1 times each, '
        + 'line 5 Σt_j times and lines 6 and 7 Σ(t_j − 1) times; each counts 1, so the total is the running time with every c_i = 1.',
      table: { caption: 'Each pass: t_j and what it counts', head: ['j', 'key', 't_j', 'comparisons', 'shifts'],
        rows: s.passes.map(function (p) { return [String(p.j), eaInt(p.key), String(p.t), String(p.comps), String(p.shifts)]; }) }
    };
  };
"""

STI_VIEW_JS["merge"] = r"""
  STI_VIEW.merge = function (inst) {
    var A = inst.list.map(function (r) { return r.n; }), n = A.length, levels = [], depthMax = 0;
    /* MERGE-SORT(A, p, r) with q = floor((p + r)/2); a merge compares until
       one half runs out. CLRS's MERGE with sentinels compares r − p + 1 times. */
    function sort(p, r, depth) {
      if (p >= r) return;
      var q = Math.floor((p + r) / 2);
      sort(p, q, depth + 1); sort(q + 1, r, depth + 1);
      var L = A.slice(p, q + 1), Rr = A.slice(q + 1, r + 1), i = 0, j = 0, k = p, c = 0;
      while (i < L.length && j < Rr.length) { c += 1; if (L[i] <= Rr[j]) A[k++] = L[i++]; else A[k++] = Rr[j++]; }
      while (i < L.length) A[k++] = L[i++];
      while (j < Rr.length) A[k++] = Rr[j++];
      if (!levels[depth]) levels[depth] = { merges: 0, size: 0, comps: 0 };
      levels[depth].merges += 1; levels[depth].size += r - p + 1; levels[depth].comps += c;
      if (depth > depthMax) depthMax = depth;
    }
    sort(0, n - 1, 1);
    var total = 0, sent = 0, per = [], rows = [];
    for (var d = 1; d < levels.length; d += 1) {
      var L2 = levels[d];
      total += L2.comps; sent += L2.size;
      per.push('level ' + d + ': ' + eaInt(L2.comps));
      rows.push([String(d), String(L2.merges), String(L2.size), String(L2.comps)]);
    }
    var N = BigInt(n), lg = 0n;
    while ((1n << lg) < N) lg += 1n;
    var bound = N * lg - (1n << lg) + 1n;
    return {
      tiles: {
        stiLevels: eaInt(levels.length ? levels.length - 1 : 0) + ' (⌈lg n⌉ = ' + eaInt(lg) + ')',
        stiPerLevel: per.length ? per.join('; ') : 'none (n = 1)',
        stiMergeTotal: eaInt(total),
        stiMergeBound: 'n⌈lg n⌉ − 2^⌈lg n⌉ + 1 = ' + eaInt(bound),
        stiSentinel: eaInt(sent),
        stiSorted: itaList(A)
      },
      status: 'Level 1 is the last merge, of the whole array; level ' + eaInt(lg) + ' merges the smallest pieces. '
        + 'A merge here stops comparing when one half runs out, so it makes at most (its length − 1) comparisons, and the total never exceeds '
        + 'n⌈lg n⌉ − 2^⌈lg n⌉ + 1, the worst case. CLRS\'s MERGE with ∞ sentinels makes exactly one comparison an element merged: '
        + eaInt(sent) + ' here, n at each full level.',
      table: { caption: 'Merges by level (level 1 is the top)', head: ['level', 'merges', 'elements merged', 'comparisons'], rows: rows }
    };
  };
"""


def _array(what, lo=1, hi=40):
    return {"kind": "list", "what": what, "control": "text", "lo": lo, "hi": hi, "things": "numbers",
            "each": ea.whole(-ea.LIMIT, ea.LIMIT)}


# ---------------------------------------------------------------------------
# recurrence (rci): T(n) = a T(n/b) + c n^k lg^p n, exactly at n = b^j
# ---------------------------------------------------------------------------

RCI_JS = r"""
  var RCI_VIEW = {};
  function rciCompute(view, inst, opts) { return eaRun(RCI_VIEW[view], inst, opts); }
  /* The integer r with r^v = b, or null. */
  function rciRoot(b, v) {
    if (v === 1n) return b;
    if (v > 64n) return null;
    var g = BigInt(Math.round(Math.pow(Number(b), 1 / Number(v))));
    for (var r = (g > 2n ? g - 1n : 2n); r <= g + 1n; r += 1n) if (r ** v === b) return r;
    return null;
  }
  function rciPow2(b) { var e = 0n; while ((1n << e) < b) e += 1n; return (1n << e) === b ? e : null; }
  function rciExp(k) { return Rint(k) ? (Requ(k, R1) ? '' : '^' + eaInt(k.n)) : '^(' + itaQ(k) + ')'; }
  function rciF(c, k, p) {
    var parts = [];
    if (Rsign(k) !== 0) parts.push('n' + rciExp(k));
    if (p > 0n) parts.push('lg' + (p === 1n ? '' : '^' + p) + ' n');
    var s = parts.join(' ');
    if (s === '') s = '1';
    if (p < 0n) s = s + '/lg' + (p === -1n ? '' : '^' + (-p)) + ' n';
    if (!Requ(c, R1)) s = itaQ(c) + (s === '1' ? '' : ' ' + s);
    return s;
  }
  /* Everything both views print, exactly. */
  function rciSolve(inst) {
    var a = inst.a.n, b = inst.b.n, c = inst.c, k = inst.k, p = inst.p.n, J = inst.j.n;
    var root = rciRoot(b, BigInt(k.d)), lgb = rciPow2(b);
    if (root === null) eaRefuse('b^k = ' + eaInt(b) + '^' + itaQ(k) + ' is not a whole number, so f(b^j) is not exact; choose k with b^k whole');
    if (p !== 0n && lgb === null) eaRefuse('With p ≠ 0, b must be a power of 2, so that lg n is a whole number at every n = b^j');
    var bk = root ** BigInt(k.n);
    var f = function (j) { return Rmul(Rmul(c, R(bk ** j)), p === 0n ? R1 : Rpow(R(j * lgb), Number(p))); };
    var T = [inst.t1];
    for (var j = 1n; j <= J; j += 1n) T.push(Radd(Rmul(R(a), T[T.length - 1]), f(j)));
    /* n^(log_b a): a power, a rational power, or irrational. */
    var crit = null, v, u;
    for (v = 1n; v <= 6n && crit === null; v += 1n) {
      var t = a ** v, e = 0n, q = 1n;
      while (q < t) { q *= b; e += 1n; }
      if (q === t) crit = R(e, v);
    }
    var critText = crit !== null ? (Rsign(crit) === 0 ? '1' : 'n' + rciExp(crit))
      : 'n^(log_' + eaInt(b) + ' ' + eaInt(a) + ') ≈ n^' + (Math.log(Number(a)) / Math.log(Number(b))).toFixed(3);
    var cmp = bk < a ? -1 : (bk > a ? 1 : 0), kase, sol, pred;
    if (cmp < 0) {
      kase = 'case 1: f(n) = O(n^(log_b a − ε))';
      sol = 'Θ(' + critText.replace(/ ≈ .*$/, '') + ')';
      pred = function (j) { return R(a ** j); };
    } else if (cmp === 0 && p === 0n) {
      kase = 'case 2: f(n) = Θ(n^(log_b a))';
      sol = 'Θ(' + (critText === '1' ? 'lg n' : critText.replace(/ ≈ .*$/, '') + ' lg n') + ')';
      pred = function (j) { return R(a ** j * j); };
    } else if (cmp === 0) {
      kase = p > 0n ? 'falls in the gap between cases 2 and 3' : 'falls in the gap between cases 1 and 2';
      sol = p > 0n ? 'no case applies (Exercise 4.6-2 extends case 2: Θ(' + (critText === '1' ? '' : critText.replace(/ ≈ .*$/, '') + ' ') + 'lg^' + (p + 1n) + ' n))'
        : 'no case applies';
      pred = p > 0n ? function (j) { return R(a ** j * j ** (p + 1n)); } : function (j) { return R(a ** j); };
    } else {
      kase = 'case 3: f(n) = Ω(n^(log_b a + ε))' + (p >= 0n ? ', and a·f(n/b) ≤ (' + itaQ(R(a, bk)) + ')·f(n)' : ', regular for large n');
      sol = 'Θ(' + rciF(R1, k, p) + ')';
      pred = f;
    }
    return { a: a, b: b, c: c, k: k, p: p, J: J, bk: bk, f: f, T: T, crit: critText, kase: kase, sol: sol, pred: pred, cmp: cmp };
  }
"""

RCI_VIEW_JS = {}

RCI_VIEW_JS["master"] = r"""
  RCI_VIEW.master = function (inst) {
    var s = rciSolve(inst), rows = [], J = s.J;
    for (var j = 0n; j <= J; j += 1n) {
      var g = j === 0n ? null : s.pred(j);
      rows.push([eaInt(j), eaNum(R(s.b ** j)), eaNum(s.T[Number(j)]), j === 0n ? EA_DASH : eaNum(s.f(j)), eaNum(R(s.a ** j)),
        g === null || Rsign(g) === 0 ? EA_DASH : eaNum(Rdiv(s.T[Number(j)], g))]);
    }
    var gJ = s.pred(J);
    return {
      tiles: {
        rciCritical: s.crit, rciCase: s.kase, rciSolution: s.sol,
        rciLast: 'T(' + eaNum(R(s.b ** J)) + ') = ' + eaNum(s.T[Number(J)]),
        rciRatio: Rsign(gJ) === 0 ? EA_DASH : eaNum(Rdiv(s.T[Number(J)], gJ))
      },
      status: 'T(n) = ' + eaInt(s.a) + 'T(n/' + eaInt(s.b) + ') + ' + rciF(s.c, s.k, s.p) + ', T(1) = ' + itaQ(inst.t1)
        + ', evaluated exactly at n = ' + eaInt(s.b) + '^j. The case is decided on integers: b^k = ' + eaInt(s.bk)
        + (s.cmp < 0 ? ' < ' : (s.cmp > 0 ? ' > ' : ' = ')) + 'a = ' + eaInt(s.a) + '. The last column divides T(n) by the predicted growth'
        + ' (n^(log_b a), times log_b n in case 2, f(n) in case 3); a ratio settling to a constant is what Θ predicts, and '
        + 'a few values of n are evidence, not the theorem.',
      table: { caption: 'T(n) at n = b^j', head: ['j', 'n', 'T(n)', 'f(n)', 'n^(log_b a) = a^j', 'T(n) / predicted'], rows: rows }
    };
  };
"""

RCI_VIEW_JS["tree"] = r"""
  RCI_VIEW.tree = function (inst) {
    var s = rciSolve(inst), J = s.J, rows = [], sums = [], total = R0;
    for (var i = 0n; i < J; i += 1n) {
      var each = s.f(J - i), sum = Rmul(R(s.a ** i), each);
      sums.push(sum); total = Radd(total, sum);
      rows.push([eaInt(i), eaNum(R(s.a ** i)), eaNum(R(s.b ** (J - i))), eaNum(each), eaNum(sum)]);
    }
    var leaves = Rmul(R(s.a ** J), inst.t1);
    total = Radd(total, leaves);
    rows.push(['leaves', eaNum(R(s.a ** J)), '1', itaQ(inst.t1), eaNum(leaves)]);
    var shown = sums.map(eaNum);
    if (shown.length > 6) shown = shown.slice(0, 3).concat(['…', shown[shown.length - 1]]);
    var trend;
    if (s.p !== 0n) trend = 'changes from level to level (p ≠ 0)';
    else {
      var q = R(s.a, s.bk);
      trend = 'each level ' + itaQ(q) + ' × the one above: ' + (s.cmp > 0 ? 'decreasing, the root dominates'
        : (s.cmp < 0 ? 'increasing, the leaves dominate' : 'every level the same'));
    }
    return {
      tiles: {
        rciLevelSums: shown.join(', '), rciLeaves: eaNum(R(s.a ** J)) + ' × T(1) = ' + eaNum(leaves),
        rciTreeTotal: eaNum(total), rciLast: 'T(' + eaNum(R(s.b ** J)) + ') = ' + eaNum(s.T[Number(J)]),
        rciTrend: trend, rciCase: s.kase
      },
      status: 'The recursion tree of T(n) at n = ' + eaInt(s.b) + '^' + eaInt(J) + ': level i has a^i nodes, each a subproblem of size n/b^i costing f(n/b^i); '
        + 'the ' + eaNum(R(s.a ** J)) + ' leaves cost T(1) each. The levels and leaves add up to the recurrence\'s own T(n), exactly.',
      table: { caption: 'The recursion tree, level by level', head: ['level', 'nodes', 'size', 'cost a node', 'level sum'], rows: rows }
    };
  };
"""


def _int_root(b, v):
    if v == 1:
        return b
    if v > 64:
        return None
    g = round(b ** (1.0 / v))
    for r in range(max(2, g - 1), g + 2):
        if r ** v == b:
            return r
    return None


def _check_recurrence(inst, fixed):
    b, k, p = int(inst["b"]), Fraction(inst["k"]), int(inst["p"])
    if _int_root(b, k.denominator) is None:
        raise ValueError("b^k = %d^%s is not a whole number, so f(b^j) is not exact; choose k with b^k whole" % (b, k))
    if p != 0 and b & (b - 1):
        raise ValueError("With p ≠ 0, b must be a power of 2, so that lg n is a whole number at every n = b^j")


# ---------------------------------------------------------------------------
# maxsub (msi): the maximum subarray by three routes
# ---------------------------------------------------------------------------

MSI_JS = r"""
  var MSI_VIEW = {};
  function msiCompute(view, inst, opts) { return eaRun(MSI_VIEW[view], inst, opts); }
"""

MSI_VIEW_JS = {}

MSI_VIEW_JS["compare"] = r"""
  /* Brute force: every pair i <= j, a running sum; the first best wins. */
  function msiBrute(A) {
    var best = null, steps = 0n;
    for (var i = 0; i < A.length; i += 1) {
      var s = 0n;
      for (var j = i; j < A.length; j += 1) {
        s += A[j]; steps += 1n;
        if (best === null || s > best.sum) best = { l: i, r: j, sum: s };
      }
    }
    return { best: best, steps: steps };
  }
  /* FIND-MAXIMUM-SUBARRAY and FIND-MAX-CROSSING-SUBARRAY (CLRS 4.1), with
     its tie order: the left half, then the right, then the crossing. */
  function msiDc(A) {
    var calls = 0n, scanned = 0n;
    function cross(lo, mid, hi) {
      var ls = null, s = 0n, ml = mid, rs = null, mr = mid + 1, i;
      for (i = mid; i >= lo; i -= 1) { s += A[i]; scanned += 1n; if (ls === null || s > ls) { ls = s; ml = i; } }
      s = 0n;
      for (i = mid + 1; i <= hi; i += 1) { s += A[i]; scanned += 1n; if (rs === null || s > rs) { rs = s; mr = i; } }
      return { l: ml, r: mr, sum: ls + rs };
    }
    function find(lo, hi) {
      calls += 1n;
      if (lo === hi) return { l: lo, r: hi, sum: A[lo] };
      var mid = Math.floor((lo + hi) / 2), L = find(lo, mid), Rt = find(mid + 1, hi), C = cross(lo, mid, hi);
      if (L.sum >= Rt.sum && L.sum >= C.sum) return L;
      if (Rt.sum >= L.sum && Rt.sum >= C.sum) return Rt;
      return C;
    }
    return { best: find(0, A.length - 1), calls: calls, scanned: scanned };
  }
  /* One pass (Exercise 4.1-5): the best subarray ending at j extends the one
     ending at j − 1 while that one's sum is positive. */
  function msiLinear(A) {
    var best = null, cur = null, steps = 0n;
    for (var j = 0; j < A.length; j += 1) {
      steps += 1n;
      cur = (cur !== null && cur.sum > 0n) ? { l: cur.l, r: j, sum: cur.sum + A[j] } : { l: j, r: j, sum: A[j] };
      if (best === null || cur.sum > best.sum) best = cur;
    }
    return { best: best, steps: steps };
  }
  function msiShow(b) { return 'A[' + (b.l + 1) + '..' + (b.r + 1) + '], sum ' + eaInt(b.sum); }
  MSI_VIEW.compare = function (inst) {
    var A = inst.list.map(function (r) { return r.n; }), n = BigInt(A.length);
    var x = msiBrute(A), y = msiDc(A), z = msiLinear(A);
    var sums = x.best.sum === y.best.sum && y.best.sum === z.best.sum;
    var same = [y.best, z.best].every(function (b) { return b.l === x.best.l && b.r === x.best.r; });
    return {
      tiles: {
        msiBrute: msiShow(x.best), msiDc: msiShow(y.best), msiLinear: msiShow(z.best),
        msiBruteSteps: eaInt(x.steps) + ' sums (n(n + 1)/2)',
        msiDcSteps: eaInt(y.calls) + ' calls, ' + eaInt(y.scanned) + ' elements scanned across the middle',
        msiLinearSteps: eaInt(z.steps) + ' elements, one pass',
        msiAgree: sums ? 'yes: all three find sum ' + eaInt(x.best.sum) + (same ? ', the same subarray' : ', by tie-breaking not all the same subarray') : 'no'
      },
      status: 'Indices are one-based, as in the book. A subarray is never empty, so an array of negative numbers has its largest element as the answer. '
        + 'Brute force adds A[j] to a running sum for every i ≤ j; divide-and-conquer makes 2n − 1 calls and scans each call\'s range once for the crossing subarray, '
        + 'about n lg n elements in all; the one-pass scan touches each element once. The counts are for this array; the bounds are the book\'s proofs.',
      table: { caption: 'The three routes', head: ['route', 'subarray', 'sum', 'steps'],
        rows: [['brute force', 'A[' + (x.best.l + 1) + '..' + (x.best.r + 1) + ']', eaInt(x.best.sum), eaInt(x.steps)],
          ['divide-and-conquer', 'A[' + (y.best.l + 1) + '..' + (y.best.r + 1) + ']', eaInt(y.best.sum), eaInt(y.calls + y.scanned)],
          ['one pass', 'A[' + (z.best.l + 1) + '..' + (z.best.r + 1) + ']', eaInt(z.best.sum), eaInt(z.steps)]] }
    };
  };
"""

# ---------------------------------------------------------------------------
# hiring (hri): hires on one order, and the average over every order
# ---------------------------------------------------------------------------

HRI_ALL = 9                 # every order is averaged up to n = 9 (362,880 orders)

HRI_JS = r"""
  var HRI_VIEW = {};
  function hriCompute(view, inst, opts) { return eaRun(HRI_VIEW[view], inst, opts); }
"""

HRI_VIEW_JS = {}

HRI_VIEW_JS["order"] = r"""
  function hriHires(a) {
    var best = 0, who = [];
    for (var i = 0; i < a.length; i += 1) if (a[i] > best) { best = a[i]; who.push(i + 1); }
    return who;
  }
  /* Every order of 1..n by Heap's algorithm: how many orders give k hires. */
  function hriAll(n) {
    var a = [], c = [], by = [], i, k;
    for (i = 0; i < n; i += 1) { a.push(i + 1); c.push(0); }
    for (k = 0; k <= n; k += 1) by.push(0);
    by[hriHires(a).length] += 1;
    i = 1;
    while (i < n) {
      if (c[i] < i) {
        var s = i % 2 === 0 ? 0 : c[i], t = a[s]; a[s] = a[i]; a[i] = t;
        by[hriHires(a).length] += 1;
        c[i] += 1; i = 1;
      } else { c[i] = 0; i += 1; }
    }
    return by;
  }
  HRI_VIEW.order = function (inst) {
    var a = inst.order.map(function (r) { return Number(r.n); }), n = a.length, seen = {};
    a.forEach(function (x, i) {
      if (x < 1 || x > n) eaRefuse('The order ranks ' + n + ' candidates, so each rank is from 1 to ' + n + ', and entry ' + (i + 1) + ' is ' + x);
      if (seen[x]) eaRefuse('The order gives rank ' + x + ' twice; it is a permutation of 1 to ' + n);
      seen[x] = true;
    });
    var who = hriHires(a), m = BigInt(who.length), N = BigInt(n);
    var H = R0;
    for (var k = 1n; k <= N; k += 1n) H = Radd(H, R(1n, k));
    var cost = Radd(Rmul(inst.ci, R(N)), Rmul(inst.ch, R(m)));
    var tiles = {
      hriHires: eaInt(m) + ': candidate' + (who.length === 1 ? ' ' : 's ') + who.join(', '),
      hriCost: eaNum(cost), hriHarmonic: eaNum(H),
      hriExpectedCost: eaNum(Radd(Rmul(inst.ci, R(N)), Rmul(inst.ch, H)))
    };
    var rows = [], status;
    if (n <= 9) {
      var by = hriAll(n), total = 0n, orders = 0n;
      by.forEach(function (cnt, h) { total += BigInt(cnt) * BigInt(h); orders += BigInt(cnt); });
      by.forEach(function (cnt, h) { if (cnt) rows.push([String(h), eaInt(cnt), eaPct(R(BigInt(cnt), orders))]); });
      var avg = R(total, orders);
      tiles.hriAverage = eaNum(avg) + ' over ' + eaInt(orders) + ' orders';
      tiles.hriAgree = Requ(avg, H) ? 'yes: the average is H_' + n : 'no';
      status = 'The lab ran the hiring loop on all ' + eaInt(orders) + ' orders of ' + n + ' candidates and averaged the hires: that average is the expectation '
        + 'under a uniformly random order, and it equals H_n = 1 + 1/2 + … + 1/n, as the indicator-variable argument says it must.';
    } else {
      tiles.hriAverage = 'not run: n > 9 (' + n + '! orders)';
      tiles.hriAgree = EA_DASH;
      status = 'With ' + n + ' candidates the lab runs the one order given; averaging every order runs only up to n = 9. H_n is still exact.';
    }
    return {
      tiles: tiles,
      status: status + ' A candidate is hired when better than everyone seen so far (a higher rank is better). '
        + 'The cost is c_i·n + c_h·m for n interviews and m hires.',
      table: rows.length ? { caption: 'Orders of 1..' + n + ' by number of hires', head: ['hires', 'orders', 'share'], rows: rows } : null
    };
  };
"""


def _check_order(inst, fixed):
    a = [int(x) for x in inst["order"]]
    n, seen = len(a), set()
    for i, x in enumerate(a):
        if not 1 <= x <= n:
            raise ValueError("The order ranks %d candidates, so each rank is from 1 to %d, and entry %d is %d" % (n, n, i + 1, x))
        if x in seen:
            raise ValueError("The order gives rank %d twice; it is a permutation of 1 to %d" % (x, n))
        seen.add(x)


# ---------------------------------------------------------------------------
# workspan (wsi): work, span and parallelism of a computation DAG
# ---------------------------------------------------------------------------

WSI_JS = r"""
  var WSI_VIEW = {};
  function wsiCompute(view, inst, opts) { return eaRun(WSI_VIEW[view], inst, opts); }
  function wsiBounds(work, span, P) {
    var p = R(P);
    return {
      wsiWork: eaInt(work), wsiSpan: eaInt(span), wsiParallelism: eaNum(R(work, span)),
      wsiBound: eaNum(Radd(R(work, P), R(span))),
      wsiLower: eaNum(Rcmp(R(work, P), R(span)) >= 0 ? R(work, P) : R(span))
    };
  }
  var WSI_RULE = ' The greedy-scheduler bound is T_P ≤ T₁/P + T∞; no scheduler beats T_P ≥ max(T₁/P, T∞). Parallelism T₁/T∞ caps the speedup.';
"""

WSI_VIEW_JS = {}

WSI_VIEW_JS["dag"] = r"""
  WSI_VIEW.dag = function (inst) {
    var idx = {}, S = inst.strands, n = S.length, out = [], indeg = [], i;
    S.forEach(function (s, k) { idx[s.strand] = k; out.push([]); indeg.push(0); });
    var seen = {};
    inst.edges.forEach(function (e, k) {
      [e.from, e.to].forEach(function (x) { if (idx[x] === undefined) eaRefuse('Edges, record ' + (k + 1) + ' names ' + x + ', which is not a strand'); });
      if (e.from === e.to) eaRefuse('Edges, record ' + (k + 1) + ' joins ' + e.from + ' to itself');
      if (seen[e.from + '>' + e.to]) eaRefuse('Edges lists ' + e.from + ', ' + e.to + ' twice');
      seen[e.from + '>' + e.to] = true;
      out[idx[e.from]].push(idx[e.to]); indeg[idx[e.to]] += 1;
    });
    var order = [], ready = [], deg = indeg.slice();
    for (i = 0; i < n; i += 1) if (deg[i] === 0) ready.push(i);
    while (ready.length) {
      ready.sort(function (x, y) { return x - y; });
      var u = ready.shift(); order.push(u);
      out[u].forEach(function (v) { deg[v] -= 1; if (deg[v] === 0) ready.push(v); });
    }
    if (order.length < n) {
      var left = S.filter(function (s, k) { return deg[k] > 0; }).map(function (s) { return s.strand; });
      eaRefuse('The edges form a cycle through ' + left.join(', ') + '; a computation DAG has none');
    }
    var fin = [], from = [], work = 0n;
    order.forEach(function (u) {
      var best = 0n, by = -1;
      S.forEach(function (s, k) { if (out[k].indexOf(u) >= 0 && (by < 0 || fin[k] > best)) { best = fin[k]; by = k; } });
      fin[u] = best + S[u].cost.n; from[u] = by; work += S[u].cost.n;
    });
    var end = 0;
    for (i = 1; i < n; i += 1) if (fin[i] > fin[end]) end = i;
    var path = [];
    for (var at = end; at >= 0; at = from[at]) path.unshift(S[at].strand);
    var tiles = wsiBounds(work, fin[end], inst.p.n);
    tiles.wsiCritical = path.join(' → ');
    return {
      tiles: tiles,
      status: 'Work T₁ is the sum of the strands\' costs; span T∞ is the costliest path, strand costs added along it. On P = ' + eaInt(inst.p.n) + ' processors.' + WSI_RULE,
      table: { caption: 'Each strand, in a topological order', head: ['strand', 'cost', 'finishes at (longest path to it)', 'after'],
        rows: order.map(function (u) { return [S[u].strand, eaInt(S[u].cost.n), eaInt(fin[u]), from[u] < 0 ? EA_DASH : S[from[u]].strand]; }) }
    };
  };
"""

WSI_VIEW_JS["recurrence"] = r"""
  WSI_VIEW.recurrence = function (inst) {
    var n = inst.n.n, P = inst.p.n, rows = [], tiles, path = [], status;
    if (inst.program === 'p-fib') {
      if (n > 40n) eaRefuse('P-FIB takes n of at most 40 here');
      /* Strands of unit cost: P-FIB(n) for n ≥ 2 is three strands (test and
         spawn; the call of P-FIB(n − 2); the sum after the sync); n ≤ 1 is one. */
      var W = [1n, 1n], Sp = [1n, 1n], k;
      for (k = 2; k <= Number(n); k += 1) {
        W.push(W[k - 1] + W[k - 2] + 3n);
        Sp.push(2n + Sp[k - 1] > 3n + Sp[k - 2] ? 2n + Sp[k - 1] : 3n + Sp[k - 2]);
      }
      for (k = 0; k <= Number(n); k += 1) rows.push([String(k), eaInt(W[k]), eaInt(Sp[k]), eaNum(R(W[k], Sp[k]))]);
      for (k = Number(n); ; ) {
        path.push('P-FIB(' + k + ')');
        if (k <= 1) break;
        k = (2n + Sp[k - 1] >= 3n + Sp[k - 2]) ? k - 1 : k - 2;
      }
      tiles = wsiBounds(W[Number(n)], Sp[Number(n)], P);
      status = 'P-FIB with every strand costing 1: T₁(n) = T₁(n − 1) + T₁(n − 2) + 3 and T∞(n) = max(T∞(n − 1) + 2, T∞(n − 2) + 3), with T₁ = T∞ = 1 at n ≤ 1. '
        + 'The work grows like the Fibonacci numbers and the span by 2 a level, so the parallelism grows without bound.';
    } else {
      if (n < 1n) eaRefuse('MERGE-SORT′ needs n of at least 1');
      /* MERGE-SORT′: spawn one half, sort the other, sync, merge serially. A
         call on 1 element costs 1; merging m elements costs m. */
      var memo = {};
      var go = function (m) {
        if (memo[m]) return memo[m];
        if (m === 1n) return (memo[m] = { w: 1n, s: 1n });
        var a = go((m + 1n) / 2n), b = go(m / 2n);
        return (memo[m] = { w: a.w + b.w + m, s: (a.s > b.s ? a.s : b.s) + m });
      };
      var top = go(n);
      for (var m = n; ; m = (m + 1n) / 2n) {
        var r = go(m);
        path.push(eaInt(m));
        rows.push([eaInt(m), eaInt(r.w), eaInt(r.s), eaNum(R(r.w, r.s))]);
        if (m === 1n) break;
      }
      tiles = wsiBounds(top.w, top.s, P);
      path = ['sizes ' + path.join(' → ')];
      status = 'MERGE-SORT′ (section 27.3): the two halves run in parallel, then a serial merge. T₁(n) = T₁(⌈n/2⌉) + T₁(⌊n/2⌋) + n and '
        + 'T∞(n) = T∞(⌈n/2⌉) + n, with 1 at n = 1: the serial merge keeps the span linear, so the parallelism is only about lg n.';
    }
    tiles.wsiCritical = path.join(' → ');
    return {
      tiles: tiles, status: status + ' On P = ' + eaInt(P) + ' processors.' + WSI_RULE,
      table: { caption: inst.program === 'p-fib' ? 'P-FIB(k) for k = 0 to n' : 'The calls down the critical path, by size',
        head: [inst.program === 'p-fib' ? 'k' : 'size', 'work T₁', 'span T∞', 'parallelism'], rows: rows }
    };
  };
"""


def _check_dag(inst, fixed):
    names = [s["strand"] for s in inst["strands"]]
    out, seen = {n: [] for n in names}, set()
    for k, e in enumerate(inst["edges"]):
        for x in (e["from"], e["to"]):
            if x not in out:
                raise ValueError("Edges, record %d names %s, which is not a strand" % (k + 1, x))
        if e["from"] == e["to"]:
            raise ValueError("Edges, record %d joins %s to itself" % (k + 1, e["from"]))
        if (e["from"], e["to"]) in seen:
            raise ValueError("Edges lists %s, %s twice" % (e["from"], e["to"]))
        seen.add((e["from"], e["to"]))
        out[e["from"]].append(e["to"])
    deg = {n: 0 for n in names}
    for n in names:
        for v in out[n]:
            deg[v] += 1
    ready, done = [n for n in names if deg[n] == 0], 0
    while ready:
        u = ready.pop()
        done += 1
        for v in out[u]:
            deg[v] -= 1
            if deg[v] == 0:
                ready.append(v)
    if done < len(names):
        left = [n for n in names if deg[n] > 0]
        raise ValueError("The edges form a cycle through %s; a computation DAG has none" % ", ".join(left))


def _check_wsrec(inst, fixed):
    if inst["program"] == "p-fib" and inst["n"] > 40:
        raise ValueError("P-FIB takes n of at most 40 here")
    if inst["program"] == "merge-sort" and inst["n"] < 1:
        raise ValueError("MERGE-SORT′ needs n of at least 1")


# ---------------------------------------------------------------------------
# lup (lui): LUP decomposition and LUP-SOLVE, exactly
# ---------------------------------------------------------------------------

LUI_JS = r"""
  var LUI_VIEW = {};
  function luiCompute(view, inst, opts) { return eaRun(LUI_VIEW[view], inst, opts); }
  function luiSize(count) {
    for (var n = 1; n <= 5; n += 1) if (n * n === count) return n;
    eaRefuse('The matrix has ' + count + ' entries; a square matrix has 1, 4, 9, 16 or 25');
  }
  function luiRows(M) { return M.map(function (row) { return row.map(itaQ).join(', '); }).join('; '); }
"""

LUI_VIEW_JS = {}

LUI_VIEW_JS["decompose"] = r"""
  LUI_VIEW.decompose = function (inst) {
    var n = luiSize(inst.matrix.length), A = [], orig = [], pi = [], i, j, k, steps = [];
    for (i = 0; i < n; i += 1) { A.push(inst.matrix.slice(i * n, i * n + n)); orig.push(A[i].slice()); pi.push(i); }
    if (inst.b.length && inst.b.length !== n) eaRefuse('b has ' + inst.b.length + ' entries and the matrix ' + n + ' rows; give b with ' + n + ' entries, or none');
    /* LUP-DECOMPOSITION (CLRS 28.1): the pivot is the entry of largest
       absolute value on or below the diagonal, the first such on a tie. */
    var pivots = [], sign = 1;
    for (k = 0; k < n; k += 1) {
      var p = -1, best = R0;
      for (i = k; i < n; i += 1) if (Rcmp(Rabs(A[i][k]), best) > 0) { best = Rabs(A[i][k]); p = i; }
      if (p < 0) eaRefuse('The matrix is singular: column ' + (k + 1) + ' has no nonzero pivot on or below the diagonal');
      if (p !== k) { var t = pi[k]; pi[k] = pi[p]; pi[p] = t; t = A[k]; A[k] = A[p]; A[p] = t; sign = -sign; }
      pivots.push(A[k][k]);
      var mult = [];
      for (i = k + 1; i < n; i += 1) {
        A[i][k] = Rdiv(A[i][k], A[k][k]); mult.push(itaQ(A[i][k]));
        for (j = k + 1; j < n; j += 1) A[i][j] = Rsub(A[i][j], Rmul(A[i][k], A[k][j]));
      }
      steps.push([String(k + 1), 'row ' + (pi[k] + 1), itaQ(A[k][k]), mult.length ? mult.join(', ') : EA_DASH]);
    }
    var L = [], U = [];
    for (i = 0; i < n; i += 1) {
      L.push([]); U.push([]);
      for (j = 0; j < n; j += 1) { L[i].push(i === j ? R1 : (j < i ? A[i][j] : R0)); U[i].push(j >= i ? A[i][j] : R0); }
    }
    var det = R(BigInt(sign));
    pivots.forEach(function (v) { det = Rmul(det, v); });
    var tiles = {
      luiPerm: 'π = ' + pi.map(function (x) { return x + 1; }).join(', '),
      luiPivots: pivots.map(itaQ).join(', '), luiL: luiRows(L), luiU: luiRows(U), luiDet: itaQ(det)
    };
    if (inst.b.length) {
      /* LUP-SOLVE: forward substitution Ly = Pb, back substitution Ux = y. */
      var y = [], x = [];
      for (i = 0; i < n; i += 1) {
        var s = inst.b[pi[i]];
        for (j = 0; j < i; j += 1) s = Rsub(s, Rmul(L[i][j], y[j]));
        y.push(s);
      }
      for (i = n - 1; i >= 0; i -= 1) {
        var s2 = y[i];
        for (j = i + 1; j < n; j += 1) s2 = Rsub(s2, Rmul(U[i][j], x[j]));
        x[i] = Rdiv(s2, U[i][i]);
      }
      var ok = orig.every(function (row, r) {
        var acc = R0;
        row.forEach(function (v, c) { acc = Radd(acc, Rmul(v, x[c])); });
        return Requ(acc, inst.b[r]);
      });
      tiles.luiX = 'x = ' + x.map(itaQ).join(', ');
      tiles.luiCheck = ok ? 'yes: A·x = b exactly' : 'no';
    } else {
      tiles.luiX = EA_DASH + ' (no b given)';
      tiles.luiCheck = EA_DASH;
    }
    return {
      tiles: tiles,
      status: 'PA = LU with L unit lower-triangular and U upper-triangular; π lists, for each row of PA, the row of A it came from. '
        + 'Every entry is an exact fraction, so nothing is lost to rounding: a pivot is chosen by size, as the book does for numerical stability, '
        + 'though here it changes no figure\'s accuracy. det A is the product of the pivots' + (sign < 0
          ? ', negated: the permutation is odd (an odd number of row swaps).'
          : ', unchanged: the permutation is even (an even number of row swaps).'),
      table: { caption: 'Elimination, column by column', head: ['column', 'pivot from', 'pivot', 'multipliers below it'], rows: steps }
    };
  };
"""


def _check_lup(inst, fixed):
    count = len(inst["matrix"])
    n = next((k for k in range(1, 6) if k * k == count), None)
    if n is None:
        raise ValueError("The matrix has %d entries; a square matrix has 1, 4, 9, 16 or 25" % count)
    if inst["b"] and len(inst["b"]) != n:
        raise ValueError("b has %d entries and the matrix %d rows; give b with %d entries, or none" % (len(inst["b"]), n, n))
    A = [list(inst["matrix"][i * n:(i + 1) * n]) for i in range(n)]
    for k in range(n):
        p = max(range(k, n), key=lambda i: (abs(A[i][k]), -i))
        if A[p][k] == 0:
            raise ValueError("The matrix is singular: column %d has no nonzero pivot on or below the diagonal" % (k + 1))
        A[k], A[p] = A[p], A[k]
        for i in range(k + 1, n):
            A[i][k] = A[i][k] / A[k][k]
            for j in range(k + 1, n):
                A[i][j] -= A[i][k] * A[k][j]


# ---------------------------------------------------------------------------
# fft (fti): multiplying polynomials, schoolbook against the FFT
# ---------------------------------------------------------------------------

FTI_JS = r"""
  var FTI_VIEW = {};
  function ftiCompute(view, inst, opts) { return eaRun(FTI_VIEW[view], inst, opts); }
"""

FTI_VIEW_JS = {}

FTI_VIEW_JS["multiply"] = r"""
  /* The iterative FFT (CLRS 30.3) in floating point: re and im arrays,
     length a power of 2; inverse divides by n. Returns the butterflies done. */
  function ftiFft(re, im, invert) {
    var n = re.length, i, j, len, bf = 0;
    for (i = 1, j = 0; i < n; i += 1) {
      var bit = n >> 1;
      for (; j & bit; bit >>= 1) j ^= bit;
      j ^= bit;
      if (i < j) { var t = re[i]; re[i] = re[j]; re[j] = t; t = im[i]; im[i] = im[j]; im[j] = t; }
    }
    for (len = 2; len <= n; len <<= 1) {
      var ang = 2 * Math.PI / len * (invert ? -1 : 1);
      for (i = 0; i < n; i += len) {
        for (j = 0; j < len / 2; j += 1) {
          var wr = Math.cos(ang * j), wi = Math.sin(ang * j);
          var ur = re[i + j], ui = im[i + j];
          var xr = re[i + j + len / 2] * wr - im[i + j + len / 2] * wi, xi = re[i + j + len / 2] * wi + im[i + j + len / 2] * wr;
          re[i + j] = ur + xr; im[i + j] = ui + xi; re[i + j + len / 2] = ur - xr; im[i + j + len / 2] = ui - xi;
          bf += 1;
        }
      }
    }
    if (invert) for (i = 0; i < n; i += 1) { re[i] /= n; im[i] /= n; }
    return bf;
  }
  /* A coefficient list: no thousands grouping, so the only commas are the
     ones between coefficients (1000000, −1999999, 3). */
  function ftiList(a) {
    return a.map(function (c) { return (c < 0n ? EA_MINUS : '') + String(c < 0n ? -c : c); }).join(', ');
  }
  FTI_VIEW.multiply = function (inst) {
    var a = inst.a.map(function (r) { return r.n; }), b = inst.b.map(function (r) { return r.n; });
    var deg = a.length + b.length - 1, n = 1, i, j;
    while (n < deg) n <<= 1;
    var school = [];
    for (i = 0; i < deg; i += 1) school.push(0n);
    for (i = 0; i < a.length; i += 1) for (j = 0; j < b.length; j += 1) school[i + j] += a[i] * b[j];
    var ar = [], ai = [], br = [], bi = [];
    for (i = 0; i < n; i += 1) {
      ar.push(i < a.length ? Number(a[i]) : 0); ai.push(0); br.push(i < b.length ? Number(b[i]) : 0); bi.push(0);
    }
    var bf = ftiFft(ar, ai, false) + ftiFft(br, bi, false);
    for (i = 0; i < n; i += 1) { var r = ar[i] * br[i] - ai[i] * bi[i], m = ar[i] * bi[i] + ai[i] * br[i]; ar[i] = r; ai[i] = m; }
    bf += ftiFft(ar, ai, true);
    var rounded = [], err = 0;
    for (i = 0; i < n; i += 1) {
      var q = Math.round(ar[i]);
      err = Math.max(err, Math.abs(ar[i] - q), Math.abs(ai[i]));
      rounded.push(BigInt(q === 0 ? 0 : q));
    }
    var agree = school.every(function (c, k) { return c === rounded[k]; }) && rounded.slice(deg).every(function (c) { return c === 0n; });
    var lg = 0;
    while ((1 << lg) < n) lg += 1;
    var rows = [];
    for (i = 0; i < n; i += 1) {
      rows.push([String(i), i < deg ? eaInt(school[i]) : '0', ar[i].toFixed(6).replace('-', EA_MINUS), eaInt(rounded[i])]);
    }
    return {
      tiles: {
        ftiN: eaInt(n) + ' (product degree ' + (deg - 1) + ')',
        ftiSchool: ftiList(school), ftiSchoolMults: eaInt(a.length * b.length) + ' (' + a.length + ' × ' + b.length + ')',
        ftiFft: ftiList(rounded.slice(0, deg)),
        ftiButterflies: eaInt(bf) + ' (3 transforms × (n/2) lg n = 3 × ' + eaInt(n / 2 * lg) + '), and ' + eaInt(n) + ' pointwise products',
        ftiAgree: agree ? 'yes' : 'no',
        ftiError: err < 1e-9 ? 'below 10^−9' : err.toExponential(1).replace('e', ' × 10^').replace('-', EA_MINUS)
      },
      status: 'Coefficients are listed from the constant term up. The FFT works in floating point: the roots of unity e^(2πik/n) are irrational, '
        + 'so each value is a double (about 16 significant digits) and the product comes back near, not on, the integers. '
        + 'The lab rounds each coefficient to the nearest integer and compares it with the schoolbook product, which is exact. '
        + 'A butterfly is one multiplication by a power of ω and one add and one subtract.',
      table: { caption: 'Each coefficient of the product', head: ['power of x', 'schoolbook', 'FFT before rounding', 'FFT rounded'], rows: rows }
    };
  };
"""


# ---------------------------------------------------------------------------
# Specs: every view's fields, tiles, check, rules
# ---------------------------------------------------------------------------

def _list(what, each, lo, hi, things, area=False, rows=2):
    f = {"kind": "list", "what": what, "control": "area" if area else "text", "lo": lo, "hi": hi,
         "things": things, "each": each}
    if area:
        f["rows"] = rows
    return f


_SPEED = ea.num(gt=0, hi=10 ** 15)
_COST = ea.num(gt=0)

GROWTH = {
    "prefix": "gri", "fn": "griCompute", "title": "Orders of growth", "js": GRI_JS,
    "views": {
        "race": {
            "fields": [("fnA", ea.choice("Program A's cost (instructions)", *RACE_FNS), None),
                       ("costA", ea.field("A's constant (instructions = constant × cost)", _COST), None),
                       ("speedA", ea.field("Machine A's speed (instructions a second)", _SPEED), None),
                       ("fnB", ea.choice("Program B's cost (instructions)", *RACE_FNS), None),
                       ("costB", ea.field("B's constant", _COST), None),
                       ("speedB", ea.field("Machine B's speed (instructions a second)", _SPEED), None),
                       ("n", ea.field("Input size n", ea.whole(1, 10 ** 12)), None)],
            "tiles": [("Where the better order of growth wins for good", "griCross"),
                      ("A's time at n", "griTimeA"), ("B's time at n", "griTimeB"), ("Faster at n", "griFaster")],
            "check": _check_race, "subtitle": "two programs on two machines",
            "rules": "Each program's time is its constant × its cost function at n, divided by its machine's speed, "
                     "in seconds. The crossover is the least n from which the program with the slower-growing cost is "
                     "strictly faster at every larger n: n = 1 to 64 are tried one by one, and past 64 (where the ratio "
                     "of the two functions only grows) it is found by bisection up to 10^15, or 4,096 when a program "
                     "costs 2^n. lg n is irrational unless n is a power of 2: times with lg n in them print rounded, "
                     "and every comparison is decided exactly.",
            "js": GRI_VIEW_JS["race"],
        },
        "bounds": {
            "fields": [("f", _menu_term("f(n) (coefficient, function; up to 4 terms)"), None),
                       ("g", _menu_term("g(n) (coefficient, function; up to 4 terms)"), None),
                       ("relation", ea.choice("Claim: f(n) = ? (g(n))", "O", "Omega", "Theta"), None),
                       ("c1", ea.field("c₁, the lower constant (Ω and Θ)", ea.num(gt=0)), "1"),
                       ("c2", ea.field("c₂, the upper constant (O and Θ)", ea.num(gt=0)), "1"),
                       ("n0", ea.field("n₀", ea.whole(1, 10 ** 6)), None)],
            "tiles": [("Witness holds from n₀ to n₀ + 10,000", "griHolds"), ("First n where it fails", "griFirstFail"),
                      ("At n₀", "griAtN0"), ("Order of growth (by the leading terms)", "griOrder"),
                      ("The claim, for some witness", "griClaim")],
            "check": _check_bounds, "subtitle": "checking a claimed witness c and n₀",
            "rules": "O: 0 ≤ f(n) ≤ c₂·g(n); Ω: 0 ≤ c₁·g(n) ≤ f(n); Θ: both, at every n from n₀ to n₀ + 10,000, "
                     "decided exactly (lg n included). The menu, slowest-growing first: 1, lg* n, lg n, n, n lg n, n^2, "
                     "n^3, F(n) (the Fibonacci numbers, F(0) = 0, F(1) = 1), 2^n, n!; each is o() of the next, so the "
                     "order-of-growth tile compares the leading terms. With F(n), 2^n or n! in f or g, n₀ is at most 1,000.",
            "js": GRI_VIEW_JS["bounds"],
        },
    },
}

SORTING = {
    "prefix": "sti", "fn": "stiCompute", "title": "Sorting, counted", "js": STI_JS,
    "views": {
        "insertion": {
            "fields": [("list", _array("Array A (whole numbers, up to 40)"), None)],
            "tiles": [("Key comparisons", "stiComparisons"), ("Shifts", "stiShifts"),
                      ("Loop invariant", "stiInvariant"), ("Sorted", "stiSorted")],
            "check": None, "subtitle": "INSERTION-SORT pass by pass, with its loop invariant",
            "rules": "Pass j takes key = A[j] and shifts each larger element of A[1..j − 1] one place right. A key "
                     "comparison is one test A[i] > key; when i reaches 0 the loop stops without one. The invariant "
                     "is checked at the start of each pass and once more at j = n + 1.",
            "js": STI_VIEW_JS["insertion"],
        },
        "cost": {
            "fields": [("list", _array("Array A (whole numbers, up to 40)"), None)],
            "tiles": [("t_j for j = 2 to n", "stiTj"), ("Σ t_j", "stiSumTj"), ("Key comparisons", "stiComparisons"),
                      ("Shifts (= inversions)", "stiShifts"), ("Best-case comparisons", "stiBest"),
                      ("Worst-case comparisons", "stiWorst"), ("Lines executed, every c_i = 1", "stiLines")],
            "check": None, "subtitle": "the line-cost sum with t_j",
            "rules": "t_j is the number of times the while-loop test runs in pass j: once for each shift, and once "
                     "more when it fails. Lines executed: n + 3(n − 1) + Σt_j + 2Σ(t_j − 1), the book's line-cost "
                     "sum with every c_i = 1 (the comment line costs 0).",
            "js": STI_VIEW_JS["cost"],
        },
        "merge": {
            "fields": [("list", _array("Array A (whole numbers, up to 40)"), None)],
            "tiles": [("Merge levels", "stiLevels"), ("Comparisons by level", "stiPerLevel"),
                      ("Comparisons in all", "stiMergeTotal"), ("Worst case for this n", "stiMergeBound"),
                      ("Comparisons with sentinels", "stiSentinel"), ("Sorted", "stiSorted")],
            "check": None, "subtitle": "MERGE-SORT's comparisons, level by level",
            "rules": "MERGE-SORT splits A[p..r] at q = ⌊(p + r)/2⌋. A merge compares the fronts of its two halves "
                     "and stops comparing when one runs out (equal keys take the left first). Level 1 is the final "
                     "merge. The sentinel count is what CLRS's MERGE, with ∞ at the end of each half, does: one "
                     "comparison an element merged.",
            "js": STI_VIEW_JS["merge"],
        },
    },
}

_RCI_FIELDS = [("a", ea.field("a (subproblems)", ea.whole(1, 1000)), None),
               ("b", ea.field("b (each of size n/b)", ea.whole(2, 1000)), None),
               ("c", ea.field("c in f(n) = c·n^k·lg^p n", ea.num(gt=0)), "1"),
               ("k", ea.field("k (at most 8; b^k must be whole)", ea.num(lo=0, hi=8)), None),
               ("p", ea.field("p (−3 to 3; p ≠ 0 needs b a power of 2)", ea.whole(-3, 3)), "0"),
               ("t1", ea.field("T(1)", ea.num(lo=0)), "1"),
               ("j", ea.field("Largest j (n = b^j)", ea.whole(1, 30)), None)]

_RCI_RULES = ("T(1) is given and T(b^j) = a·T(b^(j − 1)) + f(b^j), exactly, with lg n = j·lg b. The case compares "
              "f(n) = c·n^k·lg^p n with n^(log_b a) by comparing the whole numbers b^k and a: smaller is case 1, "
              "larger case 3 (its regularity condition holds with c = a/b^k when p ≥ 0), equal with p = 0 case 2, "
              "and equal with p ≠ 0 falls in a gap the master theorem leaves.")

RECURRENCE = {
    "prefix": "rci", "fn": "rciCompute", "title": "Recurrences", "js": RCI_JS,
    "views": {
        "master": {
            "fields": _RCI_FIELDS,
            "tiles": [("n^(log_b a)", "rciCritical"), ("Master method", "rciCase"), ("Solution", "rciSolution"),
                      ("T(n) at the largest n", "rciLast"), ("T(n) over the predicted growth there", "rciRatio")],
            "check": _check_recurrence, "subtitle": "the exact T(n) beside the master method",
            "rules": _RCI_RULES + " The ratio divides T(n) by n^(log_b a) in case 1, n^(log_b a)·log_b n in case 2, "
                                  "f(n) in case 3, and n^(log_b a)·log_b^(p + 1) n in the gap with p > 0.",
            "js": RCI_VIEW_JS["master"],
        },
        "tree": {
            "fields": _RCI_FIELDS,
            "tiles": [("Level sums, root first", "rciLevelSums"), ("Leaves", "rciLeaves"),
                      ("Sum of the tree", "rciTreeTotal"), ("T(n) by the recurrence", "rciLast"),
                      ("From level to level", "rciTrend"), ("Master method", "rciCase")],
            "check": _check_recurrence, "subtitle": "the recursion tree, level by level",
            "rules": _RCI_RULES + " The tree is drawn at the largest n: level i has a^i nodes of size n/b^i.",
            "js": RCI_VIEW_JS["tree"],
        },
    },
}

MAXSUB = {
    "prefix": "msi", "fn": "msiCompute", "title": "The maximum subarray", "js": MSI_JS,
    "views": {
        "compare": {
            "fields": [("list", _array("Array A (whole numbers, up to 60)", hi=60), None)],
            "tiles": [("Brute force", "msiBrute"), ("Divide-and-conquer", "msiDc"), ("One pass", "msiLinear"),
                      ("Brute force, steps", "msiBruteSteps"), ("Divide-and-conquer, steps", "msiDcSteps"),
                      ("One pass, steps", "msiLinearSteps"), ("Do the three agree", "msiAgree")],
            "check": None, "subtitle": "brute force, divide-and-conquer and one pass",
            "rules": "Brute force: a step is one addition to a running sum, n(n + 1)/2 of them; the first best "
                     "subarray found is kept. Divide-and-conquer: FIND-MAXIMUM-SUBARRAY with mid = ⌊(low + high)/2⌋, "
                     "preferring the left half, then the right, then the crossing subarray on a tie; its steps are "
                     "its calls and the elements its crossing scans add. One pass: a step is one element.",
            "js": MSI_VIEW_JS["compare"],
        },
    },
}

HIRING = {
    "prefix": "hri", "fn": "hriCompute", "title": "The hiring problem", "js": HRI_JS,
    "views": {
        "order": {
            "fields": [("order", _list("Candidates' ranks in interview order (a permutation of 1 to n; higher is better)",
                                       ea.whole(1, 40), 1, 40, "candidates"), None),
                       ("ci", ea.field("Cost of an interview, c_i", ea.num(lo=0)), "1"),
                       ("ch", ea.field("Cost of a hire, c_h", ea.num(lo=0)), "10")],
            "tiles": [("Hires on this order", "hriHires"), ("Cost on this order", "hriCost"),
                      ("Average hires over every order", "hriAverage"), ("H_n", "hriHarmonic"),
                      ("Average equals H_n", "hriAgree"), ("Expected cost, c_i·n + c_h·H_n", "hriExpectedCost")],
            "check": _check_order, "subtitle": "hires on one order, and on average",
            "rules": "HIRE-ASSISTANT interviews in the order given and hires each candidate better than all before; "
                     "the first is always hired. The average runs the same loop on every order of 1 to n (up to "
                     "n = 9, 362,880 orders) and divides, exactly.",
            "js": HRI_VIEW_JS["order"],
        },
    },
}

_P = ("p", ea.field("Processors P", ea.whole(1, 10 ** 6)), None)
_WSI_TILES = [("Work T₁", "wsiWork"), ("Span T∞", "wsiSpan"), ("Parallelism T₁/T∞", "wsiParallelism"),
              ("Greedy bound T₁/P + T∞", "wsiBound"), ("Lower bound max(T₁/P, T∞)", "wsiLower"),
              ("Critical path", "wsiCritical")]

WORKSPAN = {
    "prefix": "wsi", "fn": "wsiCompute", "title": "Work and span", "js": WSI_JS,
    "views": {
        "dag": {
            "fields": [("strands", ea.rec("Strands (strand, cost)", [("strand", ea.NAME), ("cost", ea.whole(1, 10 ** 6))],
                                          unique=True, hi=40), None),
                       ("edges", ea.rec("Edges (from, to)", [("from", ea.NAME), ("to", ea.NAME)], lo=0), ""), _P],
            "tiles": _WSI_TILES, "check": _check_dag, "subtitle": "a computation DAG's work and span",
            "rules": "Work is the sum of the strands' costs. Span is the largest total cost along a path of edges; "
                     "the critical path is that path (on a tie, the earlier strand in the list). The greedy bound "
                     "T₁/P + T∞ is Theorem 27.1's; max(T₁/P, T∞) is the work and span laws'.",
            "js": WSI_VIEW_JS["dag"],
        },
        "recurrence": {
            "fields": [("program", ea.choice("Program", "p-fib", "merge-sort"), None),
                       ("n", ea.field("n", ea.whole(0, 10 ** 6)), None), _P],
            "tiles": _WSI_TILES, "check": _check_wsrec, "subtitle": "P-FIB and MERGE-SORT′ as recurrences",
            "rules": "p-fib: P-FIB(n) with every strand costing 1, three strands a call for n ≥ 2 and one for n ≤ 1, "
                     "n at most 40. merge-sort: MERGE-SORT′, the halves spawned and the merge serial, a call on one "
                     "element costing 1 and a merge of m elements m. Work and span follow from the recurrences, "
                     "exactly.",
            "js": WSI_VIEW_JS["recurrence"],
        },
    },
}

LUP = {
    "prefix": "lui", "fn": "luiCompute", "title": "LUP decomposition", "js": LUI_JS,
    "views": {
        "decompose": {
            "fields": [("matrix", _list("Matrix A, row by row (1, 4, 9, 16 or 25 numbers)", ea.num(lo=-ea.LIMIT),
                                        1, 25, "entries", area=True, rows=3), None),
                       ("b", _list("b (optional; one number a row)", ea.num(lo=-ea.LIMIT), 0, 5, "entries"), "")],
            "tiles": [("Permutation", "luiPerm"), ("Pivots", "luiPivots"), ("L", "luiL"), ("U", "luiU"),
                      ("det A", "luiDet"), ("Solution", "luiX"), ("Checked", "luiCheck")],
            "check": _check_lup, "subtitle": "PA = LU, exactly, and LUP-SOLVE",
            "rules": "LUP-DECOMPOSITION: in column k the pivot is the entry of largest absolute value on or below "
                     "the diagonal (the first on a tie); its row is swapped up, the entries below are divided by it, "
                     "and the Schur complement updated. A column with no nonzero pivot is refused as singular. Every "
                     "entry is an exact fraction; matrices print row by row, rows separated by semicolons.",
            "js": LUI_VIEW_JS["decompose"],
        },
    },
}

FFT = {
    "prefix": "fti", "fn": "ftiCompute", "title": "Polynomials and the FFT", "js": FTI_JS,
    "views": {
        "multiply": {
            "fields": [("a", _list("A(x)'s coefficients, constant first (up to 16)", ea.whole(-10 ** 6, 10 ** 6), 1, 16,
                                   "coefficients"), None),
                       ("b", _list("B(x)'s coefficients, constant first (up to 16)", ea.whole(-10 ** 6, 10 ** 6), 1, 16,
                                   "coefficients"), None)],
            "tiles": [("n, padded to a power of 2", "ftiN"), ("Schoolbook product", "ftiSchool"),
                      ("Schoolbook multiplications", "ftiSchoolMults"), ("FFT product, rounded", "ftiFft"),
                      ("FFT butterflies", "ftiButterflies"), ("Agree", "ftiAgree"),
                      ("Largest distance from an integer before rounding", "ftiError")],
            "check": None, "subtitle": "the schoolbook product against evaluate, multiply, interpolate",
            "rules": "The schoolbook product multiplies every pair of coefficients, exactly. The FFT route pads both "
                     "to n, the least power of 2 at least the product's length, evaluates each at the n complex nth "
                     "roots of unity, multiplies pointwise and interpolates by the inverse FFT. It works in floating "
                     "point (doubles): the result is rounded to the nearest integer, and compared with the schoolbook "
                     "product. Coefficient lists print without thousands separators, so every comma separates two "
                     "coefficients. The distance tile is rounded and can differ between browsers in its last digit.",
            "js": FTI_VIEW_JS["multiply"],
        },
    },
}

SPECS = {"growth": GROWTH, "sorting": SORTING, "recurrence": RECURRENCE, "maxsub": MAXSUB, "hiring": HIRING,
         "workspan": WORKSPAN, "lup": LUP, "fft": FFT}
MODES_A = tuple(SPECS)


# ---------------------------------------------------------------------------
# Building a lab (both families) and the entry point
# ---------------------------------------------------------------------------

def family_intro():
    return (ea.FAMILY[1] + " The lab runs the algorithm on the instance and counts; a count on one instance is "
            "evidence about that instance, and only the book's proof bounds every input.")


def _no_options(cfg, kit, tiles):
    return {}, [], tiles


def mode_lab(cfg, mode, spec):
    """One itakit mode as a Lab, from its spec dict (module docstring; kit-contract.md section 2)."""
    views = spec["views"]
    order = tuple(views)
    view = cfg.get("view", order[0])
    if view not in views:
        raise ValueError("%s/%s: unknown view %r; the views are %s" % (KIT, mode, view, ", ".join(order)))
    kit = "%s/%s/%s" % (KIT, mode, view)
    v = views[view]
    fixed, keys, tiles = v.get("options", _no_options)(cfg, kit, v["tiles"])
    for _label, cid in tiles:
        if not cid.startswith(spec["prefix"]):
            raise ValueError("%s: tile id %r does not begin with the prefix %r" % (kit, cid, spec["prefix"]))
    return ea.build_lab(cfg, kit=kit, prefix=spec["prefix"], view=view, fields=v["fields"], tiles=tiles,
                        fn=spec["fn"], js=ITA_CORE_JS + spec["js"] + v["js"], fixed=fixed, title=spec["title"],
                        subtitle=v["subtitle"], family=v.get("family", 1), intro=family_intro(), rules=v["rules"],
                        extra_keys=keys, check=v["check"])


def itakit_lab(cfg):
    """The Introduction to Algorithms kit: cfg["mode"] chooses the mode, cfg["view"] the view."""
    cfg = cfg or {}
    mode = cfg.get("mode")
    if mode in SPECS:
        return mode_lab(cfg, mode, SPECS[mode])
    family_b = itakit_b.MODES
    if mode in family_b:
        return family_b[mode](cfg)
    raise ValueError("itakit_lab: unknown mode %r; the modes are %s"
                     % (mode, ", ".join(MODES_A + tuple(m for m in family_b if m not in SPECS))))


# Family B. Imported last, after mode_lab exists, so that itakit_b may import
# from this module at its top whichever module loads first.
from . import itakit_b  # noqa: E402

__all__ = ["itakit_lab", "mode_lab", "family_intro", "ITA_CORE_JS", "SPECS", "MODES_A", "KIT"]
