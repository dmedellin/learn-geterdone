"""earef.py -- the reference model for eakit (docs/enterprise-patterns/PLAN.md, section D).

Run it with no arguments:

    python3 docs/enterprise-patterns/earef.py

It prints every preset's tiles, lesson by lesson in PLAN section C's numbering,
in the number format of PLAN section D.0. Every eakit figure in section C is
its output. The model is not the kit: the kit is JavaScript, and its figures
are read off the page with `node scripts/labcheck.js --observe`. Where the two
disagree, the kit engineer finds out which is wrong and records it in the kit
report.

The lessons that reuse cckit (PLAN section D.5) are computed by the shipped
cckit JavaScript itself, through docs/enterprise-patterns/ccrun.js (node), so
their figures are the kit's own; `python3 earef.py --cc` prints them too.

Every computation is exact: integers and fractions.Fraction, never a float.
Nothing here is a figure from the book: every number arrives in a preset.
"""

import json
import math
import os
import subprocess
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------ format (D.0)


def grp(n):
    """A whole number with thousands grouped and U+2212 for a minus."""
    s = "{:,}".format(abs(int(n)))
    return ("−" + s) if n < 0 else s


def _two(q):
    """q to two places, half away from zero, as a string."""
    q = F(q)
    sign = -1 if q < 0 else 1
    a = abs(q) * 100
    r = int(a)
    if a - r >= F(1, 2):
        r += 1
    whole, frac = divmod(r, 100)
    s = "{:,}.{:02d}".format(whole, frac)
    return ("−" + s) if sign < 0 and r else s


def num(q):
    """A rational: whole -> grouped; else 'p/q = d.dd' or 'p/q ≈ d.dd'."""
    q = F(q)
    if q.denominator == 1:
        return grp(q.numerator)
    exact = (q * 100).denominator == 1
    frac = "%s/%s" % (grp(q.numerator), grp(q.denominator))
    return "%s %s %s" % (frac, "=" if exact else "≈", _two(q))


