"""cckit -- the lab kit of Code Complete, Read Along.

Specified in docs/code-complete/PLAN.md section D (D.0 conventions, D.1 the
eight modes and 36 views, D.2 what the kit must never do, D.3 the build-time
checks); the report an author configures a lesson from is
docs/code-complete/kit-report.md. Eight modes, in three families (PLAN.md 0):

  code     (co)  a count over a Java listing: size, class, dupes, extract,
                 ppp, dataflow, span, names, literals, complexity, basis,
                 layout                                           (family 1)
  deps     (dg)  coupling, ripple, tree, shared, integrate         (2)
  cond     (cd)  truth, range, barricade                           (2)
  search   (se)  chain, stairs, bisect                             (2)
  run      (lp; nu for arith's tiles)  loop, nested, recursion, arith  (2)
  defects  (df)  cost, removal, pipeline                           (3)
  profile  (pf)  shares, speedup                                   (3)
  project  (pj)  language, scale, effort, breakeven                (3)

This module holds the entry point and the `code` mode; cckit_b.py holds the
other seven; cckit_core.py the shared printing, parsing, tokenizer, statement
reader and wiring. Each mode has one pure JS function <xx>Compute(view, inst,
opts), which scripts/mathcheck.js calls (section "cckit"). A page ships
RATIONAL_JS, CC_CORE_JS, the tokenizer only when the mode is `code`, its mode's
base block and its own view's block -- never the other views (D.0, page
weight).

THE KIT READS CODE; IT NEVER RUNS IT (D.2). Nothing is evaluated as script:
the tokenizer and the condition parser are the kit's own.

VIEW IS NOT A CONTROL. cfg["view"] fixes which inputs and tiles the page shows;
an unknown mode or view raises. The lesson-level values (min_run, min, bands,
book, indent; table, tag, tag_label, target, unit, source) come from the cfg, never from
a preset.

IDS. Every tile id begins with its mode's prefix (co dg cd se lp nu df pf pj);
inputs are <prefix>In<Field>; the code box is coInCode beside coListing.
Grepped against scripts/mathpath/labs/*.py on 2026-10-25 for every JS function
and variable (cc*, CC_*, co*, CO_*, dg*, ..., PJ_*) and every element id the
kit defines. Two names are shared with another kit, never on one page:
lpCompute is also dekit_b.py's function, and seValue is also an argkit tile.
"""

from . import cckit_core as cc

KIT = "cckit"

# ---------------------------------------------------------------------------
# code: the shared base, then one block per view
# ---------------------------------------------------------------------------

CO_JS = r"""
  /* code: coCompute reads the listing once and hands it to the view. */
  var CO_VIEW = {};
  var CO_ORDER = ' The lab reads the lines top to bottom and does not follow branches or loops, so it is exact for '
    + 'straight-line code and an approximation otherwise.';
  function coCompute(view, inst, opts) {
    var L = ccReadCode(inst.code);
    if (L.refuse) return L;
    return CO_VIEW[view](L, inst, opts || {});
  }
  function coStatements(L) { return L.lines.filter(function (ln) { return ln.isCode && !ln.braceOnly; }); }
  function coLines(list) { return list.length === 1 ? 'line ' + list[0] : 'lines ' + list.join(', '); }
  var CO_WORD = { r: 'read', w: 'set', d: 'declared', p: 'parameter' };
"""

CO_DECIDE_JS = r"""
  /* Decision points: 1, plus one for each if, while, for, case, && and ||;
     and every switch whose block has no default. */
  var CO_KINDS = ['if', 'while', 'for', 'case', '&&', '||'];
  function coDecisions(L) {
    var pts = [], noDefault = 0, stack = [], d = 0, pending = 0, ternary = false;
    L.lines.forEach(function (ln) {
      ln.toks.forEach(function (t, k) {
        var v = t.v, next = k + 1 < ln.toks.length ? ln.toks[k + 1].v : '';
        if (CO_KINDS.indexOf(v) >= 0) pts.push({ line: ln.no, kind: v });
        if (v === '?' && next !== '>' && next !== ',' && next !== 'extends' && next !== 'super') ternary = true;
        if (v === 'switch') pending += 1;
        else if (v === 'default' && stack.length && stack[stack.length - 1].d === d) stack[stack.length - 1].def = true;
        if (v === '{') {
          d += 1;
          if (pending) { stack.push({ d: d, def: false }); pending -= 1; }
        } else if (v === '}') {
          if (stack.length && stack[stack.length - 1].d === d && !stack.pop().def) noDefault += 1;
          d -= 1;
        }
      });
    });
    stack.forEach(function (s) { if (!s.def) noDefault += 1; });
    return { pts: pts, noDefault: noDefault,
      ternary: ternary ? ' ?: is not counted: the kit\'s choice, not the book\'s.' : '' };
  }
"""

CO_VIEW_JS = {}

CO_VIEW_JS["size"] = r"""
  CO_VIEW.size = function (L) {
    var n = L.lines.length, code = 0, stm = 0, com = 0, blank = 0, both = 0, H = L.header;
    L.lines.forEach(function (ln) {
      if (ln.isCode) { code += 1; if (!ln.braceOnly) stm += 1; }
      if (ln.comment) com += 1;
      if (ln.isCode && ln.comment) both += 1;
      if (!ln.isCode && !ln.comment) blank += 1;
    });
    return {
      tiles: { coLines: ccInt(n), coCode: ccInt(code), coStatements: ccInt(stm), coComment: ccInt(com), coBlank: ccInt(blank),
        coParams: H ? ccInt(H.params.length) : 'none (a fragment)', coDensity: stm ? ccPct(R(com, stm)) : CC_DASH },
      status: ccPlural(n, 'line', 'lines') + ': ' + ccPlural(code, 'code line', 'code lines') + ' (' + stm + ' of them '
        + (stm === 1 ? 'a statement line' : 'statement lines') + '), ' + ccPlural(com, 'comment line', 'comment lines') + ', '
        + blank + ' blank.' + (both ? ' ' + both + (both === 1 ? ' line carries' : ' lines carry') + ' code and a comment and counts as both.' : '')
        + ' The book measures a routine\'s length in lines that are neither comment nor blank, which is the code-line count; '
        + 'the statement count also leaves out lines of only braces and semicolons.'
        + (H ? ' The routine ' + H.name + ' takes ' + ccPlural(H.params.length, 'parameter', 'parameters') + '.'
          : ' The listing has no routine header, so it is a fragment and has no parameter count.')
        + (stm ? ' Comment density is comment lines over statement lines, because the study the book cites counts comments per statement.'
          : ' There are no statement lines, so there is no comment density.'),
      table: null
    };
  };
"""

