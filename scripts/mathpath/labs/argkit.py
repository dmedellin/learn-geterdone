"""argkit -- the Philosophy kit for the structure of a position. Eight modes.

Specified in docs/philosophy/PLAN.md section D.1; the conventions in D.0 bind
every mode. Each mode computes a verdict FROM the lesson's stated premises,
cases or equations, in the browser, and the reader can change those inputs and
watch the verdict move.

  validity     every row of the premises and the conclusion; the
               counterexample rows; the form, found by unification against a
               catalogue of named patterns
  consistency  the models of a set of sentences and every minimal
               inconsistent subset
  syllogism    categorical statements as constraints on Venn regions; validity
               by enumerating every pattern of empty and non-empty regions,
               under the Boolean or the Aristotelian reading
  sorites      a chain of tolerance conditionals under four treatments of
               vagueness, in exact rationals for the degree treatment
  kripke       possible worlds: a modal formula at every world, the five frame
               properties and which of D, T, B, 4 and 5 the frame validates
  semantics    a finite first-order model, with witnesses and Russell's
               descriptions
  analysis     a definition against a case table, and the one- and two-literal
               formulas that would fit every case
  structural   Boolean structural equations: but-for, Halpern-Pearl (modified)
               with the smallest witness set, and joint causes

PRESETS ARE LESSON DATA. Every mode takes `cfg["presets"]` (each with an `id`,
a `label` naming the instance, the instance fields and `expect`) and
`cfg["preset"]`. The kit writes the instances into a JS table and returns
`Lab(expect={"XXPreset": {id: expect}})`; scripts/labcheck.js selects each
option on the built page and compares the tiles. A preset's change handler
rewrites the instance inputs only; a redraw-only select keeps its value.

WHAT A TEXT BOX SHIPS. A control's starting value is read by labcheck.js out
of the markup without decoding entities, so a shipped value may contain none
of `> < & "`. Formulas are therefore shipped in their glyph spelling (`->`
becomes the arrow, `&` the wedge, `~` the hook, `[]` the box); every parser
here reads both spellings, so a reader may type either.

ONE PARSER FOR THE PROPOSITIONAL MODES, NOT logic.PARSER_JS. D.0 names
logic.PARSER_JS, whose variables are single letters. Several of the instances
section C specifies have multi-letter atoms (`op`, `opq`, `ca`, `ia`) and the
structural equations have named variables (`S1`, `BH`, `shattered`), so argkit
ships its own parser with the same operators and the same precedence -- not,
and, or/xor, then the right-associative conditional, then the biconditional --
over identifiers, with the box and diamond switched on for `kripke` only.
"""

import re

from .algebra_core import RATIONAL_JS
from .common import Lab, cfg_literal

# ---------------------------------------------------------------------------
# Shared JavaScript. Every function in these blocks is module-level and named,
# and none touches the DOM except the furniture helpers in AK_UI_JS.
# ---------------------------------------------------------------------------

AK_UI_JS = r"""
  /* ---- argkit: page furniture ------------------------------------------- */
  function akEl(id) { return document.getElementById(id); }
  function akSet(id, text) { akEl(id).textContent = String(text); }
  function akEsc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }
  /* Trimmed, non-empty pieces of a typed list. */
  function akPieces(text, sep) {
    var out = [], parts = String(text).split(sep), i;
    for (i = 0; i < parts.length; i += 1) {
      var t = parts[i].replace(/^\s+|\s+$/g, '');
      if (t.length) out.push(t);
    }
    return out;
  }
  /* A refusal: every tile to the em dash, the stage cleared, the banner red
     and specific. Called from a parse step's catch, never from a render. */
  function akRefuse(statusId, tiles, stages, why) {
    var i;
    for (i = 0; i < tiles.length; i += 1) akSet(tiles[i], '—');
    for (i = 0; i < stages.length; i += 1) akEl(stages[i]).innerHTML = '';
    akEl(statusId).innerHTML = '<span class="tone-red"><strong>Refused.</strong> '
      + akEsc(why) + '</span>';
  }
  function akMsg(e) { return e && e.message ? e.message : String(e); }
  function akCell(v) { return '<td class="' + (v ? 't' : 'f') + '">' + (v ? 'T' : 'F') + '</td>'; }
  /* Rebuild a select's options and keep its value when it survives. */
  function akOptions(sel, pairs, keep) {
    var h = '', ok = false, i;
    for (i = 0; i < pairs.length; i += 1) {
      h += '<option value="' + akEsc(pairs[i][0]) + '">' + akEsc(pairs[i][1]) + '</option>';
      if (String(pairs[i][0]) === String(keep)) ok = true;
    }
    sel.innerHTML = h;
    sel.value = ok ? String(keep) : (pairs.length ? String(pairs[0][0]) : '');
  }
"""

AK_PROP_JS = r"""
  /* ---- argkit: propositional formulas (and the box and diamond) ----------

     Precedence, tightest first: not (and the box and diamond), and, or/xor,
     the conditional (right-associative), the biconditional. Atoms are
     identifiers: a letter, then letters, digits or subscript digits. */
  var AK_OPS = {
    '¬': 'not', '~': 'not', '!': 'not', '∧': 'and', '&': 'and', '∨': 'or', '|': 'or',
    '⊕': 'xor', '^': 'xor', '→': 'imp', '⇒': 'imp', '↔': 'iff', '⇔': 'iff',
    '□': 'box', '◇': 'dia'
  };
  var AK_GLYPH = { not: '¬', and: '∧', or: '∨', xor: '⊕', imp: '→', iff: '↔', box: '□', dia: '◇' };
  function akTokenize(src, modal) {
    var out = [], s = String(src), i = 0, m;
    while (i < s.length) {
      var ch = s.charAt(i);
      if (/\s/.test(ch)) { i += 1; continue; }
      if (s.substr(i, 3) === '<->') { out.push({ t: 'op', v: 'iff' }); i += 3; continue; }
      if (s.substr(i, 2) === '->') { out.push({ t: 'op', v: 'imp' }); i += 2; continue; }
      if (s.substr(i, 2) === '[]' || s.substr(i, 2) === '<>') {
        if (!modal) throw new Error('“' + s.substr(i, 2) + '” is a modal operator, and this lab has no worlds');
        out.push({ t: 'op', v: s.substr(i, 2) === '[]' ? 'box' : 'dia' }); i += 2; continue;
      }
      if (ch === '(' || ch === ')') { out.push({ t: ch }); i += 1; continue; }
      if (AK_OPS.hasOwnProperty(ch)) {
        var v = AK_OPS[ch];
        if ((v === 'box' || v === 'dia') && !modal) throw new Error('“' + ch + '” is a modal operator, and this lab has no worlds');
        out.push({ t: 'op', v: v }); i += 1; continue;
      }
      if (ch === '⊤' || ch === '⊥') { out.push({ t: 'const', v: ch === '⊤' }); i += 1; continue; }
      m = /^[A-Za-z][A-Za-z0-9_₀-₉]*/.exec(s.slice(i));
      if (m) { out.push({ t: 'var', v: m[0] }); i += m[0].length; continue; }
      throw new Error('“' + ch + '” is not part of the formula language');
    }
    return out;
  }
  function akTokText(t) {
    if (t.t === 'op') return AK_GLYPH[t.v];
    if (t.t === 'var') return t.v;
    if (t.t === 'const') return t.v ? '⊤' : '⊥';
    return t.t;
  }
  function akParse(src, modal) {
    var ts = akTokenize(src, modal), pos = 0;
    if (!ts.length) throw new Error('there is no formula here');
    function primary() {
      var t = ts[pos];
      if (!t) throw new Error('the formula stops where a sentence letter was expected');
      if (t.t === '(') {
        pos += 1;
        var inner = iff();
        if (!ts[pos] || ts[pos].t !== ')') throw new Error('a “(” is never closed');
        pos += 1;
        return inner;
      }
      if (t.t === 'op' && (t.v === 'not' || t.v === 'box' || t.v === 'dia')) {
        pos += 1;
        return { op: t.v, a: primary() };
      }
      if (t.t === 'const') { pos += 1; return { op: 'const', v: t.v }; }
      if (t.t === 'var') { pos += 1; return { op: 'var', name: t.v }; }
      throw new Error('“' + akTokText(t) + '” cannot start a formula');
    }
    function chain(next, names) {
      var node = next();
      while (ts[pos] && ts[pos].t === 'op' && names.indexOf(ts[pos].v) !== -1) {
        var v = ts[pos].v;
        pos += 1;
        node = { op: v, a: node, b: next() };
      }
      return node;
    }
    function conj() { return chain(primary, ['and']); }
    function disj() { return chain(conj, ['or', 'xor']); }
    function cond() {
      var l = disj();
      if (ts[pos] && ts[pos].t === 'op' && ts[pos].v === 'imp') { pos += 1; return { op: 'imp', a: l, b: cond() }; }
      return l;
    }
    function iff() { return chain(cond, ['iff']); }
    var tree = iff();
    if (pos !== ts.length) throw new Error('there is more after a complete formula, starting at “' + akTokText(ts[pos]) + '”');
    return tree;
  }
  function akEval(node, env) {
    switch (node.op) {
      case 'var': return !!env[node.name];
      case 'const': return node.v;
      case 'not': return !akEval(node.a, env);
      case 'and': return akEval(node.a, env) && akEval(node.b, env);
      case 'or': return akEval(node.a, env) || akEval(node.b, env);
      case 'xor': return akEval(node.a, env) !== akEval(node.b, env);
      case 'imp': return !akEval(node.a, env) || akEval(node.b, env);
      case 'iff': return akEval(node.a, env) === akEval(node.b, env);
    }
    return false;
  }
  function akShow(node, outer) {
    if (node.op === 'var') return node.name;
    if (node.op === 'const') return node.v ? '⊤' : '⊥';
    if (node.op === 'not' || node.op === 'box' || node.op === 'dia') return AK_GLYPH[node.op] + akShow(node.a, false);
    var s = akShow(node.a, false) + ' ' + AK_GLYPH[node.op] + ' ' + akShow(node.b, false);
    return outer ? s : '(' + s + ')';
  }
  function akAtoms(node, seen) {
    seen = seen || [];
    if (node.op === 'var') { if (seen.indexOf(node.name) === -1) seen.push(node.name); }
    else { if (node.a) akAtoms(node.a, seen); if (node.b) akAtoms(node.b, seen); }
    return seen;
  }
  function akSame(a, b) {
    if (a.op !== b.op) return false;
    if (a.op === 'var') return a.name === b.name;
    if (a.op === 'const') return a.v === b.v;
    if (!akSame(a.a, b.a)) return false;
    return a.b ? akSame(a.b, b.b) : true;
  }
  /* Rows in the conventional order: T before F, the first variable slowest. */
  function akRows(vars) {
    var rows = [], total = 1 << vars.length, i, j;
    for (i = 0; i < total; i += 1) {
      var env = {};
      for (j = 0; j < vars.length; j += 1) env[vars[j]] = ((i >> (vars.length - 1 - j)) & 1) === 0;
      rows.push(env);
    }
    return rows;
  }
  function akEnvText(vars, env) {
    var out = [], i;
    for (i = 0; i < vars.length; i += 1) out.push(vars[i] + '=' + (env[vars[i]] ? 'T' : 'F'));
    return out.join(' ');
  }
"""

# ---------------------------------------------------------------------------
# validity
# ---------------------------------------------------------------------------

VALIDITY_JS = r"""
  /* ---- validity: the rows, the counterexamples, the form ---------------- */
  function vaRead(premText, concText) {
    var pieces = akPieces(premText, ';'), premises = [], i;
    if (pieces.length > 6) throw new Error('this lab takes at most 6 premises, and ' + pieces.length + ' were typed');
    for (i = 0; i < pieces.length; i += 1) {
      try { premises.push(akParse(pieces[i], false)); }
      catch (e) { throw new Error('premise ' + (i + 1) + ': ' + akMsg(e)); }
    }
    if (!String(concText).replace(/\s+/g, '').length) throw new Error('the conclusion is empty; an argument needs one');
    var conclusion;
    try { conclusion = akParse(concText, false); }
    catch (e2) { throw new Error('the conclusion: ' + akMsg(e2)); }
    var seen = [];
    for (i = 0; i < premises.length; i += 1) akAtoms(premises[i], seen);
    akAtoms(conclusion, seen);
    if (seen.length > 6) throw new Error('this lab takes at most 6 sentence letters, and the argument has ' + seen.length);
    return { premises: premises, conclusion: conclusion, vars: seen.slice().sort() };
  }
  function vaAnalyse(premises, conclusion, vars) {
    var rows = akRows(vars), out = [], counter = 0, premSat = 0, concTrue = 0, first = null, i, j;
    for (i = 0; i < rows.length; i += 1) {
      var env = rows[i], pv = [], all = true;
      for (j = 0; j < premises.length; j += 1) { pv.push(akEval(premises[j], env)); if (!pv[j]) all = false; }
      var c = akEval(conclusion, env), isCounter = all && !c;
      if (all) premSat += 1;
      if (c) concTrue += 1;
      if (isCounter) { counter += 1; if (!first) first = env; }
      out.push({ env: env, pv: pv, c: c, counter: isCounter });
    }
    return { rows: out, counter: counter, premSat: premSat, concTaut: concTrue === rows.length,
             valid: counter === 0, first: first };
  }
  /* The catalogue. A metavariable binds any subformula, the same one each
     time it recurs; NEG(X) is the contradictory of X -- the negation of X,
     or, when X is itself a negation, the formula it negates -- so a -> ¬n
     with n is as much modus tollens as p -> q with ¬q. Valid forms first. */
  function vaM(n) { return { op: 'meta', name: n }; }
  function vaN(x) { return { op: 'neg', a: x }; }
  function vaP(op, a, b) { return { op: op, a: a, b: b }; }
  var VA_A = vaM('A'), VA_B = vaM('B'), VA_C = vaM('C'), VA_D = vaM('D');
  var VA_FORMS = [
    ['modus ponens', [vaP('imp', VA_A, VA_B), VA_A], VA_B],
    ['modus tollens', [vaP('imp', VA_A, VA_B), vaN(VA_B)], vaN(VA_A)],
    ['hypothetical syllogism', [vaP('imp', VA_A, VA_B), vaP('imp', VA_B, VA_C)], vaP('imp', VA_A, VA_C)],
    ['disjunctive syllogism', [vaP('or', VA_A, VA_B), vaN(VA_A)], VA_B],
    ['disjunctive syllogism', [vaP('or', VA_A, VA_B), vaN(VA_B)], VA_A],
    ['constructive dilemma', [vaP('imp', VA_A, VA_C), vaP('imp', VA_B, VA_D), vaP('or', VA_A, VA_B)], vaP('or', VA_C, VA_D)],
    ['simplification', [vaP('and', VA_A, VA_B)], VA_A],
    ['simplification', [vaP('and', VA_A, VA_B)], VA_B],
    ['conjunction', [VA_A, VA_B], vaP('and', VA_A, VA_B)],
    ['addition', [VA_A], vaP('or', VA_A, VA_B)],
    ['addition', [VA_A], vaP('or', VA_B, VA_A)],
    ['contraposition', [vaP('imp', VA_A, VA_B)], vaP('imp', vaN(VA_B), vaN(VA_A))],
    ['affirming the consequent', [vaP('imp', VA_A, VA_B), VA_B], VA_A],
    ['denying the antecedent', [vaP('imp', VA_A, VA_B), vaN(VA_A)], vaN(VA_B)],
    ['affirming a disjunct', [vaP('or', VA_A, VA_B), VA_A], vaN(VA_B)],
    ['affirming a disjunct', [vaP('or', VA_A, VA_B), VA_B], vaN(VA_A)],
    ['converse', [vaP('imp', VA_A, VA_B)], vaP('imp', VA_B, VA_A)]
  ];
  function vaCopy(b) { var c = {}, k; for (k in b) if (b.hasOwnProperty(k)) c[k] = b[k]; return c; }
  /* Every binding under which pattern PAT matches formula NODE. */
  function vaMatch(pat, node, b) {
    var out = [], i;
    if (pat.op === 'meta') {
      if (b.hasOwnProperty(pat.name)) return akSame(b[pat.name], node) ? [b] : [];
      var c = vaCopy(b); c[pat.name] = node; return [c];
    }
    if (pat.op === 'neg') {
      if (node.op === 'not') out = out.concat(vaMatch(pat.a, node.a, b));
      if (pat.a.op === 'meta' && b.hasOwnProperty(pat.a.name) && b[pat.a.name].op === 'not'
          && akSame(b[pat.a.name].a, node)) out.push(b);
      return out;
    }
    if (pat.op !== node.op) return [];
    var left = vaMatch(pat.a, node.a, b);
    if (!pat.b) return left;
    for (i = 0; i < left.length; i += 1) out = out.concat(vaMatch(pat.b, node.b, left[i]));
    return out;
  }
  function vaPerms(n) {
    if (n === 0) return [[]];
    var out = [], rest = vaPerms(n - 1), i, j;
    for (i = 0; i < rest.length; i += 1) {
      for (j = 0; j <= rest[i].length; j += 1) {
        var p = rest[i].slice(); p.splice(j, 0, n - 1); out.push(p);
      }
    }
    return out;
  }
  /* The catalogue name of the argument's form, or null. Premises are matched
     as a set: every ordering is tried, and the count must agree exactly. */
  function vaFormName(premises, conclusion) {
    var f, p, k;
    for (f = 0; f < VA_FORMS.length; f += 1) {
      var form = VA_FORMS[f];
      if (form[1].length !== premises.length) continue;
      var perms = vaPerms(premises.length);
      for (p = 0; p < perms.length; p += 1) {
        var states = [{}];
        for (k = 0; k < form[1].length && states.length; k += 1) {
          var next = [], s;
          for (s = 0; s < states.length; s += 1) next = next.concat(vaMatch(form[1][k], premises[perms[p][k]], states[s]));
          states = next;
        }
        for (k = 0; k < states.length; k += 1) {
          if (vaMatch(form[2], conclusion, states[k]).length) return form[0];
        }
      }
    }
    return null;
  }
"""

