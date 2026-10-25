"""cckit_b -- the seven modes of the Code Complete kit that do not read code.

Specified in docs/code-complete/PLAN.md section D.1; the entry point and the
`code` mode are in cckit.py, the shared printing, parsing and wiring in
cckit_core.py. Each mode has one base block (its <xx>Compute and the helpers
its views share) and one block per view; a page ships the base block and its
own view's block only.

  deps     (dg)  coupling, ripple, tree, shared, integrate   family 2
  cond     (cd)  truth, range, barricade                     family 2
  search   (se)  chain, stairs, bisect                       family 2
  run      (lp)  loop, nested, recursion, arith (tiles nu)   family 2
  defects  (df)  cost, removal, pipeline                     family 3
  profile  (pf)  shares, speedup                             family 3
  project  (pj)  language, scale, effort, breakeven          family 3

No figure from the book is a constant here (D.0, D.2): the cost table, the
rates, ratios, densities, productivities and multipliers arrive in the cfg or
the preset.
"""

import re
from fractions import Fraction

from . import cckit_core as cc

KIT = "cckit"

INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

# ---------------------------------------------------------------------------
# deps
# ---------------------------------------------------------------------------

DG_JS = r"""
  /* deps: a graph stated as records. Ties in a "largest" tile go to the
     alphabetically first name; the banner names every tied one. */
  var DG_VIEW = {};
  function dgCompute(view, inst, opts) { return DG_VIEW[view](inst, opts || {}); }
  function dgSelf(recs, a, b, what) {
    for (var i = 0; i < recs.length; i += 1) {
      if (recs[i][a] === recs[i][b]) return 'Entry ' + (i + 1) + ' of ' + what + ' names ' + recs[i][a] + ' on both sides';
    }
    return null;
  }
  function dgNamesOf(recs, keys) {
    var seen = {}, out = [];
    recs.forEach(function (r) {
      keys.forEach(function (k) { if (!seen[r[k]]) { seen[r[k]] = true; out.push(r[k]); } });
    });
    return ccSort(out);
  }
  function dgTop(count, names) {
    var best = null;
    names.forEach(function (x) { if (best === null || count[x] > count[best]) best = x; });
    return { name: best, v: count[best], tied: names.filter(function (x) { return count[x] === count[best]; }) };
  }
  function dgTie(word, t) {
    return t.tied.length > 1 ? ' The largest ' + word + ', ' + t.v + ', is shared by ' + t.tied.join(', ')
      + '; the tile shows the alphabetically first.' : '';
  }
"""

DG_VIEW_JS = {}

DG_VIEW_JS["coupling"] = r"""
  DG_VIEW.coupling = function (inst) {
    var bad = dgSelf(inst.edges, 'user', 'used', 'the uses');
    if (bad) return { refuse: bad };
    var seen = {}, E = [], conn = {}, nconn = 0, fo = {}, fi = {};
    inst.edges.forEach(function (e) {
      var k = e.user + ' ' + e.used;
      if (!seen[k]) { seen[k] = true; E.push(e); }
    });
    var mods = dgNamesOf(E, ['user', 'used']), n = mods.length, pairs = n * (n - 1) / 2;
    mods.forEach(function (m) { fo[m] = 0; fi[m] = 0; });
    E.forEach(function (e) {
      var u = ccSort([e.user, e.used]).join(' ');
      if (!conn[u]) { conn[u] = true; nconn += 1; }
      fo[e.user] += 1;
      fi[e.used] += 1;
    });
    var o = dgTop(fo, mods), i = dgTop(fi, mods);
    return {
      tiles: { dgModules: ccInt(n), dgEdges: ccInt(E.length), dgPairs: ccInt(pairs),
        dgConnected: ccPct(R(nconn, pairs)), dgFanOut: o.name + ' ' + ccInt(o.v), dgFanIn: i.name + ' ' + ccInt(i.v) },
      status: ccInt(nconn) + ' of the ' + ccPlural(pairs, 'pair', 'pairs') + ' of modules have a use in either direction.'
        + dgTie('fan-out', o) + dgTie('fan-in', i),
      table: { caption: 'Each module', head: ['Module', 'Uses (fan-out)', 'Used by (fan-in)'],
        rows: mods.map(function (m) { return [m, ccInt(fo[m]), ccInt(fi[m])]; }) }
    };
  };
"""

DG_VIEW_JS["ripple"] = r"""
  DG_VIEW.ripple = function (inst) {
    var bad = dgSelf(inst.edges, 'dependent', 'dependency', 'the dependencies');
    if (bad) return { refuse: bad };
    var names = dgNamesOf(inst.edges, ['dependent', 'dependency']), ch = inst.changed;
    if (names.indexOf(ch) < 0) return { refuse: 'No entry names ' + ch + ', so this graph cannot say what depends on it' };
    var direct = {}, dist = {}, queue = [ch];
    dist[ch] = 0;
    inst.edges.forEach(function (e) { if (e.dependency === ch) direct[e.dependent] = true; });
    while (queue.length) {
      var x = queue.shift();
      inst.edges.forEach(function (e) {
        if (e.dependency === x && dist[e.dependent] === undefined) { dist[e.dependent] = dist[x] + 1; queue.push(e.dependent); }
      });
    }
    var d = ccSort(Object.keys(direct)), all = ccSort(Object.keys(dist).filter(function (k) { return k !== ch; }));
    var rows = all.slice().sort(function (a, b) { return dist[a] - dist[b]; }).map(function (k) { return [k, ccInt(dist[k])]; });
    return {
      tiles: { dgDirect: ccCount(d), dgAffected: ccCount(all) },
      status: 'A change to ' + ch + ' reaches ' + ccPlural(d.length, 'name', 'names') + ' directly and '
        + ccPlural(all.length, 'name', 'names') + ' in all, following each edge from a dependency to what depends on it.',
      table: { caption: 'What a change to ' + ch + ' reaches', head: ['Name', 'Edges from the change'], rows: rows }
    };
  };
"""

DG_VIEW_JS["tree"] = r"""
  DG_VIEW.tree = function (inst) {
    var bad = dgSelf(inst.edges, 'child', 'parent', 'the classes');
    if (bad) return { refuse: bad };
    var parent = {}, kids = {}, i, k;
    for (i = 0; i < inst.edges.length; i += 1) {
      var e = inst.edges[i];
      if (parent[e.child] !== undefined && parent[e.child] !== e.parent) {
        return { refuse: e.child + ' has two parents, ' + parent[e.child] + ' and ' + e.parent + '; this view reads single inheritance' };
      }
      parent[e.child] = e.parent;
    }
    var classes = dgNamesOf(inst.edges, ['child', 'parent']), depth = {};
    classes.forEach(function (c) { kids[c] = 0; });
    Object.keys(parent).forEach(function (c) { kids[parent[c]] += 1; });
    for (i = 0; i < classes.length; i += 1) {
      var c = classes[i], d = 1, at = c, path = [c];
      while (parent[at] !== undefined) {
        at = parent[at];
        d += 1;
        if (at === c || d > classes.length) {
          return { refuse: c + ' is its own ancestor (' + path.concat([at]).join(' → ') + '); an inheritance tree has no cycle' };
        }
        path.push(at);
      }
      depth[c] = d;
    }
    var top = dgTop(depth, classes), leaves = classes.filter(function (c) { return kids[c] === 0; });
    return {
      tiles: { dgDepth: ccInt(top.v), dgDeepest: top.name, dgClasses: ccInt(classes.length), dgLeaves: ccInt(leaves.length) },
      status: 'A root is at depth 1. The deepest ' + (top.tied.length > 1 ? 'classes, at depth ' + top.v + ', are '
        + top.tied.join(', ') + '; the tile shows the alphabetically first.' : 'class is ' + top.name + ', at depth ' + top.v + '.'),
      table: { caption: 'Each class', head: ['Class', 'Parent', 'Depth', 'Children'],
        rows: classes.map(function (c) { return [c, parent[c] === undefined ? 'none (a root)' : parent[c], ccInt(depth[c]), ccInt(kids[c])]; }) }
    };
  };
"""

DG_VIEW_JS["shared"] = r"""
  DG_VIEW.shared = function (inst) {
    var g = {}, own = {}, i, j;
    inst.uses.forEach(function (u) {
      if (!g[u.global]) g[u.global] = {};
      var a = g[u.global][u.routine] || { r: false, w: false };
      if (u.access.indexOf('r') >= 0) a.r = true;
      if (u.access.indexOf('w') >= 0) a.w = true;
      g[u.global][u.routine] = a;
    });
    var globals = ccSort(Object.keys(g)), routines = dgNamesOf(inst.uses, ['routine']);
    for (i = 0; i < inst.owners.length; i += 1) {
      if (!g[inst.owners[i].a]) return { refuse: 'The owners name ' + inst.owners[i].a + ', which no entry uses' };
      own[inst.owners[i].a] = inst.owners[i].b;
    }
    var pairs = {}, npairs = 0, count = {}, direct = 0;
    globals.forEach(function (v) {
      var users = ccSort(Object.keys(g[v]));
      count[v] = users.length;
      direct += own[v] !== undefined ? 1 : users.length;
      for (i = 0; i < users.length; i += 1) {
        for (j = i + 1; j < users.length; j += 1) {
          var key = users[i] + ' ' + users[j];
          if ((g[v][users[i]].w || g[v][users[j]].w) && !pairs[key]) { pairs[key] = true; npairs += 1; }
        }
      }
    });
    var n = routines.length, possible = n * (n - 1) / 2, top = dgTop(count, globals);
    function who(v, letter) { return ccSort(Object.keys(g[v]).filter(function (r) { return g[v][r][letter]; })); }
    var writers = globals.map(function (v) { return v + ': ' + (own[v] !== undefined ? own[v] : ccNames(who(v, 'w'))); }).join('; ');
    return {
      tiles: { dgGlobals: ccInt(globals.length), dgRoutines: ccInt(n), dgCoupled: ccInt(npairs),
        dgMostShared: top.name + ', ' + ccPlural(top.v, 'routine', 'routines'), dgDirectAccess: ccInt(direct), dgWriters: writers },
      status: ccInt(npairs) + ' of the ' + ccPlural(possible, 'possible pair', 'possible pairs')
        + ' of routines touch a common global that at least one of them writes.'
        + (inst.owners.length ? ' Access routines move the coupling behind one name; they do not remove it, so the coupled pairs stay '
          + ccInt(npairs) + ' (section 13.3).' : '')
        + (top.tied.length > 1 ? ' The most shared globals, used by ' + top.v + ' routines each, are ' + top.tied.join(', ')
          + '; the tile shows the alphabetically first.' : ''),
      table: { caption: 'Each global', head: ['Global', 'Read by', 'Written by', 'Access routine'],
        rows: globals.map(function (v) { return [v, ccNames(who(v, 'r')), ccNames(who(v, 'w')), own[v] === undefined ? 'none' : own[v]]; }) }
    };
  };
"""

