"""eakit_b -- the inherit, lock, session and money modes of the Enterprise Patterns kit.

Specified in docs/enterprise-patterns/PLAN.md section D.1; the entry point and
the perf, remote, load and uow modes are in eakit.py, the shared printing,
parsing and wiring in eakit_core.py. Each mode has one base block (its
<xx>Compute) and one block per view; a page ships the base block and its own
view's block only.

  inherit  (ih)  tables                family 1
  lock     (ol)  reads, timeline       family 1
  session  (sn)  objects, state        family 2
  money    (mn)  allocate              family 2
"""

from . import eakit_core as ea
from .eakit import tree_check, view_lab

# ---------------------------------------------------------------------------
# inherit (ih): the three ways to map a class hierarchy to tables
# ---------------------------------------------------------------------------

IH_JS = r"""
  var IH_VIEW = {};
  function ihCompute(view, inst, opts) { return eaRun(IH_VIEW[view], inst, opts); }
"""

IH_VIEW_JS = {}

IH_VIEW_JS["tables"] = r"""
  IH_VIEW.tables = function (inst) {
    var par = {}, fld = {}, con = {}, cls = [], roots = [], rows = [];
    var has = function (c) { return Object.prototype.hasOwnProperty.call(par, c); };
    inst.classes.forEach(function (c) {
      var k = c['class'];
      par[k] = c.parent; fld[k] = c.fields.n; con[k] = c.concrete === 'yes'; cls.push(k);
      if (c.parent === '-') roots.push(k);
    });
    cls.forEach(function (c) { if (par[c] !== '-' && !has(par[c])) eaRefuse(c + '\'s parent ' + par[c] + ' is not a class'); });
    if (roots.length !== 1) eaRefuse(roots.length ? 'The hierarchy has ' + roots.length + ' roots (' + eaNames(roots) + '); this lab takes exactly one'
      : 'The hierarchy has no root: give one class the parent -');
    var chain = function (c) {
      var out = [c];
      while (par[c] !== '-') {
        c = par[c];
        if (out.indexOf(c) >= 0) eaRefuse('The parents form a cycle: ' + out.slice(out.indexOf(c)).concat([c]).join(' → '));
        out.push(c);
      }
      return out;
    };
    cls.forEach(chain);
    var subtree = function (c) { return cls.filter(function (x) { return chain(x).indexOf(c) >= 0; }); };
    var sumOf = function (list) { var s = 0n; list.forEach(function (c) { s += fld[c]; }); return s; };
    [['load', 'The class to load'], ['find', 'The class to find'], ['alter', 'The class to add a field to']].forEach(function (k) {
      if (!has(inst[k[0]])) eaRefuse(k[1] + ', ' + inst[k[0]] + ', is not one of the classes');
    });
    if (!con[inst.load]) eaRefuse('The class to load, ' + inst.load + ', is not concrete: only a concrete class has objects to load');
    var concretes = cls.filter(function (c) { return con[c]; }), allf = sumOf(cls), cCols = 0n, kCols = 0n;
    cls.forEach(function (c) {
      cCols += 1n + fld[c];
      if (con[c]) kCols += 1n + sumOf(chain(c));
      rows.push([c, par[c], eaInt(fld[c]), con[c] ? 'yes' : 'no', eaInt(sumOf(chain(c))), String(chain(c).length)]);
    });
    var three = function (a, b, c) { return eaInt(a) + ', ' + eaInt(b) + ', ' + eaInt(c); };
    var conIn = function (list) { return list.filter(function (c) { return con[c]; }).length; };
    var findUp = chain(inst.find).concat(subtree(inst.find)).filter(function (c, i, all) { return all.indexOf(c) === i; });
    return {
      tiles: { ihTables: three(1, cls.length, concretes.length), ihColumns: three(2n + allf, cCols, kCols),
        ihEmpty: eaInt(allf - sumOf(chain(inst.load))), ihLoad: three(1, chain(inst.load).length, 1),
        ihFind: three(1, findUp.length, conIn(subtree(inst.find))), ihAlter: three(1, 1, conIn(subtree(inst.alter))) },
      status: 'Each three-part tile is single table, class table, concrete table, in that order. Every table has a key column, '
        + 'and the single table a type column as well. Tables and columns are counted, not timed.',
      table: { caption: 'Each class, its own fields and its chain', head: ['class', 'parent', 'own fields', 'concrete', 'fields with its ancestors', 'depth'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# lock (ol): inconsistent reads, and a timeline under three schemes
# ---------------------------------------------------------------------------

OL_JS = r"""
  var OL_VIEW = {};
  function olCompute(view, inst, opts) { return eaRun(OL_VIEW[view], inst, opts); }