# ---------------------------------------------------------------------------
# consistency
# ---------------------------------------------------------------------------

CONSISTENCY_JS = r"""
  /* ---- consistency: models and minimal inconsistent subsets ------------- */
  function coRead(text) {
    var pieces = akPieces(text, ';'), trees = [], i;
    if (!pieces.length) throw new Error('there are no sentences here; separate them with semicolons');
    if (pieces.length > 8) throw new Error('this lab takes at most 8 sentences, and ' + pieces.length + ' were typed');
    for (i = 0; i < pieces.length; i += 1) {
      try { trees.push(akParse(pieces[i], false)); }
      catch (e) { throw new Error('sentence ' + (i + 1) + ': ' + akMsg(e)); }
    }
    var seen = [];
    for (i = 0; i < trees.length; i += 1) akAtoms(trees[i], seen);
    if (seen.length > 6) throw new Error('this lab takes at most 6 sentence letters, and the set has ' + seen.length);
    return { trees: trees, vars: seen.slice().sort() };
  }
  function coLexLess(a, b) {
    var i;
    for (i = 0; i < a.length && i < b.length; i += 1) if (a[i] !== b[i]) return a[i] < b[i];
    return a.length < b.length;
  }
  /* kept: the 0-based indices still in the set. The variables range over
     every typed sentence, so giving one up does not change the rows. */
  function coAnalyse(trees, vars, kept) {
    var rows = akRows(vars), sat = [], models = [], i, j;
    var keptMask = 0;
    for (i = 0; i < kept.length; i += 1) keptMask |= (1 << kept[i]);
    for (i = 0; i < rows.length; i += 1) {
      var m = 0;
      for (j = 0; j < trees.length; j += 1) if (akEval(trees[j], rows[i])) m |= (1 << j);
      sat.push(m);
      if ((m & keptMask) === keptMask) models.push(rows[i]);
    }
    /* subsets of the kept sentences, smallest first, then lexicographic */
    var subsets = [], s;
    for (s = 1; s < (1 << kept.length); s += 1) {
      var idx = [], mask = 0;
      for (j = 0; j < kept.length; j += 1) if (s & (1 << j)) { idx.push(kept[j]); mask |= (1 << kept[j]); }
      subsets.push({ idx: idx, mask: mask });
    }
    subsets.sort(function (a, b) {
      if (a.idx.length !== b.idx.length) return a.idx.length - b.idx.length;
      return coLexLess(a.idx, b.idx) ? -1 : (coLexLess(b.idx, a.idx) ? 1 : 0);
    });
    /* A subset is inconsistent iff no row satisfies all of it, and minimal
       iff no smaller inconsistent subset (all found already) lies inside it. */
    var mis = [];
    for (i = 0; i < subsets.length; i += 1) {
      var sub = subsets[i], minimal = true, satisfiable = false;
      for (j = 0; j < mis.length; j += 1) if ((mis[j].mask & sub.mask) === mis[j].mask) { minimal = false; break; }
      if (!minimal) continue;
      for (j = 0; j < sat.length; j += 1) if ((sat[j] & sub.mask) === sub.mask) { satisfiable = true; break; }
      if (!satisfiable) mis.push(sub);
    }
    return { rows: rows.length, models: models, mis: mis, sat: sat };
  }
  function coSetText(idx) {
    var out = [], i;
    for (i = 0; i < idx.length; i += 1) out.push(idx[i] + 1);
    return '{' + out.join(', ') + '}';
  }
"""

# ---------------------------------------------------------------------------
# syllogism
# ---------------------------------------------------------------------------

SYLLOGISM_JS = r"""
  /* ---- syllogism: statements as region constraints ---------------------- */
  function syTerm(word) {
    if (/^non-./.test(word)) return { term: word.slice(4), neg: true };
    return { term: word, neg: false };
  }
  function syStatement(text) {
    var s = String(text).toLowerCase().replace(/\s+/g, ' ').replace(/^ | $/g, '').replace(/\.$/, '');
    var m = /^(all|no|some) ([a-z][a-z-]*) are (not )?([a-z][a-z-]*)$/.exec(s);
    if (!m) throw new Error('“' + text + '” is not one of All X are Y, No X are Y, Some X are Y, Some X are not Y');
    if (m[3] && m[1] !== 'some') throw new Error('“' + text + '”: write “No X are Y” or “Some X are not Y”');
    var type = m[1] === 'all' ? 'A' : (m[1] === 'no' ? 'E' : (m[3] ? 'O' : 'I'));
    var subj = syTerm(m[2]), pred = syTerm(m[4]);
    if (/-$/.test(subj.term) || /-$/.test(pred.term)) throw new Error('“' + text + '”: a term cannot end in a hyphen');
    return { type: type, s: subj, p: pred, text: text };
  }
  /* Terms in the order: the conclusion's subject, its predicate, the rest. */
  function syRead(p1, p2, c) {
    var prem = [], i;
    if (!String(p1).replace(/\s+/g, '').length) throw new Error('the first premise is empty');
    prem.push(syStatement(p1));
    if (String(p2).replace(/\s+/g, '').length) prem.push(syStatement(p2));
    if (!String(c).replace(/\s+/g, '').length) throw new Error('the conclusion is empty');
    var conc = syStatement(c), terms = [conc.s.term];
    function add(t) { if (terms.indexOf(t) === -1) terms.push(t); }
    add(conc.p.term);
    for (i = 0; i < prem.length; i += 1) { add(prem[i].s.term); add(prem[i].p.term); }
    if (terms.length > 3) throw new Error('this lab takes at most 3 terms, and these statements use ' + terms.length + ': ' + terms.join(', '));
    return { prem: prem, conc: conc, terms: terms };
  }
  /* Region r lies inside term k iff bit (t-1-k) of r is set; regions are
     listed from r = 2^t - 1 (inside every circle) down to 0 (outside all). */
  function syIn(r, k, t) { return ((r >> (t - 1 - k)) & 1) === 1; }
  function syLit(r, lit, terms) { return syIn(r, terms.indexOf(lit.term), terms.length) !== lit.neg; }
  /* A empties X-and-not-Y, E empties X-and-Y, I needs an occupied region in
     X-and-Y, O one in X-and-not-Y. A pattern is a bitmask of occupied regions. */
  function syHolds(st, pattern, terms) {
    var n = 1 << terms.length, r, any = false;
    for (r = 0; r < n; r += 1) {
      if (!((pattern >> r) & 1)) continue;
      var s = syLit(r, st.s, terms), p = syLit(r, st.p, terms);
      if (st.type === 'A' && s && !p) return false;
      if (st.type === 'E' && s && p) return false;
      if (st.type === 'I' && s && p) any = true;
      if (st.type === 'O' && s && !p) any = true;
    }
    return (st.type === 'A' || st.type === 'E') ? true : any;
  }
  /* Aristotelian existential import: every term's circle is occupied. */
  function syImported(pattern, terms) {
    var n = 1 << terms.length, k, r;
    for (k = 0; k < terms.length; k += 1) {
      var found = false;
      for (r = 0; r < n; r += 1) if (((pattern >> r) & 1) && syIn(r, k, terms.length)) { found = true; break; }
      if (!found) return false;
    }
    return true;
  }
  function syRegions(pattern, t) {
    var out = [], r;
    for (r = (1 << t) - 1; r >= 0; r -= 1) if ((pattern >> r) & 1) out.push(r);
    return out;
  }
  /* fewest occupied regions first, then lexicographic in listing order */
  function syBefore(a, b, t) {
    var ra = syRegions(a, t), rb = syRegions(b, t), i;
    if (ra.length !== rb.length) return ra.length < rb.length;
    for (i = 0; i < ra.length; i += 1) if (ra[i] !== rb[i]) return ra[i] > rb[i];
    return false;
  }
  function syAnalyse(inst, aristotelian) {
    var terms = inst.terms, t = terms.length, total = 1 << (1 << t), pat, i;
    var models = 0, counter = null, always = total - 1, never = 0;
    for (pat = 0; pat < total; pat += 1) {
      var ok = true;
      for (i = 0; i < inst.prem.length; i += 1) if (!syHolds(inst.prem[i], pat, terms)) { ok = false; break; }
      if (ok && aristotelian && !syImported(pat, terms)) ok = false;
      if (!ok) continue;
      models += 1;
      always &= pat; never |= pat;
      if (!syHolds(inst.conc, pat, terms) && (counter === null || syBefore(pat, counter, t))) counter = pat;
    }
    return { models: models, counter: counter, valid: counter === null,
             forcedFull: models ? always : 0, forcedEmpty: (total - 1) & ~never };
  }
  function syLabels(terms) {
    var out = [], i, j;
    for (i = 0; i < terms.length; i += 1) {
      var init = terms[i].charAt(0).toUpperCase(), clash = false;
      for (j = 0; j < terms.length; j += 1) if (j !== i && terms[j].charAt(0).toUpperCase() === init) clash = true;
      out.push(clash ? terms[i] : init);
    }
    return out;
  }
  function syRegionName(r, terms) {
    var labels = syLabels(terms), parts = [], k;
    for (k = 0; k < terms.length; k += 1) if (syIn(r, k, terms.length)) parts.push(labels[k]);
    return parts.length ? parts.join('+') : 'outside';
  }
  function syPatternText(pattern, terms) {
    var rs = syRegions(pattern, terms.length), out = [], i;
    if (!rs.length) return 'every region empty';
    for (i = 0; i < rs.length; i += 1) out.push(syRegionName(rs[i], terms));
    return out.join('; ');
  }
  var SY_NAMES = {
    '1': { AAA: 'Barbara', EAE: 'Celarent', AII: 'Darii', EIO: 'Ferio', AAI: 'Barbari', EAO: 'Celaront' },
    '2': { EAE: 'Cesare', AEE: 'Camestres', EIO: 'Festino', AOO: 'Baroco', EAO: 'Cesaro', AEO: 'Camestros' },
    '3': { AII: 'Datisi', IAI: 'Disamis', OAO: 'Bocardo', EIO: 'Ferison', AAI: 'Darapti', EAO: 'Felapton' },
    '4': { AEE: 'Camenes', IAI: 'Dimaris', EIO: 'Fresison', AAI: 'Bramantip', EAO: 'Fesapo', AEO: 'Camenos' }
  };
  /* Mood and figure. The major premise is the one with the conclusion's
     predicate, whichever line it was typed on. */
  function syForm(inst) {
    if (inst.prem.length === 1) return 'immediate inference';
    var c = inst.conc, all = inst.prem.concat([c]), i;
    if (inst.terms.length !== 3) return 'not standard form';
    for (i = 0; i < all.length; i += 1) if (all[i].s.neg || all[i].p.neg) return 'not standard form';
    var S = c.s.term, P = c.p.term, M = inst.terms[2], major = null, minor = null;
    for (i = 0; i < 2; i += 1) {
      var st = inst.prem[i], ts = [st.s.term, st.p.term];
      if (ts.indexOf(M) === -1) return 'not standard form';
      if (ts.indexOf(P) !== -1 && ts.indexOf(S) === -1) major = st;
      else if (ts.indexOf(S) !== -1 && ts.indexOf(P) === -1) minor = st;
    }
    if (!major || !minor) return 'not standard form';
    var fig = major.s.term === M ? (minor.s.term === S ? '1' : '3') : (minor.s.term === S ? '2' : '4');
    var mood = major.type + minor.type + c.type;
    var name = SY_NAMES[fig][mood];
    return mood + '-' + fig + ' ' + (name || '(no name)');
  }
  /* The Venn drawing, with real shading: each region is a rectangle clipped
     into the circles it is inside and masked out of the ones it is not. */
  var SY_GEOM = {
    1: [[260, 155, 105]],
    2: [[210, 155, 100], [310, 155, 100]],
    3: [[215, 120, 92], [305, 120, 92], [260, 200, 92]]
  };
  function syPointIn(x, y, c) { var dx = x - c[0], dy = y - c[1]; return dx * dx + dy * dy < c[2] * c[2]; }
  function syMarkPoint(r, t) {
    var g = SY_GEOM[t], best = null, bestD = -1, x, y, k;
    for (x = 20; x <= 500; x += 6) {
      for (y = 20; y <= 300; y += 6) {
        var ok = true, d = Math.min(x - 10, 510 - x, y - 10, 310 - y);
        for (k = 0; k < t; k += 1) {
          if (syPointIn(x, y, g[k]) !== syIn(r, k, t)) { ok = false; break; }
          var dist = Math.abs(Math.sqrt((x - g[k][0]) * (x - g[k][0]) + (y - g[k][1]) * (y - g[k][1])) - g[k][2]);
          if (dist < d) d = dist;
        }
        if (ok && d > bestD) { bestD = d; best = [x, y]; }
      }
    }
    return best;
  }
  function sySvg(terms, empty, full) {
    var t = terms.length, g = SY_GEOM[t], defs = '', body = '', k, r, labels = syLabels(terms);
    for (k = 0; k < t; k += 1) {
      defs += '<clipPath id="syClip' + k + '"><circle cx="' + g[k][0] + '" cy="' + g[k][1] + '" r="' + g[k][2] + '"/></clipPath>'
        + '<mask id="syOut' + k + '"><rect x="0" y="0" width="520" height="320" fill="#fff"/><circle cx="'
        + g[k][0] + '" cy="' + g[k][1] + '" r="' + g[k][2] + '" fill="#000"/></mask>';
    }
    for (r = 0; r < (1 << t); r += 1) {
      if (!((empty >> r) & 1)) continue;
      var open = '', close = '';
      for (k = 0; k < t; k += 1) {
        open += syIn(r, k, t) ? '<g clip-path="url(#syClip' + k + ')">' : '<g mask="url(#syOut' + k + ')">';
        close += '</g>';
      }
      body += open + '<rect x="10" y="10" width="500" height="300" fill="var(--muted)" fill-opacity="0.45"/>' + close;
    }
    body += '<rect x="10" y="10" width="500" height="300" fill="none" stroke="var(--line-strong)"/>';
    for (k = 0; k < t; k += 1) {
      body += '<circle cx="' + g[k][0] + '" cy="' + g[k][1] + '" r="' + g[k][2] + '" fill="none" stroke="var(--text)" stroke-width="2"/>';
      var lx = t === 1 ? g[k][0] : g[k][0] + (k === 0 ? -g[k][2] * 0.8 : (k === 1 ? g[k][2] * 0.8 : 0));
      var ly = k === 2 ? g[k][1] + g[k][2] + 4 : g[k][1] - g[k][2] * 0.85;
      body += '<text x="' + lx + '" y="' + ly + '" text-anchor="middle" font-size="15" fill="var(--text)">'
        + akEsc(labels[k] + (labels[k] === terms[k] ? '' : ' = ' + terms[k])) + '</text>';
    }
    for (r = 0; r < (1 << t); r += 1) {
      if (!((full >> r) & 1)) continue;
      var pt = syMarkPoint(r, t);
      if (pt) body += '<text x="' + pt[0] + '" y="' + (pt[1] + 7) + '" text-anchor="middle" font-size="22" font-weight="700" fill="var(--red)">×</text>';
    }
    return '<defs>' + defs + '</defs>' + body;
  }
"""

# ---------------------------------------------------------------------------
# sorites
# ---------------------------------------------------------------------------