CO_VIEW_JS["class"] = r"""
  /* A member is a statement at brace depth 1, joined across lines up to its
     ; or {. A routine has ( before any =; a field ends in ; otherwise. */
  CO_VIEW['class'] = function (L) {
    var d = 0, cur = [], first = null, members = [], cls = null;
    L.lines.forEach(function (ln) {
      ln.toks.forEach(function (t, k) {
        if (d === 0 && cls === null && (t.v === 'class' || t.v === 'interface' || t.v === 'enum')) {
          cls = k + 1 < ln.toks.length ? ln.toks[k + 1].v : t.v;
        }
        if (d === 1) {
          if (t.v === ';' || t.v === '{') { if (cur.length) members.push({ line: first, v: cur.concat([t.v]) }); cur = []; first = null; }
          else if (t.v === '}') { cur = []; first = null; }
          else { if (!cur.length) first = ln.no; cur.push(t.v); }
        }
        if (t.v === '{') d += 1; else if (t.v === '}') d -= 1;
      });
    });
    var fields = [], routines = [], rows = [];
    members.forEach(function (m) {
      var v = m.v, last = v[v.length - 1], eq = v.indexOf('='), par = v.indexOf('(');
      var vis = v.filter(function (x) { return x === 'public' || x === 'private' || x === 'protected'; })[0] || 'package';
      if (par > 0 && (eq < 0 || par < eq)) {
        routines.push(vis);
        rows.push([String(m.line), v[par - 1], 'routine', vis]);
      } else if (last === ';') {
        var fin = v.indexOf('final') >= 0, end = eq >= 0 ? eq : v.length - 1;
        fields.push(vis === 'public' && !fin);
        rows.push([String(m.line), v[end - 1], 'field', vis + (fin ? ', final' : '')]);
      }
    });
    var pubF = fields.filter(Boolean).length, pubR = routines.filter(function (x) { return x === 'public'; }).length;
    return {
      tiles: { coFields: ccInt(fields.length), coPublicFields: ccInt(pubF), coRoutines: ccInt(routines.length), coPublicRoutines: ccInt(pubR) },
      status: (cls !== null ? 'The class ' + cls + ' has ' : 'The listing has no class header at brace depth 0; at brace depth 1 it has ')
        + ccPlural(fields.length, 'field', 'fields') + ' (' + pubF + ' public and not final) and '
        + ccPlural(routines.length, 'routine', 'routines') + ' (' + pubR + ' public). The lab reads the members at brace '
        + 'depth 1; a member\'s visibility is the first of public, private and protected it carries, else package.',
      table: rows.length ? { caption: 'Members at brace depth 1', head: ['line', 'member', 'kind', 'visibility'], rows: rows } : null
    };
  };
"""

CO_VIEW_JS["dupes"] = r"""
  /* Statement lines compared as text (white space collapsed, comments out);
     a repeated block is a run of at least min_run lines that occurs again,
     not overlapping, and not extendable backwards. */
  CO_VIEW.dupes = function (L, inst, opts) {
    var min = opts.min_run, st = coStatements(L).map(function (ln) { return { no: ln.no, key: ln.code.replace(/\s+/g, ' ').trim() }; });
    var n = st.length, found = {}, order = [], i, j;
    for (i = 0; i < n; i += 1) {
      for (j = i + 1; j < n; j += 1) {
        if (i > 0 && st[i - 1].key === st[j - 1].key) continue;
        var len = 0;
        while (j + len < n && i + len < j && st[i + len].key === st[j + len].key) len += 1;
        if (len < min) continue;
        var key = st.slice(i, i + len).map(function (x) { return x.key; }).join('\n');
        if (!found[key]) { found[key] = { len: len, starts: [] }; order.push(key); }
        [i, j].forEach(function (s) { if (found[key].starts.indexOf(s) < 0) found[key].starts.push(s); });
      }
    }
    var flags = {}, lines = 0, rows = [];
    var where = order.map(function (key, b) {
      var blk = found[key];
      blk.starts.sort(function (x, y) { return x - y; });
      lines += blk.len * blk.starts.length;
      var copies = blk.starts.map(function (s) {
        for (var k = s; k < s + blk.len; k += 1) ccFlag(flags, st[k].no, 'repeated');
        return 'lines ' + st[s].no + '–' + st[s + blk.len - 1].no;
      });
      rows.push([String(b + 1), ccPlural(blk.len, 'line', 'lines'), copies.join(', '), st[blk.starts[0]].key]);
      return copies.join(' and ');
    }).join('; ');
    return {
      tiles: { coDupBlocks: ccInt(order.length), coDupLines: ccInt(lines), coDupWhere: where || 'none' },
      status: (order.length ? ccPlural(order.length, 'block repeats', 'blocks repeat') + ', ' + ccPlural(lines, 'line', 'lines')
        + ' in all the copies.' : 'No run of ' + min + ' or more statement lines occurs twice.')
        + ' The lab matches text: it compares statement lines with their white space collapsed and their comments left out, '
        + 'so a copy with renamed variables is one it cannot see.',
      flags: flags,
      table: rows.length ? { caption: 'Repeated blocks', head: ['block', 'length', 'copies', 'first line of the block'], rows: rows } : null
    };
  };
"""

