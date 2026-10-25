"""cckit_core -- what every mode of the Code Complete kit shares.

Specified in docs/code-complete/PLAN.md section D (D.0 conventions, D.1 the
eight modes, D.2 what the kit must never do, D.3 the build-time checks). The
report an author configures a lesson from is docs/code-complete/kit-report.md.

JavaScript:

  CC_CORE_JS   shipped on every cckit page after RATIONAL_JS:
    ccInt(n)            "2,692,537", "−1" (thousands grouped, U+2212)
    ccNum(r[, places])  "11/4 = 2.75", "28/3 ≈ 9.33", "−29/15 ≈ −1.93", "4,000";
                        two places by default, half away from zero on the
                        exact value, "=" only when that decimal is exact; a
                        figure past 30 digits prints "≈ 4.63 × 10^4659"
    ccPct(r)            "33/50 = 66%", "31/60 ≈ 51.7%", "1 = 100%", "0 = 0%"
    ccRange(lo, hi)     "425–800", "35", "2/5 = 0.40 to 5"
    ccTimes, ccTimesRange  "85/7 ≈ 12.1× to 160/7 ≈ 22.9×"
    ccNames, ccCount    "a, b" / "none";  "5: a, b" / "0: none"
    ccRead(spec, raw)   parse every input of a view; THROWS a sentence
    ccTableHtml, ccListing  the table, and the numbered listing beside a code box
  CC_LEX_JS    shipped only when the mode is `code`: the tokenizer and the
               statement reader of D.1 (ccLex, ccDepths, ccHeader, ccEvents)
  CC_WIRE_JS   the page wiring (preset menu, inputs, redraw)

Python:

  parse(where, f, text)       the build-time mirror of ccRead for one field
  to_text(where, f, value)    a preset value -> the exact text its box holds
  lex(where, lines)           the build-time mirror of ccLex (D.3)
  header(lexed)               the mirror of ccHeader (D.3: a routine is needed)
  cond_vars(where, text, cmp) the mirror of the condition parser (D.3)
  build_lab(cfg, ...)         the whole Lab for one mode and view

A mode supplies one pure JS function <xx>Compute(view, inst, opts) returning
{tiles: {id: text}, status: text, table: {caption, head, rows} | null,
flags: {line: word} | undefined} or {refuse: sentence}. It is what
scripts/mathcheck.js calls.
"""

import html
import json
import re
from fractions import Fraction

from .algebra_core import RATIONAL_JS
from .common import Lab, cfg_literal

# ---------------------------------------------------------------------------
# JavaScript shared by every cckit page
# ---------------------------------------------------------------------------

