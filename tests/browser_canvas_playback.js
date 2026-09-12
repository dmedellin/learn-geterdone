'use strict';
const fs=require('node:fs'),path=require('node:path'),http=require('node:http'),crypto=require('node:crypto');
const R=path.resolve(process.env.SOURCE_ROOT||path.join(__dirname,'..')),OUT=process.env.BROWSER_EVIDENCE;
const {inventory,htmlParts,lex}=require(R+'/scripts/canvas_sources'),{launch}=require(R+'/tests/browser_cdp'),protocol=require(R+'/tests/mutation_protocol');
const {interceptCanvasText,reconcileRuntimeHistory}=require(R+'/tests/canvas_runtime_contract'),{canvasFinalRaster}=require(R+'/tests/canvas_raster_contract'),{reconcileCanvasRaster}=require(R+'/tests/canvas_raster_evidence'),{reconcileCanvasArtifacts}=require(R+'/tests/canvas_raster_artifacts');
const {installCanvasIntervalClock}=require('./canvas_interval_clock.js'),{boundedIntervalDomain}=require('./canvas_interval_domain.js');
const hash=value=>crypto.createHash('sha256').update(JSON.stringify(value)).digest('hex');
const fail=assertion=>{throw Object.assign(Error(assertion),{code:'LEARN_CANVAS_SEMANTIC',assertion})};
(async()=>{
 fs.mkdirSync(OUT,{recursive:true});const source=inventory(R);if(source.errors.length)fail(source.errors[0].assertion);
 const candidates=source.pages.filter(p=>p.canvases.length&&htmlParts(fs.readFileSync(p.file,'utf8')).scripts.some(s=>s.executable&&!s.attributes['data-canvas-text']&&lex(s.source).some(t=>t.kind==='identifier'&&t.value==='setInterval')));
 const server=http.createServer((req,res)=>{try{let f=path.resolve(R,'site','.'+decodeURIComponent(req.url.split('?')[0]));if(!f.startsWith(R+'/site/'))throw Error('path');if(fs.statSync(f).isDirectory())f=path.join(f,'index.html');res.setHeader('Content-Type','text/html; charset=utf-8');res.end(fs.readFileSync(f));}catch{res.writeHead(404);res.end()}});await new Promise(r=>server.listen(0,'127.0.0.1',r));const name='playback-states',c=await launch({dir:OUT,name,base:'http://127.0.0.1:'+server.address().port}),rows=[],noninterference=[];
 try{
  await c.send('Page.addScriptToEvaluateOnNewDocument',{source:'('+interceptCanvasText.toString()+')()'});
  for(const page of candidates){
   const definitions=boundedIntervalDomain(fs.readFileSync(page.file,'utf8'));if(definitions.length!==1)fail('ambiguous playback interval domain');const domain=definitions[0];
   const hook=await c.send('Page.addScriptToEvaluateOnNewDocument',{source:'('+installCanvasIntervalClock.toString()+')('+JSON.stringify(definitions)+')'});
   await c.navigate(page.route,{width:390,height:844,theme:'dark'});await c.send('Page.removeScriptToEvaluateOnNewDocument',{identifier:hook.identifier});
   const controls=await c.evaluate(`(()=>{const play=[...document.querySelectorAll('.lab button')].filter(b=>b.textContent.trim()==='Play');if(!play.length)return null;if(play.length!==1)throw Error('ambiguous playback owner');const root=play[0].closest('.lab'),siblings=[...play[0].parentElement.querySelectorAll('button')],reset=siblings.find(b=>b.textContent.trim()==='Reset'),step=siblings.find(b=>b.textContent.trim()==='Step'),selects=[...root.querySelectorAll('select')],ranges=[...root.querySelectorAll('input[type=range]')];if(!reset?.id||!step?.id||selects.length!==1||ranges.length!==1)throw Error('unresolved playback controls');const select=selects[0],range=ranges[0];return {play:play[0].id,reset:reset.id,step:step.id,select:select.id,options:[...select.options].map(o=>o.value),speed:{id:range.id,min:Number(range.min),max:Number(range.max),step:Number(range.step),initial:Number(range.value)},canvas:root.querySelector('canvas').id}})()`);if(!controls)continue;
   const speed=controls.speed;if(![speed.min,speed.max,speed.step,speed.initial].every(Number.isFinite)||speed.min<=0||speed.step<=0||(speed.max-speed.min)%speed.step)fail('unresolved playback speed domain');
   const speeds=Array.from({length:1+(speed.max-speed.min)/speed.step},(_,i)=>speed.min+i*speed.step);
   const plan={route:page.route,sourceHash:page.sha256,domain,controls,speeds,width:390,height:844,theme:'dark',states:controls.options.length*domain.states.length,finiteApplicationProofComplete:false};fs.writeFileSync(OUT+'/plan.json',JSON.stringify(plan,null,2));
   await c.evaluate(canvasFinalRaster.toString());
   const state=()=>c.evaluate(`(()=>{const c=${JSON.stringify(controls)},root=document.getElementById(c.play).closest('.lab'),tape=root.querySelector('.tape');return {frame:CanvasText.inspect().find(f=>f.canvas===c.canvas),rows:tape?[...tape.children].map(e=>e.textContent):[],kpis:root.querySelector('#kpis')?.textContent||null}})()`);
   const click=id=>c.evaluate('document.getElementById('+JSON.stringify(id)+').click()');
   const capture=async(mode,shown)=>{
    const observed=await c.evaluate(`canvasFinalRaster(${JSON.stringify(controls.canvas)}).then(result=>({result})).catch(e=>({error:e.message,assertion:e.assertion,code:e.code,evidence:window.__learnCanvasRasterEvidence}))`,900000),file=mode+'-'+shown+'.json';fs.writeFileSync(OUT+'/'+file,JSON.stringify(observed));
    if(observed.error){if(observed.code==='LEARN_CANVAS_SEMANTIC')fail(observed.assertion);throw Error(observed.error);}
    const expected=(await state()).frame,proof=reconcileCanvasRaster(observed.result,expected),frames=fs.readFileSync(OUT+'/'+name+'-raster-frames.jsonl','utf8').trim().split('\n').map(JSON.parse),artifacts=reconcileCanvasArtifacts(observed.result,expected,{directory:OUT,frames});fs.writeFileSync(OUT+'/'+mode+'-'+shown+'-proof.json',JSON.stringify({proof,artifacts}));return proof;
   };
   for(const mode of controls.options){
    await c.evaluate(`(()=>{const e=document.getElementById(${JSON.stringify(controls.select)});e.value=${JSON.stringify(mode)};e.dispatchEvent(new Event('change',{bubbles:true}));})()`);
    const manual=[];for(const shown of domain.states){const s=await state();if(s.rows.length!==shown)fail('playback collection differs from derived bounded domain');manual.push(s);if(shown<domain.terminal)await click(controls.step);}
    await click(controls.step);if(hash(await state())!==hash(manual.at(-1)))fail('playback terminal state is not bounded');
    await click(controls.reset);await click(controls.play);
    for(const shown of domain.states){
     const s=await state(),clock=await c.evaluate('__learnCanvasClock.snapshot()');if(hash(s)!==hash(manual[shown-1]))fail('interval transition differs from authored step');
     if(clock.active.length!==(shown<domain.terminal?1:0))fail('playback interval terminal lifecycle differs');
     const proof=await capture(mode,shown),after=await state();if(hash(s)!==hash(after))fail('playback state changed during held capture');
     const row={route:page.route,mode,shown,traceHash:hash(s),manualTraceHash:hash(manual[shown-1]),clock,proof};rows.push(row);fs.appendFileSync(OUT+'/observations.jsonl',JSON.stringify(row)+'\n');console.log(JSON.stringify({route:page.route,mode,shown,labels:proof.labels,samples:proof.coreSamples}));
     if(shown<domain.terminal)await c.evaluate('__learnCanvasClock.tick('+clock.active[0].id+')');
    }
    for(const delay of speeds){
     await click(controls.reset);await c.evaluate(`(()=>{const e=document.getElementById(${JSON.stringify(speed.id)});e.value=${delay};e.dispatchEvent(new Event('input',{bubbles:true}));e.dispatchEvent(new Event('change',{bubbles:true}));})()`);await click(controls.play);
     const clock=await c.evaluate('__learnCanvasClock.snapshot()');if(clock.active.length!==1||clock.active[0].delay!==delay||hash(await state())!==hash(manual[0]))fail('playback speed changes initial canvas state');
     await c.evaluate('__learnCanvasClock.tick('+clock.active[0].id+')');const next=await state();if(hash(next)!==hash(manual[1]))fail('playback speed changes transition result');noninterference.push({mode,delay,traceHash:hash(next),referenceHash:hash(manual[1])});
    }
    await click(controls.reset);
   }
   const native=await c.evaluate('__learnCanvasNative.snapshot()'),runtime=reconcileRuntimeHistory(page,native);fs.writeFileSync(OUT+'/runtime.json',JSON.stringify({native,runtime}));fs.writeFileSync(OUT+'/speed-noninterference.json',JSON.stringify(noninterference));
   if(c.events.exceptions.length||c.events.blocked.length||c.events.responses.some(r=>r.status>=400))throw Error('playback runtime/network setup failure');
   if(rows.length!==plan.states||noninterference.length!==speeds.length*controls.options.length)fail('incomplete bounded playback witnesses');
   fs.writeFileSync(OUT+'/summary.json',JSON.stringify({route:page.route,states:rows.length,options:controls.options.length,speeds:speeds.length,noninterference:noninterference.length,runtime,failures:0,finiteApplicationProofComplete:false},null,2));
  }
  if(!rows.length)fail('empty bounded playback inventory');
 }finally{fs.writeFileSync(OUT+'/events.json',JSON.stringify(c.events));await c.close();await new Promise(r=>server.close(r));}
})().catch(e=>{if(e.code==='LEARN_CANVAS_SEMANTIC')protocol.semantic(e.assertion);else protocol.setup(e);process.exitCode=1});