CO_VIEW_JS["extract"] = r"""
  CO_VIEW.extract = function (L, inst) {
    var n = L.lines.length, a = Number(inst.from.n), b = Number(inst.to.n);
    if (!n) return { refuse: 'The listing is empty, so there is no block to extract' };
    if (a > n || b > n) return { refuse: 'Line ' + (a > n ? a : b) + ' is past the end of the ' + n + '-line listing' };
    if (a > b) return { refuse: 'The block runs from line ' + a + ' to line ' + b + '; its first line must not come after its last' };
    var before = {}, all = {}, first = {}, order = [], set = {}, after = {};
    ccEvents(L).ev.forEach(function (x) {
      if (x.e !== 'r') { all[x.name] = true; if (x.line < a) before[x.name] = true; }
      if (x.line >= a && x.line <= b) {
        if (first[x.name] === undefined) { first[x.name] = x.e; order.push(x.name); }
        if (x.e === 'w') set[x.name] = true;
      }
      if (x.line > b && x.e === 'r') after[x.name] = true;
    });
    var ins = order.filter(function (v) { return first[v] === 'r' && before[v]; });
    var outs = order.filter(function (v) { return set[v] && after[v]; });
    var outside = order.filter(function (v) { return !all[v]; });
    var flags = {};
    for (var k = a; k <= b; k += 1) ccFlag(flags, k, 'in the block');
    return {
      tiles: { coIn: ccNames(ins), coOut: ccNames(outs), coParams: ccInt(ins.length), coOutside: ccNames(outside) },
      status: 'Lines ' + a + '–' + b + ' take ' + ccPlural(ins.length, 'value', 'values') + ' in (' + ccNames(ins)
        + ') and hand ' + ccPlural(outs.length, 'value', 'values') + ' out (' + ccNames(outs) + ').'
        + (outs.length > 1 ? ' A Java method returns one value, and ' + outs.length + ' names are set in the block and read after it.' : '')
        + (outside.length ? ' Read in the block but set nowhere in the listing: ' + ccNames(outside) + '.' : '')
        + CO_ORDER + ' It does not track the contents of arrays or objects: setting a field or an element only reads the names in it.',
      flags: flags,
      table: order.length ? { caption: 'Each name the block refers to', head: ['name', 'first in the block', 'set before', 'read after', 'role'],
        rows: order.map(function (v) {
          var role = !all[v] ? 'outside' : (ins.indexOf(v) >= 0 && outs.indexOf(v) >= 0 ? 'in and out'
            : (ins.indexOf(v) >= 0 ? 'in' : (outs.indexOf(v) >= 0 ? 'out' : 'local')));
          return [v, CO_WORD[first[v]], before[v] ? 'yes' : 'no', after[v] ? 'yes' : 'no', role];
        }) } : null
    };
  };
"""

CO_VIEW_JS["ppp"] = r"""
  /* The steps are the comment-only lines in the routine's body; a step's code
     is the statement lines before the next step or the body's end. */
  CO_VIEW.ppp = function (L) {
    var H = L.header;
    if (!H) {
      return { tiles: { coSteps: 'none (a fragment)' }, flags: {}, table: null,
        status: 'The listing has no routine header, so it is a fragment and has no body to read pseudocode steps in.' };
    }
    var steps = [], cur = null, code = 0;
    for (var i = 0; i < L.lines.length; i += 1) {
      var ln = L.lines[i];
      if (ln.no <= H.last) continue;
      if (L.depth[ln.no].start < 1) break;
      if (ln.comment && !ln.isCode) { cur = { line: ln.no, n: 0, text: ln.raw.trim() }; steps.push(cur); }
      else if (ln.isCode && !ln.braceOnly) { code += 1; if (cur) cur.n += 1; }
      if (L.depth[ln.no].end === 0) break;
    }
    var empty = steps.filter(function (s) { return s.n === 0; }).map(function (s) { return s.line; }), max = null, flags = {};
    steps.forEach(function (s) { if (!max || s.n > max.n) max = s; });
    empty.forEach(function (l) { ccFlag(flags, l, 'empty step'); });
    return {
      tiles: { coSteps: ccInt(steps.length), coCode: ccInt(code), coEmpty: empty.length ? coLines(empty) : 'none',
        coMaxUnder: max ? ccPlural(max.n, 'line', 'lines') + ', under line ' + max.line : CC_DASH },
      status: 'The body of ' + H.name + ' has ' + ccPlural(steps.length, 'pseudocode step', 'pseudocode steps')
        + ' (comment-only lines) and ' + ccPlural(code, 'statement line', 'statement lines') + '. '
        + (empty.length ? ccPlural(empty.length, 'step has', 'steps have') + ' no code before the next step or the end of the body: '
          + coLines(empty) + '.' : (steps.length ? 'Every step has code under it.' : 'With no steps, no step can be empty.'))
        + ' Statement lines before the first step belong to no step.',
      flags: flags,
      table: steps.length ? { caption: 'The steps', head: ['line', 'step', 'statement lines under it'],
        rows: steps.map(function (s) { return [String(s.line), s.text, { t: String(s.n), c: s.n ? '' : 'tone-amber' }]; }) } : null
    };
  };
"""