CC_CORE_JS = r"""
  /* cckit's printing and parsing (docs/code-complete/PLAN.md D.0). A parse
     THROWS an Error whose message is a sentence for the reader; the wiring
     paints it red and blanks the tiles. Every figure is exact: a rational
     over BigInt, a count or a list. */
  var CC_DASH = '—', CC_MINUS = '−';
  function ccEsc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }
  function ccClean(text) { return String(text === null || text === undefined ? '' : text).replace(/\u2212/g, '-').trim(); }
  function ccGroup(digits) { return digits.replace(/\B(?=(\d{3})+$)/g, ','); }
  function ccInt(n) { n = BigInt(n); return (n < 0n ? CC_MINUS : '') + ccGroup(String(n < 0n ? -n : n)); }
  function ccFrac(r) { return (r.n < 0n ? CC_MINUS : '') + Rtext(Rabs(r)); }
  /* Exactly `places` decimals, half away from zero, on the exact value. */
  function ccFixed(r, places) {
    var neg = r.n < 0n, num = neg ? -r.n : r.n, scale = 10n ** BigInt(places);
    var q = (num * scale * 2n / r.d + 1n) / 2n, s = q.toString();
    while (s.length <= places) s = '0' + s;
    return (neg && q !== 0n ? CC_MINUS : '') + ccGroup(s.slice(0, s.length - places))
      + (places > 0 ? '.' + s.slice(s.length - places) : '');
  }
  function ccExactAt(r, places) { return (r.n * 10n ** BigInt(places)) % r.d === 0n; }
  function ccDigits(n) { return String(n < 0n ? -n : n).length; }
  function ccBig(r) { return ccDigits(r.n) > 30 || ccDigits(r.d) > 30; }
  function ccTen(k) { return k >= 0 ? R(10n ** BigInt(k)) : R(1n, 10n ** BigInt(-k)); }
  /* A figure too long to print: three significant figures and a power of ten. */
  function ccSci(r) {
    var a = Rabs(r), e = ccDigits(a.n) - ccDigits(a.d);
    if (Rcmp(a, ccTen(e)) < 0) e -= 1;
    var t = ccFixed(Rdiv(a, ccTen(e)), 2);
    if (t === '10.00') { t = '1.00'; e += 1; }
    return '≈ ' + (r.n < 0n ? CC_MINUS : '') + t + ' × 10^' + (e < 0 ? CC_MINUS + (-e) : e);
  }
  function ccNum(r, places) {
    if (places === undefined) places = 2;
    if (ccBig(r)) return ccSci(r);
    if (Rint(r)) return ccInt(r.n);
    return ccFrac(r) + (ccExactAt(r, places) ? ' = ' : ' ≈ ') + ccFixed(r, places);
  }
  function ccPct(r) {
    var p = Rmul(r, R(100n)), exact = Rint(p) || ccExactAt(p, 1);
    var d = (Rint(p) ? ccInt(p.n) : ccFixed(p, 1)) + '%';
    if (ccBig(r)) return (exact ? '= ' : '≈ ') + d;
    return ccFrac(r) + (exact ? ' = ' : ' ≈ ') + d;
  }
  /* low–high with an en dash between whole ends; "to" between others. */
  function ccRange(lo, hi) {
    if (Requ(lo, hi)) return ccNum(lo);
    if (Rint(lo) && Rint(hi) && !ccBig(lo) && !ccBig(hi)) return ccInt(lo.n) + '–' + ccInt(hi.n);
    return ccNum(lo) + ' to ' + ccNum(hi);
  }
  function ccTimes(r) { return ccNum(r, 1) + '×'; }
  function ccTimesRange(lo, hi) { return Requ(lo, hi) ? ccTimes(lo) : ccTimes(lo) + ' to ' + ccTimes(hi); }
  function ccNames(list) { return list.length ? list.join(', ') : 'none'; }
  function ccCount(list) { return list.length + ': ' + ccNames(list); }
  function ccPlural(n, one, many) { return ccInt(n) + ' ' + (BigInt(n) === 1n ? one : many); }
  function ccSum(v) { var s = R0; v.forEach(function (x) { s = Radd(s, x); }); return s; }
  function ccSort(list) { return list.slice().sort(function (a, b) { return a < b ? -1 : (a > b ? 1 : 0); }); }
  function ccBigOf(r) { return r.n / r.d; }

  /* A listing as lines: CR LF read as LF, one final newline dropped. */
  function ccSplitLines(text) {
    var t = String(text === null || text === undefined ? '' : text).replace(/\r\n?/g, '\n');
    if (t === '') return [];
    var lines = t.split('\n');
    if (lines.length > 1 && lines[lines.length - 1] === '') lines.pop();
    return lines;
  }

  var CC_NAME = /^[A-Za-z0-9._-]+$/, CC_IDENT = /^[A-Za-z_$][A-Za-z0-9_$]*$/, CC_BAD_LABEL = /[,;:<>&"=]/;
  function ccNumber(s, what) {
    if (s === '') throw new Error(what + ' is empty');
    var r = Rparse(s);
    if (r === null) throw new Error(what + ' should be a number such as 3, 1/2 or 0.25, and "' + s + '" is not one');
    return r;
  }
  function ccScalar(f, text, what) {
    var s = ccClean(text), r, toks;
    switch (f.kind) {
      case 'label':
        if (s === '') throw new Error(what + ' is empty');
        if (CC_BAD_LABEL.test(s)) throw new Error(what + ' "' + s + '" may not contain , ; : = < > & or quotes');
        return s;
      case 'name':
        if (s === '') throw new Error(what + ' is empty');
        if (!CC_NAME.test(s)) throw new Error(what + ' "' + s + '" should be letters, digits, dots, hyphens or underscores');
        return s;
      case 'word':
        if (f.words.indexOf(s) < 0) throw new Error(what + ' should be one of ' + f.words.join(', ') + ', not "' + s + '"');
        return s;
      case 'tag':
        if (s !== '' && s !== f.tag) throw new Error(what + ' should be ' + f.tag + ' or nothing, not "' + s + '"');
        return s === f.tag;
      case 'names':
      case 'idents':
        toks = s === '' ? [] : s.split(/\s+/);
        toks.forEach(function (t) {
          if (!(f.kind === 'names' ? CC_NAME : CC_IDENT).test(t)) {
            throw new Error(what + ': "' + t + '" is not ' + (f.kind === 'names' ? 'a name of letters, digits, dots, hyphens or underscores' : 'a Java name'));
          }
        });
        if (f.lo !== undefined && toks.length < f.lo) throw new Error(what + ' is empty');
        if (f.hi !== undefined && toks.length > f.hi) throw new Error(what + ' names ' + toks.length + '; this lab takes at most ' + f.hi);
        toks.forEach(function (t, i) { if (toks.indexOf(t) !== i) throw new Error(what + ' names "' + t + '" twice'); });
        return toks;
      case 'text':
        if (s === '') throw new Error(what + ' is empty');
        if (s.length > 60 || /[<>&"]/.test(s)) throw new Error(what + ' "' + s.slice(0, 60) + '" is not a number this lab can read');
        return s;
      case 'pairs':
        var out = [];
        (s === '' ? [] : s.split(';')).forEach(function (part, i, all) {
          part = part.trim();
          if (part === '' && i === all.length - 1) return;
          var m = /^([^=\s]+)\s*=\s*([^=\s]+)$/.exec(part);
          if (!m || !CC_NAME.test(m[1]) || !CC_NAME.test(m[2])) throw new Error(what + ': "' + part + '" should be name=name');
          if (out.some(function (o) { return o.a === m[1]; })) throw new Error(what + ' names "' + m[1] + '" twice');
          out.push({ a: m[1], b: m[2] });
        });
        return out;
      case 'cond':
        if (s === '') throw new Error(what + ' is empty');
        if (s.length > 300) throw new Error(what + ' has ' + s.length + ' characters; this lab reads at most 300');
        return s;
    }
    r = ccNumber(s, what);
    if (f.kind === 'pos' && Rsign(r) <= 0) throw new Error(what + ' must be more than 0, and it is ' + ccFrac(r));
    if (f.kind === 'nn' && Rsign(r) < 0) throw new Error(what + ' cannot be negative, and it is ' + ccFrac(r));
    if (f.kind === 'share' && (Rsign(r) < 0 || Rcmp(r, R1) > 0)) throw new Error(what + ' is a share from 0 to 1, and it is ' + ccFrac(r));
    if ((f.kind === 'whole' || f.kind === 'count' || f.kind === 'nncount') && !Rint(r)) throw new Error(what + ' must be a whole number, not ' + ccFrac(r));
    if (f.kind === 'count' && Rsign(r) <= 0) throw new Error(what + ' must be at least 1, not ' + ccFrac(r));
    if (f.kind === 'nncount' && Rsign(r) < 0) throw new Error(what + ' must be 0 or more, not ' + ccFrac(r));
    if (f.min !== undefined && Rcmp(r, Rparse(f.min)) < 0) throw new Error(what + ' must be at least ' + ccNum(Rparse(f.min)) + ', and it is ' + ccFrac(r));
    if (f.max !== undefined && Rcmp(r, Rparse(f.max)) > 0) throw new Error(what + ' is at most ' + ccNum(Rparse(f.max)) + ', and it is ' + ccFrac(r));
    return r;
  }
  function ccSized(n, f, what) {
    if (n < f.lo) throw new Error(what + (n === 0 ? ' is empty' : ': this lab needs at least ' + f.lo + ', and there ' + (n === 1 ? 'is 1' : 'are ' + n)));
    if (n > f.hi) throw new Error(what + ': this lab takes at most ' + f.hi + ', and there are ' + n);
  }
  function ccList(text, f, what) {
    var s = ccClean(text), parts = s === '' ? [] : s.split(/[\s,]+/).filter(function (t) { return t !== ''; });
    ccSized(parts.length, f, what);
    return parts.map(function (t, i) { return ccScalar(f.each, t, 'Entry ' + (i + 1) + ' of ' + what); });
  }
  function ccRecords(text, f, what) {
    var s = ccClean(text), rows = s === '' ? [] : s.split(';').map(function (r) { return r.trim(); });
    if (rows.length && rows[rows.length - 1] === '') rows.pop();
    ccSized(rows.length, f, what);
    var seen = {}, need = f.sub.length - (f.opt || 0);
    return rows.map(function (row, i) {
      var cells = row.split(',').map(function (c) { return c.trim(); });
      if (cells.length < need || cells.length > f.sub.length) {
        throw new Error('Entry ' + (i + 1) + ' of ' + what + ' has ' + cells.length + ' part' + (cells.length === 1 ? '' : 's')
          + '; each needs ' + (need === f.sub.length ? need : need + ' to ' + f.sub.length) + ': '
          + f.sub.map(function (k) { return k[0]; }).join(', '));
      }
      var rec = {};
      f.sub.forEach(function (k, j) {
        rec[k[0]] = j < cells.length ? ccScalar(k[1], cells[j], 'The ' + k[0] + ' in entry ' + (i + 1) + ' of ' + what)
          : ccScalar(k[1], '', 'The ' + k[0] + ' in entry ' + (i + 1) + ' of ' + what);
      });
      if (f.unique) {
        if (seen[cells[0]]) throw new Error(what + ' names "' + cells[0] + '" twice');
        seen[cells[0]] = true;
      }
      return rec;
    });
  }
  function ccCode(text, what) {
    var lines = ccSplitLines(text);
    if (lines.length > 200) throw new Error(what + ' has ' + lines.length + ' lines; this lab reads at most 200');
    lines.forEach(function (l, i) {
      if (l.length > 120) throw new Error('Line ' + (i + 1) + ' has ' + l.length + ' characters; this lab reads at most 120 a line');
    });
    return lines;
  }
  function ccField(f, text) {
    if (f.kind === 'rec') return ccRecords(text, f, f.what);
    if (f.kind === 'list') return ccList(text, f, f.what);
    if (f.kind === 'code') return ccCode(text, f.what);
    return ccScalar(f, text, f.what);
  }
  function ccRead(spec, raw) {
    var out = {};
    spec.forEach(function (f) { out[f.key] = ccField(f, raw[f.key]); });
    return out;
  }

  /* head: header texts; rows: rows of cells, each text or {t: text, c: class}. */
  function ccTableHtml(t) {
    var h = '<caption>' + ccEsc(t.caption) + '</caption><thead><tr>'
      + t.head.map(function (x) { return '<th>' + ccEsc(x) + '</th>'; }).join('') + '</tr></thead><tbody>';
    t.rows.forEach(function (row) {
      h += '<tr>' + row.map(function (cell) {
        var x = (cell && cell.t !== undefined) ? cell.t : cell, c = (cell && cell.c) ? cell.c : '';
        return '<td' + (c ? ' class="' + c + '"' : '') + '>' + ccEsc(x) + '</td>';
      }).join('') + '</tr>';
    });
    return h + '</tbody>';
  }
  /* The listing beside a code box: a gutter of line numbers drawn here, not
     selectable, so copying the listing copies no numbers. A flagged line
     carries a glyph and a visually hidden word, never colour alone (D.0). */
  var CC_GUTTER = 'display:inline-block;min-width:3.6em;box-sizing:border-box;padding-right:.55em;margin-right:.6em;'
    + 'text-align:right;border-right:1px solid var(--line);user-select:none;-webkit-user-select:none;';
  function ccListing(el, text, flags) {
    var lines = ccSplitLines(text), h = '';
    lines.forEach(function (s, i) {
      var f = flags ? flags[i + 1] : null;
      h += '<span style="' + CC_GUTTER + (f ? 'color:var(--text);font-weight:700' : 'color:var(--muted)') + '">'
        + (f ? '▸ ' : '') + (i + 1) + (f ? '<span class="visually-hidden"> ' + ccEsc(f) + '</span>' : '') + '</span>'
        + ccEsc(s) + '\n';
    });
    el.innerHTML = h || '<span style="' + CC_GUTTER + 'color:var(--muted)">0</span>(an empty listing)';
  }
  function ccFlag(flags, line, word) {
    flags[line] = flags[line] ? (flags[line].indexOf(word) < 0 ? flags[line] + ', ' + word : flags[line]) : word;
  }
"""