SORITES_JS = r"""
  /* ---- sorites: one chain, four treatments ------------------------------ */
  function soInt(text, what) {
    var s = String(text).replace(/[\s,_]/g, '');
    if (!/^\d+$/.test(s)) throw new Error(what + ' must be a whole number, and “' + text + '” is not');
    if (s.length > 7) throw new Error(what + ' must be at most 1000000');
    return parseInt(s, 10);
  }
  function soRead(startText, endText, cutText, rangeText, treatment) {
    var start = soInt(startText, 'the starting count'), end = soInt(endText, 'the end count');
    if (start > 1000000) throw new Error('the starting count must be at most 1000000');
    if (!(end < start)) throw new Error('the end count must be smaller than the starting count');
    var out = { start: start, end: end, steps: start - end, treatment: treatment };
    if (treatment === 'cutoff') {
      var c = soInt(cutText, 'the cutoff');
      if (!(c > end && c <= start)) throw new Error('the cutoff must lie above ' + end + ' and at most ' + start);
      out.cutoff = c;
    }
    if (treatment === 'range') {
      var m = /^\s*([\d,_]+)\s*[-–]\s*([\d,_]+)\s*$/.exec(String(rangeText));
      if (!m) throw new Error('the borderline range is written lo-hi, as 50-200');
      var lo = soInt(m[1], 'the range'), hi = soInt(m[2], 'the range');
      if (!(lo < hi)) throw new Error('the range must run from a smaller number to a larger one');
      if (lo < end || hi > start) throw new Error('the range must lie between ' + end + ' and ' + start);
      out.lo = lo; out.hi = hi;
    }
    return out;
  }
  /* The degree of F(k): (k - end)/steps, exactly. */
  function soDegree(k, inst) { return R(BigInt(k - inst.end), BigInt(inst.steps)); }
  /* The value of the conditional F(k) -> F(k-1) under the treatment. The
     range treatment is supervaluation: an admissible sharpening puts its
     cutoff c with lo < c <= hi, so F(k) is false on all of them for k <= lo
     and true on all for k >= hi, and the conditional at k is false on exactly
     the sharpening c = k -- indeterminate for lo < k <= hi. */
  function soCondValue(k, inst) {
    if (inst.treatment === 'classical') return 'true';
    if (inst.treatment === 'cutoff') return k === inst.cutoff ? 'false' : 'true';
    if (inst.treatment === 'range') return (k > inst.lo && k <= inst.hi) ? 'indeterminate' : 'true';
    /* Łukasiewicz: min(1, 1 - v(F(k)) + v(F(k-1))) */
    var v = Radd(Rsub(R1, soDegree(k, inst)), soDegree(k - 1, inst));
    return Rtext(Rcmp(v, R1) > 0 ? R1 : v);
  }
  function soAnalyse(inst) {
    var t = inst.treatment, n = inst.steps;
    if (t === 'classical') return { cond: 'all ' + n + ' true', conc: 'True' };
    if (t === 'cutoff') return { cond: 'one false, at k = ' + inst.cutoff, conc: 'False' };
    if (t === 'range') {
      return { cond: (inst.hi - inst.lo) + ' indeterminate (' + (inst.lo + 1) + '–' + inst.hi + ')', conc: 'Super-false' };
    }
    /* each conditional has the same value, computed at the top of the chain;
       the chained lower bound is max(0, 1 - steps * delta) */
    var each = soCondValue(inst.start, inst), delta = R(1n, BigInt(n));
    var bound = Rsub(R1, Rmul(R(BigInt(n)), delta));
    if (Rsign(bound) < 0) bound = R0;
    return { cond: 'each ' + each, conc: Rtext(bound), each: each };
  }
  function soStrip(inst) {
    var x0 = 30, x1 = 490, y = 30, span = inst.start - inst.end, out = '';
    function X(k) { return (x0 + (x1 - x0) * (k - inst.end) / span).toFixed(1); }
    out += '<rect x="' + x0 + '" y="' + (y - 10) + '" width="' + (x1 - x0) + '" height="20" fill="var(--panel)" stroke="var(--line-strong)"/>';
    if (inst.treatment === 'classical') {
      out += '<rect x="' + x0 + '" y="' + (y - 10) + '" width="' + (x1 - x0) + '" height="20" fill="var(--green)" fill-opacity="0.45"/>';
    } else if (inst.treatment === 'cutoff') {
      out += '<rect x="' + X(inst.cutoff) + '" y="' + (y - 10) + '" width="' + (x1 - X(inst.cutoff)).toFixed(1) + '" height="20" fill="var(--green)" fill-opacity="0.45"/>'
        + '<line x1="' + X(inst.cutoff) + '" x2="' + X(inst.cutoff) + '" y1="' + (y - 16) + '" y2="' + (y + 16) + '" stroke="var(--red)" stroke-width="3"/>'
        + '<text x="' + X(inst.cutoff) + '" y="' + (y + 32) + '" text-anchor="middle" font-size="13" fill="var(--text)">cutoff ' + inst.cutoff + '</text>';
    } else if (inst.treatment === 'range') {
      out += '<rect x="' + X(inst.hi) + '" y="' + (y - 10) + '" width="' + (x1 - X(inst.hi)).toFixed(1) + '" height="20" fill="var(--green)" fill-opacity="0.45"/>'
        + '<rect x="' + X(inst.lo) + '" y="' + (y - 10) + '" width="' + Math.max(1, X(inst.hi) - X(inst.lo)).toFixed(1) + '" height="20" fill="var(--amber)" fill-opacity="0.55"/>'
        + '<text x="' + ((+X(inst.lo) + +X(inst.hi)) / 2).toFixed(1) + '" y="' + (y + 32) + '" text-anchor="middle" font-size="13" fill="var(--text)">sharpenings: cutoff ' + (inst.lo + 1) + '–' + inst.hi + '</text>';
    } else {
      out += '<polygon points="' + x0 + ',' + (y + 10) + ' ' + x1 + ',' + (y + 10) + ' ' + x1 + ',' + (y - 10) + '" fill="var(--green)" fill-opacity="0.55"/>';
    }
    out += '<text x="' + x0 + '" y="' + (y + 32) + '" text-anchor="start" font-size="13" fill="var(--muted)">' + inst.end + '</text>'
      + '<text x="' + x1 + '" y="' + (y + 32) + '" text-anchor="end" font-size="13" fill="var(--muted)">' + inst.start + '</text>';
    return out;
  }
"""

# ---------------------------------------------------------------------------
# kripke
# ---------------------------------------------------------------------------

KRIPKE_JS = r"""
  /* ---- kripke: worlds, accessibility, the five axioms -------------------- */
  function krWorld(text, n) {
    var m = /^w?(\d+)$/.exec(text);
    if (!m) throw new Error('“' + text + '” is not a world number');
    var w = parseInt(m[1], 10);
    if (w < 1 || w > n) throw new Error('world ' + w + ' is out of range; there ' + (n === 1 ? 'is 1 world' : 'are ' + n + ' worlds'));
    return w - 1;
  }
  function krRead(nText, accText, valText, formulaText) {
    var n = parseInt(nText, 10), i, j;
    if (!(n >= 1 && n <= 6)) throw new Error('this lab draws 1 to 6 worlds');
    var succ = [];
    for (i = 0; i < n; i += 1) succ.push([]);
    var pairs = akPieces(accText, /[\s,]+/);
    for (i = 0; i < pairs.length; i += 1) {
      var m = /^(w?\d+)-(w?\d+)$/.exec(pairs[i]);
      if (!m) throw new Error('“' + pairs[i] + '” is not an arc; write 1-2 for “w1 sees w2”');
      var a = krWorld(m[1], n), b = krWorld(m[2], n);
      if (succ[a].indexOf(b) === -1) succ[a].push(b);
    }
    for (i = 0; i < n; i += 1) succ[i].sort();
    var val = {}, entries = akPieces(valText, ';');
    for (i = 0; i < entries.length; i += 1) {
      var mm = /^([A-Za-z][A-Za-z0-9_]*)\s*:\s*(.*)$/.exec(entries[i]);
      if (!mm) throw new Error('“' + entries[i] + '” is not a valuation; write p: 1 2');
      var ws = akPieces(mm[2], /[\s,]+/), set = [];
      for (j = 0; j < n; j += 1) set.push(false);
      for (j = 0; j < ws.length; j += 1) set[krWorld(ws[j], n)] = true;
      val[mm[1]] = set;
    }
    var tree;
    try { tree = akParse(formulaText, true); }
    catch (e) { throw new Error('the formula: ' + akMsg(e)); }
    var atoms = akAtoms(tree);
    if (atoms.length > 4) throw new Error('this lab takes formulas over at most 4 atoms, and this one has ' + atoms.length);
    return { n: n, succ: succ, val: val, tree: tree };
  }
  /* The worlds at which a formula holds, as an array of booleans. An atom
     with no valuation is false everywhere. */
  function krTruth(node, n, succ, val) {
    var out = [], w, i, a, b;
    if (node.op === 'var') { for (w = 0; w < n; w += 1) out.push(val.hasOwnProperty(node.name) ? !!val[node.name][w] : false); return out; }
    if (node.op === 'const') { for (w = 0; w < n; w += 1) out.push(node.v); return out; }
    a = krTruth(node.a, n, succ, val);
    if (node.b) b = krTruth(node.b, n, succ, val);
    for (w = 0; w < n; w += 1) {
      var v = false;
      switch (node.op) {
        case 'not': v = !a[w]; break;
        case 'and': v = a[w] && b[w]; break;
        case 'or': v = a[w] || b[w]; break;
        case 'xor': v = a[w] !== b[w]; break;
        case 'imp': v = !a[w] || b[w]; break;
        case 'iff': v = a[w] === b[w]; break;
        case 'box': v = true; for (i = 0; i < succ[w].length; i += 1) if (!a[succ[w][i]]) v = false; break;
        case 'dia': v = false; for (i = 0; i < succ[w].length; i += 1) if (a[succ[w][i]]) v = true; break;
      }
      out.push(v);
    }
    return out;
  }
  function krSees(succ, a, b) { return succ[a].indexOf(b) !== -1; }
  function krFrame(n, succ) {
    var refl = true, ser = true, sym = true, tra = true, euc = true, a, b, c;
    for (a = 0; a < n; a += 1) {
      if (!krSees(succ, a, a)) refl = false;
      if (!succ[a].length) ser = false;
      for (b = 0; b < n; b += 1) {
        if (krSees(succ, a, b) && !krSees(succ, b, a)) sym = false;
        for (c = 0; c < n; c += 1) {
          if (krSees(succ, a, b) && krSees(succ, b, c) && !krSees(succ, a, c)) tra = false;
          if (krSees(succ, a, b) && krSees(succ, a, c) && !krSees(succ, b, c)) euc = false;
        }
      }
    }
    var out = [];
    if (refl) out.push('reflexive');
    if (ser) out.push('serial');
    if (sym) out.push('symmetric');
    if (tra) out.push('transitive');
    if (euc) out.push('euclidean');
    return out;
  }
  var KR_AXIOMS = [
    ['D', akParse('[]p -> <>p', true)], ['T', akParse('[]p -> p', true)],
    ['B', akParse('p -> []<>p', true)], ['4', akParse('[]p -> [][]p', true)],
    ['5', akParse('<>p -> []<>p', true)]
  ];
  /* An axiom is valid on the frame iff it is true at every world under every
     one of the 2^n valuations of p. */
  function krAxioms(n, succ) {
    var out = [], k, mask, w;
    for (k = 0; k < KR_AXIOMS.length; k += 1) {
      var valid = true;
      for (mask = 0; mask < (1 << n) && valid; mask += 1) {
        var set = [];
        for (w = 0; w < n; w += 1) set.push(((mask >> w) & 1) === 1);
        var tv = krTruth(KR_AXIOMS[k][1], n, succ, { p: set });
        for (w = 0; w < n; w += 1) if (!tv[w]) { valid = false; break; }
      }
      if (valid) out.push(KR_AXIOMS[k][0]);
    }
    return out;
  }
  function krWorldsText(truth) {
    var out = [], w;
    for (w = 0; w < truth.length; w += 1) if (truth[w]) out.push('w' + (w + 1));
    if (out.length === truth.length) return 'all';
    if (!out.length) return 'none';
    return out.join(', ');
  }
  function krSvg(inst, truth, at) {
    var n = inst.n, pos = [], w, i, out = '', cx = 260, cy = 150, rad = n === 1 ? 0 : 100, nr = 26;
    for (w = 0; w < n; w += 1) {
      var ang = -Math.PI / 2 + 2 * Math.PI * w / n;
      pos.push([cx + rad * Math.cos(ang), cy + rad * Math.sin(ang)]);
    }
    out += '<defs><marker id="krArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
      + '<path d="M0,0 L10,5 L0,10 z" fill="var(--text)"/></marker></defs>';
    for (w = 0; w < n; w += 1) {
      for (i = 0; i < inst.succ[w].length; i += 1) {
        var v = inst.succ[w][i], p = pos[w], q = pos[v];
        if (v === w) {
          out += '<path d="M' + (p[0] - 10).toFixed(1) + ',' + (p[1] - nr + 2).toFixed(1) + ' C' + (p[0] - 30).toFixed(1) + ',' + (p[1] - nr - 40).toFixed(1) + ' '
            + (p[0] + 30).toFixed(1) + ',' + (p[1] - nr - 40).toFixed(1) + ' ' + (p[0] + 10).toFixed(1) + ',' + (p[1] - nr + 2).toFixed(1)
            + '" fill="none" stroke="var(--text)" stroke-width="1.6" marker-end="url(#krArrow)"/>';
          continue;
        }
        var dx = q[0] - p[0], dy = q[1] - p[1], len = Math.sqrt(dx * dx + dy * dy) || 1;
        var ux = dx / len, uy = dy / len, off = krSees(inst.succ, v, w) ? 7 : 0;
        var sx = p[0] + ux * nr - uy * off, sy = p[1] + uy * nr + ux * off;
        var ex = q[0] - ux * (nr + 2) - uy * off, ey = q[1] - uy * (nr + 2) + ux * off;
        out += '<line x1="' + sx.toFixed(1) + '" y1="' + sy.toFixed(1) + '" x2="' + ex.toFixed(1) + '" y2="' + ey.toFixed(1)
          + '" stroke="var(--text)" stroke-width="1.6" marker-end="url(#krArrow)"/>';
      }
    }
    for (w = 0; w < n; w += 1) {
      var atoms = [], k;
      for (k in inst.val) if (inst.val.hasOwnProperty(k) && inst.val[k][w]) atoms.push(k);
      out += '<circle cx="' + pos[w][0].toFixed(1) + '" cy="' + pos[w][1].toFixed(1) + '" r="' + nr + '" fill="'
        + (truth[w] ? 'var(--cyan)' : 'var(--panel)') + '" fill-opacity="' + (truth[w] ? '0.35' : '1') + '" stroke="'
        + (w === at ? 'var(--amber)' : 'var(--line-strong)') + '" stroke-width="' + (w === at ? 4 : 1.5) + '"/>'
        + '<text x="' + pos[w][0].toFixed(1) + '" y="' + (pos[w][1] - 3).toFixed(1) + '" text-anchor="middle" font-size="14" font-weight="700" fill="var(--text)">w' + (w + 1) + '</text>'
        + '<text x="' + pos[w][0].toFixed(1) + '" y="' + (pos[w][1] + 13).toFixed(1) + '" text-anchor="middle" font-size="11" fill="var(--text)">'
        + akEsc(atoms.length ? atoms.join(' ') : '–') + '</text>';
    }
    return out;
  }
"""

# ---------------------------------------------------------------------------
# semantics
# ---------------------------------------------------------------------------

