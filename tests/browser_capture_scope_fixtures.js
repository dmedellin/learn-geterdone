'use strict';
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const R=process.env.SOURCE_ROOT||path.resolve(__dirname,'..'),OUT=process.env.BROWSER_EVIDENCE;
const {launch}=require(R+'/tests/browser_cdp'),contracts=require(R+'/tests/browser_contracts'),protocol=require(R+'/tests/mutation_protocol');
const cases=[
 ['opaque high contrast','<span id="target">Readable opaque text</span>',true],
 ['same paint','<span id="target" style="color:#071019">Hidden same paint</span>',false],
 ['low alpha','<span id="target" style="opacity:.1">Faint semantic text</span>',false],
 ['contrasting halo','<svg width="300" height="100"><rect width="300" height="100" fill="#ddd"/><text id="target" x="10" y="40" fill="#ddd" stroke="#071019" stroke-width="4" paint-order="stroke">Contrasting halo</text></svg>',true],
 ['later occlusion','<svg width="300" height="100"><text id="target" x="10" y="40" fill="white">Occluded label</text><rect width="300" height="100" fill="#071019"/></svg>',false],
 ['native select','<select id="target" style="font:24px sans-serif;color:white;background:#071019;border:2px solid gray"><option>Selected value</option></select>',true],
 ['clipped label','<span id="target" style="position:absolute;clip:rect(0 0 0 0)">Clipped label</span>',false],
 ['DPR two','<span id="target">Readable opaque text</span>',true,2]
];
(async()=>{
 fs.mkdirSync(OUT,{recursive:true});const c=await launch({dir:OUT,name:'capture-scope',base:'http://127.0.0.1:1'}),rows=[];
 try{
  await c.send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
  for(const [name,body,passes,dpr=1] of cases){
   await c.send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:dpr,mobile:true});
   const frame=(await c.send('Page.getFrameTree')).frameTree.frame.id;
   await c.send('Page.setDocumentContent',{frameId:frame,html:'<!doctype html><meta name="viewport" content="width=device-width, initial-scale=1"><style>html,body{background:#071019;color:white;font:24px sans-serif}body{margin:8px}</style>'+body});
   await c.evaluate(Object.values(contracts).map(f=>f.toString()).join('\n'));
   const pair=[];
   for(const scope of ['viewport','target'])pair.push((await c.evaluate(`measureTextPaint([{nodeIndex:0,threshold:4.5,element:document.getElementById('target'),node:document.getElementById('target').matches('select')?null:document.getElementById('target').firstChild}],'contrast',${JSON.stringify(scope)},true)`))[0]);
   const fields=['coreEvidence','sampleCount','expectedPixels','missingPixels','ratio','foreground','background','x','y','error'];
   const values=r=>Object.fromEntries(fields.filter(k=>k in r).map(k=>[k,r[k]]));
   rows.push({name,expectedPass:passes,viewport:pair[0],target:pair[1]});fs.writeFileSync(path.join(OUT,'observations.json'),JSON.stringify(rows,null,2));
   assert.deepEqual(values(pair[1]),values(pair[0]),name+' target capture preserves exact accepted pixel samples');
   assert.equal(!pair[1].error&&pair[1].sampleCount>0&&pair[1].ratio>=4.5,passes,name+' intended raster outcome');
  }
  assert.equal(c.events.exceptions.length+c.events.blocked.length,0,'capture calibration runtime/network');
  console.log('8/8 capture scope calibrations have identical full-viewport and target pixel samples, including every measured foreground/backdrop pixel');
 }finally{await c.close()}
})().catch(e=>{if(e.code==='ERR_ASSERTION')protocol.semantic(e.message.split('\n')[0]);else protocol.setup(e);process.exitCode=1});