CC_LEX_JS = r"""
  /* The tokenizer and statement reader of D.1 (`code` mode only). It reads;
     it never runs anything. */
  function ccWords(s) { var o = {}; s.split(' ').forEach(function (w) { o[w] = true; }); return o; }
  var CC_KW = ccWords('abstract assert boolean break byte case catch char class const continue default do double else enum '
    + 'extends final finally float for goto if implements import instanceof int interface long native new null package '
    + 'private protected public return short static strictfp super switch synchronized this throw throws transient true '
    + 'false try var void volatile while');
  var CC_PRIM = ccWords('boolean byte char double float int long short void var');
  var CC_MODS = ccWords('public private protected static final abstract');
  var CC_ASSIGN = ccWords('= += -= *= /= %=');
  var CC_CONTROL = ccWords('if for while switch catch else do try synchronized return new throw case default');
  var CC_TOK = new RegExp('\\s*(?:("(?:\\\\.|[^"\\\\])*")|(\'(?:\\\\u[0-9a-fA-F]{4}|\\\\.|[^\'\\\\])\')'
    + '|(0[xX][0-9a-fA-F_]+[lL]?|0[bB][01_]+[lL]?|(?:\\d[\\d_]*\\.[\\d_]*|\\.\\d[\\d_]*)(?:[eE][+-]?\\d+)?[fFdD]?'
    + '|\\d[\\d_]*(?:[eE][+-]?\\d+)?[lLfFdD]?)|([A-Za-z_$][A-Za-z0-9_$]*)'
    + '|(->|::|\\+\\+|--|&&|\\|\\||==|!=|<=|>=|\\+=|-=|\\*=|/=|%=|&=|\\|=|\\^=|[{}()\\[\\];,.<>=!+\\-*/%?:&|^~@]))', 'y');
  var CC_KINDS = ['str', 'chr', 'num', 'id', 'op'];
  /* Comments (line and block), opaque string and character literals, tokens.
     Returns {lines} or {error: a sentence naming the line}. */
  function ccLex(src) {
    var out = [], inBlock = false;
    for (var n = 0; n < src.length; n += 1) {
      var raw = src[n], code = '', comment = false, i = 0, m;
      while (i < raw.length) {
        if (inBlock) {
          var j = raw.indexOf('*/', i);
          comment = true;
          if (j < 0) i = raw.length; else { inBlock = false; i = j + 2; code += ' '; }
          continue;
        }
        if (raw.startsWith('//', i)) { comment = true; break; }
        if (raw.startsWith('/*', i)) { inBlock = true; comment = true; i += 2; continue; }
        var c = raw.charAt(i);
        if (c === '"' || c === "'") {
          var re = c === '"' ? /"(?:\\.|[^"\\])*"/y : /'(?:\\u[0-9a-fA-F]{4}|\\.|[^'\\])'/y;
          re.lastIndex = i;
          m = re.exec(raw);
          if (!m) {
            return { error: 'Line ' + (n + 1) + ' has a ' + (c === '"' ? 'string' : 'character')
              + ' literal that does not close on that line, which this lab cannot read' };
          }
          code += m[0];
          i += m[0].length;
          continue;
        }
        code += c;
        i += 1;
      }
      var toks = [], pos = 0;
      while (pos < code.length && /\S/.test(code.slice(pos))) {
        CC_TOK.lastIndex = pos;
        m = CC_TOK.exec(code);
        if (!m) {
          return { error: 'Line ' + (n + 1) + ' has "' + code.slice(pos).trim().charAt(0)
            + '", which is outside the part of Java this lab reads' };
        }
        for (var g = 1; g <= 5; g += 1) if (m[g] !== undefined) { toks.push({ k: CC_KINDS[g - 1], v: m[g] }); break; }
        pos = CC_TOK.lastIndex;
      }
      out.push({ no: n + 1, raw: raw, code: code, comment: comment, toks: toks,
        vals: toks.map(function (t) { return t.v; }), isCode: toks.length > 0,
        braceOnly: toks.length > 0 && toks.every(function (t) { return t.v === '{' || t.v === '}' || t.v === ';'; }) });
    }
    return { lines: out };
  }
  /* Brace depth at each line's start (start), after the closing braces that
     open the line (at), and after the line (end); `bad` is the first line that
     closes a brace no earlier line opened. */
  function ccDepths(lines) {
    var d = 0, at = {}, bad = null;
    lines.forEach(function (ln) {
      var k = 0;
      while (k < ln.vals.length && ln.vals[k] === '}') k += 1;
      var row = { start: d, at: d - k };
      ln.vals.forEach(function (v) {
        if (v === '{') d += 1;
        else if (v === '}') { d -= 1; if (d < 0 && bad === null) bad = ln.no; }
      });
      if (d < 0) d = 0;
      row.end = d;
      at[ln.no] = row;
    });
    return { at: at, bad: bad };
  }
  function ccClose(v, i, open, close) {
    var depth = 0;
    for (var k = i; k < v.length; k += 1) {
      if (v[k] === open) depth += 1;
      else if (v[k] === close) { depth -= 1; if (depth === 0) return k; }
    }
    return -1;
  }
  /* split a token list at `sep` outside ( ) [ ] { } */
  function ccSplitTop(toks, sep) {
    var out = [[]], depth = 0;
    toks.forEach(function (t) {
      if (t.v === '(' || t.v === '[' || t.v === '{') depth += 1;
      else if (t.v === ')' || t.v === ']' || t.v === '}') depth -= 1;
      if (t.v === sep && depth === 0) out.push([]); else out[out.length - 1].push(t);
    });
    return out;
  }
  function ccIndexTop(toks, seps) {
    var depth = 0;
    for (var k = 0; k < toks.length; k += 1) {
      var v = toks[k].v;
      if (v === '(' || v === '[') depth += 1;
      else if (v === ')' || v === ']') depth -= 1;
      else if (depth === 0 && seps.indexOf(v) >= 0) return k;
    }
    return -1;
  }
  /* type name(parameters) [throws …] -- the shape of a routine header. */
  function ccShape(toks) {
    var v = toks.map(function (t) { return t.v; }), s = 0;
    while (v[s] === '@' && s + 1 < v.length) {
      s += 2;
      if (v[s] === '(') { var e = ccClose(v, s, '(', ')'); if (e < 0) return null; s = e + 1; }
    }
    if (s >= v.length || CC_CONTROL[v[s]]) return null;
    if (v.some(function (x) { return x === '=' || x === 'new' || x === 'class' || x === 'interface' || x === 'enum'; })) return null;
    var p = v.indexOf('(', s);
    if (p < s + 2 || toks[p - 1].k !== 'id' || CC_KW[v[p - 1]]) return null;
    if (!(toks[p - 2].k === 'id' || v[p - 2] === '>' || v[p - 2] === ']')) return null;
    var q = ccClose(v, p, '(', ')');
    if (q < 0 || (q + 1 < v.length && v[q + 1] !== 'throws')) return null;
    var params = [], cur = [], depth = 0;
    for (var k = p + 1; k < q; k += 1) {
      var x = v[k];
      if (x === '(' || x === '<' || x === '[') depth += 1;
      else if (x === ')' || x === '>' || x === ']') depth -= 1;
      if (x === ',' && depth === 0) { if (cur.length) params.push(cur); cur = []; } else cur.push(toks[k]);
    }
    if (cur.length) params.push(cur);
    return { name: v[p - 1], params: params.map(function (c) { return c[c.length - 1].v; }) };
  }
  /* The routine: the first statement at brace depth 0 that ends in { and has
     the shape of a header, joined across lines. {name, params, first, last},
     or null for a fragment. */
  function ccHeader(lines) {
    var d = 0, cur = [], first = null;
    for (var i = 0; i < lines.length; i += 1) {
      var ln = lines[i];
      for (var j = 0; j < ln.toks.length; j += 1) {
        var v = ln.toks[j].v;
        if (d > 0) { if (v === '{') d += 1; else if (v === '}') d -= 1; continue; }
        if (v === '{') {
          var h = ccShape(cur);
          if (h) { h.first = first; h.last = ln.no; return h; }
          cur = []; first = null; d = 1;
        } else if (v === ';' || v === '}') {
          cur = []; first = null;
        } else {
          if (!cur.length) first = ln.no;
          cur.push(ln.toks[j]);
        }
      }
    }
    return null;
  }
  function ccIsName(v) { return /^[a-z_]/.test(v) && !CC_KW[v]; }
  /* A variable: lower-case or _, not a keyword, not a call, not a member. */
  function ccIsVar(toks, k) {
    var t = toks[k];
    if (t.k !== 'id' || !ccIsName(t.v)) return false;
    if (k + 1 < toks.length && toks[k + 1].v === '(') return false;
    if (k > 0 && (toks[k - 1].v === '.' || toks[k - 1].v === '::')) return false;
    return true;
  }
  /* Every variable in toks is read; x++ and --x read and then set x. */
  function ccReads(toks, line, ev) {
    for (var k = 0; k < toks.length; k += 1) {
      if (!ccIsVar(toks, k)) continue;
      ev.push({ line: line, name: toks[k].v, e: 'r' });
      var nx = k + 1 < toks.length ? toks[k + 1].v : '', pv = k > 0 ? toks[k - 1].v : '';
      if (nx === '++' || nx === '--' || pv === '++' || pv === '--') ev.push({ line: line, name: toks[k].v, e: 'w' });
    }
  }
  function ccTypeEnd(toks, i) {
    if (i >= toks.length) return -1;
    var t = toks[i];
    if (!(CC_PRIM[t.v] || (t.k === 'id' && /^[A-Z]/.test(t.v)))) return -1;
    var j = i + 1;
    if (j < toks.length && toks[j].v === '<') {
      j = ccClose(toks.map(function (x) { return x.v; }), j, '<', '>');
      if (j < 0) return -1;
      j += 1;
    }
    while (j + 1 < toks.length && toks[j].v === '[' && toks[j + 1].v === ']') j += 2;
    return j;
  }
  /* One statement: a declaration (sets, or only declares, each name), an
     assignment `name op expr`, or anything else (reads every variable). */
  function ccStmt(toks, line, ev, decls, loop) {
    var s = 0;
    while (s < toks.length && CC_MODS[toks[s].v]) s += 1;
    var j = ccTypeEnd(toks, s);
    if (j > 0 && j < toks.length && toks[j].k === 'id' && !CC_KW[toks[j].v]
        && (j + 1 === toks.length || /^(=|,|;|:)$/.test(toks[j + 1].v))) {
      ccSplitTop(toks.slice(j), ',').forEach(function (p) {
        if (!p.length || p[0].k !== 'id') { ccReads(p, line, ev); return; }
        var name = p[0].v, init = p.length > 1 && p[1].v === '=';
        decls.push({ line: line, name: name, loop: !!loop });
        ccReads(p.slice(init ? 2 : 1), line, ev);
        if (ccIsName(name)) ev.push({ line: line, name: name, e: init ? 'w' : 'd' });
      });
      return;
    }
    if (toks.length > 1 && CC_ASSIGN[toks[1].v] && ccIsVar(toks, 0)) {
      if (toks[1].v !== '=') ev.push({ line: line, name: toks[0].v, e: 'r' });
      ccReads(toks.slice(2), line, ev);
      ev.push({ line: line, name: toks[0].v, e: 'w' });
      return;
    }
    ccReads(toks, line, ev);
  }
  /* One segment of a line (split at ; { } outside parentheses), with its
     control keywords peeled off: a condition is read; a `for` header is read
     as its three parts in order; an enhanced `for` reads its collection and
     then sets its variable. */
  function ccSegment(seg, line, ev, decls) {
    var v = seg.map(function (t) { return t.v; }), i = 0, q;
    while (i < seg.length) {
      var w = v[i];
      if (w === 'else' || w === 'do' || w === 'try' || w === 'finally') { i += 1; continue; }
      if ((w === 'if' || w === 'while' || w === 'switch' || w === 'catch' || w === 'synchronized') && v[i + 1] === '(') {
        q = ccClose(v, i + 1, '(', ')');
        if (q < 0) q = seg.length;
        if (w !== 'catch') ccReads(seg.slice(i + 2, q), line, ev);
        i = q + 1;
        continue;
      }
      if (w === 'for' && v[i + 1] === '(') {
        q = ccClose(v, i + 1, '(', ')');
        if (q < 0) q = seg.length;
        var inner = seg.slice(i + 2, q), parts = ccSplitTop(inner, ';'), c = ccIndexTop(inner, [':']);
        if (parts.length === 1 && c >= 0) {
          ccReads(inner.slice(c + 1), line, ev);
          var each = inner.slice(0, c), s = 0;
          while (s < each.length && CC_MODS[each[s].v]) s += 1;
          var j = ccTypeEnd(each, s);
          if (j > 0 && j === each.length - 1 && each[j].k === 'id') {
            decls.push({ line: line, name: each[j].v, loop: true });
            if (ccIsName(each[j].v)) ev.push({ line: line, name: each[j].v, e: 'w' });
          } else ccReads(each, line, ev);
        } else {
          if (parts[0] && parts[0].length) ccStmt(parts[0], line, ev, decls, true);
          if (parts[1]) ccReads(parts[1], line, ev);
          if (parts[2]) ccSplitTop(parts[2], ',').forEach(function (p) { if (p.length) ccStmt(p, line, ev, decls); });
        }
        i = q + 1;
        continue;
      }
      if (w === 'case') {
        var col = ccIndexTop(seg.slice(i), [':', '->']);
        ccReads(seg.slice(i + 1, col < 0 ? seg.length : i + col), line, ev);
        i = col < 0 ? seg.length : i + col + 1;
        continue;
      }
      if (w === 'default' && (v[i + 1] === ':' || v[i + 1] === '->')) { i += 2; continue; }
      if (w === 'return' || w === 'throw' || w === 'assert') { ccReads(seg.slice(i + 1), line, ev); return; }
      if (w === 'break' || w === 'continue') return;
      break;
    }
    if (i < seg.length) ccStmt(seg.slice(i), line, ev, decls);
  }
  function ccSegments(toks) {
    var out = [], cur = [], depth = 0;
    toks.forEach(function (t) {
      if (t.v === '(' || t.v === '[') depth += 1;
      else if (t.v === ')' || t.v === ']') depth -= 1;
      if (depth <= 0 && (t.v === ';' || t.v === '{' || t.v === '}')) { if (cur.length) out.push(cur); cur = []; }
      else cur.push(t);
    });
    if (cur.length) out.push(cur);
    return out;
  }
  /* Every read (r), set (w), bare declaration (d) and parameter (p), in line
     order, and every declared name. Parameters are set at the header's line. */
  function ccEvents(L) {
    var ev = [], decls = [], H = L.header;
    L.lines.forEach(function (ln) {
      if (!ln.isCode) return;
      if (H && ln.no >= H.first && ln.no <= H.last) {
        if (ln.no === H.first) {
          H.params.forEach(function (p) {
            decls.push({ line: ln.no, name: p, loop: false });
            if (ccIsName(p)) ev.push({ line: ln.no, name: p, e: 'p' });
          });
        }
        return;
      }
      ccSegments(ln.toks).forEach(function (seg) { ccSegment(seg, ln.no, ev, decls); });
    });
    return { ev: ev, decls: decls };
  }
  /* A listing read: {lines, depth, header} or {refuse}. */
  function ccReadCode(src) {
    var L = ccLex(src);
    if (L.error) return { refuse: L.error };
    var D = ccDepths(L.lines);
    if (D.bad !== null) return { refuse: 'Line ' + D.bad + ' closes a brace that no earlier line opened' };
    L.depth = D.at;
    L.header = ccHeader(L.lines);
    return L;
  }
"""