SEMANTICS_JS = r"""
  /* ---- semantics: a finite first-order model ---------------------------- */
  var SE_VARS = ['x', 'y', 'z'];
  function seReadModel(domText, extText, namesText) {
    var dom = akPieces(domText, /[\s,]+/), i, j, c;
    if (!dom.length) throw new Error('the domain is empty; a model needs at least one individual');
    if (dom.length > 6) throw new Error('this lab takes at most 6 individuals, and ' + dom.length + ' were typed');
    for (i = 0; i < dom.length; i += 1) {
      if (!/^[a-z]$/.test(dom[i])) throw new Error('“' + dom[i] + '” is not an individual; use single lowercase letters');
      if (SE_VARS.indexOf(dom[i]) !== -1) throw new Error('x, y and z are variables, so they cannot be individuals');
      if (dom.indexOf(dom[i]) !== i) throw new Error(dom[i] + ' is listed twice');
    }
    var preds = {}, entries = akPieces(extText, ';');
    for (i = 0; i < entries.length; i += 1) {
      var m = /^([A-Z][A-Za-z0-9_]*)\s*:\s*(.*)$/.exec(entries[i]);
      if (!m) throw new Error('“' + entries[i] + '” is not an extension; write Planet: a b');
      if (preds.hasOwnProperty(m[1])) throw new Error(m[1] + ' is given two extensions');
      var items = akPieces(m[2], /[\s,]+/), arity = null, ext = {};
      for (j = 0; j < items.length; j += 1) {
        var it = items[j];
        if (!/^[a-z]{1,2}$/.test(it)) throw new Error(m[1] + ': “' + it + '” is not one individual or a pair like ab');
        if (arity !== null && it.length !== arity) throw new Error(m[1] + ' mixes single individuals with pairs');
        arity = it.length;
        for (c = 0; c < it.length; c += 1) {
          if (dom.indexOf(it.charAt(c)) === -1) throw new Error(m[1] + ': ' + it.charAt(c) + ' is not in the domain');
        }
        ext[it] = true;
      }
      preds[m[1]] = { arity: arity, ext: ext };
    }
    var names = {}, nps = akPieces(namesText, /[\s,]+/);
    for (i = 0; i < nps.length; i += 1) {
      var nm = /^([a-z][a-z0-9_]*)=([a-z])$/.exec(nps[i]);
      if (!nm) throw new Error('“' + nps[i] + '” is not a name; write h=a');
      if (SE_VARS.indexOf(nm[1]) !== -1) throw new Error(nm[1] + ' is a variable and cannot be a name');
      if (dom.indexOf(nm[1]) !== -1) throw new Error(nm[1] + ' is an individual of the domain, so it cannot also be a name');
      if (dom.indexOf(nm[2]) === -1) throw new Error('the name ' + nm[1] + ' refers to ' + nm[2] + ', which is not in the domain');
      names[nm[1]] = nm[2];
    }
    return { dom: dom, preds: preds, names: names };
  }
  function seTokenize(src) {
    var out = [], s = String(src), i = 0, m;
    while (i < s.length) {
      var ch = s.charAt(i);
      if (/\s/.test(ch)) { i += 1; continue; }
      if (s.substr(i, 3) === '<->') { out.push({ t: 'iff' }); i += 3; continue; }
      if (s.substr(i, 2) === '->') { out.push({ t: 'imp' }); i += 2; continue; }
      if ('¬~!'.indexOf(ch) !== -1) { out.push({ t: 'not' }); i += 1; continue; }
      if ('∧&'.indexOf(ch) !== -1) { out.push({ t: 'and' }); i += 1; continue; }
      if ('∨|'.indexOf(ch) !== -1) { out.push({ t: 'or' }); i += 1; continue; }
      if ('→⇒'.indexOf(ch) !== -1) { out.push({ t: 'imp' }); i += 1; continue; }
      if ('↔⇔'.indexOf(ch) !== -1) { out.push({ t: 'iff' }); i += 1; continue; }
      if (ch === '∀') { out.push({ t: 'all' }); i += 1; continue; }
      if (ch === '∃') { out.push({ t: 'ex' }); i += 1; continue; }
      if ('()[]:,='.indexOf(ch) !== -1) { out.push({ t: ch }); i += 1; continue; }
      m = /^[A-Za-z][A-Za-z0-9_]*/.exec(s.slice(i));
      if (m) { out.push({ t: 'word', v: m[0] }); i += m[0].length; continue; }
      throw new Error('“' + ch + '” is not part of the sentence language');
    }
    return out;
  }
  /* Quantifiers are Ax / Ex (or A x, or the symbols) with x, y or z, scoping
     over what follows them; [the x: F(x)] G(x) is Russell's description. */
  function seParse(src, model) {
    var ts = seTokenize(src), pos = 0, usedArity = {};
    if (!ts.length) throw new Error('there is no sentence here');
    function at(t) { return ts[pos] && ts[pos].t === t; }
    function here() { return ts[pos] ? '“' + (ts[pos].v || ts[pos].t) + '”' : 'the end'; }
    function need(t, what) { if (!at(t)) throw new Error('expected ' + what + ' at ' + here()); pos += 1; }
    function variable() {
      if (!at('word') || SE_VARS.indexOf(ts[pos].v) === -1) throw new Error('a quantifier needs one of the variables x, y, z');
      pos += 1; return ts[pos - 1].v;
    }
    function term() {
      if (!at('word')) throw new Error('expected a name, an individual or a variable at ' + here());
      var w = ts[pos].v; pos += 1;
      if (SE_VARS.indexOf(w) !== -1) return { kind: 'var', v: w };
      if (model.names.hasOwnProperty(w)) return { kind: 'const', d: model.names[w], text: w };
      if (model.dom.indexOf(w) !== -1) return { kind: 'const', d: w, text: w };
      throw new Error('“' + w + '” is not a name or an individual of this model');
    }
    function quantWord() {
      var t = ts[pos];
      if (!t || t.t !== 'word') return null;
      if (/^[AE][xyz]$/.test(t.v) && !model.preds.hasOwnProperty(t.v)) return { q: t.v.charAt(0) === 'A' ? 'all' : 'ex', v: t.v.charAt(1), len: 1 };
      if ((t.v === 'A' || t.v === 'E') && ts[pos + 1] && ts[pos + 1].t === 'word' && SE_VARS.indexOf(ts[pos + 1].v) !== -1) {
        return { q: t.v === 'A' ? 'all' : 'ex', v: ts[pos + 1].v, len: 2 };
      }
      return null;
    }
    function unary() {
      if (at('not')) { pos += 1; return { op: 'not', a: unary() }; }
      if (at('all') || at('ex')) { var q = ts[pos].t; pos += 1; var v = variable(); return { op: q, v: v, a: unary() }; }
      var qw = quantWord();
      if (qw) { pos += qw.len; return { op: qw.q, v: qw.v, a: unary() }; }
      if (at('[')) {
        pos += 1;
        if (!at('word') || ts[pos].v !== 'the') throw new Error('a description is written [the x: F(x)]');
        pos += 1;
        var dv = variable();
        need(':', '“:” after the description’s variable');
        var r = iff();
        need(']', '“]” to close the description');
        return { op: 'the', v: dv, r: r, a: unary() };
      }
      if (at('(')) { pos += 1; var inner = iff(); need(')', '“)”'); return inner; }
      if (at('word') && /^[A-Z]/.test(ts[pos].v) && ts[pos + 1] && ts[pos + 1].t === '(') {
        var name = ts[pos].v; pos += 2;
        if (!model.preds.hasOwnProperty(name)) throw new Error('the predicate ' + name + ' has no extension in the model; list it, even as “' + name + ':”');
        var args = [term()];
        while (at(',')) { pos += 1; args.push(term()); }
        need(')', '“)” to close ' + name + '(…)');
        if (args.length > 2) throw new Error(name + ' takes one or two arguments');
        var declared = model.preds[name].arity;
        if (declared !== null && declared !== args.length) throw new Error(name + ' has ' + (declared === 1 ? 'single individuals' : 'pairs') + ' in its extension but is used with ' + args.length + ' argument' + (args.length === 1 ? '' : 's'));
        if (usedArity.hasOwnProperty(name) && usedArity[name] !== args.length) throw new Error(name + ' is used with different numbers of arguments');
        usedArity[name] = args.length;
        return { op: 'pred', name: name, args: args };
      }
      if (at('word')) {
        var l = term();
        need('=', '“=” after ' + (l.text || l.v));
        return { op: 'eq', a: l, b: term() };
      }
      throw new Error(here() + ' cannot start a sentence');
    }
    function conj() { var n = unary(); while (at('and')) { pos += 1; n = { op: 'and', a: n, b: unary() }; } return n; }
    function disj() { var n = conj(); while (at('or')) { pos += 1; n = { op: 'or', a: n, b: conj() }; } return n; }
    function cond() { var l = disj(); if (at('imp')) { pos += 1; return { op: 'imp', a: l, b: cond() }; } return l; }
    function iff() { var n = cond(); while (at('iff')) { pos += 1; n = { op: 'iff', a: n, b: cond() }; } return n; }
    var tree = iff();
    if (pos !== ts.length) throw new Error('there is more after a complete sentence, starting at ' + here());
    var free = seFree(tree, [], []);
    if (free.length) throw new Error('the variable ' + free[0] + ' is not bound by any quantifier');
    if (seDepth(tree) > 3) throw new Error('this lab takes quantifiers and descriptions nested at most 3 deep');
    return tree;
  }
  function seFree(node, bound, out) {
    var i;
    if (node.op === 'pred' || node.op === 'eq') {
      var args = node.op === 'pred' ? node.args : [node.a, node.b];
      for (i = 0; i < args.length; i += 1) if (args[i].kind === 'var' && bound.indexOf(args[i].v) === -1 && out.indexOf(args[i].v) === -1) out.push(args[i].v);
      return out;
    }
    if (node.op === 'all' || node.op === 'ex') return seFree(node.a, bound.concat([node.v]), out);
    if (node.op === 'the') { seFree(node.r, bound.concat([node.v]), out); return seFree(node.a, bound.concat([node.v]), out); }
    seFree(node.a, bound, out);
    if (node.b) seFree(node.b, bound, out);
    return out;
  }
  function seDepth(node) {
    if (node.op === 'pred' || node.op === 'eq') return 0;
    if (node.op === 'all' || node.op === 'ex') return 1 + seDepth(node.a);
    if (node.op === 'the') return 1 + Math.max(seDepth(node.r), seDepth(node.a));
    return Math.max(seDepth(node.a), node.b ? seDepth(node.b) : 0);
  }
  function seVal(t, env) { return t.kind === 'var' ? env[t.v] : t.d; }
  function seWith(env, v, d) { var e = {}, k; for (k in env) if (env.hasOwnProperty(k)) e[k] = env[k]; e[v] = d; return e; }
  function seEval(node, env, M) {
    var i, c, hit, key;
    switch (node.op) {
      case 'not': return !seEval(node.a, env, M);
      case 'and': return seEval(node.a, env, M) && seEval(node.b, env, M);
      case 'or': return seEval(node.a, env, M) || seEval(node.b, env, M);
      case 'imp': return !seEval(node.a, env, M) || seEval(node.b, env, M);
      case 'iff': return seEval(node.a, env, M) === seEval(node.b, env, M);
      case 'eq': return seVal(node.a, env) === seVal(node.b, env);
      case 'pred':
        key = '';
        for (i = 0; i < node.args.length; i += 1) key += seVal(node.args[i], env);
        return M.preds[node.name].ext.hasOwnProperty(key);
      case 'all':
        for (i = 0; i < M.dom.length; i += 1) if (!seEval(node.a, seWith(env, node.v, M.dom[i]), M)) return false;
        return true;
      case 'ex':
        for (i = 0; i < M.dom.length; i += 1) if (seEval(node.a, seWith(env, node.v, M.dom[i]), M)) return true;
        return false;
      case 'the':
        /* Russell: Ex (F(x) & Ay (F(y) -> y = x) & G(x)) */
        c = 0; hit = null;
        for (i = 0; i < M.dom.length; i += 1) if (seEval(node.r, seWith(env, node.v, M.dom[i]), M)) { c += 1; hit = M.dom[i]; }
        return c === 1 && seEval(node.a, seWith(env, node.v, hit), M);
    }
    return false;
  }
  /* Breadth-first: the first node satisfying WANT, never looking inside a
     node for which STOP holds. */
  function seFind(tree, want, stop) {
    var queue = [tree];
    while (queue.length) {
      var n = queue.shift();
      if (want(n)) return n;
      if (stop(n)) continue;
      if (n.r) queue.push(n.r);
      if (n.a && n.a.op) queue.push(n.a);
      if (n.b && n.b.op) queue.push(n.b);
    }
    return null;
  }
  /* The outermost quantifier is the first one met from the root that is
     not inside a description; its matrix is checked at every individual. The
     description reported is the first whose restrictor is closed. */
  function seAnalyse(tree, M) {
    var value = seEval(tree, {}, M), i;
    var q = seFind(tree, function (n) { return n.op === 'all' || n.op === 'ex'; },
                   function (n) { return n.op === 'the'; });
    var witness = '—', satText = '—', sat = [];
    if (q) {
      for (i = 0; i < M.dom.length; i += 1) if (seEval(q.a, seWith({}, q.v, M.dom[i]), M)) sat.push(M.dom[i]);
      satText = sat.length + ' of ' + M.dom.length + ' satisfy';
      if (q.op === 'ex' && sat.length) witness = q.v + ' = ' + sat[0];
      if (q.op === 'all' && sat.length < M.dom.length) {
        for (i = 0; i < M.dom.length; i += 1) if (sat.indexOf(M.dom[i]) === -1) { witness = 'fails at ' + q.v + ' = ' + M.dom[i]; break; }
      }
    }
    var anyDesc = seFind(tree, function (n) { return n.op === 'the'; }, function () { return false; });
    var d = seFind(tree, function (n) { return n.op === 'the' && seFree(n.r, [n.v], []).length === 0; },
                   function () { return false; });
    var desc = 'no description', denot = [];
    if (d) {
      for (i = 0; i < M.dom.length; i += 1) if (seEval(d.r, seWith({}, d.v, M.dom[i]), M)) denot.push(M.dom[i]);
      desc = denot.length === 1 ? 'denotes ' + denot[0] : (denot.length ? 'not unique: ' + denot.join(', ') : 'denotes nothing');
    } else if (anyDesc) {
      desc = '—';
    }
    return { value: value, quant: q, sat: sat, satText: satText, witness: witness, desc: desc, descNode: d, denot: denot };
  }
  function seTermText(t) { return t.kind === 'var' ? t.v : t.text; }
  function seShow(node, outer) {
    var s, i, a;
    switch (node.op) {
      case 'pred':
        a = [];
        for (i = 0; i < node.args.length; i += 1) a.push(seTermText(node.args[i]));
        return node.name + '(' + a.join(', ') + ')';
      case 'eq': return seTermText(node.a) + ' = ' + seTermText(node.b);
      case 'not': return '¬' + seShow(node.a, false);
      case 'all': return '∀' + node.v + ' ' + seShow(node.a, false);
      case 'ex': return '∃' + node.v + ' ' + seShow(node.a, false);
      case 'the': return '[the ' + node.v + ': ' + seShow(node.r, true) + '] ' + seShow(node.a, false);
    }
    var g = { and: '∧', or: '∨', imp: '→', iff: '↔' }[node.op];
    s = seShow(node.a, false) + ' ' + g + ' ' + seShow(node.b, false);
    return outer ? s : '(' + s + ')';
  }
"""

# ---------------------------------------------------------------------------
# analysis
# ---------------------------------------------------------------------------

ANALYSIS_JS = r"""
  /* ---- analysis: a definition against a case table ---------------------- */
  function anRead(defText, conditions) {
    if (!String(defText).replace(/\s+/g, '').length) throw new Error('the definition is empty');
    var tree;
    try { tree = akParse(defText, false); }
    catch (e) { throw new Error('the definition: ' + akMsg(e)); }
    var atoms = akAtoms(tree), i;
    for (i = 0; i < atoms.length; i += 1) {
      if (conditions.indexOf(atoms[i]) === -1) throw new Error(atoms[i] + ' is not one of the conditions (' + conditions.join(', ') + ')');
    }
    return tree;
  }
  function anEnv(conditions, values) {
    var env = {}, i;
    for (i = 0; i < conditions.length; i += 1) env[conditions[i]] = values[i] === 1;
    return env;
  }
  /* Too broad: the definition counts a case the verdict excludes. Too
     narrow: it excludes a case the verdict counts. */
  function anAnalyse(tree, conditions, cases) {
    var agree = 0, broad = false, narrow = false, fail = null, vals = [], i;
    for (i = 0; i < cases.length; i += 1) {
      var d = akEval(tree, anEnv(conditions, cases[i].values)), v = cases[i].verdict === 1;
      vals.push(d);
      if (d === v) { agree += 1; continue; }
      if (d) broad = true; else narrow = true;
      if (!fail) fail = { name: cases[i].name, dir: d ? 'too broad' : 'too narrow' };
    }
    var verdict = broad && narrow ? 'Too broad and too narrow' : (broad ? 'Too broad' : (narrow ? 'Too narrow' : 'Adequate'));
    return { agree: agree, fail: fail, verdict: verdict, vals: vals };
  }
  /* singles: every literal, in condition order, positive before negated.
     pairs: those, then every conjunction and then every disjunction of two
     literals on distinct conditions. A candidate fits when it agrees with
     every verdict. */
  function anLitVal(l, c) { return (c.values[l.i] === 1) === l.pos; }
  function anFits(cases, f) {
    var c;
    for (c = 0; c < cases.length; c += 1) if (f(cases[c]) !== (cases[c].verdict === 1)) return false;
    return true;
  }
  function anCandidates(conditions, cases, search) {
    var lits = [], out = [], i, j, o;
    for (i = 0; i < conditions.length; i += 1) { lits.push({ i: i, pos: true }); lits.push({ i: i, pos: false }); }
    function text(l) { return (l.pos ? '' : '~') + conditions[l.i]; }
    function single(l) { return function (c) { return anLitVal(l, c); }; }
    function both(a, b, op) {
      return op === '&' ? function (c) { return anLitVal(a, c) && anLitVal(b, c); }
                        : function (c) { return anLitVal(a, c) || anLitVal(b, c); };
    }
    for (i = 0; i < lits.length; i += 1) if (anFits(cases, single(lits[i]))) out.push(text(lits[i]));
    if (search !== 'pairs') return out;
    var ops = ['&', '|'];
    for (o = 0; o < ops.length; o += 1) {
      for (i = 0; i < lits.length; i += 1) {
        for (j = 0; j < lits.length; j += 1) {
          if (!(lits[i].i < lits[j].i)) continue;
          if (anFits(cases, both(lits[i], lits[j], ops[o]))) out.push(text(lits[i]) + ' ' + ops[o] + ' ' + text(lits[j]));
        }
      }
    }
    return out;
  }
"""

# ---------------------------------------------------------------------------
# structural
# ---------------------------------------------------------------------------

