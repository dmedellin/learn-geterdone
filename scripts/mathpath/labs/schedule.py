"""Course 6's scheduling kit -- nine modes, one machine model underneath.

Every rule on this course is proved by an ADJACENT EXCHANGE, and that is the
one thing this kit exists to make visible. A page that reported "SPT is
optimal" would be asserting the theorem; these pages swap two neighbouring
jobs, print the exact quantity the swap moved, and then check the claim against
every one of the n! orders.

  objectives  one sequence, eight objectives at once, each with the exhaustive
              optimum beside it -- a schedule is never simply good
  spt         shortest processing time, and the exchange that proves it: swap
              neighbours and sum C moves by p_b - p_a and by nothing else
  wspt        Smith's ratio p/w, the same exchange weighted, and the rival
              rule -- heaviest weight first -- shown losing on the same data
  edd         earliest due date for L max, and the same order LOSING on total
              tardiness, which is the misconception this lesson is about
  late        Moore-Hodgson step by step: the job thrown out is the LONGEST
              accepted so far, not the one that was late
  flowshop    two machines in series, Johnson's rule, and the idle time on the
              second machine that the rule is actually minimising
  parallel    m machines, LPT against the exhaustive optimum and against BOTH
              lower bounds the 4/3 ratio is proved from
  jobshop     every disjunctive orientation scored, the deadlocks counted as
              answers rather than errors, and the best one drawn
  crash       the crashing linear programme, the exact time-cost curve by
              rhsCurve on the deadline row, and CPM run on the crashed
              durations to confirm the deadline is actually met

WHAT A MODE MAY NOT DO, and the reason this kit is shaped the way it is.

  NO MODE PRINTS AN OPTIMUM IT HAS NOT CHECKED. Every objective on the one
  machine is recomputed by a SECOND route before anything is shown -- sum C as
  `sum_k (n - k) p_[k]` and sum wC as `sum_k p_[k] * (suffix weight)`, neither
  of which forms a running clock the way `seqObjectives` does -- and the two
  must agree entry for entry or the panel refuses. Then the claim of optimality
  is held to `bestSequence`, which enumerates every order. When the enumeration
  cap bites, the page SAYS the claim is unchecked rather than printing it
  unqualified.

  A RULE'S ORDER IS AUDITED AS AN ORDER, NOT AS A COUNT. `orderAudit` returns
  `permutation` and `ordered` as two separate booleans. Counting "how many
  adjacent pairs are out of order" is not enough on its own: a list that is not
  a permutation of the jobs has a count too, and a count of zero. Both halves
  are asserted by name in scripts/mathcheck.js.

  THE EXCHANGE IS RUN, NOT DESCRIBED. `exchangeChain` repeatedly takes the
  first adjacent swap that improves the objective and reports the exact
  quantity it moved. On sum C and sum wC the walk stops at the rule's own
  order, and the page says so having watched it happen -- which is the
  difference between a demonstration and a claim.

WHAT IS DELIBERATELY ABSENT.

  A TARDINESS ALGORITHM. `sumT` has no exchange rule and this course does not
  pretend otherwise: `edd` shows EDD losing on it and `objectives` shows the
  exhaustive optimum, and the lesson names 1||sum T as the boundary of what an
  exchange argument reaches. Inventing a plausible-looking heuristic here would
  teach the opposite of the course.

  A RELEASE-DATE OR PREEMPTION MODEL. Every job here is available at time zero
  and runs to completion. Release dates change which exchanges are legal and
  the proofs in this course do not survive them; saying so is cheaper than a
  mode that silently assumes them away.

  A GANTT EDITOR. The reader types a sequence and the picture follows. Dragging
  bars would need a pointer model this library does not have, and the sequence
  box is the thing a reader can check by hand.

BLOCKS PER MODE, because the measured ceiling is 62 KB gzipped (AGENTS.md,
"A note on page weight"). or_core's docstring puts this kit's engine share at
27.2 KB -- that figure is the blocks WITHOUT `NET_JS`, and `SCHED_JS`'s own
dependency note one page further down says `jobShopAll` needs it; with it the
same concatenation measures 32.7 KB. Only two modes call into `NET_JS` and only
one solves a linear programme, so the kit selects per mode rather than paying
either figure nine times.

Measured as whole pages by scripts/build_paths.py, page frame included:

    objectives 33.7 KB   spt 33.2   wspt 33.4   edd 33.4   late 33.3
    flowshop 33.2   parallel 33.6   jobshop 38.6   crash 55.2

against the 62 KB ceiling. `crash` is the heaviest page in this Subject and the
figure to re-derive first when anything here grows; the rest have room.
"""

from .algebra_core import RATIONAL_JS
from .algebra_systems import FORMAT_JS, MATRIX_JS
from .common import Lab
from .or_core import (DUAL_JS, NET_JS, ORFMT_JS, PHASE_JS, RANGE_JS, SCHED_JS,
                      TABLEAU_JS)

# ---------------------------------------------------------------------------
# The kit's own arithmetic. Top-level functions only, so scripts/mathcheck.js
# executes the shipped source rather than a transcription of it: nothing here
# touches the document, and the drawing functions take data and return a
# string.
# ---------------------------------------------------------------------------