DG_VIEW_JS["integrate"] = r"""
  DG_VIEW.integrate = function (inst) {
    var bad = dgSelf(inst.edges, 'caller', 'callee', 'the calls');
    if (bad) return { refuse: bad };
    var names = dgNamesOf(inst.edges, ['caller', 'callee']);
    var missing = names.filter(function (x) { return inst.order.indexOf(x) < 0; });
    if (missing.length) return { refuse: 'The order leaves out ' + missing.join(', ') + '; it names every component once' };
    var extra = inst.order.filter(function (x) { return names.indexOf(x) < 0; });
    if (extra.length) return { refuse: 'The order names ' + extra.join(', ') + ', which no call names' };
    var done = {}, stubs = {}, drivers = {}, rows = [];
    inst.order.forEach(function (m, step) {
      done[m] = true;
      var callers = inst.edges.filter(function (e) { return e.callee === m; });
      var driver = callers.length > 0 && !callers.some(function (e) { return done[e.caller] && e.caller !== m; });
      if (driver) drivers[m] = true;
      var now = {};
      inst.edges.forEach(function (e) { if (done[e.caller] && !done[e.callee]) { stubs[e.callee] = true; now[e.callee] = true; } });
      rows.push([ccInt(step + 1), m, driver ? 'yes' : 'no', ccNames(ccSort(Object.keys(now)))]);
    });
    var s = ccSort(Object.keys(stubs)), d = ccSort(Object.keys(drivers));
    return {
      tiles: { dgStubs: ccCount(s), dgDrivers: ccCount(d) },
      status: 'This order needs ' + ccPlural(s.length, 'stub', 'stubs') + ' and ' + ccPlural(d.length, 'driver', 'drivers')
        + '. A stub stands in for a component that an integrated one calls before it is itself integrated; a driver calls a'
        + ' component that has callers, none of them integrated when it is.',
      table: { caption: 'The order, step by step', head: ['Step', 'Component', 'Needs a driver', 'Stubbed after this step'], rows: rows }
    };
  };
"""

_NAME = {"kind": "name"}


def _edges(what, a, b, lo=1, hi=60):
    return {"kind": "rec", "what": what, "sub": [[a, _NAME], [b, _NAME]], "lo": lo, "hi": hi}


DG_VIEWS = {
    "coupling": ([("edges", _edges("Uses (a, b: a uses b; one pair per entry)", "user", "used"), None)],
                 [("Modules", "dgModules"), ("Distinct uses", "dgEdges"), ("Possible pairs", "dgPairs"),
                  ("Pairs connected either way", "dgConnected"), ("Largest fan-out", "dgFanOut"),
                  ("Largest fan-in", "dgFanIn")]),
    "ripple": ([("edges", _edges("Dependencies (a, b: a depends on b)", "dependent", "dependency"), None),
                ("changed", dict(_NAME, what="What changes"), None)],
               [("Depend on it directly", "dgDirect"), ("Reached in all", "dgAffected")]),
    "tree": ([("edges", _edges("Classes (child, parent)", "child", "parent", 1, 40), None)],
             [("Deepest level (a root is 1)", "dgDepth"), ("Deepest class", "dgDeepest"), ("Classes", "dgClasses"),
              ("Leaves", "dgLeaves")]),
    "shared": ([("uses", {"kind": "rec", "what": "Uses (routine, access r, w or rw, global)",
                          "sub": [["routine", _NAME], ["access", {"kind": "word", "words": ["r", "w", "rw"]}],
                                  ["global", _NAME]], "lo": 1, "hi": 60}, None),
                ("owners", {"kind": "pairs", "what": "Access routines (global=routine; optional)"}, "")],
               [("Globals", "dgGlobals"), ("Routines", "dgRoutines"), ("Coupled pairs of routines", "dgCoupled"),
                ("Most shared global", "dgMostShared"), ("Places that touch a global directly", "dgDirectAccess"),
                ("Who writes each global", "dgWriters")]),
    "integrate": ([("edges", _edges("Calls (caller, callee)", "caller", "callee"), None),
                   ("order", {"kind": "names", "lo": 1, "hi": 60, "what": "Integration order (space-separated)"}, None)],
                  [("Stubs needed", "dgStubs"), ("Drivers needed", "dgDrivers")]),
}

DG_SUBTITLES = {
    "coupling": "who uses whom, and how connected the modules are",
    "ripple": "what a change reaches",
    "tree": "depth and breadth of an inheritance tree",
    "shared": "routines coupled through global data",
    "integrate": "stubs and drivers for an integration order",
}

# ---------------------------------------------------------------------------
# cond
# ---------------------------------------------------------------------------

CD_JS = r"""
  /* cond: the kit's own parser for a Java condition. It builds a tree and
     evaluates the tree; it never evaluates text as script (D.2). */
  var CD_VIEW = {}, CD_MIN = -(2n ** 31n), CD_MAX = 2n ** 31n - 1n;
  function cdCompute(view, inst, opts) { return CD_VIEW[view](inst, opts || {}); }
  var CD_TOK = /\s*(?:(\d+)|([A-Za-z_][A-Za-z0-9_]*)|(&&|\|\||<=|>=|==|!=|[!()<>-]))/y;
  var CD_FLIP = { '<': '>', '<=': '>=', '>': '<', '>=': '<=', '==': '==', '!=': '!=' };
  /* cmp false: boolean variables; cmp true: comparisons of one integer
     variable with whole numbers. Throws a sentence naming `what`. */
  function cdParse(text, cmp, what) {
    var s = String(text).trim(), toks = [], pos = 0, k = 0, vars = [], lits = [], m;
    while (pos < s.length) {
      CD_TOK.lastIndex = pos;
      m = CD_TOK.exec(s);
      if (!m || CD_TOK.lastIndex === pos) throw new Error(what + ' has "' + s.slice(pos).trim().charAt(0) + '", which this lab cannot read');
      toks.push(m[1] !== undefined ? { k: 'n', v: m[1] } : (m[2] !== undefined ? { k: 'i', v: m[2] } : { k: 'o', v: m[3] }));
      pos = CD_TOK.lastIndex;
      if (/^\s*$/.test(s.slice(pos))) break;
    }
    function peek() { return k < toks.length ? toks[k] : { k: '', v: '' }; }
    function take() { var t = peek(); k += 1; return t; }
    function fail(why) { throw new Error(what + ' ' + why); }
    function name(v) { if (vars.indexOf(v) < 0) vars.push(v); }
    function operand() {
      var t = take();
      if (t.v === '-') {
        var u = take();
        if (u.k !== 'n') fail('has a minus sign that is not before a whole number');
        return { k: 'n', v: -BigInt(u.v) };
      }
      if (t.k === 'n') return { k: 'n', v: BigInt(t.v) };
      if (t.k === 'i' && t.v !== 'true' && t.v !== 'false') return t;
      fail(t.v === '' ? 'ends where a comparison needs a value' : 'has "' + t.v + '" where a variable or a whole number belongs');
    }
    function atom() {
      var t = peek();
      if (t.v === '(') {
        take();
        var x = disj();
        if (take().v !== ')') fail('has a parenthesis that does not close');
        return x;
      }
      if (t.v === 'true' || t.v === 'false') { take(); return { t: 'k', v: t.v === 'true' }; }
      if (cmp) {
        var a = operand(), op = take();
        if (!CD_FLIP[op.v]) fail('compares nothing: a range check compares the variable with a whole number using < <= > >= == or !=');
        var b = operand();
        if ((a.k === 'i') === (b.k === 'i')) fail('compares ' + (a.k === 'i' ? 'two variables' : 'two numbers') + '; each comparison is between the variable and a whole number');
        var x2 = a.k === 'i' ? { t: 'c', op: op.v, name: a.v, c: b.v } : { t: 'c', op: CD_FLIP[op.v], name: b.v, c: a.v };
        if (x2.c < CD_MIN || x2.c > CD_MAX) fail('compares with ' + ccInt(x2.c) + ', which is outside Java\'s int');
        name(x2.name);
        lits.push(x2.c);
        return x2;
      }
      if (t.k === 'i') { take(); name(t.v); return { t: 'v', name: t.v }; }
      fail(t.v === '' ? 'ends where a variable belongs' : 'has "' + t.v + '" where a variable belongs');
    }
    function neg() {
      if (peek().v === '!') {
        take();
        var n = peek().v;
        if (cmp && n !== '!' && n !== '(' && n !== 'true' && n !== 'false') fail('negates a number; put the comparison in parentheses');
        return { t: '!', a: neg() };
      }
      return atom();
    }
    function conj() { var x = neg(); while (peek().v === '&&') { take(); x = { t: '&', a: x, b: neg() }; } return x; }
    function disj() { var x = conj(); while (peek().v === '||') { take(); x = { t: '|', a: x, b: conj() }; } return x; }
    if (!toks.length) fail('is empty');
    var tree = disj();
    if (k !== toks.length) fail('has "' + peek().v + '" after the condition ends');
    return { tree: tree, vars: vars, lits: lits };
  }
  function cdEval(x, env) {
    switch (x.t) {
      case 'k': return x.v;
      case 'v': return env[x.name];
      case '!': return !cdEval(x.a, env);
      case '&': return cdEval(x.a, env) && cdEval(x.b, env);
      case '|': return cdEval(x.a, env) || cdEval(x.b, env);
    }
    var v = env[x.name], c = x.c;
    switch (x.op) {
      case '<': return v < c;
      case '<=': return v <= c;
      case '>': return v > c;
      case '>=': return v >= c;
      case '==': return v === c;
    }
    return v !== c;
  }
"""

CD_VIEW_JS = {}