STRUCTURAL_JS = r"""
  /* ---- structural: Boolean structural causal models --------------------- */
  function stRead(eqText, exoText) {
    var exo = {}, exoOrder = [], pieces = akPieces(exoText, /[\s,;]+/), i, j;
    for (i = 0; i < pieces.length; i += 1) {
      var m = /^([A-Za-z][A-Za-z0-9_₀-₉]*)=([01])$/.exec(pieces[i]);
      if (!m) throw new Error('“' + pieces[i] + '” is not an exogenous setting; write S1=1');
      if (exo.hasOwnProperty(m[1])) throw new Error(m[1] + ' is set twice');
      exo[m[1]] = m[2] === '1'; exoOrder.push(m[1]);
    }
    var eqs = {}, endo = [], lines = akPieces(eqText, ';');
    if (!lines.length) throw new Error('there are no equations here; write D = S1 | S2');
    for (i = 0; i < lines.length; i += 1) {
      var mm = /^([A-Za-z][A-Za-z0-9_₀-₉]*)\s*=\s*(.+)$/.exec(lines[i]);
      if (!mm) throw new Error('“' + lines[i] + '” is not an equation; write F = D & ~G');
      if (eqs.hasOwnProperty(mm[1])) throw new Error(mm[1] + ' has two equations');
      if (exo.hasOwnProperty(mm[1])) throw new Error(mm[1] + ' is exogenous and also has an equation');
      try { eqs[mm[1]] = akParse(mm[2], false); }
      catch (e) { throw new Error('the equation for ' + mm[1] + ': ' + akMsg(e)); }
      endo.push(mm[1]);
    }
    var all = exoOrder.concat(endo);
    if (all.length > 8) throw new Error('this lab takes at most 8 variables, and the model has ' + all.length);
    for (i = 0; i < endo.length; i += 1) {
      var used = akAtoms(eqs[endo[i]]);
      for (j = 0; j < used.length; j += 1) if (all.indexOf(used[j]) === -1) throw new Error(used[j] + ', in the equation for ' + endo[i] + ', is neither exogenous nor defined by an equation');
    }
    /* dependency order, ties broken by equation order */
    var order = [], placed = {}, progress = true;
    for (i = 0; i < exoOrder.length; i += 1) placed[exoOrder[i]] = true;
    while (order.length < endo.length && progress) {
      progress = false;
      for (i = 0; i < endo.length; i += 1) {
        if (placed[endo[i]]) continue;
        var deps = akAtoms(eqs[endo[i]]), ready = true;
        for (j = 0; j < deps.length; j += 1) if (!placed[deps[j]]) { ready = false; break; }
        if (ready) { order.push(endo[i]); placed[endo[i]] = true; progress = true; break; }
      }
    }
    if (order.length < endo.length) {
      var stuck = [];
      for (i = 0; i < endo.length; i += 1) if (!placed[endo[i]]) stuck.push(endo[i]);
      throw new Error('the equations form a cycle through ' + stuck.join(', ') + '; a structural model must be acyclic');
    }
    return { exo: exo, exoOrder: exoOrder, eqs: eqs, endo: endo, order: order, vars: all };
  }
  /* Solve with some variables held: FIX maps a name to a value and
     overrides that variable's equation or its exogenous setting. */
  function stSolve(model, fix) {
    var v = {}, i, k;
    for (i = 0; i < model.exoOrder.length; i += 1) {
      k = model.exoOrder[i];
      v[k] = fix.hasOwnProperty(k) ? fix[k] : model.exo[k];
    }
    for (i = 0; i < model.order.length; i += 1) {
      k = model.order[i];
      v[k] = fix.hasOwnProperty(k) ? fix[k] : akEval(model.eqs[k], v);
    }
    return v;
  }
  function stNameLess(a, b) {
    var i;
    for (i = 0; i < a.length && i < b.length; i += 1) if (a[i] !== b[i]) return a[i] < b[i];
    return a.length < b.length;
  }
  /* But-for: flip the cause, re-solve. Halpern-Pearl (modified): W ranges
     over the other endogenous variables (never the effect), held at their
     actual values while the cause is flipped; the witness is the smallest W,
     then the lexicographically first. Joint: when no W works, flip the cause
     together with each other variable in turn, exogenous ones first; a
     partner that changes the effect on its own is skipped, because then the
     pair proves nothing about the cause. */
  function stAnalyse(model, cause, effect) {
    var actual = stSolve(model, {}), i, j;
    var flip = {}; flip[cause] = !actual[cause];
    var flipped = stSolve(model, flip);
    var butFor = flipped[effect] !== actual[effect];
    var pool = [];
    for (i = 0; i < model.endo.length; i += 1) if (model.endo[i] !== cause && model.endo[i] !== effect) pool.push(model.endo[i]);
    var subsets = [];
    for (i = 0; i < (1 << pool.length); i += 1) {
      var names = [];
      for (j = 0; j < pool.length; j += 1) if (i & (1 << j)) names.push(pool[j]);
      names.sort();
      subsets.push(names);
    }
    subsets.sort(function (a, b) {
      if (a.length !== b.length) return a.length - b.length;
      return stNameLess(a, b) ? -1 : (stNameLess(b, a) ? 1 : 0);
    });
    var witness = null, held = null;
    for (i = 0; i < subsets.length; i += 1) {
      var fix = {}; fix[cause] = !actual[cause];
      for (j = 0; j < subsets[i].length; j += 1) fix[subsets[i][j]] = actual[subsets[i][j]];
      var res = stSolve(model, fix);
      if (res[effect] !== actual[effect]) { witness = subsets[i]; held = res; break; }
    }
    var partner = null, joint = null;
    if (!witness) {
      for (i = 0; i < model.vars.length; i += 1) {
        var o = model.vars[i];
        if (o === cause || o === effect) continue;
        var fx = {}; fx[cause] = !actual[cause]; fx[o] = !actual[o];
        var alone = {}; alone[o] = !actual[o];
        if (stSolve(model, alone)[effect] !== actual[effect]) continue;
        var jr = stSolve(model, fx);
        if (jr[effect] !== actual[effect]) { partner = o; joint = jr; break; }
      }
    }
    var hp = witness ? (witness.length ? 'Yes, holding {' + witness.join(', ') + '}' : 'Yes, holding nothing') : 'No';
    var kind = butFor ? 'but-for cause' : (witness ? 'cause (holding fixed)' : (partner ? 'joint cause with ' + partner : 'not a cause'));
    return { actual: actual, flipped: flipped, butFor: butFor, witness: witness, held: held,
             partner: partner, joint: joint, hp: hp, kind: kind };
  }
"""


# ---------------------------------------------------------------------------
# Control furniture -- the shapes every kit on the generated paths uses.
# ---------------------------------------------------------------------------


def _attr(text):
    return (str(text).replace("&", "&amp;").replace('"', "&quot;")
            .replace("<", "&lt;").replace(">", "&gt;"))


def _select(cid, label, options, chosen):
    opts = "".join(
        '<option value="%s"%s>%s</option>'
        % (_attr(v), " selected" if str(v) == str(chosen) else "", _attr(t))
        for v, t in options
    )
    return (
        '        <div class="field">\n          <label for="%s">%s</label>\n'
        '          <select id="%s">%s</select>\n        </div>\n' % (cid, label, cid, opts)
    )


def _text(cid, label, value):
    """A text box. Its shipped value may contain none of > < & "; see the module doc."""
    value = str(value)
    for bad in '><&"':
        if bad in value:
            raise ValueError("argkit: a control value may not contain %r: %r" % (bad, value))
    return (
        '        <div class="field">\n          <label for="%s">%s</label>\n'
        '          <input id="%s" type="text" value="%s" inputmode="text" autocomplete="off" spellcheck="false">\n'
        "        </div>\n" % (cid, label, cid, value)
    )


def _range(cid, label, lo, hi, value):
    return (
        "        <div>\n"
        '          <div class="range-row"><label class="small-copy" for="%s">%s</label>'
        '<span class="range-value" id="%sOut">%s</span></div>\n'
        '          <input id="%s" type="range" min="%s" max="%s" step="1" value="%s" />\n'
        "        </div>\n" % (cid, label, cid, value, cid, lo, hi, value)
    )


def _kpis(items):
    cells = "".join(
        '          <div class="kpi"><span>%s</span><strong id="%s">&mdash;</strong></div>\n'
        % (label, cid) for label, cid in items
    )
    return '        <div class="kpi-grid">\n%s        </div>\n' % cells


def _hint(text):
    return '        <p class="small-copy" style="margin:0;">%s</p>\n' % text


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


def _wrap(cid, top=12):
    return '      <div class="table-wrap" style="margin-top:%dpx;" id="%s"></div>\n' % (top, cid)


def _banner(cid):
    return '      <div class="status-banner" id="%s" style="margin-top:12px;"></div>\n' % cid


# ---------------------------------------------------------------------------
# Presets: lesson data, validated at build time. A malformed instance raises
# ValueError naming the preset; a missing `expect` does not (labcheck owns it).
# ---------------------------------------------------------------------------

_IDENT = re.compile(r"[A-Za-z][A-Za-z0-9_₀-₉]*")


def _canon(text, modal=False):
    """The glyph spelling of a formula: what a text box ships."""
    s = str(text).replace("<->", "↔").replace("->", "→")
    if modal:
        s = s.replace("[]", "□").replace("<>", "◇")
    return s.replace("&", "∧").replace("|", "∨").replace("~", "¬")


def _atoms(text):
    return sorted(set(_IDENT.findall(str(text))))


def _presets(cfg, mode):
    presets = cfg.get("presets")
    if not isinstance(presets, list) or not presets:
        raise ValueError("argkit/%s: cfg['presets'] must be a non-empty list" % mode)
    seen = set()
    for p in presets:
        if not isinstance(p, dict) or not p.get("id") or not p.get("label"):
            raise ValueError("argkit/%s: every preset needs an id and a label: %r" % (mode, p))
        pid = str(p["id"])
        if pid in seen:
            raise ValueError("argkit/%s: preset id %r is used twice" % (mode, pid))
        if any(c in pid for c in '<>&"'):
            raise ValueError("argkit/%s: preset id %r may not contain < > & \"" % (mode, pid))
        seen.add(pid)
    return presets


def _check(mode, preset, ok, why):
    if not ok:
        raise ValueError("argkit/%s: preset %r: %s" % (mode, preset.get("id"), why))


def _chosen(presets, cfg, mode):
    want = str(cfg.get("preset", presets[0]["id"]))
    for p in presets:
        if str(p["id"]) == want:
            return p
    raise ValueError("argkit/%s: no preset %r; this lesson has %s"
                     % (mode, want, ", ".join(str(p["id"]) for p in presets)))


def _expect(presets):
    return {str(p["id"]): dict(p.get("expect") or {}) for p in presets}


def _options(presets):
    return [(str(p["id"]), p["label"]) for p in presets]


def _choice(cfg, key, allowed, mode):
    value = str(cfg.get(key, allowed[0]))
    if value not in allowed:
        raise ValueError("argkit/%s: cfg[%r] must be one of %s, not %r"
                         % (mode, key, ", ".join(allowed), value))
    return value


def _lab(cfg, *, title, subtitle, markup, controls, script, panel_title, panel_intro,
         select, presets):
    return Lab(
        title=title,
        subtitle=subtitle,
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", panel_title),
        panel_intro=cfg.get("panel_intro", panel_intro),
        script=script,
        expect={select: _expect(presets)},
    )


# ---------------------------------------------------------------------------
# validity
# ---------------------------------------------------------------------------