SCHEDKIT_JS = r"""

  /* ================================================== jobs, as a reader types

     A job is {id, p, w, d} and a sequence is an array of INDICES into the job
     list -- not of ids, because two jobs may not share an id and the index is
     what every function in SCHED_JS takes.  The parsers below are the only
     door into this kit; everything else is given structure. */

  var SCHEDJOBS = 8;      /* ids a table and a Gantt strip can hold */
  var SCHEDPERM = 7;      /* jobs the page enumerates: 7! = 5040 orders */

  function schedClauses(text) {
    var parts = String(text).split(/[,;\n]+/), out = [], i;
    for (i = 0; i < parts.length; i += 1) {
      var s = parts[i].trim();
      if (s) out.push(s);
    }
    return out;
  }

  /* One clause is a name, a space, then the fields colon separated:
       A 6:1:8      six hours of work, weight 1, due at 8
     A fraction is a fraction -- 7/2 reads as seven halves -- because the field
     separator is a colon and never a slash. */
  function parseJobs(text, keys, labels) {
    var cl = schedClauses(text), jobs = [], seen = {}, i, k;
    if (!cl.length) return { bad: 'there are no jobs here yet' };
    if (cl.length > SCHEDJOBS) {
      return { bad: 'that is ' + cl.length + ' jobs, and this lab schedules at most ' + SCHEDJOBS };
    }
    for (i = 0; i < cl.length; i += 1) {
      var m = /^([A-Za-z][A-Za-z0-9]{0,3})\s+(.*)$/.exec(cl[i]);
      if (!m) {
        return { bad: '"' + esc(cl[i]) + '" is not a job: write a name, a space, then '
                      + labels.join(' and then ') + ', colon separated' };
      }
      if (seen[m[1]]) {
        return { bad: 'there are two jobs called ' + esc(m[1])
                      + ', and a sequence could not name either of them' };
      }
      var vals = m[2].split(':'), job = { id: m[1] };
      if (vals.length !== keys.length) {
        return { bad: '"' + esc(cl[i]) + '" gives ' + vals.length + ' number'
                      + (vals.length === 1 ? '' : 's') + '; a job here carries '
                      + labels.join(' and then ') + ' — ' + keys.length + ' of them' };
      }
      for (k = 0; k < keys.length; k += 1) {
        var v = Rread(vals[k].trim());
        if (v === null) {
          return { bad: '"' + esc(vals[k]) + '" in "' + esc(cl[i]) + '" is not a number' };
        }
        if ((keys[k] === 'p' || keys[k] === 'p1' || keys[k] === 'p2') && Rsign(v) <= 0) {
          return { bad: labels[k] + ' on ' + esc(m[1]) + ' is ' + Rtext(v)
                        + ', and a job that takes no time is not a job this course can order' };
        }
        if (keys[k] === 'w' && Rsign(v) <= 0) {
          return { bad: 'the weight on ' + esc(m[1]) + ' is ' + Rtext(v)
                        + ", and Smith's ratio p/w needs a positive weight" };
        }
        if (keys[k] === 'd' && Rsign(v) < 0) {
          return { bad: 'the due date on ' + esc(m[1]) + ' is ' + Rtext(v) + ', which is before the shift starts' };
        }
        job[keys[k]] = v;
      }
      seen[m[1]] = true;
      jobs.push(job);
    }
    return { jobs: jobs };
  }

  function jobIndex(jobs) {
    var ix = {}, k;
    for (k = 0; k < jobs.length; k += 1) ix[jobs[k].id] = k;
    return ix;
  }

  /* A sequence, as names.  It must be a PERMUTATION -- every job once -- and
     the refusal says which job is missing or repeated rather than reporting
     "invalid", because the reader is holding a list and wants to know where. */
  function parseSeq(text, jobs) {
    var toks = String(text).split(/[\s,;>]+/).filter(function (s) { return s.length; });
    var ix = jobIndex(jobs), seq = [], used = {}, i;
    if (!toks.length) return { bad: 'there is no sequence here yet' };
    for (i = 0; i < toks.length; i += 1) {
      if (ix[toks[i]] === undefined) {
        return { bad: 'there is no job called ' + esc(toks[i]) + ' in the list above' };
      }
      if (used[toks[i]]) return { bad: esc(toks[i]) + ' runs twice, and a machine does one job once' };
      used[toks[i]] = true;
      seq.push(ix[toks[i]]);
    }
    if (seq.length !== jobs.length) {
      var missing = [];
      for (i = 0; i < jobs.length; i += 1) if (!used[jobs[i].id]) missing.push(jobs[i].id);
      return { bad: 'the sequence leaves out ' + missing.join(' and ')
                    + ' — every job has to be somewhere in the order' };
    }
    return { seq: seq };
  }

  /* ========================================================= the rules

     Each rule is a KEY the sequence is sorted by, ascending, with ties broken
     by the order the jobs were typed in.  That tie-break is part of the rule
     and not an implementation detail: without it "the SPT order" is not a
     function of the data, and two pages could show two different orders under
     the same heading. */
  var SCHEDRULES = {
    FCFS: { label: 'in the order typed', key: null },
    SPT: { label: 'shortest processing time first', key: function (j) { return j.p; } },
    LPT: { label: 'longest processing time first', key: function (j) { return Rneg(j.p); } },
    WSPT: { label: "Smith's ratio, smallest p/w first", key: function (j) { return Rdiv(j.p, j.w); } },
    WEIGHT: { label: 'heaviest weight first', key: function (j) { return Rneg(j.w); } },
    EDD: { label: 'earliest due date first', key: function (j) { return j.d; } },
    SLACK: { label: 'least slack d − p first', key: function (j) { return Rsub(j.d, j.p); } }
  };

  function ruleKey(job, rule) {
    var r = SCHEDRULES[rule];
    return r && r.key ? r.key(job) : null;
  }

  function ruleOrder(jobs, rule) {
    var seq = [], k;
    for (k = 0; k < jobs.length; k += 1) seq.push(k);
    if (!SCHEDRULES[rule] || !SCHEDRULES[rule].key) return seq;
    seq.sort(function (a, b) {
      var c = Rcmp(ruleKey(jobs[a], rule), ruleKey(jobs[b], rule));
      return c !== 0 ? c : a - b;
    });
    return seq;
  }

  /* IS THIS ACTUALLY THE RULE'S ORDER?  Two separate questions, answered
     separately.  Counting adjacent pairs that are out of order is not enough
     on its own -- an array that is not a permutation of the jobs has a count
     too, and it can be zero -- so `permutation` and `ordered` come back as two
     booleans and scripts/mathcheck.js asserts both by name. */
  function orderAudit(seq, jobs, rule) {
    var n = jobs.length, seen = [], k;
    for (k = 0; k < n; k += 1) seen.push(0);
    if (seq.length !== n) {
      return { permutation: false, ordered: false, fault: null,
               why: 'the sequence holds ' + seq.length + ' entries where there are ' + n + ' jobs' };
    }
    for (k = 0; k < seq.length; k += 1) {
      if (!(seq[k] >= 0 && seq[k] < n)) {
        return { permutation: false, ordered: false, fault: null,
                 why: 'position ' + (k + 1) + ' names no job in the list' };
      }
      seen[seq[k]] += 1;
    }
    var dup = [], missing = [];
    for (k = 0; k < n; k += 1) {
      if (seen[k] > 1) dup.push(jobs[k].id);
      if (seen[k] === 0) missing.push(jobs[k].id);
    }
    if (dup.length || missing.length) {
      return { permutation: false, ordered: false, fault: null,
               why: (dup.length ? dup.join(' and ') + ' appear' + (dup.length === 1 ? 's' : '') + ' twice' : '')
                    + (dup.length && missing.length ? ' and ' : '')
                    + (missing.length ? missing.join(' and ') + ' not at all' : '') };
    }
    var ordered = true, fault = null;
    if (SCHEDRULES[rule] && SCHEDRULES[rule].key) {
      for (k = 0; k + 1 < n; k += 1) {
        if (Rcmp(ruleKey(jobs[seq[k]], rule), ruleKey(jobs[seq[k + 1]], rule)) > 0) {
          ordered = false;
          if (fault === null) {
            fault = { at: k, before: jobs[seq[k]].id, after: jobs[seq[k + 1]].id,
                      keyBefore: ruleKey(jobs[seq[k]], rule), keyAfter: ruleKey(jobs[seq[k + 1]], rule) };
          }
        }
      }
    }
    return { permutation: true, ordered: ordered, fault: fault,
             why: ordered ? 'every job once, and each key no larger than the next'
                          : 'every job once, but ' + fault.before + ' is placed before ' + fault.after
                            + ' with the larger key' };
  }

  /* ============================================ the second route, and the cross

     `seqObjectives` sweeps forward accumulating a clock.  This one never forms
     a clock: sum C is  sum_k (n - k) p_[k] , because the k-th job's processing
     time is paid by itself and by everything after it, and sum wC is
     sum_k p_[k] * (the weight of everything from k onwards) .  The lateness
     figures are then read BACKWARDS from the makespan.  No line is shared with
     the forward sweep, so an error in one is not an error in the other. */
  function recheckObjectives(seq, jobs) {
    var n = seq.length, total = R0, k, q;
    for (k = 0; k < n; k += 1) total = Radd(total, jobs[seq[k]].p);
    var sumC = R0, sumWC = R0;
    for (k = 0; k < n; k += 1) {
      var p = jobs[seq[k]].p, suffix = R0;
      sumC = Radd(sumC, Rmul(R(BigInt(n - k), 1n), p));
      for (q = k; q < n; q += 1) {
        suffix = Radd(suffix, jobs[seq[q]].w === undefined ? R1 : jobs[seq[q]].w);
      }
      sumWC = Radd(sumWC, Rmul(p, suffix));
    }
    var C = total, sumT = R0, sumU = 0, Lmax = null, Tmax = null;
    for (k = n - 1; k >= 0; k -= 1) {
      var j = jobs[seq[k]], L = Rsub(C, j.d === undefined ? R0 : j.d);
      var T = Rsign(L) > 0 ? L : R0;
      if (Rsign(L) > 0) sumU += 1;
      sumT = Radd(sumT, T);
      if (Lmax === null || Rcmp(L, Lmax) > 0) Lmax = L;
      if (Tmax === null || Rcmp(T, Tmax) > 0) Tmax = T;
      C = Rsub(C, j.p);
    }
    return { sumC: sumC, sumWC: sumWC, sumT: sumT, sumU: sumU, makespan: total,
             Lmax: Lmax === null ? R0 : Lmax, Tmax: Tmax === null ? R0 : Tmax, zero: C };
  }

  /* The two routes, field by field.  Every mode reads `agree` before it prints
     a single number, and prints nothing but the disagreement if it is false. */
  function crossCheck(seq, jobs) {
    var a = seqObjectives(seq, jobs), b = recheckObjectives(seq, jobs), off = [], k;
    var pairs = [['sum C', 'sumC'], ['sum wC', 'sumWC'], ['sum T', 'sumT'],
                 ['L max', 'Lmax'], ['T max', 'Tmax'], ['the makespan', 'makespan']];
    for (k = 0; k < pairs.length; k += 1) {
      if (!Requ(a[pairs[k][1]], b[pairs[k][1]])) off.push(pairs[k][0]);
    }
    if (a.sumU !== b.sumU) off.push('the count of late jobs');
    if (!Rzero(b.zero)) off.push('the clock, which did not return to zero');
    return { agree: off.length === 0, disagree: off, forward: a, second: b };
  }

  /* ==================================================== objectives, by name */
  var SCHEDOBJ = {
    sumC: { label: 'sum of completion times', get: function (o) { return o.sumC; } },
    sumWC: { label: 'weighted sum of completion times', get: function (o) { return o.sumWC; } },
    sumT: { label: 'total tardiness', get: function (o) { return o.sumT; } },
    Lmax: { label: 'maximum lateness', get: function (o) { return o.Lmax; } },
    Tmax: { label: 'maximum tardiness', get: function (o) { return o.Tmax; } },
    sumU: { label: 'number of late jobs', get: function (o) { return R(BigInt(o.sumU), 1n); } },
    makespan: { label: 'makespan', get: function (o) { return o.makespan; } }
  };

  /* Does this sequence attain the exhaustive optimum?  `bestSequence` checks
     every one of the n! orders.  When the cap bites the answer is `checked:
     false` and a reason -- never an unqualified claim. */
  function attainsOptimum(jobs, seq, obj, cap) {
    var get = SCHEDOBJ[obj].get;
    var best = bestSequence(jobs, get, { maxJobs: cap === undefined ? SCHEDPERM : cap });
    if (best.truncated) return { checked: false, why: best.why, attains: null };
    var here = get(seqObjectives(seq, jobs));
    return { checked: true, optimum: best.value, here: here, attains: Requ(here, best.value),
             count: best.count, ties: best.ties, best: best.seq,
             excess: Rsub(here, best.value) };
  }

  /* THE ADJACENT EXCHANGE, RUN RATHER THAN DESCRIBED.  Take the first adjacent
     pair whose swap improves the objective, swap it, and carry on; each step
     records the exact quantity the swap moved and the two ratios that decided
     it.  On sum C and sum wC the walk stops at the rule's own order, and the
     page says so having watched it happen. */
  function exchangeChain(jobs, seq, obj, cap) {
    var get = SCHEDOBJ[obj].get, cur = seq.slice(), steps = [], guard = 0;
    var limit = cap || 64;
    while (guard < limit) {
      var moved = -1, k;
      for (k = 0; k + 1 < cur.length; k += 1) {
        var trial = adjacentSwap(cur, k, jobs);
        if (Rcmp(get(trial.after), get(trial.before)) < 0) { moved = k; break; }
      }
      if (moved < 0) break;
      var sw = adjacentSwap(cur, moved, jobs);
      steps.push({ at: moved, a: jobs[cur[moved]].id, b: jobs[cur[moved + 1]].id,
                   from: get(sw.before), to: get(sw.after),
                   delta: Rsub(get(sw.after), get(sw.before)),
                   deltaSumC: sw.deltaSumC, deltaSumWC: sw.deltaSumWC,
                   ratios: sw.ratios, checked: sw.checkC && sw.checkWC,
                   seq: sw.seq.slice() });
      cur = sw.seq;
      guard += 1;
    }
    return { seq: cur, steps: steps, stalled: guard >= limit,
             objectives: seqObjectives(cur, jobs) };
  }

  /* ============================================================== drawing

     ONE GANTT FOR SIX MODES.  `tracks` is [{name, bars}], a bar is
     {label, start, end, tone, sub, dash, faint}, and `opts.marks` are dashed
     verticals with a caption -- which is how a due date, a deadline or a
     lower bound appears.  A machine, a flow-shop stage and a parallel
     processor are all a track, so nothing below draws its own time axis. */
  function schedXY(v) { return Math.round(v * 10) / 10; }

  function schedGantt(tracks, opts) {
    opts = opts || {};
    var width = opts.width || 660, height = opts.height || 220;
    var left = opts.left === undefined ? 54 : opts.left, right = width - 14;
    var topPad = 24, axis = height - 28, s = '', i, b;
    var span = opts.span;
    if (!span) {
      span = R0;
      for (i = 0; i < tracks.length; i += 1) {
        for (b = 0; b < tracks[i].bars.length; b += 1) {
          if (Rcmp(tracks[i].bars[b].end, span) > 0) span = tracks[i].bars[b].end;
        }
      }
      if (opts.marks) {
        for (i = 0; i < opts.marks.length; i += 1) {
          if (Rcmp(opts.marks[i].at, span) > 0) span = opts.marks[i].at;
        }
      }
    }
    var total = Rnum(span);
    if (!(total > 0)) total = 1;
    var X = function (v) { return left + (right - left) * (Rnum(v) / total); };
    var lanes = Math.max(1, tracks.length);
    var lane = Math.max(16, Math.min(44, (axis - topPad - 6) / lanes));
    var barH = Math.max(11, lane - 12);

    s += '<line x1="' + schedXY(left) + '" y1="' + schedXY(axis) + '" x2="' + schedXY(right)
      + '" y2="' + schedXY(axis) + '" stroke="var(--line-strong)" stroke-width="1" />';
    var ticks = opts.ticks || [];
    for (i = 0; i < ticks.length; i += 1) {
      var tx = X(ticks[i]);
      s += '<line x1="' + schedXY(tx) + '" y1="' + schedXY(axis) + '" x2="' + schedXY(tx)
        + '" y2="' + schedXY(axis + 5) + '" stroke="var(--line-strong)" stroke-width="1" />'
        + '<text x="' + schedXY(tx) + '" y="' + schedXY(axis + 17) + '" text-anchor="middle" '
        + 'font-size="10" fill="var(--muted)">' + Rtext(ticks[i]) + '</text>';
    }
    for (i = 0; opts.marks && i < opts.marks.length; i += 1) {
      var mk = opts.marks[i], mx = X(mk.at), mt = mk.tone || 'amber';
      s += '<line x1="' + schedXY(mx) + '" y1="' + schedXY(topPad - 8) + '" x2="' + schedXY(mx)
        + '" y2="' + schedXY(axis) + '" stroke="var(--' + mt
        + ')" stroke-width="1.3" stroke-dasharray="3 3" />'
        + '<text x="' + schedXY(mx) + '" y="' + schedXY(topPad - 12) + '" text-anchor="middle" '
        + 'font-size="9" fill="var(--' + mt + ')">' + mk.label + '</text>';
    }
    for (i = 0; i < tracks.length; i += 1) {
      var y = topPad + i * lane;
      s += '<text x="' + schedXY(left - 8) + '" y="' + schedXY(y + barH / 2 + 4)
        + '" text-anchor="end" font-size="11" font-weight="600" fill="var(--muted)">'
        + tracks[i].name + '</text>';
      for (b = 0; b < tracks[i].bars.length; b += 1) {
        var bar = tracks[i].bars[b], x0 = X(bar.start), x1 = X(bar.end);
        var w = Math.max(2, x1 - x0), tone = bar.tone || 'cyan';
        s += '<rect x="' + schedXY(x0) + '" y="' + schedXY(y) + '" width="' + schedXY(w)
          + '" height="' + schedXY(barH) + '" rx="3" fill="var(--' + tone + ')" fill-opacity="'
          + (bar.faint ? '0.14' : '0.3') + '" stroke="var(--' + tone + ')" stroke-width="'
          + (bar.wide ? 2.2 : 1.2) + '"' + (bar.dash ? ' stroke-dasharray="4 3"' : '') + ' />';
        if (bar.label && w > 13) {
          s += '<text x="' + schedXY((x0 + x1) / 2) + '" y="' + schedXY(y + barH / 2 + 4)
            + '" text-anchor="middle" font-size="10" font-weight="700" fill="var(--' + tone + ')">'
            + bar.label + '</text>';
        }
        if (bar.sub) {
          s += '<text x="' + schedXY(x1) + '" y="' + schedXY(y + barH + 10) + '" text-anchor="middle" '
            + 'font-size="9" fill="var(--muted)">' + bar.sub + '</text>';
        }
      }
    }
    if (opts.caption) {
      s += '<text x="' + schedXY(width / 2) + '" y="' + schedXY(height - 6) + '" text-anchor="middle" '
        + 'font-size="10" fill="var(--muted)">' + opts.caption + '</text>';
    }
    return s;
  }

  /* The bars a sequence makes on one machine, with the due date carried on
     each so the strip and the table cannot drift apart. */
  function seqBars(seq, jobs, obj, opts) {
    opts = opts || {};
    var bars = [], k, t = R0;
    for (k = 0; k < seq.length; k += 1) {
      var j = jobs[seq[k]], start = t;
      t = Radd(t, j.p);
      var late = j.d !== undefined && Rcmp(t, j.d) > 0;
      bars.push({ label: j.id, start: start, end: t, tone: late ? 'red' : (opts.tone || 'cyan'),
                  sub: opts.sub === false ? null : Rtext(t), wide: late });
    }
    return bars;
  }

  function dueMarks(jobs, seq) {
    var marks = [], k;
    for (k = 0; k < seq.length; k += 1) {
      var j = jobs[seq[k]];
      if (j.d !== undefined) marks.push({ at: j.d, label: 'd' + j.id, tone: 'amber' });
    }
    return marks;
  }

  /* Whole numbers along the axis, at most nine of them, so a strip that runs
     to 40 does not print forty labels. */
  /* A mode that does not ask for a weight or a due date still has to hand
     `seqObjectives` a complete job, because the lateness figures are computed
     whether or not the page prints them.  Filling them in once, here, is the
     alternative to nine modes each remembering to -- and a job whose due date
     was never given has d = 0, so its lateness IS its completion time, which
     is a true statement rather than a placeholder.  */
  function fillJobs(jobs, w, d) {
    var k;
    for (k = 0; k < jobs.length; k += 1) {
      if (jobs[k].w === undefined) jobs[k].w = w === undefined ? R1 : w;
      if (jobs[k].d === undefined) jobs[k].d = d === undefined ? R0 : d;
    }
    return jobs;
  }

  /* The ids of a sequence, which is what a reader reads and types. */
  function seqText(seq, jobs) {
    var out = [], k;
    for (k = 0; k < seq.length; k += 1) out.push(jobs[seq[k]].id);
    return out.join(' ');
  }

  function schedTicks(span) {
    var top = Math.ceil(Rnum(span)), step = Math.max(1, Math.ceil(top / 8)), out = [], v;
    for (v = 0; v <= top; v += step) out.push(R(BigInt(v), 1n));
    return out;
  }

  /* ================================================ the two-machine flow shop

     `bestSequence` cannot answer this and must not be asked to: it scores
     through `seqObjectives`, which is a ONE-machine clock and knows nothing
     about a job waiting for a second machine.  So the enumeration here is its
     own, over the same n! orders, scored by `flowshopMakespan`. */
  function bestFlowshop(jobs, cap) {
    var n = jobs.length, limit = cap === undefined ? SCHEDPERM : cap;
    if (n > limit) {
      return { seq: null, value: null, truncated: true,
               why: n + ' jobs is ' + n + '! orders, past the point where checking them all is a demonstration' };
    }
    var best = null, bestSeq = null, ties = 0, count = 0, used = [], acc = [];
    var go = function () {
      if (acc.length === n) {
        count += 1;
        var v = flowshopMakespan(acc, jobs).value;
        if (best === null || Rcmp(v, best) < 0) { best = v; bestSeq = acc.slice(); ties = 1; }
        else if (Requ(v, best)) ties += 1;
        return;
      }
      for (var k = 0; k < n; k += 1) {
        if (used[k]) continue;
        used[k] = true; acc.push(k); go(); acc.pop(); used[k] = false;
      }
    };
    go();
    return { seq: bestSeq, value: best, ties: ties, count: count, truncated: false };
  }

  /* The bars, read off the same rows the makespan came from.  Machine 1 runs
     back to back; machine 2 starts a job when that job is off machine 1 AND
     machine 2 is free, which is the max the recursion takes. */
  function flowshopBars(seq, jobs) {
    var run = flowshopMakespan(seq, jobs), one = [], two = [], k, t1 = R0;
    for (k = 0; k < seq.length; k += 1) {
      var r = run.rows[k], j = jobs[seq[k]];
      one.push({ label: j.id, start: t1, end: r.off1, tone: 'cyan' });
      t1 = r.off1;
      two.push({ label: j.id, start: Rsub(r.off2, j.p2), end: r.off2, tone: 'purple' });
    }
    return { one: one, two: two, run: run };
  }

  /* THE SECOND ROUTE for the flow shop.  The recursion returns a number; this
     reads the picture back -- machine 1 without gaps, machine 2 never
     overlapping itself, no job on machine 2 before it is off machine 1 -- and
     takes the makespan as the end of the last bar. */
  function flowshopVerify(bars, jobs, seq) {
    var faults = [], k;
    for (k = 0; k < seq.length; k += 1) {
      if (Rcmp(bars.two[k].start, bars.one[k].end) < 0) {
        faults.push(jobs[seq[k]].id + ' reaches machine 2 before it is off machine 1');
      }
      if (k) {
        if (!Requ(bars.one[k].start, bars.one[k - 1].end)) {
          faults.push('machine 1 idles before ' + jobs[seq[k]].id);
        }
        if (Rcmp(bars.two[k].start, bars.two[k - 1].end) < 0) {
          faults.push('machine 2 is asked to run two jobs at once at ' + jobs[seq[k]].id);
        }
      }
    }
    var end = bars.two.length ? bars.two[bars.two.length - 1].end : R0, work = R0;
    for (k = 0; k < seq.length; k += 1) work = Radd(work, jobs[seq[k]].p2);
    return { ok: faults.length === 0, faults: faults, makespan: end,
             work: work, idle: Rsub(end, work) };
  }

  /* ============================================== machines side by side

     THE SECOND ROUTE for a parallel assignment.  `parallelAssign` tracks a
     running load as it places each job; this adds the loads up afterwards from
     the assignment alone, which is how a makespan reported by a heuristic gets
     checked against the schedule the heuristic actually produced. */
  function loadCheck(assign, jobs, m) {
    var loads = [], k, i;
    for (i = 0; i < m; i += 1) loads.push(R0);
    for (k = 0; k < jobs.length; k += 1) {
      if (!(assign[k] >= 0 && assign[k] < m)) {
        return { ok: false, why: jobs[k].id + ' is assigned to no machine at all' };
      }
      loads[assign[k]] = Radd(loads[assign[k]], jobs[k].p);
    }
    var span = loads[0];
    for (i = 1; i < m; i += 1) if (Rcmp(loads[i], span) > 0) span = loads[i];
    return { ok: true, loads: loads, makespan: span };
  }

  /* The bars for one machine's queue, in the order the jobs were placed. */
  function machineBars(assign, jobs, m, order) {
    var tracks = [], t = [], i, k;
    for (i = 0; i < m; i += 1) { tracks.push({ name: 'M' + (i + 1), bars: [] }); t.push(R0); }
    for (k = 0; k < order.length; k += 1) {
      var q = order[k], to = assign[q];
      if (!(to >= 0 && to < m)) continue;
      var start = t[to];
      t[to] = Radd(t[to], jobs[q].p);
      tracks[to].bars.push({ label: jobs[q].id, start: start, end: t[to], sub: Rtext(t[to]) });
    }
    return tracks;
  }
"""


SCHEDSHOP_JS = r"""
  /* ============================================== the job shop, as a picture

     `jobShopAll` scores every orientation by longestPath and returns the best
     mask.  It does not return WHEN each operation runs, and a makespan with no
     schedule under it is a number a reader cannot check.  So this rebuilds the
     arc set for one mask and reads the start times off the same longest path
     -- and then verifies the schedule it drew, which is the independent route:
     no two operations on a machine may overlap, and each job's operations must
     run in its own order. */
  function shopTimes(ops, pairs, mask) {
    var byJob = {}, k, i;
    for (k = 0; k < ops.length; k += 1) {
      (byJob[ops[k].job] = byJob[ops[k].job] || []).push(k);
    }
    var nodes = ['S'], arcs = [];
    for (k = 0; k < ops.length; k += 1) nodes.push('o' + k);
    nodes.push('T');
    for (var jkey in byJob) {
      if (!Object.prototype.hasOwnProperty.call(byJob, jkey)) continue;
      var chain = byJob[jkey];
      arcs.push({ from: 'S', to: 'o' + chain[0], cost: R0 });
      for (i = 1; i < chain.length; i += 1) {
        arcs.push({ from: 'o' + chain[i - 1], to: 'o' + chain[i], cost: ops[chain[i - 1]].dur });
      }
      arcs.push({ from: 'o' + chain[chain.length - 1], to: 'T', cost: ops[chain[chain.length - 1]].dur });
    }
    for (k = 0; k < pairs.length; k += 1) {
      var a = pairs[k][0], b = pairs[k][1];
      if (mask & (1 << k)) arcs.push({ from: 'o' + a, to: 'o' + b, cost: ops[a].dur });
      else arcs.push({ from: 'o' + b, to: 'o' + a, cost: ops[b].dur });
    }
    var lp = longestPath(nodes, arcs, 'S', 'T');
    if (lp.cycle) return { cycle: lp.cycle, start: null, makespan: null };
    var ix = netIndex(nodes), start = [], critical = {};
    for (k = 0; k < ops.length; k += 1) start.push(lp.dist[ix['o' + k]]);
    for (k = 0; k < lp.path.length; k += 1) critical[lp.path[k]] = true;
    return { start: start, makespan: lp.value, cycle: null, path: lp.path, critical: critical };
  }

  /* The schedule, checked as a schedule.  A makespan is a claim about a
     picture, and this is the picture being read back. */
  function shopFeasible(ops, start) {
    var bad = [], k, q;
    for (k = 0; k < ops.length; k += 1) {
      for (q = k + 1; q < ops.length; q += 1) {
        if (ops[k].machine !== ops[q].machine) continue;
        var e1 = Radd(start[k], ops[k].dur), e2 = Radd(start[q], ops[q].dur);
        if (Rcmp(start[k], e2) < 0 && Rcmp(start[q], e1) < 0) {
          bad.push(ops[k].job + '/' + ops[k].machine + ' overlaps ' + ops[q].job + '/' + ops[q].machine);
        }
      }
    }
    var byJob = {};
    for (k = 0; k < ops.length; k += 1) (byJob[ops[k].job] = byJob[ops[k].job] || []).push(k);
    for (var jkey in byJob) {
      if (!Object.prototype.hasOwnProperty.call(byJob, jkey)) continue;
      var chain = byJob[jkey];
      for (k = 1; k < chain.length; k += 1) {
        if (Rcmp(start[chain[k]], Radd(start[chain[k - 1]], ops[chain[k - 1]].dur)) < 0) {
          bad.push(jkey + ' starts its step ' + (k + 1) + ' before step ' + k + ' has finished');
        }
      }
    }
    var span = R0;
    for (k = 0; k < ops.length; k += 1) {
      var e = Radd(start[k], ops[k].dur);
      if (Rcmp(e, span) > 0) span = e;
    }
    return { ok: bad.length === 0, faults: bad, makespan: span };
  }

  /* The operations a reader types:  J1 M1 3  -- job, machine, duration, in the
     job's own order.  Two jobs may share a machine and a job may visit a
     machine twice; nothing here assumes a rectangle. */
  function parseOps(text) {
    var cl = schedClauses(text), ops = [], i;
    if (!cl.length) return { bad: 'there are no operations here yet' };
    if (cl.length > 8) {
      return { bad: 'that is ' + cl.length + ' operations, and this lab lays out at most 8' };
    }
    for (i = 0; i < cl.length; i += 1) {
      var m = /^([A-Za-z][A-Za-z0-9]{0,3})\s+([A-Za-z][A-Za-z0-9]{0,3})\s+(.*)$/.exec(cl[i]);
      if (!m) {
        return { bad: '"' + esc(cl[i]) + '" is not an operation: write the job, the machine, then how long' };
      }
      var v = Rread(m[3].trim());
      if (v === null) return { bad: '"' + esc(m[3]) + '" in "' + esc(cl[i]) + '" is not a number' };
      if (Rsign(v) <= 0) return { bad: 'the step "' + esc(cl[i]) + '" takes no time at all' };
      ops.push({ job: m[1], machine: m[2], dur: v });
    }
    return { ops: ops };
  }
"""