"""

OL_VIEW_JS = {}

OL_VIEW_JS["reads"] = r"""
  OL_VIEW.reads = function (inst) {
    var seen = 0n, B = 0n, A = 0n, stale = [], fresh = [], rows = [];
    inst.items.forEach(function (x) {
      var b = x.before.n, a = x.after.n, early = x.read === 'before', v = early ? b : a;
      seen += v; B += b; A += a;
      if (b !== a) (early ? stale : fresh).push(x.change);
      rows.push([x.item, eaInt(b), eaInt(a), x.read, x.change, eaInt(v), b === a ? 'unchanged' : (early ? 'stale' : 'fresh')]);
    });
    var cons, level;
    if (!stale.length) cons = 'yes: the state after the commit';
    else if (!fresh.length) cons = 'yes: the state before the commit';
    else if (seen === B || seen === A) cons = 'no, though ' + eaInt(seen) + ' equals the total ' + (seen === B ? 'before' : 'after') + ' the commit';
    else if (A === B) cons = 'no: ' + eaInt(seen) + ' is not ' + eaInt(B) + ', before or after';
    else cons = 'no: ' + eaInt(seen) + ' is neither ' + eaInt(B) + ' nor ' + eaInt(A);
    if (!stale.length || !fresh.length) level = 'none needed: no read straddles the commit';
    else if (stale.every(function (c) { return c === 'insert'; })) level = 'repeatable read allows it (a phantom); serializable prevents it';
    else level = 'read committed allows it (an unrepeatable read); repeatable read prevents it';
    return {
      tiles: { olSeen: eaInt(seen), olBefore: eaInt(B), olAfter: eaInt(A), olConsistent: cons, olLevel: level },
      status: 'One writer commits once; the reader reads each item on one side of that commit. A read before the commit of an item '
        + 'the commit changes is stale, and a read after it fresh: ' + eaPlural(stale.length, 'stale read', 'stale reads') + ', '
        + eaPlural(fresh.length, 'fresh read', 'fresh reads') + '. The levels are the four standard ones Chapter 5 describes, '
        + 'and a database\'s own implementation of each can be stronger.',
      table: { caption: 'Each item, and what the reader saw', head: ['item', 'before', 'after', 'read', 'change', 'seen', 'read was'], rows: rows }
    };
  };
