#!/usr/bin/env node
/* Exercise the contracts with actual Chromium layout, including negative and
 * non-vacuity fixtures. No site content or source is modified. */
'use strict';
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {launch}=require('./browser_cdp'),contracts=require('./browser_contracts');
const {refine}=require('./browser_contrast_pixels');
const OUT=process.env.BROWSER_EVIDENCE;
assert(OUT&&!path.resolve(OUT).startsWith(path.resolve(__dirname,'..')+'/'),'external evidence required');
const functions=Object.values(contracts).map(f=>f.toString()).join('\n');
async function main(){
 const c=await launch({dir:OUT,name:'contract-fixtures',base:'http://127.0.0.1:1'}),rows=[];
 async function check(name,markup,expression,message,raster=false){
  await c.send('Page.setDocumentContent',{frameId:(await c.send('Page.getFrameTree')).frameTree.frame.id,html:'<!doctype html><html data-theme="dark"><head><style>:root{--bg:#071019;--text:#edf7ff}body{background:var(--bg);color:var(--text)}</style></head><body>'+markup+'</body></html>'});
  let result=await c.evaluate('(()=>{'+functions+';return '+expression+'})()');
  if(raster)result=await refine(c,result);
  if(name==='inherited group opacity'){
   const foreground=result.rows[0].foreground;
   assert(foreground.every((x,i)=>Math.abs(x-[12,16.5,21][i])<=1),'opacity compositing foreground must use the exterior backdrop');
  }
  const pass=message?result.failures.some(f=>JSON.stringify(f).includes(message)):result.failures.length===0;
  rows.push({name,message,result,pass});console.log((pass?'PASS ':'FAIL ')+name+' '+JSON.stringify(result));
 }
 try{
  await check('content clipping','<main style="height:20px;overflow:hidden"><p>One line</p><p>Another line</p></main>','rootLayout()','clipped content owner');
  await check('empty content owners','<p>Only body text</p>','rootLayout()','no visible content owners');
  await check('visible semantic SVG','<main><svg width="300" height="100"><text x="10" y="30">Required label</text></svg></main>','svgGeometry()');
  await check('all semantic SVG labels hidden','<main><svg width="300" height="100"><text style="opacity:0" x="10" y="30">Required label</text></svg></main>','svgGeometry()','no readable semantic SVG labels');
  await check('one-to-one dark text','<style>:root{--text:var(--bg)}</style><main><p>Meaningful text</p></main>',"themeState('dark')",'text contrast');
  await check('vertical root masking','<style>body{overflow-y:hidden}</style><main>Readable</main>','rootLayout()','root masking');
  await check('named keyboard scroller','<main><div tabindex="0" role="region" aria-label="Data table" style="width:100px;overflow:auto"><div style="width:300px">Wide data</div></div></main>','rootLayout()');
  await check('unlabelled scroller','<main><div style="width:100px;overflow:auto"><div style="width:300px">Wide data</div></div></main>','rootLayout()','unnamed or unfocusable horizontal scroller');
  await check('inactive slide SVG','<section style="display:none"><svg width="300" height="100"><text style="opacity:0">Inactive label</text></svg></section>','svgGeometry()');
  await check('text-free decorative SVG','<svg width="300" height="100"><circle cx="30" cy="30" r="20"/></svg>','svgGeometry()');
  await check('all semantic SVG offscale','<svg width="300" height="100"><text x="900" y="30">Required label</text></svg>','svgGeometry()','no readable semantic SVG labels');
  await check('all semantic SVG clipped','<svg width="300" height="100"><text x="-10" y="30">Required label</text></svg>','svgGeometry()','no readable semantic SVG labels');
  await check('literal SVG entity','<svg width="300" height="100"><text x="10" y="30">&amp;asymp;</text></svg>','svgGeometry()','"entity":true');
  await check('rendered contrast ignores unrelated token health','<p style="color:#071019">Meaningful text</p>','renderedContrast()','text contrast below threshold');
  await check('alpha text','<p style="color:rgba(237,247,255,.1)">Meaningful text</p>','renderedContrast()','text contrast below threshold');
  await check('inherited background','<main style="background:#fff;color:#111"><section><p>Readable inherited text</p></section></main>','renderedContrast()');
  await check('large qualifying text','<p style="background:#fff;color:#888;font-size:24px">Large text</p>','renderedContrast()');
  await check('normal text threshold','<p style="background:#fff;color:#888;font-size:16px">Normal text</p>','renderedContrast()','text contrast below threshold');
  await check('hidden decorative glyph','<p>Readable</p><span aria-hidden="true" style="color:transparent">✓</span>','renderedContrast()');
  await check('meaningful labels cannot be exempted','<span aria-hidden="true" style="color:transparent">Intrinsic</span>','renderedContrast()','text contrast below threshold');
  await check('empty contrast scope','<section></section>','renderedContrast()','no meaningful text contrast samples');
  await check('contrast measurement error','<p style="background-image:url(data:image/png;base64,AA==)">Unresolved paint</p>','renderedContrast()','text contrast measurement error');
  await check('gradient and alpha backgrounds','<main style="background:linear-gradient(#fff,#eee);color:#111"><p style="background:rgba(255,255,255,.5)">Readable gradient</p></main>','renderedContrast()');
  await check('decorative owner glow','<style>article{height:100px;position:relative;overflow:hidden}article:after{content:"";position:absolute;right:-50px;bottom:-50px;width:100px;height:100px;background:red}</style><main><article>Readable card</article></main>','rootLayout()');
  await check('SVG sibling paint raster','<svg width="300" height="100"><rect width="300" height="100" fill="#fff"/><text x="10" y="30" fill="#111">Readable label</text></svg>','renderedContrast()',null,true);
  await check('SVG true failure raster','<svg width="300" height="100"><rect width="300" height="100" fill="#071019"/><text x="10" y="30" fill="#071019">Unreadable label</text></svg>','renderedContrast()','text contrast below threshold',true);
  await check('SVG same accent paint','<svg width="300" height="100"><rect width="300" height="100" fill="#37d7e7"/><text x="10" y="30" fill="#37d7e7">Unreadable accent label</text></svg>','renderedContrast()','text contrast below threshold',true);
  await check('SVG contrasting halo','<svg width="300" height="100"><rect width="300" height="100" fill="#37d7e7"/><text x="10" y="30" fill="#37d7e7" stroke="#071019" stroke-width="3" paint-order="stroke">Readable halo label</text></svg>','renderedContrast()',null,true);
  await check('inherited group opacity','<main style="background:#fff;opacity:.5"><p style="color:#111;font-size:24px">Large translucent group</p></main>','renderedContrast()',null,true);
  await check('translucent group negative','<style>body{background:#fff}</style><main style="background:#000;opacity:.5"><p style="color:#fff">Translucent white label</p></main>','renderedContrast()','text contrast below threshold',true);
  await check('nested opacity groups','<style>body{background:#fff}</style><main style="background:#000;opacity:.5"><section style="background:#fff;opacity:.5"><p style="color:#fff">Nested translucent label</p></section></main>','renderedContrast()','text contrast below threshold',true);
 }finally{await c.close();}
 const summary={passed:rows.filter(r=>r.pass).length,failed:rows.filter(r=>!r.pass).length,rows};
 fs.writeFileSync(path.join(OUT,'summary.json'),JSON.stringify(summary,null,2)+'\n');
 assert.equal(summary.failed,0,'browser contracts must reject intended negative fixtures');
}
main().catch(e=>{console.error(e.stack);process.exitCode=1});
