"""eakit -- the lab kit of Patterns of Enterprise Application Architecture, Read Along.

Specified in docs/enterprise-patterns/PLAN.md section D (D.0 conventions, D.1
the eight modes, D.2 what the kit must never do, D.3 the build-time checks);
the report an author configures a lesson from is
docs/enterprise-patterns/kit-report.md. Eight modes, in two families (D.0):

  perf     (pz)  load, scale                                 family 2
  remote   (rr)  boundary (family 1), calls, payload         family 2
  load     (ld)  instances, identity, graph, tree (family 1), finds (2)
  uow      (uw)  commit, order                               family 1
  inherit  (ih)  tables                                      family 1
  lock     (ol)  reads, timeline                             family 1
  session  (sn)  objects, state                              family 2
  money    (mn)  allocate                                    family 2

This module holds the entry point and the perf, remote, load and uow modes;
eakit_b.py holds inherit, lock, session and money; eakit_core.py the shared
printing, parsing and wiring. Each mode has one pure JS function
<xx>Compute(view, inst, opts), which scripts/mathcheck.js calls (section
"eakit"). A page ships RATIONAL_JS, EA_CORE_JS, its mode's base block and its
own view's block -- never the other views (D.0, page weight).

THE FIGURES ARE THE LESSON'S (D.0, D.2). No response time, throughput,
latency, row count, session size or amount is a constant here: every one
arrives in a preset. Nothing typed is evaluated as script.

IDS. Every tile id begins with its mode's prefix; inputs are <prefix>In<Field>;
each page has <prefix>Preset, <prefix>Status and <prefix>Table. Grepped against
scripts/mathpath/labs/*.py on 2026-10-31 for every JS function and variable
(ea*, EA_*, pz*, PZ_*, rr*, RR_*, ld*, LD_*, uw*, UW_*, ih*, IH_*, ol*, OL_*,
sn*, SN_*, mn*, MN_*) and every element id the kit defines: none is used by
another kit.
"""

import re

from . import eakit_core as ea

KIT = "eakit"
SEARCH = 10000          # D.0: a projected search stops at 10,000 servers

# ---------------------------------------------------------------------------
# perf (pz): response time against load, and throughput against servers
# ---------------------------------------------------------------------------

PZ_JS = r"""
  var PZ_VIEW = {};
  function pzCompute(view, inst, opts) { return eaRun(PZ_VIEW[view], inst, opts); }
  /* The points by system, in the order each system first appears, each
     system's sorted by its load (x). A load measured twice is refused. */
  function pzSystems(points, xk, yk, what) {
    var by = {}, order = [];
    points.forEach(function (p) {
      if (!Object.prototype.hasOwnProperty.call(by, p.system)) { by[p.system] = []; order.push(p.system); }
      by[p.system].forEach(function (q) {
        if (Requ(q.x, p[xk])) eaRefuse('System ' + p.system + ' is measured at ' + eaInt(p[xk].n) + ' ' + what + ' twice');
      });
      by[p.system].push({ x: p[xk], y: p[yk] });
    });
    return order.map(function (s) {
      var pts = by[s].slice().sort(function (a, b) { return Rcmp(a.x, b.x); });
      var first = pts[0], last = pts[pts.length - 1];
      return { name: s, pts: pts, first: first, last: last,
        rate: pts.length > 1 ? Rdiv(Rsub(last.y, first.y), Rsub(last.x, first.x)) : null };
    });
  }
"""

PZ_VIEW_JS = {}

PZ_VIEW_JS["load"] = r"""
  PZ_VIEW.load = function (inst) {
    var S = pzSystems(inst.points, 'users', 'ms', 'users'), u = inst.users;
    var per = [], ratio = [], at = [], rows = [], outside = [];
    S.forEach(function (s) {
      per.push(s.name + ' ' + (s.rate ? eaNum(s.rate) + ' ms a user' : EA_DASH));
      ratio.push(s.name + ' ' + (s.rate ? eaTimes(Rdiv(s.last.y, s.first.y)) : EA_DASH));
      var v = null;
      s.pts.forEach(function (p, i) {
        if (v !== null) return;
        if (Requ(p.x, u)) { v = p.y; return; }
        var q = s.pts[i + 1];
        if (q && Rcmp(p.x, u) < 0 && Rcmp(u, q.x) < 0) {
          v = Radd(p.y, Rmul(Rsub(q.y, p.y), Rdiv(Rsub(u, p.x), Rsub(q.x, p.x))));
        }
      });
      if (v === null) outside.push(s.name);
      at.push(s.name + (v === null ? ' outside its measured loads' : ' ' + eaNum(v) + ' ms'));
      s.pts.forEach(function (p) { rows.push([s.name, eaInt(p.x.n), eaNum(p.y)]); });
    });
    var one = S.filter(function (s) { return !s.rate; }).map(function (s) { return s.name; });
    return {
      tiles: { pzPerUser: per.join('; '), pzRatio: ratio.join('; '), pzAt: at.join('; ') },
      status: 'The response times are the lesson\'s figures, not a measurement of your system. '
        + 'Between two measurements the lab draws a straight line; that is the lab\'s assumption, not a measurement, '
        + 'and Fowler\'s advice is to measure at the load you care about.'
        + (outside.length ? ' At ' + eaInt(u.n) + ' users ' + eaNames(outside) + (outside.length === 1 ? ' has' : ' have')
          + ' no measurement either side, and the lab does not extrapolate.' : '')
        + (one.length ? ' ' + eaNames(one) + (one.length === 1 ? ' has' : ' have') + ' one measurement, which gives no change per user and no ratio.' : ''),
      table: { caption: 'Each measurement, by system and load', head: ['system', 'users', 'response (ms)'], rows: rows }
    };
  };
"""

