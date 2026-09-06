#!/usr/bin/env node
/* Each mutation changes an evidence-side copy; the worktree is never mutated.
 * Success requires the intended behavioral assertion, not just a nonzero exit.
 */
'use strict';
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),{spawnSync}=require('node:child_process');
const ROOT=path.resolve(__dirname,'..'),OUT=process.env.BROWSER_EVIDENCE;
assert(OUT&&path.resolve(OUT)!==ROOT&&!path.resolve(OUT).startsWith(ROOT+'/'),'external evidence directory required');
fs.mkdirSync(OUT,{recursive:true});
const COPY=path.join(OUT,'disposable-export');assert(!fs.existsSync(COPY),'fresh mutation export required');
try {
fs.mkdirSync(COPY);
for(const dir of ['site','scripts','tests','content'])fs.cpSync(path.join(ROOT,dir),path.join(COPY,dir),{recursive:true,filter:p=>!p.includes('__pycache__')});
const preflight=path.join(OUT,'target-preflight');fs.mkdirSync(preflight);
const baseline=spawnSync(process.execPath,[path.join(ROOT,'tests/browser_acceptance.js')],{env:{...process.env,SOURCE_ROOT:COPY,BROWSER_EVIDENCE:preflight},encoding:'utf8'});
fs.writeFileSync(path.join(preflight,'command.log'),baseline.stdout+baseline.stderr);
assert.equal(baseline.status,0,'mutation baseline must be green');
for(const [name,driver,args] of [
 ['contrast-preflight','browser_contrast.js',['--capstones']],
 ['contract-preflight','browser_contract_fixtures.js',[]]]){
 const out=path.join(OUT,name);fs.mkdirSync(out);
 const run=spawnSync(process.execPath,[path.join(COPY,'tests',driver),...args],{env:{...process.env,SOURCE_ROOT:COPY,BROWSER_EVIDENCE:out},encoding:'utf8'});
 fs.writeFileSync(path.join(out,'command.log'),run.stdout+run.stderr);
 assert.equal(run.status,0,name+' mutation baseline must be green');
}
const witnesses=new Map();
for(const line of fs.readFileSync(path.join(preflight,'observations.jsonl'),'utf8').trim().split('\n')) {
 const row=JSON.parse(line);
 if(row.group==='svg'&&row.rows.some(r=>r.text.startsWith('log_10 ≈')))witnesses.set('svg:log_10',path.join(COPY,'site',row.route,'index.html'));
 if(row.group!=='targets')continue;
 for(const target of row.rows)if(!target.disabled&&!witnesses.has(target.kind))witnesses.set(target.kind,path.join(COPY,'site',row.route,'index.html'));
}
const pages=[];function walk(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){const f=path.join(dir,e.name);if(e.isDirectory())walk(f);else if(e.name.endsWith('.html'))pages.push(f);}}walk(path.join(COPY,'site'));
function select(re){const found=pages.filter(p=>re.test(fs.readFileSync(p,'utf8')));assert(found.length,'non-vacuous mutation capability '+re);return found.sort()[0];}
function route(file){return '/'+path.relative(path.join(COPY,'site'),file).replace(/index\.html$/,'');}
function replace(old,value){return source=>{assert(source.includes(old),'mutation anchor absent: '+old);return source.replace(old,value);};}
const cases=[];
function add(name,file,change,group,expected,extra=[]){cases.push({name,file,change,group,expected,extra});}
const inventory=path.join(COPY,'tests/interactive_targets.js'),core=path.join(COPY,'scripts/mathpath/labs/algebra_core.py');
add('runtime-named-process',inventory,replace("if (nodeModule && process.argv.includes('--test'))", "if (typeof process !== 'undefined' && process.argv.includes('--test'))"),'inventory','browser named-global collision');
add('runtime-named-module',inventory,replace('if (nodeModule) module.exports = api;',"if (typeof module !== 'undefined') module.exports = api;"),'inventory','named module was treated as CommonJS');
add('file-label-owner',inventory,replace("['checkbox', 'radio', 'file']","['checkbox', 'radio']"),'inventory','associated label owner missing');
add('checkbox-radio-owners',inventory,replace("['checkbox', 'radio', 'file']","['file']"),'inventory','associated label owner missing');
add('empty-inventory',inventory,replace('Array.from(scope.querySelectorAll(SELECTOR)', 'Array.from([]'),'inventory','non-vacuous fixture inventory');
add('cached-dynamic-inventory',inventory,replace('scope.querySelectorAll(SELECTOR)', '(root.cachedControls ||= scope.querySelectorAll(SELECTOR))'),'inventory','dynamic control omitted');
add('dangling-label-policy',inventory,replace('Array.from(control.labels || [])',"Array.from(document.querySelectorAll('label'))"),'inventory','dangling label claimed');
for(const [name,old,value] of [
 ['left-edge','bounds[0] + gap - b.x','-Infinity'],['right-edge','bounds[2] - gap - b.x - b.width','Infinity'],
 ['top-edge','bounds[1] + gap - b.y','-Infinity'],['bottom-edge','bounds[3] - gap - b.y - b.height','Infinity'],
 ['long-annotation','t.remove(); return null;','return null;'],
 ['invisible-annotation','t.textContent = text;','t.textContent = text; t.style.opacity = "0";'],
 ['offscale-annotation','x >= xmin && x <= xmax && y >= ymin && y <= ymax','true'],
 ['x-grid-overshoot','v = start; v <= xmax;','v = start; v <= xmax + gx / 2;'],
 ['y-grid-overshoot','v = start; v <= ymax;','v = start; v <= ymax + gy / 2;'],
 ['x-tick-overshoot','v = Math.ceil(xmin / gx) * gx; v <= xmax;','v = Math.ceil(xmin / gx) * gx; v <= xmax + gx / 2;'],
 ['y-tick-overshoot','v = Math.ceil(ymin / gy) * gy; v <= ymax;','v = Math.ceil(ymin / gy) * gy; v <= ymax + gy / 2;'],
 ['numberline-overshoot','v <= hi; v += step','v <= hi + step / 2; v += step'],
 ['curve-clip',"{ 'clip-path': 'url(#plotclip)' }",'{}']])
 add(name,core,replace(old,value),'svg',name==='invisible-annotation'?'no readable semantic SVG labels':name==='curve-clip'?'curve clipping lost':name.includes('grid')?'grid outside declared window':'FAIL svg-fixture',['--fixtures-only']);
