// Reproduce the -s / -ing / -ed hit rates and the doubling counts with the
// JavaScript the pages ship, outside a browser.
//
//   node scripts/wordlists/verbrules_check.js [verbrules_cases.json] [doubling_verbs.json]
//
// Both arguments default to the cleaned files beside this script, which
// scripts/wordlists/clean_verbs.py writes. The forming rules and the scorer
// are read out of ENGLISH_VERB_JS in english_core.py, so this checks the code
// readers run, not a copy of it. Its figures must equal the tiles pinned on
// five-forms-and-the-whole-table and when-the-last-letter-doubles.
const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..', '..');
const core = fs.readFileSync(path.join(root, 'scripts/mathpath/labs/english_core.py'), 'utf8');
const js = core.split('ENGLISH_VERB_JS = r"""')[1].split('"""')[0];
eval(js);
const fx = JSON.parse(fs.readFileSync(process.argv[2] || path.join(__dirname, 'verbrules_cases.json'), 'utf8'));
for (const [k, v] of Object.entries(fx.stress)) VB_FINAL_STRESS[k] = v;
const rows = fx.cases.s.map(([base, s], i) => ({
  base, last: fx.stress[base], s, ing: fx.cases.ing[i][1], ed: fx.cases.ed[i][1],
}));
const rules = [
  ['-s', 's', vbThird], ['-s before the -o fix', 's', vbThirdBeforeFix],
  ['-s with f -> ves', 's', vbThirdWithVes], ['-ing', 'ing', vbIng], ['-ed', 'ed', vbEd],
];
for (const [name, slot, fn] of rules) {
  const r = vbScoreSlot(rows, slot, fn);
  console.log(`${name.padEnd(22)} ${r.hit} of ${r.total}  ${vbPct2(r.hit, r.total)}  ` +
              `missed ${r.miss.length}: ${r.miss.map((m) => m.base).join(', ')}`);
}
console.log(`excluded from the list: ${Object.keys(fx.excluded).length}`);

const db = JSON.parse(fs.readFileSync(process.argv[3] || path.join(__dirname, 'doubling_verbs.json'), 'utf8'));
const v = db.verbs, n = v.length;
const wrong = v.filter((r) => r[1] !== r[2]);
const doubles = v.filter((r) => r[2] === 1).length;
console.log(`doubling: ${n} verbs; stress rule ${n - wrong.length} right, ${wrong.length} wrong ` +
            `(${wrong.filter((r) => /l$/.test(r[0])).length} end in -l); double all ${doubles}, ` +
            `double none ${n - doubles}; excluded ${Object.keys(db.excluded).length}`);
console.log(`  wrong: ${wrong.map((r) => r[0]).join(', ')}`);