CD_VIEW_JS["truth"] = r"""
  CD_VIEW.truth = function (inst) {
    var A, B;
    try { A = cdParse(inst.a, false, 'Condition A'); B = cdParse(inst.b, false, 'Condition B'); } catch (err) { return { refuse: err.message }; }
    var atoms = A.vars.slice();
    B.vars.forEach(function (v) { if (atoms.indexOf(v) < 0) atoms.push(v); });
    if (atoms.length > 5) return { refuse: 'The two conditions name ' + atoms.length + ' variables; this lab tabulates at most 5' };
    var n = atoms.length, rows = Math.pow(2, n), ta = 0, tb = 0, diff = 0, first = null, out = [];
    for (var r = 0; r < rows; r += 1) {
      var env = {}, cells = [];
      atoms.forEach(function (v, j) { env[v] = ((r >> (n - 1 - j)) & 1) === 0; cells.push(env[v] ? 'T' : 'F'); });
      var x = cdEval(A.tree, env), y = cdEval(B.tree, env);
      if (x) ta += 1;
      if (y) tb += 1;
      if (x !== y) {
        diff += 1;
        if (first === null) first = atoms.map(function (v) { return v + ' = ' + (env[v] ? 'T' : 'F'); }).join(', ');
      }
      out.push(cells.concat([x ? 'T' : 'F', y ? 'T' : 'F', x === y ? 'agree' : 'differ']));
    }
    return {
      tiles: { cdAtoms: ccInt(n), cdRows: ccInt(rows), cdTrueA: ccInt(ta), cdTrueB: ccInt(tb),
        cdEquivalent: diff ? 'no, on ' + diff + ' of ' + rows + ' rows' : 'yes', cdFirstDiff: first === null ? 'none' : first },
      status: diff ? 'The conditions differ on ' + diff + ' of the ' + rows + ' rows; the first is ' + first + '.'
        : 'The conditions agree on every one of the ' + ccPlural(rows, 'row', 'rows') + ', so they are equivalent.',
      table: { caption: 'Every row, T before F, the first variable most significant', head: atoms.concat(['A', 'B', 'A and B']), rows: out }
    };
  };
"""

CD_VIEW_JS["range"] = r"""
  function cdInterval(a, b) {
    if (a === CD_MIN && b === CD_MAX) return 'every int';
    if (a === b) return ccInt(a);
    if (b === CD_MAX) return ccInt(a) + ' and above';
    if (a === CD_MIN) return ccInt(b) + ' and below';
    return ccInt(a) + ' to ' + ccInt(b);
  }
  CD_VIEW.range = function (inst) {
    var P;
    try { P = cdParse(inst.cond, true, 'The check'); } catch (err) { return { refuse: err.message }; }
    if (P.vars.length > 1) return { refuse: 'The check names ' + P.vars.join(' and ') + '; this view reads a condition over one integer variable' };
    var lo = ccBigOf(inst.lo), hi = ccBigOf(inst.hi), valid = inst.means === 'valid', v = P.vars[0] || 'x';
    if (lo > hi) return { refuse: 'The valid range runs from ' + ccInt(lo) + ' to ' + ccInt(hi) + ', which is empty; the low end must not be above the high end' };
    function says(x) { var e = {}; e[v] = x; return cdEval(P.tree, e) === valid; }
    function inRange(x) { return lo <= x && x <= hi; }
    var seen = {}, pts = [];
    P.lits.concat([lo, hi]).forEach(function (c) {
      [c - 1n, c, c + 1n].forEach(function (p) { if (p >= CD_MIN && p <= CD_MAX && !seen[p]) { seen[p] = true; pts.push(p); } });
    });
    [CD_MIN, CD_MAX].forEach(function (p) { if (!seen[p]) { seen[p] = true; pts.push(p); } });
    pts.sort(function (a, b) { return a < b ? -1 : (a > b ? 1 : 0); });
    var bad = [];
    pts.forEach(function (p, i) {
      var spans = [[p, p]];
      if (i + 1 < pts.length && pts[i + 1] - p > 1n) spans.push([p + 1n, pts[i + 1] - 1n]);
      spans.forEach(function (s) {
        if (says(s[0]) !== inRange(s[0])) {
          if (bad.length && bad[bad.length - 1][1] === s[0] - 1n) bad[bad.length - 1][1] = s[1];
          else bad.push([s[0], s[1]]);
        }
      });
    });
    var tests = [], tseen = {};
    [lo - 1n, lo, lo + 1n, hi - 1n, hi, hi + 1n].forEach(function (t) {
      if (t >= CD_MIN && t <= CD_MAX && !tseen[t]) { tseen[t] = true; tests.push(t); }
    });
    tests.sort(function (a, b) { return a < b ? -1 : (a > b ? 1 : 0); });
    var exposed = tests.filter(function (t) { return says(t) !== inRange(t); });
    var word = function (b) { return b ? 'valid' : 'invalid'; };
    return {
      tiles: { cdDisagree: bad.length ? bad.map(function (s) { return cdInterval(s[0], s[1]); }).join(', ') : 'none',
        cdTests: tests.map(ccInt).join(', '), cdExposed: exposed.length ? exposed.map(ccInt).join(', ') : 'none' },
      status: (bad.length ? 'The check and the range ' + ccInt(lo) + ' to ' + ccInt(hi) + ' disagree on '
        + bad.map(function (s) { return cdInterval(s[0], s[1]); }).join(', ') + '; the boundary tests expose '
        + ccPlural(exposed.length, 'value', 'values') + ' of them.'
        : 'The check agrees with the range ' + ccInt(lo) + ' to ' + ccInt(hi) + ' on every int.')
        + ' A true check says the value is ' + word(valid) + '.',
      table: { caption: 'The boundary tests', head: ['Test value', 'The range says', 'The check says', 'Exposes a difference'],
        rows: tests.map(function (t) { return [ccInt(t), word(inRange(t)), word(says(t)), says(t) !== inRange(t) ? 'yes' : 'no']; }) }
    };
  };
"""

CD_VIEW_JS["barricade"] = r"""
  CD_VIEW.barricade = function (inst) {
    function names(side, handling) {
      return inst.values.filter(function (r) { return r.side === side && r.handling === handling; }).map(function (r) { return r.value; });
    }
    var ou = names('outside', 'none'), oa = names('outside', 'assert'), iu = names('inside', 'none'), iv = names('inside', 'validate');
    return {
      tiles: { cdValues: ccInt(inst.values.length), cdOutsideUnchecked: ccCount(ou), cdOutsideAsserted: ccCount(oa),
        cdInsideUnchecked: ccCount(iu), cdInsideValidated: ccCount(iv) },
      status: 'The chapter\'s rule (section 8.5): data outside the barricade is validated by error handling, and data inside'
        + ' may be asserted. These tiles apply that rule to the values the lesson states; they are not a verdict. Section 8.8'
        + ' leaves room for judgement, and validating inside is a cost, not a defect.',
      table: { caption: 'Each value', head: ['Value', 'Side of the barricade', 'Handling'],
        rows: inst.values.map(function (r) { return [r.value, r.side, r.handling]; }) }
    };
  };
"""

CD_VIEWS = {
    "truth": ([("a", {"kind": "cond", "rows": 3, "what": "Condition A (Java: names, !, &&, ||, parentheses)"}, None),
               ("b", {"kind": "cond", "rows": 3, "what": "Condition B"}, None)],
              [("Variables", "cdAtoms"), ("Rows", "cdRows"), ("Rows where A is true", "cdTrueA"),
               ("Rows where B is true", "cdTrueB"), ("Equivalent", "cdEquivalent"), ("First row that differs", "cdFirstDiff")]),
    "range": ([("cond", {"kind": "cond", "rows": 3, "what": "The check (Java, over one int variable)"}, None),
               ("lo", {"kind": "whole", "min": str(INT_MIN), "max": str(INT_MAX), "what": "Valid from"}, None),
               ("hi", {"kind": "whole", "min": str(INT_MIN), "max": str(INT_MAX), "what": "Valid to (inclusive)"}, None),
               ("means", {"kind": "word", "words": ["valid", "invalid"], "what": "A true check means (valid or invalid)"}, None)],
              [("Where check and range disagree", "cdDisagree"), ("Boundary tests", "cdTests"),
               ("Tests that expose a difference", "cdExposed")]),
    "barricade": ([("values", {"kind": "rec", "what": "Values (name, outside or inside, validate, assert or none)",
                               "sub": [["value", _NAME], ["side", {"kind": "word", "words": ["outside", "inside"]}],
                                       ["handling", {"kind": "word", "words": ["validate", "assert", "none"]}]],
                               "lo": 1, "hi": 20, "unique": True}, None)],
                  [("Values", "cdValues"), ("Outside, unchecked", "cdOutsideUnchecked"),
                   ("Outside, only asserted", "cdOutsideAsserted"), ("Inside, unchecked", "cdInsideUnchecked"),
                   ("Inside, validated", "cdInsideValidated")]),
}

CD_SUBTITLES = {
    "truth": "two conditions over every row of their truth table",
    "range": "a range check against the range it should check",
    "barricade": "which values are checked, and how, on each side",
}

# ---------------------------------------------------------------------------
# search
# ---------------------------------------------------------------------------

SE_JS = r"""
  /* search: tests counted along a chain, a staircase table and a bisection. */
  var SE_VIEW = {};
  function seCompute(view, inst, opts) { return SE_VIEW[view](inst, opts || {}); }
"""

SE_VIEW_JS = {}