const controlPage=select(/id="premiumIv"/),carry=select(/class="progress-note"/),filePage=select(/id="reviewImport"/);
for(const [name,file,css,expected] of [
 ['brand-height',carry,'[data-ui="masthead"] .brand {min-height:43.99px!important;height:43.99px!important}', '"class":"brand"'],
 ['footer-height',carry,'[data-ui="footer"] a {min-height:43.99px!important;height:43.99px!important}', 'learn.geterdone.io'],
 ['range-height',controlPage,'#premiumIv {min-height:43.99px!important;height:43.99px!important}', 'premiumIv'],
 ['range-width',controlPage,'#premiumIv {min-width:43.99px!important;width:43.99px!important}', 'premiumIv'],
 ['fragmented-inline-link',carry,'.progress-note a {display:inline!important;min-height:0!important}', 'Carry it'],
 ['unreachable-center',carry,'.progress-note a {pointer-events:none!important}', '"reachable":false'],
 ['file-label-height',filePage,'label[for="reviewImport"] {min-height:43.99px!important;height:43.99px!important;padding:0!important}', 'reviewImport']])
 add(name,file,replace('</head>','<style>'+css+'</style></head>'),'targets',expected,['--only='+route(file)]);
// Native categories are discovered from published markup, rather than a route list.
for(const type of ['text','number','checkbox','select','textarea','button']){
 const selector=type==='select'||type==='textarea'||type==='button'?type:'input[type="'+type+'"]';
 const file=witnesses.get(type==='select'?'select-one':type);assert(file,'visible native capability: '+type);
 const css=selector+'{min-width:1px!important;min-height:1px!important;width:1px!important;height:1px!important;padding:0!important;border:0!important}'+(type==='checkbox'?'label:has(input[type="checkbox"]){min-width:1px!important;min-height:1px!important;width:1px!important;height:1px!important;padding:0!important}':'');
 add('native-'+type,file,replace('</head>','<style>'+css+'</style></head>'),'targets','FAIL targets',['--only='+route(file)]);
}
const caps=pages.filter(p=>/<body data-page-kind="(?:slides|supplemental)"/.test(fs.readFileSync(p,'utf8')));assert.equal(caps.length,2);
for(const file of caps) {
 const suffix=/data-page-kind="slides"/.test(fs.readFileSync(file,'utf8'))?'deck':'lab';
 add('masthead-'+suffix,file,replace('<header class="topbar" data-ui="masthead"','<header class="topbar" data-ui="absent"'),'capstone','shared anatomy',['--only='+route(file)]);
 add('brand-identity-'+suffix,file,replace('</head>','<style>.brand-copy{display:none!important}</style></head>'),'capstone','Learn masthead identity',['--only='+route(file)]);
 add('root-mask-'+suffix,file,replace('</head>','<style>html{overflow-x:hidden!important}</style></head>'),'capstone','root masking',['--only='+route(file)]);
 add('page-kind-'+suffix,file,source=>source.replace(/<body data-page-kind="(?:slides|supplemental)"/,'<body data-page-kind="course"'),'capstone','page type',['--only='+route(file)]);
 if(suffix==='lab')add('tablet-price-layout',file,replace('</head>','<style>body[data-page-kind="supplemental"] [data-ui="hero"]{grid-template-columns:repeat(2,minmax(0,1fr))!important}</style></head>'),'capstone','supplemental price wraps mid-number',['--only='+route(file)]);
}
const deck=caps.find(p=>/data-page-kind="slides"/.test(fs.readFileSync(p,'utf8')));
add('removed-print-slide',deck,source=>{const result=source.replace(/<section class="slide">[\s\S]*?<\/section>/,'');assert.notEqual(result,source);return result;},'capstone','preserved sixteen authored slides',['--only='+route(deck)]);
for(const [name,css,expected] of [
 ['print-height','.slide{height:1px!important}','one fixed page'],
 ['print-width','.slide{width:1px!important}','one fixed page'],
 ['print-break','.slide{page-break-after:auto!important}','one fixed page'],
 ['print-controls','.nav{display:flex!important}','printed deck navigation'],
 ['print-content','.chart{height:1000px!important;flex:none!important}','printed slide content clipped']])
 add(name,deck,replace('</head>','<style>@media print{'+css+'}</style></head>'),'capstone',expected,['--only='+route(deck)]);
