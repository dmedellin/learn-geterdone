'use strict';
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const R=process.env.SOURCE_ROOT||path.resolve(__dirname,'..'),OUT=process.env.BROWSER_EVIDENCE;
const {launch}=require(R+'/tests/browser_cdp'),contracts=require(R+'/tests/browser_contracts'),protocol=require(R+'/tests/mutation_protocol');
const {reconcileTextTiles}=require(R+'/tests/text_tile_contract');
const {reconcileSvgRaster}=require(R+'/tests/svg_raster_evidence');
async function nativeMask(){
 const target=document.getElementById('target'),nodes=[target,...target.querySelectorAll('*')],backgrounds=[document.documentElement,document.body],all=[...document.querySelectorAll('*')],styles=all.map(e=>e.getAttribute('style'));
 for(const e of all)e.style.setProperty('visibility','hidden','important');
 for(const e of [...backgrounds,...nodes])e.style.setProperty('visibility','visible','important');
 for(const e of backgrounds)e.style.setProperty('background','#7f7f7f','important');
 const rect=target.getBoundingClientRect(),strokeOnly=getComputedStyle(target).fill==='none';
 async function capture(ink){
  for(const e of nodes){e.style.setProperty('fill',strokeOnly?'none':ink,'important');e.style.setProperty('-webkit-text-fill-color',ink,'important');e.style.setProperty('stroke',strokeOnly?ink:'transparent','important');}
  await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
  const image=new Image();image.src='data:image/png;base64,'+await learnCaptureRaster({mode:'svg-native-mask-calibration',phase:ink,metrics:{innerWidth,innerHeight,devicePixelRatio,scrollX,scrollY}});await image.decode();
  if(image.width!==innerWidth*2*devicePixelRatio||image.height!==innerHeight*2*devicePixelRatio)throw Error('raster setup failure: native calibration dimensions');
  const canvas=document.createElement('canvas');canvas.width=image.width;canvas.height=image.height;const ctx=canvas.getContext('2d');ctx.drawImage(image,0,0);return {width:image.width,height:image.height,data:ctx.getImageData(0,0,image.width,image.height).data};
 }
 try{
  const black=await capture('#000'),white=await capture('#fff'),pixels=[],scale=2*devicePixelRatio;
  for(let y=Math.max(0,Math.floor(rect.top*scale));y<Math.min(black.height,Math.ceil(rect.bottom*scale));y++)for(let x=Math.max(0,Math.floor(rect.left*scale));x<Math.min(black.width,Math.ceil(rect.right*scale));x++){
   const i=(y*black.width+x)*4;if(Math.min(...[0,1,2].map(k=>Math.abs(white.data[i+k]-black.data[i+k])))/255===1)pixels.push([x/scale,y/scale]);
  }
  return pixels;
 }finally{all.forEach((e,i)=>{e.setAttribute('style',styles[i]||'');e.getAttribute('style');if(styles[i]===null)e.removeAttribute('style')});}
}
const fixtures=[
 ['plain native SVG','<text id="target" x="16" y="55">Readable label</text>',true],
 ['transformed native SVG','<g transform="translate(35 65) rotate(9)"><text id="target" x="0" y="0" transform="scale(1.05 .95)">Rotated label</text></g>',true],
 ['native tspan layout','<text id="target" x="16" y="48">Label <tspan dx="3" dy="5" font-size="18">subscript</tspan><tspan x="16" dy="32">Second line</tspan></text>',true],
 ['native halo','<text id="target" x="16" y="55" fill="#ddd" stroke="#071019" stroke-width="4" paint-order="stroke">Halo label</text>',true],
 ['fractional SVG viewport','<g style="font:800 12px/19.8px system-ui;letter-spacing:.48px"><text id="target" x="88" y="29" fill="white" stroke="#071019" stroke-width="3" paint-order="stroke">SIGNAL</text></g>',true,{width:'285.975',height:'119.15625',viewBox:'0 0 360 150',style:'position:relative;left:17.0125px;top:337.4px'}],
 ['scrolled fractional small SVG','<g style="font:800 12px/19.8px system-ui;letter-spacing:.48px"><text id="target" x="216" y="30" fill="#52697a">HH</text></g>',true,{width:'357',height:'148.75',viewBox:'0 0 360 150',style:'position:relative;left:17px;top:1500.015625px;background:#f3f8fb'},1000],
 ['native stroke only','<text id="target" x="16" y="55" fill="none" stroke="white" stroke-width="2">Outline label</text>',true],
 ['SVG clip path','<defs><clipPath id="cut"><rect x="0" y="0" width="75" height="150"/></clipPath></defs><text id="target" x="16" y="55" clip-path="url(#cut)">Clipped label</text>',false],
 ['later total paint','<text id="target" x="16" y="55">Covered label</text><rect width="360" height="180" fill="#071019"/>',false],
 ['later partial paint','<text id="target" x="16" y="55">Partial label</text><rect x="30" y="30" width="12" height="40" fill="#071019"/>',false],
 ['zero opacity','<text id="target" x="16" y="55" opacity="0">Invisible label</text>',false]
];
(async()=>{
 fs.mkdirSync(OUT,{recursive:true});const c=await launch({dir:OUT,name:'svg-isolation',base:'http://127.0.0.1:1'}),rows=[];
 const save=()=>fs.writeFileSync(path.join(OUT,'observations.json'),JSON.stringify(rows,null,2));
 const reset=async body=>{
  await c.send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
  await c.send('Page.setDocumentContent',{frameId:(await c.send('Page.getFrameTree')).frameTree.frame.id,html:'<!doctype html><meta name="viewport" content="width=device-width, initial-scale=1"><style>html,body{margin:0;background:#071019;color:white}svg{display:block;font:24px sans-serif;fill:white}#port{width:240px;height:120px;overflow:auto;scroll-behavior:smooth}</style>'+body});
  await c.evaluate(nativeMask.toString()+'\n'+Object.values(contracts).map(f=>f.toString()).join('\n')+';window.originalBridge=window.originalBridge||window.learnCaptureRaster;window.learnCaptureRaster=window.originalBridge;');
 };
 const state=()=>c.evaluate('({html:document.documentElement.outerHTML,scroll:[...document.querySelectorAll("*")].map(e=>[e.scrollLeft,e.scrollTop])})');
 const measure=(scope='viewport')=>c.evaluate("measureTextPaint([{nodeIndex:0,element:document.getElementById('target')}],'geometry',"+JSON.stringify(scope)+",true)");
 try{
  for(const [name,content,passes,attributes={width:'360',height:'180',viewBox:'0 0 360 180'},initialScroll=0] of fixtures){
   await reset('<svg '+Object.entries(attributes).map(([k,v])=>k+'="'+v+'"').join(' ')+'>'+content+'</svg>');
   if(initialScroll)await c.evaluate(`(()=>{document.body.style.minHeight='2800px';scrollTo(0,${initialScroll});document.getElementById('target').ownerSVGElement.scrollIntoView({block:'center',inline:'center',behavior:'instant'});return new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))})()`);
   const before=await state(),result=(await measure())[0],targetPaint=(await measure('target'))[0],nativePixels=passes?await c.evaluate('nativeMask()'):null,after=await state();
   rows.push({name,expectedPass:passes,result,targetPaint,nativePixels,before,after,restored:JSON.stringify(before)===JSON.stringify(after)});save();
   const fields=['coreEvidence','sampleCount','expectedPixels','missingPixels','ratio','foreground','background','x','y','error'];
   const sampled=p=>Object.fromEntries(fields.filter(k=>k in p).map(k=>[k,p[k]]));
   assert.deepEqual(sampled(targetPaint),sampled(result),name+' exact target and viewport samples');
   if(nativePixels)assert.deepEqual(result.coreEvidence.map(p=>p.slice(0,2)),nativePixels,name+' isolated mask equals native glyph-core mask');
   assert.equal(!result.error&&result.sampleCount>0&&result.missingPixels===0,passes,name+' intended geometry assertion');
   if(!passes)assert.equal(result.error,'semantic SVG glyph pixels absent, clipped, masked or occluded',name+' exact semantic reason');
   assert.deepEqual(after,before,name+' restores layout and scroll');
  }
  await reset('<svg width="360" height="180"><text id="first" x="16" y="55">Initially visible label</text></svg><svg width="360" height="180" style="margin-top:1200px"><text id="second" x="16" y="55">Initially offscreen label</text></svg>');
  {
   // Reproduce a stable camera whose first post-fence SVG raster lacks the
   // glyph. Later untouched rasters are identical and must become the accepted
   // foreground only after consecutive pixel equality.
   await c.evaluate(`window.fixtureSettleKeys=new Set();window.fixtureSettlePhases=0;window.fixtureUntouchedCaptures=0;window.learnCaptureRaster=async metadata=>{const key=metadata.nodeIndex+':'+metadata.tile;if(metadata.phase==='settle'){window.fixtureSettleKeys.add(key);window.fixtureSettlePhases++;window.fixtureUntouchedCaptures++;return window.originalBridge(metadata)}if(metadata.phase==='original'){window.fixtureUntouchedCaptures++;if(window.fixtureSettleKeys.delete(key)){const e=document.getElementById(metadata.site),style=e.getAttribute('style');e.style.setProperty('visibility','hidden','important');await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));try{return await window.originalBridge(metadata)}finally{e.setAttribute('style',style||'');if(style===null)e.removeAttribute('style')}}}return window.originalBridge(metadata)}`);
   const before=await state(),result=await c.evaluate('svgGeometry()'),after=await state();
   const settlePhases=await c.evaluate('window.fixtureSettlePhases'),untouchedCaptures=await c.evaluate('window.fixtureUntouchedCaptures');
   rows.push({name:'offscreen sibling SVG consecutive untouched settle',expectedPass:true,settlePhases,untouchedCaptures,result,restored:JSON.stringify(before)===JSON.stringify(after)});save();
   assert.equal(result.rows.length,2,'offscreen sibling fixture owns both semantic labels');
   assert.equal(settlePhases,2,'one initial untouched capture starts each semantic SVG tile');
   assert.equal(untouchedCaptures,8,'each stale first original is followed by two equal untouched rasters');
   assert.equal(result.failures.length,0,'offscreen sibling labels retain final glyph paint after camera movement');
   for(const row of result.rows){const tile=row.paint.tiling.tiles[0];assert.equal(tile.settleCaptures,3,'each SVG tile records all frames before its accepted original');assert.equal(tile.untouchedCaptures,4,'each SVG tile records its full bounded stability sequence');assert.equal(tile.untouchedFramesEqual,true,'accepted untouched frames agree exactly');assert.equal(reconcileTextTiles(row.paint),true,'offscreen sibling tile evidence reconciles');}
   assert.deepEqual(after,before,'offscreen sibling measurement restores layout and scroll');
  }
  await reset('<svg width="360" height="180"><text id="target" x="16" y="55">Never stable label</text></svg>');
  {
   await c.evaluate(`window.fixtureOscillatingCaptures=0;window.learnCaptureRaster=async metadata=>{if(metadata.phase!=='settle'&&metadata.phase!=='original')return window.originalBridge(metadata);const hide=window.fixtureOscillatingCaptures++%2===1;if(!hide)return window.originalBridge(metadata);const e=document.getElementById(metadata.site),style=e.getAttribute('style');e.style.setProperty('visibility','hidden','important');await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));try{return await window.originalBridge(metadata)}finally{e.setAttribute('style',style||'');if(style===null)e.removeAttribute('style')}}`);
   let error;try{await measure()}catch(e){error=e.message}
   const captures=await c.evaluate('window.fixtureOscillatingCaptures');rows.push({name:'oscillating untouched SVG frame guard',error,captures,semanticCatch:false});save();
   assert.equal(captures,6,'untouched stability guard reaches its bounded final attempt');
   assert(error?.includes('raster setup failure: untouched frame did not settle'),'perpetual untouched raster drift remains setup rejection');
  }
  const wide='<svg width="720" height="420"><text id="target" x="10" y="70" font-size="30">Horizontal complete glyph coverage<tspan x="10" y="370">Vertical complete glyph coverage</tspan></text></svg>';
  for(const [name,attrs,passes] of [
   ['named focusable scroll owner','tabindex="0" aria-label="Chart labels"',true],
   ['unnamed owner','tabindex="0"',false],
   ['unfocusable owner','aria-label="Chart labels"',false],
   ['hidden outer clipping','tabindex="0" aria-label="Chart labels" style="overflow:hidden"',false]
  ]){
   await reset('<div id="port" '+attrs+'>'+wide+'</div>');
   const before=await state(),result=(await measure())[0],after=await state();
   rows.push({name,expectedPass:passes,result,restored:JSON.stringify(before)===JSON.stringify(after)});save();
   assert.equal(!result.error&&result.sampleCount>0&&result.missingPixels===0,passes,name+' intended geometry assertion');
   if(passes){assert(result.tiling.capturedTiles>1,'off-port SVG glyphs need real tiles');assert.equal(reconcileTextTiles(result),true,'complete independent SVG tile reconciliation');}
   else assert.equal(result.error,'unmeasured semantic text outside viewport',name+' exact semantic reason');
   assert.deepEqual(after,before,name+' exact restoration');
  }
  assert.equal(c.events.exceptions.length+c.events.blocked.length,0,'SVG isolation runtime/network');
  const good=rows.find(r=>r.name==='named focusable scroll owner').result;
  assert.equal(reconcileSvgRaster({rows:[{paint:good}],failures:[]}),true,'positive SVG visibility evidence');
  for(const [name,change,reason] of [
   ['missing SVG identity',r=>{delete r.rows[0].paint.nodeIndex},'missing SVG raster identity'],
   ['missing SVG raster phase',r=>{delete r.rows[0].paint.tiling.tiles[0].captures},'incomplete tile capture phases'],
   ['missing SVG settle proof',r=>{delete r.rows[0].paint.tiling.tiles[0].settleCaptures},'incomplete tile frame metadata'],
   ['missing SVG untouched count',r=>{delete r.rows[0].paint.tiling.tiles[0].untouchedCaptures},'incomplete tile frame metadata'],
   ['missing SVG stable-frame equality',r=>{delete r.rows[0].paint.tiling.tiles[0].untouchedFramesEqual},'incomplete tile frame metadata'],
   ['missing SVG tile',r=>{r.rows[0].paint.tiling.tiles.pop()},'incomplete tile metadata'],
   ['missing SVG samples',r=>{r.rows[0].paint.sampleCount++},'tile sample reconciliation mismatch']
  ]){
   const record={rows:[{paint:JSON.parse(JSON.stringify(good))}],failures:[]};change(record);
   let error;try{reconcileSvgRaster(record)}catch(e){error=e.message}
   rows.push({name,error,semanticCatch:false});save();assert.equal(error,'raster setup failure: '+reason,name+' remains setup rejection');
  }
  for(const fault of ['unequal','metric']){
   await reset('<svg width="360" height="180"><text id="target" x="16" y="55">Guarded label</text></svg>');
   await c.evaluate(`window.fixtureInjected=false;window.learnCaptureRaster=async metadata=>{const image=await window.originalBridge(metadata);if(metadata.phase==='backdrop'){window.fixtureInjected=true;if(${JSON.stringify(fault)}==='metric')document.getElementById('target').setAttribute('x','17');else{const canvas=document.createElement('canvas');canvas.width=7;canvas.height=11;return canvas.toDataURL().split(',')[1]}}return image}`);
   let error;try{await measure()}catch(e){error=e.message}
   const injected=await c.evaluate('window.fixtureInjected');rows.push({name:'SVG '+fault+' guard',error,injected,semanticCatch:false});save();assert(injected,'SVG '+fault+' fixture reaches intended capture');assert(error?.includes('raster setup failure: '+(fault==='metric'?'capture metrics changed':'dimensions changed')),'SVG '+fault+' remains setup rejection');
  }

  console.log(rows.length+'/'+rows.length+' SVG isolation and owned scrolling fixtures passed');
 }finally{await c.close()}
})().catch(e=>{if(e.code==='ERR_ASSERTION')protocol.semantic(e.message.split('\n')[0]);else protocol.setup(e);process.exitCode=1});
