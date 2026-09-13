#!/usr/bin/env node
/* Complete final-pixel records for initial states. This is one component of
 * finite canvas acceptance, and never asserts finite state-space closure. */
'use strict';
const fs=require('node:fs'),path=require('node:path'),http=require('node:http');
const ROOT=path.resolve(process.env.SOURCE_ROOT||path.join(__dirname,'..')),OUT=process.env.BROWSER_EVIDENCE;
const {inventory}=require(ROOT+'/scripts/canvas_sources'),{launch}=require(ROOT+'/tests/browser_cdp'),protocol=require(ROOT+'/tests/mutation_protocol'),contracts=require(ROOT+'/tests/browser_contracts');
const {interceptCanvasText,reconcileRuntime}=require(ROOT+'/tests/canvas_runtime_contract');
const {canvasFinalRaster}=require(ROOT+'/tests/canvas_raster_contract'),{reconcileCanvasRaster}=require(ROOT+'/tests/canvas_raster_evidence'),{reconcileCanvasArtifacts}=require(ROOT+'/tests/canvas_raster_artifacts');
const {reconcileInitialStates}=require('./canvas_initial_evidence');
const fail=assertion=>{throw Object.assign(Error(assertion),{assertion,code:'LEARN_CANVAS_SEMANTIC'})};
async function main(){
 if(!OUT||path.resolve(OUT)===ROOT||path.resolve(OUT).startsWith(ROOT+'/'))throw Error('external canvas evidence required');
 fs.mkdirSync(OUT,{recursive:true});if(fs.existsSync(path.join(OUT,'observations.jsonl')))throw Error('fresh canvas evidence required');
 const args=process.argv.slice(2);if(args.some(a=>a!=='--mobile-only'&&!a.startsWith('--only=')))throw Error('unknown canvas initial-state selection');
 const only=args.find(a=>a.startsWith('--only='))?.slice(7),mobile=args.includes('--mobile-only'),source=inventory(ROOT);
 fs.writeFileSync(path.join(OUT,'source-inventory.json'),JSON.stringify(source));if(source.errors.length)fail(source.errors[0].assertion);
 const pages=source.pages.filter(p=>p.canvases.length&&(!only||p.route===only));if(!pages.length||only&&pages.length!==1)fail('empty canvas initial-state selection');
 const viewports=mobile?[[390,844]]:[[320,800],[390,844],[1440,900]],themes=mobile?['dark']:['dark','system-light','explicit-light'];
 const plan=pages.flatMap(page=>viewports.flatMap(([width,height])=>themes.map(theme=>({page,width,height,theme}))));
 fs.writeFileSync(path.join(OUT,'plan.json'),JSON.stringify({phase:'initial',finiteProofComplete:false,sourceRoutes:source.htmlRoutes,selectedRoutes:pages.map(p=>p.route),viewports,themes,states:plan.length},null,2));
 const server=http.createServer((req,res)=>{try{let file=path.resolve(ROOT,'site','.'+decodeURIComponent(req.url.split('?')[0]));if(!file.startsWith(ROOT+'/site/'))throw Error('path');if(fs.statSync(file).isDirectory())file=path.join(file,'index.html');res.setHeader('Content-Type','text/html; charset=utf-8');res.end(fs.readFileSync(file));}catch{res.writeHead(404);res.end()}});
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const rows=[];
 const functions=Object.values(contracts).map(f=>f.toString()).join('\n');
 try{for(const [pageIndex,pageOwner]of pages.entries()){
  const name='canvas-initial-'+pageIndex,c=await launch({dir:OUT,name,base:'http://127.0.0.1:'+server.address().port});
  try{
  await c.send('Page.addScriptToEvaluateOnNewDocument',{source:'('+interceptCanvasText.toString()+')()'});
  for(const [stateIndex,{page,width,height,theme}]of plan.entries()){
   if(page!==pageOwner)continue;
   const state={index:stateIndex,route:page.route,sourceHash:page.sha256,width,height,theme,state:'initial'};
   await c.navigate(page.route,{width,height,theme});await c.evaluate(functions+'\n'+canvasFinalRaster.toString());
   const value=await c.evaluate(`(()=>{__learnCanvasNative.clear();const redraw=window.redrawLab||window.redraw||window.drawCurrent;if(typeof redraw!=='function')throw Error('canvas redraw entry missing');redraw();return {live:CanvasText.inspect(),native:__learnCanvasNative.snapshot()}})()`);
   const runtime=reconcileRuntime(page,value.live,value.native),layout=await c.evaluate('rootLayout()'),actualTheme=await c.evaluate('themeState('+JSON.stringify(theme)+')');
   fs.writeFileSync(path.join(OUT,stateIndex+'-runtime.json'),JSON.stringify({state,value,runtime,layout,actualTheme}));
   if(layout.failures.length)fail(layout.failures[0].reason);if(actualTheme.failures.length)fail(actualTheme.failures[0].reason);
   for(const canvas of page.canvases){
    const observed=await c.evaluate(`canvasFinalRaster(${JSON.stringify(canvas.id)}).then(result=>({result})).catch(e=>({error:e.message,assertion:e.assertion||null,code:e.code||null,evidence:window.__learnCanvasRasterEvidence||null}))`,900000);
    const file=stateIndex+'-'+canvas.id+'-raster.json';fs.writeFileSync(path.join(OUT,file),JSON.stringify(observed));
    let proof=null,artifactProof=null;
    if(observed.error){if(observed.code==='LEARN_CANVAS_SEMANTIC')fail(observed.assertion);throw Error(observed.error);}
    if(!observed.result.inactive){
     const expected=value.live.find(f=>f.canvas===canvas.id);proof=reconcileCanvasRaster(observed.result,expected);
     const frames=fs.readFileSync(path.join(OUT,name+'-raster-frames.jsonl'),'utf8').trim().split('\n').map(JSON.parse);
     artifactProof=reconcileCanvasArtifacts(observed.result,expected,{directory:OUT,frames});
     fs.writeFileSync(path.join(OUT,stateIndex+'-'+canvas.id+'-artifact-proof.json'),JSON.stringify(artifactProof));
    }
    const row={...state,canvas:canvas.id,file,runtime,proof,artifactProof,inactive:observed.result.inactive||false,events:structuredClone(c.events)};rows.push(row);fs.appendFileSync(path.join(OUT,'observations.jsonl'),JSON.stringify(row)+'\n');
    if(row.events.exceptions.length||row.events.blocked.length||row.events.responses.some(r=>r.status>=400))throw Error('canvas runtime/network setup failure');
    console.log(JSON.stringify({...state,canvas:canvas.id,inactive:row.inactive,labels:proof?.labels||0,samples:proof?.coreSamples||proof?.samples||0}));
   }
  }
  }finally{await c.close();}
 }}finally{await new Promise(r=>server.close(r));}
 const summary=reconcileInitialStates(plan,rows);
 fs.writeFileSync(path.join(OUT,'summary.json'),JSON.stringify(summary,null,2));console.log(JSON.stringify(summary));
}
if(require.main===module)main().catch(e=>{if(e.code==='LEARN_CANVAS_SEMANTIC')protocol.semantic(e.assertion);else protocol.setup(e);process.exitCode=1});