SE_VIEW_JS["chain"] = r"""
  SE_VIEW.chain = function (inst) {
    var cs = inst.cases, n = cs.length, i;
    for (i = 0; i < n - 1; i += 1) {
      if (cs[i].case === 'else') return { refuse: 'else is entry ' + (i + 1) + ' of ' + n + '; the final else comes last' };
    }
    var hasElse = cs[n - 1].case === 'else', k = n - (hasElse ? 1 : 0);
    var total = ccSum(cs.map(function (c) { return c.frequency; }));
    if (Rzero(total)) return { refuse: 'The frequencies add up to 0; an expected number of tests needs a total above 0' };
    function tests(pos) { return hasElse && pos === n - 1 ? k : pos + 1; }
    function cost(order) {
      var s = R0;
      order.forEach(function (c, p) { s = Radd(s, Rmul(R(tests(p)), c.frequency)); });
      return Rdiv(s, total);
    }
    var conds = cs.slice(0, k).map(function (c, j) { return { c: c, j: j }; });
    conds.sort(function (a, b) { return Rcmp(b.c.frequency, a.c.frequency) || a.j - b.j; });
    var best = conds.map(function (x) { return x.c; }).concat(hasElse ? [cs[n - 1]] : []);
    var e = cost(cs), b = cost(best), where = {};
    best.forEach(function (c, p) { where[c.case] = tests(p); });
    return {
      tiles: { seExpected: ccNum(e), seBest: ccNum(b), seSaved: ccNum(Rsub(e, b)) },
      status: 'The best order is ' + best.map(function (c) { return c.case; }).join(', ') + '. Reordering is valid only if the'
        + ' conditions are mutually exclusive: if two can both hold, the order decides which branch runs.',
      table: { caption: 'Tests to reach each case', head: ['Case', 'Frequency', 'Tests as written', 'Tests in the best order'],
        rows: cs.map(function (c, p) { return [c.case, ccNum(c.frequency), ccInt(tests(p)), ccInt(where[c.case])]; }) }
    };
  };
"""

SE_VIEW_JS["stairs"] = r"""
  SE_VIEW.stairs = function (inst) {
    var st = inst.steps, n = st.length, key = inst.key, i;
    for (i = 1; i < n; i += 1) {
      if (Rcmp(st[i].bound, st[i - 1].bound) <= 0) {
        return { refuse: 'The upper bounds must rise from step to step, and step ' + (i + 1) + ' (' + ccNum(st[i].bound)
          + ') is not above step ' + i + ' (' + ccNum(st[i - 1].bound) + ')' };
      }
    }
    function passes(b) { var c = Rcmp(key, b); return inst.rule === 'below' ? c < 0 : c <= 0; }
    var linear = 0, found = null, probe = {};
    for (i = 0; i < n; i += 1) { linear += 1; if (passes(st[i].bound)) { found = i; break; } }
    var lo = 0, hi = n, binary = 0;
    while (lo < hi) {
      var mid = Math.floor((lo + hi) / 2);
      binary += 1;
      probe[mid] = 'probe ' + binary + ': ' + (passes(st[mid].bound) ? 'passes' : 'fails');
      if (passes(st[mid].bound)) hi = mid; else lo = mid + 1;
    }
    var value = found === null ? 'above the table' : st[found].value;
    return {
      tiles: { seValue: value, seLinear: ccInt(linear), seBinary: ccInt(binary) },
      status: (found === null ? 'The key ' + ccNum(key) + ' passes no step: it is above the table.'
        : 'The key ' + ccNum(key) + ' falls in step ' + (found + 1) + ' (upper bound ' + ccNum(st[found].bound) + ').')
        + ' A step passes when the key is ' + (inst.rule === 'below' ? 'below' : 'at or below') + ' its upper bound.',
      table: { caption: 'The steps', head: ['Step', 'Upper bound', 'Value', 'Linear search', 'Binary search'],
        rows: st.map(function (s, j) { return [ccInt(j + 1), ccNum(s.bound), s.value, j < linear ? 'tested' : '', probe[j] || '']; }) }
    };
  };
"""

SE_VIEW_JS["bisect"] = r"""
  SE_VIEW.bisect = function (inst) {
    var n = ccBigOf(inst.n), k = ccBigOf(inst.k);
    if (k > n) return { refuse: 'The defect is at ' + ccInt(k) + ', past the last of the ' + ccInt(n) + ' positions' };
    var lo = 1n, hi = n, steps = 0, rows = [];
    while (lo < hi) {
      var mid = (lo + hi) / 2n, yes = k <= mid;
      steps += 1;
      rows.push([ccInt(steps), ccRange(R(lo), R(hi)), ccInt(mid), yes ? 'yes: ' + ccRange(R(lo), R(mid)) : 'no: ' + ccRange(R(mid + 1n), R(hi))]);
      if (yes) hi = mid; else lo = mid + 1n;
    }
    var worst = n - 1n === 0n ? 0 : (n - 1n).toString(2).length;
    return {
      tiles: { seSteps: ccInt(steps), seWorst: ccInt(worst) },
      status: 'Halving ' + ccRange(R1, R(n)) + ' finds position ' + ccInt(k) + ' in ' + ccPlural(steps, 'step', 'steps')
        + '; no position takes more than ' + ccInt(worst) + ', the number of times ' + ccInt(n) + ' can be halved before one is left.',
      table: { caption: 'Each step', head: ['Step', 'Interval', 'Midpoint', 'Is it in the lower half?'], rows: rows }
    };
  };
"""

SE_VIEWS = {
    "chain": ([("cases", {"kind": "rec", "what": "Cases in the chain's order (case, frequency; a last case named else is the final else)",
                          "sub": [["case", {"kind": "label"}], ["frequency", {"kind": "nn"}]],
                          "lo": 1, "hi": 20, "unique": True}, None)],
              [("Expected tests as written", "seExpected"), ("Expected tests, best order", "seBest"),
               ("Saved per case", "seSaved")]),
    "stairs": ([("steps", {"kind": "rec", "what": "Steps (upper bound, value), bounds rising",
                           "sub": [["bound", {"kind": "num"}], ["value", {"kind": "label"}]], "lo": 1, "hi": 60}, None),
                ("key", {"kind": "num", "what": "Key"}, None),
                ("rule", {"kind": "word", "words": ["below", "atmost"], "what": "A step holds keys below or atmost its bound"},
                 "below")],
               [("Value", "seValue"), ("Tests, linear search", "seLinear"), ("Tests, binary search", "seBinary")]),
    "bisect": ([("n", {"kind": "count", "max": "1000000000000", "what": "Positions (n)"}, None),
                ("k", {"kind": "count", "max": "1000000000000", "what": "Where the defect is (k)"}, None)],
               [("Steps to find it", "seSteps"), ("Most steps any position takes", "seWorst")]),
}

SE_SUBTITLES = {
    "chain": "expected tests along an if-else chain",
    "stairs": "a staircase table searched two ways",
    "bisect": "halving the search space",
}

# ---------------------------------------------------------------------------
# run
# ---------------------------------------------------------------------------

LP_JS = r"""
  /* run: loops, nests and recursion counted in closed form, never by running
     them; and Java's arithmetic simulated in BigInt (arith, tiles nu*). */
  var LP_VIEW = {}, LP_MIN = -(2n ** 31n), LP_MAX = 2n ** 31n - 1n;
  function lpCompute(view, inst, opts) { return LP_VIEW[view](inst, opts || {}); }
"""

LP_VIEW_JS = {}

LP_VIEW_JS["loop"] = r"""
  var LP_OP = { lt: '<', le: '<=', ne: '!=', gt: '>', ge: '>=' };
  function lpCeil(a, b) { return (a + b - 1n) / b; }
  function lpGcd(a, b) { a = a < 0n ? -a : a; while (b) { var t = a % b; a = b; b = t; } return a; }
  LP_VIEW.loop = function (inst) {
    var start = ccBigOf(inst.start), bound = ccBigOf(inst.bound), step = ccBigOf(inst.step), cmp = inst.cmp;
    var text = 'for (int i = ' + start + '; i ' + LP_OP[cmp] + ' ' + bound + '; i += ' + step + ')';
    if (step === 0n) return { refuse: 'The step is 0, so i never changes; this view needs a step that is not 0' };
    var b = bound, it = null, never = null;
    if (cmp === 'le') { cmp = 'lt'; b = bound + 1n; }
    if (cmp === 'ge') { cmp = 'gt'; b = bound - 1n; }
    if (cmp === 'lt') {
      if (start >= b) it = 0n; else if (step < 0n) never = 'never ends without overflow'; else it = lpCeil(b - start, step);
    } else if (cmp === 'gt') {
      if (start <= b) it = 0n; else if (step > 0n) never = 'never ends without overflow'; else it = lpCeil(start - b, -step);
    } else if (start === b) {
      it = 0n;
    } else if ((b - start) % step === 0n && (b - start) / step > 0n) {
      it = (b - start) / step;
    } else {
      never = (b - start) % lpGcd(step, 2n ** 32n) !== 0n ? 'never ends' : 'never ends without overflow';
    }
    var note = ' An index declared in the for header does not exist after the loop in Java; the last tile is the value an i'
      + ' declared before the loop would hold, which the book advises against relying on.';
    if (never) {
      return { tiles: { lpIterations: never, lpLast: CC_DASH, lpAfter: CC_DASH },
        status: text + ': ' + (never === 'never ends' ? 'no value of i, wrap-around included, ever equals the bound.'
          : 'the test stays true until i passes the end of int and wraps, which is a defect, not an ending.') };
    }
    var last = start + (it - 1n) * step, after = start + it * step;
    if (it > 0n && (after < LP_MIN || after > LP_MAX)) {
      var wrapped = BigInt.asIntN(32, after);
      return { tiles: { lpIterations: 'overflows int after ' + ccInt(it) + ' iterations', lpLast: ccInt(last), lpAfter: CC_DASH },
        status: text + ': after ' + ccPlural(it, 'iteration', 'iterations') + ' i += ' + step + ' passes the end of int and wraps to '
          + ccInt(wrapped) + ', which still passes the test, so the loop does not stop there.' };
    }
    return {
      tiles: { lpIterations: ccInt(it), lpLast: it === 0n ? CC_DASH : ccInt(last), lpAfter: ccInt(after) },
      status: text + ' runs its body ' + ccPlural(it, 'time', 'times') + '.' + note
    };
  };
"""

LP_VIEW_JS["nested"] = r"""
  LP_VIEW.nested = function (inst) {
    var sizes = inst.sizes.map(ccBigOf), asc = sizes.slice().sort(function (a, b) { return a < b ? -1 : (a > b ? 1 : 0); });
    function levels(s) { var p = 1n, out = []; s.forEach(function (x) { p *= x; out.push(p); }); return out; }
    var given = levels(sizes), best = levels(asc), sum = function (v) { return v.reduce(function (a, x) { return a + x; }, 0n); };
    var it = sum(given), bt = sum(best), body = given[given.length - 1];
    return {
      tiles: { lpBody: ccInt(body), lpIterations: ccInt(it), lpBest: ccInt(bt), lpSaved: ccPct(R(it - bt, it)) },
      status: 'The body runs ' + ccInt(body) + ' times in any order. Counting every pass through every loop header, the order given'
        + ' makes ' + ccInt(it) + ' and the smallest loop outermost makes ' + ccInt(bt) + '.',
      table: { caption: 'Each level, outer to inner', head: ['Level', 'Size as given', 'Passes', 'Size, smallest outside', 'Passes'],
        rows: sizes.map(function (s, i) { return [ccInt(i + 1), ccInt(s), ccInt(given[i]), ccInt(asc[i]), ccInt(best[i])]; }) }
    };
  };
"""