SCHEDCRASH_JS = r"""
  /* ================================================== crashing, and its check

     `crashModel` builds the linear programme and `rhsCurve` walks the deadline
     row exactly.  Neither of them knows what a project is, so neither can tell
     a reader whether the plan it priced actually finishes on time.  That is
     what `crashVerify` does: it takes the crash amounts out of the solved x,
     subtracts them from the normal durations, and runs CPM on the result.  The
     deadline is met because a forward and a backward pass say so, not because
     a solver reported a feasible basis. */
  function parseActivities(text) {
    var cl = schedClauses(text), acts = [], seen = {}, i, k;
    if (!cl.length) return { bad: 'there are no activities here yet' };
    if (cl.length > 7) {
      return { bad: 'that is ' + cl.length + ' activities, and this lab crashes at most 7' };
    }
    for (i = 0; i < cl.length; i += 1) {
      var m = /^([A-Za-z][A-Za-z0-9]{0,3})\s+([^|]*)(?:\|\s*(.*))?$/.exec(cl[i]);
      if (!m) return { bad: '"' + esc(cl[i]) + '" is not an activity' };
      var vals = m[2].trim().split(':');
      if (vals.length !== 4) {
        return { bad: '"' + esc(cl[i]) + '" gives ' + vals.length
                      + ' numbers; an activity carries normal time, crash time, normal cost and '
                      + 'crash cost — four of them, colon separated, then | and its predecessors' };
      }
      var nums = [], q;
      for (q = 0; q < 4; q += 1) {
        var v = Rread(vals[q].trim());
        if (v === null) return { bad: '"' + esc(vals[q]) + '" in "' + esc(cl[i]) + '" is not a number' };
        nums.push(v);
      }
      if (Rsign(nums[0]) <= 0) return { bad: esc(m[1]) + ' takes no time at all' };
      if (Rcmp(nums[1], nums[0]) > 0) {
        return { bad: esc(m[1]) + ' crashes to ' + Rtext(nums[1]) + ', which is LONGER than its normal '
                      + Rtext(nums[0]) + '; crashing shortens' };
      }
      if (Rsign(nums[1]) < 0) return { bad: esc(m[1]) + ' crashes to a negative duration' };
      if (Rcmp(nums[3], nums[2]) < 0) {
        return { bad: 'crashing ' + esc(m[1]) + ' is cheaper than not crashing it, which makes the '
                      + 'normal plan the wrong baseline rather than the cheap one' };
      }
      if (seen[m[1]]) return { bad: 'there are two activities called ' + esc(m[1]) };
      seen[m[1]] = true;
      var pred = (m[3] || '').split(/[\s,]+/).filter(function (t) { return t.length; });
      acts.push({ id: m[1], normal: nums[0], crash: nums[1], normalCost: nums[2],
                  crashCost: nums[3], pred: pred });
    }
    for (i = 0; i < acts.length; i += 1) {
      for (k = 0; k < acts[i].pred.length; k += 1) {
        if (!seen[acts[i].pred[k]]) {
          return { bad: esc(acts[i].id) + ' waits for ' + esc(acts[i].pred[k])
                        + ', and there is no activity by that name' };
        }
      }
    }
    if (cpmPasses(acts.map(function (a) { return { id: a.id, dur: a.normal, pred: a.pred }; })).cycle) {
      return { bad: 'these activities wait for each other in a circle, so nothing can start' };
    }
    return { acts: acts };
  }

  /* The crash amounts out of a solved x, and the durations they leave. */
  function crashPlan(cm, sol) {
    var n = cm.activities.length, y = [], dur = [], bill = R0, i;
    for (i = 0; i < n; i += 1) {
      var amount = sol.x[n + i];
      y.push(amount);
      dur.push(Rsub(cm.activities[i].normal, amount));
      bill = Radd(bill, Rmul(cm.rates[i], amount));
    }
    return { y: y, dur: dur, crashBill: bill, finish: sol.x[2 * n],
             total: Radd(cm.normalCost, bill) };
  }

  /* THE INDEPENDENT ROUTE.  CPM on the crashed durations, with no reference to
     the tableau that produced them. */
  function crashVerify(cm, plan, deadline) {
    var acts = cm.activities.map(function (a, i) {
      return { id: a.id, dur: plan.dur[i], pred: a.pred };
    });
    var cp = cpmPasses(acts);
    var overspent = [], i;
    for (i = 0; i < cm.activities.length; i += 1) {
      var room = Rsub(cm.activities[i].normal, cm.activities[i].crash);
      if (Rcmp(plan.y[i], room) > 0) overspent.push(cm.activities[i].id);
      if (Rsign(plan.y[i]) < 0) overspent.push(cm.activities[i].id + ' (negative)');
    }
    return { cpm: cp, makespan: cp.makespan, meets: Rcmp(cp.makespan, deadline) <= 0,
             overspent: overspent, ok: Rcmp(cp.makespan, deadline) <= 0 && !overspent.length,
             critical: cp.critical, paths: cp.paths };
  }

  /* The exact time-cost curve, and each piece confirmed by a FRESH solve at
     its own left endpoint.  rhsCurve walks the basis; a fresh lpSolve does not
     know the walk happened, so the two agreeing is evidence rather than
     bookkeeping. */
  function crashCurve(acts, lo, hi, opts) {
    var cm = crashModel(acts, hi);
    var curve = rhsCurve(cm.model, cm.deadlineRow, lo, hi, opts || { rule: 'bland', maxPivots: 400 });
    var confirmed = 0, checked = 0, k;
    for (k = 0; k < curve.pieces.length; k += 1) {
      var fresh = lpSolve(crashModel(acts, curve.pieces[k].from).model,
                          opts || { rule: 'bland', maxPivots: 400 });
      checked += 1;
      if (fresh.status === 'optimal' && Requ(fresh.zOrig, curve.pieces[k].z)) confirmed += 1;
    }
    return { curve: curve, pieces: curve.pieces, confirmed: confirmed, checked: checked,
             normalCost: cm.normalCost, rates: cm.rates };
  }

  /* A line, drawn from exact pieces.  The bend is the point, so every
     breakpoint gets a dot and the slope is printed beside the segment. */
  function crashPlot(pieces, opts) {
    opts = opts || {};
    var width = opts.width || 520, height = opts.height || 260;
    var left = 52, right = width - 16, top = 18, bottom = height - 30;
    if (!pieces.length) return '';
    var xlo = pieces[0].from, xhi = pieces[pieces.length - 1].to;
    var ylo = null, yhi = null, k;
    for (k = 0; k < pieces.length; k += 1) {
      var vals = [pieces[k].z, pieces[k].zEnd];
      for (var q = 0; q < 2; q += 1) {
        var v = opts.add ? Radd(vals[q], opts.add) : vals[q];
        if (ylo === null || Rcmp(v, ylo) < 0) ylo = v;
        if (yhi === null || Rcmp(v, yhi) > 0) yhi = v;
      }
    }
    var x0 = Rnum(xlo), x1 = Rnum(xhi), y0 = Rnum(ylo), y1 = Rnum(yhi);
    if (x1 === x0) x1 = x0 + 1;
    if (y1 === y0) y1 = y0 + 1;
    var X = function (v) { return left + (right - left) * ((Rnum(v) - x0) / (x1 - x0)); };
    var Y = function (v) { return bottom - (bottom - top) * ((Rnum(v) - y0) / (y1 - y0)); };
    var s = '<line x1="' + schedXY(left) + '" y1="' + schedXY(bottom) + '" x2="' + schedXY(right)
      + '" y2="' + schedXY(bottom) + '" stroke="var(--line-strong)" stroke-width="1" />'
      + '<line x1="' + schedXY(left) + '" y1="' + schedXY(top) + '" x2="' + schedXY(left)
      + '" y2="' + schedXY(bottom) + '" stroke="var(--line-strong)" stroke-width="1" />';
    for (k = 0; k < pieces.length; k += 1) {
      var p = pieces[k];
      var a = opts.add ? Radd(p.z, opts.add) : p.z, b = opts.add ? Radd(p.zEnd, opts.add) : p.zEnd;
      s += '<line x1="' + schedXY(X(p.from)) + '" y1="' + schedXY(Y(a)) + '" x2="' + schedXY(X(p.to))
        + '" y2="' + schedXY(Y(b)) + '" stroke="var(--cyan)" stroke-width="2.2" />'
        + '<circle cx="' + schedXY(X(p.from)) + '" cy="' + schedXY(Y(a))
        + '" r="3.2" fill="var(--purple)" />'
        + '<text x="' + schedXY((X(p.from) + X(p.to)) / 2) + '" y="' + schedXY((Y(a) + Y(b)) / 2 - 6)
        + '" text-anchor="middle" font-size="9" fill="var(--muted)">' + Rtext(Rneg(p.slope))
        + ' a day</text>';
    }
    var last = pieces[pieces.length - 1];
    var lastY = opts.add ? Radd(last.zEnd, opts.add) : last.zEnd;
    s += '<circle cx="' + schedXY(X(last.to)) + '" cy="' + schedXY(Y(lastY)) + '" r="3.2" fill="var(--purple)" />';
    s += '<text x="' + schedXY(left) + '" y="' + schedXY(bottom + 16) + '" text-anchor="middle" '
      + 'font-size="10" fill="var(--muted)">' + Rtext(xlo) + '</text>'
      + '<text x="' + schedXY(right) + '" y="' + schedXY(bottom + 16) + '" text-anchor="middle" '
      + 'font-size="10" fill="var(--muted)">' + Rtext(xhi) + '</text>'
      + '<text x="' + schedXY(left - 6) + '" y="' + schedXY(top + 4) + '" text-anchor="end" '
      + 'font-size="10" fill="var(--muted)">' + Rtext(yhi) + '</text>'
      + '<text x="' + schedXY(left - 6) + '" y="' + schedXY(bottom) + '" text-anchor="end" '
      + 'font-size="10" fill="var(--muted)">' + Rtext(ylo) + '</text>'
      + '<text x="' + schedXY(width / 2) + '" y="' + schedXY(height - 6) + '" text-anchor="middle" '
      + 'font-size="10" fill="var(--muted)">' + (opts.caption || 'the deadline, in days') + '</text>';
    return s;
  }
"""


# ---------------------------------------------------------------------------
# WHICH BLOCKS EACH MODE SHIPS. The rule is integer.py's: a block belongs in a
# mode's list when that mode CALLS something in it. Every block here is
# top-level function declarations, so a function that is present but unused
# costs bytes and nothing else, while one that is called but absent throws on
# the first redraw -- which scripts/labcheck.js catches on every page.
#
# Seven of the nine modes are one machine and a list of jobs; they ship 9.5 KB
# gzipped of engine between them. `jobshop` adds NET_JS for longestPath and
# `crash` adds the whole simplex and the ranging block, because the exact
# time-cost curve is rhsCurve on the deadline row rather than a scan. NET_JS's
# `submatrixDet` is the only thing in it that needs MATRIX_JS and no mode here
# calls it, so `jobshop` does not pay for the matrix block; `crash` does,
# because DUAL_JS does.
# ---------------------------------------------------------------------------

_ONE = RATIONAL_JS + FORMAT_JS + ORFMT_JS + SCHED_JS + SCHEDKIT_JS
_SHOP = RATIONAL_JS + FORMAT_JS + ORFMT_JS + NET_JS + SCHED_JS + SCHEDKIT_JS + SCHEDSHOP_JS
_CRASH = (RATIONAL_JS + FORMAT_JS + MATRIX_JS + ORFMT_JS + TABLEAU_JS + PHASE_JS + DUAL_JS
          + RANGE_JS + NET_JS + SCHED_JS + SCHEDKIT_JS + SCHEDCRASH_JS)

_MODE_JS = {
    "objectives": _ONE,
    "spt": _ONE,
    "wspt": _ONE,
    "edd": _ONE,
    "late": _ONE,
    "flowshop": _ONE,
    "parallel": _ONE,
    "jobshop": _SHOP,
    "crash": _CRASH,
}


# ---------------------------------------------------------------------------
# Control furniture. The same shapes the rest of the library uses, so a reader
# crossing a course boundary meets the same widgets. Drawings use only the two
# viewBox widths theme.py gives a horizontal-scroll minimum -- 520 and 660.
# ---------------------------------------------------------------------------


def _attr(text):
    return (str(text).replace("&", "&amp;").replace('"', "&quot;")
            .replace("<", "&lt;").replace(">", "&gt;"))


def _range(cid, label, lo, hi, value, step=1):
    return (
        "        <div>\n"
        '          <div class="range-row"><label class="small-copy" for="%s">%s</label>'
        '<span class="range-value" id="%sOut">%s</span></div>\n'
        '          <input id="%s" type="range" min="%s" max="%s" step="%s" value="%s" />\n'
        "        </div>\n" % (cid, label, cid, value, cid, lo, hi, step, value)
    )


def _select(cid, label, options, chosen):
    opts = "".join(
        '<option value="%s"%s>%s</option>'
        % (_attr(v), " selected" if str(v) == str(chosen) else "", t)
        for v, t in options
    )
    return (
        '        <div class="field">\n          <label for="%s">%s</label>\n'
        '          <select id="%s">%s</select>\n        </div>\n' % (cid, label, cid, opts)
    )


def _text(cid, label, value):
    """A text box whose default really is in the markup.

    Nothing this kit asks a reader to type contains a `>` -- a job is a name
    and some numbers, an operation is a job, a machine and a number, an
    activity ends with a `|` and its predecessors -- so the empty-value
    workaround network.py needs is not needed here, and the value a reader
    sees is the value scripts/labcheck.js runs the lab against.
    """
    return (
        '        <div class="field">\n          <label for="%s">%s</label>\n'
        '          <input id="%s" type="text" value="%s" inputmode="text" autocomplete="off">\n'
        "        </div>\n" % (cid, label, cid, _attr(value))
    )


def _kpis(items):
    cells = "".join(
        '          <div class="kpi"><span>%s</span><strong id="%s">&mdash;</strong></div>\n' % (label, cid)
        for label, cid in items
    )
    return '        <div class="kpi-grid">\n%s        </div>\n' % cells


def _hint(cid, text):
    return '        <p class="small-copy" id="%s" style="margin:0;">%s</p>' % (cid, text)


def _toolbar(name, subtitle, legend):
    swatches = "".join(
        '<span class="tone-%s"><i class="legend-swatch"></i>%s</span>' % (tone, text)
        for tone, text in legend
    )
    return (
        '      <div class="lab-toolbar">\n'
        '        <div class="lab-title"><strong>%s</strong><span>%s</span></div>\n'
        '        <div class="inline-legend">%s</div>\n'
        "      </div>\n" % (name, subtitle, swatches)
    )


def _stage(inner):
    return '      <div class="lab-stage">%s</div>\n' % inner


def _svg(cid, box, alt):
    return '<svg id="%s" viewBox="%s" role="img" aria-label="%s"></svg>' % (cid, box, alt)


def _table(cid, top=12):
    return ('      <div class="table-wrap" style="margin-top:%dpx;">'
            '<table class="tt" id="%s"></table></div>\n' % (top, cid))


def _banner(cid):
    return '      <div class="status-banner" id="%s" style="margin-top:12px;"></div>' % cid


def _js(text):
    """A JavaScript single-quoted string literal for a preset's own text."""
    return "'" + str(text).replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n") + "'"


def _presets_js(name, presets, keys):
    """The preset table, as data the script reads -- not as branches.

    Every preset goes through the same parser the reader's own typing does, so
    a preset cannot show a number the typed version would not.
    """
    rows = []
    for p in presets:
        body = ", ".join("%s: %s" % (k, _js(p[k])) for k in keys)
        rows.append("    '%s': { %s }" % (p["id"], body))
    return "  var %s = {\n%s\n  };\n" % (name, ",\n".join(rows))


def _options(presets):
    return [(p["id"], p["label"]) for p in presets]


def _choose(cfg, mode, presets, default):
    """The preset this lesson opens on, or a refusal.

    A preset that fell back to a default would render the WRONG worked example
    under the right lesson's prose, and nothing in the suite would notice
    because the lab still builds and still draws. So an unknown one raises, the
    same way an unknown mode does.
    """
    name = str(cfg.get("preset", default))
    for p in presets:
        if p["id"] == name:
            return p
    raise ValueError(
        "schedule_lab: mode %r has no preset %r; its presets are %s"
        % (mode, name, ", ".join(sorted(p["id"] for p in presets)))
    )


# ---------------------------------------------------------------------------
# L1 -- objectives: a schedule is good at one thing and bad at another
# ---------------------------------------------------------------------------

_OB_PRESETS = [
    {
        "id": "mixed",
        "label": "five jobs, and no order is best at everything",
        "jobs": "A 6:1:8, B 4:2:4, C 5:4:12, D 3:3:6, E 7:1:20",
        "seq": "A B C D E",
        "note": "the order they arrived in, which is optimal for nothing at all",
    },
    {
        "id": "weights",
        "label": "a long job that everyone is waiting for",
        "jobs": "A 2:1:9, B 8:5:10, C 3:1:4, D 6:4:14",
        "seq": "A B C D",
        "note": "B is the longest and the heaviest, and the two rules disagree about it",
    },
    {
        "id": "tight",
        "label": "due dates nothing can meet",
        "jobs": "A 5:2:5, B 4:1:6, C 6:3:7, D 2:2:9",
        "seq": "A B C D",
        "note": "seventeen hours of work against a last due date of nine",
    },
]