CO_VIEW_JS["dataflow"] = r"""
  /* Used before set: a read with no earlier set, once per name. Set twice: a
     set followed by another with no read between. Set, never used: the
     name's last event is a set. A name never set or declared is outside. */
  CO_VIEW.dataflow = function (L) {
    var ev = ccEvents(L).ev, hist = {}, order = [], lastw = {}, deps = {}, depList = [];
    ev.forEach(function (x) {
      if (!hist[x.name]) { hist[x.name] = []; order.push(x.name); }
      hist[x.name].push(x);
      if (x.e === 'r' && lastw[x.name] !== undefined && lastw[x.name] !== x.line) {
        var key = lastw[x.name] + '→' + x.line;
        if (!deps[key]) { deps[key] = true; depList.push([lastw[x.name], x.line]); }
      }
      if (x.e === 'w' || x.e === 'p') lastw[x.name] = x.line;
    });
    var ubs = [], twice = [], unused = [], outside = [], flags = {}, rows = [];
    order.forEach(function (name) {
      var h = hist[name], defined = false, pend = null, notes = [];
      if (!h.some(function (x) { return x.e !== 'r'; })) { outside.push(name); return; }
      h.forEach(function (x) {
        if (x.e === 'r') {
          if (!defined) { ubs.push({ name: name, line: x.line }); notes.push('used before set'); defined = true; }
          pend = null;
        } else if (x.e === 'w' || x.e === 'p') {
          if (pend !== null) { twice.push({ name: name, line: pend, b: x.line }); notes.push('set twice'); }
          defined = true;
          pend = x.line;
        }
      });
      var last = h[h.length - 1];
      if (last.e === 'w' || last.e === 'p') { unused.push({ name: name, line: last.line }); notes.push('set, never used'); }
      rows.push([name, h.map(function (x) { return CO_WORD[x.e] + ' ' + x.line; }).join(', '), notes.length ? notes.join('; ') : 'none']);
    });
    var byLine = function (a, b) { return a.line - b.line; };
    ubs.sort(byLine); twice.sort(byLine); unused.sort(byLine);
    ubs.forEach(function (x) { ccFlag(flags, x.line, 'used before set'); });
    twice.forEach(function (x) { ccFlag(flags, x.line, 'set twice'); ccFlag(flags, x.b, 'set twice'); });
    unused.forEach(function (x) { ccFlag(flags, x.line, 'set, never used'); });
    depList.sort(function (a, b) { return a[0] - b[0] || a[1] - b[1]; });
    var total = ubs.length + twice.length + unused.length;
    return {
      tiles: {
        coAnomalies: ccInt(total),
        coUsedBeforeSet: ccNames(ubs.map(function (x) { return x.name + ' (line ' + x.line + ')'; })),
        coSetTwice: ccNames(twice.map(function (x) { return x.name + ' (lines ' + x.line + ', ' + x.b + ')'; })),
        coUnused: ccNames(unused.map(function (x) { return x.name + ' (line ' + x.line + ')'; })),
        coDeps: ccNames(depList.map(function (p) { return p[0] + '→' + p[1]; }))
      },
      status: ccPlural(total, 'anomaly', 'anomalies') + ' in ' + ccPlural(rows.length, 'name', 'names') + ' the listing sets or declares'
        + ' (parameters are set on the header\'s line). A dependency i→j means line j reads a name whose latest set is on line i.'
        + (outside.length ? ' Read but never set in the listing (from outside it): ' + ccNames(outside) + '.' : '') + CO_ORDER,
      flags: flags,
      table: rows.length ? { caption: 'Each name, its events in line order', head: ['name', 'events', 'anomaly'], rows: rows } : null
    };
  };
"""

CO_VIEW_JS["span"] = r"""
  /* A name's references are the lines it appears on; a span is the lines
     strictly between two references; live time is last - first + 1. */
  CO_VIEW.span = function (L, inst) {
    var refs = {}, order = [], setters = {};
    ccEvents(L).ev.forEach(function (x) {
      if (!refs[x.name]) { refs[x.name] = []; order.push(x.name); }
      if (refs[x.name].indexOf(x.line) < 0) refs[x.name].push(x.line);
      if (x.e !== 'r') setters[x.name] = true;
    });
    var names = inst.vars.length ? inst.vars : order.filter(function (v) { return setters[v]; });
    for (var i = 0; i < names.length; i += 1) {
      if (!refs[names[i]]) return { refuse: '"' + names[i] + '" does not appear as a variable in the listing' };
    }
    if (!names.length) return { tiles: {}, table: null, status: 'The listing sets no variable, so there is nothing to measure.' };
    var spans = [], lives = [], best = null, rows = names.map(function (v) {
      var r = refs[v], sp = [];
      for (var k = 1; k < r.length; k += 1) sp.push(r[k] - r[k - 1] - 1);
      var live = r[r.length - 1] - r[0] + 1;
      spans = spans.concat(sp);
      lives.push(live);
      if (!best || live > best.live) best = { name: v, live: live };
      return [v, r.join(', '), sp.length ? sp.join(', ') : 'none', String(live)];
    });
    var sum = function (v) { return v.reduce(function (s, x) { return s + x; }, 0); };
    return {
      tiles: { coAvgSpan: spans.length ? ccNum(R(sum(spans), spans.length)) : CC_DASH, coAvgLive: ccNum(R(sum(lives), lives.length)),
        coLongest: best.name + ': ' + best.live },
      status: ccPlural(names.length, 'name', 'names') + ': ' + ccPlural(spans.length, 'span', 'spans') + ' pooled for the average span, '
        + 'and the live times averaged over the names.' + (spans.length ? '' : ' Each name is on one line only, so there are no spans to average.')
        + ' The book counts statements between references; the lab counts listing lines, and pooling the spans of several '
        + 'names is the lab\'s extension of the book\'s per-name average.' + CO_ORDER,
      table: { caption: 'References, spans and live time', head: ['name', 'lines', 'spans', 'live time'], rows: rows }
    };
  };
"""

CO_VIEW_JS["names"] = r"""
  /* Declared names: parameters, declarations, enhanced-for variables; loop
     indexes (declared in a for header) are listed and not counted. */
  CO_VIEW.names = function (L, inst, opts) {
    var names = [], seen = {}, loop = {}, min = opts.min;
    ccEvents(L).decls.forEach(function (d) {
      if (d.loop) loop[d.name] = true;
      if (!seen[d.name]) { seen[d.name] = true; names.push(d.name); }
    });
    var counted = names.filter(function (v) { return !loop[v]; });
    var short = counted.filter(function (v) { return v.length < min; });
    var total = counted.reduce(function (s, v) { return s + v.length; }, 0);
    var mean = counted.length ? R(total, counted.length) : null;
    return {
      tiles: { coNames: ccInt(names.length), coAvgLen: counted.length ? ccNum(R(total, counted.length)) : CC_DASH, coShort: ccNames(short) },
      status: ccPlural(names.length, 'declared name', 'declared names') + ', ' + counted.length + ' counted'
        + (names.length > counted.length ? ' (loop indexes are listed and not counted)' : '') + '. '
        + (counted.length ? 'Their mean length is ' + ccNum(mean) + (Requ(mean, R1) ? ' character; ' : ' characters; ')
          + ccPlural(short.length, 'is', 'are')
          + ' shorter than ' + min + '.' : 'No name is counted, so there is no mean length.'),
      table: names.length ? { caption: 'Declared names, in order', head: ['name', 'length', 'counted'],
        rows: names.map(function (v) { return [v, String(v.length), loop[v] ? 'no: a loop index' : (v.length < min ? { t: 'yes, short', c: 'tone-amber' } : 'yes')]; }) } : null
    };
  };
"""