PZ_VIEW_JS["scale"] = r"""
  /* A system's projection at n servers: the measured value where n was
     measured, otherwise the straight line through its first and last
     measurements; null with one measurement. */
  function pzProj(s, n) {
    for (var i = 0; i < s.pts.length; i += 1) if (Requ(s.pts[i].x, n)) return s.pts[i].y;
    return s.rate ? Radd(s.last.y, Rmul(s.rate, Rsub(n, s.last.x))) : null;
  }
  function pzMeasured(s, n) { return s.pts.some(function (p) { return Requ(p.x, n); }); }
  /* The least n from 1 to 10,000 whose projection reaches `need`, in closed
     form: the least measured n that reaches it, against the least unmeasured
     n on the line that does. */
  function pzNeedOf(s, need) {
    var best = null, n;
    s.pts.forEach(function (p) { if (best === null && Rcmp(p.y, need) >= 0) best = p.x.n; });
    if (s.rate) {
      if (Rsign(s.rate) > 0) {
        n = eaCeil(Radd(s.last.x, Rdiv(Rsub(need, s.last.y), s.rate)));
        if (n < 1n) n = 1n;
      } else {
        n = 1n;
      }
      while (n <= 10000n && pzMeasured(s, R(n))) n += 1n;
      if (n <= 10000n && Rcmp(pzProj(s, R(n)), need) >= 0 && (best === null || n < best)) best = n;
    }
    return best;
  }
  PZ_VIEW.scale = function (inst, opts) {
    var unit = opts.unit, units = unit + 's', plural = function (n) { return eaInt(n) + ' ' + (n === 1n ? unit : units); };
    var S = pzSystems(inst.points, 'servers', 'tps', units), eff = [], marg = [], need = [], at = [], rows = [], cross;
    S.forEach(function (s) {
      eff.push(s.name + ' ' + eaNum(Rdiv(s.first.y, s.first.x)) + ' a ' + unit);
      marg.push(s.name + ' ' + (s.rate ? eaNum(s.rate) : EA_DASH));
      var n = pzNeedOf(s, inst.need);
      need.push(s.name + ' ' + (n !== null ? eaInt(n) : (!s.rate ? 'not measured: one measurement gives no rate'
        : (Rsign(s.rate) <= 0 ? 'never at this rate' : 'more than 10,000'))));
      var v = pzProj(s, inst.at);
      at.push(s.name + ' ' + (v === null ? EA_DASH : eaNum(v)));
      s.pts.forEach(function (p) { rows.push([s.name, eaInt(p.x.n), eaNum(p.y), eaNum(Rdiv(p.y, p.x))]); });
    });
    if (S.length !== 2) cross = EA_DASH + ': the crossover compares two systems';
    else if (!S[0].rate || !S[1].rate) cross = EA_DASH + ': each system needs two measurements';
    else {
      cross = 'none';
      var a = S[0], b = S[1], first = null;
      for (var k = 1n; k <= 10000n; k += 1n) {
        var va = pzProj(a, R(k)), vb = pzProj(b, R(k)), sg = Rcmp(va, vb);
        if (first === null) first = sg;
        if (sg === 0 || sg !== first) {
          cross = plural(k) + (sg === 0 ? ' (both ' + eaNum(va) + ')' : ' (' + a.name + ' ' + eaNum(va) + ', ' + b.name + ' ' + eaNum(vb) + ')');
          break;
        }
      }
    }
    return {
      tiles: { pzEfficiency: eff.join('; '), pzMarginal: marg.join('; '), pzCrossover: cross,
        pzNeed: need.join('; '), pzAt: at.join('; ') },
      status: 'The throughputs are the lesson\'s figures, not a measurement of your system. '
        + 'Past the last measurement the lab carries on at the measured rate, which is what the lesson\'s figures say and nothing more. '
        + 'The crossover and the ' + units + ' needed are looked for from 1 to 10,000 ' + units + ', and no further.',
      table: { caption: 'Each measurement, by system and ' + unit + ' count', head: ['system', units, 'throughput (tps)', 'tps a ' + unit], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# remote (rr): calls across a boundary, coarse calls, and the DTO
# ---------------------------------------------------------------------------

RR_JS = r"""
  var RR_VIEW = {};
  function rrCompute(view, inst, opts) { return eaRun(RR_VIEW[view], inst, opts); }
  var RR_TIMES = ' The times are the lesson\'s figures, not a measurement of your system.';
"""

RR_VIEW_JS = {}

RR_VIEW_JS["boundary"] = r"""
  RR_VIEW.boundary = function (inst) {
    var node = {}, named = {}, total = 0n, remote = 0n, rows = [];
    inst.calls.forEach(function (c) { named[c.caller] = true; named[c.callee] = true; });
    inst.nodes.forEach(function (p) {
      if (!named[p.a]) eaRefuse('Nodes names ' + p.a + ', which no call has');
      node[p.a] = p.b;
    });
    var on = function (c) { return Object.prototype.hasOwnProperty.call(node, c) ? node[c] : 'main'; };
    var R_ = inst.remoteUs, L_ = inst.localUs;
    inst.calls.forEach(function (c) {
      var far = on(c.caller) !== on(c.callee), k = c.count.n;
      total += k;
      if (far) remote += k;
      rows.push([c.caller, c.callee, eaInt(k), on(c.caller) + ' → ' + on(c.callee), far ? 'remote' : 'local',
        eaNum(Rmul(R(k), far ? R_ : L_))]);
    });
    var t = Radd(Rmul(R(remote), R_), Rmul(R(total - remote), L_)), one = Rmul(R(total), L_);
    return {
      tiles: { rrCalls: eaInt(total), rrRemote: eaInt(remote), rrTime: eaNum(t),
        rrShare: total ? eaPct(Rdiv(Rmul(R(remote), R_), t)) : EA_DASH, rrOneNode: eaNum(one),
        rrRatio: total ? eaTimes(Rdiv(t, one)) : EA_DASH },
      status: eaInt(remote) + ' of ' + eaPlural(total, 'call', 'calls') + ' cross a node boundary. '
        + 'The times are the lesson\'s, in microseconds: a remote call\'s cost against a local one is what the lesson states, not a measurement.'
        + (inst.nodes.length ? '' : ' No node is given, so every class runs on main and no call is remote.')
        + (total ? '' : ' There are no calls, so there is no share and no ratio.'),
      table: { caption: 'Each call, and where it runs', head: ['caller', 'callee', 'calls', 'nodes', 'kind', 'time (µs)'], rows: rows }
    };
  };