def _objectives(cfg):
    chosen = _choose(cfg, "objectives", _OB_PRESETS, "mixed")

    markup = (
        _toolbar(
            "One sequence, every objective at once",
            "a schedule is not good or bad; it is good at one thing and bad at another",
            [("cyan", "a job that finishes on time"), ("red", "a job that finishes late"),
             ("amber", "its due date"), ("green", "an objective this order is optimal for")],
        )
        + _stage(_svg("obPlot", "0 0 660 210",
                      "The sequence as a strip of time, each job labelled and each due date marked.")
                 + _svg("obBars", "0 0 660 66",
                        "A strip comparing this order with the exhaustive optimum for each objective."))
        + _table("obJobs")
        + _table("obObj")
        + _banner("obStatus")
    )
    controls = (
        _select("obPreset", "Worked example", _options(_OB_PRESETS), chosen["id"])
        + _text("obJobsIn", "Jobs, as name time:weight:due", chosen["jobs"])
        + _text("obSeq", "The order to run them in", chosen["seq"])
        + _select("obRule", "Fill that order from a rule",
                  [("KEEP", "leave what is typed"), ("SPT", "shortest processing time first"),
                   ("WSPT", "Smith's ratio p/w"), ("EDD", "earliest due date first"),
                   ("WEIGHT", "heaviest weight first"), ("LPT", "longest processing time first")],
                  "KEEP")
        + _kpis([
            ("Sum of completion times", "obSumC"),
            ("Weighted sum, sum wC", "obSumWC"),
            ("Maximum lateness, L max", "obLmax"),
            ("Total tardiness, sum T", "obSumT"),
            ("Jobs finishing late", "obLate"),
            ("Objectives this order is best at", "obBestAt"),
        ])
        + _hint(
            "obHint",
            "A job is <span class=\"tt\">name time:weight:due</span>. Every figure below is computed "
            "twice by two different routes and shown only if they agree, and each objective is "
            "compared against the best of all <span class=\"tt\">n!</span> orders &mdash; so "
            "&ldquo;optimal&rdquo; here means checked rather than claimed.",
        )
    )

    script = _MODE_JS["objectives"] + r"""
""" + _presets_js("OBP", _OB_PRESETS, ["jobs", "seq", "note"]) + r"""
  var presetIn = document.getElementById('obPreset');
  var jobsIn = document.getElementById('obJobsIn'), seqIn = document.getElementById('obSeq');
  var ruleIn = document.getElementById('obRule');
  var plot = document.getElementById('obPlot'), bars = document.getElementById('obBars');
  var jobsT = document.getElementById('obJobs'), objT = document.getElementById('obObj');
  var status = document.getElementById('obStatus');
  var KPIS = ['obSumC', 'obSumWC', 'obLmax', 'obSumT', 'obLate', 'obBestAt'];
  var SHOW = ['sumC', 'sumWC', 'Lmax', 'Tmax', 'sumT', 'sumU'];

  function blank(why) {
    plot.innerHTML = ''; bars.innerHTML = ''; jobsT.innerHTML = ''; objT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> A job is a name, a space, then '
      + 'its processing time, its weight and its due date separated by colons.';
  }

  function redraw() {
    var parsed = parseJobs(jobsIn.value, ['p', 'w', 'd'],
                           ['the processing time', 'the weight', 'the due date']);
    if (parsed.bad) { blank(parsed.bad); return; }
    var jobs = parsed.jobs;
    var ps = parseSeq(seqIn.value, jobs);
    if (ps.bad) { blank(ps.bad); return; }
    var seq = ps.seq, cross = crossCheck(seq, jobs);
    if (!cross.agree) {
      blank('the two ways of computing ' + cross.disagree.join(' and ') + ' disagree, so nothing here '
            + 'is trustworthy and nothing is shown');
      return;
    }
    var o = cross.forward, i;

    plot.innerHTML = schedGantt([{ name: 'machine', bars: seqBars(seq, jobs, o) }], {
      width: 660, height: 210, marks: dueMarks(jobs, seq), ticks: schedTicks(o.makespan),
      caption: 'each bar is labelled with the job and the clock it finishes at; the dashed lines are due dates'
    });

    var rows = '';
    for (i = 0; i < o.rows.length; i += 1) {
      var r = o.rows[i];
      rows += tr([rowhead((i + 1) + '. ' + r.id), td(Rtext(r.p)), td(Rtext(r.w)), td(Rtext(r.d)),
                  td(Rtext(r.C)), td(Rtext(r.L)), td(Rtext(r.T)),
                  td(r.U ? tone('late', 'red') : tone('on time', 'green'))],
                 r.U ? 'tone-red' : null);
    }
    jobsT.innerHTML = '<caption>The schedule, job by job</caption><thead>'
      + tr([th('position'), th('p'), th('w'), th('due'), th('finishes'), th('lateness'),
            th('tardiness'), th('verdict')]) + '</thead><tbody>' + rows + '</tbody>';

    var best = {}, wins = 0, strip = '', wide = 660 / SHOW.length;
    var orows = '';
    for (i = 0; i < SHOW.length; i += 1) {
      var key = SHOW[i], got = SCHEDOBJ[key].get(o);
      var chk = attainsOptimum(jobs, seq, key);
      best[key] = chk;
      var x = wide * (i + 0.5);
      var good = chk.checked && chk.attains;
      if (good) wins += 1;
      strip += '<text x="' + Math.round(x) + '" y="20" text-anchor="middle" font-size="11" '
        + 'font-weight="700" fill="var(--' + (good ? 'green' : 'cyan') + ')">' + key + ' ' + Rtext(got)
        + '</text><text x="' + Math.round(x) + '" y="38" text-anchor="middle" font-size="10" '
        + 'fill="var(--muted)">' + (chk.checked ? 'best is ' + Rtext(chk.optimum) : 'not checked')
        + '</text><text x="' + Math.round(x) + '" y="54" text-anchor="middle" font-size="9" '
        + 'fill="var(--' + (good ? 'green' : 'muted') + ')">' + (good ? 'optimal' : 'beaten') + '</text>';
      orows += tr([rowhead(SCHEDOBJ[key].label), td(Rtext(got)),
                   td(chk.checked ? Rtext(chk.optimum) : 'not checked'),
                   td(chk.checked ? seqText(chk.best, jobs) : '—'),
                   td(chk.checked ? Rtext(chk.excess) : '—'),
                   td(good ? tone('optimal', 'green') : tone('beaten', 'red'))],
                  good ? 'tone-green' : null);
    }
    bars.innerHTML = strip;
    objT.innerHTML = '<caption>Every objective, against the best of all ' + (best.sumC.checked
        ? best.sumC.count : 'n!') + ' orders</caption><thead>'
      + tr([th('objective'), th('this order'), th('the best there is'), th('an order that attains it'),
            th('what this order costs'), th('verdict')]) + '</thead><tbody>' + orows + '</tbody>';

    document.getElementById('obSumC').textContent = Rtext(o.sumC);
    document.getElementById('obSumWC').textContent = Rtext(o.sumWC);
    document.getElementById('obLmax').textContent = Rtext(o.Lmax);
    document.getElementById('obSumT').textContent = Rtext(o.sumT);
    document.getElementById('obLate').textContent = o.sumU + ' of ' + jobs.length;
    document.getElementById('obBestAt').textContent = wins + ' of ' + SHOW.length;

    var beaten = [];
    for (i = 0; i < SHOW.length; i += 1) {
      if (best[SHOW[i]].checked && !best[SHOW[i]].attains) beaten.push(SHOW[i]);
    }
    status.innerHTML = '<strong>The makespan is ' + tone(Rtext(o.makespan), 'cyan')
      + ' whatever order you choose</strong> — one machine, no idle time, so the last job finishes when '
      + 'the work runs out. Everything else moves. This order is optimal for '
      + (wins ? tone(wins + ' of the six objectives', 'green') : tone('none of the six', 'red'))
      + (beaten.length
          ? ' and is beaten on ' + tone(beaten.join(', '), 'red') + ' — by a different order in each case, '
            + 'which is why there is no such thing as the good schedule. '
          : '. ')
      + 'Both routes to these figures agree: the forward sweep and the position-weighted sum '
      + tone('sum (n − k) p', 'muted') + ' give the same sum C, and the lateness column was read '
      + 'backwards from the makespan rather than forwards from zero.';
  }

  function apply() {
    var p = OBP[presetIn.value];
    if (!p) return;
    jobsIn.value = p.jobs; seqIn.value = p.seq; ruleIn.value = 'KEEP';
    redraw();
  }
  function fill() {
    if (ruleIn.value === 'KEEP') { redraw(); return; }
    var parsed = parseJobs(jobsIn.value, ['p', 'w', 'd'],
                           ['the processing time', 'the weight', 'the due date']);
    if (parsed.bad) { redraw(); return; }
    seqIn.value = seqText(ruleOrder(parsed.jobs, ruleIn.value), parsed.jobs);
    redraw();
  }
  presetIn.addEventListener('change', apply);
  ruleIn.addEventListener('change', fill);
  jobsIn.addEventListener('input', redraw);
  seqIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="One sequence, every objective at once",
        subtitle="The makespan never moves; everything else does, and no order wins on all of them",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Type the jobs and an order, and watch eight figures move"),
        panel_intro=cfg.get(
            "panel_intro",
            "Each objective is computed from what you type, checked against a second route that "
            "shares no arithmetic with the first, and then compared with the best of every possible "
            "order. On this example: " + chosen["note"] + ".",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L2 and L3 -- spt and wspt: the adjacent exchange, run rather than described
#
# One builder serves both, because they ARE one argument: swap two neighbours,
# only those two change completion time, and the whole of the difference is one
# subtraction. What differs is which subtraction -- p_b - p_a unweighted, and
# w_a p_b - w_b p_a weighted -- and which rival rule the contrast is drawn
# against. Writing it twice would let the two drift, and the second lesson's
# whole claim is that it is the first one again with weights on.
# ---------------------------------------------------------------------------

_SPT_PRESETS = [
    {
        "id": "worst",
        "label": "the longest job first, which is the worst order there is",
        "jobs": "A 9, B 2, C 6, D 3, E 5",
        "seq": "A C E D B",
        "note": "every job waits behind the nine-hour one",
    },
    {
        "id": "near",
        "label": "one pair out of order",
        "jobs": "A 2, B 3, C 7, D 5, E 6",
        "seq": "A B C D E",
        "note": "C and D are the only adjacent pair the rule disagrees with",
    },
    {
        "id": "ties",
        "label": "two jobs the same length",
        "jobs": "A 4, B 4, C 1, D 7",
        "seq": "D A B C",
        "note": "A and B tie, so the rule has to say what it does with a tie",
    },
]

_WSPT_PRESETS = [
    {
        "id": "ratio",
        "label": "the heaviest job is also the longest",
        "jobs": "A 3:1, B 8:4, C 2:3, D 6:2",
        "seq": "A B C D",
        "note": "heaviest first says B, the ratio says C, and only one of them is right",
    },
    {
        "id": "shortest",
        "label": "the shortest job is nearly worthless",
        "jobs": "A 1:1, B 4:8, C 3:2, D 5:5",
        "seq": "A C D B",
        "note": "shortest first puts A at the front and it is worth almost nothing",
    },
    {
        "id": "equal",
        "label": "equal weights, so the ratio is the time again",
        "jobs": "A 5:2, B 3:2, C 8:2, D 2:2",
        "seq": "C A B D",
        "note": "with every weight the same, Smith's rule collapses back to SPT",
    },
]

_EXCHANGE = {
    "spt": {
        "presets": _SPT_PRESETS,
        "default": "worst",
        "keys": "['p']",
        "labels": "['the processing time']",
        "spec": "name time",
        "obj": "sumC",
        "rule": "SPT",
        "rivals": "['LPT', 'FCFS']",
        "title": "Shortest processing time, and the exchange that proves it",
        "subtitle": "Swap two neighbours and the sum of completion times moves by p_b &minus; p_a, and by nothing else",
        "quantity": "p<sub>b</sub> &minus; p<sub>a</sub>",
        "compares": "the two processing times",
        "legend": [("cyan", "the order you typed"), ("green", "after the swap, if it improves"),
                   ("red", "after the swap, if it does not"), ("purple", "the rule's own order")],
    },
    "wspt": {
        "presets": _WSPT_PRESETS,
        "default": "ratio",
        "keys": "['p', 'w']",
        "labels": "['the processing time', 'the weight']",
        "spec": "name time:weight",
        "obj": "sumWC",
        "rule": "WSPT",
        "rivals": "['WEIGHT', 'SPT', 'FCFS']",
        "title": "Smith's rule, and the same exchange with weights on",
        "subtitle": "The swap moves sum wC by w_a p_b &minus; w_b p_a, which is negative exactly when p_a/w_a &gt; p_b/w_b",
        "quantity": "w<sub>a</sub>p<sub>b</sub> &minus; w<sub>b</sub>p<sub>a</sub>",
        "compares": "the two ratios p/w",
        "legend": [("cyan", "the order you typed"), ("green", "after the swap, if it improves"),
                   ("red", "after the swap, if it does not"), ("purple", "the rule's own order")],
    },
}


def _exchange(cfg, mode):
    spec = _EXCHANGE[mode]
    chosen = _choose(cfg, mode, spec["presets"], spec["default"])

    markup = (
        _toolbar(spec["title"], spec["subtitle"], spec["legend"])
        + _stage(_svg("exPlot", "0 0 660 250",
                      "The order you typed and the same order with one adjacent pair swapped, "
                      "drawn on the same time axis."))
        + _table("exSwap")
        + _table("exChain")
        + _table("exRules")
        + _banner("exStatus")
    )
    controls = (
        _select("exPreset", "Worked example", _options(spec["presets"]), chosen["id"])
        + _text("exJobs", "Jobs, as " + spec["spec"], chosen["jobs"])
        + _text("exSeq", "The order to run them in", chosen["seq"])
        + _range("exPos", "Swap the job in this position with the next", 1, 7, 1)
        + _kpis([
            ("The objective, as typed", "exNow"),
            ("After the swap", "exAfter"),
            ("The exact quantity the swap moved", "exDelta"),
            ("The rule's own order scores", "exRule"),
            ("The best of every order", "exBest"),
            ("Swaps from here to the rule", "exSteps"),
        ])
        + _hint(
            "exHint",
            "Only the two swapped jobs change completion time &mdash; everything before them finishes "
            "at the same clock and everything after them finishes when the same total amount of work "
            "is done. So the whole difference is one subtraction, and the lab prints it beside a full "
            "recomputation of both orders to show that nothing else moved.",
        )
    )

    script = _MODE_JS[mode] + r"""