CO_VIEW_JS["literals"] = r"""
  /* The value of a numeric literal, exactly; null when it is plainly
     neither 0 nor 1 and too long to work out. */
  function coLiteral(text) {
    var t = text.replace(/_/g, '');
    if (/^0[xXbB]/.test(t)) return R(BigInt(t.replace(/[lL]$/, '')));
    t = t.replace(/[lLfFdD]$/, '');
    var m = /^(\d*)(?:\.(\d*))?(?:[eE]([+-]?\d+))?$/.exec(t);
    if (!m) return null;
    var frac = m[2] || '', n = BigInt((m[1] || '0') + frac), e = (m[3] ? parseInt(m[3], 10) : 0) - frac.length;
    if (n === 0n) return R0;
    if (e > 400 || e < -400) return null;
    return e >= 0 ? R(n * 10n ** BigInt(e)) : R(n, 10n ** BigInt(-e));
  }
  CO_VIEW.literals = function (L) {
    var occ = {}, order = [], total = 0;
    L.lines.forEach(function (ln) {
      if (ln.vals.indexOf('final') >= 0) return;
      ln.toks.forEach(function (t) {
        if (t.k !== 'num') return;
        var v = coLiteral(t.v);
        if (v && (Requ(v, R0) || Requ(v, R1))) return;
        if (!occ[t.v]) { occ[t.v] = []; order.push(t.v); }
        occ[t.v].push(ln.no);
        total += 1;
      });
    });
    return {
      tiles: { coMagic: ccInt(total), coDistinct: ccInt(order.length),
        coMagicList: ccNames(order.map(function (k) { return k + ' (' + coLines(occ[k]) + ')'; })) },
      status: ccPlural(total, 'numeric literal', 'numeric literals') + ' (' + order.length + ' distinct) outside the lines that '
        + 'declare a final. The lab leaves out 0 and 1, and every literal on a line that contains final.',
      table: null
    };
  };
"""

CO_VIEW_JS["complexity"] = r"""
  CO_VIEW.complexity = function (L, inst, opts) {
    var D = coDecisions(L), n = 1 + D.pts.length, lo = opts.bands[0], hi = opts.bands[1];
    var band = n <= lo ? '0–' + lo : (n <= hi ? (lo + 1) + '–' + hi : hi + '+');
    var counts = CO_KINDS.map(function (k) { return [k, D.pts.filter(function (p) { return p.kind === k; }).length]; });
    var breakdown = '1' + counts.filter(function (c) { return c[1]; }).map(function (c) { return ' + ' + c[0] + ' ' + c[1]; }).join('');
    var base = L.header ? 1 : 0, depth = -1, where = null, H = L.header;
    coStatements(L).forEach(function (ln) {
      if (H && ln.no >= H.first && ln.no <= H.last) return;
      var dd = L.depth[ln.no].at - base;
      if (dd > depth) { depth = dd; where = ln.no; }
    });
    return {
      tiles: { coDecisions: ccInt(n), coBreakdown: breakdown, coBand: band,
        coDepth: where === null ? CC_DASH : ccInt(depth), coDeepest: where === null ? CC_DASH : 'line ' + where },
      status: ccPlural(n, 'decision point', 'decision points') + ': ' + breakdown + ', which falls in the band ' + band + '. '
        + 'The bands are McConnell\'s guidance on what to think about doing with a routine, not a grade.'
        + (lo === 5 && hi === 10 ? ' The book prints its bands as 0–5, 6–10 and 10+, so 10 sits in two of them; the lab puts 10 in 6–10.' : '')
        + ' Depth counts brace levels below the routine\'s own braces: a statement directly in the body is at depth 0, so the '
        + 'statements of a third nested if are at depth 3, and an unbraced body adds nothing (the layout view checks those).' + D.ternary,
      table: null
    };
  };
"""

# cfg "book": "other" (docs/enterprise-patterns/PLAN.md H.1). On a path whose
# "book" is not Code Complete, the complexity banner's two sentences about "the
# book" and the ?: note would name the wrong author. This block ships ONLY when
# a lesson sets book "other", after the complexity view's own block, and
# rewrites those three phrases of its banner; with the default it is not on the
# page, so every Code Complete page is byte-for-byte what it was.
CO_BOOK_OTHER_JS = r"""
  (function (plain) {
    CO_VIEW.complexity = function (L, inst, opts) {
      var out = plain(L, inst, opts);
      if (out.status) {
        out.status = out.status
          .replace('McConnell\'s guidance on what', 'McConnell\'s guidance in Code Complete on what')
          .replace('The book prints its bands', 'McConnell prints his bands')
          .replace('the kit\'s choice, not the book\'s.', 'the kit\'s choice, not McConnell\'s.');
      }
      return out;
    };
  })(CO_VIEW.complexity);
"""

CO_VIEW_JS["basis"] = r"""
  CO_VIEW.basis = function (L) {
    var D = coDecisions(L), n = 1 + D.pts.length + D.noDefault;
    return {
      tiles: { coBasis: ccInt(n), coNoDefault: ccInt(D.noDefault),
        coPoints: ccNames(D.pts.map(function (p) { return p.kind + ' line ' + p.line; })) },
      status: 'Structured basis testing needs ' + ccPlural(n, 'test case', 'test cases') + ': one for the straight path, one for each of the '
        + ccPlural(D.pts.length, 'decision point', 'decision points') + ' (if, while, for, case, && and ||), and one for each of the '
        + ccPlural(D.noDefault, 'switch', 'switches') + ' with no default.' + D.ternary,
      table: null
    };
  };
"""

