'use strict';
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const R=process.env.SOURCE_ROOT||path.resolve(__dirname,'..'),OUT=process.env.BROWSER_EVIDENCE;
const {launch}=require(R+'/tests/browser_cdp'),contracts=require(R+'/tests/browser_contracts'),protocol=require(R+'/tests/mutation_protocol');
const definitions=Object.values(contracts).map(f=>f.toString()).join('\n');
const markup='<!doctype html><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{margin:0;background:#071019;color:white;font:24px sans-serif}.spacer{height:900px}#owner{width:280px;height:140px;overflow:auto}#wide{width:720px;height:180px}#target{display:inline-block;margin:12px}</style><div class="spacer"></div><main id="owner" tabindex="0" aria-label="Scrollable data"><div id="wide"><span id="target">Boundary label</span></div></main><div style="height:20px"></div>';
(async()=>{
 fs.mkdirSync(OUT,{recursive:true});const c=await launch({dir:OUT,name:'capture-frame',base:'http://127.0.0.1:1'}),rows=[];
 try{
 const reset=async()=>{
  await c.send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
  await c.send('Page.setDocumentContent',{frameId:(await c.send('Page.getFrameTree')).frameTree.frame.id,html:markup});
  await c.evaluate(definitions+';window.originalBridge=window.originalBridge||window.learnCaptureRaster;window.learnCaptureRaster=window.originalBridge;');
 };
 const measure=()=>c.evaluate("measureTextPaint([{nodeIndex:0,threshold:4.5,element:document.getElementById('target'),node:document.getElementById('target').firstChild}])");
 await reset();let error=null,normal;
 const before=await c.evaluate('document.documentElement.outerHTML');
 try{normal=await measure()}catch(e){error=e.message}
 rows.push({name:'near-boundary-scroll-owner',error,normal});
 fs.writeFileSync(path.join(OUT,'observations.json'),JSON.stringify(rows,null,2));
 assert.equal(error,null,'contrast capture frame must remain stable');
 assert(normal.length===1&&!normal[0].error&&normal[0].sampleCount>0&&normal[0].ratio>=4.5,'boundary label has real passing raster samples');
 assert.equal(await c.evaluate('document.documentElement.outerHTML'),before,'capture restores exact markup');
 await reset();
 await c.evaluate("window.fixtureCaptures=0;window.learnCaptureRaster=async metadata=>{if(++window.fixtureCaptures===2){const unequal=document.createElement('canvas');unequal.width=7;unequal.height=11;return unequal.toDataURL().split(',')[1]}return window.originalBridge(metadata)}");
 error=null;try{await measure()}catch(e){error=e.message}
 rows.push({name:'unequal-raster',error,semanticCatch:false});
 assert(error?.includes('raster setup failure: dimensions changed'),'unequal rasters must reject as setup failure');
 await reset();
 await c.evaluate("window.learnCaptureRaster=metadata=>window.originalBridge({...metadata,captureFrame:null})");
 error=null;try{await measure()}catch(e){error=e.message}
 rows.push({name:'equal-wrong-frame',error,semanticCatch:false});
 assert(error?.includes('raster setup failure: dimensions changed'),'equal wrong-frame rasters must reject as setup failure');
 await reset();
 await c.evaluate("window.fixtureCaptures=0;window.learnCaptureRaster=async metadata=>{const shot=await window.originalBridge(metadata);if(++window.fixtureCaptures===1)document.getElementById('owner').scrollLeft+=1;return shot}");
 error=null;try{await measure()}catch(e){error=e.message}
 rows.push({name:'metric-drift',error,semanticCatch:false});
 assert(error?.includes('raster setup failure: capture metrics changed'),'metric drift must reject as setup failure');
 fs.writeFileSync(path.join(OUT,'observations.json'),JSON.stringify(rows,null,2));
 assert.equal(c.events.blocked.length,0,'capture fixture network');
 console.log('4/4 capture frame fixtures pass; injected raster/metric failures remain setup failures.');
 }finally{await c.close()}
})().catch(e=>{if(e.code==='ERR_ASSERTION')protocol.semantic(e.message.split('\n')[0]);else protocol.setup(e);process.exitCode=1});