LP_VIEW_JS["recursion"] = r"""
  LP_VIEW.recursion = function (inst) {
    var n = ccBigOf(inst.n), fact = inst.fn === 'factorial';
    if (fact && n > 20n) return { refuse: 'factorial(' + n + ') does not fit a Java long; this view stops at n = 20' };
    var value = 1n, calls, i;
    if (fact) {
      for (i = 2n; i <= n; i += 1n) value *= i;
      calls = n > 1n ? n : 1n;
    } else {
      /* f0 = F(i), f1 = F(i + 1); the recursive fibonacci(n) makes 2F(n + 1) - 1 calls */
      var f0 = 0n, f1 = 1n;
      for (i = 0n; i < n; i += 1n) { var u = f0 + f1; f0 = f1; f1 = u; }
      value = f0;
      calls = 2n * f1 - 1n;
    }
    var depth = n > 1n ? n : 1n, loop = n > 1n ? n - 1n : 0n;
    return {
      tiles: { lpCalls: ccInt(calls), lpDepth: ccInt(depth), lpValue: ccInt(value), lpLoop: ccInt(loop) },
      status: 'The recursive ' + inst.fn + '(' + n + ') makes ' + ccPlural(calls, 'call', 'calls') + ', at most ' + ccInt(depth)
        + ' deep; a loop computes the same value in ' + ccPlural(loop, 'iteration', 'iterations') + '.'
    };
  };
"""

LP_VIEW_JS["arith"] = r"""
  /* Java's int and long wrap at 32 and 64 bits (BigInt.asIntN); a double is
     the exact value s*m*2^e with 2^52 <= m < 2^53, rounded from an exact
     rational ties to even. Subnormals and infinities are refused. */
  var NU_REFUSE = 'Java would print Infinity or NaN; this lab does not model it';
  function nuBits(x) { return x === 0n ? 0 : (x < 0n ? -x : x).toString(2).length; }
  function nuRound(r) {
    if (r.n === 0n) return { s: 1, m: 0n, e: 0 };
    var s = r.n < 0n ? -1 : 1, a = r.n < 0n ? -r.n : r.n, d = r.d, e = nuBits(a) - nuBits(d) - 53;
    for (;;) {
      var num = e < 0 ? a << BigInt(-e) : a, den = e > 0 ? d << BigInt(e) : d, q = num / den, rem = num - q * den;
      if (q >= (1n << 53n)) { e += 1; continue; }
      if (q < (1n << 52n)) { e -= 1; continue; }
      if (2n * rem > den || (2n * rem === den && (q & 1n) === 1n)) q += 1n;
      if (q === (1n << 53n)) { q = 1n << 52n; e += 1; }
      if (e > 971) return { over: true };
      if (e < -1074) return { sub: true };
      return { s: s, m: q, e: e };
    }
  }
  function nuValue(x) {
    var n = BigInt(x.s) * x.m;
    return x.e >= 0 ? R(n << BigInt(x.e)) : R(n, 1n << BigInt(-x.e));
  }
  /* Double.toString as JDK 19 prints it: the shortest decimal in the rounding
     interval, the closest to the value of those. (JDK 19 also weighs two-digit
     decimals when the shortest has one digit; for a normal double the interval
     is too narrow to hold a different one, and subnormals are refused.) */
  function nuShort(x) {
    var v = nuValue({ s: 1, m: x.m, e: x.e }), unit = x.e >= 2 ? R(1n << BigInt(x.e - 2)) : R(1n, 1n << BigInt(2 - x.e));
    var down = x.m === (1n << 52n) && x.e > -1074 ? 1n : 2n, incl = (x.m & 1n) === 0n;
    var lo = Rsub(v, Rmul(R(down), unit)), hi = Radd(v, Rmul(R(2n), unit));
    var k0 = ccDigits(v.n) - ccDigits(v.d), best = null;
    function ceil(r) { return r.n >= 0n ? (r.n + r.d - 1n) / r.d : r.n / r.d; }
    function floor(r) { return r.n >= 0n ? r.n / r.d : (r.n - r.d + 1n) / r.d; }
    function consider(len) {
      var found = null;
      for (var k = k0 - len - 1; k <= k0 - len + 2; k += 1) {
        var t = ccTen(k), cmin = ceil(Rdiv(lo, t)), cmax = floor(Rdiv(hi, t));
        if (!incl && Requ(Rmul(R(cmin), t), lo)) cmin += 1n;
        if (!incl && Requ(Rmul(R(cmax), t), hi)) cmax -= 1n;
        var a = 10n ** BigInt(len - 1), b = 10n ** BigInt(len) - 1n;
        if (cmin < a) cmin = a;
        if (cmax > b) cmax = b;
        if (cmin > cmax) continue;
        var exact = Rdiv(v, t), c = floor(exact), frac = Rsub(exact, R(c));
        var cmpHalf = Rcmp(frac, R(1n, 2n));
        if (cmpHalf > 0 || (cmpHalf === 0 && (c & 1n) === 1n)) c += 1n;
        if (c < cmin) c = cmin;
        if (c > cmax) c = cmax;
        var cand = { c: c, k: k, dist: Rabs(Rsub(Rmul(R(c), t), v)) };
        if (!found || Rcmp(cand.dist, found.dist) < 0) found = cand;
      }
      return found;
    }
    for (var len = 1; len <= 17 && !best; len += 1) best = consider(len);
    var ds = String(best.c), k = best.k;
    while (ds.length > 1 && ds.charAt(ds.length - 1) === '0') { ds = ds.slice(0, -1); k += 1; }
    var E = ds.length - 1 + k, out;
    if (E >= -3 && E < 7) {
      if (k >= 0) out = ds + '0'.repeat(k) + '.0';
      else if (ds.length + k > 0) out = ds.slice(0, ds.length + k) + '.' + ds.slice(ds.length + k);
      else out = '0.' + '0'.repeat(-(ds.length + k)) + ds;
    } else {
      out = ds.charAt(0) + '.' + (ds.length > 1 ? ds.slice(1) : '0') + 'E' + E;
    }
    return (x.s < 0 ? '-' : '') + out;
  }
  function nuJava(x) { return x.m === 0n ? (x.neg ? '-0.0' : '0.0') : nuShort(x); }
  /* A Java literal of the type: an exact rational, or a sentence. */
  function nuLiteral(text, type, what) {
    var s = String(text).trim(), m, lim;
    if (type === 'double') {
      m = /^(-?)(\d+\.?\d*|\.\d+)(?:[eE]([+-]?\d+))?[dD]?$/.exec(s);
      if (!m) return what + ' "' + s + '" is not a double literal such as 0.1, 2 or 1.5e-3';
      var parts = m[2].split('.'), digits = parts[0] + (parts[1] || ''), exp = (m[3] ? Number(m[3]) : 0) - (parts[1] || '').length;
      if (Math.abs(exp) > 400) return what + ' "' + s + '" is outside the range of normal doubles';
      var r = exp >= 0 ? R(BigInt(digits) * 10n ** BigInt(exp)) : R(BigInt(digits), 10n ** BigInt(-exp));
      return m[1] === '-' ? { r: Rneg(r), neg: true } : { r: r, neg: false };
    }
    m = type === 'long' ? /^-?\d+[lL]?$/.exec(s) : /^-?\d+$/.exec(s);
    if (!m) return what + ' "' + s + '" is not ' + (type === 'int' ? 'an int literal such as 7 or -12' : 'a long literal such as 7 or 3000000000L');
    var n = BigInt(s.replace(/[lL]$/, ''));
    lim = type === 'int' ? 31n : 63n;
    if (n < -(2n ** lim) || n > 2n ** lim - 1n) return what + ' ' + ccInt(n) + ' does not fit a Java ' + type;
    return { r: R(n), neg: false };
  }
  function nuTrunc(r) { return r.n / r.d; }
  function nuExactOp(a, op, b) {
    if (op === '+') return Radd(a, b);
    if (op === '-') return Rsub(a, b);
    if (op === '*') return Rmul(a, b);
    if (op === '/') return Rdiv(a, b);
    return Rsub(a, Rmul(b, R(nuTrunc(Rdiv(a, b)))));
  }
  LP_VIEW.arith = function (inst) {
    var type = inst.type, op = inst.op, times = Number(ccBigOf(inst.times));
    var A = nuLiteral(inst.start, type, 'The start'), B = nuLiteral(inst.operand, type, 'The operand');
    if (typeof A === 'string') return { refuse: A };
    if (typeof B === 'string') return { refuse: B };
    var zero = Rzero(B.r) && (op === '/' || op === '%');
    if (zero && type === 'double') return { refuse: 'Division by zero: ' + NU_REFUSE };
    var exact = A.r, lost = false, java, stored, i;
    var line = type + ' acc = ' + String(inst.start).trim() + '; repeat ' + times + (times === 1 ? ' time' : ' times') + ': acc = acc '
      + op + ' ' + String(inst.operand).trim() + ';';
    if (zero) {
      return { tiles: { nuJava: 'ArithmeticException', nuExact: CC_DASH, nuEqual: CC_DASH, nuStored: CC_DASH },
        status: line + ' Java throws ArithmeticException on the first step: integer division by zero. The exact value is undefined too.' };
    }
    for (i = 0; i < times && !lost; i += 1) {
      exact = nuExactOp(exact, op, B.r);
      if (ccDigits(exact.n) + ccDigits(exact.d) > 800) lost = true;
    }
    if (type === 'double') {
      var x = nuRound(A.r), y = nuRound(B.r);
      if (x.over || y.over) return { refuse: 'A literal past the largest double: ' + NU_REFUSE };
      if (x.sub || y.sub) return { refuse: 'A literal below the smallest normal double: this lab does not model subnormal numbers' };
      x.neg = A.neg && x.m === 0n;
      y.neg = B.neg && y.m === 0n;
      for (i = 0; i < times; i += 1) {
        var xv = nuValue(x), yv = nuValue(y), r = nuExactOp(xv, op, yv), z = nuRound(r);
        if (z.over) return { refuse: 'Step ' + (i + 1) + ' passes the largest double: ' + NU_REFUSE };
        if (z.sub) return { refuse: 'Step ' + (i + 1) + ' falls below the smallest normal double: this lab does not model subnormal numbers' };
        if (z.m === 0n) {
          var xs = x.m === 0n ? x.neg : x.s < 0, ys = y.m === 0n ? y.neg : y.s < 0;
          if (op === '+') z.neg = x.m === 0n && y.m === 0n && x.neg && y.neg;
          else if (op === '-') z.neg = x.m === 0n && y.m === 0n && x.neg && !y.neg;
          else if (op === '*' || op === '/') z.neg = xs !== ys;
          else z.neg = xs;
        }
        x = z;
      }
      java = nuJava(x);
      stored = nuValue(x);
    } else {
      var bits = type === 'int' ? 32 : 64, acc = A.r.n, o = B.r.n;
      for (i = 0; i < times; i += 1) {
        if (op === '+') acc = acc + o;
        else if (op === '-') acc = acc - o;
        else if (op === '*') acc = acc * o;
        else if (op === '/') acc = acc / o;
        else acc = acc % o;
        acc = BigInt.asIntN(bits, acc);
      }
      java = String(acc);
      stored = R(acc);
    }
    var equal = lost ? CC_DASH : (Requ(stored, exact) ? 'yes' : 'no');
    return {
      tiles: { nuJava: java, nuExact: lost ? CC_DASH : ccNum(exact), nuEqual: equal, nuStored: ccNum(stored) },
      status: line + ' Java prints ' + java + (lost ? '; the exact value passed 400 digits, and this lab stops tracking it there.'
        : (equal === 'yes' ? ', which is the exact value.' : '; the exact value is ' + ccNum(exact) + '.'))
    };
  };
"""