CO_VIEW_JS["layout"] = r"""
  /* The depth the compiler's structure gives each line, against its leading
     spaces / indent. A line that continues a statement (inside parentheses,
     or after a line ending in an operator or a comma) and a comment-only line
     are not checked. */
  var CO_CONT = ccWords(', = + - * / % && || ? . ( [ += -= *= /= %= == != < > <= >= & | ^ ->');
  CO_VIEW.layout = function (L, inst, opts) {
    var w = opts.indent, logical = [], paren = 0, cont = false;
    L.lines.forEach(function (ln) {
      if (!ln.isCode) return;
      if (logical.length && (paren > 0 || cont)) logical[logical.length - 1].vals = logical[logical.length - 1].vals.concat(ln.vals);
      else logical.push({ no: ln.no, raw: ln.raw, vals: ln.vals.slice() });
      ln.vals.forEach(function (v) { if (v === '(' || v === '[') paren += 1; else if ((v === ')' || v === ']') && paren > 0) paren -= 1; });
      cont = CO_CONT[ln.vals[ln.vals.length - 1]] === true;
    });
    var frames = [], cands = [], bad = [], rows = [];
    function top() { return frames.length ? frames[frames.length - 1].depth : 0; }
    function brace(exp) { frames.push({ kind: 'brace', depth: exp + 1, opener: exp }); }
    function popBrace() {
      while (frames.length && frames[frames.length - 1].kind !== 'brace') frames.pop();
      var fr = frames.pop();
      return fr ? fr.opener : 0;
    }
    logical.forEach(function (ll) {
      var vals = ll.vals, lead = /^[ \t]*/.exec(ll.raw)[0].replace(/\t/g, new Array(w + 1).join(' ')).length;
      var my = cands, exp = null, rest = vals, last = vals[vals.length - 1];
      cands = [];
      function check(e) {
        var ok = lead === e * w;
        if (!ok) bad.push(ll.no);
        rows.push([String(ll.no), String(lead), String(e * w), ok ? 'yes' : { t: 'no', c: 'tone-amber' }]);
      }
      while (rest[0] === '}') { exp = popBrace(); rest = rest.slice(1); }
      if (rest[0] === 'else' && vals[0] !== '}') {
        if (my.length) { frames = my[0].below.slice(); exp = my[0].d; } else exp = top();
      }
      if (exp === null) {
        if (vals.length === 1 && vals[0] === '{' && frames.length && frames[frames.length - 1].kind === 'single') {
          exp = frames.pop().opener;
          check(exp);
          brace(exp);
          return;
        }
        if (vals[0] === 'case' || vals[0] === 'default') {
          if (frames.length && frames[frames.length - 1].kind === 'case') frames.pop();
          exp = top();
          check(exp);
          frames.push({ kind: 'case', depth: exp + 1, opener: exp });
          if (last === '{') brace(exp + 1);
          return;
        }
        exp = top();
      }
      check(exp);
      var opens = rest.filter(function (v) { return v === '{'; }).length, closes = rest.filter(function (v) { return v === '}'; }).length;
      var hdr = rest.length && (rest[0] === 'if' || rest[0] === 'for' || rest[0] === 'while' || rest[0] === 'else');
      if (last === '{' || opens > closes) {
        for (var k = closes; k < opens; k += 1) brace(exp);
      } else if (closes > opens) {
        for (var k2 = opens; k2 < closes; k2 += 1) popBrace();
      } else if (hdr && last !== ';' && last !== '}') {
        frames.push({ kind: 'single', depth: exp + 1, opener: exp, hdr: rest[0] === 'if' || (rest[0] === 'else' && rest[1] === 'if') });
      } else if (last === ';' || last === '}') {
        while (frames.length && frames[frames.length - 1].kind === 'single') {
          var fr = frames.pop();
          if (fr.hdr) cands.push({ d: fr.opener, below: frames.slice() });
        }
      }
    });
    var flags = {};
    bad.forEach(function (l) { ccFlag(flags, l, 'mis-indented'); });
    return {
      tiles: { coMisIndented: ccInt(bad.length), coLines: bad.length ? bad.join(', ') : 'none' },
      status: ccPlural(bad.length, 'line is', 'lines are') + ' indented other than the structure Java gives '
        + (bad.length === 1 ? 'it' : 'them') + ', at ' + w + ' spaces a level' + (bad.length ? ': ' + coLines(bad) + '.' : '.')
        + ' An unbraced if, else, for or while governs one statement, one level deeper; an else belongs to the nearest '
        + 'unmatched if, as Java binds it. Comment-only lines and the lines that continue a statement are not checked.',
      flags: flags,
      table: rows.length ? { caption: 'Each line checked: leading spaces against the structure', head: ['line', 'spaces', 'expected', 'agrees'], rows: rows } : null
    };
  };
"""

# The rules stated under every code listing (D.1, "the subset the kit reads").
_SUBSET = (
    "<ul>"
    "<li>Comments run from <code>//</code> to the end of the line, or from <code>/*</code> to <code>*/</code>; "
    "string and character literals are read as single tokens. The lab reads Java; it never runs it.</li>"
    "<li>A line is blank, a comment line (it carries a comment, alone or after code) and/or a code line (it has "
    "code outside comments). A statement line is a code line that is not only braces and semicolons.</li>"
    "<li>The routine is the first statement at brace depth 0 that ends in <code>{</code> and has the shape "
    "<em>type name(parameters)</em>. Without one the listing is a fragment.</li>"
    "<li>A variable is a name that begins with a lower-case letter or <code>_</code>, is not a keyword, is not "
    "followed by <code>(</code> and does not follow a dot. Capitalised names are types or constants.</li>"
    "<li>A declaration (a type, then a name and <code>=</code>, <code>;</code>, <code>,</code> or <code>:</code>) "
    "sets the name when it has a value and only declares it otherwise; parameters are set on the header's line. "
    "<code>name op expr</code> with <code>op</code> one of <code>= += -= *= /= %=</code> reads the expression (and "
    "the name too, unless <code>op</code> is <code>=</code>) and then sets the name; <code>x++</code> reads and then "
    "sets <code>x</code>. Setting an element or a field only reads the names in it. A <code>for</code> header is read "
    "as its three parts in order.</li>"
    "<li>The lab reads the lines top to bottom and does not follow branches or loops.</li>"
    "</ul>"
)