# The wiring every cckit page shares. %P% is the prefix, %FN% the mode's pure
# function. The code boxes ship empty (D.0: no attribute or text content
# carries code); the preset fills them here, at load and on a preset change.
CC_WIRE_JS = r"""
  function field(id) { return document.getElementById(id); }
  var presetS = field('%P%Preset'), statusEl = field('%P%Status'), tableEl = field('%P%Table');
  var listEl = LISTING ? field('%P%Listing') : null;
  function ccRed(why) {
    TILES.forEach(function (id) { field(id).textContent = CC_DASH; });
    tableEl.innerHTML = '';
    statusEl.innerHTML = '<span class="tone-red">' + ccEsc(String(why).replace(/\.$/, '')) + '.</span>';
  }
  function redraw() {
    var raw = {}, inst;
    SPEC.forEach(function (f) { raw[f.key] = field(f.id).value; });
    if (listEl) ccListing(listEl, raw[LISTING], null);
    try { inst = ccRead(SPEC, raw); } catch (err) { ccRed(err.message); return; }
    var out = %FN%(VIEW, inst, FIXED);
    if (out.refuse) { ccRed(out.refuse); return; }
    if (listEl && out.flags) ccListing(listEl, raw[LISTING], out.flags);
    TILES.forEach(function (id) { field(id).textContent = out.tiles[id] === undefined ? CC_DASH : out.tiles[id]; });
    tableEl.innerHTML = out.table ? ccTableHtml(out.table) : '';
    statusEl.textContent = out.status;
  }
  function ccFill(id) {
    var inst = PRESETS[id];
    if (!inst) return false;
    SPEC.forEach(function (f) { if (inst[f.key] !== undefined) field(f.id).value = inst[f.key]; });
    return true;
  }
  presetS.addEventListener('change', function () { if (ccFill(presetS.value)) redraw(); });
  SPEC.forEach(function (f) { field(f.id).addEventListener('input', redraw); });
  ccFill(presetS.value);
  redraw();
  window.redrawLab = redraw;
"""