def _validity(cfg):
    mode = "validity"
    presets = _presets(cfg, mode)
    table = {}
    for p in presets:
        prem = p.get("premises")
        _check(mode, p, isinstance(prem, list) and all(isinstance(x, str) for x in prem),
               "premises must be a list of strings")
        _check(mode, p, len(prem) <= 6, "at most 6 premises")
        _check(mode, p, all(x.strip() and ";" not in x for x in prem),
               "a premise may be neither empty nor contain ';'")
        conc = p.get("conclusion")
        _check(mode, p, isinstance(conc, str) and conc.strip(), "the conclusion is empty")
        atoms = set()
        for x in prem + [conc]:
            atoms.update(_atoms(x))
        _check(mode, p, len(atoms) <= 6, "more than 6 sentence letters: %s" % ", ".join(sorted(atoms)))
        table[str(p["id"])] = {"premises": "; ".join(_canon(x) for x in prem),
                               "conclusion": _canon(conc)}
    chosen = _chosen(presets, cfg, mode)
    show = _choice(cfg, "show", ["all", "counter"], mode)
    first = table[str(chosen["id"])]
    tiles = [("Rows", "vaRows"), ("Counterexample rows", "vaCounter"),
             ("Verdict", "vaVerdict"), ("Form", "vaForm")]
    markup = (
        _toolbar("Every row, and the rows that refute",
                 "a counterexample row makes every premise true and the conclusion false",
                 [("green", "T"), ("red", "F"), ("amber", "counterexample row")])
        + _stage('<div class="table-wrap" id="vaTable"></div>')
        + _banner("vaStatus")
    )
    controls = (
        _select("vaPreset", "Argument", _options(presets), chosen["id"])
        + _text("vaPremises", "Premises, separated by semicolons", first["premises"])
        + _text("vaConclusion", "Conclusion", first["conclusion"])
        + _select("vaShow", "Rows shown", [("all", "every row"), ("counter", "counterexample rows only")], show)
        + _kpis(tiles)
        + _hint("Sentence letters are words such as p or q; type ~ for not, &amp; for and, | for or, "
                "-&gt; for if-then and &lt;-&gt; for if and only if, or use the symbols.")
    )
    script = AK_UI_JS + AK_PROP_JS + VALIDITY_JS + cfg_literal("VAP", table) + r"""
  var VA_TILES = ['vaRows', 'vaCounter', 'vaVerdict', 'vaForm'];
  var vaPresetIn = akEl('vaPreset'), vaPremIn = akEl('vaPremises'), vaConcIn = akEl('vaConclusion');
  var vaShowIn = akEl('vaShow');
  function vaRender(inst, res) {
    var form = vaFormName(inst.premises, inst.conclusion), i, j;
    akSet('vaRows', res.rows.length);
    akSet('vaCounter', res.counter);
    akSet('vaVerdict', res.valid ? 'Valid' : 'Invalid');
    akSet('vaForm', form || 'no catalogued form');
    var head = '<tr>';
    for (i = 0; i < inst.vars.length; i += 1) head += '<th>' + akEsc(inst.vars[i]) + '</th>';
    for (i = 0; i < inst.premises.length; i += 1) head += '<th>P' + (i + 1) + ': ' + akEsc(akShow(inst.premises[i], true)) + '</th>';
    head += '<th class="rowhead">C: ' + akEsc(akShow(inst.conclusion, true)) + '</th></tr>';
    var body = '', shown = 0;
    for (i = 0; i < res.rows.length; i += 1) {
      var row = res.rows[i];
      if (vaShowIn.value === 'counter' && !row.counter) continue;
      shown += 1;
      body += '<tr' + (row.counter ? ' class="focus"' : '') + '>';
      for (j = 0; j < inst.vars.length; j += 1) body += akCell(row.env[inst.vars[j]]);
      for (j = 0; j < row.pv.length; j += 1) body += akCell(row.pv[j]);
      body += akCell(row.c) + '</tr>';
    }
    if (!shown) body = '<tr><td colspan="' + (inst.vars.length + inst.premises.length + 1) + '">no row makes every premise true and the conclusion false</td></tr>';
    akEl('vaTable').innerHTML = '<table class="tt"><caption>' + res.rows.length + ' row' + (res.rows.length === 1 ? '' : 's')
      + ' over ' + inst.vars.length + ' sentence letter' + (inst.vars.length === 1 ? '' : 's')
      + '; a highlighted row is a counterexample</caption><thead>' + head + '</thead><tbody>' + body + '</tbody></table>';
    var why;
    if (!res.valid) {
      why = '<strong>Invalid.</strong> ' + res.counter + ' of the ' + res.rows.length + ' rows make every premise true and the conclusion false; the first is <strong>'
        + akEsc(akEnvText(inst.vars, res.first)) + '</strong>. One such row is all it takes.';
    } else if (inst.premises.length && res.premSat === 0) {
      why = '<strong>Valid because the premises cannot all be true:</strong> no row makes every premise true, so no row can be a counterexample.';
    } else if (res.concTaut) {
      why = '<strong>Valid because the conclusion is a tautology:</strong> it is true in every row, whatever the premises say.';
    } else {
      why = '<strong>Valid.</strong> ' + res.premSat + ' of the ' + res.rows.length + ' rows make every premise true, and the conclusion is true in each of them.';
    }
    akEl('vaStatus').innerHTML = why + (form ? ' It has the shape of <strong>' + form + '</strong>.' : ' The shape matches nothing in the catalogue.')
      + ' Computed from ' + inst.premises.length + ' premise' + (inst.premises.length === 1 ? '' : 's') + ' and the conclusion over every row.';
  }
  function redraw() {
    var inst;
    try {
      inst = vaRead(vaPremIn.value, vaConcIn.value);
    } catch (e) {
      akRefuse('vaStatus', VA_TILES, ['vaTable'], akMsg(e)); return;
    }
    vaRender(inst, vaAnalyse(inst.premises, inst.conclusion, inst.vars));
  }
  vaPresetIn.addEventListener('change', function () {
    var p = VAP[vaPresetIn.value];
    if (p) { vaPremIn.value = p.premises; vaConcIn.value = p.conclusion; }
    redraw();
  });
  [vaPremIn, vaConcIn].forEach(function (el) { el.addEventListener('input', redraw); });
  vaShowIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg, title="Validity by cases", subtitle="Every row, every counterexample, and the form",
        markup=markup, controls=controls, script=script, select="vaPreset", presets=presets,
        panel_title="Choose the argument",
        panel_intro="The table lists every assignment of true and false to the sentence letters. "
                    "The verdict is read off it: valid exactly when no row is a counterexample.",
    )


# ---------------------------------------------------------------------------
# consistency
# ---------------------------------------------------------------------------


def _consistency(cfg):
    mode = "consistency"
    presets = _presets(cfg, mode)
    table = {}
    for p in presets:
        s = p.get("sentences")
        _check(mode, p, isinstance(s, list) and s and all(isinstance(x, str) and x.strip() for x in s),
               "sentences must be a non-empty list of strings")
        _check(mode, p, len(s) <= 8, "at most 8 sentences")
        _check(mode, p, all(";" not in x for x in s), "a sentence may not contain ';'")
        atoms = set()
        for x in s:
            atoms.update(_atoms(x))
        _check(mode, p, len(atoms) <= 6, "more than 6 sentence letters: %s" % ", ".join(sorted(atoms)))
        table[str(p["id"])] = {"sentences": "; ".join(_canon(x) for x in s), "n": len(s)}
    chosen = _chosen(presets, cfg, mode)
    first = table[str(chosen["id"])]
    drops = [("0", "keep all")] + [(str(i), "drop %d" % i) for i in range(1, first["n"] + 1)]
    tiles = [("Models", "coModels"), ("Verdict", "coVerdict"),
             ("Smallest inconsistent subset", "coMis"), ("A model", "coWitness")]
    markup = (
        _toolbar("Can they all be true together?",
                 "a model makes every kept sentence true; a minimal inconsistent subset has none",
                 [("green", "T"), ("red", "F")])
        + _stage('<div class="table-wrap" id="coModelsTable"></div>')
        + _wrap("coMisList")
        + _banner("coStatus")
    )
    controls = (
        _select("coPreset", "Set of sentences", _options(presets), chosen["id"])
        + _text("coSentences", "Sentences, separated by semicolons", first["sentences"])
        + _select("coDrop", "Give one up", drops, "0")
        + _kpis(tiles)
        + _hint("Up to 8 sentences over up to 6 sentence letters. Type ~ for not, &amp; for and, "
                "| for or, -&gt; for if-then, or use the symbols.")
    )
    script = AK_UI_JS + AK_PROP_JS + CONSISTENCY_JS + cfg_literal("COP", table) + r"""
  var CO_TILES = ['coModels', 'coVerdict', 'coMis', 'coWitness'];
  var coPresetIn = akEl('coPreset'), coIn = akEl('coSentences'), coDropIn = akEl('coDrop');
  function coRebuildDrop(keep) {
    var n = akPieces(coIn.value, ';').length, pairs = [['0', 'keep all']], i;
    for (i = 1; i <= Math.min(n, 8); i += 1) pairs.push([String(i), 'drop ' + i]);
    akOptions(coDropIn, pairs, keep);
  }
  function coRender(inst, drop) {
    var kept = [], i, j;
    for (i = 0; i < inst.trees.length; i += 1) if (i !== drop - 1) kept.push(i);
    var res = coAnalyse(inst.trees, inst.vars, kept);
    var ok = res.models.length > 0;
    akSet('coModels', res.models.length + ' of ' + res.rows);
    akSet('coVerdict', ok ? 'Consistent' : 'Inconsistent');
    akSet('coMis', res.mis.length ? coSetText(res.mis[0].idx) : 'none');
    akSet('coWitness', ok ? akEnvText(inst.vars, res.models[0]) : 'none');
    var shown = res.models.slice(0, 16), h;
    if (shown.length) {
      h = '<table class="tt"><caption>' + (res.models.length > 16 ? 'the first 16 of ' : '') + res.models.length
        + ' model' + (res.models.length === 1 ? '' : 's') + ', one per column</caption><thead><tr><th></th>';
      for (j = 0; j < shown.length; j += 1) h += '<th>m' + (j + 1) + '</th>';
      h += '</tr></thead><tbody>';
      for (i = 0; i < inst.vars.length; i += 1) {
        h += '<tr><th class="rowhead">' + akEsc(inst.vars[i]) + '</th>';
        for (j = 0; j < shown.length; j += 1) h += akCell(shown[j][inst.vars[i]]);
        h += '</tr>';
      }
      h += '</tbody></table>';
    } else {
      h = '<p class="small-copy">No assignment of the ' + res.rows + ' makes every kept sentence true.</p>';
    }
    akEl('coModelsTable').innerHTML = h;
    var list = '<table class="tt"><thead><tr><th>#</th><th>sentence</th><th>status</th></tr></thead><tbody>';
    for (i = 0; i < inst.trees.length; i += 1) {
      list += '<tr' + (i === drop - 1 ? ' class="focus"' : '') + '><td>' + (i + 1) + '</td><td>' + akEsc(akShow(inst.trees[i], true))
        + '</td><td>' + (i === drop - 1 ? 'given up' : 'kept') + '</td></tr>';
    }
    var misTexts = [];
    for (i = 0; i < res.mis.length; i += 1) misTexts.push(coSetText(res.mis[i].idx));
    list += '</tbody></table><p class="small-copy">Minimal inconsistent subsets: ' + (misTexts.length ? misTexts.join(', ') : 'none') + '.</p>';
    akEl('coMisList').innerHTML = list;
    akEl('coStatus').innerHTML = (ok
      ? '<strong>Consistent.</strong> ' + res.models.length + ' of the ' + res.rows + ' assignments make every kept sentence true; the first is <strong>'
        + akEsc(akEnvText(inst.vars, res.models[0])) + '</strong>.'
      : '<strong>Inconsistent.</strong> No assignment of the ' + res.rows + ' makes every kept sentence true. The smallest set that cannot all be true is <strong>'
        + coSetText(res.mis[0].idx) + '</strong>' + (res.mis.length > 1 ? ', one of ' + res.mis.length + ' minimal inconsistent subsets' : '')
        + '; giving up any one of its members leaves the rest of it satisfiable, and nothing here says which one to give up.')
      + ' Computed from ' + kept.length + ' kept sentence' + (kept.length === 1 ? '' : 's') + ' over ' + inst.vars.length + ' sentence letter' + (inst.vars.length === 1 ? '' : 's') + '.';
  }
  function redraw() {
    var inst;
    try {
      inst = coRead(coIn.value);
    } catch (e) {
      akRefuse('coStatus', CO_TILES, ['coModelsTable', 'coMisList'], akMsg(e)); return;
    }
    var drop = parseInt(coDropIn.value, 10);
    if (!(drop >= 1 && drop <= inst.trees.length)) drop = 0;
    coRender(inst, drop);
  }
  coPresetIn.addEventListener('change', function () {
    var p = COP[coPresetIn.value];
    if (p) coIn.value = p.sentences;
    coRebuildDrop('0');
    redraw();
  });
  coIn.addEventListener('input', function () { coRebuildDrop(coDropIn.value); redraw(); });
  coDropIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg, title="Consistency and what must go", subtitle="Every model, and every minimal inconsistent subset",
        markup=markup, controls=controls, script=script, select="coPreset", presets=presets,
        panel_title="Choose the set",
        panel_intro="A set is consistent when one assignment makes every sentence in it true. When none "
                    "does, the lab finds the smallest subsets that already fail, by trying them all.",
    )


# ---------------------------------------------------------------------------
# syllogism
# ---------------------------------------------------------------------------

_SY_RE = re.compile(r"^(all|no|some) ([a-z][a-z-]*) are (not )?([a-z][a-z-]*)$")


def _sy_terms(mode, p, text):
    s = " ".join(str(text).lower().split()).rstrip(".")
    m = _SY_RE.match(s)
    _check(mode, p, m is not None and (not m.group(3) or m.group(1) == "some"),
           "%r is not a categorical statement" % text)
    return {t[4:] if t.startswith("non-") and len(t) > 4 else t for t in (m.group(2), m.group(4))}


def _syllogism(cfg):
    mode = "syllogism"
    presets = _presets(cfg, mode)
    table = {}
    for p in presets:
        prem = p.get("premises")
        _check(mode, p, isinstance(prem, list) and 1 <= len(prem) <= 2
               and all(isinstance(x, str) and x.strip() for x in prem), "one or two premises")
        conc = p.get("conclusion")
        _check(mode, p, isinstance(conc, str) and conc.strip(), "the conclusion is empty")
        terms = set()
        for x in prem + [conc]:
            terms |= _sy_terms(mode, p, x)
        _check(mode, p, len(terms) <= 3, "more than 3 terms: %s" % ", ".join(sorted(terms)))
        table[str(p["id"])] = {"p1": prem[0], "p2": prem[1] if len(prem) > 1 else "", "c": conc}
    chosen = _chosen(presets, cfg, mode)
    reading = _choice(cfg, "import", ["boolean", "aristotelian"], mode)
    first = table[str(chosen["id"])]
    tiles = [("Verdict", "syVerdict"), ("Form", "syForm"),
             ("Patterns the premises allow", "syModels"), ("Counterexample regions", "syCounter")]
    markup = (
        _toolbar("Regions, emptied and occupied",
                 "every pattern of empty and non-empty regions, tested",
                 [("muted", "empty"), ("red", "× occupied")])
        + _stage(_svg("sySvg", "0 0 520 320",
                      "A Venn diagram of the terms, shaded where a region is empty and marked "
                      "with a cross where it is occupied."))
        + _banner("syStatus")
    )
    controls = (
        _select("syPreset", "Argument", _options(presets), chosen["id"])
        + _text("syP1", "First premise", first["p1"])
        + _text("syP2", "Second premise (may be empty)", first["p2"])
        + _text("syC", "Conclusion", first["c"])
        + _select("syImport", "Reading", [("boolean", "Boolean: terms may be empty"),
                                          ("aristotelian", "Aristotelian: every term non-empty")], reading)
        + _kpis(tiles)
        + _hint("Write All X are Y, No X are Y, Some X are Y or Some X are not Y, with one-word terms; "
                "non-X is the complement of X.")
    )
    script = AK_UI_JS + SYLLOGISM_JS + cfg_literal("SYP", table) + r"""
  var SY_TILES = ['syVerdict', 'syForm', 'syModels', 'syCounter'];
  var syPresetIn = akEl('syPreset'), syP1 = akEl('syP1'), syP2 = akEl('syP2'), syC = akEl('syC');
  var syImportIn = akEl('syImport');
  function syRender(inst) {
    var aris = syImportIn.value === 'aristotelian';
    var res = syAnalyse(inst, aris), other = syAnalyse(inst, !aris);
    var form = syForm(inst), t = inst.terms.length, all = (1 << (1 << t)) - 1;
    akSet('syVerdict', res.valid ? 'Valid' : 'Invalid');
    akSet('syForm', form);
    akSet('syModels', res.models);
    akSet('syCounter', res.valid ? 'none' : syPatternText(res.counter, inst.terms));
    akEl('sySvg').innerHTML = res.valid ? sySvg(inst.terms, res.forcedEmpty, res.forcedFull)
                                        : sySvg(inst.terms, all & ~res.counter, res.counter);
    var name = aris ? 'Aristotelian' : 'Boolean', otherName = aris ? 'Boolean' : 'Aristotelian';
    akEl('syStatus').innerHTML = (res.valid
      ? '<strong>Valid on the ' + name + ' reading.</strong> All ' + res.models + ' patterns the premises allow make the conclusion true; the drawing shades the regions every one of them leaves empty.'
      : '<strong>Invalid on the ' + name + ' reading.</strong> Of the ' + res.models + ' patterns the premises allow, at least one makes the conclusion false; the drawing shows the smallest: <strong>'
        + akEsc(syPatternText(res.counter, inst.terms)) + '</strong>' + (res.counter ? ' occupied, every other region empty.' : '.'))
      + ' On the ' + otherName + ' reading the argument is <strong>' + (other.valid ? 'valid' : 'invalid') + '</strong>.'
      + ' Computed over all ' + (all + 1) + ' patterns of the ' + (1 << t) + ' regions of ' + t + ' term' + (t === 1 ? '' : 's') + '.';
  }
  function redraw() {
    var inst;
    try {
      inst = syRead(syP1.value, syP2.value, syC.value);
    } catch (e) {
      akRefuse('syStatus', SY_TILES, ['sySvg'], akMsg(e)); return;
    }
    syRender(inst);
  }
  syPresetIn.addEventListener('change', function () {
    var p = SYP[syPresetIn.value];
    if (p) { syP1.value = p.p1; syP2.value = p.p2; syC.value = p.c; }
    redraw();
  });
  [syP1, syP2, syC].forEach(function (el) { el.addEventListener('input', redraw); });
  syImportIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg, title="Categorical logic by regions", subtitle="Every pattern of empty and occupied regions",
        markup=markup, controls=controls, script=script, select="syPreset", presets=presets,
        panel_title="Choose the argument",
        panel_intro="Each statement says some regions are empty or some region is occupied. The lab "
                    "tries every pattern the premises allow and looks for one where the conclusion fails.",
    )


# ---------------------------------------------------------------------------
# sorites
# ---------------------------------------------------------------------------


def _sorites(cfg):
    mode = "sorites"
    presets = _presets(cfg, mode)
    table = {}
    for p in presets:
        start, end = p.get("start"), p.get("end")
        _check(mode, p, isinstance(start, int) and isinstance(end, int)
               and 0 <= end < start <= 10 ** 6, "need 0 <= end < start <= 1000000")
        cutoff = p.get("cutoff", (start + end) // 2 + 1)
        _check(mode, p, isinstance(cutoff, int) and end < cutoff <= start,
               "the cutoff must satisfy end < cutoff <= start")
        span = start - end
        rng = p.get("range", [end + span // 3, end + max(span // 3 + 1, (2 * span) // 3)])
        _check(mode, p, isinstance(rng, (list, tuple)) and len(rng) == 2
               and all(isinstance(x, int) for x in rng) and end <= rng[0] < rng[1] <= start,
               "the range must be [lo, hi] with end <= lo < hi <= start")
        pred = p.get("predicate", "F")
        _check(mode, p, isinstance(pred, str) and not any(c in pred for c in '<>&"'),
               "the predicate is display text without < > & \"")
        table[str(p["id"])] = {"start": str(start), "end": str(end), "cutoff": str(cutoff),
                               "range": "%d-%d" % (rng[0], rng[1]), "pred": pred}
    chosen = _chosen(presets, cfg, mode)
    treatment = _choice(cfg, "treatment", ["classical", "cutoff", "range", "degrees"], mode)
    first = table[str(chosen["id"])]
    tiles = [("Steps", "soSteps"), ("The conditionals", "soCond"), ("The conclusion", "soConc")]
    markup = (
        _toolbar("One chain, four treatments",
                 "F(k) → F(k−1), from the start count down to the end count",
                 [("green", "F true"), ("amber", "borderline"), ("red", "the cutoff")])
        + _stage(_svg("soStrip", "0 0 520 70",
                      "A strip from the end count to the start count, coloured where the "
                      "predicate holds under the chosen treatment."))
        + _wrap("soList")
        + _banner("soStatus")
    )
    controls = (
        _select("soPreset", "Chain", _options(presets), chosen["id"])
        + _text("soPred", "The predicate F (display only)", first["pred"])
        + _text("soStart", "Start count (the clear case)", first["start"])
        + _text("soEnd", "End count (the conclusion)", first["end"])
        + _text("soCutoff", "Cutoff (for the cutoff treatment)", first["cutoff"])
        + _text("soRange", "Borderline range lo-hi (for the range treatment)", first["range"])
        + _select("soTreat", "Treatment of vagueness",
                  [("classical", "classical: every conditional true"),
                   ("cutoff", "epistemic: one sharp cutoff"),
                   ("range", "supervaluation: a borderline range"),
                   ("degrees", "degrees of truth (Łukasiewicz)")], treatment)
        + _kpis(tiles)
    )
    script = AK_UI_JS + RATIONAL_JS + SORITES_JS + cfg_literal("SOP", table) + r"""
  var SO_TILES = ['soSteps', 'soCond', 'soConc'];
  var soPresetIn = akEl('soPreset'), soStartIn = akEl('soStart'), soEndIn = akEl('soEnd');
  var soCutIn = akEl('soCutoff'), soRangeIn = akEl('soRange'), soTreatIn = akEl('soTreat'), soPredIn = akEl('soPred');
  function soRender(inst) {
    var res = soAnalyse(inst), head = [], tail = [], k, i;
    akSet('soSteps', inst.steps);
    akSet('soCond', res.cond);
    akSet('soConc', res.conc);
    akEl('soStrip').innerHTML = soStrip(inst);
    for (k = inst.start; k > inst.end && head.length < 5; k -= 1) head.push(k);
    for (k = inst.end + 1; k < head[head.length - 1] && tail.length < 5; k += 1) tail.unshift(k);
    var h = '<table class="tt"><thead><tr><th>conditional</th><th>value</th></tr></thead><tbody>';
    for (i = 0; i < head.length; i += 1) h += '<tr><td>F(' + head[i] + ') → F(' + (head[i] - 1) + ')</td><td>' + soCondValue(head[i], inst) + '</td></tr>';
    if (tail.length && tail[0] < head[head.length - 1] - 1) h += '<tr><td colspan="2">… ' + (head[head.length - 1] - tail[0] - 1) + ' more …</td></tr>';
    for (i = 0; i < tail.length; i += 1) h += '<tr><td>F(' + tail[i] + ') → F(' + (tail[i] - 1) + ')</td><td>' + soCondValue(tail[i], inst) + '</td></tr>';
    akEl('soList').innerHTML = h + '</tbody></table>';
    var why;
    if (inst.treatment === 'classical') {
      why = 'Classically every one of the ' + inst.steps + ' conditionals is true and F(' + inst.start + ') is true, so ' + inst.steps
        + ' applications of modus ponens deliver F(' + inst.end + '): the absurd conclusion is <strong>true</strong>.';
    } else if (inst.treatment === 'cutoff') {
      why = 'With a sharp cutoff at ' + inst.cutoff + ', F(' + inst.cutoff + ') is true and F(' + (inst.cutoff - 1) + ') false, so exactly one conditional fails and the chain breaks there: F(' + inst.end + ') is <strong>false</strong>. Nobody can say where the cutoff is; this treatment says there is one.';
    } else if (inst.treatment === 'range') {
      why = 'Every admissible sharpening puts its cutoff somewhere from ' + (inst.lo + 1) + ' to ' + inst.hi + '; each makes one conditional false, so the claim that every conditional holds is <strong>super-false</strong> although no single conditional is, and F(' + inst.end + ') is false on every sharpening.';
    } else {
      why = 'With degrees, F(k) has value (k − ' + inst.end + ')/' + inst.steps + ', so each conditional has value ' + res.each
        + ' exactly: almost true. Each modus ponens loses 1/' + inst.steps + ', and after ' + inst.steps + ' steps the guaranteed value of F(' + inst.end + ') is <strong>' + res.conc + '</strong>.';
    }
    akEl('soStatus').innerHTML = 'F(k): “' + akEsc(soPredIn.value || 'F') + '”. ' + why;
  }
  function redraw() {
    var inst;
    try {
      inst = soRead(soStartIn.value, soEndIn.value, soCutIn.value, soRangeIn.value, soTreatIn.value);
    } catch (e) {
      akRefuse('soStatus', SO_TILES, ['soStrip', 'soList'], akMsg(e)); return;
    }
    soRender(inst);
  }
  soPresetIn.addEventListener('change', function () {
    var p = SOP[soPresetIn.value];
    if (p) { soStartIn.value = p.start; soEndIn.value = p.end; soCutIn.value = p.cutoff; soRangeIn.value = p.range; soPredIn.value = p.pred; }
    redraw();
  });
  [soStartIn, soEndIn, soCutIn, soRangeIn, soPredIn].forEach(function (el) { el.addEventListener('input', redraw); });
  soTreatIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg, title="The sorites, four ways", subtitle="A chain of tolerance conditionals under four treatments of vagueness",
        markup=markup, controls=controls, script=script, select="soPreset", presets=presets,
        panel_title="Choose the chain and the treatment",
        panel_intro="The chain runs from a clear case to its opposite one small step at a time. Each "
                    "treatment assigns the conditionals values, and the conclusion follows from them.",
    )