LP_WHOLE = {"kind": "whole", "min": str(INT_MIN), "max": str(INT_MAX)}

LP_VIEWS = {
    "loop": ([("start", dict(LP_WHOLE, what="int i = (start)"), None),
              ("cmp", {"kind": "word", "words": ["lt", "le", "ne", "gt", "ge"], "what": "Test (lt, le, ne, gt or ge)"}, None),
              ("bound", dict(LP_WHOLE, what="Bound"), None),
              ("step", dict(LP_WHOLE, what="Step (a negative step counts down)"), None)],
             [("Iterations", "lpIterations"), ("Last value of i in the body", "lpLast"),
              ("i after the loop, if declared before it", "lpAfter")]),
    "nested": ([("sizes", {"kind": "list", "lo": 1, "hi": 5, "each": {"kind": "count", "max": "1000000"},
                           "what": "Loop sizes, outer to inner"}, None)],
               [("Body runs", "lpBody"), ("Passes, as given", "lpIterations"), ("Passes, smallest outside", "lpBest"),
                ("Saved", "lpSaved")]),
    "recursion": ([("fn", {"kind": "word", "words": ["factorial", "fibonacci"], "what": "Function (factorial or fibonacci)"}, None),
                   ("n", {"kind": "nncount", "max": "90", "what": "n (to 20 for factorial, 90 for fibonacci)"}, None)],
                  [("Calls", "lpCalls"), ("Deepest call", "lpDepth"), ("Value", "lpValue"),
                   ("Iterations of a loop", "lpLoop")]),
    "arith": ([("type", {"kind": "word", "words": ["int", "long", "double"], "what": "Type (int, long or double)"}, None),
               ("start", {"kind": "text", "what": "Start (a Java literal)"}, None),
               ("op", {"kind": "word", "words": ["+", "-", "*", "/", "%"], "what": "Operator (+ - * / %)"}, None),
               ("operand", {"kind": "text", "what": "Operand (a Java literal)"}, None),
               ("times", {"kind": "count", "max": "1000", "what": "Times (1 to 1,000)"}, 1)],
              [("Java prints", "nuJava"), ("Exact arithmetic", "nuExact"), ("The same?", "nuEqual"),
               ("The value stored, exactly", "nuStored")]),
}

LP_SUBTITLES = {
    "loop": "how many times a for loop runs",
    "nested": "passes through nested loops, in two orders",
    "recursion": "calls made by a recursive routine",
    "arith": "what Java computes, against exact arithmetic",
}

# ---------------------------------------------------------------------------
# defects
# ---------------------------------------------------------------------------

DF_JS = r"""
  /* defects: the lesson's cost table and removal rates, multiplied out. */
  var DF_VIEW = {};
  function dfCompute(view, inst, opts) { return DF_VIEW[view](inst, opts || {}); }
  /* Each stage finds its rate of what is left. */
  function dfRemove(inst, hours) {
    var left = inst.injected, found = R0, spent = R0, rows = [];
    inst.stages.forEach(function (s) {
      var f = Rmul(left, s.rate);
      found = Radd(found, f);
      left = Rsub(left, f);
      if (hours) spent = Radd(spent, Rmul(f, s.hours));
      rows.push([s.stage, ccPct(s.rate), ccNum(f), ccNum(left)].concat(hours ? [ccNum(s.hours), ccNum(Rmul(f, s.hours))] : []));
    });
    return { found: found, left: left, spent: spent, rows: rows };
  }
"""

DF_VIEW_JS = {}

DF_VIEW_JS["cost"] = r"""
  DF_VIEW.cost = function (inst, opts) {
    var T = opts.table, lo = R0, hi = R0, early = R0, rows = [], i;
    for (i = 0; i < inst.defects.length; i += 1) {
      var d = inst.defects[i], pair = T[d.introduced + ' ' + d.detected], diag = T[d.introduced + ' ' + d.introduced];
      if (!pair) return { refuse: 'The lesson\'s table has no figure for a defect introduced in ' + d.introduced + ' and found in ' + d.detected };
      if (!diag) return { refuse: 'The lesson\'s table has no figure for a defect found in ' + d.introduced + ', the stage that introduced it' };
      var a = Rparse(pair[0]), b = Rparse(pair[1]), c = d.count;
      lo = Radd(lo, Rmul(c, a));
      hi = Radd(hi, Rmul(c, b));
      early = Radd(early, Rmul(c, Rparse(diag[0])));
      rows.push([d.introduced, d.detected, ccInt(c.n), ccRange(a, b), ccRange(Rmul(c, a), Rmul(c, b))]);
    }
    var none = Rzero(early);
    return {
      tiles: { dfCost: ccRange(lo, hi), dfEarly: ccNum(early),
        dfRatio: none ? CC_DASH : ccTimesRange(Rdiv(lo, early), Rdiv(hi, early)) },
      status: 'Costs are multiples of fixing a defect in the stage that introduced it, from the lesson\'s table.'
        + (none ? ' No defects are counted, so there is no ratio.' : ''),
      table: { caption: 'Each kind of defect', head: ['Introduced', 'Found', 'Count', 'Cost of each', 'Cost'], rows: rows }
    };
  };
"""

DF_VIEW_JS["removal"] = r"""
  DF_VIEW.removal = function (inst) {
    var r = dfRemove(inst, false);
    return {
      tiles: { dfFound: ccNum(r.found), dfRemaining: ccNum(r.left), dfCombined: ccPct(Rdiv(r.found, inst.injected)) },
      status: 'Each stage finds its rate of the defects still there when it runs, so the rates do not add.',
      table: { caption: 'Each stage, in order', head: ['Stage', 'Rate', 'Found', 'Left after'], rows: r.rows }
    };
  };
"""

DF_VIEW_JS["pipeline"] = r"""
  DF_VIEW.pipeline = function (inst) {
    var r = dfRemove(inst, true), none = Rzero(r.found);
    return {
      tiles: { dfFound: ccNum(r.found), dfRemaining: ccNum(r.left), dfCombined: ccPct(Rdiv(r.found, inst.injected)),
        dfHours: ccNum(r.spent), dfPerDefect: none ? CC_DASH : ccNum(Rdiv(r.spent, r.found)) },
      status: 'Each stage finds its rate of the defects still there, at its own hours per defect found.'
        + (none ? ' No defects are found, so there are no hours per defect.' : ''),
      table: { caption: 'Each stage, in order', head: ['Stage', 'Rate', 'Found', 'Left after', 'Hours each', 'Hours'], rows: r.rows }
    };
  };
"""

STAGES = ("req", "arch", "cons", "test", "post")
_STAGE = {"kind": "word", "words": list(STAGES)}
_INJECTED = ("injected", {"kind": "count", "max": "1000000000", "what": "Defects at the start"}, None)

DF_VIEWS = {
    "cost": ([("defects", {"kind": "rec", "what": "Defects (introduced, found, count; stages req arch cons test post)",
                           "sub": [["introduced", _STAGE], ["detected", _STAGE], ["count", {"kind": "nncount"}]],
                           "lo": 1, "hi": 20}, None)],
             [("Cost to fix", "dfCost"), ("Cost had each been found where it was introduced", "dfEarly"),
              ("How many times more", "dfRatio")]),
    "removal": ([_INJECTED,
                 ("stages", {"kind": "rec", "what": "Stages in order (stage, rate as a share)",
                             "sub": [["stage", {"kind": "label"}], ["rate", {"kind": "share"}]],
                             "lo": 1, "hi": 13, "unique": True}, None)],
                [("Found", "dfFound"), ("Remaining", "dfRemaining"), ("Combined removal", "dfCombined")]),
    "pipeline": ([_INJECTED,
                  ("stages", {"kind": "rec", "what": "Stages in order (stage, rate, hours per defect found)",
                              "sub": [["stage", {"kind": "label"}], ["rate", {"kind": "share"}], ["hours", {"kind": "nn"}]],
                              "lo": 1, "hi": 13, "unique": True}, None)],
                 [("Found", "dfFound"), ("Remaining", "dfRemaining"), ("Combined removal", "dfCombined"),
                  ("Hours spent", "dfHours"), ("Hours per defect found", "dfPerDefect")]),
}