const log=witnesses.get('svg:log_10');assert(log,'visible logarithm annotation witness');add('literal-svg-entity',log,replace('log_10 ≈','log_10 &asymp;'),'svg','"entity":true',['--only='+route(log)]);
const thumb=select(/>CONFIRM ON PRICE</);add('authored-svg-edge',thumb,replace('x="348" text-anchor="end" y="142">CONFIRM ON PRICE','x="355" y="142">CONFIRM ON PRICE'),'svg','CONFIRM ON PRICE',['--only='+route(thumb)]);
add('auth-rewrite-current',path.join(COPY,'scripts/build_auth_pages.py'),replace('if target.is_file() and target.read_text', 'if False and target.is_file() and target.read_text'),'source','current auth pages must not be rewritten');
const driver=path.join(COPY,'tests/browser_acceptance.js');
add('empty-fixture-selection',driver,replace("assert(!arg('--fixtures-only')", "assert(true||!arg('--fixtures-only')"),'source','fixture-only requires inventory or svg');
add('incompatible-capstone-selection',driver,replace("assert(!only||wanted!=='capstone'", "assert(true||!only||wanted!=='capstone'"),'source','selected route has no capstone capability');
const course=select(/<body data-page-kind="course">/);
add('light-theme-handler',course,replace('</body>','<script>document.getElementById("themeToggle").replaceWith(document.getElementById("themeToggle").cloneNode(true));</script></body>'),'theme','actual theme policy',['--only='+route(course),'--all']);
add('light-theme-colors',course,replace('</head>','<style>body{color:#edf7ff!important}</style></head>'),'theme','resolved theme colors',['--only='+route(course),'--all']);
add('dark-theme-palette',course,replace('--bg: #071019;', '--bg: #edf4f8;'),'theme','resolved theme colors',['--only='+route(course),'--all']);
const contractFile=path.join(COPY,'tests/browser_contracts.js');
for(const [name,old,value,expected] of [
 ['contract-clipped-main',"failures.push({reason:'clipped content owner'","false&&failures.push({reason:'clipped content owner'",'FAIL content clipping'],
 ['contract-svg-nonvacuity',"if(!readable.length)failures.push",'if(false)failures.push','FAIL all semantic SVG labels hidden'],
 ['contract-dark-contrast','if(ratio<4.5)failures.push','if(false)failures.push','FAIL one-to-one dark text'],
 ['contract-rendered-contrast','if(row.ratio+1e-6<row.threshold)failures.push','if(false)failures.push','FAIL rendered contrast ignores unrelated token health'],
 ['contract-empty-contrast',"if(!rows.length)failures.push({reason:'no meaningful text contrast samples'})","if(false)failures.push({reason:'no meaningful text contrast samples'})",'FAIL empty contrast scope']])
 add(name,contractFile,replace(old,value),'contract',expected);