# ---------------------------------------------------------------------------
# kripke
# ---------------------------------------------------------------------------


def _kripke(cfg):
    mode = "kripke"
    presets = _presets(cfg, mode)
    table = {}
    for p in presets:
        n = p.get("n")
        _check(mode, p, isinstance(n, int) and 1 <= n <= 6, "n must be 1 to 6")
        acc = p.get("access", [])
        _check(mode, p, isinstance(acc, list) and all(
            isinstance(a, (list, tuple)) and len(a) == 2 and all(isinstance(w, int) and 1 <= w <= n for w in a)
            for a in acc), "access must be pairs of worlds 1..n")
        val = p.get("valuation", {})
        _check(mode, p, isinstance(val, dict) and all(
            _IDENT.fullmatch(str(k)) and isinstance(ws, list) and all(isinstance(w, int) and 1 <= w <= n for w in ws)
            for k, ws in val.items()), "valuation must map letters to worlds 1..n")
        f = p.get("formula")
        _check(mode, p, isinstance(f, str) and f.strip(), "the formula is empty")
        _check(mode, p, len(_atoms(f)) <= 4, "a formula over more than 4 atoms")
        table[str(p["id"])] = {
            "n": str(n),
            "access": " ".join("%d-%d" % (a, b) for a, b in acc),
            "val": "; ".join("%s: %s" % (k, " ".join(str(w) for w in ws)) for k, ws in val.items()),
            "formula": _canon(f, modal=True),
        }
    chosen = _chosen(presets, cfg, mode)
    first = table[str(chosen["id"])]
    n0 = int(first["n"])
    at = str(cfg.get("at", 1)).lstrip("w")
    if not at.isdigit() or not 1 <= int(at) <= n0:
        raise ValueError("argkit/kripke: cfg['at'] = %r is not a world of preset %r" % (cfg.get("at"), chosen["id"]))
    reading = _choice(cfg, "reading", ["alethic", "epistemic", "deontic"], mode)
    tiles = [("Value", "krValue"), ("Worlds where it holds", "krWorlds"),
             ("Frame", "krFrame"), ("Axioms valid on the frame", "krAxioms")]
    markup = (
        _toolbar("Worlds and what they can see",
                 "□ holds where every visible world agrees; ◇ where one does",
                 [("cyan", "the formula holds"), ("amber", "the world evaluated")])
        + _stage(_svg("krSvg", "0 0 520 290",
                      "The worlds as circles with arrows for accessibility; the atoms true at each "
                      "world are written inside it, and the worlds where the formula holds are filled."))
        + _banner("krStatus")
    )
    controls = (
        _select("krPreset", "Model", _options(presets), chosen["id"])
        + _range("krN", "Worlds", 1, 6, first["n"])
        + _text("krAccess", "Accessibility: 1-2 means w1 sees w2", first["access"])
        + _text("krVal", "Valuation: p: 1 2; q: 3", first["val"])
        + _text("krFormula", "Formula", first["formula"])
        + _select("krAt", "Evaluate at", [(str(i), "w%d" % i) for i in range(1, n0 + 1)], at)
        + _select("krReading", "Read the box as", [("alethic", "necessarily"), ("epistemic", "it is known that"),
                                                   ("deontic", "it is obligatory that")], reading)
        + _kpis(tiles)
        + _hint("Type [] for the box and &lt;&gt; for the diamond, or use the symbols, with ~ &amp; | -&gt; "
                "&lt;-&gt; as usual.")
    )
    script = AK_UI_JS + AK_PROP_JS + KRIPKE_JS + cfg_literal("KRP", table) + r"""
  var KR_TILES = ['krValue', 'krWorlds', 'krFrame', 'krAxioms'];
  var krPresetIn = akEl('krPreset'), krNIn = akEl('krN'), krAccIn = akEl('krAccess'), krValIn = akEl('krVal');
  var krFIn = akEl('krFormula'), krAtIn = akEl('krAt'), krReadIn = akEl('krReading');
  var KR_WORDS = {
    alethic: ['necessarily', 'possibly', 'the worlds possible relative to it'],
    epistemic: ['it is known that', 'for all that is known', 'the worlds compatible with what is known there'],
    deontic: ['it is obligatory that', 'it is permitted that', 'the worlds ideal relative to it']
  };
  function krRebuildAt() {
    var n = parseInt(krNIn.value, 10), pairs = [], i;
    if (!(n >= 1 && n <= 6)) n = 1;
    for (i = 1; i <= n; i += 1) pairs.push([String(i), 'w' + i]);
    akOptions(krAtIn, pairs, krAtIn.value);
    var out = akEl('krNOut'); if (out) out.textContent = String(n);
  }
  function krRender(inst) {
    var at = parseInt(krAtIn.value, 10) - 1;
    if (!(at >= 0 && at < inst.n)) at = 0;
    var truth = krTruth(inst.tree, inst.n, inst.succ, inst.val);
    var frame = krFrame(inst.n, inst.succ), axioms = krAxioms(inst.n, inst.succ);
    akSet('krValue', (truth[at] ? 'True' : 'False') + ' at w' + (at + 1));
    akSet('krWorlds', krWorldsText(truth));
    akSet('krFrame', frame.length ? frame.join(', ') : 'none of the five');
    akSet('krAxioms', axioms.length ? axioms.join(', ') : 'none');
    akEl('krSvg').innerHTML = krSvg(inst, truth, at);
    var words = KR_WORDS[krReadIn.value] || KR_WORDS.alethic, seen = [], i;
    for (i = 0; i < inst.succ[at].length; i += 1) seen.push('w' + (inst.succ[at][i] + 1));
    akEl('krStatus').innerHTML = '<strong>' + akEsc(akShow(inst.tree, true)) + '</strong> is <strong>' + (truth[at] ? 'true' : 'false')
      + '</strong> at w' + (at + 1) + ', which sees ' + (seen.length ? seen.join(', ') : 'no world at all') + '. Read □ as “' + words[0]
      + '” and ◇ as “' + words[1] + '”: □ quantifies over ' + words[2] + '. Computed at all ' + inst.n + ' world' + (inst.n === 1 ? '' : 's')
      + ' of this model; the axioms are checked under all ' + (1 << inst.n) + ' valuations of p on this frame.';
  }
  function redraw() {
    var inst;
    try {
      inst = krRead(krNIn.value, krAccIn.value, krValIn.value, krFIn.value);
    } catch (e) {
      akRefuse('krStatus', KR_TILES, ['krSvg'], akMsg(e)); return;
    }
    krRender(inst);
  }
  krPresetIn.addEventListener('change', function () {
    var p = KRP[krPresetIn.value];
    if (p) { krNIn.value = p.n; krAccIn.value = p.access; krValIn.value = p.val; krFIn.value = p.formula; }
    krRebuildAt();
    redraw();
  });
  krNIn.addEventListener('input', function () { krRebuildAt(); redraw(); });
  [krAccIn, krValIn, krFIn].forEach(function (el) { el.addEventListener('input', redraw); });
  krAtIn.addEventListener('change', redraw);
  krReadIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg, title="Possible worlds", subtitle="Modal formulas at every world, and the axioms the frame validates",
        markup=markup, controls=controls, script=script, select="krPreset", presets=presets,
        panel_title="Build the model",
        panel_intro="A box is true at a world when the formula is true at every world it can see; a "
                    "diamond, when it is true at one. The axioms are tested under every valuation.",
    )


# ---------------------------------------------------------------------------
# semantics
# ---------------------------------------------------------------------------


def _semantics(cfg):
    mode = "semantics"
    presets = _presets(cfg, mode)
    table = {}
    for p in presets:
        dom = p.get("domain")
        _check(mode, p, isinstance(dom, list) and 1 <= len(dom) <= 6 and len(set(dom)) == len(dom)
               and all(isinstance(d, str) and re.fullmatch("[a-w]", d) for d in dom),
               "the domain must be 1 to 6 distinct lowercase letters other than x, y, z")
        names = p.get("names", {})
        _check(mode, p, isinstance(names, dict) and all(
            re.fullmatch("[a-z][a-z0-9_]*", str(k)) and k not in ("x", "y", "z") and k not in dom and v in dom
            for k, v in names.items()), "names must map lowercase words to individuals of the domain")
        preds = p.get("predicates", {})
        _check(mode, p, isinstance(preds, dict), "predicates must be a dict")
        ext = []
        for name, items in preds.items():
            _check(mode, p, re.fullmatch("[A-Z][A-Za-z0-9_]*", str(name)) is not None,
                   "predicate %r must be a capitalised word" % name)
            _check(mode, p, isinstance(items, list), "the extension of %s must be a list" % name)
            flat = ["".join(it) if isinstance(it, (list, tuple)) else str(it) for it in items]
            _check(mode, p, all(1 <= len(it) <= 2 and all(c in dom for c in it) for it in flat)
                   and len({len(it) for it in flat}) <= 1,
                   "the extension of %s must be individuals or pairs from the domain" % name)
            ext.append("%s: %s" % (name, " ".join(flat)) if flat else "%s:" % name)
        sentence = p.get("sentence")
        _check(mode, p, isinstance(sentence, str) and sentence.strip(), "the sentence is empty")
        table[str(p["id"])] = {
            "domain": " ".join(dom), "ext": "; ".join(ext),
            "names": " ".join("%s=%s" % kv for kv in names.items()),
            "sentence": _canon(sentence),
        }
    chosen = _chosen(presets, cfg, mode)
    first = table[str(chosen["id"])]
    tiles = [("Value", "seValue"), ("Witness", "seWitness"),
             ("The description", "seDesc"), ("The outermost quantifier", "seSat")]
    markup = (
        _toolbar("A finite model",
                 "every quantifier checked against every individual",
                 [("green", "satisfies the outermost matrix"), ("red", "does not")])
        + _stage('<div class="table-wrap" id="seTable"></div>')
        + _banner("seStatus")
    )
    controls = (
        _select("sePreset", "Model and sentence", _options(presets), chosen["id"])
        + _text("seDomain", "Domain: individuals a b c", first["domain"])
        + _text("seExt", "Extensions: Planet: a b; Orbits: ab bc", first["ext"])
        + _text("seNames", "Names: h=a p=b", first["names"])
        + _text("seSentence", "Sentence", first["sentence"])
        + _kpis(tiles)
        + _hint("Quantifiers are Ax and Ex (or the symbols), variables x y z; "
                "a description is [the x: King(x)] Bald(x); connectives ~ &amp; | -&gt; &lt;-&gt;.")
    )
    script = AK_UI_JS + SEMANTICS_JS + cfg_literal("SEP", table) + r"""
  var SE_TILES = ['seValue', 'seWitness', 'seDesc', 'seSat'];
  var sePresetIn = akEl('sePreset'), seDomIn = akEl('seDomain'), seExtIn = akEl('seExt');
  var seNamesIn = akEl('seNames'), seSentIn = akEl('seSentence');
  function seRender(tree, M) {
    var res = seAnalyse(tree, M), i;
    akSet('seValue', res.value ? 'True' : 'False');
    akSet('seWitness', res.witness);
    akSet('seDesc', res.desc);
    akSet('seSat', res.satText);
    var h = '<table class="tt"><thead><tr><th>individual</th><th>named</th><th>in the extension of</th>'
      + (res.quant ? '<th>' + akEsc(seShow(res.quant.a, true)) + ', ' + res.quant.v + ' = it</th>' : '') + '</tr></thead><tbody>';
    for (i = 0; i < M.dom.length; i += 1) {
      var d = M.dom[i], named = [], inExt = [], k, key;
      for (k in M.names) if (M.names.hasOwnProperty(k) && M.names[k] === d) named.push(k);
      for (k in M.preds) {
        if (!M.preds.hasOwnProperty(k)) continue;
        for (key in M.preds[k].ext) if (M.preds[k].ext.hasOwnProperty(key) && key.indexOf(d) !== -1) inExt.push(k + '(' + key.split('').join(', ') + ')');
      }
      h += '<tr><th class="rowhead">' + d + '</th><td>' + akEsc(named.join(', ') || '–') + '</td><td>' + akEsc(inExt.join(' ') || '–') + '</td>'
        + (res.quant ? akCell(res.sat.indexOf(d) !== -1) : '') + '</tr>';
    }
    akEl('seTable').innerHTML = h + '</tbody></table>';
    var why = '<strong>' + akEsc(seShow(tree, true)) + '</strong> is <strong>' + (res.value ? 'true' : 'false') + '</strong> in this model of '
      + M.dom.length + ' individual' + (M.dom.length === 1 ? '' : 's') + '.';
    if (res.quant) {
      why += ' Its outermost quantifier, ' + (res.quant.op === 'all' ? '∀' : '∃') + res.quant.v + ', was checked at every individual: '
        + res.satText + (res.witness !== '—' ? ' (' + res.witness + ')' : '') + '.';
    }
    if (res.descNode) {
      why += ' The description “the ' + res.descNode.v + ': ' + akEsc(seShow(res.descNode.r, true)) + '” ' + res.desc
        + (res.denot.length === 1 ? '.' : ', so on Russell’s expansion “the ' + res.descNode.v + ' is …” is false whatever follows, where Strawson would say the presupposition fails.');
    }
    akEl('seStatus').innerHTML = why;
  }
  function redraw() {
    var M, tree;
    try {
      M = seReadModel(seDomIn.value, seExtIn.value, seNamesIn.value);
      tree = seParse(seSentIn.value, M);
    } catch (e) {
      akRefuse('seStatus', SE_TILES, ['seTable'], akMsg(e)); return;
    }
    seRender(tree, M);
  }
  sePresetIn.addEventListener('change', function () {
    var p = SEP[sePresetIn.value];
    if (p) { seDomIn.value = p.domain; seExtIn.value = p.ext; seNamesIn.value = p.names; seSentIn.value = p.sentence; }
    redraw();
  });
  [seDomIn, seExtIn, seNamesIn, seSentIn].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg, title="Truth in a model", subtitle="A first-order sentence evaluated over a domain you can edit",
        markup=markup, controls=controls, script=script, select="sePreset", presets=presets,
        panel_title="Build the model",
        panel_intro="A sentence is true or false only relative to a model. Change an extension and "
                    "watch the value move; descriptions are expanded the way Russell did.",
    )