DF_SUBTITLES = {
    "cost": "what it costs to find a defect late",
    "removal": "stages that each find a share of what is left",
    "pipeline": "removal, and the hours it takes",
}

# ---------------------------------------------------------------------------
# profile
# ---------------------------------------------------------------------------

PF_JS = r"""
  /* profile: shares of a total, and what tuning some entries does to it. */
  var PF_VIEW = {};
  function pfCompute(view, inst, opts) { return PF_VIEW[view](inst, opts || {}); }
  /* The fewest entries, largest first, whose amounts reach target of the total. */
  function pfPareto(amounts, total, target) {
    var s = amounts.slice().sort(function (a, b) { return Rcmp(b, a); }), acc = R0, k = 0;
    for (var i = 0; i < s.length; i += 1) {
      acc = Radd(acc, s[i]);
      k += 1;
      if (Rcmp(Rdiv(acc, total), target) >= 0) break;
    }
    return k;
  }
"""

PF_VIEW_JS = {}

PF_VIEW_JS["shares"] = r"""
  PF_VIEW.shares = function (inst, opts) {
    var es = inst.entries, total = ccSum(es.map(function (e) { return e.amount; })), target = Rparse(opts.target);
    if (Rzero(total)) return { refuse: 'The amounts add up to 0; a share needs a total above 0' };
    var tagged = ccSum(es.filter(function (e) { return e.tag; }).map(function (e) { return e.amount; })), top = es[0];
    es.forEach(function (e) { if (Rcmp(e.amount, top.amount) > 0) top = e; });
    var tied = es.filter(function (e) { return Requ(e.amount, top.amount); }).map(function (e) { return e.name; });
    var k = pfPareto(es.map(function (e) { return e.amount; }), total, target);
    return {
      tiles: { pfTotal: ccNum(total), pfTagged: ccPct(Rdiv(tagged, total)), pfTop: top.name + ', ' + ccPct(Rdiv(top.amount, total)),
        pfPareto: k + ' of ' + es.length },
      status: k + ' of ' + es.length + ' entries reach ' + ccFrac(target) + ' of the total, taken largest first.'
        + (tied.length > 1 ? ' The largest amount is shared by ' + tied.join(', ') + '; the tile shows the first listed.' : ''),
      table: { caption: 'Each entry', head: ['Entry', 'Amount', 'Share', opts.tag_label],
        rows: es.map(function (e) { return [e.name, ccNum(e.amount), ccPct(Rdiv(e.amount, total)), e.tag ? 'yes' : '']; }) }
    };
  };
"""

PF_VIEW_JS["speedup"] = r"""
  PF_VIEW.speedup = function (inst, opts) {
    var rs = inst.routines, before = ccSum(rs.map(function (r) { return r.time; })), target = Rparse(opts.target);
    if (Rzero(before)) return { refuse: 'The times add up to 0; a speedup needs a total above 0' };
    var after = ccSum(rs.map(function (r) { return Rdiv(r.time, r.factor); }));
    var k = pfPareto(rs.map(function (r) { return r.time; }), before, target);
    return {
      tiles: { pfBefore: ccNum(before), pfAfter: ccNum(after), pfSpeedup: ccNum(Rdiv(before, after)),
        pfSaved: ccPct(Rdiv(Rsub(before, after), before)), pfPareto: k + ' of ' + rs.length },
      status: k + ' of ' + rs.length + ' routines reach ' + ccFrac(target) + ' of the time before tuning, taken largest first.'
        + ' A factor of 1 leaves a routine unchanged; a factor of 10 makes it ten times as fast.',
      table: { caption: 'Each routine', head: ['Routine', 'Before', 'Factor', 'After', 'Share before'],
        rows: rs.map(function (r) { return [r.name, ccNum(r.time), ccNum(r.factor), ccNum(Rdiv(r.time, r.factor)), ccPct(Rdiv(r.time, before))]; }) }
    };
  };
"""

PF_VIEWS = {
    "shares": ([("entries", None, None)],
               [("Total", "pfTotal"), ("Tagged share", "pfTagged"), ("Largest entry", "pfTop"),
                ("Entries reaching the target", "pfPareto")]),
    "speedup": ([("routines", {"kind": "rec", "what": "Routines (name, time, speedup factor; 1 = unchanged)",
                               "sub": [["name", {"kind": "label"}], ["time", {"kind": "nn"}],
                                       ["factor", {"kind": "pos", "min": "1/1000"}]],
                               "lo": 1, "hi": 20, "unique": True}, None)],
                [("Time before", "pfBefore"), ("Time after", "pfAfter"), ("Speedup", "pfSpeedup"), ("Saved", "pfSaved"),
                 ("Routines reaching 4/5 of the time", "pfPareto")]),
}

PF_SUBTITLES = {
    "shares": "each entry's share of the total",
    "speedup": "tuning some routines, and the whole program's time",
}

# ---------------------------------------------------------------------------
# project
# ---------------------------------------------------------------------------

PJ_JS = r"""
  /* project: the lesson's figures for size, staff, effort and payback. */
  var PJ_VIEW = {};
  function pjCompute(view, inst, opts) { return PJ_VIEW[view](inst, opts || {}); }
"""

PJ_VIEW_JS = {}

PJ_VIEW_JS["language"] = r"""
  PJ_VIEW.language = function (inst) {
    var eq = Rdiv(inst.size, inst.ratio);
    return {
      tiles: { pjEquivalent: ccNum(eq) },
      status: ccNum(inst.size) + ' statements of C do the work of ' + ccNum(eq) + ' statements of a language at a ratio of '
        + ccNum(inst.ratio) + '. The ratio measures statements, not time, defects or the team\'s experience.'
    };
  };
"""

PJ_VIEW_JS["scale"] = r"""
  PJ_VIEW.scale = function (inst) {
    var p = ccBigOf(inst.people), k = inst.kloc;
    if (Rcmp(inst.densityLow, inst.densityHigh) > 0) return { refuse: 'The low defect density is above the high one' };
    if (Rcmp(inst.prodLow, inst.prodHigh) > 0) return { refuse: 'The low productivity is above the high one' };
    var thousand = Rmul(k, R(1000n));
    return {
      tiles: { pjPaths: ccInt(p * (p - 1n) / 2n), pjDefects: ccRange(Rmul(k, inst.densityLow), Rmul(k, inst.densityHigh)),
        pjStaffYears: ccRange(Rdiv(thousand, inst.prodHigh), Rdiv(thousand, inst.prodLow)),
        pjSpread: ccNum(Rdiv(inst.prodHigh, inst.prodLow)) },
      status: ccInt(p) + ' people have ' + ccInt(p * (p - 1n) / 2n) + ' possible communication paths. The staff-years run from'
        + ' the fastest productivity to the slowest; the slowest estimate is ' + ccTimes(Rdiv(inst.prodHigh, inst.prodLow))
        + ' the fastest.'
    };
  };
"""

PJ_VIEW_JS["effort"] = r"""
  PJ_VIEW.effort = function (inst) {
    var p = R1, rows = [];
    inst.factors.forEach(function (f) { p = Rmul(p, f.multiplier); rows.push([f.factor, ccNum(f.multiplier), ccNum(p)]); });
    return {
      tiles: { pjProduct: ccNum(p), pjEffort: ccNum(Rmul(inst.nominal, p)) },
      status: 'The multipliers multiply: the nominal estimate of ' + ccNum(inst.nominal) + ' times ' + ccNum(p) + '.',
      table: { caption: 'Each factor', head: ['Factor', 'Multiplier', 'Running product'], rows: rows }
    };
  };
"""

PJ_VIEW_JS["breakeven"] = r"""
  PJ_VIEW.breakeven = function (inst) {
    var gain = Rsub(inst.manual, inst.auto);
    if (Rsign(gain) <= 0) return { refuse: 'A run by hand must take longer than an automated run, or the tool never pays back' };
    var need = Rdiv(Rmul(inst.build, R(60n)), gain), runs = (need.n + need.d - 1n) / need.d;
    var year = Rsub(Rdiv(Rmul(Rmul(gain, inst.perWeek), R(52n)), R(60n)), inst.build);
    return {
      tiles: { pjRuns: ccInt(runs), pjWeeks: ccNum(Rdiv(R(runs), inst.perWeek)), pjYear: ccNum(year) },
      status: 'Each automated run saves ' + ccNum(gain) + ' minutes, so ' + ccInt(runs) + ' runs repay the '
        + ccNum(inst.build) + ' hours of building it. Over a year of 52 weeks the net is ' + ccNum(year) + ' hours'
        + (Rsign(year) < 0 ? ', a loss.' : '.')
    };
  };
"""

_POS = {"kind": "pos"}

PJ_VIEWS = {
    "language": ([("size", dict(_POS, what="Statements of C"), None),
                  ("ratio", dict(_POS, what="Statements of C per statement of the language"), None)],
                 [("Statements of the language", "pjEquivalent")]),
    "scale": ([("people", {"kind": "count", "max": "100000", "what": "People"}, None),
               ("kloc", dict(_POS, what="Size (thousands of lines)"), None),
               ("densityLow", {"kind": "nn", "what": "Defects per thousand lines, low"}, None),
               ("densityHigh", {"kind": "nn", "what": "Defects per thousand lines, high"}, None),
               ("prodLow", dict(_POS, what="Lines per staff-year, low"), None),
               ("prodHigh", dict(_POS, what="Lines per staff-year, high"), None)],
              [("Communication paths", "pjPaths"), ("Defects", "pjDefects"), ("Staff-years", "pjStaffYears"),
               ("Spread of the productivity range", "pjSpread")]),
    "effort": ([("nominal", dict(_POS, what="Nominal effort"), None),
                ("factors", {"kind": "rec", "what": "Factors (factor, multiplier)",
                             "sub": [["factor", {"kind": "label"}], ["multiplier", {"kind": "pos"}]],
                             "lo": 1, "hi": 17, "unique": True}, None)],
               [("Product of the multipliers", "pjProduct"), ("Adjusted effort", "pjEffort")]),
    "breakeven": ([("build", dict(_POS, what="Hours to build the tool"), None),
                   ("manual", dict(_POS, what="Minutes per run by hand"), None),
                   ("auto", {"kind": "nn", "what": "Minutes per run, automated"}, None),
                   ("perWeek", dict(_POS, what="Runs per week"), None)],
                  [("Runs to pay back", "pjRuns"), ("Weeks to pay back", "pjWeeks"),
                   ("Hours saved in the first year", "pjYear")]),
}