# ---------------------------------------------------------------------------
# Python: the build-time mirror of ccRead and ccLex
# ---------------------------------------------------------------------------

_NAME = re.compile(r"^[A-Za-z0-9._-]+$")
_IDENT = re.compile(r"^[A-Za-z_$][A-Za-z0-9_$]*$")
_BAD_LABEL = re.compile(r'[,;:<>&"=]')


def rparse(text):
    """Rparse: "3", "-7/4", "0.25" -> Fraction; anything else (1/0 too) -> None."""
    s = str(text).strip().replace("\u2212", "-")
    m = re.fullmatch(r"([+-]?\d+)\s*/\s*(\d+)", s)
    if m:
        return None if int(m.group(2)) == 0 else Fraction(int(m.group(1)), int(m.group(2)))
    if re.fullmatch(r"[+-]?\d+", s):
        return Fraction(int(s))
    if re.fullmatch(r"[+-]?\d*\.\d+", s):
        return Fraction(s)
    return None


def ftext(f):
    """A Fraction as a box holds it: "3", "85/2", "-1"."""
    f = Fraction(f)
    return str(f.numerator) if f.denominator == 1 else "%d/%d" % (f.numerator, f.denominator)


def split_lines(text):
    t = str(text).replace("\r\n", "\n").replace("\r", "\n")
    if t == "":
        return []
    lines = t.split("\n")
    if len(lines) > 1 and lines[-1] == "":
        lines.pop()
    return lines


def parse_scalar(where, f, text, what):
    s = str(text).replace("\u2212", "-").strip()
    k = f["kind"]
    if k == "label":
        if not s or _BAD_LABEL.search(s):
            raise ValueError("%s: %s %r is empty or contains , ; : = < > & or quotes" % (where, what, s))
        return s
    if k == "name":
        if not _NAME.match(s):
            raise ValueError("%s: %s %r should be letters, digits, dots, hyphens or underscores" % (where, what, s))
        return s
    if k == "word":
        if s not in f["words"]:
            raise ValueError("%s: %s should be one of %s, not %r" % (where, what, ", ".join(f["words"]), s))
        return s
    if k == "tag":
        if s not in ("", f["tag"]):
            raise ValueError("%s: %s should be %s or nothing, not %r" % (where, what, f["tag"], s))
        return s == f["tag"]
    if k in ("names", "idents"):
        toks = s.split() if s else []
        rx = _NAME if k == "names" else _IDENT
        for t in toks:
            if not rx.match(t):
                raise ValueError("%s: %s: %r is not a usable name" % (where, what, t))
        if len(set(toks)) != len(toks):
            raise ValueError("%s: %s names something twice" % (where, what))
        if len(toks) < f.get("lo", 0) or len(toks) > f.get("hi", 10 ** 9):
            raise ValueError("%s: %s has %d names; this lab takes %s to %s"
                             % (where, what, len(toks), f.get("lo", 0), f.get("hi")))
        return toks
    if k == "text":
        if not s or len(s) > 60 or re.search(r'[<>&"]', s):
            raise ValueError("%s: %s %r is not usable" % (where, what, s))
        return s
    if k == "pairs":
        out = {}
        for i, part in enumerate(s.split(";") if s else []):
            part = part.strip()
            if not part and i == len(s.split(";")) - 1:
                continue
            m = re.fullmatch(r"([^=\s]+)\s*=\s*([^=\s]+)", part)
            if not m or not _NAME.match(m.group(1)) or not _NAME.match(m.group(2)) or m.group(1) in out:
                raise ValueError("%s: %s: %r should be name=name, each name once" % (where, what, part))
            out[m.group(1)] = m.group(2)
        return out
    if k == "cond":
        if not s or len(s) > 300:
            raise ValueError("%s: %s is empty or longer than 300 characters" % (where, what))
        return s
    if not s:
        raise ValueError("%s: %s is empty" % (where, what))
    r = rparse(s)
    if r is None:
        raise ValueError("%s: %s should be a number, not %r" % (where, what, s))
    bad = ((k == "pos" and r <= 0) or (k == "nn" and r < 0) or (k == "share" and not 0 <= r <= 1)
           or (k in ("whole", "count", "nncount") and r.denominator != 1)
           or (k == "count" and r < 1) or (k == "nncount" and r < 0)
           or ("min" in f and r < rparse(f["min"])) or ("max" in f and r > rparse(f["max"])))
    if bad:
        raise ValueError("%s: %s is %s, which this field refuses (%s)" % (where, what, s, k))
    if k not in ("num", "pos", "nn", "share", "whole", "count", "nncount"):
        raise ValueError("%s: unknown field kind %r" % (where, k))
    return r