"""

RR_VIEW_JS["calls"] = r"""
  RR_VIEW.calls = function (inst) {
    var n = 0n, m = BigInt(inst.ops.length), L_ = inst.latencyMs, w = inst.workMs, rows = [];
    inst.ops.forEach(function (o) {
      n += o.fine.n;
      rows.push([o.operation, eaInt(o.fine.n), eaNum(Rmul(o.fine, Radd(L_, w))), eaNum(Radd(L_, Rmul(o.fine, w)))]);
    });
    var fine = Rmul(R(n), Radd(L_, w)), coarse = Radd(Rmul(R(m), L_), Rmul(R(n), w));
    return {
      tiles: { rrFineTrips: eaInt(n), rrCoarseTrips: eaInt(m), rrFineMs: eaNum(fine), rrCoarseMs: eaNum(coarse),
        rrLatencyShare: eaPct(Rdiv(Rmul(R(n), L_), fine)), rrSpeedup: eaTimes(Rdiv(fine, coarse)) },
      status: eaPlural(n, 'fine-grained call', 'fine-grained calls') + ' become ' + eaPlural(m, 'coarse-grained call', 'coarse-grained calls')
        + '. The lab assumes the work is the same either way; what the coarse calls remove is the waits.' + RR_TIMES,
      table: { caption: 'Each coarse-grained call and the fine-grained calls it replaces',
        head: ['operation', 'fine-grained calls', 'their time (ms)', 'one coarse call (ms)'], rows: rows }
    };
  };