PJ_SUBTITLES = {
    "language": "statements of C, and of another language",
    "scale": "paths, defects and staff-years as a project grows",
    "effort": "a nominal estimate and its multipliers",
    "breakeven": "when a tool repays the time it took",
}

# ---------------------------------------------------------------------------
# The modes, and the Lab
# ---------------------------------------------------------------------------

_INTRO = {
    "deps": "Each record is one edge of the structure the lesson states.",
    "cond": "The lab parses each condition with its own parser; it never runs it.",
    "search": "Every test is counted, not timed.",
    "run": "Counted in closed form from the inputs; nothing is run.",
    "defects": "Every rate, cost and hour is the lesson's figure, not the lab's.",
    "profile": "The amounts are the lesson's figures, not a measurement the lab made.",
    "project": "Every ratio, density and productivity is the lesson's figure, not the lab's.",
}

_VIEW_INTRO = {
    ("run", "loop"): "In Java an index declared in the for header does not exist after the loop; the last tile is the value"
                     " an i declared before it would hold, which the book advises against relying on (p. 377).",
    ("run", "arith"): "Java prints a double as JDK 19 and later print it: the shortest decimal that reads back to the same"
                      " double. Earlier JDKs print longer strings for some values.",
    ("cond", "range"): "The check is evaluated at every int that can change its answer, so every int is decided exactly.",
}

# mode: (prefix, fn, base JS, view JS, views, subtitles, family, title)
MODE_TABLE = {
    "deps": ("dg", "dgCompute", DG_JS, DG_VIEW_JS, DG_VIEWS, DG_SUBTITLES, 2, "Counting dependencies"),
    "cond": ("cd", "cdCompute", CD_JS, CD_VIEW_JS, CD_VIEWS, CD_SUBTITLES, 2, "Reading conditions"),
    "search": ("se", "seCompute", SE_JS, SE_VIEW_JS, SE_VIEWS, SE_SUBTITLES, 2, "Counting tests"),
    "run": ("lp", "lpCompute", LP_JS, LP_VIEW_JS, LP_VIEWS, LP_SUBTITLES, 2, "Counting what runs"),
    "defects": ("df", "dfCompute", DF_JS, DF_VIEW_JS, DF_VIEWS, DF_SUBTITLES, 3, "Defect arithmetic"),
    "profile": ("pf", "pfCompute", PF_JS, PF_VIEW_JS, PF_VIEWS, PF_SUBTITLES, 3, "Where the time goes"),
    "project": ("pj", "pjCompute", PJ_JS, PJ_VIEW_JS, PJ_VIEWS, PJ_SUBTITLES, 3, "Project arithmetic"),
}
MODES = tuple(MODE_TABLE)


def _fraction(kit, key, value, lo_open=0, hi=1):
    f = cc.rparse(cc.ftext(value)) if isinstance(value, (int, Fraction)) and not isinstance(value, bool) else (
        cc.rparse(value) if isinstance(value, str) else None)
    if f is None or not lo_open < f <= hi:
        raise ValueError("%s: cfg[%r] is %r; it is a number above %s and at most %s" % (kit, key, value, lo_open, hi))
    return f


def _cost_table(kit, table):
    """cfg['table'] -> {"req test": [lo, hi]}; keys a (stage, stage) pair or "req test"; values a number, a
    (low, high) pair or "5-10". Every figure is positive, and a stage's own cell is one figure."""
    if not isinstance(table, dict) or not table:
        raise ValueError("%s: cfg['table'] is the lesson's cost table, a dict from (introduced, found) to a multiplier" % kit)
    out = {}
    for key, value in table.items():
        pair = re.split(r"[\s,]+", key.strip()) if isinstance(key, str) else list(key)
        if len(pair) != 2 or any(s not in STAGES for s in pair):
            raise ValueError("%s: cfg['table'] key %r is not two of the stages %s" % (kit, key, " ".join(STAGES)))
        if isinstance(value, str):
            ends = [cc.rparse(x) for x in re.split(r"\s*[-–]\s*", value.strip())]
        elif isinstance(value, (list, tuple)):
            ends = [cc.rparse(cc.ftext(x)) if not isinstance(x, str) else cc.rparse(x) for x in value]
        else:
            ends = [cc.rparse(cc.ftext(value))]
        if len(ends) == 1:
            ends = ends * 2
        if len(ends) != 2 or any(x is None or x <= 0 for x in ends) or ends[0] > ends[1]:
            raise ValueError("%s: cfg['table'][%r] is %r; it is a positive multiplier or a low-high range" % (kit, key, value))
        if pair[0] == pair[1] and ends[0] != ends[1]:
            raise ValueError("%s: cfg['table'][%r]: a stage's own cell is one figure, the baseline" % (kit, key))
        out[" ".join(pair)] = [cc.ftext(ends[0]), cc.ftext(ends[1])]
    for a, b in [k.split() for k in list(out)]:
        if "%s %s" % (a, a) not in out:
            raise ValueError("%s: cfg['table'] has (%s, %s) but not (%s, %s), the baseline the ratio needs" % (kit, a, b, a, a))
    return out


def _options(cfg, kit, mode, view, fields):
    """(fixed opts, extra cfg keys, fields with any cfg-dependent spec filled in)."""
    fixed, keys = {}, []
    if MODE_TABLE[mode][6] == 3:
        keys.append("source")
    if (mode, view) == ("defects", "cost"):
        fixed["table"], keys = _cost_table(kit, cfg.get("table")), keys + ["table"]
    if mode == "profile":
        fixed["target"] = cc.ftext(_fraction(kit, "target", cfg.get("target", Fraction(4, 5))))
        keys += ["target", "unit"]
        cc.plain(cfg, kit, "unit", "", limit=30)
    if (mode, view) == ("profile", "shares"):
        tag = cfg.get("tag", "c")
        if not isinstance(tag, str) or not re.fullmatch(r"[a-z]", tag):
            raise ValueError("%s: cfg['tag'] is %r; it is one lower-case letter" % (kit, tag))
        label = cc.plain(cfg, kit, "tag_label", "tagged", limit=40)
        fixed["tag_label"], keys = label[:1].upper() + label[1:], keys + ["tag", "tag_label"]
        fields = [("entries", {"kind": "rec", "what": "Entries (name, amount, and %s to mark it %s)" % (tag, label),
                               "sub": [["name", {"kind": "label"}], ["amount", {"kind": "nn"}],
                                       ["tag", {"kind": "tag", "tag": tag}]],
                               "opt": 1, "lo": 1, "hi": 20, "unique": True}, None)]
    return fixed, keys, fields


def _tiles(cfg, mode, view, tiles, fixed):
    """Tile labels that carry the lesson's unit, target or tag."""
    if mode != "profile":
        return tiles
    unit, out = cfg.get("unit", ""), []
    for label, cid in tiles:
        if cid in ("pfTotal", "pfBefore", "pfAfter") and unit:
            label = "%s (%s)" % (label, unit)
        if cid == "pfPareto":
            label = ("Entries reaching %s of the total" if view == "shares" else "Routines reaching %s of the time") % fixed["target"]
        if cid == "pfTagged" and cfg.get("tag_label"):
            label = "Share that is %s" % cfg["tag_label"]
        out.append((label, cid))
    return out


def _check_presets(kit, mode, view, fields, cfg):
    """D.3: a condition the Python mirror cannot parse, or a range check over
    more than one variable, raises here, naming the preset."""
    if mode != "cond" or view == "barricade":
        return
    for p in cfg["presets"]:
        where = "%s preset %r" % (kit, p.get("id"))
        if view == "range":
            names = cc.cond_vars(where, str(p.get("cond", cfg.get("cond"))), True)
            if len(names) > 1:
                raise ValueError("%s: the check names %s; the range view reads one variable" % (where, ", ".join(names)))
        else:
            names = []
            for key in ("a", "b"):
                for n in cc.cond_vars(where, str(p.get(key, cfg.get(key))), False):
                    if n not in names:
                        names.append(n)
            if len(names) > 5:
                raise ValueError("%s: the two conditions name %d variables; the truth view tabulates at most 5" % (where, len(names)))


def mode_lab(cfg, mode):
    prefix, fn, base, view_js, views, subtitles, family, title = MODE_TABLE[mode]
    order = tuple(views)
    view = cfg.get("view", order[0])
    kit = "%s/%s/%s" % (KIT, mode, view)
    if view not in views:
        raise ValueError("cckit/%s: unknown view %r; the views are %s" % (mode, view, ", ".join(order)))
    fields, tiles = views[view]
    fixed, keys, fields = _options(cfg, kit, mode, view, fields)
    intro = cc.FAMILY[family] + " " + _INTRO[mode]
    if (mode, view) in _VIEW_INTRO:
        intro += " " + _VIEW_INTRO[(mode, view)]
    # cfg["source"] is appended to the kit's own intro, and a custom panel_intro
    # replaces that intro whole (cckit_core.build_lab), so the two together
    # would publish the panel without its "Figures:" sentence and say nothing.
    # Every family-3 lesson writes its "Figures:" sentence into its panel_intro
    # already; appending source as well would print it twice. So refuse the pair.
    if cfg.get("source") and cfg.get("panel_intro"):
        raise ValueError("%s: cfg sets both 'source' and 'panel_intro'; a panel_intro replaces the intro that source "
                         "is appended to, so the source would be dropped. Write the \"Figures: ...\" sentence into "
                         "panel_intro and drop 'source', or drop panel_intro" % kit)
    if family == 3 and cfg.get("source"):
        intro +=" Figures: %s." % cc.plain(cfg, kit, "source", "", limit=200).rstrip(".")
    lab = cc.build_lab(cfg, kit=kit, prefix=prefix, view=view, fields=fields, tiles=_tiles(cfg, mode, view, tiles, fixed), fn=fn,
                       js=base + view_js[view], fixed=fixed,
                       title="Java's arithmetic" if view == "arith" else title, subtitle=subtitles[view],
                       family=family, intro=intro, extra_keys=keys)
    _check_presets(kit, mode, view, fields, cfg)
    return lab


__all__ = ["MODES", "MODE_TABLE", "mode_lab"]