def _sized(where, n, f, what):
    if not f["lo"] <= n <= f["hi"]:
        raise ValueError("%s: %s has %d entries; this lab takes %d to %d" % (where, what, n, f["lo"], f["hi"]))


def parse(where, f, text):
    """Mirror of ccField for one field, at build time."""
    what = f["what"]
    if f["kind"] == "code":
        lines = split_lines(text)
        if len(lines) > 200 or any(len(x) > 120 for x in lines):
            raise ValueError("%s: %s is past 200 lines or 120 characters a line" % (where, what))
        return lines
    s = str(text).replace("\u2212", "-").strip()
    if f["kind"] == "list":
        parts = [t for t in re.split(r"[\s,]+", s) if t] if s else []
        _sized(where, len(parts), f, what)
        return [parse_scalar(where, f["each"], t, "entry %d of %s" % (i + 1, what)) for i, t in enumerate(parts)]
    if f["kind"] == "rec":
        rows = [r.strip() for r in s.split(";")] if s else []
        if rows and rows[-1] == "":
            rows.pop()
        _sized(where, len(rows), f, what)
        need = len(f["sub"]) - f.get("opt", 0)
        out, seen = [], set()
        for i, row in enumerate(rows):
            cells = [c.strip() for c in row.split(",")]
            if not need <= len(cells) <= len(f["sub"]):
                raise ValueError("%s: entry %d of %s has %d parts; it needs %s"
                                 % (where, i + 1, what, len(cells), ", ".join(k for k, _ in f["sub"])))
            rec = {}
            for j, (key, kk) in enumerate(f["sub"]):
                rec[key] = parse_scalar(where, kk, cells[j] if j < len(cells) else "",
                                        "%s of entry %d of %s" % (key, i + 1, what))
            if f.get("unique"):
                if cells[0] in seen:
                    raise ValueError("%s: %s names %r twice" % (where, what, cells[0]))
                seen.add(cells[0])
            out.append(rec)
        return out
    return parse_scalar(where, f, s, what)


def _part_text(v):
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, (int, Fraction)):
        return ftext(v)
    if isinstance(v, float):
        return repr(v)
    if isinstance(v, (list, tuple)):
        return " ".join(_part_text(x) for x in v)
    return str(v)


def to_text(where, f, value):
    """A preset's value for one field -> the exact text its box holds.

    A string is taken as typed (code keeps its indentation). A number or
    Fraction prints reduced. A list field takes a list of items; a record field
    takes a list of records, each a list/tuple of parts or a string.
    """
    if f["kind"] == "code":
        if not isinstance(value, str):
            raise ValueError("%s: %s must be a string of Java" % (where, f["what"]))
        text = value.replace("\r\n", "\n")
        if text.endswith("\n"):
            text = text[:-1]
    elif isinstance(value, str):
        text = value.strip()
    elif f["kind"] in ("list", "names", "idents") and isinstance(value, (list, tuple)):
        text = " ".join(_part_text(v) for v in value)
    elif f["kind"] == "rec" and isinstance(value, (list, tuple)):
        rows = []
        for rec in value:
            if isinstance(rec, str):
                rows.append(rec.strip())
            elif isinstance(rec, (list, tuple)):
                rows.append(", ".join(_part_text(p) for p in rec))
            else:
                raise ValueError("%s: %s: each record is a list of parts or a string, not %r" % (where, f["what"], rec))
        text = "; ".join(rows)
    elif isinstance(value, (bool, int, Fraction, float)):
        text = _part_text(value)
    else:
        raise ValueError("%s: %s cannot be %r" % (where, f["what"], value))
    if f["kind"] not in ("code", "cond") and ("<" in text or ">" in text or "&" in text):
        raise ValueError("%s: %s %r contains < > or &, which no shipped value may" % (where, f["what"], text))
    parse(where, f, text)
    return text


# --- the tokenizer, mirrored (D.3) -------------------------------------------

KEYWORDS = set("""abstract assert boolean break byte case catch char class const continue default do double else enum
extends final finally float for goto if implements import instanceof int interface long native new null package
private protected public return short static strictfp super switch synchronized this throw throws transient true
false try var void volatile while""".split())
_CONTROL = set("if for while switch catch else do try synchronized return new throw case default".split())
_TOK = re.compile(r"""\s*(?:(?P<str>"(?:\\.|[^"\\])*")|(?P<chr>'(?:\\u[0-9a-fA-F]{4}|\\.|[^'\\])')"""
                  r"""|(?P<num>0[xX][0-9a-fA-F_]+[lL]?|0[bB][01_]+[lL]?|(?:\d[\d_]*\.[\d_]*|\.\d[\d_]*)(?:[eE][+-]?\d+)?[fFdD]?"""
                  r"""|\d[\d_]*(?:[eE][+-]?\d+)?[lLfFdD]?)|(?P<id>[A-Za-z_$][A-Za-z0-9_$]*)"""
                  r"""|(?P<op>->|::|\+\+|--|&&|\|\||==|!=|<=|>=|\+=|-=|\*=|/=|%=|&=|\|=|\^=|[{}()\[\];,.<>=!+\-*/%?:&|^~@]))""")


def lex(where, lines):
    """Mirror of ccLex: [(line no, [(kind, text)])], or ValueError naming the line."""
    out, in_block = [], False
    for no, raw in enumerate(lines, 1):
        code, i = "", 0
        while i < len(raw):
            if in_block:
                j = raw.find("*/", i)
                if j < 0:
                    i = len(raw)
                else:
                    in_block, i = False, j + 2
                    code += " "
                continue
            if raw.startswith("//", i):
                break
            if raw.startswith("/*", i):
                in_block, i = True, i + 2
                continue
            c = raw[i]
            if c in "\"'":
                m = re.compile(r'"(?:\\.|[^"\\])*"' if c == '"' else r"'(?:\\u[0-9a-fA-F]{4}|\\.|[^'\\])'").match(raw, i)
                if not m:
                    raise ValueError("%s: line %d has a literal that does not close on that line" % (where, no))
                code += m.group(0)
                i = m.end()
                continue
            code += c
            i += 1
        toks, pos = [], 0
        while pos < len(code) and code[pos:].strip():
            m = _TOK.match(code, pos)
            if not m:
                raise ValueError("%s: line %d has %r, outside the Java this lab reads" % (where, no, code[pos:].strip()[:1]))
            toks.append((m.lastgroup, m.group(m.lastgroup)))
            pos = m.end()
        out.append((no, toks))
    depth = 0
    for no, toks in out:
        for _k, v in toks:
            depth += (v == "{") - (v == "}")
            if depth < 0:
                raise ValueError("%s: line %d closes a brace that no earlier line opened" % (where, no))
    return out