""" + _presets_js("EXP", spec["presets"], ["jobs", "seq", "note"]) + r"""
  var KEYS = """ + spec["keys"] + r""", LABELS = """ + spec["labels"] + r""";
  var OBJ = '""" + spec["obj"] + r"""', RULE = '""" + spec["rule"] + r"""';
  var RIVALS = """ + spec["rivals"] + r""";
  var presetIn = document.getElementById('exPreset');
  var jobsIn = document.getElementById('exJobs'), seqIn = document.getElementById('exSeq');
  var posIn = document.getElementById('exPos'), plot = document.getElementById('exPlot');
  var swapT = document.getElementById('exSwap'), chainT = document.getElementById('exChain');
  var rulesT = document.getElementById('exRules'), status = document.getElementById('exStatus');
  var KPIS = ['exNow', 'exAfter', 'exDelta', 'exRule', 'exBest', 'exSteps'];

  function blank(why) {
    plot.innerHTML = ''; swapT.innerHTML = ''; chainT.innerHTML = ''; rulesT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> A job is a name, a space, then '
      + LABELS.join(' and then ') + '.';
  }

  function redraw() {
    var parsed = parseJobs(jobsIn.value, KEYS, LABELS);
    if (parsed.bad) { blank(parsed.bad); return; }
    var jobs = fillJobs(parsed.jobs), n = jobs.length;
    var ps = parseSeq(seqIn.value, jobs);
    if (ps.bad) { blank(ps.bad); return; }
    var seq = ps.seq, cross = crossCheck(seq, jobs);
    if (!cross.agree) {
      blank('the two ways of computing ' + cross.disagree.join(' and ') + ' disagree, so nothing is shown');
      return;
    }
    var get = SCHEDOBJ[OBJ].get, here = get(cross.forward), i;
    var pos = Math.max(1, Math.min(n - 1, Math.round(+posIn.value)));
    document.getElementById('exPosOut').textContent = pos + ' and ' + (pos + 1);
    var sw = adjacentSwap(seq, pos - 1, jobs);
    var after = get(sw.after), delta = Rsub(after, here);
    var improves = Rsign(delta) < 0;

    var ruleSeq = ruleOrder(jobs, RULE), audit = orderAudit(ruleSeq, jobs, RULE);
    var chain = exchangeChain(jobs, seq, OBJ);
    var span = cross.forward.makespan;
    plot.innerHTML = schedGantt([
      { name: 'as typed', bars: seqBars(seq, jobs, cross.forward, { sub: false }) },
      { name: 'swapped', bars: seqBars(sw.seq, jobs, sw.after, { tone: improves ? 'green' : 'red', sub: false }) },
      { name: RULE, bars: seqBars(ruleSeq, jobs, seqObjectives(ruleSeq, jobs), { tone: 'purple', sub: false }) }
    ], { width: 660, height: 250, span: span, ticks: schedTicks(span),
         caption: 'three orders on one axis; the work finishes at ' + Rtext(span) + ' in all of them' });

    var a = jobs[seq[pos - 1]], b = jobs[seq[pos]];
    var cells = [
      ['the pair you swapped', 'positions ' + pos + ' and ' + (pos + 1) + ': '
        + tone(a.id, 'cyan') + ' then ' + tone(b.id, 'cyan')],
      ['what the rule compares', """ + '"' + spec["compares"] + '"' + r""" + ': '
        + a.id + ' at ' + Rtext(sw.ratios.a) + ' against ' + b.id + ' at ' + Rtext(sw.ratios.b)],
      ['sum C moves by p_' + b.id + ' − p_' + a.id, Rtext(b.p) + ' − ' + Rtext(a.p) + ' = '
        + tone(Rtext(sw.deltaSumC), Rsign(sw.deltaSumC) < 0 ? 'green' : 'red')],
      ['sum wC moves by w_' + a.id + 'p_' + b.id + ' − w_' + b.id + 'p_' + a.id,
        Rtext(Rmul(a.w, b.p)) + ' − ' + Rtext(Rmul(b.w, a.p)) + ' = '
        + tone(Rtext(sw.deltaSumWC), Rsign(sw.deltaSumWC) < 0 ? 'green' : 'red')],
      ['both, against a full recomputation of the whole schedule',
        sw.checkC && sw.checkWC
          ? tone('the two agree, so nothing outside the pair moved', 'green')
          : tone('THEY DISAGREE — something outside the pair moved, and that cannot happen', 'red')]
    ];
    var srows = '';
    for (i = 0; i < cells.length; i += 1) srows += tr([rowhead(cells[i][0]), tdl(cells[i][1])]);
    swapT.innerHTML = '<caption>The swap, decomposed</caption><tbody>' + srows + '</tbody>';

    var crows = '';
    for (i = 0; i < chain.steps.length; i += 1) {
      var st = chain.steps[i];
      crows += tr([rowhead(String(i + 1)), td(st.a + ' ↔ ' + st.b),
                   td(Rtext(st.from)), td(Rtext(st.to)),
                   td(tone(Rtext(st.delta), 'green')),
                   td(st.checked ? tone('decomposes', 'green') : tone('does not', 'red')),
                   tdl(seqText(st.seq, jobs))]);
    }
    if (!chain.steps.length) {
      crows = tr([tdl('no adjacent swap improves ' + SCHEDOBJ[OBJ].label
        + ' — this order is already where the exchange argument stops', 'small-copy')
        .replace('<td', '<td colspan="7"')]);
    }
    chainT.innerHTML = '<caption>Every improving adjacent swap, taken in turn</caption><thead>'
      + tr([th('step'), th('the pair'), th('before'), th('after'), th('moved by'),
            th('one subtraction?'), th('the order it leaves')]) + '</thead><tbody>' + crows + '</tbody>';

    var rows = '', names = [RULE].concat(RIVALS), bestChk = null;
    for (i = 0; i < names.length; i += 1) {
      var nm = names[i], sq = ruleOrder(jobs, nm), ob = seqObjectives(sq, jobs);
      var chk = attainsOptimum(jobs, sq, OBJ);
      if (nm === RULE) bestChk = chk;
      var good = chk.checked && chk.attains;
      rows += tr([rowhead(nm), tdl(SCHEDRULES[nm].label), td(seqText(sq, jobs)),
                  td(Rtext(SCHEDOBJ[OBJ].get(ob))),
                  td(chk.checked ? Rtext(chk.excess) : 'not checked'),
                  td(good ? tone('optimal', 'green') : tone('beaten', 'red'))],
                 good ? 'tone-green' : 'tone-red');
    }
    rulesT.innerHTML = '<caption>' + SCHEDOBJ[OBJ].label + ', rule by rule, against every order</caption>'
      + '<thead>' + tr([th('rule'), th('what it says'), th('the order it gives'), th('scores'),
                        th('over the best'), th('verdict')]) + '</thead><tbody>' + rows + '</tbody>';

    document.getElementById('exNow').textContent = Rtext(here);
    document.getElementById('exAfter').textContent = Rtext(after);
    document.getElementById('exDelta').textContent = (Rsign(delta) > 0 ? '+' : '') + Rtext(delta)
      + (improves ? ' — better' : (Rzero(delta) ? ' — no change' : ' — worse'));
    document.getElementById('exRule').textContent = Rtext(SCHEDOBJ[OBJ].get(seqObjectives(ruleSeq, jobs)));
    document.getElementById('exBest').textContent = bestChk.checked
      ? Rtext(bestChk.optimum) + ' over ' + bestChk.count + ' orders' : 'not checked';
    document.getElementById('exSteps').textContent = chain.steps.length
      + (chain.stalled ? ' (still going)' : '');

    var reached = seqText(chain.seq, jobs) === seqText(ruleSeq, jobs);
    status.innerHTML = '<strong>Swapping ' + tone(a.id + ' and ' + b.id, 'cyan') + ' moves '
      + SCHEDOBJ[OBJ].label + ' by exactly ' + tone((Rsign(delta) > 0 ? '+' : '') + Rtext(delta),
        improves ? 'green' : 'red') + '.</strong> '
      + (improves ? 'It improves because ' : (Rzero(delta) ? 'It changes nothing because ' : 'It does not, because '))
      + a.id + ' has ' + """ + '"' + spec["compares"] + '"' + r""" + ' of ' + Rtext(sw.ratios.a)
      + ' and ' + b.id + ' has ' + Rtext(sw.ratios.b) + '. Taking every improving swap in turn stops after '
      + tone(chain.steps.length + ' of them', 'cyan') + ' at ' + tone(seqText(chain.seq, jobs), 'purple')
      + ' — ' + (reached
          ? 'which is ' + RULE + "'s own order, arrived at without ever being told what the rule is. "
          : 'which is NOT ' + RULE + "'s order (" + seqText(ruleSeq, jobs) + '), and that is worth '
            + 'looking at rather than explaining away. ')
      + (audit.permutation && audit.ordered
          ? 'The rule&rsquo;s order was audited as an order: every job appears exactly once, and each key '
            + 'is no larger than the next. '
          : tone('The rule&rsquo;s own order failed its audit: ' + audit.why + '. ', 'red'))
      + (bestChk.checked
          ? (bestChk.attains
              ? 'Against all ' + bestChk.count + ' orders it is optimal, and '
                + (bestChk.ties > 1 ? bestChk.ties + ' orders tie with it.' : 'it is the only one.')
              : tone('Against all ' + bestChk.count + ' orders it is NOT optimal, by '
                     + Rtext(bestChk.excess) + '.', 'red'))
          : 'There are too many orders to enumerate here, so this page does not claim optimality.');
  }

  function apply() {
    var p = EXP[presetIn.value];
    if (!p) return;
    jobsIn.value = p.jobs; seqIn.value = p.seq;
    redraw();
  }
  presetIn.addEventListener('change', apply);
  jobsIn.addEventListener('input', redraw);
  seqIn.addEventListener('input', redraw);
  posIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title=spec["title"],
        subtitle=spec["subtitle"],
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Swap two neighbours and watch one subtraction do the work"),
        panel_intro=cfg.get(
            "panel_intro",
            "The swap is decomposed into the single quantity it moves, then checked against a full "
            "recomputation of both schedules; the walk down to the rule's own order is taken one "
            "improving swap at a time. On this example: " + chosen["note"] + ".",
        ),
        script=script,
    )


def _spt(cfg):
    return _exchange(cfg, "spt")


def _wspt(cfg):
    return _exchange(cfg, "wspt")


# ---------------------------------------------------------------------------
# L4 -- edd: the rule that wins on L max and loses on total tardiness
# ---------------------------------------------------------------------------

_EDD_PRESETS = [
    {
        "id": "loses",
        "label": "EDD is optimal for L max and beaten on sum T",
        "jobs": "A 6:8, B 4:4, C 5:12, D 3:6, E 7:20",
        "seq": "B D A C E",
        "note": "the same five jobs, and the two due-date objectives disagree about them",
    },
    {
        "id": "onelate",
        "label": "one job is hopeless and drags L max with it",
        "jobs": "A 3:4, B 2:3, C 8:9, D 4:30",
        "seq": "B A C D",
        "note": "D is never late; C decides L max wherever it goes",
    },
    {
        "id": "slack",
        "label": "least slack disagrees with earliest due date",
        "jobs": "A 2:6, B 7:10, C 3:7, D 5:12",
        "seq": "A C B D",
        "note": "d − p and d order these four differently",
    },
]


def _edd(cfg):
    chosen = _choose(cfg, "edd", _EDD_PRESETS, "loses")

    markup = (
        _toolbar(
            "Earliest due date, and the objective it does not touch",
            "EDD minimises the worst lateness; it has nothing to say about the total",
            [("cyan", "a job that finishes on time"), ("red", "a job that finishes late"),
             ("amber", "its due date"), ("green", "an objective this rule is optimal for")],
        )
        + _stage(_svg("edPlot", "0 0 660 210",
                      "The chosen rule's order as a strip of time, with every due date marked.")
                 + _svg("edSwap", "0 0 660 96",
                        "The same order with one adjacent pair swapped, shown beneath it."))
        + _table("edRules")
        + _table("edJobs")
        + _banner("edStatus")
    )
    controls = (
        _select("edPreset", "Worked example", _options(_EDD_PRESETS), chosen["id"])
        + _text("edJobsIn", "Jobs, as name time:due", chosen["jobs"])
        + _select("edRule", "Order by",
                  [("EDD", "earliest due date first"), ("SLACK", "least slack d − p first"),
                   ("SPT", "shortest processing time first"), ("FCFS", "the order typed")], "EDD")
        + _range("edPos", "Swap the job in this position with the next", 1, 7, 1)
        + _kpis([
            ("Maximum lateness, L max", "edLmax"),
            ("The best L max there is", "edBestL"),
            ("Total tardiness, sum T", "edSumT"),
            ("The best sum T there is", "edBestT"),
            ("Jobs finishing late", "edLate"),
            ("Objectives this rule is best at", "edWins"),
        ])
        + _hint(
            "edHint",
            "The exchange argument for L max is the one on the previous page with a different "
            "quantity: swapping an out-of-order adjacent pair cannot make the worst lateness worse, "
            "because the later job finishes earlier and the earlier job finishes no later than the "
            "pair did before. The lab swaps a pair you choose and prints both maxima.",
        )
    )

    script = _MODE_JS["edd"] + r"""
""" + _presets_js("EDP", _EDD_PRESETS, ["jobs", "seq", "note"]) + r"""
  var RULES = ['EDD', 'SLACK', 'SPT', 'FCFS'], SHOW = ['Lmax', 'Tmax', 'sumT', 'sumU'];
  var presetIn = document.getElementById('edPreset'), jobsIn = document.getElementById('edJobsIn');
  var ruleIn = document.getElementById('edRule'), posIn = document.getElementById('edPos');
  var plot = document.getElementById('edPlot'), swapSvg = document.getElementById('edSwap');
  var rulesT = document.getElementById('edRules'), jobsT = document.getElementById('edJobs');
  var status = document.getElementById('edStatus');
  var KPIS = ['edLmax', 'edBestL', 'edSumT', 'edBestT', 'edLate', 'edWins'];

  function blank(why) {
    plot.innerHTML = ''; swapSvg.innerHTML = ''; rulesT.innerHTML = ''; jobsT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> A job is a name, a space, then its '
      + 'processing time and its due date separated by a colon.';
  }

  function redraw() {
    var parsed = parseJobs(jobsIn.value, ['p', 'd'], ['the processing time', 'the due date']);
    if (parsed.bad) { blank(parsed.bad); return; }
    var jobs = fillJobs(parsed.jobs), n = jobs.length, i, k;
    var seq = ruleOrder(jobs, ruleIn.value), cross = crossCheck(seq, jobs);
    if (!cross.agree) {
      blank('the two ways of computing ' + cross.disagree.join(' and ') + ' disagree, so nothing is shown');
      return;
    }
    var o = cross.forward;
    var audit = orderAudit(seq, jobs, ruleIn.value);
    var pos = Math.max(1, Math.min(n - 1, Math.round(+posIn.value)));
    document.getElementById('edPosOut').textContent = pos + ' and ' + (pos + 1);
    var sw = adjacentSwap(seq, pos - 1, jobs);

    plot.innerHTML = schedGantt([{ name: ruleIn.value, bars: seqBars(seq, jobs, o) }], {
      width: 660, height: 210, marks: dueMarks(jobs, seq), ticks: schedTicks(o.makespan),
      caption: 'L max is the largest of the lateness column, and it is set by one job'
    });
    swapSvg.innerHTML = schedGantt([{ name: 'swapped',
        bars: seqBars(sw.seq, jobs, sw.after, { sub: false }) }], {
      width: 660, height: 96, span: o.makespan, marks: dueMarks(jobs, sw.seq),
      caption: 'swapping ' + jobs[seq[pos - 1]].id + ' and ' + jobs[seq[pos]].id + ' moves L max from '
               + Rtext(o.Lmax) + ' to ' + Rtext(sw.after.Lmax)
    });

    var rows = '', wins = 0, bestOf = {};
    for (k = 0; k < SHOW.length; k += 1) bestOf[SHOW[k]] = attainsOptimum(jobs, seq, SHOW[k]);
    for (i = 0; i < RULES.length; i += 1) {
      var sq = ruleOrder(jobs, RULES[i]), ob = seqObjectives(sq, jobs), cells = [];
      cells.push(rowhead(RULES[i]));
      cells.push(td(seqText(sq, jobs)));
      for (k = 0; k < SHOW.length; k += 1) {
        var v = SCHEDOBJ[SHOW[k]].get(ob), chk = bestOf[SHOW[k]];
        var best = chk.checked && Requ(v, chk.optimum);
        cells.push(td(best ? tone(Rtext(v), 'green') : Rtext(v)));
      }
      rows += tr(cells, RULES[i] === ruleIn.value ? 'tone-cyan' : null);
    }
    var last = [rowhead('the best of every order'), td('—')];
    for (k = 0; k < SHOW.length; k += 1) {
      last.push(td(bestOf[SHOW[k]].checked ? tone(Rtext(bestOf[SHOW[k]].optimum), 'purple') : 'not checked'));
      if (bestOf[SHOW[k]].checked && bestOf[SHOW[k]].attains) wins += 1;
    }
    rows += tr(last, 'tone-purple');
    rulesT.innerHTML = '<caption>Four rules and four due-date objectives, on the same jobs</caption>'
      + '<thead>' + tr([th('rule'), th('order'), th('L max'), th('T max'), th('sum T'),
                        th('late jobs')]) + '</thead><tbody>' + rows + '</tbody>';

    var jrows = '';
    for (i = 0; i < o.rows.length; i += 1) {
      var r = o.rows[i], sets = Requ(r.L, o.Lmax);
      jrows += tr([rowhead((i + 1) + '. ' + r.id), td(Rtext(r.p)), td(Rtext(r.d)), td(Rtext(r.C)),
                   td(sets ? tone(Rtext(r.L), 'red') : Rtext(r.L)), td(Rtext(r.T)),
                   td(sets ? tone('this job sets L max', 'red') : (r.U ? 'late' : 'on time'))],
                  sets ? 'tone-red' : null);
    }
    jobsT.innerHTML = '<caption>The chosen order, job by job</caption><thead>'
      + tr([th('position'), th('p'), th('due'), th('finishes'), th('lateness'), th('tardiness'),
            th('note')]) + '</thead><tbody>' + jrows + '</tbody>';

    document.getElementById('edLmax').textContent = Rtext(o.Lmax);
    document.getElementById('edBestL').textContent = bestOf.Lmax.checked ? Rtext(bestOf.Lmax.optimum) : '—';
    document.getElementById('edSumT').textContent = Rtext(o.sumT);
    document.getElementById('edBestT').textContent = bestOf.sumT.checked ? Rtext(bestOf.sumT.optimum) : '—';
    document.getElementById('edLate').textContent = o.sumU + ' of ' + n;
    document.getElementById('edWins').textContent = wins + ' of ' + SHOW.length;

    var lossT = bestOf.sumT.checked ? Rsub(o.sumT, bestOf.sumT.optimum) : null;
    status.innerHTML = '<strong>' + ruleIn.value + ' gives ' + tone(seqText(seq, jobs), 'cyan')
      + '.</strong> '
      + (audit.permutation && audit.ordered
          ? 'Audited as an order: every job once, each key no larger than the next. '
          : tone('That order failed its audit: ' + audit.why + '. ', 'red'))
      + 'Swapping positions ' + pos + ' and ' + (pos + 1) + ' takes L max from ' + Rtext(o.Lmax)
      + ' to ' + Rtext(sw.after.Lmax) + ' — '
      + (Rcmp(sw.after.Lmax, o.Lmax) < 0 ? tone('an improvement, so this order was not EDD', 'green')
          : (Requ(sw.after.Lmax, o.Lmax) ? 'no change at all'
             : tone('worse, which is what the exchange argument predicts for a pair already in due-date order', 'amber')))
      + '. '
      + (bestOf.Lmax.checked && bestOf.Lmax.attains
          ? 'On L max this order is optimal, checked against all ' + bestOf.Lmax.count + ' orders. '
          : (bestOf.Lmax.checked ? tone('On L max it is beaten by ' + Rtext(Rsub(o.Lmax, bestOf.Lmax.optimum))
              + '. ', 'red') : ''))
      + (lossT === null ? ''
          : (Rzero(lossT)
              ? 'And on total tardiness it happens to be optimal here too — which is luck, not a theorem.'
              : tone('And on total tardiness it is beaten by ' + Rtext(lossT), 'red')
                + ': the best order for sum T is ' + tone(seqText(bestOf.sumT.best, jobs), 'purple')
                + ', found by enumeration and by no rule on this page. 1||sum T has no exchange '
                + 'argument, and this course says so rather than offering one that looks like it does.'));
  }

  function apply() {
    var p = EDP[presetIn.value];
    if (!p) return;
    jobsIn.value = p.jobs;
    redraw();
  }
  presetIn.addEventListener('change', apply);
  ruleIn.addEventListener('change', redraw);
  jobsIn.addEventListener('input', redraw);
  posIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Earliest due date, and the objective it does not touch",
        subtitle="EDD minimises the worst lateness; total tardiness is a different problem with no rule",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Four rules, four due-date objectives, one set of jobs"),
        panel_intro=cfg.get(
            "panel_intro",
            "Each rule's order is audited as an order, scored on all four objectives, and compared "
            "with the best of every possible order. On this example: " + chosen["note"] + ".",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L5 -- late: Moore-Hodgson, and the job it throws out
# ---------------------------------------------------------------------------

_LATE_PRESETS = [
    {
        "id": "throws",
        "label": "the job thrown out is not the job that was late",
        "jobs": "A 6:8, B 4:4, C 5:12, D 3:6, E 7:20",
        "note": "at the third step the algorithm discards a job that had been on time for two rounds",
    },
    {
        "id": "onebad",
        "label": "one enormous job and four small ones",
        "jobs": "A 12:14, B 2:5, C 3:7, D 2:9, E 4:13",
        "note": "A fits only if nothing else does, which is exactly the trade the rule makes",
    },
    {
        "id": "allfit",
        "label": "everything fits, and nothing is discarded",
        "jobs": "A 2:3, B 3:7, C 1:9, D 4:14",
        "note": "a run with no discard at all, so the steps table shows the accepting half",
    },
]


def _late(cfg):
    chosen = _choose(cfg, "late", _LATE_PRESETS, "throws")

    markup = (
        _toolbar(
            "Moore-Hodgson: fewest jobs late",
            "when the schedule goes late, throw out the LONGEST job accepted so far",
            [("green", "kept, and on time"), ("red", "discarded, and run at the end"),
             ("amber", "its due date"), ("purple", "the job thrown out at this step")],
        )
        + _stage(_svg("mhPlot", "0 0 660 210",
                      "The kept jobs in due-date order followed by the discarded ones, with due dates marked.")
                 + _svg("mhStrip", "0 0 660 52",
                        "A strip showing the accepted set at the chosen step."))
        + _table("mhSteps")
        + _table("mhCompare")
        + _banner("mhStatus")
    )
    controls = (
        _select("mhPreset", "Worked example", _options(_LATE_PRESETS), chosen["id"])
        + _text("mhJobs", "Jobs, as name time:due", chosen["jobs"])
        + _range("mhStep", "Stop after this many jobs have been offered", 1, 8, 8)
        + _kpis([
            ("Jobs finishing late", "mhLate"),
            ("The fewest there can be", "mhBest"),
            ("Jobs kept on time", "mhKept"),
            ("Jobs discarded", "mhDrop"),
            ("What EDD alone leaves late", "mhEdd"),
            ("Is this the minimum?", "mhVerdict"),
        ])
        + _hint(
            "mhHint",
            "The jobs are offered in due-date order. Each one joins, and the moment the accepted set "
            "runs past a due date the <em>longest</em> job accepted so far is thrown out &mdash; not "
            "the one that was late. Throwing out the late job is the obvious move and it is wrong: "
            "the longest job frees the most time for the same single unit of lateness.",
        )
    )

    script = _MODE_JS["late"] + r"""