add('contract-empty-layout',contractFile,replace("if(!rows.length)failures.push({reason:'no visible content owners'})","if(false)failures.push({reason:'no visible content owners'})"),'contract','FAIL empty content owners');
const pixels=path.join(COPY,'tests/browser_contrast_pixels.js');
add('raster-svg-coverage',pixels,replace('r.requiresRaster||failed.has(r.nodeIndex)','failed.has(r.nodeIndex)'),'contract','FAIL SVG same accent paint');
add('raster-group-opacity',pixels,replace('for(let i=opacities.length-1;i>=0;i--)','for(let i=-1;i>=0;i--)'),'contract','opacity compositing foreground');
const plottedLabels=select(/id="alPlot"/);
add('svg-label-halo',plottedLabels,replace('</head>','<style>svg text{stroke:none!important}</style></head>'),'contrast','text contrast below threshold',['--only='+route(plottedLabels)]);
add('contract-halo-paint',contractFile,replace('if(halo[3]===1){row.halo=halo','if(false){row.halo=halo'),'contract','FAIL SVG contrasting halo');
for(const file of caps){
 const suffix=file===deck?'deck':'lab';
 add('light-accent-contrast-'+suffix,file,replace('--capstone-accent: #08616e','--capstone-accent: #98f5ff'),'contrast','text contrast below threshold',['--only='+route(file)]);
}
add('light-active-button-contrast',caps.find(p=>p!==deck),replace('color:var(--on-accent);background:var(--cyan)','color:#041116;background:var(--cyan)'),'contrast','text contrast below threshold',['--only='+route(caps.find(p=>p!==deck))]);
const chosen=process.argv.find(a=>a.startsWith('--case='))?.slice(7),selected=chosen?cases.filter(c=>c.name===chosen):cases;
assert(selected.length,'nonempty mutation case selection');
const summary=[];
 for(const c of selected){const original=fs.readFileSync(c.file,'utf8');const out=path.join(OUT,c.name);fs.mkdirSync(out);let run;
  try{fs.writeFileSync(c.file,c.change(original));run=c.group==='source'
    ?spawnSync('/usr/bin/python3',['-m','unittest','discover','-s',path.join(ROOT,'tests'),'-p','test_browser_source.py','-v'],{env:{...process.env,SOURCE_ROOT:COPY,TMPDIR:out},encoding:'utf8'})
    :spawnSync(process.execPath,c.group==='contract'?[path.join(COPY,'tests/browser_contract_fixtures.js')]
      :c.group==='contrast'?[path.join(ROOT,'tests/browser_contrast.js'),...c.extra]
      :[path.join(ROOT,'tests/browser_acceptance.js'),'--class='+c.group,...c.extra],{env:{...process.env,SOURCE_ROOT:COPY,BROWSER_EVIDENCE:out},encoding:'utf8'});}
  finally{fs.writeFileSync(c.file,original);}
  fs.writeFileSync(path.join(out,'command.log'),(run?.stdout||'')+(run?.stderr||''));
  const caught=run.status===1&&((run.stdout||'')+(run.stderr||'')).includes(c.expected);
  summary.push({name:c.name,caught,exit:run.status,expected:c.expected});fs.writeFileSync(path.join(OUT,'summary.json'),JSON.stringify(summary,null,2)+'\n');
  console.log((caught?'CAUGHT ':'ESCAPED ')+c.name);assert(caught,'mutation escaped or failed for an unrelated reason: '+c.name);
 }
 console.log(summary.filter(x=>x.caught).length+'/'+selected.length+' browser mutations caught; worktree inputs untouched.');
}finally{fs.rmSync(COPY,{recursive:true,force:true});}