def _close(v, i, op, cl):
    depth = 0
    for k in range(i, len(v)):
        if v[k] == op:
            depth += 1
        elif v[k] == cl:
            depth -= 1
            if depth == 0:
                return k
    return -1


def _shape(toks):
    v = [t for _k, t in toks]
    s = 0
    while s + 1 < len(v) and v[s] == "@":
        s += 2
        if s < len(v) and v[s] == "(":
            e = _close(v, s, "(", ")")
            if e < 0:
                return None
            s = e + 1
    if s >= len(v) or v[s] in _CONTROL or any(x in ("=", "new", "class", "interface", "enum") for x in v):
        return None
    p = v.index("(", s) if "(" in v[s:] else -1
    if p < s + 2 or toks[p - 1][0] != "id" or v[p - 1] in KEYWORDS:
        return None
    if not (toks[p - 2][0] == "id" or v[p - 2] in (">", "]")):
        return None
    q = _close(v, p, "(", ")")
    if q < 0 or (q + 1 < len(v) and v[q + 1] != "throws"):
        return None
    return v[p - 1]


def header(lexed):
    """Mirror of ccHeader: the routine's name, or None for a fragment."""
    d, cur = 0, []
    for _no, toks in lexed:
        for t in toks:
            v = t[1]
            if d > 0:
                d += (v == "{") - (v == "}")
                continue
            if v == "{":
                name = _shape(cur)
                if name:
                    return name
                cur, d = [], 1
            elif v in (";", "}"):
                cur = []
            else:
                cur.append(t)
    return None


# --- conditions, mirrored (D.3) ---------------------------------------------

_CTOK = re.compile(r"\s*(?:(\d+)|([A-Za-z_][A-Za-z0-9_]*)|(&&|\|\||<=|>=|==|!=|[!()<>-]))")


def cond_vars(where, text, cmp):
    """Mirror of the cond parser: the variables, in order; ValueError if it does not parse."""
    toks, pos, s = [], 0, text.strip()
    while pos < len(s):
        m = _CTOK.match(s, pos)
        if not m or m.end() == pos:
            raise ValueError("%s: the condition %r has %r, which this lab cannot read" % (where, text, s[pos:].strip()[:1]))
        toks.append(("n", m.group(1)) if m.group(1) else ("i", m.group(2)) if m.group(2) else ("o", m.group(3)))
        pos = m.end()
        if not s[pos:].strip():
            break
    seen = []
    k = [0]

    def peek():
        return toks[k[0]] if k[0] < len(toks) else (None, None)

    def take():
        t = peek()
        k[0] += 1
        return t

    def operand():
        t = take()
        if t[1] == "-":
            t2 = take()
            if t2[0] != "n":
                raise ValueError("%s: %r: a minus sign must come before a whole number" % (where, text))
            return ("n", "-" + t2[1])
        if t[0] in ("n", "i") and t[1] not in ("true", "false"):
            return t
        raise ValueError("%s: %r does not parse" % (where, text))

    def atom():
        t = peek()
        if t[1] == "(":
            take()
            disj()
            if take()[1] != ")":
                raise ValueError("%s: %r has a parenthesis that does not close" % (where, text))
            return
        if t[1] in ("true", "false"):
            take()
            return
        if cmp:
            a = operand()
            op = take()
            if op[1] not in ("<", "<=", ">", ">=", "==", "!="):
                raise ValueError("%s: %r: a range check compares the variable with a whole number" % (where, text))
            b = operand()
            names = [x[1] for x in (a, b) if x[0] == "i"]
            if len(names) != 1:
                raise ValueError("%s: %r: each comparison is between the variable and a whole number" % (where, text))
            if names[0] not in seen:
                seen.append(names[0])
            return
        if t[0] == "i":
            take()
            if t[1] not in seen:
                seen.append(t[1])
            return
        raise ValueError("%s: %r does not parse at %r" % (where, text, t[1]))

    def neg():
        if peek()[1] == "!":
            take()
            if cmp and peek()[1] not in ("!", "(", "true", "false"):
                raise ValueError("%s: %r negates a number; put the comparison in parentheses" % (where, text))
            neg()
        else:
            atom()

    def conj():
        neg()
        while peek()[1] == "&&":
            take()
            neg()

    def disj():
        conj()
        while peek()[1] == "||":
            take()
            conj()

    disj()
    if k[0] != len(toks):
        raise ValueError("%s: %r has text after the condition ends" % (where, text))
    return seen


# ---------------------------------------------------------------------------
# Presets and the Lab
# ---------------------------------------------------------------------------