def pct(q):
    """A share: '9/10 = 90%', '31/60 ≈ 51.7%', '1 = 100%', '0 = 0%'."""
    q = F(q)
    p = q * 100
    if q.denominator == 1:
        head = grp(q.numerator)
    else:
        head = "%s/%s" % (grp(q.numerator), grp(q.denominator))
    if p.denominator == 1:
        return "%s = %s%%" % (head, grp(p.numerator))
    a = abs(p) * 10
    r = int(a)
    if a - r >= F(1, 2):
        r += 1
    return "%s ≈ %d.%d%%" % (head, r // 10, r % 10)


def times(q):
    q = F(q)
    if q.denominator == 1:
        return grp(q.numerator) + "×"
    a = abs(q) * 10
    r = int(a)
    if a - r >= F(1, 2):
        r += 1
    return "%s/%s ≈ %s.%d×" % (grp(q.numerator), grp(q.denominator), grp(r // 10), r % 10)


def names(xs):
    return ", ".join(xs) if xs else "none"


def counted(xs):
    return "%d: %s" % (len(xs), names(xs))


def signed(n):
    return ("+" + grp(n)) if n > 0 else grp(n)


def recs(text, k):
    """'a, 1; b, 2' -> [['a','1'], ['b','2']] with exactly k parts each."""
    out = []
    for r in text.split(";"):
        if not r.strip():
            continue
        p = [x.strip() for x in r.split(",")]
        if len(p) != k:
            raise ValueError("record %r has %d parts, not %d" % (r, len(p), k))
        out.append(p)
    return out


# ------------------------------------------------------------------ perf (pz)


def perf_load(inst):
    """records system, users, ms (a measured response time at a load)."""
    by = {}
    order = []
    for s, u, ms in recs(inst["points"], 3):
        if s not in by:
            by[s] = []
            order.append(s)
        by[s].append((int(u), F(ms)))
    per, ratio, at = [], [], []
    for s in order:
        pts = sorted(by[s])
        (u0, r0), (u1, r1) = pts[0], pts[-1]
        slope = (r1 - r0) / (u1 - u0) if u1 != u0 else None
        per.append("%s %s ms a user" % (s, num(slope) if slope is not None else "—"))
        ratio.append("%s %s" % (s, times(r1 / r0)))
        u = int(inst["users"])
        val = None
        for (ua, ra), (ub, rb) in zip(pts, pts[1:]):
            if ua <= u <= ub:
                val = ra + (rb - ra) * F(u - ua, ub - ua) if ub != ua else ra
                break
        if len(pts) == 1 and pts[0][0] == u:
            val = pts[0][1]
        at.append("%s %s ms" % (s, num(val)) if val is not None else "%s outside its measured loads" % s)
    return {"pzPerUser": "; ".join(per), "pzRatio": "; ".join(ratio), "pzAt": "; ".join(at)}


def perf_scale(inst):
    """records system, servers, tps; inputs need, at. Linear in the servers past
    the last measurement, at the rate between the first and last measurement."""
    by, order = {}, []
    for s, n, t in recs(inst["points"], 3):
        if s not in by:
            by[s] = []
            order.append(s)
        by[s].append((int(n), F(t)))
    eff, marg, need, at = [], [], [], []
    proj = {}
    for s in order:
        pts = sorted(by[s])
        n0, t0 = pts[0]
        nl, tl = pts[-1]
        eff.append("%s %s a %s" % (s, num(t0 / n0), inst.get("unit", "server")))
        rate = (tl - t0) / (nl - n0) if nl != n0 else None
        marg.append("%s %s" % (s, num(rate) if rate is not None else "—"))

        def f(n, pts=pts, rate=rate, nl=nl, tl=tl):
            for (a, ta) in pts:
                if a == n:
                    return ta
            if rate is None:
                return None
            return tl + rate * (n - nl)
        proj[s] = f
        if "need" in inst:
            want = F(inst["need"])
            got = None
            for n in range(1, 10001):
                v = f(n)
                if v is not None and v >= want:
                    got = n
                    break
            need.append("%s %s" % (s, grp(got) if got else
                                   ("not measured: one measurement gives no rate" if rate is None
                                    else "never at this rate")))
        if "at" in inst:
            v = f(int(inst["at"]))
            at.append("%s %s" % (s, num(v) if v is not None else "—"))
    out = {"pzEfficiency": "; ".join(eff), "pzMarginal": "; ".join(marg)}
    if len(order) == 2:
        a, b = order
        first_a = proj[a](1) >= proj[b](1) if proj[a](1) is not None and proj[b](1) is not None else None
        cross = None
        for n in range(1, 10001):
            va, vb = proj[a](n), proj[b](n)
            if va is None or vb is None:
                break
            if (va >= vb) != first_a or va == vb:
                cross = (n, va, vb)
                break
        if cross:
            n, va, vb = cross
            out["pzCrossover"] = ("%s servers (both %s)" % (grp(n), num(va)) if va == vb
                                  else "%s servers (%s %s, %s %s)" % (grp(n), a, num(va), b, num(vb)))
        else:
            out["pzCrossover"] = ("—: each system needs two measurements"
                                  if any(len(by[x]) < 2 for x in order) else "none")
    if need:
        out["pzNeed"] = "; ".join(need)
    if at:
        out["pzAt"] = "; ".join(at)
    return out


# ------------------------------------------------------------------ remote (rr)


def remote_boundary(inst):
    """records caller, callee, calls; nodes 'class=node; ...'; remoteUs, localUs."""
    node = {}
    for part in inst.get("nodes", "").split(";"):
        if part.strip():
            k, v = [x.strip() for x in part.split("=")]
            node[k] = v
    total = remote = 0
    for a, b, c in recs(inst["calls"], 3):
        c = int(c)
        total += c
        if node.get(a, "main") != node.get(b, "main"):
            remote += c
    R, Lc = F(inst["remoteUs"]), F(inst["localUs"])
    t = remote * R + (total - remote) * Lc
    one = total * Lc
    return {"rrCalls": grp(total), "rrRemote": grp(remote), "rrTime": num(t),
            "rrShare": pct(remote * R / t) if t else "—", "rrOneNode": num(one),
            "rrRatio": times(t / one)}


def remote_calls(inst):
    """records operation, fine; latencyMs, workMs."""
    ops = recs(inst["ops"], 2)
    n = sum(int(f) for _, f in ops)
    m = len(ops)
    L, w = F(inst["latencyMs"]), F(inst["workMs"])
    fine = n * (L + w)
    coarse = m * L + n * w
    return {"rrFineTrips": grp(n), "rrCoarseTrips": grp(m), "rrFineMs": num(fine),
            "rrCoarseMs": num(coarse), "rrLatencyShare": pct(n * L / fine), "rrSpeedup": times(fine / coarse)}


def remote_payload(inst):
    """records field, bytes, needed (yes|no); latencyMs, bytesPerMs, factor."""
    fs = recs(inst["fields"], 3)
    L, bw = F(inst["latencyMs"]), F(inst["bytesPerMs"])
    k = F(inst.get("factor", 1))
    need = [(f, int(b)) for f, b, n in fs if n == "yes"]
    allb = sum(int(b) for _, b, _ in fs) * k
    needb = sum(b for _, b in need) * k
    calls = len(need)
    getter = calls * L + needb / bw
    dto = L + allb / bw
    spare = (calls - 1) * L * bw if calls else 0
    return {"rrGetterCalls": grp(calls), "rrGetterMs": num(getter), "rrDtoBytes": num(allb),
            "rrDtoMs": num(dto), "rrExtraBytes": num(allb - needb), "rrSpare": num(spare)}


# ------------------------------------------------------------------ load (ld)


def load_instances(inst):
    rows = recs(inst["tables"], 2)
    r = sum(int(x) for _, x in rows)
    t = len(rows)
    big, bigrows = max(rows, key=lambda x: int(x[1]))
    return {"ldTables": grp(t), "ldRows": grp(r), "ldRowObjects": grp(r), "ldTableObjects": grp(t),
            "ldLargest": "%s %s" % (big, grp(int(bigrows)))}


def load_finds(inst):
    K, R, b = int(inst["wanted"]), int(inst["broad"]), int(inst["batch"])
    L, r = F(inst["latencyMs"]), F(inst["rowMs"])
    bs = -(-K // b)
    return {"ldKeyedStatements": grp(K), "ldKeyedMs": num(K * L + K * r),
            "ldBroadRows": grp(R), "ldBroadMs": num(L + R * r),
            "ldBatchStatements": grp(bs), "ldBatchMs": num(bs * L + K * r),
            "ldUnneeded": grp(R - K)}


def load_identity(inst):
    finds = recs(inst["finds"], 2)
    seen = {}
    order = []
    for c, i in finds:
        key = "%s %s" % (c, i)
        if key not in seen:
            seen[key] = 0
            order.append(key)
        seen[key] += 1
    shared = ["%s ×%d" % (k, seen[k]) for k in order if seen[k] > 1]
    return {"ldFinds": grp(len(finds)), "ldDistinct": grp(len(order)),
            "ldDuplicates": grp(len(finds) - len(order)), "ldShared": names(shared)}


def load_graph(inst):
    """records parent, children, used (yes|no); batch."""
    ps = recs(inst["parents"], 3)
    N = len(ps)
    tot = sum(int(c) for _, c, _ in ps)
    used = [(p, int(c)) for p, c, u in ps if u == "yes"]
    t = len(used)
    tc = sum(c for _, c in used)
    b = int(inst["batch"])
    joined = sum(max(int(c), 1) for _, c, _ in ps)

    def s(st, rows):
        return "%s %s, %s %s" % (grp(st), "statement" if st == 1 else "statements",
                                 grp(rows), "row" if rows == 1 else "rows")
    return {"ldLazy": s(1 + t, N + tc), "ldBatched": s(1 + -(-t // b) if t else 1, N + tc),
            "ldTwoQueries": s(2, N + tot), "ldJoin": s(1, joined)}


def load_tree(inst):
    """records node, parent ('-' for the root)."""
    rs = recs(inst["nodes"], 2)
    parent = {n: p for n, p in rs}
    roots = [n for n, p in rs if p == "-"]
    if len(roots) != 1:
        raise ValueError("one root")

    def depth(n):
        d = 1
        while parent[n] != "-":
            n = parent[n]
            d += 1
        return d
    D = max(depth(n) for n in parent)
    return {"ldNodes": grp(len(rs)), "ldDepth": grp(D), "ldPerNode": grp(1 + len(rs)),
            "ldPerLevel": grp(D + 1), "ldLob": "1"}


# ------------------------------------------------------------------ uow (uw)


def uow_commit(inst):
    ops = recs(inst["script"], 2)
    state = {}   # name -> loaded | new | deleted
    changed, first = {}, []
    imm = 0
    for op, x in ops:
        if x not in first:
            first.append(x)
        st = state.get(x)
        if st == "deleted":
            raise ValueError("%s after delete of %s" % (op, x))
        if op == "load":
            if st == "new":
                raise ValueError("load of new %s" % x)
            state[x] = st or "loaded"
        elif op == "new":
            if st:
                raise ValueError("new of existing %s" % x)
            state[x] = "new"
            imm += 1
        elif op == "change":
            if not st:
                raise ValueError("change of %s before load or new" % x)
            changed[x] = True
            imm += 1
        elif op == "delete":
            if not st:
                raise ValueError("delete of %s before load or new" % x)
            state[x] = "deleted:" + st
            imm += 1
            state[x] = "deleted"
            changed.setdefault("__del__", []).append((x, st))
        else:
            raise ValueError(op)
    wasnew = {x for op, x in ops if op == "new"}
    ins, upd, dele, clean = [], [], [], []
    for x in first:
        st = state[x]
        if st == "deleted":
            if x not in wasnew:
                dele.append(x)
        elif st == "new":
            ins.append(x)
        elif changed.get(x):
            upd.append(x)
        else:
            clean.append(x)
    writes = ["INSERT " + x for x in ins] + ["UPDATE " + x for x in upd] + ["DELETE " + x for x in dele]
    c = len(writes)
    return {"uwImmediate": grp(imm), "uwCommit": grp(c), "uwSaved": "%s (%s)" % (grp(imm - c), pct(F(imm - c, imm)) if imm else "—"),
            "uwWrites": "; ".join(writes) if writes else "none", "uwClean": counted(clean)}


def uow_order(inst):
    """records child, parent (child holds a foreign key to parent); input 'as'."""
    es = recs(inst["keys"], 2)
    nodes = sorted({x for e in es for x in e} | set(inst.get("as", "").split()))
    deps = {n: set() for n in nodes}
    for c, p in es:
        deps[c].add(p)
    done, order = set(), []
    while len(order) < len(nodes):
        ready = [n for n in nodes if n not in done and deps[n] <= done]
        if not ready:
            raise ValueError("cycle")
        n = sorted(ready)[0]
        order.append(n)
        done.add(n)
    out = {"uwInsertOrder": ", ".join(order), "uwDeleteOrder": ", ".join(reversed(order))}
    if inst.get("as"):
        pos = {n: i for i, n in enumerate(inst["as"].split())}
        bad = ["%s before %s" % (c, p) for c, p in es if pos[c] < pos[p]]
        out["uwBroken"] = counted(bad)
    return out


# ------------------------------------------------------------------ inherit (ih)


def inherit_tables(inst):
    """records class, parent ('-' for a root), fields, concrete (yes|no); load, find, alter."""
    rs = recs(inst["classes"], 4)
    par = {c: p for c, p, _, _ in rs}
    fld = {c: int(f) for c, _, f, _ in rs}
    con = {c: k == "yes" for c, _, _, k in rs}
    cls = [c for c, _, _, _ in rs]

    def chain(c):
        out = [c]
        while par[c] != "-":
            c = par[c]
            out.append(c)
        return out

    def subtree(c):
        return [x for x in cls if c in chain(x)]
    allf = sum(fld.values())
    concretes = [c for c in cls if con[c]]
    s_cols = 2 + allf
    c_cols = sum(1 + fld[c] for c in cls)
    k_cols = sum(1 + sum(fld[a] for a in chain(c)) for c in concretes)
    L, Fd, A = inst["load"], inst["find"], inst["alter"]
    empty = allf - sum(fld[a] for a in chain(L))
    find_class = len(set(chain(Fd)) | set(subtree(Fd)))
    find_conc = len([x for x in subtree(Fd) if con[x]])
    alter_conc = len([x for x in subtree(A) if con[x]])
    three = lambda a, b, c: "%s, %s, %s" % (grp(a), grp(b), grp(c))
    return {"ihTables": three(1, len(cls), len(concretes)), "ihColumns": three(s_cols, c_cols, k_cols),
            "ihEmpty": grp(empty), "ihLoad": three(1, len(chain(L)), 1),
            "ihFind": three(1, find_class, find_conc), "ihAlter": three(1, 1, alter_conc)}


# ------------------------------------------------------------------ lock (ol)


def lock_reads(inst):
    """records item, before, after, read (before|after the writer's commit), change (insert|update).
    A read before the commit of an item the commit changes is stale; the reads are
    inconsistent when a stale read and a read of a changed item after the commit
    are in the same session."""
    rs = recs(inst["items"], 5)
    seen = sum(int(b) if r == "before" else int(a) for _, b, a, r, _ in rs)
    B = sum(int(b) for _, b, _, _, _ in rs)
    A = sum(int(a) for _, _, a, _, _ in rs)
    stale = [ch for _, b, a, r, ch in rs if r == "before" and b != a]
    fresh = [ch for _, b, a, r, ch in rs if r == "after" and b != a]
    if not stale:
        cons = "yes: the state after the commit"
    elif not fresh:
        cons = "yes: the state before the commit"
    elif seen == B or seen == A:
        cons = ("no, though %s equals the total %s the commit" %
                (grp(seen), "before" if seen == B else "after"))
    elif A == B:
        cons = "no: %s is not %s, before or after" % (grp(seen), grp(B))
    else:
        cons = "no: %s is neither %s nor %s" % (grp(seen), grp(B), grp(A))
    if not stale or not fresh:
        level = "none needed: no read straddles the commit"
    elif all(ch == "insert" for ch in stale):
        level = "repeatable read allows it (a phantom); serializable prevents it"
    else:
        level = "read committed allows it (an unrepeatable read); repeatable read prevents it"
    return {"olSeen": grp(seen), "olBefore": grp(B), "olAfter": grp(A), "olConsistent": cons, "olLevel": level}


def lock_timeline(inst):
    """records minute, session, action (read|edit|commit), record ('-' for commit)."""
    rs = recs(inst["events"], 4)
    scheme = inst["scheme"]
    checkreads = inst.get("checkReads", "no") == "yes"
    grp_of = {}
    for part in inst.get("groups", "").split(";"):
        if part.strip():
            k, v = [x.strip() for x in part.split("=")]
            grp_of[k] = v
    G = lambda r: grp_of.get(r, r)
    version = {}
    locks = {}            # group -> session
    start, ended, failed = {}, {}, set()
    seenv = {}            # session -> {group: version when read/edited}
    edits = {}            # session -> [groups]
    reads = {}
    committed, conflicts, refused = [], [], []
    lost = 0
    redo = 0
    peak = 0
    last = -1
    will_edit = {}        # session -> groups it edits anywhere in the timeline
    for _, s0, a0, r0 in rs:
        if a0 == "edit":
            will_edit.setdefault(s0, set()).add(G(r0))
    for m, s, a, r in rs:
        m = int(m)
        if m < last:
            raise ValueError("minutes must not decrease")
        last = m
        if s in failed:
            continue      # a refused or conflicted session's later events are skipped
        if s in ended:
            raise ValueError("%s acts after it committed" % s)
        start.setdefault(s, m)
        seenv.setdefault(s, {})
        edits.setdefault(s, [])
        reads.setdefault(s, [])
        if a in ("read", "edit"):
            g = G(r)
            if scheme == "pessimistic" and g in will_edit.get(s, ()) and locks.get(g) != s:
                # the lock is taken when the data is first loaded (PDF p. 384)
                holder = locks.get(g)
                if holder and holder != s:
                    refused.append(s)
                    failed.add(s)
                    redo += m - start[s]
                    for k in [k for k, v in locks.items() if v == s]:
                        del locks[k]
                    ended[s] = m
                    continue
                locks[g] = s
                peak = max(peak, len(locks))
            seenv[s].setdefault(g, version.get(g, 0))
            (edits if a == "edit" else reads)[s].append(g)
        elif a == "commit":
            ended[s] = m
            if scheme == "optimistic":
                check = set(edits[s]) | (set(reads[s]) if checkreads else set())
                if any(version.get(g, 0) != seenv[s][g] for g in check):
                    conflicts.append(s)
                    failed.add(s)
                    redo += m - start[s]
                    continue
            if scheme == "none":
                lost += sum(1 for g in set(edits[s]) if version.get(g, 0) != seenv[s][g])
            for g in set(edits[s]):
                version[g] = version.get(g, 0) + 1
            for k in [k for k, v in locks.items() if v == s]:
                del locks[k]
            committed.append(s)
        else:
            raise ValueError(a)
    return {"olCommitted": counted(committed), "olConflicts": counted(conflicts),
            "olRefused": counted(refused), "olLostUpdates": grp(lost), "olRedo": grp(redo),
            "olPeakLocks": grp(peak) if scheme == "pessimistic" else "—"}


# ------------------------------------------------------------------ session (sn)


def session_objects(inst):
    U, s, t = int(inst["users"]), F(inst["serviceMs"]), F(inst["thinkMs"])
    return {"snStateful": grp(U), "snStateless": num(U * s / t), "snIdle": pct(1 - s / t),
            "snPerObject": num(t / s)}


def session_state(inst):
    U, B, R, idb = int(inst["users"]), int(inst["stateBytes"]), int(inst["requests"]), int(inst["idBytes"])
    return {"snWire": grp(2 * B), "snSessionWire": grp(2 * B * R), "snIdOnly": grp(idb),
            "snMemory": grp(U * B), "snDatabase": grp(2 * B)}


# ------------------------------------------------------------------ money (mn)


def _half_up(q):
    return int(q) + (1 if q - int(q) >= F(1, 2) else 0)


def money_allocate(inst):
    A = int(inst["amount"])
    rs = [int(x) for x in inst["ratios"].split()]
    T = sum(rs)
    exact = [F(A * r, T) for r in rs]
    rule = inst["rule"]
    if rule == "nearest":
        got = [_half_up(e) for e in exact]
    elif rule == "down":
        got = [math.floor(e) for e in exact]
    elif rule == "up":
        got = [math.ceil(e) for e in exact]
    elif rule == "last":
        got = [_half_up(e) for e in exact[:-1]]
        got.append(A - sum(got))
    elif rule == "allocator":
        got = [math.floor(e) for e in exact]
        for i in range(A - sum(got)):
            got[i] += 1
    else:
        raise ValueError(rule)
    far = max(abs(g - e) for g, e in zip(got, exact))
    return {"mnShares": ", ".join(grp(g) for g in got), "mnTotal": grp(sum(got)),
            "mnDiff": signed(sum(got) - A), "mnExact": ", ".join(num(e) for e in exact),
            "mnFurthest": num(far)}


VIEWS = {
    ("perf", "load"): perf_load, ("perf", "scale"): perf_scale,
    ("remote", "boundary"): remote_boundary, ("remote", "calls"): remote_calls,
    ("remote", "payload"): remote_payload,
    ("load", "instances"): load_instances, ("load", "finds"): load_finds,
    ("load", "identity"): load_identity, ("load", "graph"): load_graph, ("load", "tree"): load_tree,
    ("uow", "commit"): uow_commit, ("uow", "order"): uow_order,
    ("inherit", "tables"): inherit_tables,
    ("lock", "reads"): lock_reads, ("lock", "timeline"): lock_timeline,
    ("session", "objects"): session_objects, ("session", "state"): session_state,
    ("money", "allocate"): money_allocate,
}


def run(lessons, cc=False):
    from presets import LESSONS, CC_JOBS
    for tag, mode, view, cfg, presets in LESSONS:
        if lessons and tag not in lessons:
            continue
        print("== %s %s/%s" % (tag, mode, view))
        for pid, inst in presets:
            full = dict(cfg)
            full.update(inst)
            out = VIEWS[(mode, view)](full)
            print("  %-22s %s" % (pid, " | ".join("%s %s" % kv for kv in out.items())))
    if cc:
        res = subprocess.run(["node", os.path.join(HERE, "ccrun.js")], input=json.dumps(CC_JOBS),
                             capture_output=True, text=True, check=True)
        for r in json.loads(res.stdout):
            print("== %s cckit %s" % (r["id"], " | ".join("%s %s" % kv for kv in (r.get("tiles") or {}).items())
                                       or r.get("refuse") or r.get("error")))


if __name__ == "__main__":
    sys.path.insert(0, HERE)
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    run(args, cc="--cc" in sys.argv)