_RULE = {
    "size": "This view counts lines: code, statement, comment and blank lines, the routine's parameters, and comment "
            "lines over statement lines.",
    "class": "This view reads one class: a field is a member statement at brace depth 1 ending in <code>;</code> whose "
             "first <code>(</code>, if any, comes after its <code>=</code>; a routine has <code>(</code> before any "
             "<code>=</code>. A public field that is not <code>final</code> is counted as public.",
    "dupes": "This view compares statement lines as text, white space collapsed. A repeated block is a run of at least "
             "the lesson's minimum of consecutive statement lines that occurs again, not overlapping, and as long as it "
             "can be made at its start.",
    "extract": "In: names whose first event inside the block is a read and that were set or declared before it. Out: "
               "names set inside the block and read after it. Outside: names read but set or declared nowhere.",
    "ppp": "The steps are the comment-only lines inside the routine's body; each step's code is the statement lines "
           "before the next step or the end of the body. A step with none is empty.",
    "dataflow": "Used before set: a read with no earlier set (once per name). Set twice: a set followed by another set "
                "with no read between. Set, never used: the name's last event is a set. A dependency i&rarr;j: line j "
                "reads a name whose latest earlier set is on line i.",
    "span": "A name's references are the lines it appears on; a span is the number of lines strictly between two "
            "consecutive references; its live time is the last reference's line minus the first's, plus one.",
    "names": "Declared names are the parameters, the declarations and the enhanced-<code>for</code> variables, in order; "
             "a loop index (declared in a <code>for</code> header) is listed and not counted.",
    "literals": "Numeric literals on code lines count, except 0 and 1 and except on a line that contains "
                "<code>final</code>.",
    "complexity": "Decision points: 1, plus one for each <code>if</code>, <code>while</code>, <code>for</code>, "
                  "<code>case</code>, <code>&amp;&amp;</code> and <code>||</code>; <code>else</code>, "
                  "<code>default</code>, <code>do</code>, <code>?:</code>, <code>try</code> and <code>catch</code> add "
                  "nothing. Depth is brace depth below the routine's own braces.",
    "basis": "Basis cases: the decision points, plus one for each <code>switch</code> with no <code>default</code>.",
    "layout": "Each line's expected depth: its braces, plus one for the single statement after an unbraced "
              "<code>if</code>, <code>else</code>, <code>for</code> or <code>while</code>; an <code>else</code> takes "
              "the depth of the <code>if</code> Java binds it to; a <code>case</code> label at the switch block's "
              "depth and its statements one deeper. Expected spaces are the depth times the lesson's indent; a tab "
              "counts as that many spaces.",
}

_CODE = ({"kind": "code", "what": "Java listing (the lab reads it; it never runs it)"}, None)
_LINE = {"kind": "count", "max": "200"}

# view: (fields, tiles, needs a routine, order-dependent)
CODE_VIEWS = {
    "size": ([("code",) + _CODE],
             [("Lines", "coLines"), ("Code lines (braces included)", "coCode"), ("Statement lines", "coStatements"),
              ("Comment lines", "coComment"), ("Blank lines", "coBlank"), ("Parameters", "coParams"),
              ("Comment lines per statement line", "coDensity")]),
    "class": ([("code",) + _CODE],
              [("Fields", "coFields"), ("Public fields (not final)", "coPublicFields"), ("Routines", "coRoutines"),
               ("Public routines", "coPublicRoutines")]),
    "dupes": ([("code",) + _CODE],
              [("Repeated blocks", "coDupBlocks"), ("Lines in all the copies", "coDupLines"), ("Where", "coDupWhere")]),
    "extract": ([("code",) + _CODE, ("from", dict(_LINE, what="Block from line"), None),
                 ("to", dict(_LINE, what="Block to line"), None)],
                [("In", "coIn"), ("Out", "coOut"), ("Parameters the routine needs", "coParams"),
                 ("Read but set nowhere", "coOutside")]),
    "ppp": ([("code",) + _CODE],
            [("Pseudocode steps", "coSteps"), ("Statement lines in the body", "coCode"), ("Empty steps", "coEmpty"),
             ("Most code under one step", "coMaxUnder")]),
    "dataflow": ([("code",) + _CODE],
                 [("Anomalies", "coAnomalies"), ("Used before set", "coUsedBeforeSet"), ("Set twice", "coSetTwice"),
                  ("Set, never used", "coUnused"), ("Dependencies (line → line)", "coDeps")]),
    "span": ([("code",) + _CODE,
              ("vars", {"kind": "idents", "hi": 12, "what": "Variables (space-separated; empty for every one set)"}, "")],
             [("Average span (lines)", "coAvgSpan"), ("Average live time (lines)", "coAvgLive"),
              ("Longest live time", "coLongest")]),
    "names": ([("code",) + _CODE],
              [("Declared names", "coNames"), ("Mean length of the counted names", "coAvgLen"),
               ("Shorter than the lesson's minimum", "coShort")]),
    "literals": ([("code",) + _CODE],
                 [("Magic numbers", "coMagic"), ("Distinct", "coDistinct"), ("Each, with its lines", "coMagicList")]),
    "complexity": ([("code",) + _CODE],
                   [("Decision points", "coDecisions"), ("Breakdown", "coBreakdown"), ("Band", "coBand"),
                    ("Deepest nesting", "coDepth"), ("First line at that depth", "coDeepest")]),
    "basis": ([("code",) + _CODE],
              [("Basis test cases", "coBasis"), ("switch with no default", "coNoDefault"),
               ("Decision points, in line order", "coPoints")]),
    "layout": ([("code",) + _CODE],
               [("Mis-indented lines", "coMisIndented"), ("Which", "coLines")]),
}
CODE_VIEW_ORDER = tuple(CODE_VIEWS)