"""

OL_VIEW_JS["timeline"] = r"""
  OL_VIEW.timeline = function (inst) {
    var scheme = inst.scheme, checkReads = inst.checkReads === 'yes', grp = {}, touched = {}, last = -1n;
    var own = function (o, k) { return Object.prototype.hasOwnProperty.call(o, k); };
    inst.events.forEach(function (e, i) {
      var at = 'Events, record ' + (i + 1) + ': ';
      if (e.minute.n < last) eaRefuse(at + 'minute ' + eaInt(e.minute.n) + ' comes before minute ' + eaInt(last) + ' of the record before it; the minutes must not decrease');
      last = e.minute.n;
      if (e.action === 'commit' && e.record !== '-') eaRefuse(at + 'a commit names no record; write - for it');
      if (e.action !== 'commit' && e.record === '-') eaRefuse(at + 'a ' + e.action + ' needs a record, not -');
      if (e.action !== 'commit') touched[e.record] = true;
    });
    inst.groups.forEach(function (p) {
      if (!touched[p.a]) eaRefuse('Groups names ' + p.a + ', which no event reads or edits');
      grp[p.a] = p.b;
    });
    var G = function (r) { return own(grp, r) ? grp[r] : r; };
    /* the groups each session edits anywhere in the timeline: under pessimistic
       locking it takes their locks when it first loads them (D.1) */
    var willEdit = {};
    inst.events.forEach(function (e) { if (e.action === 'edit') willEdit[e.session + ' ' + G(e.record)] = true; });
    var version = {}, locks = {}, start = {}, ended = {}, failed = {}, seenv = {}, edits = {}, reads = {}, sessions = [];
    var committed = [], conflicts = [], refused = [], skipped = [], lost = 0n, redo = 0n, peak = 0, rows = [];
    var ver = function (g) { return own(version, g) ? version[g] : 0; };
    var release = function (s) { Object.keys(locks).forEach(function (g) { if (locks[g] === s) delete locks[g]; }); };
    inst.events.forEach(function (e, i) {
      var s = e.session, m = e.minute.n, a = e.action, g = a === 'commit' ? '' : G(e.record), what;
      var row = function (w) { rows.push([eaInt(m), s, a, e.record, a === 'commit' ? '' : g, w]); };
      if (failed[s]) { skipped.push(s + ' at minute ' + eaInt(m)); row('skipped'); return; }
      if (ended[s]) eaRefuse('Events, record ' + (i + 1) + ': ' + s + ' acts after it committed');
      if (!own(start, s)) { start[s] = m; seenv[s] = {}; edits[s] = []; reads[s] = []; sessions.push(s); }
      if (a !== 'commit') {
        what = a + ', version ' + ver(g);
        if (scheme === 'pessimistic' && willEdit[s + ' ' + g] && locks[g] !== s) {
          if (own(locks, g)) {
            refused.push(s); failed[s] = true; redo += m - start[s]; release(s); ended[s] = m;
            row('refused: ' + locks[g] + ' holds the lock on ' + g);
            return;
          }
          locks[g] = s;
          peak = Math.max(peak, Object.keys(locks).length);
          what += ', lock taken';
        }
        if (!own(seenv[s], g)) seenv[s][g] = ver(g);
        (a === 'edit' ? edits : reads)[s].push(g);
        row(what);
        return;
      }
      ended[s] = m;
      var mine = edits[s].filter(function (x, j, all) { return all.indexOf(x) === j; });
      if (scheme === 'optimistic') {
        var check = mine.concat(checkReads ? reads[s] : []).filter(function (x, j, all) { return all.indexOf(x) === j; });
        var moved = check.filter(function (x) { return ver(x) !== seenv[s][x]; });
        if (moved.length) {
          conflicts.push(s); failed[s] = true; redo += m - start[s];
          row('conflict: ' + eaNames(moved) + ' changed since ' + s + ' saw ' + (moved.length === 1 ? 'it' : 'them'));
          return;
        }
      }
      var lostHere = scheme === 'none' ? mine.filter(function (x) { return ver(x) !== seenv[s][x]; }) : [];
      lost += BigInt(lostHere.length);
      mine.forEach(function (x) { version[x] = ver(x) + 1; });
      release(s);
      committed.push(s);
      row('commit' + (lostHere.length ? ', overwriting ' + eaNames(lostHere) : ''));
    });
    var open = sessions.filter(function (s) { return !failed[s] && committed.indexOf(s) < 0; });
    var rule = scheme === 'none' ? 'With no control every commit succeeds; a lost update is counted for each group a committing session edited that changed after the session saw it.'
      : (scheme === 'optimistic' ? 'Optimistic: a commit fails, a conflict, when a group the session edited' + (checkReads ? ' or only read' : '') + ' has changed since the session saw it.'
        : 'Pessimistic: a session takes the exclusive write lock on a group when it first loads it for editing, at its first read or edit of a group it edits anywhere in the timeline; taking a lock another session holds is refused at once, and a commit releases the session\'s locks. A read of a group the session never edits takes no lock.');
    return {
      tiles: { olCommitted: eaCount(committed), olConflicts: eaCount(conflicts), olRefused: eaCount(refused),
        olLostUpdates: eaInt(lost), olRedo: eaInt(redo), olPeakLocks: scheme === 'pessimistic' ? eaInt(peak) : EA_DASH },
      status: rule + ' The minutes are the lesson\'s.'
        + (skipped.length ? ' A refused or conflicted session\'s later events are skipped: ' + eaNames(skipped) + '.' : '')
        + (open.length ? ' ' + eaNames(open) + (open.length === 1 ? ' neither commits nor fails' : ' neither commit nor fail') + ' in this timeline.' : '')
        + (checkReads && scheme !== 'optimistic' ? ' Checking reads applies only to the optimistic scheme, so it changes nothing here.' : ''),
      table: { caption: 'Each event, and what the scheme does with it', head: ['minute', 'session', 'action', 'record', 'group', 'what happens'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# session (sn): stateful against stateless objects, and where state lives
# ---------------------------------------------------------------------------

SN_JS = r"""
  var SN_VIEW = {};
  function snCompute(view, inst, opts) { return eaRun(SN_VIEW[view], inst, opts); }
"""

SN_VIEW_JS = {}

SN_VIEW_JS["objects"] = r"""
  SN_VIEW.objects = function (inst) {
    var U = inst.users, s = inst.serviceMs, t = inst.thinkMs;
    if (Rcmp(t, s) < 0) eaRefuse('The time between requests must be at least the service time: it is ' + eaNum(t) + ' ms against ' + eaNum(s) + ' ms');
    return {
      tiles: { snStateful: eaInt(U.n), snStateless: eaNum(Rdiv(Rmul(U, s), t)), snIdle: eaPct(Rsub(R1, Rdiv(s, t))),
        snPerObject: eaNum(Rdiv(t, s)) },
      status: 'An average: a pool sized to it is too small at a peak. The service time and the time between requests are '
        + 'the lesson\'s figures, not a measurement of your system.',
      table: null
    };
  };
"""

SN_VIEW_JS["state"] = r"""
  SN_VIEW.state = function (inst) {
    var U = inst.users.n, B = inst.stateBytes.n, Q = inst.requests.n, id = inst.idBytes.n;
    return {
      tiles: { snWire: eaInt(2n * B), snSessionWire: eaInt(2n * B * Q), snIdOnly: eaInt(id), snMemory: eaInt(U * B), snDatabase: eaInt(2n * B) },
      status: 'The sizes are the lesson\'s figures, not a measurement of your system; compression, partial loading and caching change every figure.',
      table: { caption: 'Bytes for one request, by where the session state lives', head: ['where the state lives', 'on the wire', 'held in server memory', 'database read and write'],
        rows: [['client', eaInt(2n * B), '0', '0'], ['server', eaInt(id), eaInt(B), '0'], ['database', eaInt(id), '0', eaInt(2n * B)]] }
    };
  };
"""

# ---------------------------------------------------------------------------
# money (mn): allocating an amount by ratios
# ---------------------------------------------------------------------------

MN_JS = r"""
  var MN_VIEW = {};
  function mnCompute(view, inst, opts) { return eaRun(MN_VIEW[view], inst, opts); }
"""

MN_VIEW_JS = {}

MN_VIEW_JS["allocate"] = r"""
  MN_VIEW.allocate = function (inst) {
    var A = inst.amount.n, rs = inst.ratios.map(function (r) { return r.n; }), T = 0n, rule = inst.rule;
    rs.forEach(function (r) { T += r; });
    if (T === 0n) eaRefuse('At least one ratio must be more than 0');
    var exact = rs.map(function (r) { return R(A * r, T); });
    var half = function (e) { return eaFloor(Radd(e, R(1n, 2n))); };
    var got;
    if (rule === 'nearest') got = exact.map(half);
    else if (rule === 'down') got = exact.map(eaFloor);
    else if (rule === 'up') got = exact.map(eaCeil);
    else if (rule === 'last') {
      got = exact.slice(0, -1).map(half);
      var used = 0n; got.forEach(function (g) { used += g; });
      got.push(A - used);
    } else {
      got = exact.map(eaFloor);
      var left = A; got.forEach(function (g) { left -= g; });
      for (var i = 0n; i < left; i += 1n) got[Number(i)] += 1n;
    }
    var total = 0n, far = R0, rows = [];
    got.forEach(function (g, i) {
      total += g;
      var gap = Rabs(Rsub(R(g), exact[i]));
      if (Rcmp(gap, far) > 0) far = gap;
      rows.push([String(i + 1), eaInt(rs[i]), eaNum(exact[i]), eaInt(g), eaNum(gap)]);
    });
    var words = { nearest: 'each share rounded to the nearest cent, a half up', down: 'each share rounded down',
      up: 'each share rounded up', last: 'each share but the last rounded to the nearest cent, and the last taking what is left',
      allocator: 'each share rounded down, then the cents left over given one each to the shares in order from the first' };
    return {
      tiles: { mnShares: got.map(eaInt).join(', '), mnTotal: eaInt(total), mnDiff: eaSigned(total - A),
        mnExact: exact.map(eaNum).join(', '), mnFurthest: eaNum(far) },
      status: 'Rule: ' + words[rule] + '. The shares total ' + eaInt(total) + ' against an amount of ' + eaInt(A) + '.'
        + (got[got.length - 1] < 0n ? ' The last share is negative: rounding the others took more than the amount.' : '')
        + ' The amount is in the smallest unit, cents; the amount and the ratios are the lesson\'s.',
      table: { caption: 'Each share', head: ['share', 'ratio', 'exact', 'given', 'gap'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# the views
# ---------------------------------------------------------------------------


def _check_inherit(inst, fixed):
    rows = inst["classes"]
    parent = tree_check(rows, "class", "a class", "hierarchy")
    for key, what in (("load", "The class to load"), ("find", "The class to find"), ("alter", "The class to add a field to")):
        if inst[key] not in parent:
            raise ValueError("%s, %s, is not one of the classes" % (what, inst[key]))
    if next(r["concrete"] for r in rows if r["class"] == inst["load"]) != "yes":
        raise ValueError("The class to load, %s, is not concrete: only a concrete class has objects to load" % inst["load"])


def _check_timeline(inst, fixed):
    last, touched = -1, set()
    for i, e in enumerate(inst["events"]):
        at = "Events, record %d: " % (i + 1)
        if e["minute"] < last:
            raise ValueError("%sminute %s comes before minute %s of the record before it; the minutes must not decrease"
                             % (at, ea.grp(e["minute"]), ea.grp(last)))
        last = e["minute"]
        if e["action"] == "commit" and e["record"] != "-":
            raise ValueError("%sa commit names no record; write - for it" % at)
        if e["action"] != "commit" and e["record"] == "-":
            raise ValueError("%sa %s needs a record, not -" % (at, e["action"]))
        if e["action"] != "commit":
            touched.add(e["record"])
    grp = {}
    for a, b in inst["groups"]:
        if a not in touched:
            raise ValueError("Groups names %s, which no event reads or edits" % a)
        grp[a] = b
    # The simulation, as far as refusals need it: a session acting after its
    # own commit is refused, unless it failed (then its events are skipped).
    scheme, check_reads = inst["scheme"], inst["checkReads"] == "yes"
    will_edit = {(e["session"], grp.get(e["record"], e["record"])) for e in inst["events"] if e["action"] == "edit"}
    version, locks, ended, failed, seen, edits, reads = {}, {}, set(), set(), {}, {}, {}
    for i, e in enumerate(inst["events"]):
        s, a = e["session"], e["action"]
        if s in failed:
            continue
        if s in ended:
            raise ValueError("Events, record %d: %s acts after it committed" % (i + 1, s))
        seen.setdefault(s, {})
        edits.setdefault(s, [])
        reads.setdefault(s, [])
        if a != "commit":
            g = grp.get(e["record"], e["record"])
            if scheme == "pessimistic" and (s, g) in will_edit and locks.get(g) != s:
                if g in locks:
                    failed.add(s)
                    for k in [k for k, v in locks.items() if v == s]:
                        del locks[k]
                    continue
                locks[g] = s
            seen[s].setdefault(g, version.get(g, 0))
            (edits if a == "edit" else reads)[s].append(g)
            continue
        ended.add(s)
        mine = set(edits[s])
        if scheme == "optimistic":
            check = mine | (set(reads[s]) if check_reads else set())
            if any(version.get(g, 0) != seen[s][g] for g in check):
                failed.add(s)
                continue
        for g in mine:
            version[g] = version.get(g, 0) + 1
        for k in [k for k, v in locks.items() if v == s]:
            del locks[k]


def _check_objects(inst, fixed):
    if inst["thinkMs"] < inst["serviceMs"]:
        raise ValueError("The time between requests must be at least the service time")


def _check_allocate(inst, fixed):
    if not any(inst["ratios"]):
        raise ValueError("At least one ratio must be more than 0")


_RULES = {
    ("inherit", "tables"): "A class's chain is the class and its ancestors; its subtree the class and its descendants. "
                           "Every table has a key column, and the single table a type column too. Single table: one "
                           "table, 2 + every field columns. Class table: a table a class, 1 + its own fields each. "
                           "Concrete table: a table a concrete class, 1 + its chain's fields each. To load an object "
                           "the class table joins the class's chain. To find every instance of a class, subclasses "
                           "included, the class table reads its chain and its subtree (joins up, unions down) and the "
                           "concrete table unions the concrete tables in its subtree. To add a field, the concrete "
                           "table alters every concrete table in the subtree.",
    ("lock", "reads"): "One writer commits once; each item's value before and after that commit is given, and the "
                       "reader reads each item on one side of it. A read before the commit of an item the commit "
                       "changes is stale; a read after it of a changed item is fresh. The reads are consistent when "
                       "none is stale or none is fresh. The stale item decides the level: an update is an "
                       "unrepeatable read, an insert a phantom.",
    ("lock", "timeline"): "Every group has a version, 0 at the start, and a successful commit adds one to each group "
                          "the session edited; a record not given a group is its own. A session's first read or edit "
                          "of a group records the version it saw. None: every commit succeeds, and a lost update is "
                          "counted for each edited group whose version changed since the session saw it. Optimistic: "
                          "a commit fails (a conflict) when an edited group has changed since the session saw it; "
                          "with reads checked, the groups it only read too. Pessimistic: the lock is taken when the "
                          "record is first loaded for editing, not when the edit begins: at the session's first read or edit of a group it edits "
                          "anywhere in the timeline (a read of a group it never edits takes none); this is the "
                          "exclusive write lock, the first of Pessimistic Offline Lock's three. Taking a lock another "
                          "session holds is refused and ends the session, releasing its locks; a commit releases them. A failed session's later events are skipped. Redo is the minutes from a "
                          "failed session's first event to its failure.",
    ("session", "objects"): "Stateful: one object a user. Stateless: an object is busy for the service time of each "
                            "request, so users × service time / the time between requests are busy on average. A "
                            "stateful object is idle for 1 − service / time between requests of the time.",
    ("session", "state"): "Client session state goes to the browser and back on every request (2 × the state). With "
                          "server or database session state a request carries only the session id. Server session "
                          "state holds every user's state in memory; database session state reads it and writes it "
                          "back once a request. Compression, partial loading and caching change every figure.",
    ("money", "allocate"): "The exact share is amount × ratio / the sum of the ratios. nearest: each rounded half up. "
                           "down: each rounded down. up: each rounded up. last: nearest for all but the last share, "
                           "which takes what is left (possibly negative). allocator: each rounded down, then the cents "
                           "left over given one each to the shares in order from the first. Fowler's Money allows "
                           "other ways of placing the leftover cents; allocator is the one his example uses.",
}

_CLASS = {"kind": "name"}

VIEWS = {
    "inherit": {
        "tables": ([("classes", ea.rec("Classes (class, parent or -, own fields, concrete: yes or no)",
                                       [("class", ea.NAME), ("parent", ea.PARENT), ("fields", ea.whole(0, 1000)),
                                        ("concrete", ea.YESNO)], unique=True), None),
                    ("load", ea.field("Class to load (a concrete one)", _CLASS), None),
                    ("find", ea.field("Class to find, with its subclasses", _CLASS), None),
                    ("alter", ea.field("Class to add a field to", _CLASS), None)],
                   [("Tables (single, class, concrete)", "ihTables"), ("Columns (single, class, concrete)", "ihColumns"),
                    ("Empty columns in a row of the class loaded, single table", "ihEmpty"),
                    ("Tables read to load one object (single, class, concrete)", "ihLoad"),
                    ("Tables read to find every instance (single, class, concrete)", "ihFind"),
                    ("Tables altered to add a field (single, class, concrete)", "ihAlter")], 1, _check_inherit),
    },
    "lock": {
        "reads": ([("items", ea.rec("Items (item, before, after, read: before or after, change: insert or update)",
                                    [("item", ea.NAME), ("before", ea.whole(0)), ("after", ea.whole(0)),
                                     ("read", ea.word("before", "after")), ("change", ea.word("insert", "update"))],
                                    unique=True), None)],
                  [("Total the reader saw", "olSeen"), ("Total before the commit", "olBefore"),
                   ("Total after the commit", "olAfter"), ("Matches a state of the data", "olConsistent"),
                   ("Isolation level", "olLevel")], 1, None),
        "timeline": ([("events", ea.rec("Events (minute, session, action: read, edit or commit, record; - for a commit)",
                                        [("minute", ea.whole(0)), ("session", ea.NAME),
                                         ("action", ea.word("read", "edit", "commit")), ("record", ea.PARENT)], rows=4),
                       None),
                      ("scheme", ea.choice("Scheme", "none", "optimistic", "pessimistic"), None),
                      ("groups", ea.pairs("Groups (record=group; a record not listed is its own; optional)",
                                          "record=group"), ""),
                      ("checkReads", ea.choice("Check the records only read (optimistic)", "no", "yes"), "no")],
                     [("Committed", "olCommitted"), ("Conflicts at commit", "olConflicts"),
                      ("Refused a lock", "olRefused"), ("Lost updates", "olLostUpdates"),
                      ("Minutes of work redone", "olRedo"), ("Most locks held at once", "olPeakLocks")], 1,
                     _check_timeline),
    },
    "session": {
        "objects": ([("users", ea.field("Users", ea.whole(1)), None),
                     ("serviceMs", ea.field("Service time of a request (ms)", ea.num(gt=0)), None),
                     ("thinkMs", ea.field("Time between a user's requests (ms)", ea.num(gt=0)), None)],
                    [("Objects, one a user (stateful)", "snStateful"),
                     ("Objects busy on average (stateless)", "snStateless"),
                     ("Share of the time a stateful object is idle", "snIdle"),
                     ("Users a stateless object serves", "snPerObject")], 2, _check_objects),
        "state": ([("users", ea.field("Users", ea.whole(1)), None),
                   ("stateBytes", ea.field("Session state (bytes)", ea.whole(1)), None),
                   ("requests", ea.field("Requests in a session", ea.whole(1)), None),
                   ("idBytes", ea.field("Session id (bytes)", ea.whole(0)), None)],
                  [("Bytes on the wire a request, client state", "snWire"),
                   ("Bytes on the wire a session, client state", "snSessionWire"),
                   ("Bytes on the wire a request, server or database state", "snIdOnly"),
                   ("Bytes held in memory, server state", "snMemory"),
                   ("Bytes read and written a request, database state", "snDatabase")], 2, None),
    },
    "money": {
        "allocate": ([("amount", ea.field("Amount (cents)", ea.whole(0)), None),
                      ("ratios", dict(what="Ratios (whole numbers, space-separated)", control="text", kind="list",
                                      lo=2, hi=20, things="ratios", each=ea.whole(0, 10 ** 6)), None),
                      ("rule", ea.choice("Rounding rule", "nearest", "down", "up", "last", "allocator"), None)],
                     [("Shares (cents)", "mnShares"), ("Total of the shares", "mnTotal"),
                      ("Total less the amount", "mnDiff"), ("Exact shares", "mnExact"),
                      ("Largest gap from an exact share", "mnFurthest")], 2, _check_allocate),
    },
}

SUBTITLES = {
    ("inherit", "tables"): "single, class and concrete table inheritance",
    ("lock", "reads"): "what a reader sees across one commit",
    ("lock", "timeline"): "sessions under no control, optimistic and pessimistic locking",
    ("session", "objects"): "stateful against stateless server objects",
    ("session", "state"): "client, server and database session state",
    ("money", "allocate"): "dividing an amount by ratios without losing a cent",
}

TITLES = {"inherit": "Inheritance mappings", "lock": "Concurrency", "session": "Session state",
          "money": "Money arithmetic"}

PREFIX = {"inherit": ("ih", "ihCompute", IH_JS, IH_VIEW_JS), "lock": ("ol", "olCompute", OL_JS, OL_VIEW_JS),
          "session": ("sn", "snCompute", SN_JS, SN_VIEW_JS), "money": ("mn", "mnCompute", MN_JS, MN_VIEW_JS)}


def _options(cfg, kit, mode, view, tiles):
    return {}, [], tiles


def mode_lab(cfg, mode):
    return view_lab(cfg, mode, VIEWS, TITLES, SUBTITLES, PREFIX, _RULES, options=_options)


__all__ = ["mode_lab", "VIEWS"]