""" + _presets_js("MHP", _LATE_PRESETS, ["jobs", "note"]) + r"""
  var presetIn = document.getElementById('mhPreset'), jobsIn = document.getElementById('mhJobs');
  var stepIn = document.getElementById('mhStep');
  var plot = document.getElementById('mhPlot'), strip = document.getElementById('mhStrip');
  var stepsT = document.getElementById('mhSteps'), cmpT = document.getElementById('mhCompare');
  var status = document.getElementById('mhStatus');
  var KPIS = ['mhLate', 'mhBest', 'mhKept', 'mhDrop', 'mhEdd', 'mhVerdict'];

  function blank(why) {
    plot.innerHTML = ''; strip.innerHTML = ''; stepsT.innerHTML = ''; cmpT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> A job is a name, a space, then its '
      + 'processing time and its due date separated by a colon.';
  }

  function redraw() {
    var parsed = parseJobs(jobsIn.value, ['p', 'd'], ['the processing time', 'the due date']);
    if (parsed.bad) { blank(parsed.bad); return; }
    var jobs = fillJobs(parsed.jobs), n = jobs.length, i;
    var mh = mooreHodgson(jobs), cross = crossCheck(mh.seq, jobs);
    if (!cross.agree) {
      blank('the two ways of computing ' + cross.disagree.join(' and ') + ' disagree, so nothing is shown');
      return;
    }
    var o = cross.forward;
    var step = Math.max(1, Math.min(n, Math.round(+stepIn.value)));
    document.getElementById('mhStepOut').textContent = step + ' of ' + n;
    var at = mh.steps[step - 1];
    var dropped = {};
    for (i = 0; i < mh.discarded.length; i += 1) dropped[mh.discarded[i]] = true;

    var bars = seqBars(mh.seq, jobs, o);
    for (i = 0; i < bars.length; i += 1) {
      bars[i].tone = dropped[mh.seq[i]] ? 'red' : 'green';
      if (at && at.removed === mh.seq[i]) bars[i].tone = 'purple';
    }
    plot.innerHTML = schedGantt([{ name: 'machine', bars: bars }], {
      width: 660, height: 210, marks: dueMarks(jobs, mh.seq), ticks: schedTicks(o.makespan),
      caption: 'the kept jobs first, in due-date order, then everything that was thrown out'
    });

    var cells = '', wide = 660 / Math.max(1, n);
    for (i = 0; i < n; i += 1) {
      var inKept = at && at.kept.indexOf(i) >= 0, inDrop = at && at.discarded.indexOf(i) >= 0;
      var x = wide * (i + 0.5);
      cells += '<text x="' + Math.round(x) + '" y="20" text-anchor="middle" font-size="11" '
        + 'font-weight="700" fill="var(--' + (inKept ? 'green' : (inDrop ? 'red' : 'muted')) + ')">'
        + jobs[i].id + '</text>'
        + '<text x="' + Math.round(x) + '" y="36" text-anchor="middle" font-size="9" '
        + 'fill="var(--muted)">' + (inKept ? 'kept' : (inDrop ? 'out' : 'not yet offered')) + '</text>';
    }
    strip.innerHTML = cells;

    var rows = '';
    for (i = 0; i < mh.steps.length; i += 1) {
      var s = mh.steps[i];
      rows += tr([rowhead(String(i + 1)), td(s.id), td(Rtext(jobs[s.job].p)), td(Rtext(jobs[s.job].d)),
                  td(Rtext(s.time)),
                  td(s.removed === null ? tone('nothing', 'green') : tone(s.removedId, 'red')),
                  tdl(s.why)], i === step - 1 ? 'tone-cyan' : null);
    }
    stepsT.innerHTML = '<caption>Moore-Hodgson, one offered job at a time</caption><thead>'
      + tr([th('step'), th('offered'), th('p'), th('due'), th('finish'), th('thrown out'), th('why')])
      + '</thead><tbody>' + rows + '</tbody>';

    var edd = ruleOrder(jobs, 'EDD'), eddO = seqObjectives(edd, jobs);
    var chk = attainsOptimum(jobs, mh.seq, 'sumU');
    var crows = '';
    var lines = [['Moore-Hodgson', seqText(mh.seq, jobs), mh.sumU],
                 ['EDD alone', seqText(edd, jobs), eddO.sumU],
                 ['shortest first', seqText(ruleOrder(jobs, 'SPT'), jobs),
                  seqObjectives(ruleOrder(jobs, 'SPT'), jobs).sumU]];
    for (i = 0; i < lines.length; i += 1) {
      var best = chk.checked && lines[i][2] === Number(chk.optimum.n);
      crows += tr([rowhead(lines[i][0]), td(lines[i][1]), td(String(lines[i][2])),
                   td(best ? tone('fewest possible', 'green') : tone('more than necessary', 'red'))],
                  best ? 'tone-green' : 'tone-red');
    }
    if (chk.checked) {
      crows += tr([rowhead('the best of every order'), td(seqText(chk.best, jobs)),
                   td(Rtext(chk.optimum)), td(tone('found by enumeration', 'purple'))], 'tone-purple');
    }
    cmpT.innerHTML = '<caption>How many finish late, rule by rule</caption><thead>'
      + tr([th('rule'), th('order'), th('late'), th('verdict')]) + '</thead><tbody>' + crows + '</tbody>';

    document.getElementById('mhLate').textContent = String(mh.sumU);
    document.getElementById('mhBest').textContent = chk.checked ? Rtext(chk.optimum) : 'not checked';
    document.getElementById('mhKept').textContent = mh.kept.length + ': '
      + (mh.kept.length ? mh.kept.map(function (k) { return jobs[k].id; }).join(', ') : 'none');
    document.getElementById('mhDrop').textContent = mh.discarded.length
      ? mh.discarded.map(function (k) { return jobs[k].id; }).join(', ') : 'none';
    document.getElementById('mhEdd').textContent = String(eddO.sumU);
    document.getElementById('mhVerdict').textContent = chk.checked
      ? (chk.attains ? 'yes — checked against every order' : 'NO') : 'not checked';

    var surprise = null;
    for (i = 0; i < mh.steps.length; i += 1) {
      if (mh.steps[i].removed !== null && mh.steps[i].removed !== mh.steps[i].job) {
        surprise = mh.steps[i]; break;
      }
    }
    status.innerHTML = '<strong>' + mh.sumU + ' of the ' + n + ' jobs finish late</strong>'
      + (chk.checked
          ? (chk.attains ? ', and ' + tone('no order does better', 'green') + ' — checked against all '
              + chk.count + ' of them. '
            : tone(', and that is NOT the minimum: ' + Rtext(chk.optimum) + ' is. ', 'red'))
          : '. ')
      + (surprise
          ? 'Step ' + (mh.steps.indexOf(surprise) + 1) + ' is the one to look at: '
            + tone(surprise.id, 'cyan') + ' arrived and went late, and the algorithm threw out '
            + tone(surprise.removedId, 'purple') + ' instead — the longest job accepted so far, which '
            + 'had been comfortably on time. One late job either way; ' + Rtext(jobs[surprise.removed].p)
            + ' hours of room freed rather than ' + Rtext(jobs[surprise.job].p) + '. '
          : 'No step here throws out a job other than the one that went late, so this instance does not '
            + 'show the rule at its least obvious — try another. ')
      + 'EDD alone leaves ' + eddO.sumU + ' late; ordering by due date is how the jobs are OFFERED, and '
      + 'it is not the algorithm.';
  }

  function apply() {
    var p = MHP[presetIn.value];
    if (!p) return;
    jobsIn.value = p.jobs;
    redraw();
  }
  presetIn.addEventListener('change', apply);
  jobsIn.addEventListener('input', redraw);
  stepIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Moore-Hodgson: fewest jobs late",
        subtitle="The job thrown out is the longest one accepted so far, not the one that was late",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Offer the jobs in due-date order and watch what gets dropped"),
        panel_intro=cfg.get(
            "panel_intro",
            "Each step shows the accepted set, the clock it reaches, and what was discarded and why; "
            "the count is then checked against the best of every order. On this example: "
            + chosen["note"] + ".",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L6 -- flowshop: two machines in series, and the idle time Johnson attacks
# ---------------------------------------------------------------------------

_FS_PRESETS = [
    {
        "id": "johnson",
        "label": "five jobs through two machines",
        "jobs": "A 5:2, B 1:6, C 9:7, D 3:8, E 10:4",
        "seq": "A B C D E",
        "note": "two of the five are quicker on the first machine and go to the front",
    },
    {
        "id": "starved",
        "label": "the second machine waits at the start",
        "jobs": "A 8:1, B 7:2, C 6:9, D 2:5",
        "seq": "A B C D",
        "note": "put a long first-machine job first and machine 2 stands idle for all of it",
    },
    {
        "id": "balanced",
        "label": "every job the same length on both",
        "jobs": "A 4:4, B 3:3, C 6:6, D 2:2",
        "seq": "C A B D",
        "note": "no job is quicker on either machine, so the rule's first test is a tie throughout",
    },
]


def _flowshop(cfg):
    chosen = _choose(cfg, "flowshop", _FS_PRESETS, "johnson")

    markup = (
        _toolbar(
            "Two machines in series: Johnson's rule",
            "the makespan is the second machine's finishing time, and idle time on it is the whole cost",
            [("cyan", "machine 1"), ("purple", "machine 2"),
             ("green", "Johnson's order"), ("red", "the order you typed")],
        )
        + _stage(_svg("fsPlot", "0 0 660 156",
                      "The order you typed, drawn as two machines in series.")
                 + _svg("fsBest", "0 0 660 156",
                        "Johnson's order, drawn on the same time axis."))
        + _table("fsSplit")
        + _table("fsCompare")
        + _banner("fsStatus")
    )
    controls = (
        _select("fsPreset", "Worked example", _options(_FS_PRESETS), chosen["id"])
        + _text("fsJobs", "Jobs, as name time-on-1:time-on-2", chosen["jobs"])
        + _text("fsSeq", "An order of your own to compare", chosen["seq"])
        + _kpis([
            ("Johnson's makespan", "fsJohn"),
            ("Your order's makespan", "fsMine"),
            ("The best of every order", "fsBestV"),
            ("Idle time on machine 2, Johnson", "fsIdleJ"),
            ("Idle time on machine 2, yours", "fsIdleM"),
            ("Does the rule attain the best?", "fsVerdict"),
        ])
        + _hint(
            "fsHint",
            "Machine 1 never stops: it is the machine 2 timeline that has gaps, and the makespan is "
            "the sum of every second-machine time plus the idle in between. So minimising the "
            "makespan and minimising idle time on machine 2 are the same problem, which is what the "
            "rule is doing when it puts the quick-on-1 jobs first.",
        )
    )

    script = _MODE_JS["flowshop"] + r"""
""" + _presets_js("FSP", _FS_PRESETS, ["jobs", "seq", "note"]) + r"""
  var presetIn = document.getElementById('fsPreset'), jobsIn = document.getElementById('fsJobs');
  var seqIn = document.getElementById('fsSeq');
  var plot = document.getElementById('fsPlot'), bestSvg = document.getElementById('fsBest');
  var splitT = document.getElementById('fsSplit'), cmpT = document.getElementById('fsCompare');
  var status = document.getElementById('fsStatus');
  var KPIS = ['fsJohn', 'fsMine', 'fsBestV', 'fsIdleJ', 'fsIdleM', 'fsVerdict'];

  function blank(why) {
    plot.innerHTML = ''; bestSvg.innerHTML = ''; splitT.innerHTML = ''; cmpT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> A job is a name, a space, then its '
      + 'time on machine 1 and its time on machine 2 separated by a colon.';
  }

  function redraw() {
    var parsed = parseJobs(jobsIn.value, ['p1', 'p2'],
                           ['the time on machine 1', 'the time on machine 2']);
    if (parsed.bad) { blank(parsed.bad); return; }
    var jobs = parsed.jobs, i;
    var ps = parseSeq(seqIn.value, jobs);
    if (ps.bad) { blank(ps.bad); return; }
    var mine = ps.seq;
    var jr = johnsonRule(jobs), john = jr.seq;
    var jb = flowshopBars(john, jobs), mb = flowshopBars(mine, jobs);
    var jv = flowshopVerify(jb, jobs, john), mv = flowshopVerify(mb, jobs, mine);
    if (!jv.ok || !mv.ok) {
      blank('the schedule drawn does not hold together: ' + jv.faults.concat(mv.faults).join('; '));
      return;
    }
    if (!Requ(jv.makespan, jr.makespan.value) || !Requ(mv.makespan, flowshopMakespan(mine, jobs).value)) {
      blank('the makespan read off the picture disagrees with the recursion that drew it');
      return;
    }
    var best = bestFlowshop(jobs);
    var span = Rcmp(mv.makespan, jv.makespan) > 0 ? mv.makespan : jv.makespan;

    plot.innerHTML = schedGantt([{ name: 'M1', bars: mb.one }, { name: 'M2', bars: mb.two }], {
      width: 660, height: 156, span: span, ticks: schedTicks(span),
      caption: 'your order — machine 2 finishes at ' + Rtext(mv.makespan)
               + ' after ' + Rtext(mv.idle) + ' idle'
    });
    bestSvg.innerHTML = schedGantt([{ name: 'M1', bars: jb.one }, { name: 'M2', bars: jb.two }], {
      width: 660, height: 156, span: span, ticks: schedTicks(span),
      caption: "Johnson's order — machine 2 finishes at " + Rtext(jv.makespan)
               + ' after ' + Rtext(jv.idle) + ' idle'
    });

    var rows = '';
    for (i = 0; i < jobs.length; i += 1) {
      var j = jobs[i], quick = Rcmp(j.p1, j.p2) < 0;
      var where = jr.front.indexOf(i) >= 0 ? 'front' : 'back';
      rows += tr([rowhead(j.id), td(Rtext(j.p1)), td(Rtext(j.p2)),
                  td(quick ? tone('quicker on 1', 'cyan') : tone('not quicker on 1', 'purple')),
                  td(where === 'front' ? 'to the front, by increasing p1' : 'to the back, by decreasing p2'),
                  td(String(john.indexOf(i) + 1))],
                 quick ? 'tone-cyan' : 'tone-purple');
    }
    splitT.innerHTML = '<caption>The rule sorts each job into one of two lists</caption><thead>'
      + tr([th('job'), th('p1'), th('p2'), th('test'), th('which list'), th('final position')])
      + '</thead><tbody>' + rows + '</tbody>';

    var lines = [["Johnson's rule", john, jv], ['your order', mine, mv],
                 ['shortest p1 first', ruleOrder(jobs.map(function (j) { return { id: j.id, p: j.p1 }; }), 'SPT'), null],
                 ['longest p2 last', ruleOrder(jobs.map(function (j) { return { id: j.id, p: j.p2 }; }), 'LPT'), null]];
    var crows = '';
    for (i = 0; i < lines.length; i += 1) {
      var sq = lines[i][1], vf = lines[i][2] || flowshopVerify(flowshopBars(sq, jobs), jobs, sq);
      var good = !best.truncated && Requ(vf.makespan, best.value);
      crows += tr([rowhead(lines[i][0]), td(seqText(sq, jobs)), td(Rtext(vf.makespan)),
                   td(Rtext(vf.idle)),
                   td(good ? tone('best there is', 'green') : tone('beaten', 'red'))],
                  good ? 'tone-green' : 'tone-red');
    }
    if (!best.truncated) {
      crows += tr([rowhead('the best of every order'), td(seqText(best.seq, jobs)),
                   td(Rtext(best.value)), td('—'),
                   td(tone(best.count + ' orders checked, ' + best.ties + ' tied', 'purple'))], 'tone-purple');
    }
    cmpT.innerHTML = '<caption>Four orders, and the enumeration behind them</caption><thead>'
      + tr([th('order'), th('sequence'), th('makespan'), th('idle on M2'), th('verdict')])
      + '</thead><tbody>' + crows + '</tbody>';

    document.getElementById('fsJohn').textContent = Rtext(jv.makespan);
    document.getElementById('fsMine').textContent = Rtext(mv.makespan);
    document.getElementById('fsBestV').textContent = best.truncated ? 'not checked' : Rtext(best.value);
    document.getElementById('fsIdleJ').textContent = Rtext(jv.idle);
    document.getElementById('fsIdleM').textContent = Rtext(mv.idle);
    document.getElementById('fsVerdict').textContent = best.truncated ? 'not checked'
      : (Requ(jv.makespan, best.value) ? 'yes — checked against every order' : 'NO');

    status.innerHTML = '<strong>' + tone(seqText(john, jobs), 'green') + ' finishes at '
      + tone(Rtext(jv.makespan), 'green') + '</strong> against ' + tone(Rtext(mv.makespan), 'red')
      + ' for ' + seqText(mine, jobs) + '. ' + jr.why + '. Machine 2 does '
      + Rtext(jv.work) + ' hours of work whatever the order, so the only thing an order can change is '
      + 'the idle time in front of it: ' + tone(Rtext(jv.idle), 'green') + ' under the rule against '
      + tone(Rtext(mv.idle), 'red') + ' under yours, and the two makespans differ by exactly that. '
      + (best.truncated ? best.why + '. '
          : (Requ(jv.makespan, best.value)
              ? 'Checked against all ' + best.count + ' orders, the rule attains the minimum'
                + (best.ties > 1 ? ' — as do ' + (best.ties - 1) + ' others.' : ', uniquely.')
              : tone('Checked against all ' + best.count + ' orders, the rule does NOT attain the '
                     + 'minimum of ' + Rtext(best.value) + '.', 'red')))
      + ' Both pictures were read back before anything was printed: machine 1 without gaps, machine 2 '
      + 'never running two jobs at once, and no job on machine 2 before it left machine 1.';
  }

  function apply() {
    var p = FSP[presetIn.value];
    if (!p) return;
    jobsIn.value = p.jobs; seqIn.value = p.seq;
    redraw();
  }
  presetIn.addEventListener('change', apply);
  jobsIn.addEventListener('input', redraw);
  seqIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Two machines in series: Johnson's rule",
        subtitle="Machine 2's idle time is the whole of the difference between one order and another",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Send the jobs through two machines and watch the second one wait"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both schedules are drawn and then read back — machine 1 without gaps, machine 2 never "
            "overlapping itself — and the makespan is taken from the picture before it is compared "
            "with the best of every order. On this example: " + chosen["note"] + ".",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L7 -- parallel: LPT, the optimum, and BOTH lower bounds
# ---------------------------------------------------------------------------

_PAR_PRESETS = [
    {
        "id": "ratio",
        "label": "the instance LPT gets wrong",
        "jobs": "A 7, B 6, C 5, D 4, E 4, F 4, G 4",
        "machines": "3",
        "note": "LPT finishes at 13 where three machines can finish at 12",
    },
    {
        "id": "onebig",
        "label": "one job longer than the average load",
        "jobs": "A 11, B 3, C 3, D 2, E 2",
        "machines": "3",
        "note": "no schedule beats 11, and the average-load bound cannot see why",
    },
    {
        "id": "even",
        "label": "work that divides exactly",
        "jobs": "A 4, B 4, C 4, D 4, E 4, F 4",
        "machines": "3",
        "note": "the two bounds meet, so the optimum is known before any schedule is built",
    },
]


def _parallel(cfg):
    chosen = _choose(cfg, "parallel", _PAR_PRESETS, "ratio")

    markup = (
        _toolbar(
            "Identical machines in parallel",
            "a heuristic is worth what its bound is worth, and there are two bounds here",
            [("cyan", "the heuristic's schedule"), ("purple", "the exhaustive optimum"),
             ("amber", "the lower bounds"), ("red", "the machine that finishes last")],
        )
        + _stage(_svg("plPlot", "0 0 660 190",
                      "The heuristic's assignment, one track per machine.")
                 + _svg("plBest", "0 0 660 190",
                        "The best assignment there is, found by trying every one."))
        + _table("plSteps")
        + _table("plBounds")
        + _banner("plStatus")
    )
    controls = (
        _select("plPreset", "Worked example", _options(_PAR_PRESETS), chosen["id"])
        + _text("plJobs", "Jobs, as name time", chosen["jobs"])
        + _range("plM", "Machines", 2, 4, int(chosen["machines"]))
        + _select("plRule", "The rule to place them by",
                  [("LPT", "longest processing time first"), ("SPT", "shortest processing time first")],
                  "LPT")
        + _kpis([
            ("The heuristic's makespan", "plMake"),
            ("The best there is", "plOpt"),
            ("The ratio between them", "plRatio"),
            ("Total work over m", "plAvg"),
            ("The longest single job", "plMax"),
            ("The better lower bound", "plBound"),
        ])
        + _hint(
            "plHint",
            "Two things bound every schedule from below and neither implies the other: the total work "
            "divided by the number of machines, because some machine must do at least its share, and "
            "the longest single job, because that job runs on one machine without a break. The 4/3 "
            "guarantee for LPT is proved against them, so the lab prints both.",
        )
    )

    script = _MODE_JS["parallel"] + r"""
""" + _presets_js("PLP", _PAR_PRESETS, ["jobs", "machines", "note"]) + r"""
  var presetIn = document.getElementById('plPreset'), jobsIn = document.getElementById('plJobs');
  var mIn = document.getElementById('plM'), ruleIn = document.getElementById('plRule');
  var plot = document.getElementById('plPlot'), bestSvg = document.getElementById('plBest');
  var stepsT = document.getElementById('plSteps'), boundT = document.getElementById('plBounds');
  var status = document.getElementById('plStatus');
  var KPIS = ['plMake', 'plOpt', 'plRatio', 'plAvg', 'plMax', 'plBound'];

  function blank(why) {
    plot.innerHTML = ''; bestSvg.innerHTML = ''; stepsT.innerHTML = ''; boundT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> A job is a name, a space, then how '
      + 'long it takes.';
  }

  function redraw() {
    var parsed = parseJobs(jobsIn.value, ['p'], ['the processing time']);
    if (parsed.bad) { blank(parsed.bad); return; }
    var jobs = fillJobs(parsed.jobs), m = Math.max(2, Math.min(4, Math.round(+mIn.value))), i;
    document.getElementById('plMOut').textContent = String(m);
    var par = parallelAssign(jobs, m, ruleIn.value);
    var check = loadCheck(par.assign, jobs, m);
    if (!check.ok) { blank(check.why); return; }
    if (!Requ(check.makespan, par.makespan)) {
      blank('the makespan the rule reported is not the makespan of the assignment it produced');
      return;
    }
    var optCheck = par.optimumAssign ? loadCheck(par.optimumAssign, jobs, m) : null;
    if (optCheck && !Requ(optCheck.makespan, par.optimum)) {
      blank('the optimum reported is not the makespan of the assignment said to attain it');
      return;
    }
    var order = par.steps.map(function (s) { return s.job; });
    var span = par.optimum === null ? par.makespan
      : (Rcmp(par.makespan, par.optimum) > 0 ? par.makespan : par.optimum);

    plot.innerHTML = schedGantt(machineBars(par.assign, jobs, m, order), {
      width: 660, height: 190, span: span, ticks: schedTicks(span),
      marks: [{ at: par.bounds.best, label: 'lower bound ' + Rtext(par.bounds.best), tone: 'amber' }],
      caption: ruleIn.value + ' finishes at ' + Rtext(par.makespan)
    });
    if (par.optimumAssign) {
      var oorder = [];
      for (i = 0; i < jobs.length; i += 1) oorder.push(i);
      bestSvg.innerHTML = schedGantt(machineBars(par.optimumAssign, jobs, m, oorder), {
        width: 660, height: 190, span: span, ticks: schedTicks(span),
        marks: [{ at: par.bounds.best, label: 'lower bound ' + Rtext(par.bounds.best), tone: 'amber' }],
        caption: 'the best of ' + par.count + ' assignments finishes at ' + Rtext(par.optimum)
      });
    } else {
      bestSvg.innerHTML = '<text x="330" y="96" text-anchor="middle" font-size="11" fill="var(--muted)">'
        + 'too many assignments to enumerate — no optimum is claimed</text>';
    }

    var rows = '';
    for (i = 0; i < par.steps.length; i += 1) {
      var s = par.steps[i];
      rows += tr([rowhead(String(i + 1)), td(s.id), td(Rtext(jobs[s.job].p)), td('M' + (s.machine + 1)),
                  td(Rtext(s.load)),
                  tdl('it went to the machine with the least on it at that moment')]);
    }
    stepsT.innerHTML = '<caption>' + ruleIn.value + ', one placement at a time</caption><thead>'
      + tr([th('step'), th('job'), th('p'), th('machine'), th('its load after'), th('why there')])
      + '</thead><tbody>' + rows + '</tbody>';

    var brows = '';
    brows += tr([rowhead('total work ÷ machines'), td(Rtext(par.bounds.average)),
                 tdl('some machine must do at least its share of the work')]);
    brows += tr([rowhead('the longest single job'), td(Rtext(par.bounds.longest)),
                 tdl('that job runs on one machine and cannot be split')]);
    brows += tr([rowhead('the better of the two'), td(tone(Rtext(par.bounds.best), 'amber')),
                 tdl('neither implies the other, which is why the proof uses both')], 'tone-amber');
    if (par.optimum !== null) {
      brows += tr([rowhead('the optimum, by enumeration'), td(tone(Rtext(par.optimum), 'purple')),
                   tdl('every one of the ' + par.count + ' ways to deal ' + jobs.length
                       + ' jobs to ' + m + ' machines')], 'tone-purple');
    }
    brows += tr([rowhead(ruleIn.value + "'s makespan"), td(tone(Rtext(par.makespan), 'cyan')),
                 tdl('what the rule actually achieved')], 'tone-cyan');
    boundT.innerHTML = '<caption>What is known before any schedule is built, and what is known after</caption>'
      + '<thead>' + tr([th('quantity'), th('value'), th('why it is what it is')]) + '</thead>'
      + '<tbody>' + brows + '</tbody>';

    document.getElementById('plMake').textContent = Rtext(par.makespan);
    document.getElementById('plOpt').textContent = par.optimum === null ? 'not enumerated' : Rtext(par.optimum);
    document.getElementById('plRatio').textContent = par.ratio === null ? '—'
      : Rtext(par.ratio) + (Rcmp(par.ratio, R(4n, 3n)) <= 0 ? ' — inside 4/3' : ' — OUTSIDE 4/3');
    document.getElementById('plAvg').textContent = Rtext(par.bounds.average);
    document.getElementById('plMax').textContent = Rtext(par.bounds.longest);
    document.getElementById('plBound').textContent = Rtext(par.bounds.best)
      + (Rcmp(par.bounds.average, par.bounds.longest) > 0 ? ' — the average' : ' — the longest job');

    var tight = par.optimum !== null && Requ(par.optimum, par.bounds.best);
    status.innerHTML = '<strong>' + ruleIn.value + ' finishes at ' + tone(Rtext(par.makespan), 'cyan')
      + (par.optimum === null ? '' : ' where the best possible is ' + tone(Rtext(par.optimum), 'purple'))
      + '.</strong> The two lower bounds are ' + Rtext(par.bounds.average) + ' and '
      + Rtext(par.bounds.longest) + ', and ' + (Rcmp(par.bounds.average, par.bounds.longest) > 0
          ? 'here the average is the binding one'
          : (Requ(par.bounds.average, par.bounds.longest)
              ? 'here they are equal' : 'here the longest job is the binding one'))
      + '. ' + (tight
          ? 'The optimum meets the bound, so nothing was left on the table and the bound alone would '
            + 'have told you the answer. '
          : (par.optimum === null ? ''
             : 'The optimum is ' + Rtext(Rsub(par.optimum, par.bounds.best)) + ' above the bound, so a '
               + 'reader who stopped at the bound would have believed a schedule existed that does not. '))
      + (par.ratio === null ? ''
          : (Rzero(Rsub(par.ratio, R1))
              ? tone('On this instance the rule is exactly optimal.', 'green')
              : tone('The rule is ' + Rtext(par.ratio) + ' times the optimum here', 'red')
                + ', inside the 4/3 it is proved to but not at it — and that gap is the reason a '
                + 'heuristic is reported with a bound rather than on its own.'))
      + ' Every load above was added up a second time from the assignment itself before it was '
      + 'printed, so the makespan is the schedule&rsquo;s and not the rule&rsquo;s bookkeeping.';
  }

  function apply() {
    var p = PLP[presetIn.value];
    if (!p) return;
    jobsIn.value = p.jobs; mIn.value = p.machines;
    redraw();
  }
  presetIn.addEventListener('change', apply);
  ruleIn.addEventListener('change', redraw);
  jobsIn.addEventListener('input', redraw);
  mIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Identical machines in parallel",
        subtitle="LPT against the exhaustive optimum, and against both of the bounds its guarantee is proved from",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Deal the jobs to m machines, then check the deal"),
        panel_intro=cfg.get(
            "panel_intro",
            "The heuristic places one job at a time; the loads are then added up again from the "
            "assignment alone, and the result is compared with every possible assignment and with "
            "both lower bounds. On this example: " + chosen["note"] + ".",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L8 -- jobshop: every orientation of every disjunctive pair
# ---------------------------------------------------------------------------

_JS_PRESETS = [
    {
        "id": "two",
        "label": "two jobs, two machines, opposite routes",
        "ops": "J1 M1 3, J1 M2 2, J2 M2 4, J2 M1 1",
        "note": "four orientations, one of which deadlocks",
    },
    {
        "id": "three",
        "label": "three jobs sharing two machines",
        "ops": "J1 M1 2, J1 M2 3, J2 M2 2, J2 M1 4, J3 M1 3",
        "note": "five operations, four disjunctive pairs, sixteen orientations",
    },
    {
        "id": "chain",
        "label": "one machine everything has to pass through",
        "ops": "J1 M1 4, J1 M2 2, J2 M1 3, J2 M2 5, J3 M1 2",
        "note": "M1 carries three operations, so three of the pairs are on it alone",
    },
]


def _jobshop(cfg):
    chosen = _choose(cfg, "jobshop", _JS_PRESETS, "two")

    markup = (
        _toolbar(
            "The job shop: orienting every conflict",
            "two operations on one machine must be ordered somehow, and some choices deadlock",
            [("cyan", "machine 1"), ("purple", "machine 2"), ("green", "on the critical path"),
             ("red", "an orientation that deadlocks")],
        )
        + _stage(_svg("jsPlot", "0 0 660 190",
                      "The chosen orientation, drawn as one track per machine.")
                 + _svg("jsBars", "0 0 660 70",
                        "A strip of every orientation's makespan, deadlocks marked."))
        + _table("jsOps")
        + _table("jsAll")
        + _banner("jsStatus")
    )
    controls = (
        _select("jsPreset", "Worked example", _options(_JS_PRESETS), chosen["id"])
        + _text("jsOpsIn", "Operations, as job machine duration, in each job's own order", chosen["ops"])
        + _range("jsPick", "Which orientation to draw", 0, 63, 0)
        + _select("jsShow", "Draw",
                  [("best", "the best orientation"), ("pick", "the one the slider names")], "best")
        + _kpis([
            ("Operations", "jsOps1"),
            ("Pairs on a shared machine", "jsPairs"),
            ("Orientations, 2 to that power", "jsTotal"),
            ("The shortest makespan", "jsBestV"),
            ("Orientations that deadlock", "jsDead"),
            ("The one drawn finishes at", "jsDrawn"),
        ])
        + _hint(
            "jsHint",
            "Each job visits its machines in its own order, and that is fixed. What is not fixed is "
            "which of two operations sharing a machine goes first &mdash; one bit per pair. Choose all "
            "the bits and the shop becomes an ordinary project network whose longest path is the "
            "makespan; choose them badly and the network has a cycle, which is a deadlock and a real "
            "answer rather than an error.",
        )
    )

    script = _MODE_JS["jobshop"] + r"""
""" + _presets_js("JSP", _JS_PRESETS, ["ops", "note"]) + r"""
  var presetIn = document.getElementById('jsPreset'), opsIn = document.getElementById('jsOpsIn');
  var pickIn = document.getElementById('jsPick'), showIn = document.getElementById('jsShow');
  var plot = document.getElementById('jsPlot'), bars = document.getElementById('jsBars');
  var opsT = document.getElementById('jsOps'), allT = document.getElementById('jsAll');
  var status = document.getElementById('jsStatus');
  var KPIS = ['jsOps1', 'jsPairs', 'jsTotal', 'jsBestV', 'jsDead', 'jsDrawn'];

  function blank(why) {
    plot.innerHTML = ''; bars.innerHTML = ''; opsT.innerHTML = ''; allT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An operation is a job, a machine '
      + 'and a duration, and a job&rsquo;s operations run in the order you write them.';
  }

  function redraw() {
    var parsed = parseOps(opsIn.value);
    if (parsed.bad) { blank(parsed.bad); return; }
    var ops = parsed.ops, i, k;
    var all = jobShopAll(ops);
    if (all.truncated) { blank(all.why); return; }
    if (!all.best) { blank('every orientation of these operations deadlocks, so there is no schedule'); return; }
    var total = all.total;
    var pick = Math.max(0, Math.min(total - 1, Math.round(+pickIn.value)));
    document.getElementById('jsPickOut').textContent = pick + ' of ' + (total - 1);
    var mask = showIn.value === 'best' ? all.best.mask : pick;
    var times = shopTimes(ops, all.pairs, mask);
    var bestTimes = shopTimes(ops, all.pairs, all.best.mask);
    if (!bestTimes.cycle && !Requ(bestTimes.makespan, all.best.makespan)) {
      blank('the start times read off the best orientation do not reproduce its makespan');
      return;
    }
    var feas = times.cycle ? null : shopFeasible(ops, times.start);
    if (feas && (!feas.ok || !Requ(feas.makespan, times.makespan))) {
      blank('the schedule drawn is not a schedule: ' + (feas.faults.join('; ')
            || 'its last bar ends at ' + Rtext(feas.makespan) + ' and the longest path says '
               + Rtext(times.makespan)));
      return;
    }

    var machines = [], mix = {};
    for (k = 0; k < ops.length; k += 1) {
      if (mix[ops[k].machine] === undefined) { mix[ops[k].machine] = machines.length; machines.push(ops[k].machine); }
    }
    var tones = ['cyan', 'purple', 'blue', 'amber'];
    if (times.cycle) {
      plot.innerHTML = '<text x="330" y="90" text-anchor="middle" font-size="12" font-weight="700" '
        + 'fill="var(--red)">orientation ' + mask + ' deadlocks</text>'
        + '<text x="330" y="112" text-anchor="middle" font-size="11" fill="var(--muted)">'
        + times.cycle.join(' → ') + ' → ' + times.cycle[0] + '</text>';
    } else {
      var tracks = [];
      for (i = 0; i < machines.length; i += 1) tracks.push({ name: machines[i], bars: [] });
      for (k = 0; k < ops.length; k += 1) {
        var critical = times.critical['o' + k];
        tracks[mix[ops[k].machine]].bars.push({
          label: ops[k].job, start: times.start[k], end: Radd(times.start[k], ops[k].dur),
          tone: critical ? 'green' : tones[mix[ops[k].machine] % tones.length], wide: !!critical
        });
      }
      plot.innerHTML = schedGantt(tracks, {
        width: 660, height: 190, span: times.makespan, ticks: schedTicks(times.makespan),
        caption: 'orientation ' + mask + ' finishes at ' + Rtext(times.makespan)
                 + '; the green bars are the longest path through it'
      });
    }

    var strip = '', wide = 660 / Math.max(1, total), shown = Math.min(total, 32);
    for (i = 0; i < shown; i += 1) {
      var o = all.orientations[i], x = (660 / shown) * (i + 0.5);
      strip += '<text x="' + Math.round(x) + '" y="22" text-anchor="middle" font-size="10" '
        + 'font-weight="700" fill="var(--' + (o.cyclic ? 'red' : (Requ(o.makespan, all.best.makespan)
            ? 'green' : 'cyan')) + ')">' + (o.cyclic ? 'dead' : Rtext(o.makespan)) + '</text>'
        + '<text x="' + Math.round(x) + '" y="38" text-anchor="middle" font-size="9" '
        + 'fill="var(--muted)">' + i + '</text>';
    }
    bars.innerHTML = strip;

    var rows = '';
    for (k = 0; k < ops.length; k += 1) {
      rows += tr([rowhead(ops[k].job + ' on ' + ops[k].machine), td(Rtext(ops[k].dur)),
                  td(times.cycle ? '—' : Rtext(times.start[k])),
                  td(times.cycle ? '—' : Rtext(Radd(times.start[k], ops[k].dur))),
                  td(times.cycle ? '—' : (times.critical['o' + k] ? tone('critical', 'green') : 'has slack'))],
                 times.cycle ? null : (times.critical['o' + k] ? 'tone-green' : null));
    }
    opsT.innerHTML = '<caption>The operations under orientation ' + mask + '</caption><thead>'
      + tr([th('operation'), th('takes'), th('starts'), th('finishes'), th('on the longest path')])
      + '</thead><tbody>' + rows + '</tbody>';

    var arows = '', limit = Math.min(total, 32);
    for (i = 0; i < limit; i += 1) {
      var or = all.orientations[i], bits = [];
      for (k = 0; k < all.pairs.length; k += 1) {
        var a = all.pairs[k][0], b = all.pairs[k][1];
        bits.push((or.mask & (1 << k))
          ? ops[a].job + '→' + ops[b].job : ops[b].job + '→' + ops[a].job);
      }
      arows += tr([rowhead(String(or.mask)), tdl(bits.join(', ')),
                   td(or.cyclic ? tone('deadlock', 'red') : Rtext(or.makespan)),
                   td(or.cyclic ? tone(or.cycle.join(' → '), 'red')
                      : (Requ(or.makespan, all.best.makespan) ? tone('the best', 'green') : ''))],
                  or.cyclic ? 'tone-red' : (Requ(or.makespan, all.best.makespan) ? 'tone-green' : null));
    }
    if (total > limit) {
      arows += tr([tdl('and ' + (total - limit) + ' more, all of them scored', 'small-copy')
                   .replace('<td', '<td colspan="4"')]);
    }
    allT.innerHTML = '<caption>Every orientation, scored by the longest path through it</caption>'
      + '<thead>' + tr([th('mask'), th('who goes first on each shared machine'), th('makespan'),
                        th('note')]) + '</thead><tbody>' + arows + '</tbody>';

    document.getElementById('jsOps1').textContent = String(ops.length);
    document.getElementById('jsPairs').textContent = String(all.pairs.length);
    document.getElementById('jsTotal').textContent = '2^' + all.pairs.length + ' = ' + total;
    document.getElementById('jsBestV').textContent = Rtext(all.best.makespan);
    document.getElementById('jsDead').textContent = all.cyclic + ' of ' + total;
    document.getElementById('jsDrawn').textContent = times.cycle ? 'it deadlocks' : Rtext(times.makespan);

    var worst = null;
    for (i = 0; i < all.orientations.length; i += 1) {
      var q = all.orientations[i];
      if (!q.cyclic && (worst === null || Rcmp(q.makespan, worst) > 0)) worst = q.makespan;
    }
    status.innerHTML = '<strong>' + all.pairs.length + ' pair'
      + plural(all.pairs.length, '', 's') + ' share a machine, so there are ' + tone(String(total), 'cyan')
      + ' orientations</strong> and every one of them was scored. The best finishes at '
      + tone(Rtext(all.best.makespan), 'green') + ', the worst that works at '
      + tone(Rtext(worst), 'amber') + ', and ' + tone(all.cyclic + ' of them', 'red')
      + ' cannot be run at all: the orientations point round in a circle and each operation is waiting '
      + 'for one that is waiting for it. '
      + (times.cycle
          ? 'The one drawn is one of those — ' + tone(times.cycle.join(' → '), 'red') + '. '
          : 'The one drawn was read back operation by operation before it was printed: no machine runs '
            + 'two things at once, and no job starts a step before the step before it has finished. ')
      + 'Doubling the shop doubles the exponent, which is why this page stops at eight operations and '
      + 'why a real shop is not solved this way.';
  }

  function apply() {
    var p = JSP[presetIn.value];
    if (!p) return;
    opsIn.value = p.ops;
    redraw();
  }
  presetIn.addEventListener('change', apply);
  showIn.addEventListener('change', redraw);
  opsIn.addEventListener('input', redraw);
  pickIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The job shop: orienting every conflict",
        subtitle="One bit per pair of operations on a machine; some settings of those bits deadlock",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose who goes first on each machine, or let the lab try them all"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every orientation is scored by the longest path through the network it makes, the "
            "deadlocks are counted rather than hidden, and the schedule drawn is read back before "
            "any figure is printed. On this example: " + chosen["note"] + ".",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# L9 -- crash: the time-cost curve, and CPM run on what the LP bought
# ---------------------------------------------------------------------------

_CR_PRESETS = [
    {
        "id": "diamond",
        "label": "four activities, two parallel paths",
        "acts": "A 6:4:100:140, B 4:2:80:120 | A, C 5:3:60:90 | A, D 3:2:50:80 | B C",
        "note": "shortening A helps until the two middle paths become critical together",
    },
    {
        "id": "series",
        "label": "a straight chain of three",
        "acts": "A 5:3:40:70, B 6:3:50:110 | A, C 4:2:30:70 | B",
        "note": "one path, so the cheapest rate is bought first and the curve has three pieces",
    },
    {
        "id": "cheapfirst",
        "label": "the cheapest activity to crash is not on the critical path",
        "acts": "A 4:2:40:48, B 7:4:60:120 | A, C 2:1:20:24, D 5:3:40:70 | C",
        "note": "A and C cost little to shorten and only one of the two chains decides the finish",
    },
]


def _crash(cfg):
    chosen = _choose(cfg, "crash", _CR_PRESETS, "diamond")

    markup = (
        _toolbar(
            "Buying time, and what each day costs",
            "the crash bill is a linear programme, and its time-cost curve bends where the critical path changes",
            [("cyan", "an activity with slack"), ("red", "on the critical path"),
             ("purple", "a breakpoint in the curve"), ("green", "the deadline, met and verified")],
        )
        + _stage(_svg("crPlot", "0 0 660 200",
                      "The crashed project, each activity drawn from its earliest start to its earliest finish.")
                 + _svg("crCurve", "0 0 520 260",
                        "The total cost of the project against the deadline it is held to."))
        + _table("crActs")
        + _table("crPieces")
        + _banner("crStatus")
    )
    controls = (
        _select("crPreset", "Worked example", _options(_CR_PRESETS), chosen["id"])
        + _text("crActs2", "Activities, as name normal:crash:normal cost:crash cost | predecessors",
                chosen["acts"])
        + _range("crCut", "Days off the normal finish", 0, 10, 3)
        + _kpis([
            ("The project at normal durations", "crNormal"),
            ("The deadline you set", "crDeadline"),
            ("The crash bill", "crBill"),
            ("Total cost, normal plus crash", "crTotal"),
            ("CPM on the crashed durations", "crCheck"),
            ("Curve pieces confirmed by a fresh solve", "crConf"),
        ])
        + _hint(
            "crHint",
            "The objective is only the crash bill: the normal cost is paid whatever the deadline, so "
            "it shifts the curve without bending it. The deadline is one right-hand side, which is "
            "why the exact time-cost curve is the same ranging function &ldquo;Duality and "
            "Sensitivity Analysis&rdquo; used on a resource row and not a second implementation of "
            "anything.",
        )
    )

    script = _MODE_JS["crash"] + r"""
""" + _presets_js("CRP", _CR_PRESETS, ["acts", "note"]) + r"""
  var OPTS = { rule: 'bland', maxPivots: 400 };
  var presetIn = document.getElementById('crPreset'), actsIn = document.getElementById('crActs2');
  var cutIn = document.getElementById('crCut');
  var plot = document.getElementById('crPlot'), curveSvg = document.getElementById('crCurve');
  var actsT = document.getElementById('crActs'), piecesT = document.getElementById('crPieces');
  var status = document.getElementById('crStatus');
  var KPIS = ['crNormal', 'crDeadline', 'crBill', 'crTotal', 'crCheck', 'crConf'];

  function blank(why) {
    plot.innerHTML = ''; curveSvg.innerHTML = ''; actsT.innerHTML = ''; piecesT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An activity is a name, then its '
      + 'normal time, crash time, normal cost and crash cost separated by colons, then a vertical bar '
      + 'and the activities it waits for.';
  }

  function redraw() {
    var parsed = parseActivities(actsIn.value);
    if (parsed.bad) { blank(parsed.bad); return; }
    var acts = parsed.acts, n = acts.length, i;
    var normal = cpmPasses(acts.map(function (a) { return { id: a.id, dur: a.normal, pred: a.pred }; }));
    var floor = cpmPasses(acts.map(function (a) { return { id: a.id, dur: a.crash, pred: a.pred }; }));
    var cut = Math.max(0, Math.min(10, Math.round(+cutIn.value)));
    var want = Rsub(normal.makespan, R(BigInt(cut), 1n));
    if (Rcmp(want, floor.makespan) < 0) want = floor.makespan;
    document.getElementById('crCutOut').textContent = cut + ' → deadline ' + Rtext(want);

    var cm = crashModel(acts, want);
    var sol = lpSolve(cm.model, OPTS);
    if (sol.status !== 'optimal') {
      blank('at a deadline of ' + Rtext(want) + ' the programme is ' + sol.status);
      return;
    }
    var plan = crashPlan(cm, sol);
    var check = crashVerify(cm, plan, want);
    if (!check.ok) {
      blank('the plan the programme returned does not survive a forward and backward pass: '
            + (check.overspent.length ? 'it crashes ' + check.overspent.join(' and ')
               + ' past what they can be crashed' : 'CPM makes it finish at ' + Rtext(check.makespan)
               + ' against a deadline of ' + Rtext(want)));
      return;
    }
    var cc = crashCurve(acts, floor.makespan, normal.makespan, OPTS);

    var bars = [], cp = check.cpm, crit = {};
    for (i = 0; i < check.critical.length; i += 1) crit[check.critical[i]] = true;
    for (i = 0; i < n; i += 1) {
      bars.push({ label: acts[i].id, start: cp.ES[i], end: cp.EF[i],
                  tone: crit[acts[i].id] ? 'red' : 'cyan', wide: !!crit[acts[i].id],
                  sub: Rzero(cp.slack[i]) ? null : 'slack ' + Rtext(cp.slack[i]) });
    }
    plot.innerHTML = schedGantt([{ name: 'project', bars: bars }], {
      width: 660, height: 200, span: normal.makespan, ticks: schedTicks(normal.makespan),
      marks: [{ at: want, label: 'deadline ' + Rtext(want), tone: 'green' }],
      caption: 'each activity at its earliest start, with the crashed durations the programme bought'
    });
    curveSvg.innerHTML = crashPlot(cc.pieces, { width: 520, height: 260, add: cm.normalCost,
      caption: 'the deadline, in days — total cost on the vertical' });

    var rows = '';
    for (i = 0; i < n; i += 1) {
      var a = acts[i], room = Rsub(a.normal, a.crash);
      rows += tr([rowhead(a.id), td(Rtext(a.normal)), td(Rtext(a.crash)),
                  td(Rzero(room) ? 'cannot be crashed' : Rtext(cm.rates[i]) + ' a day'),
                  td(Rtext(plan.y[i])), td(Rtext(plan.dur[i])),
                  td(Rtext(cp.ES[i]) + ' → ' + Rtext(cp.EF[i])),
                  td(crit[a.id] ? tone('critical', 'red') : 'slack ' + Rtext(cp.slack[i]))],
                 crit[a.id] ? 'tone-red' : null);
    }
    actsT.innerHTML = '<caption>What the programme bought, and what a forward and backward pass make of it</caption>'
      + '<thead>' + tr([th('activity'), th('normal'), th('crash limit'), th('rate'), th('crashed by'),
                        th('runs for'), th('ES → EF'), th('verdict')]) + '</thead>'
      + '<tbody>' + rows + '</tbody>';

    var prows = '';
    for (i = 0; i < cc.pieces.length; i += 1) {
      var p = cc.pieces[i];
      prows += tr([rowhead(Rtext(p.from) + ' to ' + Rtext(p.to)),
                   td(Rtext(Rneg(p.slope)) + ' a day'),
                   td(Rtext(Radd(p.z, cm.normalCost))),
                   td(Rtext(Radd(p.zEnd, cm.normalCost))),
                   tdl(i ? 'a different set of paths is critical here, so a different activity is '
                         + 'the cheapest one left to shorten'
                         : 'the cheapest way to buy the first days')]);
    }
    piecesT.innerHTML = '<caption>The exact time-cost curve, piece by piece — ' + cc.confirmed
      + ' of ' + cc.checked + ' confirmed by a fresh solve at the left end</caption><thead>'
      + tr([th('deadline range'), th('each day costs'), th('total at the left'), th('total at the right'),
            th('what changed')]) + '</thead><tbody>' + prows + '</tbody>';

    document.getElementById('crNormal').textContent = Rtext(normal.makespan) + ' days';
    document.getElementById('crDeadline').textContent = Rtext(want) + ' days';
    document.getElementById('crBill').textContent = Rtext(plan.crashBill);
    document.getElementById('crTotal').textContent = Rtext(plan.total);
    document.getElementById('crCheck').textContent = Rtext(check.makespan)
      + (check.meets ? ' — meets it' : ' — MISSES it');
    document.getElementById('crConf').textContent = cc.confirmed + ' of ' + cc.checked;

    var bought = [];
    for (i = 0; i < n; i += 1) if (Rsign(plan.y[i]) > 0) bought.push(acts[i].id + ' by ' + Rtext(plan.y[i]));
    status.innerHTML = '<strong>Finishing by ' + tone(Rtext(want), 'green') + ' costs '
      + tone(Rtext(plan.crashBill), 'cyan') + ' in crashing</strong>, on top of the '
      + Rtext(cm.normalCost) + ' the project costs anyway — ' + Rtext(plan.total) + ' in all. '
      + (bought.length ? 'It buys ' + bought.join(' and ') + '. ' : 'It buys nothing: the normal plan '
        + 'already meets the deadline. ')
      + 'That is what the tableau says; what makes it believable is the row below it. A forward and a '
      + 'backward pass over the CRASHED durations — nothing to do with the simplex — finish the '
      + 'project at ' + tone(Rtext(check.makespan), check.meets ? 'green' : 'red') + ', with '
      + tone(check.critical.join(', '), 'red') + ' critical along '
      + check.paths.length + ' path' + plural(check.paths.length, '', 's') + '. '
      + 'The curve has ' + tone(cc.pieces.length + ' piece' + plural(cc.pieces.length, '', 's'), 'purple')
      + ' and it steepens from left to right: ' + cc.pieces.map(function (q) { return Rtext(Rneg(q.slope)); })
        .join(', then ') + ' a day. It bends where the set of critical paths changes, because after '
      + 'that point a day has to be bought on two paths at once. Each piece was re-solved from '
      + 'scratch at its own left endpoint and ' + cc.confirmed + ' of ' + cc.checked + ' agreed.';
  }

  function apply() {
    var p = CRP[presetIn.value];
    if (!p) return;
    actsIn.value = p.acts;
    redraw();
  }
  presetIn.addEventListener('change', apply);
  actsIn.addEventListener('input', redraw);
  cutIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Buying time, and what each day costs",
        subtitle="The crash bill is a linear programme; its curve bends where the critical path changes",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Set a deadline and watch what it costs to meet"),
        panel_intro=cfg.get(
            "panel_intro",
            "The programme is solved exactly, the durations it buys are put back through a forward "
            "and a backward pass to confirm the deadline is really met, and every piece of the "
            "time-cost curve is re-solved from scratch at its own endpoint. On this example: "
            + chosen["note"] + ".",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# The dispatch. `tardiness` is deliberately absent: 1||sum T has no exchange
# argument, and a mode offering a rule for it would teach the opposite of the
# course. The `objectives` and `edd` modes show its exhaustive optimum and name
# it as the boundary instead.
# ---------------------------------------------------------------------------

_MODES = {
    "objectives": _objectives,
    "spt": _spt,
    "wspt": _wspt,
    "edd": _edd,
    "late": _late,
    "flowshop": _flowshop,
    "parallel": _parallel,
    "jobshop": _jobshop,
    "crash": _crash,
}

MODES = tuple(sorted(_MODES))


def schedule_lab(cfg):
    """Course 6's scheduling kit. `cfg["mode"]` chooses the lesson.

    An unknown mode raises, and so does an unknown preset. The raise is the
    contract rather than defensiveness: a kit that fell back to a default would
    render a finished-looking page carrying another lesson's widget, or the
    right lesson's widget opened on someone else's worked example. Both pass
    every markup assertion in the suite and both pass labcheck, because the lab
    builds and draws; the reader is simply shown the wrong arithmetic under the
    right title.
    """
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "schedule_lab: unknown mode %r; the nine modes of the scheduling course are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["schedule_lab", "MODES", "SCHEDKIT_JS", "SCHEDSHOP_JS", "SCHEDCRASH_JS"]
