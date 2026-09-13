'use strict';
const fs=require('node:fs'),http=require('node:http'),path=require('node:path'),assert=require('node:assert/strict');
const ROOT=process.env.SOURCE_ROOT||path.resolve(__dirname,'..'),OUT=process.env.BROWSER_EVIDENCE;
const {launch}=require(ROOT+'/tests/browser_cdp'),protocol=require(ROOT+'/tests/mutation_protocol');
const {interceptCanvasText}=require(ROOT+'/tests/canvas_runtime_contract'),{canvasFinalRaster}=require(ROOT+'/tests/canvas_raster_contract'),{reconcileCanvasRaster}=require(ROOT+'/tests/canvas_raster_evidence');
const definition={id:'capture.label',role:'value',minimumContrast:4.5,region:'status',collision:'fixed',formatter:'literal',family:'fixture',mode:'capture',dependencies:['frame.width','frame.height','theme']};
async function main(){
 fs.mkdirSync(OUT,{recursive:true});const helper=fs.readFileSync(ROOT+'/scripts/canvas_contract.js','utf8');
 const server=http.createServer((req,res)=>{res.setHeader('Content-Type','text/html');res.end('<!doctype html><meta name=viewport content="width=device-width,initial-scale=1"><link rel=icon href=data:,><style>:root{--text:#fff;--panel-2:#071019}body{margin:0}#owner{width:280px;height:170px;overflow:auto}canvas{width:320px;height:200px}</style><div id=owner tabindex=0 aria-label="Capture fixture chart"><canvas id=chart></canvas></div>')});
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const c=await launch({dir:OUT,name:'canvas-capture',base:'http://127.0.0.1:'+server.address().port}),rows=[];
 try{
  await c.send('Page.addScriptToEvaluateOnNewDocument',{source:'('+interceptCanvasText.toString()+')()'});await c.navigate('/',{width:390,height:844,theme:'dark'});await c.evaluate(helper);await c.evaluate(canvasFinalRaster.toString());
  await c.evaluate(`window.__canvasFixtureRedraw=()=>CanvasText.frame(()=>{const ctx=CanvasText.begin(document.getElementById('chart'),320,200,2);ctx.font='600 16px monospace';CanvasText.text(ctx,CanvasText.site(${JSON.stringify(definition)}),'Stable capture',30,80)});__canvasFixtureRedraw();window.__savedCanvasRedraw=__canvasFixtureRedraw;window.__savedCanvasCapture=learnCaptureRaster;window.__tinyRaster=(()=>{const c=document.createElement('canvas');c.width=7;c.height=11;return c.toDataURL().split(',')[1]})();window.learnCaptureRaster=async metadata=>{const png=await __savedCanvasCapture(metadata);if(window.__captureFault&&metadata.phase.startsWith('isolated:')){window.__captureInjection={fault:__captureFault,metadata,injectedDecoded:__captureFault==='unequal'?[7,11]:null};if(__captureFault==='unequal')return __tinyRaster;owner.style.width='281px';window.__canvasFixtureRedraw=()=>{throw Error('fixture restoration injection')};}return png;};`);
  const measure=()=>c.evaluate('canvasFinalRaster("chart").then(result=>({result})).catch(e=>({error:e.message,code:e.code,assertion:e.assertion,evidence:window.__learnCanvasRasterEvidence,injection:window.__captureInjection}))',900000);
  const green=await measure();assert(green.result,'initial capture baseline');reconcileCanvasRaster(green.result,await c.evaluate('CanvasText.inspect()[0]'));fs.writeFileSync(OUT+'/baseline.json',JSON.stringify(green));
  for(const fault of ['unequal','capture-and-restoration']){
   await c.evaluate('window.__captureFault='+JSON.stringify(fault)+';window.__captureInjection=null');const red=await measure();
   fs.writeFileSync(OUT+'/'+fault+'-rejection.json',JSON.stringify(red));assert.equal(red.injection?.fault,fault,'capture injection must execute');assert.equal(red.code,undefined,'capture setup cannot become a semantic catch');
   if(fault==='unequal')assert.equal(red.error,'raster setup failure: dimensions changed','unequal raster remains setup');
   else{assert.match(red.error,/^raster setup failure: canvas capture metrics changed after isolated:/,'capture setup outranks restoration failure');assert.equal(red.evidence.restorationFailure.error,'fixture restoration injection');assert.equal(red.evidence.finalRestorationFailure.error,'fixture restoration injection');}
   const residue=await c.evaluate('({width:owner.style.width,restoreFunction:__canvasFixtureRedraw.toString(),scroll:[scrollX,scrollY,owner.scrollLeft,owner.scrollTop]})');fs.writeFileSync(OUT+'/'+fault+'-before-teardown.json',JSON.stringify(residue));
   await c.evaluate('window.__captureFault=null;owner.style.removeProperty("width");window.__canvasFixtureRedraw=__savedCanvasRedraw;__canvasFixtureRedraw()');const restored=await measure();assert(restored.result,'restored capture baseline');reconcileCanvasRaster(restored.result,await c.evaluate('CanvasText.inspect()[0]'));fs.writeFileSync(OUT+'/'+fault+'-restored.json',JSON.stringify(restored));rows.push({fault,reached:true,rejection:red.error,semanticRecord:false,restored:true});
  }
  fs.writeFileSync(OUT+'/observations.json',JSON.stringify(rows,null,2));assert.equal(c.events.exceptions.length,0);assert.equal(c.events.blocked.length,0);console.log('2/2 canvas setup and restoration fixtures passed');
 }finally{await c.close();await new Promise(r=>server.close(r))}
}
main().catch(e=>{if(e.code==='ERR_ASSERTION'||e.code==='LEARN_CANVAS_SEMANTIC')protocol.semantic(e.assertion||e.message.split('\n')[0]);else protocol.setup(e);process.exitCode=1});
