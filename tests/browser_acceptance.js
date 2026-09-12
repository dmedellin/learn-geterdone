#!/usr/bin/env node
/* No packages: real Chrome/CDP and a localhost server over exact working bytes.
 * BROWSER_EVIDENCE must point outside the repository. --all checks every route
 * at all five widths; the default derives a small set from source capabilities.
 */
'use strict';
const fs=require('node:fs'),path=require('node:path'),http=require('node:http'),assert=require('node:assert/strict');
const {launch}=require('./browser_cdp'),contracts=require('./browser_contracts');
const protocol=require('./mutation_protocol');
const {reconcileSvgRaster}=require('./svg_raster_evidence');
const ROOT=path.resolve(process.env.SOURCE_ROOT||path.join(__dirname,'..'));
const SITE=path.join(ROOT,'site'),OUT=process.env.BROWSER_EVIDENCE;
assert(OUT&&path.resolve(OUT)!==ROOT&&!path.resolve(OUT).startsWith(ROOT+'/'),'external BROWSER_EVIDENCE is required');
fs.mkdirSync(OUT,{recursive:true});
assert(!fs.existsSync(path.join(OUT,'observations.jsonl')),'use a fresh evidence directory');
function selection(condition,message){if(!condition){console.log(JSON.stringify({schema:'learn-selection-v1',phase:'rejected',assertion:message}));process.exit(1);}}
const arg=name=>process.argv.includes(name),wanted=process.argv.find(a=>a.startsWith('--class='))?.split('=')[1];
selection(!wanted||['inventory','targets','svg','capstone','theme'].includes(wanted),'unknown browser contract class');
selection(!arg('--fixtures-only')||!wanted||['inventory','svg'].includes(wanted),'fixture-only requires inventory or svg');
const enabled=name=>!wanted||wanted===name;
const only=process.argv.find(a=>a.startsWith('--only='))?.slice(7);
function pages(dir=SITE) {return fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.isDirectory()?pages(path.join(dir,e.name)):e.name.endsWith('.html')?[path.join(dir,e.name)]:[]);}
const corpus=pages().sort().map(file=>({file,route:'/'+path.relative(SITE,file).replace(/index\.html$/,''),source:fs.readFileSync(file,'utf8')}));
assert.equal(corpus.length,369,'full non-vacuous published HTML corpus');
selection(!only||corpus.some(p=>p.route===only),'no matching browser route');
const caps=corpus.filter(p=>/class="deck"/.test(p.source)||/id="as-of"/.test(p.source));
assert.equal(caps.length,2,'derive both supplemental layouts from content capability');
selection(!only||wanted!=='capstone'||caps.some(p=>p.route===only),'selected route has no capstone capability');
console.log(JSON.stringify({schema:'learn-selection-v1',phase:'validated'}));
if(arg('--validate-selection'))process.exit(0);
const keys=new Set(),focused=corpus.filter(p=>{
  const candidates=[...p.source.matchAll(/<input\b[^>]*\btype="([^"]+)"/g)].map(m=>'input:'+m[1]);
  for(const m of p.source.matchAll(/function\s+(\w*[Ll]ab)\s*\(/g)) candidates.push('lab:'+m[1]);
  for(const re of [/class="progress-note"/,/function Plot\(/,/function NumberLine\(/,/data-ui="hero"/]) if(re.test(p.source)) candidates.push(String(re));
  // The default includes every Course hero and the two concrete label callers;
  // new courses inherit coverage without a maintained route list.
  if(/data-page-kind="course"/.test(p.source)||/id="(?:lgPlot|iqLine)"/.test(p.source)||caps.includes(p)) return true;
  const fresh=candidates.some(k=>!keys.has(k));candidates.forEach(k=>keys.add(k));return fresh;
});
assert(focused.length>=25&&keys.size>=10,'non-vacuous source-owner selection');
const widths=[[320,800],[390,844],[768,1024],[1024,768],[1440,900]];
const inventorySource=fs.readFileSync(path.join(ROOT,'tests/interactive_targets.js'),'utf8');
const functions=Object.values(contracts).map(f=>f.toString()).join('\n');
const results=[];
function record(group,context,result){const row={group,...context,...result};results.push(row);fs.appendFileSync(path.join(OUT,'observations.jsonl'),JSON.stringify(row)+'\n');if(group==='svg'||group==='svg-fixture')reconcileSvgRaster(result);if(result.failures?.length){console.log('FAIL '+group+' '+JSON.stringify(context)+' '+JSON.stringify(result.failures.slice(0,2)));if(group==='runtime')protocol.setup(JSON.stringify(result.failures));else protocol.failures(group,result.failures);}}
const server=http.createServer((req,res)=>{let file=path.join(SITE,decodeURIComponent(req.url.split('?')[0]));if(!file.startsWith(SITE+'/')&&file!==SITE){res.writeHead(403);res.end();return;}if(fs.existsSync(file)&&fs.statSync(file).isDirectory())file=path.join(file,'index.html');try{const data=fs.readFileSync(file);res.setHeader('Content-Type',file.endsWith('.html')?'text/html; charset=utf-8':'application/json');res.end(data);}catch{res.writeHead(404);res.end();}});
async function fixture(c,markup,code,timeoutMs=60000){await c.send('Page.setDocumentContent',{frameId:(await c.send('Page.getFrameTree')).frameTree.frame.id,html:'<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="icon" href="data:,"><style>svg{width:660px;max-width:none;display:block}.fixture-stage{box-sizing:border-box;max-width:100%;overflow-x:auto;overscroll-behavior-inline:contain}.plot-label,.plot-tick{font:12px system-ui}.edge-left{text-anchor:end}label{display:inline-flex;min-width:44px;min-height:44px}</style></head><body>'+markup+'</body></html>'});return c.evaluate('(async()=>{'+functions+'\n'+code+'})()',timeoutMs);}
async function main(){
 await new Promise(r=>server.listen(0,'127.0.0.1',r));
 const base=process.env.BROWSER_BASE||'http://127.0.0.1:'+server.address().port;
 assert(/^http:\/\/127\.0\.0\.1:\d+$/.test(base),'local candidate runtime only');
 const c=await launch({dir:OUT,name:'acceptance',base});
 try{
  await c.navigate('/',{width:390,height:844});
  if(enabled('inventory')) {
   const markup='<section id="process"></section><form name="module"></form><label for="file">Import</label><input id="file" type="file" hidden><label for="clipped">Import clipped</label><input id="clipped" type="file" style="position:absolute;width:1px;height:1px;clip-path:inset(50%)"><input id="missing" type="file"><label for="dangling">Dangling</label><label><input id="wrapped" type="checkbox">Wrapped</label><label for="radio">Radio</label><input id="radio" type="radio"><label for="range">Slider</label><input id="range" type="range"><div id="empty"></div>';
   const r=await fixture(c,markup,`const failures=[];try{(0,eval)(${JSON.stringify(inventorySource)})}catch(e){failures.push('browser named-global collision: '+e.message)}
    if(window.module.exports!==undefined) failures.push('named module was treated as CommonJS');
    const api=window.learnInteractiveTargets;if(!api)return {failures:[...failures,'missing inventory API']};
    const first=api.inventory(); if(first.length!==6)failures.push('non-vacuous fixture inventory: '+first.length);
    for(const id of ['file','clipped','wrapped','radio']){const item=first.find(i=>i.control.id===id);if(!item||!item.owners.some(e=>e.tagName==='LABEL')) failures.push(id+': associated label owner missing');}
    for(const id of ['missing','range']){const item=first.find(i=>i.control.id===id);if(!item||item.owners.length!==1||item.owners[0]!==item.control) failures.push(id+': invalid label owner');}
    if(first.some(i=>i.owners.some(e=>e.htmlFor==='dangling')))failures.push('dangling label claimed');
    const measured=targets();for(const id of ['file','clipped'])if(!measured.rows.some(r=>r.id===id&&r.owner==='LABEL'&&r.width>=44&&r.height>=44))failures.push(id+': visible file owner not measured');
    const file=document.querySelector('#file');let activated=0;file.addEventListener('click',e=>{e.preventDefault();activated++});file.labels[0].click();if(activated!==1)failures.push('native file label did not activate its input');
    if(api.inventory(document.querySelector('#empty')).length!==0)failures.push('empty scope not empty');
    const dynamic=document.createElement('button');dynamic.textContent='Dynamic';document.body.append(dynamic);
    if(api.inventory().length!==first.length+1||!api.inventory().some(i=>i.control===dynamic))failures.push('dynamic control omitted');
    return {count:first.length,dynamic:api.inventory().length,failures};`);
   record('inventory',{fixture:'native DOM owners and named globals'},r);
  }
  if(enabled('svg')) {
   const source=fs.readFileSync(path.join(ROOT,'scripts/mathpath/labs/algebra_core.py'),'utf8').match(/PLOT_JS = r"""([\s\S]*?)"""/)[1];
   for(const edge of ['left','right','top','bottom','long','offscale','ticks','numberline']) {
    // These fixtures rasterize hundreds of labels across their plots. Preserve
    // the oracle, with the whole-document SVG transport ceiling per fixture.
    const r=await fixture(c,'<div class="fixture-stage" tabindex="0" role="region" aria-label="SVG geometry fixture; scroll horizontally for complete labels"><svg id="plot"></svg></div>',source+`\nconst svg=document.querySelector('svg'),stage=svg.closest('.fixture-stage'),edge=${JSON.stringify(edge)},win={xmin:-3.3,xmax:13.3,ymin:-3.3,ymax:13.3};
      if(edge==='numberline')NumberLine(svg,-3.3,13.3);
      else {const p=Plot(svg,win).frame();const point={left:[-3.3,5],right:[13.3,5],top:[5,13.3],bottom:[5,-3.3],long:[5,5],offscale:[30,30],ticks:[5,5]}[edge];
        if(edge!=='ticks'){
          const text=edge==='long'?'Long annotation '.repeat(30):'Boundary annotation';
          // Exercise each caller on its own plot. Painting four identical
          // labels on one point makes the fixture itself occlude semantic ink.
          const plots=[p];for(let i=1;i<4;i++){const owner=svg.cloneNode(false);owner.id='plot-'+i;svg.after(owner);plots.push(Plot(owner,win).frame());}
          plots[0].label(...point,text,edge==='left'?'plot-label edge-left':undefined);
          plots[1].point(...point,undefined,text);plots[2].vline(point[0],undefined,text);plots[3].hline(point[1],undefined,text);
        }}
      const result=await svgGeometry();if(!result.rows.length)result.failures.push({reason:'vacuous SVG fixture'});
      if(!stage||stage.tabIndex<0||stage.getAttribute('role')!=='region'||!stage.getAttribute('aria-label')||stage.scrollWidth<=stage.clientWidth)result.failures.push({reason:'fixture horizontal scroll owner inaccessible'});
      const annotations=[...document.querySelectorAll('text.plot-label')];
      const expected=['left','right','top','bottom'].includes(edge)?4:0;
      if(annotations.length!==expected||annotations.filter(visible).length!==expected)result.failures.push({reason:'annotation presence',expected,actual:annotations.length,visible:annotations.filter(visible).length});
      if(edge!=='numberline') {
        if(!svg.querySelector('g[clip-path]')||!svg.querySelector('clipPath rect'))result.failures.push({reason:'curve clipping lost'});
        for(const line of document.querySelectorAll('.plot-grid'))for(const [attr,lo,hi] of [['x1',44,644],['x2',44,644],['y1',16,386],['y2',16,386]]){const v=+line.getAttribute(attr);if(v<lo||v>hi)result.failures.push({reason:'grid outside declared window',attr,value:v});}
      }
      if(edge==='ticks'||edge==='numberline')for(const t of svg.querySelectorAll('text.plot-tick')){const v=Number(t.textContent);if(v < -3.3||v > 13.3)result.failures.push({reason:'tick outside declared window',value:v});}
      return result;`,900000);
    record('svg-fixture',{edge},r);
   }
  }
  if(!arg('--fixtures-only')&&(!wanted||['targets','svg','capstone','theme'].includes(wanted))) {
   const selected=only?corpus.filter(p=>p.route===only):wanted==='capstone'?caps:arg('--all')?corpus:focused;
   for(const page of selected)for(const [width,height,theme='dark'] of [...(caps.includes(page)||arg('--all')?widths:widths.slice(0,2)),...(arg('--all')&&/data-page-kind="course"/.test(page.source)?[[390,844,'system-light'],[1440,900,'explicit-light']]:[])]) {
    await c.navigate(page.route,{width,height,theme});
    // Load the exact utility; runtime errors are separately fatal. Its API may
    // still be present after an exception, letting RED report other classes.
    const injection=await c.evaluate(`(()=>{try{(0,eval)(${JSON.stringify(inventorySource)});return []}catch(e){return [String(e)]}})()`);
    const context={route:page.route,width,height,theme};
    record('inventory-runtime',context,{failures:injection});
    await c.evaluate(functions);
    record('root',context,await c.evaluate('rootLayout()'));
    record('theme',context,await c.evaluate('themeState('+JSON.stringify(theme)+')'));
    if(enabled('targets')) record('targets',context,await c.evaluate('targets()'));
    if(enabled('svg')) {
      // Whole-document geometry may measure hundreds of labels in one async
      // call. Keep the exact oracle, with a finite workload-derived deadline.
      const labels=await c.evaluate('document.querySelectorAll("svg text").length');
      const timeoutMs=Math.min(900000,60000+labels*5000);
      record('svg',context,await c.evaluate('svgGeometry()',timeoutMs));
    }
    if(enabled('capstone')&&caps.includes(page)) {
      record('capstone',context,await c.evaluate('capstone()'));
      if(/class="slide(?: active)?"/.test(page.source)) {
        await c.send('Emulation.setEmulatedMedia',{media:'print'});
        await c.evaluate('window.dispatchEvent(new Event("beforeprint"))');
        record('print',context,await c.evaluate('capstone()'));
        if(width===1440){const pdf=await c.send('Page.printToPDF',{printBackground:true,preferCSSPageSize:true});fs.writeFileSync(path.join(OUT,'slides.pdf'),Buffer.from(pdf.data,'base64'));}
        await c.send('Emulation.setEmulatedMedia',{media:''});await c.evaluate('window.dispatchEvent(new Event("afterprint"))');
      }
    }
    const responses=c.events.responses.filter(r=>r.type==='Document');
    record('runtime',context,{http:responses.map(r=>({url:r.url,status:r.status})),failures:[...c.events.exceptions,...c.events.console,...c.events.logs,...c.events.blocked,...(responses.length!==1||responses[0].status!==200?[{reason:'exactly one successful document response',responses}]:[])]});
    if(caps.includes(page)||/id="(?:lgPlot|iqLine|premiumIv)"/.test(page.source)) {const shot=await c.send('Page.captureScreenshot',{format:'png',captureBeyondViewport:false});fs.writeFileSync(path.join(OUT,page.route.replace(/\W/g,'_')+width+'-'+theme+'.png'),Buffer.from(shot.data,'base64'));}
   }
  }
 }finally{await c.close();await new Promise(r=>server.close(r));}
 const summary={browser:c.browserVersion,corpus:corpus.length,focused:focused.length,observations:results.length,groups:{}};
 for(const r of results){const s=summary.groups[r.group]||={observations:0,measured:0,failures:0};s.observations++;s.measured+=r.rows?.length||r.count||0;s.failures+=r.failures.length;}
 const requested=wanted?[wanted]:arg('--fixtures-only')?['inventory','svg']:['inventory','targets','svg','capstone'];
 for(const group of requested)assert((summary.groups[group]?.observations||summary.groups[group+'-fixture']?.observations)>0,'non-vacuous requested browser contract: '+group);
 fs.writeFileSync(path.join(OUT,'summary.json'),JSON.stringify(summary,null,2)+'\n');console.log(JSON.stringify(summary));
 if(results.some(r=>r.failures.length))process.exitCode=1;
}
main().catch(e=>{protocol.setup(e);server.close();process.exitCode=1;});