# ---------------------------------------------------------------------------
# analysis
# ---------------------------------------------------------------------------


def _analysis(cfg):
    mode = "analysis"
    presets = _presets(cfg, mode)
    table = {}
    for p in presets:
        conds = p.get("conditions")
        _check(mode, p, isinstance(conds, list) and 1 <= len(conds) <= 6 and len(set(conds)) == len(conds)
               and all(isinstance(c, str) and _IDENT.fullmatch(c) for c in conds),
               "conditions must be 1 to 6 distinct letters")
        cases = p.get("cases")
        _check(mode, p, isinstance(cases, list) and 1 <= len(cases) <= 10, "1 to 10 cases")
        rows = []
        for c in cases:
            _check(mode, p, isinstance(c, dict) and isinstance(c.get("name"), str) and c["name"].strip(),
                   "every case needs a name")
            vals = c.get("values")
            _check(mode, p, isinstance(vals, list) and len(vals) == len(conds) and all(v in (0, 1) for v in vals),
                   "case %r: a row of %d values of 0 or 1" % (c.get("name"), len(conds)))
            _check(mode, p, c.get("verdict") in (0, 1), "case %r: the verdict is 0 or 1" % c.get("name"))
            rows.append({"name": c["name"], "values": [int(v) for v in vals], "verdict": int(c["verdict"])})
        d = p.get("definition")
        _check(mode, p, isinstance(d, str) and d.strip(), "the definition is empty")
        stray = [a for a in _atoms(d) if a not in conds]
        _check(mode, p, not stray, "the definition uses %s, which are not conditions" % ", ".join(stray))
        table[str(p["id"])] = {"conditions": list(conds), "cases": rows,
                               "target": str(p.get("target", "")), "definition": _canon(d)}
    chosen = _chosen(presets, cfg, mode)
    search = _choice(cfg, "search", ["off", "singles", "pairs"], mode)
    first = table[str(chosen["id"])]
    tiles = [("Agreement", "anAgree"), ("First failure", "anFail"),
             ("Verdict", "anVerdict"), ("Formulas that fit", "anCands")]
    markup = (
        _toolbar("A definition against the cases",
                 "click a value or a verdict to change the case",
                 [("green", "1 / yes"), ("red", "0 / no"), ("amber", "the definition disagrees")])
        + _stage('<div class="table-wrap" id="anTable"></div>')
        + _banner("anStatus")
    )
    controls = (
        _select("anPreset", "Case table", _options(presets), chosen["id"])
        + _text("anDef", "Definition, over the condition letters", first["definition"])
        + _select("anSearch", "Search for formulas that fit",
                  [("off", "off"), ("singles", "single conditions"), ("pairs", "up to two conditions")], search)
        + _kpis(tiles)
        + _hint("A definition is too broad when it counts a case the verdict excludes, and too narrow "
                "when it excludes a case the verdict counts.")
    )
    script = AK_UI_JS + AK_PROP_JS + ANALYSIS_JS + cfg_literal("ANP", table) + r"""
  var AN_TILES = ['anAgree', 'anFail', 'anVerdict', 'anCands'];
  var anPresetIn = akEl('anPreset'), anDefIn = akEl('anDef'), anSearchIn = akEl('anSearch');
  var anState = null;
  function anLoad(id) {
    var p = ANP[id], i;
    if (!p) return;
    anState = { conditions: p.conditions.slice(), target: p.target, cases: [] };
    for (i = 0; i < p.cases.length; i += 1) {
      anState.cases.push({ name: p.cases[i].name, values: p.cases[i].values.slice(), verdict: p.cases[i].verdict });
    }
  }
  function anRender(tree) {
    var st = anState, res = anAnalyse(tree, st.conditions, st.cases), i, j;
    var search = anSearchIn.value, cands = search === 'off' ? null : anCandidates(st.conditions, st.cases, search);
    akSet('anAgree', res.agree + ' / ' + st.cases.length);
    akSet('anFail', res.fail ? res.fail.name + ': ' + res.fail.dir : 'none');
    akSet('anVerdict', res.verdict);
    akSet('anCands', cands === null ? '—' : (cands.length ? cands.length + ': first ' + cands[0] : 'none'));
    var h = '<table class="tt"><thead><tr><th>case</th>';
    for (j = 0; j < st.conditions.length; j += 1) h += '<th>' + akEsc(st.conditions[j]) + '</th>';
    h += '<th>verdict' + (st.target ? ': ' + akEsc(st.target) : '') + '</th><th class="rowhead">' + akEsc(akShow(tree, true)) + '</th></tr></thead><tbody>';
    for (i = 0; i < st.cases.length; i += 1) {
      var c = st.cases[i], agree = res.vals[i] === (c.verdict === 1);
      h += '<tr' + (agree ? '' : ' class="focus"') + '><th class="rowhead">' + akEsc(c.name) + '</th>';
      for (j = 0; j < st.conditions.length; j += 1) {
        h += '<td class="' + (c.values[j] ? 't' : 'f') + '" data-ci="' + i + '" data-k="' + j + '" role="button" tabindex="0" style="cursor:pointer;">' + c.values[j] + '</td>';
      }
      h += '<td class="' + (c.verdict ? 't' : 'f') + '" data-ci="' + i + '" data-k="v" role="button" tabindex="0" style="cursor:pointer;">' + (c.verdict ? 'yes' : 'no') + '</td>'
        + akCell(res.vals[i]) + '</tr>';
    }
    akEl('anTable').innerHTML = h + '</tbody></table>';
    var why = '<strong>' + akEsc(akShow(tree, true)) + '</strong> agrees with the verdict in ' + res.agree + ' of ' + st.cases.length + ' cases: <strong>' + res.verdict.toLowerCase() + '</strong>.';
    if (res.fail) why += ' The first disagreement is ' + akEsc(res.fail.name) + ', where the definition ' + (res.fail.dir === 'too broad' ? 'counts a case the verdict excludes' : 'excludes a case the verdict counts') + '.';
    if (cands !== null) {
      why += cands.length ? ' Of the formulas searched, ' + cands.length + ' fit every case: ' + akEsc(cands.slice(0, 6).join(', ')) + (cands.length > 6 ? ', …' : '') + '. Fitting these cases is not yet being the definition; one new case can break it.'
                          : ' No formula searched fits every case.';
    }
    akEl('anStatus').innerHTML = why;
  }
  function redraw() {
    var tree;
    if (!anState) anLoad(anPresetIn.value);
    try {
      if (!anState) throw new Error('there is no case table for this choice');
      tree = anRead(anDefIn.value, anState.conditions);
    } catch (e) {
      akRefuse('anStatus', AN_TILES, ['anTable'], akMsg(e)); return;
    }
    anRender(tree);
  }
  function anToggle(td) {
    if (!td || !td.getAttribute || td.getAttribute('data-ci') === null || !anState) return;
    var i = parseInt(td.getAttribute('data-ci'), 10), k = td.getAttribute('data-k'), c = anState.cases[i];
    if (!c) return;
    if (k === 'v') c.verdict = c.verdict ? 0 : 1;
    else c.values[parseInt(k, 10)] = c.values[parseInt(k, 10)] ? 0 : 1;
    redraw();
  }
  function anCellOf(e) { var t = e && e.target; return t && t.closest ? t.closest('td[data-ci]') : null; }
  akEl('anTable').addEventListener('click', function (e) { anToggle(anCellOf(e)); });
  akEl('anTable').addEventListener('keydown', function (e) {
    if (e.key !== 'Enter' && e.key !== ' ') return;
    var td = anCellOf(e);
    if (td) { e.preventDefault(); anToggle(td); }
  });
  anPresetIn.addEventListener('change', function () {
    var p = ANP[anPresetIn.value];
    if (p) { anDefIn.value = p.definition; anLoad(anPresetIn.value); }
    redraw();
  });
  anDefIn.addEventListener('input', redraw);
  anSearchIn.addEventListener('change', redraw);
  anLoad(anPresetIn.value);
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg, title="The method of cases", subtitle="A definition tested against every case in the table",
        markup=markup, controls=controls, script=script, select="anPreset", presets=presets,
        panel_title="Test the definition",
        panel_intro="Each case has the conditions it meets and the verdict intuition gives. A definition "
                    "is adequate to the table when it agrees with every verdict.",
    )


# ---------------------------------------------------------------------------
# structural
# ---------------------------------------------------------------------------


def _structural(cfg):
    mode = "structural"
    presets = _presets(cfg, mode)
    table = {}
    for p in presets:
        eqs, exo = p.get("equations"), p.get("exogenous")
        _check(mode, p, isinstance(eqs, dict) and eqs and all(
            _IDENT.fullmatch(str(k)) and isinstance(v, str) and v.strip() for k, v in eqs.items()),
            "equations must map variable names to formulas")
        _check(mode, p, isinstance(exo, dict) and all(
            _IDENT.fullmatch(str(k)) and v in (0, 1) for k, v in exo.items()),
            "exogenous must map variable names to 0 or 1")
        _check(mode, p, not set(eqs) & set(exo), "a variable is both exogenous and defined")
        names = list(exo) + list(eqs)
        _check(mode, p, len(names) <= 8, "more than 8 variables")
        for k, v in eqs.items():
            stray = [a for a in _atoms(v) if a not in names]
            _check(mode, p, not stray, "the equation for %s uses undefined %s" % (k, ", ".join(stray)))
        done, progress = set(exo), True
        while progress:
            progress = False
            for k, v in eqs.items():
                if k not in done and all(a in done for a in _atoms(v)):
                    done.add(k)
                    progress = True
        _check(mode, p, len(done) == len(names), "the equations form a cycle")
        cause, effect = p.get("cause"), p.get("effect")
        _check(mode, p, cause in names and effect in names and cause != effect,
               "cause and effect must be two different variables of the model")
        table[str(p["id"])] = {
            "eqs": "; ".join("%s = %s" % (k, _canon(v)) for k, v in eqs.items()),
            "exo": " ".join("%s=%d" % kv for kv in exo.items()),
            "cause": cause, "effect": effect, "vars": names,
        }
    chosen = _chosen(presets, cfg, mode)
    first = table[str(chosen["id"])]
    var_opts = [(v, v) for v in first["vars"]]
    tiles = [("The effect, actually", "stActual"), ("But-for", "stButFor"),
             ("Halpern–Pearl", "stHP"), ("Kind", "stKind")]
    markup = (
        _toolbar("Flip the cause, recompute the world",
                 "actual values, the cause flipped, and the cause flipped with the witness held",
                 [("green", "1"), ("red", "0"), ("amber", "held at its actual value")])
        + _stage('<div class="table-wrap" id="stTable"></div>')
        + _banner("stStatus")
    )
    controls = (
        _select("stPreset", "Model", _options(presets), chosen["id"])
        + _text("stEqs", "Equations, separated by semicolons", first["eqs"])
        + _text("stExo", "Exogenous settings", first["exo"])
        + _select("stCause", "Candidate cause", var_opts, first["cause"])
        + _select("stEffect", "Effect", var_opts, first["effect"])
        + _kpis(tiles)
        + _hint("An equation is F = D &amp; ~G; settings are S1=1 G=0. A variable without an equation "
                "is exogenous and needs a setting.")
    )
    script = AK_UI_JS + AK_PROP_JS + STRUCTURAL_JS + cfg_literal("STP", table) + r"""
  var ST_TILES = ['stActual', 'stButFor', 'stHP', 'stKind'];
  var stPresetIn = akEl('stPreset'), stEqsIn = akEl('stEqs'), stExoIn = akEl('stExo');
  var stCauseIn = akEl('stCause'), stEffectIn = akEl('stEffect');
  function stRebuild(cause, effect) {
    var model, pairs = [], i;
    try { model = stRead(stEqsIn.value, stExoIn.value); } catch (e) { return; }
    for (i = 0; i < model.vars.length; i += 1) pairs.push([model.vars[i], model.vars[i]]);
    akOptions(stCauseIn, pairs, cause);
    akOptions(stEffectIn, pairs, model.vars.indexOf(effect) !== -1 ? effect : model.vars[model.vars.length - 1]);
  }
  function stBit(v) { return '<td class="' + (v ? 't' : 'f') + '">' + (v ? '1' : '0') + '</td>'; }
  function stRender(model, cause, effect) {
    var res = stAnalyse(model, cause, effect), i;
    akSet('stActual', effect + ' = ' + (res.actual[effect] ? 1 : 0));
    akSet('stButFor', res.butFor ? 'Yes' : 'No');
    akSet('stHP', res.hp);
    akSet('stKind', res.kind);
    var third = res.witness && res.witness.length ? res.held : (res.partner ? res.joint : null);
    var thirdHead = res.witness && res.witness.length ? 'flipped, {' + res.witness.join(', ') + '} held'
                  : (res.partner ? cause + ' and ' + res.partner + ' flipped' : '');
    var h = '<table class="tt"><thead><tr><th>variable</th><th>equation</th><th>actual</th><th>' + akEsc(cause) + ' flipped</th>'
      + (third ? '<th>' + akEsc(thirdHead) + '</th>' : '') + '</tr></thead><tbody>';
    for (i = 0; i < model.vars.length; i += 1) {
      var v = model.vars[i], isHeld = res.witness && res.witness.indexOf(v) !== -1;
      h += '<tr' + (v === effect ? ' class="focus"' : '') + '><th class="rowhead">' + akEsc(v) + (v === cause ? ' (cause)' : (v === effect ? ' (effect)' : '')) + '</th><td>'
        + (model.eqs.hasOwnProperty(v) ? akEsc(v + ' = ' + akShow(model.eqs[v], true)) : 'exogenous') + '</td>'
        + stBit(res.actual[v]) + stBit(res.flipped[v])
        + (third ? (isHeld ? '<td class="tone-amber">' + (third[v] ? '1' : '0') + ' held</td>' : stBit(third[v])) : '') + '</tr>';
    }
    akEl('stTable').innerHTML = h + '</tbody></table>';
    var why = 'Actually ' + akEsc(effect) + ' = ' + (res.actual[effect] ? 1 : 0) + '. Setting ' + akEsc(cause) + ' to ' + (res.actual[cause] ? 0 : 1) + ' and recomputing '
      + (res.butFor ? '<strong>changes</strong> ' + akEsc(effect) + ', so ' + akEsc(cause) + ' is a but-for cause.'
                    : 'leaves ' + akEsc(effect) + ' where it was, so ' + akEsc(cause) + ' is not a but-for cause.');
    if (!res.butFor) {
      why += res.witness ? ' Holding {' + akEsc(res.witness.join(', ')) + '} at ' + (res.witness.length === 1 ? 'its actual value' : 'their actual values') + ' and flipping ' + akEsc(cause) + ' does change it: a cause on the modified Halpern–Pearl definition, with the smallest such set chosen.'
        : (res.partner ? ' No set held fixed recovers it, but flipping ' + akEsc(cause) + ' together with ' + akEsc(res.partner) + ' changes it: a joint cause.'
                       : ' No set held fixed, and no partner flipped with it, changes it: not a cause.');
    }
    akEl('stStatus').innerHTML = why + ' Computed by re-solving the ' + model.vars.length + ' variables in dependency order for every intervention.';
  }
  function redraw() {
    var model, cause = stCauseIn.value, effect = stEffectIn.value;
    try {
      model = stRead(stEqsIn.value, stExoIn.value);
      if (model.vars.indexOf(cause) === -1) throw new Error('the candidate cause ' + cause + ' is not a variable of this model');
      if (model.vars.indexOf(effect) === -1) throw new Error('the effect ' + effect + ' is not a variable of this model');
      if (cause === effect) throw new Error('the cause and the effect must be different variables');
    } catch (e) {
      akRefuse('stStatus', ST_TILES, ['stTable'], akMsg(e)); return;
    }
    stRender(model, cause, effect);
  }
  stPresetIn.addEventListener('change', function () {
    var p = STP[stPresetIn.value];
    if (p) { stEqsIn.value = p.eqs; stExoIn.value = p.exo; stRebuild(p.cause, p.effect); }
    redraw();
  });
  [stEqsIn, stExoIn].forEach(function (el) {
    el.addEventListener('input', function () { stRebuild(stCauseIn.value, stEffectIn.value); redraw(); });
  });
  stCauseIn.addEventListener('change', redraw);
  stEffectIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg, title="Causes in a structural model", subtitle="But-for, held fixed, and joint",
        markup=markup, controls=controls, script=script, select="stPreset", presets=presets,
        panel_title="Build the model",
        panel_intro="Each endogenous variable is computed from its equation. A cause is tested by setting "
                    "it the other way and recomputing everything downstream of it.",
    )


_MODES = {
    "validity": _validity,
    "consistency": _consistency,
    "syllogism": _syllogism,
    "sorites": _sorites,
    "kripke": _kripke,
    "semantics": _semantics,
    "analysis": _analysis,
    "structural": _structural,
}

MODES = tuple(_MODES)


def argkit_lab(cfg):
    """The Philosophy argument kit. `cfg["mode"]` chooses the mode; unknown raises."""
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError("argkit_lab: unknown mode %r; the eight modes are %s"
                         % (mode, ", ".join(MODES)))
    return _MODES[mode](cfg or {})


__all__ = ["argkit_lab", "MODES"]