_SUBTITLES = {
    "size": "lines, statements, comments and parameters",
    "class": "fields and routines, and how many are public",
    "dupes": "repeated runs of statements, matched as text",
    "extract": "what a block would take in and hand out",
    "ppp": "pseudocode steps, and the code under each",
    "dataflow": "each name's sets and reads, line by line",
    "span": "lines between references, and live time",
    "names": "declared names and their lengths",
    "literals": "numbers written into the code",
    "complexity": "decision points and nesting depth",
    "basis": "the test cases structured basis testing needs",
    "layout": "indentation against the structure Java reads",
}


def _code_options(cfg, kit, view):
    """The lesson-level cfg values a code view takes, validated."""
    fixed, keys = {}, []
    if view == "dupes":
        n = cfg.get("min_run", 2)
        if isinstance(n, bool) or not isinstance(n, int) or not 2 <= n <= 10:
            raise ValueError("%s: cfg['min_run'] is %r; it is a whole number from 2 to 10" % (kit, n))
        fixed["min_run"], keys = n, ["min_run"]
    if view == "names":
        n = cfg.get("min", 8)
        if isinstance(n, bool) or not isinstance(n, int) or not 1 <= n <= 40:
            raise ValueError("%s: cfg['min'] is %r; it is a whole number from 1 to 40" % (kit, n))
        fixed["min"], keys = n, ["min"]
    if view == "complexity":
        b = cfg.get("bands", [5, 10])
        if (not isinstance(b, (list, tuple)) or len(b) != 2 or any(isinstance(x, bool) or not isinstance(x, int) for x in b)
                or not 0 < b[0] < b[1]):
            raise ValueError("%s: cfg['bands'] is %r; it is two whole numbers 0 < a < b" % (kit, b))
        fixed["bands"], keys = list(b), ["bands", "book"]
        if cfg.get("book", "code-complete") not in ("code-complete", "other"):
            raise ValueError("%s: cfg['book'] is %r; it is \"code-complete\" (the default) or \"other\"" % (kit, cfg.get("book")))
    if view == "layout":
        n = cfg.get("indent", 4)
        if isinstance(n, bool) or not isinstance(n, int) or not 1 <= n <= 8:
            raise ValueError("%s: cfg['indent'] is %r; it is a whole number from 1 to 8" % (kit, n))
        fixed["indent"], keys = n, ["indent"]
    return fixed, keys


def _check_code_presets(kit, view, fields, cfg):
    """D.3: every preset's listing is read by the Python mirror of the
    tokenizer; a view that needs a routine refuses a listing without one, and
    a line range must lie inside the listing."""
    spec = fields[0][1]
    for p in cfg["presets"]:
        where = "%s preset %r" % (kit, p.get("id"))
        text = cc.to_text(where, spec, p.get("code", cfg.get("code")))
        lexed = cc.lex(where, cc.split_lines(text))
        if view == "ppp" and cc.header(lexed) is None:
            raise ValueError("%s: the listing has no routine header, which the ppp view needs" % where)
        if view == "extract":
            n = len(lexed)
            a, b = (int(cc.rparse(str(p.get(k, cfg.get(k))))) for k in ("from", "to"))
            if not 1 <= a <= b <= n:
                raise ValueError("%s: lines %d-%d are not a range inside the %d-line listing" % (where, a, b, n))
        if view == "span":
            names = p.get("vars", cfg.get("vars", ""))
            names = names.split() if isinstance(names, str) else list(names)
            words = {t for _no, toks in lexed for _k, t in toks}
            missing = [v for v in names if v not in words]
            if missing:
                raise ValueError("%s: vars names %s, which the listing does not contain" % (where, ", ".join(missing)))


def _code_lab(cfg, view):
    kit = "%s/code/%s" % (KIT, view)
    fields, tiles = CODE_VIEWS[view]
    fixed, keys = _code_options(cfg, kit, view)
    lab = cc.build_lab(cfg, kit=kit, prefix="co", view=view, fields=fields, tiles=tiles, fn="coCompute",
                       js=CO_JS + (CO_DECIDE_JS if view in ("complexity", "basis") else "") + CO_VIEW_JS[view]
                       + (CO_BOOK_OTHER_JS if view == "complexity" and cfg.get("book") == "other" else ""),
                       fixed=fixed, title="Reading the code", subtitle=_SUBTITLES[view], family=1,
                       intro=cc.FAMILY[1] + " The lab reads the listing; it never runs it, and no count is a verdict.",
                       extra_keys=keys, rules=_SUBSET + "<p>" + _RULE[view] + "</p>", listing_key="code")
    _check_code_presets(kit, view, fields, cfg)
    return lab


def cckit_lab(cfg):
    """The Code Complete kit. `cfg["mode"]` chooses the mode, `cfg["view"]` the view; an unknown one raises."""
    cfg = cfg or {}
    mode = cfg.get("mode")
    if mode == "code":
        view = cfg.get("view", CODE_VIEW_ORDER[0])
        if view not in CODE_VIEWS:
            raise ValueError("cckit/code: unknown view %r; the views are %s" % (view, ", ".join(CODE_VIEW_ORDER)))
        return _code_lab(cfg, view)
    from . import cckit_b
    if mode not in cckit_b.MODES:
        raise ValueError("cckit_lab: unknown mode %r; the eight modes are code, %s" % (mode, ", ".join(cckit_b.MODES)))
    return cckit_b.mode_lab(cfg, mode)


__all__ = ["cckit_lab", "CODE_VIEWS"]
