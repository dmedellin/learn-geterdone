'use strict';
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const R=process.env.SOURCE_ROOT||path.resolve(__dirname,'..'),OUT=process.env.BROWSER_EVIDENCE;
const {launch}=require(R+'/tests/browser_cdp'),contracts=require(R+'/tests/browser_contracts'),protocol=require(R+'/tests/mutation_protocol');
const {reconcileTextTiles}=require(R+'/tests/text_tile_contract');
const definitions=Object.values(contracts).map(f=>f.toString()).join('\n');
(async()=>{
 fs.mkdirSync(OUT,{recursive:true});const c=await launch({dir:OUT,name:'tiles',base:'http://127.0.0.1:1'}),rows=[];
 const save=()=>fs.writeFileSync(path.join(OUT,'observations.json'),JSON.stringify(rows,null,2));
 const reset=async body=>{
  await c.send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
  await c.send('Page.setDocumentContent',{frameId:(await c.send('Page.getFrameTree')).frameTree.frame.id,html:'<!doctype html><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{margin:0;background:#071019;color:white;font:24px sans-serif}.sr{position:absolute;width:1px;height:1px;clip:rect(0 0 0 0);clip-path:inset(50%);overflow:hidden}#owner{width:240px;height:120px;overflow:auto}#target{margin:0;padding:2px;white-space:pre;font:24px/32px monospace}textarea{font:24px/32px monospace;color:white;background:#071019;width:240px;height:120px;box-sizing:border-box}</style>'+body});
  await c.evaluate(definitions+';window.originalBridge=window.originalBridge||window.learnCaptureRaster;window.learnCaptureRaster=window.originalBridge;');
 };
 const measure=()=>c.evaluate("measureTextPaint([{nodeIndex:0,threshold:4.5,element:document.getElementById('target'),node:document.getElementById('target').matches('textarea,input,select')?null:document.getElementById('target').firstChild}])");
 try{
  await reset('<label class="sr" id="direct" for="control">Accessible name</label><input id="control"><label class="sr" id="dangling" for="missing">Dangling label</label><label class="sr" id="hidden" for="hidden-control">Hidden control label</label><input id="hidden-control" style="display:none"><span class="sr" id="unrelated">Unrelated clipped text</span>');
  const ownership=await c.evaluate("['direct','dangling','hidden','unrelated'].map(id=>({id,excluded:accessibleControlName(document.getElementById(id))}))");
  rows.push({name:'narrow accessible naming ownership',ownership});save();assert.deepEqual(ownership.map(r=>r.excluded),[true,false,false,false],'accessible-only names require visible associated owner');
  for(const id of ['dangling','hidden','unrelated']){const measured=await c.evaluate(`measureTextPaint([{nodeIndex:0,threshold:4.5,element:document.getElementById('${id}'),node:document.getElementById('${id}').firstChild}])`);assert.equal(measured[0].error,'no rendered glyph interior samples','unrelated clipped semantic text is rejected');}
  const cases=[
   ['horizontal and vertical owner','<main id="owner" tabindex="0" aria-label="Code"><pre id="target" style="width:max-content;min-width:100%">'+Array.from({length:16},(_,i)=>'LINE '+i+' — ABCDEFGHIJKLMNOPQRSTUVWXYZ').join('\n')+'</pre></main>'],
   ['horizontal owner inside fixed clip','<article style="width:260px;overflow:hidden"><main id="owner" tabindex="0" aria-label="Clipped-card code" style="width:240px"><pre id="target" style="width:max-content;min-width:100%">'+Array.from({length:4},(_,i)=>'LINE '+i+' — ABCDEFGHIJKLMNOPQRSTUVWXYZ').join('\n')+'</pre></main></article>'],
   ['smooth horizontal and vertical owner','<main id="owner" tabindex="0" aria-label="Code" style="scroll-behavior:smooth"><pre id="target" style="width:max-content;min-width:100%">'+Array.from({length:16},(_,i)=>'LINE '+i+' — ABCDEFGHIJKLMNOPQRSTUVWXYZ').join('\n')+'</pre></main>'],
   ['taller than viewport','<pre id="target">'+Array.from({length:50},(_,i)=>'LINE '+i).join('\n')+'</pre>'],
   ['smooth document scroll','<style>html{scroll-behavior:smooth}</style><pre id="target">'+Array.from({length:50},(_,i)=>'LINE '+i).join('\n')+'</pre>'],
   ['native input','<input id="target" readonly value="ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ" style="width:220px;box-sizing:border-box;color:white;background:#071019">'],
   ['native textarea','<textarea id="target" readonly>'+Array.from({length:15},(_,i)=>'LINE '+i+' ABCDEFGHIJKLMNOPQRSTUVWXYZ').join('\n')+'</textarea>'],
   ['native select border','<select id="target" style="border:2px solid gray;color:white;background:#071019"><option>Selected value</option></select>']
  ];
  for(const [name,markup] of cases){
   await reset(markup);const before=await c.evaluate('({html:document.documentElement.outerHTML,scroll:[...document.querySelectorAll("*")].map(e=>[e.scrollLeft,e.scrollTop])})');
   let result,error;try{result=await measure()}catch(e){error=e.message}
   const after=await c.evaluate('({html:document.documentElement.outerHTML,scroll:[...document.querySelectorAll("*")].map(e=>[e.scrollLeft,e.scrollTop])})');
   rows.push({name,result,error,restored:JSON.stringify(before)===JSON.stringify(after)});save();
   if(error)throw Error(error); // Capture/setup failures are never semantic catches.
   if(result&&!result[0].error){
    assert.equal(reconcileTextTiles(result[0]),true,'complete real tiles reconcile');
    if(name==='horizontal and vertical owner'){
     const positive=result[0],clone=()=>JSON.parse(JSON.stringify(positive));
     const rejects=(fn,pattern,message)=>{let failure;try{fn()}catch(e){failure=e}assert(failure&&pattern.test(failure.message),message);rows.push({name:message,error:failure.message,expectedSetupFailure:true,semanticCatch:false});save()};
     const metadata=clone();delete metadata.tiling.tiles[0].captures;rejects(()=>reconcileTextTiles(metadata),/incomplete tile capture phases/,'missing raster metadata rejects');
     const missing=clone();missing.tiling.tiles.pop();missing.tiling.plannedTiles--;missing.tiling.capturedTiles--;for(const k of ['sampleCount','expectedPixels','missingPixels'])missing[k]=missing.tiling.tiles.reduce((n,t)=>n+t[k],0);rejects(()=>reconcileTextTiles(missing),/tile coverage reconciliation mismatch/,'missing noninitial tile rejects');
     const overlap=clone();overlap.tiling.tiles[1].coverage.push(overlap.tiling.tiles[0].coverage[0]);rejects(()=>reconcileTextTiles(overlap),/overlapping tile ownership/,'duplicate tile ownership rejects');
     const samples=clone();samples.sampleCount++;rejects(()=>reconcileTextTiles(samples),/tile sample reconciliation mismatch/,'missing visibility samples reject');
    }
   }
   assert(!error&&result?.length===1&&!result[0].error&&result[0].ratio>=4.5&&result[0].sampleCount>0&&result[0].tiling?.complete&&result[0].tiling.capturedTiles>=(name==='native select border'?1:2),name+' complete real tiles');assert.deepEqual(after,before,name+' exact restoration');
  }
  await reset('<article style="width:240px;overflow:hidden"><pre id="target" style="width:max-content">THIS FIXED-CLIPPED LABEL EXTENDS BEYOND ITS NONSCROLLING OWNER</pre></article>');
  const clippedBefore=await c.evaluate('({html:document.documentElement.outerHTML,scroll:[...document.querySelectorAll("*")].map(e=>[e.scrollLeft,e.scrollTop])})');
  const clipped=await measure(),clippedAfter=await c.evaluate('({html:document.documentElement.outerHTML,scroll:[...document.querySelectorAll("*")].map(e=>[e.scrollLeft,e.scrollTop])})');
  rows.push({name:'fixed clip without scroll camera',result:clipped,restored:JSON.stringify(clippedBefore)===JSON.stringify(clippedAfter)});save();
  assert.equal(clipped[0].error,'unmeasured semantic text outside viewport','fixed clipping remains fail closed');assert(clipped[0].tiling.gaps.length&&!clipped[0].tiling.complete,'fixed clipping retains real coverage gaps');assert.deepEqual(clippedAfter,clippedBefore,'fixed clipping restores exact state');
  assert.equal(c.events.exceptions.length+c.events.blocked.length,0,'positive fixtures have no runtime/network errors');
  await reset(cases[0][1]);
  const driftBefore=await c.evaluate('({html:document.documentElement.outerHTML,scroll:[...document.querySelectorAll("*")].map(e=>[e.scrollLeft,e.scrollTop])})');
  await c.evaluate("window.learnCaptureRaster=async metadata=>{const result=await window.originalBridge(metadata);if(metadata.tile===1&&metadata.phase==='original')document.getElementById('owner').scrollLeft+=1;return result}");
  let error;try{await measure()}catch(e){error=e.message}rows.push({name:'deliberate noninitial tile drift',error});save();assert(error?.includes('raster setup failure: capture metrics changed'),'tile drift remains setup failure');
  const driftAfter=await c.evaluate('({html:document.documentElement.outerHTML,scroll:[...document.querySelectorAll("*")].map(e=>[e.scrollLeft,e.scrollTop])})');assert.deepEqual(driftAfter,driftBefore,'tile capture failure restores exact scroll and style state');
  await reset('<main id="owner" tabindex="0" aria-label="Position fixture"><div style="width:720px;height:400px"><span id="target" style="display:inline-block">Position label</span></div></main>');
  await c.evaluate("window.positionDriftInjected=false;window.learnCaptureRaster=async metadata=>{const result=await window.originalBridge(metadata);if(metadata.tile===0&&metadata.phase==='original'){document.getElementById('target').style.transform='translateX(1px)';window.positionDriftInjected=true}return result}");
  error=null;try{await measure()}catch(e){error=e.message}const injected=await c.evaluate('window.positionDriftInjected');rows.push({name:'target-position drift',error,injected});save();assert(injected,'position drift fixture reaches intended capture');assert(error?.includes('raster setup failure: capture metrics changed'),'target-position drift remains setup failure');
  console.log('16/16 naming, complete tiling, fixed-clipping and metadata fixtures passed');
 }finally{await c.close()}
})().catch(e=>{if(e.code==='ERR_ASSERTION')protocol.semantic(e.message.split('\n')[0]);else protocol.setup(e);process.exitCode=1});
