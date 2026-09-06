#!/usr/bin/env node
/* Exercise real UI state changes against the localhost candidate. All file
 * input bytes are synthetic and created in memory. Never signs in. */
'use strict';
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {launch,sleep}=require('./browser_cdp'),contracts=require('./browser_contracts');
const ROOT=path.resolve(__dirname,'..'),OUT=process.env.BROWSER_EVIDENCE,base=process.env.BROWSER_BASE;
assert(OUT&&path.resolve(OUT)!==ROOT&&!path.resolve(OUT).startsWith(ROOT+'/'),'external evidence required');
assert(/^http:\/\/127\.0\.0\.1:\d+$/.test(base),'local candidate runtime required');
fs.mkdirSync(OUT,{recursive:true});assert(!fs.existsSync(path.join(OUT,'observations.jsonl')),'fresh evidence directory required');
const corpus=[];function walk(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){const f=path.join(dir,e.name);if(e.isDirectory())walk(f);else if(e.name.endsWith('.html'))corpus.push({file:f,source:fs.readFileSync(f,'utf8'),route:'/'+path.relative(path.join(ROOT,'site'),f).replace(/index\.html$/,'')});}}walk(path.join(ROOT,'site'));
assert.equal(corpus.length,369);
function routeFor(id){const pages=corpus.filter(p=>p.source.includes('id="'+id+'"'));assert(pages.length,'missing interactive capability '+id);return pages.sort((a,b)=>a.route.localeCompare(b.route))[0].route;}
const inventory=fs.readFileSync(path.join(ROOT,'tests/interactive_targets.js'),'utf8'),functions=Object.values(contracts).map(f=>f.toString()).join('\n');
const rows=[],states=[];
async function main(){const c=await launch({dir:OUT,name:'interactions',base});let current;
 async function load(route,width=390,height=844,theme='dark'){current={route,width,height,theme};await c.navigate(route,{width,height,theme});await c.evaluate(inventory+'\n'+functions);const state=await c.evaluate('themeState('+JSON.stringify(theme)+')');assert.equal(state.failures.length,0,JSON.stringify(state));current.actualTheme=state.actual;}
 async function set(id,value){await c.evaluate(`(()=>{const e=document.querySelector(${JSON.stringify(id)});if(!e)throw Error('missing input');e.value=${JSON.stringify(String(value))};e.dispatchEvent(new Event('input',{bubbles:true}));e.dispatchEvent(new Event('change',{bubbles:true}));})()`);}
 async function click(selector){const b=await c.evaluate(`(()=>{const e=document.querySelector(${JSON.stringify(selector)});if(!e)throw Error('missing click target');e.scrollIntoView({block:'center',inline:'center',behavior:'instant'});const b=e.getBoundingClientRect();return{x:b.x+b.width/2,y:b.y+b.height/2}})()`);await c.send('Input.dispatchMouseEvent',{type:'mousePressed',button:'left',clickCount:1,...b});await c.send('Input.dispatchMouseEvent',{type:'mouseReleased',button:'left',clickCount:1,...b});await c.evaluate('new Promise(r=>requestAnimationFrame(r))');}
 async function snapshot(name,details={},selector){const measured=await c.evaluate('({targets:targets(),svg:svgGeometry(),root:rootLayout()})');const failures=[...measured.targets.failures,...measured.svg.failures,...measured.root.failures,...c.events.exceptions,...c.events.console,...c.events.logs,...c.events.blocked];const row={name,...current,...details,...measured,failures};rows.push(row);fs.appendFileSync(path.join(OUT,'observations.jsonl'),JSON.stringify(row)+'\n');if(selector)await c.evaluate(`document.querySelector(${JSON.stringify(selector)}).scrollIntoView({block:'center',behavior:'instant'})`);else await c.evaluate('window.scrollTo({top:0,left:0,behavior:"instant"})');await c.evaluate('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');const png=await c.send('Page.captureScreenshot',{format:'png',captureBeyondViewport:false});fs.writeFileSync(path.join(OUT,name+'-'+current.width+'.png'),Buffer.from(png.data,'base64'));assert.equal(failures.length,0,name+': '+JSON.stringify(failures.slice(0,3)));}
 async function action(name,selector,fn){const before=await c.evaluate(`(()=>{const e=document.querySelector(${JSON.stringify(selector)});return {value:e.value,text:e.innerText,checked:e.checked,pressed:e.getAttribute('aria-pressed')}})()`);await fn();const after=await c.evaluate(`(()=>{const e=document.querySelector(${JSON.stringify(selector)});return {value:e.value,text:e.innerText,checked:e.checked,pressed:e.getAttribute('aria-pressed')}})()`);assert.notDeepEqual(before,after,name+' must change rendered state');states.push({name,before,after});await snapshot(name,{before,after},selector);}
 try{
  await load(routeFor('courseSearch'));await action('search','#courseSearch',()=>set('#courseSearch','Algebra'));
  await click('#themeToggle');assert.equal(await c.evaluate('document.documentElement.dataset.theme'),'light');await snapshot('theme-light');
  const premium=routeFor('premiumIv');
  const scenarios=[{name:'zero',stock:100,strike:105,dte:30,iv:30,type:'call'},
   {name:'tiny',stock:105.01,strike:105,dte:365,iv:100,type:'call'},
   {name:'dominant',stock:200,strike:100,dte:1,iv:10,type:'call'},
   {name:'put',stock:50,strike:100,dte:365,iv:100,type:'put'}];
  for(const [width,height] of [[320,800],[390,844],[768,1024],[1024,768],[1440,900]]){
   await load(premium,width,height,width>=1024?'explicit-light':'dark');
   const observed=new Set();
   for(const s of scenarios){for(const [id,val] of Object.entries({premiumStock:s.stock,premiumStrike:s.strike,premiumDte:s.dte,premiumIv:s.iv}))await set('#'+id,val);await click('#premiumType [data-value="'+s.type+'"]');
    const values=await c.evaluate(`(()=>{const number=id=>Number(document.getElementById(id).textContent.replace(/[^\\d.-]/g,''));return{intrinsic:number('premiumIntrinsic'),extrinsic:number('premiumExtrinsic'),total:number('premiumTotal'),labels:[...document.querySelectorAll('[aria-label="Premium components"] .legend-item')].map(e=>({text:e.textContent,visible:visible(e),independent:!e.closest('.value-stack,#premiumIntrinsic,#premiumExtrinsic')}))}})()`);
    assert.equal(values.intrinsic,Math.round(Math.max(0,s.type==='call'?s.stock-s.strike:s.strike-s.stock)*100)/100);
    assert(Math.abs(values.intrinsic+values.extrinsic-values.total)<=.011,'premium components add to total');
    assert.equal(values.labels.length,2);for(const [i,name] of ['Intrinsic','Extrinsic'].entries())assert(values.labels[i].visible&&values.labels[i].independent&&values.labels[i].text.trim()===name,'independent premium label');
    observed.add(values.intrinsic);await snapshot('premium-'+s.name,{scenario:s,values},'[aria-label="Premium components"]');
   }assert(observed.size>=3,'premium state sweep changes values');
  }
  await load(premium);
  await action('range','#premiumIv',async()=>{await click('#premiumIv');await c.send('Input.dispatchKeyEvent',{type:'keyDown',key:'ArrowRight',code:'ArrowRight',windowsVirtualKeyCode:39});await c.send('Input.dispatchKeyEvent',{type:'keyUp',key:'ArrowRight',code:'ArrowRight',windowsVirtualKeyCode:39});});
  await action('completion','#progressToggle',()=>click('#progressToggle'));
  await action('feedback-text','#fbText',()=>set('#fbText','Synthetic verification <example> & local only.'));
  await click('#fbForm button');assert.equal(await c.evaluate('document.querySelectorAll(".fb-tick").length'),1);await snapshot('feedback-added',{},'#fbForm');
  await click('.fb-tick');await snapshot('feedback-ticked',{},'#fbForm');await click('.fb-drop');assert.equal(await c.evaluate('document.querySelectorAll(".fb-tick").length'),0);await snapshot('feedback-removed',{},'#fbForm');
  await load(routeFor('showLabels'));await action('checkbox','#showLabels',()=>click('#showLabels'));
  await load(routeFor('nlA'));await action('text','#nlA',()=>set('#nlA','-7/2'));
  const option=await c.evaluate('document.querySelector("#nlPreset").options[1].value');await action('select','#nlPreset',()=>set('#nlPreset',option));
  await load(routeFor('gMatrix'));await set('#gAlgo','degree');
  const graph=()=>c.evaluate(`(()=>{const cells=[...document.querySelectorAll('#gMatrix [role="button"]')];return{cells:cells.map(e=>e.textContent),text:document.querySelector('#gMatrix').textContent}})()`);
  const before=await graph();await click('#gMatrix [role="button"]:nth-child(3)');const after=await graph();assert.notDeepEqual(before,after,'graph cell action changes adjacency matrix');await snapshot('graph-edited',{before,after},'#gMatrix');
  await load(routeFor('journalImport'));await action('date','#journalDate',()=>set('#journalDate','2026-01-15'));
  await c.evaluate(`(()=>{const dt=new DataTransfer();dt.items.add(new File([JSON.stringify({entries:[{id:'verify-local',date:'2026-01-15',symbol:'SYNTHETIC',setup:'Pullback',direction:'Long',timeframe:'1 hour',resultR:1,executionScore:3,followedPlan:true,mistakes:[],context:'verification only',notes:'synthetic local data'}]})],'synthetic-verification.json',{type:'application/json'}));const e=document.querySelector('#journalImport');e.files=dt.files;e.dispatchEvent(new Event('change',{bubbles:true}));})()`);
  await sleep(100);assert(await c.evaluate('document.body.innerText.includes("SYNTHETIC")'),'synthetic file import must render its row');await snapshot('file-import',{},'label[for="journalImport"]');
  for(const page of corpus.filter(p=>/<body data-page-kind="(?:library|subject|course|supplemental|slides|progress)"/.test(p.source)))for(const [width,height,theme] of [[390,844,'dark'],[768,1024,'system-light'],[1440,900,'explicit-light']]){await load(page.route,width,height,theme);await snapshot('family-'+page.route.replace(/\W/g,'_')+'-'+theme);}
 }finally{await c.close();const summary={observations:rows.length,interactions:states,failures:rows.reduce((n,r)=>n+r.failures.length,0),controls:rows.reduce((n,r)=>n+r.targets.rows.length,0),svgTexts:rows.reduce((n,r)=>n+r.svg.rows.length,0)};fs.writeFileSync(path.join(OUT,'summary.json'),JSON.stringify(summary,null,2)+'\n');console.log(JSON.stringify(summary));}
}
main().catch(e=>{console.error(e.stack);process.exitCode=1});
