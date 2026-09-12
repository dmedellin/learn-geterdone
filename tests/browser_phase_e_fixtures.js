#!/usr/bin/env node
/* Independent real-paint regression fixtures. Setup exceptions are never catches. */
'use strict';
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {launch}=require('./browser_cdp'),contracts=require('./browser_contracts');
const {refine}=require('./browser_contrast_pixels');
const protocol=require('./mutation_protocol');
const OUT=process.env.BROWSER_EVIDENCE;
assert(OUT&&!path.resolve(OUT).startsWith(path.resolve(__dirname,'..')+'/'),'external evidence required');
const svg=(body,style='')=>`<main><svg width="360" height="120" style="background:#071019;${style}">${body}</svg></main>`;
const label=(attrs='',text='Required readable label')=>`<text x="20" y="50" fill="#fff" ${attrs}>${text}</text>`;
const cases=[
 ['scaled-small-text','contrast',true,'<main><p style="font-size:28px;color:#888;background:#fff;transform:scale(.5);transform-origin:top left">Small rendered text</p></main>'],
 ['scaled-large-text','contrast',false,'<main><p style="font-size:48px;color:#888;background:#fff;transform:scale(.75);transform-origin:top left">Large rendered text</p></main>'],

 ['text-shadow-halo','contrast',false,'<main style="background:#fff;color:#fff"><p style="font:28px sans-serif;text-shadow:1px 0 #000,-1px 0 #000,0 1px #000,0 -1px #000">Readable shadow halo</p></main>'],
 ['text-shadow-faint','contrast',true,'<main style="background:#fff;color:#fff"><p style="font:28px sans-serif;text-shadow:1px 0 #0001,-1px 0 #0001,0 1px #0001,0 -1px #0001">Required shadow halo</p></main>'],

 ['accessible-icon-label','contrast',false,'<main><p>Readable heading</p><button style="width:44px;height:44px;background:#071019"><svg width="20" height="20"><circle cx="10" cy="10" r="8" fill="white"/></svg><span style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);clip-path:inset(50%);white-space:nowrap">Accessible control name</span></button></main>'],
 ['unowned-hidden-label','contrast',true,'<main><p>Readable heading</p><span style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);clip-path:inset(50%);white-space:nowrap">Required unowned label</span></main>'],

 ['disabled-value-hidden','contrast',true,'<main><h1>Readable heading</h1><input disabled value="Required displayed value" style="color:#071019;background:#071019;opacity:1"></main>'],

 ['unmeasured-viewport','geometry',true,'<main><svg width="1400" height="100"><text x="10" y="50" fill="#fff" style="font:48px sans-serif">This required label extends far beyond the captured viewport</text></svg></main>'],
 ['fully-tiled-wide-label','geometry',false,'<main><div tabindex="0" aria-label="Wide label" style="width:360px;overflow:auto"><svg width="1400" height="100"><text x="10" y="50" fill="#fff" style="font:48px sans-serif">This required label extends far beyond the captured viewport</text></svg></div></main>'],
 ['restored-long-frame','geometry',false,'<main><div style="height:6000px"></div><svg width="360" height="120" style="background:#071019"><text x="20" y="50" fill="#fff" style="font:16px sans-serif">Required distant label</text></svg></main>'],
 ['wide-label-root-overflow','layout',true,'<main><svg width="1400" height="100"><text x="10" y="50" fill="#fff" style="font:48px sans-serif">This required label extends far beyond the captured viewport</text></svg></main>'],

 ['transformed-rect-visible','geometry',false,svg('<defs><clipPath id="c"><rect width="220" height="70"/></clipPath></defs><g transform="translate(180 0) rotate(25)" clip-path="url(#c)">'+label()+'</g>')],

 ['geometry-halo','geometry',false,svg('<rect width="360" height="120" fill="#37d7e7"/>'+label('style="fill:#37d7e7" stroke="#071019" stroke-width="3" paint-order="stroke"'))],

 ['native-date-value','contrast',false,'<main><label for="v">Date</label><input id="v" type="date" value="2026-09-06" style="color:#fff;background:#071019"></main>'],
 ['native-date-hidden','contrast',true,'<main><h1>Readable heading</h1><input type="date" value="2026-09-06" style="color:#071019;background:#071019"></main>'],
 ['native-placeholder-hidden','contrast',true,'<main><h1>Readable heading</h1><input placeholder="Required placeholder" style="color:#071019;background:#071019"><style>input::placeholder{color:#071019;opacity:1}</style></main>'],
 ['group-opacity-exact','contrast',false,'<main style="background:#fff;opacity:.5"><p style="color:#111;font-size:24px">Large translucent group</p></main>'],
 ['pattern-background','contrast',false,svg('<defs><pattern id="bg" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#000"/><rect width="4" height="8" fill="#071019"/></pattern></defs><rect width="360" height="120" fill="url(#bg)"/>'+label())],

 ['semantic-opacity-zero','contrast',true,'<main><h1>Readable heading</h1><p style="opacity:0">Required invisible text</p></main>'],
 ['semantic-visibility-hidden','contrast',true,'<main><h1>Readable heading</h1><p style="visibility:hidden">Required hidden text</p></main>'],
 ['whole-svg-opacity-zero','geometry',true,svg(label(),'opacity:0')],
 ['hidden-svg-decoration','geometry',false,svg('<text aria-hidden="true" style="opacity:0" x="20" y="50">✓</text>')],
 ['scroller-in-clipped-card','layout',false,'<main><article style="width:200px;overflow:hidden"><div tabindex="0" aria-label="Wide data" style="width:100px;overflow:auto"><div style="width:400px">Reachable horizontal data extends across this entire table</div></div></article></main>'],
 ['svg-scroller-in-clipped-card','layout',false,'<main><article style="width:200px;overflow:hidden"><div tabindex="0" role="region" aria-label="Wide chart" style="width:100px;overflow:auto"><svg width="400" height="100"><text x="20" y="30">Reachable chart label</text></svg></div></article></main>'],

 ['calibration-high','contrast',false,svg(label())],
 ['calibration-same','contrast',true,svg(label('style="fill:#071019"'))],
 ['calibration-alpha','contrast',true,svg(label('fill-opacity=".05"'))],
 ['nested-group-fill-opacity','contrast',true,svg('<g opacity=".5"><g opacity=".4">'+label('fill-opacity=".3"')+'</g></g>')],
 ['webkit-ink','contrast',true,'<main><p style="color:#fff;-webkit-text-fill-color:#071019">Required actual ink</p></main>'],
 ['input-value','contrast',true,'<main><h1>Readable heading</h1><label for="v">Value</label><input id="v" value="Hidden value" style="color:#071019;background:#071019"></main>'],
 ['textarea-value','contrast',true,'<main><h1>Readable heading</h1><textarea style="color:#071019;background:#071019">Hidden value</textarea></main>'],
 ['selected-option','contrast',true,'<main><h1>Readable heading</h1><select style="color:#071019;background:#071019"><option>Hidden selected value</option><option>Unused</option></select></main>'],
 ['native-values-readable','contrast',false,'<main><label for="v">Value</label><input id="v" value="Readable input" style="color:#fff;background:#071019"><textarea style="color:#fff;background:#071019">Readable textarea</textarea><select style="color:#fff;background:#071019"><option>Readable selected value</option><option>Unused</option></select></main>'],
 ['svg-paint-occlusion','contrast',true,svg(label()+'<rect width="360" height="120" fill="#071019"/>')],
 ['html-overlay-occlusion','contrast',true,'<main style="position:relative">'+svg(label())+'<div style="position:absolute;inset:0;background:#071019"></div></main>'],
 ['gradient-white-gray','contrast',false,svg('<defs><linearGradient id="ink"><stop stop-color="#fff"/><stop offset="1" stop-color="#ddd"/></linearGradient></defs>'+label('style="fill:url(#ink)"'))],
 ['gradient-multistop','contrast',false,svg('<defs><linearGradient id="ink"><stop stop-color="#fff"/><stop offset=".4" stop-color="#bbb"/><stop offset="1" stop-color="#eee"/></linearGradient></defs>'+label('style="fill:url(#ink)"'))],
 ['gradient-bad-stop','contrast',true,svg('<defs><linearGradient id="ink"><stop stop-color="#fff"/><stop offset=".4" stop-color="#071019"/><stop offset="1" stop-color="#fff"/></linearGradient></defs>'+label('style="fill:url(#ink)"'))],
 ['pattern-ink','contrast',false,svg('<defs><pattern id="ink" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#ddd"/><rect width="4" height="8" fill="#fff"/></pattern></defs>'+label('style="fill:url(#ink)"'))],
 ['pattern-bad-ink','contrast',true,svg('<defs><pattern id="ink" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#071019"/><rect width="4" height="8" fill="#fff"/></pattern></defs>'+label('style="fill:url(#ink)"'))],
 ['gradient-background','contrast',false,'<main style="background:linear-gradient(90deg,#fff,#bbb,#eee);color:#111"><p>Readable gradient backdrop</p></main>'],
 ['gradient-background-bad','contrast',true,'<main style="background:linear-gradient(90deg,#fff,#111,#eee);color:#111;width:220px"><p>Required gradient backdrop label</p></main>'],
 ['svg-halo','contrast',false,svg('<rect width="360" height="120" fill="#37d7e7"/>'+label('style="fill:#37d7e7" stroke="#071019" stroke-width="3" paint-order="stroke"'))],
 ['svg-faint-halo','contrast',true,svg('<rect width="360" height="120" fill="#37d7e7"/>'+label('style="fill:#37d7e7" stroke="#071019" stroke-opacity=".05" stroke-width="3" paint-order="stroke"'))],
 ['html-stroke','contrast',false,'<main style="background:#37d7e7"><p style="font:28px sans-serif;color:#37d7e7;-webkit-text-stroke:2px #071019;paint-order:stroke">Readable halo</p></main>'],
 ['empty-contrast','contrast',true,'<main></main>'],
 ['empty-style-inventory','inventory',true,'<main></main>'],
 ['circular-clip','geometry',true,svg('<defs><clipPath id="c"><circle cx="0" cy="0" r="1"/></clipPath></defs>'+label('clip-path="url(#c)"'))],
 ['transformed-circle','geometry',true,svg('<defs><clipPath id="c"><circle cx="0" cy="0" r="1" transform="translate(5 4)"/></clipPath></defs><g transform="translate(25 10) rotate(8)">'+label('clip-path="url(#c)"')+'</g>')],
 ['transformed-ellipse','geometry',true,svg('<defs><clipPath id="c"><ellipse cx="40" cy="40" rx="15" ry="5" transform="rotate(20 40 40)"/></clipPath></defs><g transform="translate(20 5)">'+label('clip-path="url(#c)"')+'</g>')],
 ['transformed-polygon','geometry',true,svg('<defs><clipPath id="c"><polygon points="10,10 200,10 20,50" transform="translate(10 0)"/></clipPath></defs><g transform="translate(20 5) scale(.9)">'+label('clip-path="url(#c)"')+'</g>')],
 ['partial-glyph','geometry',true,svg('<defs><clipPath id="c"><rect x="20" y="0" width="14" height="120"/></clipPath></defs>'+label('clip-path="url(#c)"','MMMM'))],
 ['mask-invisible','geometry',true,svg('<defs><mask id="m"><rect width="360" height="120" fill="black"/></mask></defs>'+label('mask="url(#m)"'))],
 ['mask-partial','geometry',true,svg('<defs><mask id="m"><rect width="35" height="120" fill="white"/></mask></defs>'+label('mask="url(#m)"'))],
 ['geometry-svg-occlusion','geometry',true,svg(label()+'<rect width="360" height="120" fill="#071019"/>')],
 ['geometry-html-occlusion','geometry',true,'<main style="position:relative">'+svg(label())+'<div style="position:absolute;inset:0;background:#071019"></div></main>'],
 ['geometry-readable-transform','geometry',false,svg('<g transform="translate(10 10) rotate(5)">'+label()+'</g>')],
 ['geometry-readable-clip','geometry',false,svg('<defs><clipPath id="c"><ellipse cx="180" cy="60" rx="180" ry="60"/></clipPath></defs>'+label('clip-path="url(#c)"'))],
 ['hidden-decorative-svg','geometry',false,'<main><svg width="300" height="100"><g opacity="0"><circle cx="30" cy="30" r="20"/></g></svg></main>'],
 ['empty-svg','geometry',false,'<main><svg width="300" height="100"></svg></main>'],
 ['antialias-core','geometry',false,'<main style="padding-top:1500.015625px"><svg width="357" height="148.75" viewBox="0 0 360 150" style="background:#f3f8fb"><g style="font:800 12px/19.8px system-ui;letter-spacing:.48px"><text x="216" y="30" fill="#52697a">HH</text></g></svg></main>'],
 ['tiny-antialias-only','geometry',true,'<main><svg width="100" height="50" style="background:#071019"><text x="10" y="20" fill="#fff" style="font:1px system-ui">Required</text></svg></main>'],
 ['arbitrary-descendant','layout',true,'<main><div style="height:20px;overflow:hidden"><p>First label</p><p>Required second label</p></div></main>'],
 ['transformed-clipping','layout',true,'<main><div style="width:200px;height:60px;overflow:hidden"><div style="transform:translate(-80px,0)"><p>Required shifted label</p></div></div></main>'],
 ['nested-scroller','layout',false,'<main><div tabindex="0" role="region" aria-label="Data" style="width:100px;overflow:auto"><div style="width:400px"><p>Intentionally scrollable data</p></div></div></main>'],
 ['decorative-pseudo','layout',false,'<style>article{height:100px;position:relative;overflow:hidden}article:after{content:"";position:absolute;right:-50px;bottom:-50px;width:100px;height:100px;background:red}</style><main><article>Readable card</article></main>'],
];
const mutations=[
 {name:'rendered-font-threshold',case:'scaled-small-text',from:'screenFontSize(e,row.fontSize)',to:'row.fontSize'},

 {name:'text-shadow-paint',case:'text-shadow-halo',from:"||s.textShadow!=='none'",to:''},
 {name:'halo-neighborhood',case:'html-stroke',from:'sample.ratio<adequate&&dy<=radius',to:'false'},

 {name:'accessible-control-name',case:'accessible-icon-label',from:'if(accessibleControlName(e))',to:'if(false)'},

 {name:'disabled-native-inventory',case:'disabled-value-hidden',from:'const s=getComputedStyle(e),row={nodeIndex',to:"if(e.closest('[disabled]'))continue;const s=getComputedStyle(e),row={nodeIndex"},

 {name:'viewport-inventory',case:'unmeasured-viewport',from:'else if(gaps.length)measurement.error=',to:'else if(false)measurement.error='},
 {name:'restored-frame-settle',case:'restored-long-frame',from:'await settleRestoredFrame();',to:''},

 {name:'named-scroller',case:'scroller-in-clipped-card',from:'if(namedHorizontalScroller(p))',to:'if(false)'},
 {name:'named-svg-scroller',case:'svg-scroller-in-clipped-card',from:'if(namedHorizontalScroller(p)){mediaScroller=p;break;}',to:'if(false){mediaScroller=p;break;}'},
 {name:'halo-visibility',case:'geometry-halo',from:'actualDelta<1&&(!halo||sample.ratio<=1)',to:'actualDelta<1'},

 {name:'semantic-opacity-inventory',case:'semantic-opacity-zero',from:"(!native&&e.closest('textarea,select'))||!activeContent(e)",to:"(!native&&e.closest('textarea,select'))||!visible(e)"},
 {name:'semantic-svg-inventory',case:'whole-svg-opacity-zero',from:'if(!activeContent(svg))continue;',to:'if(!visible(svg))continue;'},
 {name:'subpixel-calibration',case:'group-opacity-exact',from:'if(coverage!==1)continue;',to:'if(coverage<.25)continue;'},
 {name:'svg-meaningful-core',case:'tiny-antialias-only',from:'if(coverage!==1)continue;',to:'if(coverage<.1)continue;'},

 {name:'transformed-layout',case:'transformed-clipping',from:'if(clipX||clipY) {',to:'if((clipX&&e.scrollWidth>e.clientWidth+1)||(clipY&&e.scrollHeight>e.clientHeight+1)) {'},

 {name:'clip-enforcement',case:'circular-clip',from:'actualDelta<1&&(!halo||sample.ratio<=1)',to:'false'},
 {name:'mask-enforcement',case:'mask-partial',from:'actualDelta<1&&(!halo||sample.ratio<=1)',to:'false'},
 {name:'partial-glyph-enforcement',case:'partial-glyph',from:'actualDelta<1&&(!halo||sample.ratio<=1)',to:'false'},

 {name:'opacity-composition',case:'nested-group-fill-opacity',from:'const original=await capture();',to:"for(let t=e;t;t=t.parentElement)set(t,'opacity','1');for(const t of targets)set(t,'fill-opacity','1');const original=await capture();"},
 {name:'fill-opacity',case:'calibration-alpha',from:'const original=await capture();',to:"for(const t of targets)set(t,'fill-opacity','1');const original=await capture();"},
 {name:'webkit-actual-ink',case:'webkit-ink',from:'const original=await capture();',to:"set(e,'-webkit-text-fill-color',s.color);const original=await capture();"},
 {name:'native-inventory',case:'input-value',from:"for(const control of scope.querySelectorAll('input,textarea,select'))",to:"for(const control of [])"},
 {name:'later-occlusion',case:'svg-paint-occlusion',from:'const original=await capture();',to:"for(let t=e.nextElementSibling;t;t=t.nextElementSibling)set(t,'visibility','hidden');const original=await capture();"},
 {name:'gradient-stale-color',case:'gradient-white-gray',from:'const original=await capture();',to:"set(e,'fill','#000');const original=await capture();"},
 {name:'gradient-sampling',case:'gradient-bad-stop',from:'if(!worst||sample.ratio<worst.ratio)worst=sample;',to:'if(!worst||sample.ratio>worst.ratio)worst=sample;'},
 {name:'halo-opacity',case:'svg-faint-halo',from:'const original=await capture();',to:"for(const t of targets)set(t,'stroke-opacity','1');const original=await capture();"},
 {name:'empty-inventory',case:'empty-style-inventory',from:"if(!rows.length)failures.push({reason:'no meaningful text contrast samples'});",to:''},
];
const paintInvariant=(condition,assertion)=>{if(!condition)throw Object.assign(Error(assertion),{code:'LEARN_PAINT_SEMANTIC',assertion});};
async function main(){
 const rows=[],c=await launch({dir:OUT,name:'phase-e',base:'http://127.0.0.1:1'});
 const source=Object.values(contracts).map(f=>f.toString()).join('\n');
 async function run(test,mutation){
  const [name,kind,reject,html]=test;
  await c.send('Page.setDocumentContent',{frameId:(await c.send('Page.getFrameTree')).frameTree.frame.id,html:'<!doctype html><html><head><style>html,body{background:#071019;color:#edf7ff}body{margin:8px}</style></head><body>'+html+'</body></html>'});
  let replacements=0;
  const probe={...c,evaluate:expression=>{if(mutation&&expression.includes(mutation.from)){expression=expression.replaceAll(mutation.from,mutation.to);replacements++;}return c.evaluate(expression);}};
  let measurementSource=source,tileOmission=null;
  if(name==='unmeasured-viewport'){
   const loop='for(tileIndex=0;tileIndex<captureStates.length;tileIndex++){',limited='for(tileIndex=0;tileIndex<Math.min(1,captureStates.length);tileIndex++){';
   assert.equal(measurementSource.split(loop).length-1,1,'missing-tile fixture has exactly one capture-loop anchor');
   measurementSource=measurementSource.replace(loop,limited);tileOmission={from:loop,to:limited};
  }
  await probe.evaluate(measurementSource);
  const before=await c.evaluate('document.documentElement.outerHTML');
  const restoreSettlesBefore=await c.evaluate('window.learnRasterRestoreSettles||0');
  let result=await probe.evaluate(['contrast','inventory'].includes(kind)?'renderedContrast()':kind==='geometry'?'svgGeometry()':'rootLayout()');
  if(kind==='contrast')result=await refine(probe,result);
  assert.equal(await c.evaluate('document.documentElement.outerHTML'),before,'measurement restores every authored style before assertions/cleanup');
  if(['unmeasured-viewport','fully-tiled-wide-label'].includes(name)){
   paintInvariant(result.rows.length===1,'wide-label fixture owns one semantic text occurrence');
   const paint=result.rows[0].paint,tiles=paint?.tiling;paintInvariant(tiles&&tiles.plannedTiles>1,'wide-label fixture requires multiple real tiles');
   paintInvariant(paint.sampleCount>0&&paint.expectedPixels>0,'wide-label fixture has actual glyph samples');
   if(name==='unmeasured-viewport'){
    paintInvariant(tiles.capturedTiles===1,'missing-tile fixture captures exactly one planned tile');
    paintInvariant(tiles.gaps.length>0&&!tiles.complete,'missing-tile fixture retains measured coverage gaps');
   }else{
    paintInvariant(tiles.capturedTiles===tiles.plannedTiles,'wide-label fixture captures every planned tile');
    paintInvariant(tiles.complete&&!tiles.gaps.length,'wide-label fixture reconciles complete target coverage');
    paintInvariant(paint.missingPixels===0,'wide-label fixture retains all meaningful glyph pixels');
    paintInvariant(paint.sampleCount===paint.expectedPixels,'wide-label fixture has complete final-frame samples');
    paintInvariant((await c.evaluate('rootLayout().failures')).length===0,'fully tiled wide-label owner remains named and accessible');
   }
  }
  let restoration=null;
  if(name==='restored-long-frame'){
   const restoreSettlesAfter=await c.evaluate('window.learnRasterRestoreSettles||0');
   restoration={before:restoreSettlesBefore,after:restoreSettlesAfter,
    rootRows:await c.evaluate('rootLayout().rows.length')};
  }
  const rejected=Boolean(result.failures.length);
  const calibrated=name!=='group-opacity-exact'||result.rows[0].foreground.every((x,i)=>Math.abs(x-[12,16.5,21][i])<=1);
  const correct=rejected===reject&&calibrated&&(!restoration||
   restoration.after>restoration.before&&restoration.rootRows>0);
  const pass=mutation?replacements>0&&!correct:correct;
  const row={name,kind,reject,pass,mutation:mutation?.name,replacements,tileOmission,restoration,result};
  rows.push(row);console.log(JSON.stringify({name,mutation:mutation?.name,pass,rejected,failures:result.failures.length}));
 }
 try{
  if(process.argv.includes('--batch-proof')){
   await c.send('Page.setDocumentContent',{frameId:(await c.send('Page.getFrameTree')).frameTree.frame.id,html:'<html><body style="color:#fff;background:#071019">'+Array.from({length:14},(_,i)=>'<p>Required batch label '+i+'</p>').join('')+'</body></html>'});
   await c.evaluate(source);const batches=[];
   const probe={...c,evaluate:expression=>{const match=expression.match(/const rows=(\[.*\]);/);if(match){const count=JSON.parse(match[1]).length;batches.push(count);assert(count<=4,'bounded real-paint evaluation inventory');}return c.evaluate(expression);}};
   const result=await refine(probe,await c.evaluate('renderedContrast()'));
   assert.equal(result.rows.length,14);assert.equal(result.failures.length,0);assert(batches.length>1);
   rows.push({name:'bounded-browser-evaluations',pass:true,batches,result});
  }else if(process.argv.includes('--failure-proof')){
   const empty=await refine(c,{rows:[],failures:[]});
   assert(empty.failures.length,'empty raster inventory must fail closed');
   rows.push({name:'empty-raster-inventory',pass:true,result:empty});
   await run(cases.find(t=>t[0]==='calibration-high'));
   const before=await c.evaluate('document.documentElement.outerHTML');
   await c.evaluate('window.savedCapture=window.learnCaptureRaster;window.captureCount=0;window.learnCaptureRaster=()=>++window.captureCount===2?Promise.reject(new Error("raster setup failure: planted capture failure")):window.savedCapture()');
   let error;
   try{await refine(c,await c.evaluate('renderedContrast()'));}catch(e){error=e;}
   assert.match(String(error),/raster setup failure: planted capture failure/,'a capture failure must propagate as setup, never a semantic catch');
   assert.equal(await c.evaluate('document.documentElement.outerHTML'),before,'restore after a failed capture before cleanup');
   rows.push({name:'capture-setup-failure',pass:true,classification:'SETUP_FAILURE',error:String(error)});
   await c.evaluate('window.learnCaptureRaster=window.savedCapture');
  }else if(process.argv.includes('--mutations')){
   for(const mutation of mutations){const test=cases.find(t=>t[0]===mutation.case);assert(test,'mutation fixture exists');await run(test);await run(test,mutation);}
  }else for(const test of cases){if(process.env.PHASE_E_KIND&&test[1]!==process.env.PHASE_E_KIND)continue;if(process.env.PHASE_E_CASE&&test[0]!==process.env.PHASE_E_CASE)continue;await run(test);}
 }finally{await c.close();fs.writeFileSync(path.join(OUT,'events.json'),JSON.stringify(c.events,null,2)+'\n');if(c.events.exceptions.length||c.events.blocked.length||c.events.responses.some(r=>r.status>=400))throw Error('real-paint fixture setup failure: runtime or network errors');}
 assert(rows.length,'non-vacuous selected fixtures');
 const summary={total:rows.length,passed:rows.filter(r=>r.pass).length,rows};fs.writeFileSync(path.join(OUT,'summary.json'),JSON.stringify(summary,null,2)+'\n');
 if(summary.passed!==summary.total){protocol.semantic('real-paint fixture classifications',rows.filter(r=>!r.pass).map(r=>r.name));process.exitCode=1;}
}
main().catch(e=>{if(e.code==='LEARN_PAINT_SEMANTIC')protocol.semantic(e.assertion);else protocol.setup(e);process.exitCode=1});