"""

RR_VIEW_JS["payload"] = r"""
  RR_VIEW.payload = function (inst) {
    var L_ = inst.latencyMs, bw = inst.bytesPerMs, f = inst.factor, k = 0n, all = 0n, needB = 0n, rows = [];
    inst.fields.forEach(function (x) {
      all += x.bytes.n;
      if (x.needed === 'yes') { k += 1n; needB += x.bytes.n; }
      rows.push([x.field, eaInt(x.bytes.n), x.needed, eaNum(Rmul(x.bytes, f))]);
    });
    var allB = Rmul(R(all), f), nb = Rmul(R(needB), f);
    var getter = Radd(Rmul(R(k), L_), Rdiv(nb, bw)), dto = Radd(L_, Rdiv(allB, bw));
    var spare = k > 1n ? Rmul(Rmul(R(k - 1n), L_), bw) : R0;
    return {
      tiles: { rrGetterCalls: eaInt(k), rrGetterMs: eaNum(getter), rrDtoBytes: eaNum(allB), rrDtoMs: eaNum(dto),
        rrExtraBytes: eaNum(Rsub(allB, nb)), rrSpare: eaNum(spare) },
      status: 'The model sends data at a steady rate after a fixed latency; real networks are lumpier.'
        + ' The latency, the rate and the encoding factor are the lesson\'s figures, not a measurement of your system.'
        + (k ? '' : ' No field is needed, so the getters make no call.'),
      table: { caption: 'Each field, and the bytes it sends once encoded', head: ['field', 'bytes', 'needed', 'bytes encoded'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# load (ld): objects held, finds, identity, the object graph, the tree
# ---------------------------------------------------------------------------

LD_JS = r"""
  var LD_VIEW = {};
  function ldCompute(view, inst, opts) { return eaRun(LD_VIEW[view], inst, opts); }
  function ldStatements(st, rows) { return eaPlural(st, 'statement', 'statements') + ', ' + eaPlural(rows, 'row', 'rows'); }
"""

LD_VIEW_JS = {}

LD_VIEW_JS["instances"] = r"""
  LD_VIEW.instances = function (inst) {
    var t = BigInt(inst.tables.length), r = 0n, rows = [], big = inst.tables[0];
    inst.tables.forEach(function (x) {
      r += x.rows.n;
      if (x.rows.n > big.rows.n) big = x;
      rows.push([x.table, eaInt(x.rows.n)]);
    });
    return {
      tiles: { ldTables: eaInt(t), ldRows: eaInt(r), ldRowObjects: eaInt(r), ldTableObjects: eaInt(t),
        ldLargest: big.table + ' ' + eaInt(big.rows.n) },
      status: 'Objects, not memory, and every row loaded, which neither pattern requires.',
      table: { caption: 'Each table and its rows', head: ['table', 'rows'], rows: rows }
    };
  };
"""

LD_VIEW_JS["finds"] = r"""
  LD_VIEW.finds = function (inst) {
    var K = inst.wanted.n, B = inst.broad.n, b = inst.batch.n, L_ = inst.latencyMs, r = inst.rowMs;
    if (B < K) eaRefuse('The broad query returns at least the rows you want: broad is ' + eaInt(B) + ' and wanted is ' + eaInt(K));
    var bs = (K + b - 1n) / b;
    var keyed = Rmul(R(K), Radd(L_, r)), broad = Radd(L_, Rmul(R(B), r)), batched = Radd(Rmul(R(bs), L_), Rmul(R(K), r));
    return {
      tiles: { ldKeyedStatements: eaInt(K), ldKeyedMs: eaNum(keyed), ldBroadRows: eaInt(B), ldBroadMs: eaNum(broad),
        ldBatchStatements: eaInt(bs), ldBatchMs: eaNum(batched), ldUnneeded: eaInt(B - K) },
      status: 'The latency and the time a row are the lesson\'s figures, not a measurement of your system: '
        + 'each statement waits once, and each row it returns costs its time.',
      table: { caption: 'The three ways to fetch the rows', head: ['way', 'statements', 'rows', 'time (ms)'],
        rows: [['one find a row', eaInt(K), eaInt(K), eaNum(keyed)], ['one broad query', '1', eaInt(B), eaNum(broad)],
          ['finds in batches of ' + eaInt(b), eaInt(bs), eaInt(K), eaNum(batched)]] }
    };
  };
"""

LD_VIEW_JS["identity"] = r"""
  LD_VIEW.identity = function (inst) {
    var seen = {}, order = [], rows = [];
    inst.finds.forEach(function (f, i) {
      var key = f['class'] + ' ' + f.id;
      if (!Object.prototype.hasOwnProperty.call(seen, key)) { seen[key] = 0; order.push(key); }
      seen[key] += 1;
      rows.push([String(i + 1), f['class'], f.id, seen[key] === 1 ? 'first find' : 'found before (' + eaInt(seen[key]) + ' finds)']);
    });
    var shared = order.filter(function (k) { return seen[k] > 1; }).map(function (k) { return k + ' ×' + seen[k]; });
    var n = inst.finds.length, d = order.length;
    return {
      tiles: { ldFinds: eaInt(n), ldDistinct: eaInt(d), ldDuplicates: eaInt(n - d), ldShared: eaNames(shared) },
      status: 'Without an Identity Map each find loads its own copy, so ' + eaPlural(n - d, 'find makes', 'finds make')
        + ' a second copy of an object already loaded; with one, those finds return the object already in memory.',
      table: { caption: 'Each find, in order', head: ['find', 'class', 'id', 'seen'], rows: rows }
    };
  };
"""

LD_VIEW_JS["graph"] = r"""
  LD_VIEW.graph = function (inst) {
    var N = BigInt(inst.parents.length), all = 0n, t = 0n, cu = 0n, joined = 0n, b = inst.batch.n, rows = [];
    inst.parents.forEach(function (p) {
      var c = p.children.n;
      all += c;
      joined += c > 1n ? c : 1n;
      if (p.used === 'yes') { t += 1n; cu += c; }
      rows.push([p.parent, eaInt(c), p.used]);
    });
    return {
      tiles: { ldLazy: ldStatements(1n + t, N + cu), ldBatched: ldStatements(1n + (t + b - 1n) / b, N + cu),
        ldTwoQueries: ldStatements(2n, N + all), ldJoin: ldStatements(1n, joined) },
      status: eaInt(t) + ' of ' + eaPlural(N, 'parent is', 'parents are') + ' used. Statements and rows are counted, not timed.',
      table: { caption: 'Each parent, its children, and whether it is used', head: ['parent', 'children', 'used'], rows: rows }
    };
  };
"""

LD_VIEW_JS["tree"] = r"""
  LD_VIEW.tree = function (inst) {
    var parent = {}, roots = [], rows = [], depth = {}, D = 0;
    inst.nodes.forEach(function (x) { parent[x.node] = x.parent; if (x.parent === '-') roots.push(x.node); });
    inst.nodes.forEach(function (x) {
      if (x.parent !== '-' && !Object.prototype.hasOwnProperty.call(parent, x.parent)) eaRefuse(x.node + '\'s parent ' + x.parent + ' is not a node');
    });
    if (roots.length !== 1) eaRefuse(roots.length ? 'The tree has ' + roots.length + ' roots (' + eaNames(roots) + '); this lab takes exactly one'
      : 'The tree has no root: give one node the parent -');
    inst.nodes.forEach(function (x) {
      var d = 1, at = x.node, path = [at];
      while (parent[at] !== '-') {
        at = parent[at];
        if (path.indexOf(at) >= 0) eaRefuse('The parents form a cycle: ' + path.slice(path.indexOf(at)).concat([at]).join(' → '));
        path.push(at);
        d += 1;
      }
      depth[x.node] = d;
      if (d > D) D = d;
      rows.push([x.node, x.parent, String(d)]);
    });
    var n = inst.nodes.length;
    return {
      tiles: { ldNodes: eaInt(n), ldDepth: eaInt(D), ldPerNode: eaInt(1 + n), ldPerLevel: eaInt(D + 1), ldLob: '1' },
      status: 'Queries are counted, not timed: one query a node reads that node\'s children, one a level reads a whole level, '
        + 'and a Serialized LOB reads the whole tree from one column.',
      table: { caption: 'Each node, its parent, and its depth', head: ['node', 'parent', 'depth'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# uow (uw): what a Unit of Work writes at commit, and in what order
# ---------------------------------------------------------------------------

UW_JS = r"""
  var UW_VIEW = {};
  function uwCompute(view, inst, opts) { return eaRun(UW_VIEW[view], inst, opts); }
"""

UW_VIEW_JS = {}

UW_VIEW_JS["commit"] = r"""
  UW_VIEW.commit = function (inst) {
    var state = {}, made = {}, changed = {}, first = [], imm = 0, rows = [];
    inst.script.forEach(function (r, i) {
      var x = r.object, st = state[x], at = 'Script, record ' + (i + 1) + ': ';
      if (first.indexOf(x) < 0) first.push(x);
      if (st === 'deleted') eaRefuse(at + r.op + ' of ' + x + ' after its delete');
      if (r.op === 'load') {
        if (st === 'new') eaRefuse(at + 'load of ' + x + ', which the script created');
        state[x] = st || 'loaded';
      } else if (r.op === 'new') {
        if (st) eaRefuse(at + 'new ' + x + ', which the script has already loaded or created');
        state[x] = 'new'; made[x] = true; imm += 1;
      } else {
        if (!st) eaRefuse(at + r.op + ' of ' + x + ', which the script has neither loaded nor created');
        imm += 1;
        if (r.op === 'change') changed[x] = true; else state[x] = 'deleted';
      }
      rows.push([String(i + 1), r.op, x, r.op === 'load' ? '0' : '1']);
    });
    var ins = [], upd = [], del = [], clean = [];
    first.forEach(function (x) {
      if (state[x] === 'deleted') { if (!made[x]) del.push(x); }
      else if (state[x] === 'new') ins.push(x);
      else if (changed[x]) upd.push(x);
      else clean.push(x);
    });
    var writes = ins.map(function (x) { return 'INSERT ' + x; }).concat(upd.map(function (x) { return 'UPDATE ' + x; }),
      del.map(function (x) { return 'DELETE ' + x; }));
    var c = writes.length;
    return {
      tiles: { uwImmediate: eaInt(imm), uwCommit: eaInt(c),
        uwSaved: eaInt(imm - c) + ' (' + (imm ? eaPct(R(imm - c, imm)) : EA_DASH) + ')',
        uwWrites: writes.length ? writes.join('; ') : 'none', uwClean: eaCount(clean) },
      status: 'Every new, change and delete is one write when each is written at once; at commit an object is written once, '
        + 'and an object created and deleted in the script is not written at all. '
        + (imm ? '' : 'Nothing is written either way, so there is no share saved. ')
        + 'Writes in this order can still break a foreign key; the order view is lesson 4.4\'s.',
      table: { caption: 'Each step of the script', head: ['step', 'op', 'object', 'written at once'], rows: rows }
    };
  };
"""

UW_VIEW_JS["order"] = r"""
  UW_VIEW.order = function (inst) {
    var nodes = [], deps = {}, seen = {}, rows = [];
    inst.keys.forEach(function (k, i) {
      if (k.child === k.parent) eaRefuse('Keys, record ' + (i + 1) + ': ' + k.child + ' refers to itself; a table that refers to itself needs its rows ordered, which this lab does not do');
      var key = k.child + ' ' + k.parent;
      if (seen[key]) eaRefuse('Keys lists ' + k.child + ', ' + k.parent + ' twice');
      seen[key] = true;
      [k.child, k.parent].forEach(function (n) { if (!deps[n]) { deps[n] = []; nodes.push(n); } });
      deps[k.child].push(k.parent);
    });
    nodes = eaSort(nodes);
    var done = {}, order = [];
    while (order.length < nodes.length) {
      var ready = nodes.filter(function (n) { return !done[n] && deps[n].every(function (p) { return done[p]; }); });
      if (!ready.length) {
        /* walk parent links among the tables left until one repeats: that is a cycle */
        var at = nodes.filter(function (n) { return !done[n]; })[0], path = [];
        while (path.indexOf(at) < 0) {
          path.push(at);
          at = eaSort(deps[at].filter(function (p) { return !done[p]; }))[0];
        }
        eaRefuse('The keys form a cycle: ' + path.slice(path.indexOf(at)).concat([at]).join(' → ') + '; no order puts every parent first');
      }
      done[ready[0]] = true;
      order.push(ready[0]);
      rows.push([String(order.length), ready[0], eaNames(eaSort(deps[ready[0]]))]);
    }
    var broken = EA_DASH, status = 'Ties are broken alphabetically, so this is one valid order of several.';
    if (inst.as.length) {
      var pos = {};
      inst.as.forEach(function (n, i) {
        if (!deps[n]) eaRefuse('The order given names ' + n + ', which no key has');
        pos[n] = i;
      });
      var missing = nodes.filter(function (n) { return pos[n] === undefined; });
      if (missing.length) eaRefuse('The order given misses ' + eaNames(missing) + '; it names every table in the keys once');
      broken = eaCount(inst.keys.filter(function (k) { return pos[k.child] < pos[k.parent]; })
        .map(function (k) { return k.child + ' before ' + k.parent; }));
    } else {
      status += ' No order is given, so there is nothing to check against the keys.';
    }
    var rev = order.slice().reverse();
    return {
      tiles: { uwInsertOrder: order.join(', '), uwDeleteOrder: rev.join(', '), uwBroken: broken },
      status: status,
      table: { caption: 'The insert order, step by step', head: ['step', 'table', 'its parents'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# the views: inputs, tiles, the rules the page states, and the Python checks
# ---------------------------------------------------------------------------

_POINTS_LOAD = ea.rec("Measurements (system, users, response time in ms)",
                      [("system", ea.NAME), ("users", ea.whole(1)), ("ms", ea.num(gt=0))])
_POINTS_SCALE = ea.rec("Measurements (system, servers, throughput in tps)",
                       [("system", ea.NAME), ("servers", ea.whole(1, SEARCH)), ("tps", ea.num(lo=0))])


def _systems(points, xk, what):
    by, order = {}, []
    for p in points:
        if p["system"] not in by:
            by[p["system"]] = []
            order.append(p["system"])
        if p[xk] in by[p["system"]]:
            raise ValueError("System %s is measured at %s %s twice" % (p["system"], ea.grp(p[xk]), what))
        by[p["system"]].append(p[xk])
    return order


def _check_load(inst, fixed):
    _systems(inst["points"], "users", "users")


def _check_scale(inst, fixed):
    _systems(inst["points"], "servers", fixed["unit"] + "s")


def _check_boundary(inst, fixed):
    named = {c["caller"] for c in inst["calls"]} | {c["callee"] for c in inst["calls"]}
    for a, _b in inst["nodes"]:
        if a not in named:
            raise ValueError("Nodes names %s, which no call has" % a)


def _check_finds(inst, fixed):
    if inst["broad"] < inst["wanted"]:
        raise ValueError("The broad query returns at least the rows you want: broad is %s and wanted is %s"
                         % (ea.grp(inst["broad"]), ea.grp(inst["wanted"])))


def tree_check(rows, key, what_root, what_cycle):
    """One root, every parent a node, no cycle (load/tree, inherit/tables)."""
    parent = {r[key]: r["parent"] for r in rows}
    for r in rows:
        if r["parent"] != "-" and r["parent"] not in parent:
            raise ValueError("%s's parent %s is not %s" % (r[key], r["parent"], what_root))
    roots = [r[key] for r in rows if r["parent"] == "-"]
    if len(roots) != 1:
        raise ValueError(("The %s has %d roots (%s); this lab takes exactly one" % (what_cycle, len(roots), ", ".join(roots)))
                         if roots else "The %s has no root: give one %s the parent -" % (what_cycle, key))
    for r in rows:
        at, path = r[key], [r[key]]
        while parent[at] != "-":
            at = parent[at]
            if at in path:
                raise ValueError("The parents form a cycle: %s" % " → ".join(path[path.index(at):] + [at]))
            path.append(at)
    return parent


def _check_tree(inst, fixed):
    tree_check(inst["nodes"], "node", "a node", "tree")



def _check_commit(inst, fixed):
    state = {}
    for i, r in enumerate(inst["script"]):
        x, op, st, at = r["object"], r["op"], state.get(r["object"]), "Script, record %d: " % (i + 1)
        if st == "deleted":
            raise ValueError("%s%s of %s after its delete" % (at, op, x))
        if op == "load":
            if st == "new":
                raise ValueError("%sload of %s, which the script created" % (at, x))
            state[x] = st or "loaded"
        elif op == "new":
            if st:
                raise ValueError("%snew %s, which the script has already loaded or created" % (at, x))
            state[x] = "new"
        else:
            if not st:
                raise ValueError("%s%s of %s, which the script has neither loaded nor created" % (at, op, x))
            if op == "delete":
                state[x] = "deleted"


def _check_order(inst, fixed):
    deps, seen = {}, set()
    for i, k in enumerate(inst["keys"]):
        c, p = k["child"], k["parent"]
        if c == p:
            raise ValueError("Keys, record %d: %s refers to itself; a table that refers to itself needs its rows "
                             "ordered, which this lab does not do" % (i + 1, c))
        if (c, p) in seen:
            raise ValueError("Keys lists %s, %s twice" % (c, p))
        seen.add((c, p))
        deps.setdefault(c, []).append(p)
        deps.setdefault(p, [])
    nodes, done = sorted(deps), set()
    while len(done) < len(nodes):
        ready = [n for n in nodes if n not in done and all(p in done for p in deps[n])]
        if not ready:
            at, path = [n for n in nodes if n not in done][0], []
            while at not in path:
                path.append(at)
                at = sorted(p for p in deps[at] if p not in done)[0]
            raise ValueError("The keys form a cycle: %s; no order puts every parent first"
                             % " → ".join(path[path.index(at):] + [at]))
        done.add(ready[0])
    if inst["as"]:
        for n in inst["as"]:
            if n not in deps:
                raise ValueError("The order given names %s, which no key has" % n)
        missing = [n for n in nodes if n not in inst["as"]]
        if missing:
            raise ValueError("The order given misses %s; it names every table in the keys once" % ", ".join(missing))


_RULES = {
    ("perf", "load"): "Each system's measurements are sorted by load. Its change per user is (last response time − "
                      "first) / (last users − first); its ratio is the last response time over the first. Its "
                      "response at the load given is read on a straight line between the two measurements either "
                      "side; outside its measured loads the lab says so and does not extrapolate.",
    ("perf", "scale"): "A system's rate is (throughput at its last measurement − at its first) / (the difference in "
                       "servers). Its projection at n is the measured throughput where n was measured, and otherwise "
                       "the straight line through its first and last measurements. The crossover is the first n from "
                       "1 up at which two systems' projections are equal or have changed order; the servers needed "
                       "is the least n whose projection reaches the throughput needed. Both searches stop at 10,000.",
    ("remote", "boundary"): "A call is remote when its caller and callee are on different nodes; a class no node is "
                            "given for runs on main. Time is remote calls × the remote time plus local calls × the "
                            "local time, in microseconds.",
    ("remote", "calls"): "Each record is one coarse-grained call that does the work of the given number of "
                         "fine-grained ones. Fine-grained: every call waits the latency and does its work. "
                         "Coarse-grained: one wait a coarse call, and the same work.",
    ("remote", "payload"): "The getters make one call a needed field; the DTO is one call carrying every field. A "
                           "call's time is the latency plus its bytes × the factor / the bytes a millisecond. The "
                           "spare bytes are the round trips the DTO saves (needed fields − 1) × latency × bytes a "
                           "millisecond.",
    ("load", "instances"): "One object a row, as a Domain Model or Row Data Gateway holds them; one object a table, "
                           "as Table Module holds them. The largest table is the first with the most rows.",
    ("load", "finds"): "One find a row: a statement for each wanted row. One broad query: one statement returning "
                       "every row it matches. Batches: ⌈wanted / batch⌉ statements returning the wanted rows. Each "
                       "statement costs the latency, each row its time.",
    ("load", "identity"): "A find is a class and an id, in the order the finds happen. An object found before is a "
                          "duplicate: without an Identity Map, a second copy.",
    ("load", "graph"): "Lazy load: one query for the parents, then one for each used parent's children. In batches: "
                       "the used parents' children, the batch size of parents at a time. Two queries: the parents, "
                       "then every child. One join: a left outer join, one statement, one row a child, and a parent "
                       "with no children still one row.",
    ("load", "tree"): "The root is at depth 1. A query a node: one for the root, then one for each node's children, "
                      "a leaf's finding none (1 + nodes queries). A query a level: one for each level, the last "
                      "finding the level below the leaves empty (depth + 1 queries). A Serialized LOB reads the tree "
                      "from one column (1 query). Both counts include the queries that come back empty.",
    ("uow", "commit"): "Written at once, every new, change and delete is a write. At commit: created and deleted, "
                       "nothing; created, one INSERT; loaded and deleted, one DELETE; loaded and changed (any number "
                       "of times), one UPDATE; loaded only, nothing (clean). INSERTs come first, then UPDATEs, then "
                       "DELETEs, each in the order the script first names the object.",
    ("uow", "order"): "Each key is child, parent: the child's table holds a key to the parent's. Inserts go parents "
                      "first, taking the alphabetically first table that is ready at each step; deletes go in the "
                      "reverse order. A key breaks the order given when its child comes before its parent.",
}

_PZ_UNIT = "server"

# view: (fields, tiles, family, check)
VIEWS = {
    "perf": {
        "load": ([("points", _POINTS_LOAD, None), ("users", ea.field("Load to read it at (users)", ea.whole(1)), None)],
                 [("Change in response time a user", "pzPerUser"), ("Last response time over first", "pzRatio"),
                  ("Response time at the load given", "pzAt")], 2, _check_load),
        "scale": ([("points", _POINTS_SCALE, None),
                   ("need", ea.field("Throughput needed (tps)", ea.num(gt=0)), None),
                   ("at", ea.field("Servers to project at", ea.whole(1, SEARCH)), None)],
                  [("Throughput a server, first measurement", "pzEfficiency"),
                   ("Throughput added a server", "pzMarginal"), ("Where the projections meet or cross", "pzCrossover"),
                   ("Servers needed", "pzNeed"), ("Projected throughput at the count given", "pzAt")], 2, _check_scale),
    },
    "remote": {
        "boundary": ([("calls", ea.rec("Calls (caller, callee, how many)",
                                       [("caller", ea.NAME), ("callee", ea.NAME), ("count", ea.whole(0))]), None),
                      ("nodes", ea.pairs("Nodes (class=node; a class not listed runs on main)", "class=node"), ""),
                      ("remoteUs", ea.field("Time of a remote call (µs)", ea.num(gt=0)), None),
                      ("localUs", ea.field("Time of a local call (µs)", ea.num(gt=0)), None)],
                     [("Calls", "rrCalls"), ("Remote calls", "rrRemote"), ("Time (µs)", "rrTime"),
                      ("Share of the time in remote calls", "rrShare"),
                      ("Time with every class on one node (µs)", "rrOneNode"), ("Time against one node", "rrRatio")],
                     1, _check_boundary),
        "calls": ([("ops", ea.rec("Coarse-grained calls (operation, fine-grained calls it replaces)",
                                  [("operation", ea.NAME), ("fine", ea.whole(1))], unique=True), None),
                   ("latencyMs", ea.field("Latency of a round trip (ms)", ea.num(gt=0)), None),
                   ("workMs", ea.field("Work in a fine-grained call (ms)", ea.num(lo=0)), None)],
                  [("Round trips, %(fine)s", "rrFineTrips"), ("Round trips, %(coarse)s", "rrCoarseTrips"),
                   ("Time, %(fine)s (ms)", "rrFineMs"), ("Time, %(coarse)s (ms)", "rrCoarseMs"),
                   ("Share of the time of the %(fine)s spent waiting", "rrLatencyShare"),
                   ("Time of the %(fine)s over the %(coarse)s", "rrSpeedup")], 2, None),
        "payload": ([("fields", ea.rec("Fields (field, bytes, needed: yes or no)",
                                       [("field", ea.NAME), ("bytes", ea.whole(0)), ("needed", ea.YESNO)], unique=True),
                      None),
                     ("latencyMs", ea.field("Latency of a round trip (ms)", ea.num(gt=0)), None),
                     ("bytesPerMs", ea.field("Bytes sent a millisecond", ea.num(gt=0)), None),
                     ("factor", ea.field("Encoding factor (encoded size over raw)", ea.num(gt=0)), None)],
                    [("Calls, one getter a needed field", "rrGetterCalls"), ("Time, the getters (ms)", "rrGetterMs"),
                     ("Bytes in the DTO", "rrDtoBytes"), ("Time, one DTO (ms)", "rrDtoMs"),
                     ("Bytes the DTO carries that are not needed", "rrExtraBytes"),
                     ("Bytes the saved round trips could have carried", "rrSpare")], 2, None),
    },
    "load": {
        "instances": ([("tables", ea.rec("Tables (table, rows)", [("table", ea.NAME), ("rows", ea.whole(0))], unique=True),
                        None)],
                      [("Tables", "ldTables"), ("Rows", "ldRows"), ("Objects, one a row", "ldRowObjects"),
                       ("Objects, one a table", "ldTableObjects"), ("Largest table, and its rows", "ldLargest")], 1, None),
        "finds": ([("wanted", ea.field("Rows wanted", ea.whole(1)), None),
                   ("broad", ea.field("Rows the broad query returns", ea.whole(1)), None),
                   ("batch", ea.field("Rows in a batch", ea.whole(1)), None),
                   ("latencyMs", ea.field("Latency of a statement (ms)", ea.num(gt=0)), None),
                   ("rowMs", ea.field("Time a row (ms)", ea.num(lo=0)), None)],
                  [("Statements, one find a row", "ldKeyedStatements"), ("Time, one find a row (ms)", "ldKeyedMs"),
                   ("Rows, one broad query", "ldBroadRows"), ("Time, one broad query (ms)", "ldBroadMs"),
                   ("Statements, finds in batches", "ldBatchStatements"), ("Time, finds in batches (ms)", "ldBatchMs"),
                   ("Rows the broad query returns that are not wanted", "ldUnneeded")], 2, _check_finds),
        "identity": ([("finds", ea.rec("Finds, in order (class, id)", [("class", ea.NAME), ("id", ea.NAME)]), None)],
                     [("Finds", "ldFinds"), ("Distinct objects", "ldDistinct"),
                      ("Finds of an object already found", "ldDuplicates"), ("Found more than once", "ldShared")], 1,
                     None),
        "graph": ([("parents", ea.rec("Parents (parent, children, used: yes or no)",
                                      [("parent", ea.NAME), ("children", ea.whole(0)), ("used", ea.YESNO)], unique=True),
                    None),
                   ("batch", ea.field("Parents in a batch", ea.whole(1)), None)],
                  [("Lazy load, a query a used parent", "ldLazy"), ("Lazy load in batches", "ldBatched"),
                   ("Two queries, the parents then every child", "ldTwoQueries"), ("One join", "ldJoin")], 1, None),
        "tree": ([("nodes", ea.rec("Nodes (node, parent; - for the root)", [("node", ea.NAME), ("parent", ea.PARENT)],
                                   unique=True), None)],
                 [("Nodes", "ldNodes"), ("Depth (the root is 1)", "ldDepth"),
                  ("Queries, one a node's children", "ldPerNode"), ("Queries, one a level", "ldPerLevel"),
                  ("Queries, the tree in one column", "ldLob")], 1, _check_tree),
    },
    "uow": {
        "commit": ([("script", ea.rec("Script (op: load, new, change or delete; object)",
                                      [("op", ea.word("load", "new", "change", "delete")), ("object", ea.NAME)]), None)],
                   [("Writes, each written at once", "uwImmediate"), ("Writes at commit", "uwCommit"),
                    ("Writes saved", "uwSaved"), ("The writes at commit", "uwWrites"),
                    ("Loaded and never changed", "uwClean")], 1, _check_commit),
        "order": ([("keys", ea.rec("Foreign keys (child table, parent table)", [("child", ea.NAME), ("parent", ea.NAME)]),
                    None),
                   ("as", dict(what="An order to check (tables, space-separated; optional)", control="text",
                               kind="list", lo=0, hi=ea.MAX_RECORDS, things="tables", each={"kind": "name"}), "")],
                  [("Insert order, parents first", "uwInsertOrder"), ("Delete order, children first", "uwDeleteOrder"),
                   ("Keys the order given breaks", "uwBroken")], 1, _check_order),
    },
}

SUBTITLES = {
    ("perf", "load"): "response time against load",
    ("perf", "scale"): "throughput against servers",
    ("remote", "boundary"): "calls that cross a node boundary",
    ("remote", "calls"): "fine-grained calls against coarse-grained ones",
    ("remote", "payload"): "getters against one data transfer object",
    ("load", "instances"): "objects held, one a row or one a table",
    ("load", "finds"): "a find a row, one broad query, or batches",
    ("load", "identity"): "finds of an object already loaded",
    ("load", "graph"): "statements and rows to load an object graph",
    ("load", "tree"): "queries to load a tree",
    ("uow", "commit"): "writes at once against writes at commit",
    ("uow", "order"): "the order foreign keys put writes in",
}

TITLES = {"perf": "Performance arithmetic", "remote": "Remote calls", "load": "Loading from the database",
          "uow": "Unit of Work"}

PREFIX = {"perf": ("pz", "pzCompute", PZ_JS, PZ_VIEW_JS), "remote": ("rr", "rrCompute", RR_JS, RR_VIEW_JS),
          "load": ("ld", "ldCompute", LD_JS, LD_VIEW_JS), "uow": ("uw", "uwCompute", UW_JS, UW_VIEW_JS)}


def _options(cfg, kit, mode, view, tiles):
    """(fixed opts, extra cfg keys, tiles with their labels filled in)."""
    if (mode, view) == ("perf", "scale"):
        unit = cfg.get("unit", _PZ_UNIT)
        if not isinstance(unit, str) or not re.fullmatch(r"[a-z]{1,20}", unit):
            raise ValueError("%s: cfg['unit'] is %r; it is one lower-case word" % (kit, unit))
        cap = unit[:1].upper() + unit[1:]
        labels = {"pzEfficiency": "Throughput a %s, first measurement" % unit,
                  "pzMarginal": "Throughput added a %s" % unit, "pzNeed": "%ss needed" % cap,
                  "pzAt": "Projected throughput at the %s count given" % unit}
        return {"unit": unit}, ["unit"], [(labels.get(cid, label), cid) for label, cid in tiles]
    if (mode, view) == ("remote", "calls"):
        words = {"fine": ea.plain(cfg, kit, "fine_label", "fine-grained calls", limit=40),
                 "coarse": ea.plain(cfg, kit, "coarse_label", "coarse-grained calls", limit=40)}
        return {}, ["fine_label", "coarse_label"], [(label % words, cid) for label, cid in tiles]
    return {}, [], tiles


def _intro(mode, view, family):
    if family == 1:
        return ea.FAMILY[1] + " The lab counts; it runs nothing, and no count is a verdict."
    return ea.FAMILY[2] + " Every figure is the lesson's; the lab does the arithmetic and measures nothing."


def view_lab(cfg, mode, table, titles, subtitles, prefixes, rules, kit_name=KIT, options=None):
    """One mode's lab, from that module's tables (eakit.py and eakit_b.py share this)."""
    views = table[mode]
    order = tuple(views)
    view = cfg.get("view", order[0])
    kit = "%s/%s/%s" % (kit_name, mode, view)
    if view not in views:
        raise ValueError("%s/%s: unknown view %r; the views are %s" % (kit_name, mode, view, ", ".join(order)))
    fields, tiles, family, check = views[view]
    fixed, keys, tiles = (options or _options)(cfg, kit, mode, view, tiles)
    prefix, fn, base, view_js = prefixes[mode]
    return ea.build_lab(cfg, kit=kit, prefix=prefix, view=view, fields=fields, tiles=tiles, fn=fn,
                        js=base + view_js[view], fixed=fixed, title=titles[mode], subtitle=subtitles[(mode, view)],
                        family=family, intro=_intro(mode, view, family), rules=rules[(mode, view)],
                        extra_keys=keys, check=check)


MODES = ("perf", "remote", "load", "uow", "inherit", "lock", "session", "money")


def eakit_lab(cfg):
    """The Enterprise Patterns kit. `cfg["mode"]` chooses the mode, `cfg["view"]` the view; an unknown one raises."""
    cfg = cfg or {}
    mode = cfg.get("mode")
    if mode in VIEWS:
        return view_lab(cfg, mode, VIEWS, TITLES, SUBTITLES, PREFIX, _RULES)
    if mode not in MODES:
        raise ValueError("eakit_lab: unknown mode %r; the eight modes are %s" % (mode, ", ".join(MODES)))
    from . import eakit_b
    return eakit_b.mode_lab(cfg, mode)


__all__ = ["eakit_lab", "VIEWS", "MODES", "view_lab", "tree_check"]