def presets(cfg, kit, fields, tiles):
    """(instance table, menu pairs, expect by preset id, the chosen id).

    fields: [(key, spec, default)]. A field's default may be overridden by a
    cfg key of the same name (a lesson's fixed instance -- the late-fee table,
    the build graph -- with presets varying the rest). A preset key that is not
    an input of the view raises; so does an expectation naming a tile the view
    does not show.
    """
    plist = cfg.get("presets")
    if not isinstance(plist, list) or not plist:
        raise ValueError("%s: cfg['presets'] must be a non-empty list of instances" % kit)
    known = {key for key, _s, _d in fields} | {"id", "label", "note", "expect"}
    tile_ids = {cid for _l, cid in tiles}
    table, menu, expect = {}, [], {}
    for p in plist:
        pid = p.get("id") if isinstance(p, dict) else None
        if not isinstance(pid, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", pid):
            raise ValueError("%s: every preset needs an id of lowercase letters, digits and hyphens, not %r" % (kit, pid))
        where = "%s preset %r" % (kit, pid)
        if pid in table:
            raise ValueError("%s: the id is used twice" % where)
        label = p.get("label")
        if not isinstance(label, str) or not label.strip() or re.search(r"[<>&]", label):
            raise ValueError("%s: needs a plain-text label" % where)
        extra = sorted(set(p) - known)
        if extra:
            raise ValueError("%s: %s %s not an input of this view (it shows %s)"
                             % (where, ", ".join(extra), "is" if len(extra) == 1 else "are",
                                ", ".join(k for k, _s, _d in fields)))
        exp = p.get("expect") or {}
        if not isinstance(exp, dict) or any(k not in tile_ids or not isinstance(v, str) for k, v in exp.items()):
            raise ValueError("%s: expect maps this view's tile ids (%s) to the exact text printed"
                             % (where, ", ".join(sorted(tile_ids))))
        inst = {}
        for key, spec, default in fields:
            value = p.get(key, cfg.get(key, default))
            if value is None:
                raise ValueError("%s: needs %s" % (where, key))
            inst[key] = to_text(where, spec, value)
        table[pid] = inst
        menu.append((pid, label.strip()))
        expect[pid] = dict(exp)
    chosen = cfg.get("preset", plist[0]["id"])
    if chosen not in table:
        raise ValueError("%s: cfg['preset'] %r is not one of the presets (%s)" % (kit, chosen, ", ".join(table)))
    return table, menu, expect, chosen


def plain(cfg, kit, key, default, limit=200):
    """A lesson-level text value: plain, short, no markup."""
    v = cfg.get(key, default)
    if not isinstance(v, str) or re.search(r"[<>&]", v) or len(v) > limit:
        raise ValueError("%s: cfg[%r] should be plain text of at most %d characters, not %r" % (kit, key, limit, v))
    return v


def attr(text):
    return html.escape(str(text), quote=True)


def esc(text):
    return html.escape(str(text), quote=False)


def camel(prefix, key):
    """An input's id: prefix + 'In' + CamelKey ('co', 'code' -> 'coInCode'; 'pj', 'perWeek' -> 'pjInPerWeek')."""
    return prefix + "In" + "".join(part[:1].upper() + part[1:] for part in key.split("_"))


def select_html(cid, label, options, chosen):
    opts = "".join('<option value="%s"%s>%s</option>' % (attr(v), " selected" if v == chosen else "", esc(t))
                   for v, t in options)
    return ('        <div class="field">\n          <label for="%s">%s</label>\n'
            '          <select id="%s">%s</select>\n        </div>\n' % (cid, esc(label), cid, opts))


def text_html(cid, label, value):
    return ('        <div class="field">\n          <label for="%s">%s</label>\n'
            '          <input id="%s" type="text" value="%s" inputmode="text" autocomplete="off" spellcheck="false">\n'
            "        </div>\n" % (cid, esc(label), cid, attr(value)))


_MONO = "font-family:var(--mono);font-size:0.85rem;line-height:1.5;"


def area_html(cid, label, rows):
    """A condition box: empty in the markup, filled by script (D.0)."""
    return ('        <div class="field">\n          <label for="%s">%s</label>\n'
            '          <textarea id="%s" rows="%d" spellcheck="false" autocomplete="off" autocapitalize="off" '
            'style="width:100%%;box-sizing:border-box;%s"></textarea>\n'
            "        </div>\n" % (cid, esc(label), cid, rows, _MONO))


def kpis_html(items):
    cells = "".join('          <div class="kpi"><span>%s</span><strong id="%s">&mdash;</strong></div>\n'
                    % (esc(label), cid) for label, cid in items)
    return '        <div class="kpi-grid">\n%s        </div>\n' % cells


def code_html(prefix, cid, label, rules):
    """The code box and its numbered listing, side by side; stacked below
    about 40em (two 19.5em columns no longer fit), each scrolling in its own
    box. The rules the view counts by are stated beneath (D.0, D.1)."""
    col = "flex:1 1 19.5em;min-width:0;"
    return ('      <div style="display:flex;flex-wrap:wrap;gap:12px;align-items:flex-start;margin-top:4px;">\n'
            '        <div style="%s">\n'
            '          <label for="%s" class="small-copy" style="display:block;margin-bottom:4px;">%s</label>\n'
            '          <textarea id="%s" rows="16" wrap="off" spellcheck="false" autocomplete="off" autocapitalize="off" '
            'style="width:100%%;box-sizing:border-box;white-space:pre;overflow:auto;tab-size:4;%s"></textarea>\n'
            "        </div>\n"
            '        <div style="%s">\n'
            '          <p class="small-copy" id="%sListingLabel" style="margin:0 0 4px;">The listing, numbered as every '
            "tile and the banner number it</p>\n"
            '          <pre id="%sListing" aria-labelledby="%sListingLabel" style="margin:0;max-height:30em;overflow:auto;'
            'white-space:pre;tab-size:4;padding:8px 10px 8px 0;border:1px solid var(--line);border-radius:9px;'
            'background:var(--panel-2);color:var(--text);%s"></pre>\n'
            "        </div>\n"
            "      </div>\n"
            '      <details style="margin-top:10px;"><summary class="small-copy">How the lab reads Java</summary>\n'
            '        <div class="small-copy">%s</div>\n'
            "      </details>\n"
            % (col, cid, esc(label), cid, _MONO, col, prefix, prefix, prefix, _MONO, rules))


def markup_html(prefix, name, subtitle, top=""):
    return ('      <div class="lab-toolbar">\n'
            '        <div class="lab-title"><strong>%s</strong><span>%s</span></div>\n'
            "      </div>\n" % (esc(name), esc(subtitle))
            + top
            + '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="%sTable"></table></div>\n'
            % prefix
            + '      <div class="status-banner" id="%sStatus" style="margin-top:12px;" aria-live="polite"></div>\n' % prefix)


FAMILY = {
    1: "A count over code, by the rules stated below the listing.",
    2: "A count over the structure the lesson states.",
    3: "The arithmetic of figures the lesson quotes (marked with their source).",
}

COMMON_CFG = {"mode", "view", "presets", "preset", "title", "panel_title", "panel_intro"}

_COMMENT_LINES = re.compile(r"^[ \t]*/\*(?:(?!\*/).)*\*/[ \t]*\n", re.S | re.M)


def build_lab(cfg, *, kit, prefix, view, fields, tiles, fn, js, fixed, title, subtitle, family, intro,
              extra_keys=(), rules=None, listing_key=None):
    """One mode, one view, as a Lab.

    fields: [(key, spec, default)] in display order; spec["what"] is the label.
            kind "code" is the code box beside its listing (in the main panel);
            kind "cond" is a condition box; the rest are text inputs. Every
            input's id is prefix + 'In' + CamelKey.
    tiles:  [(label, id)].
    fixed:  the lesson-level values handed to the compute function as opts.
    """
    allowed = COMMON_CFG | set(extra_keys) | {key for key, _s, _d in fields}
    stray = sorted(set(cfg) - allowed)
    if stray:
        raise ValueError("%s: cfg sets %s, which this view does not take (it takes %s)"
                         % (kit, ", ".join(stray), ", ".join(sorted(allowed))))
    table, menu, expect, chosen = presets(cfg, kit, fields, tiles)
    here = table[chosen]
    spec, controls, top = [], select_html(prefix + "Preset", "Worked example", menu, chosen), ""
    for key, fspec, _default in fields:
        cid = camel(prefix, key)
        spec.append(dict(fspec, key=key, id=cid))
        if fspec["kind"] == "code":
            top += code_html(prefix, cid, fspec["what"], rules or "")
        elif fspec["kind"] == "cond":
            controls += area_html(cid, fspec["what"], fspec.get("rows", 3))
        else:
            controls += text_html(cid, fspec["what"], here[key])
    controls += kpis_html(tiles)
    ids = [s["id"] for s in spec] + [cid for _l, cid in tiles]
    if len(set(ids)) != len(ids):
        raise ValueError("%s: two controls or tiles share an id: %s" % (kit, sorted(i for i in ids if ids.count(i) > 1)))
    lex_js = CC_LEX_JS if listing_key else ""
    script = (RATIONAL_JS + CC_CORE_JS + lex_js + js
              + cfg_literal("PRESETS", table) + cfg_literal("SPEC", spec)
              + cfg_literal("TILES", [cid for _label, cid in tiles])
              + cfg_literal("FIXED", fixed) + cfg_literal("VIEW", view)
              + cfg_literal("LISTING", listing_key)
              + CC_WIRE_JS.replace("%P%", prefix).replace("%FN%", fn))
    script = _COMMENT_LINES.sub("", script)
    panel_intro = plain(cfg, kit, "panel_intro", intro, limit=1200)
    if FAMILY[family] not in panel_intro:
        panel_intro = FAMILY[family] + " " + panel_intro
    title = plain(cfg, kit, "title", title)
    return Lab(title=title, subtitle=subtitle,
               markup=markup_html(prefix, title, subtitle, top), controls=controls, script=script,
               panel_title=plain(cfg, kit, "panel_title", "Change the inputs, or choose a worked example"),
               panel_intro=panel_intro, expect={prefix + "Preset": expect})


__all__ = ["CC_CORE_JS", "CC_LEX_JS", "CC_WIRE_JS", "FAMILY", "rparse", "ftext", "parse", "parse_scalar", "to_text",
           "lex", "header", "cond_vars", "split_lines", "presets", "plain", "camel", "build_lab", "esc"]
