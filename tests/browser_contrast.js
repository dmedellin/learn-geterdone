#!/usr/bin/env node
/* Rendered text contrast across page families and every capstone slide/state.
 * Uses local candidate documents only; browser_cdp blocks other requests. */
'use strict';
const fs=require('node:fs'),path=require('node:path'),http=require('node:http'),assert=require('node:assert/strict');
const {launch}=require('./browser_cdp'),contracts=require('./browser_contracts');
const {refine}=require('./browser_contrast_pixels');
const ROOT=path.resolve(process.env.SOURCE_ROOT||path.join(__dirname,'..')),SITE=path.join(ROOT,'site'),OUT=process.env.BROWSER_EVIDENCE;
assert(OUT&&!path.resolve(OUT).startsWith(ROOT+'/'),'external evidence required');
fs.mkdirSync(OUT,{recursive:true});assert(!fs.existsSync(path.join(OUT,'observations.jsonl')),'fresh evidence required');
const capOnly=process.argv.includes('--capstones'),only=process.argv.find(a=>a.startsWith('--only='))?.slice(7);
const corpus=[];function walk(dir){for(const entry of fs.readdirSync(dir,{withFileTypes:true})){const file=path.join(dir,entry.name);if(entry.isDirectory())walk(file);else if(entry.name.endsWith('.html')){const source=fs.readFileSync(file,'utf8');corpus.push({file,route:'/'+path.relative(SITE,file).replace(/index\.html$/,''),kind:source.match(/<body data-page-kind="([^"]+)"/)?.[1]||'fallback',source});}}}walk(SITE);
assert.equal(corpus.length,369,'complete corpus');
const caps=corpus.filter(p=>['slides','supplemental'].includes(p.kind));assert.equal(caps.length,2,'both capstone capabilities');
const seen=new Set(),families=corpus.sort((a,b)=>a.route.localeCompare(b.route)).filter(p=>{
 if(p.kind!=='lesson')return true;
 const course=p.route.split('/')[1];if(seen.has(course))return false;seen.add(course);return true;
});assert.equal(seen.size,25,'one Lesson from each Course');
const selected=only?corpus.filter(p=>p.route===only):capOnly?caps:families;
assert(selected.length,'nonempty contrast selection');
const server=http.createServer((req,res)=>{try{let file=path.join(SITE,decodeURIComponent(req.url.split('?')[0]));if(!file.startsWith(SITE+'/')&&file!==SITE)throw Error('outside site');if(fs.statSync(file).isDirectory())file=path.join(file,'index.html');res.setHeader('Content-Type','text/html; charset=utf-8');res.end(fs.readFileSync(file));}catch{res.writeHead(404);res.end();}});
const functions=Object.values(contracts).map(f=>f.toString()).join('\n'),rows=[];
async function main(){
 await new Promise(r=>server.listen(0,'127.0.0.1',r));
 const c=await launch({dir:OUT,name:'contrast',base:'http://127.0.0.1:'+server.address().port});
 async function measure(page,width,height,theme,state){
  await c.evaluate('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');
  const result=await refine(c,await c.evaluate('renderedContrast()'));
  const row={route:page.route,kind:page.kind,width,height,theme,state,...result};rows.push(row);
  fs.appendFileSync(path.join(OUT,'observations.jsonl'),JSON.stringify(row)+'\n');
  console.log((result.failures.length?'FAIL':'PASS')+' contrast '+page.route+' '+width+' '+theme+' '+state+' samples='+result.rows.length+' failures='+result.failures.length+' '+JSON.stringify(result.failures.slice(0,2)));
  if(caps.includes(page)&&['initial','slide-16','active-states'].includes(state)){
   await c.evaluate('window.scrollTo(0,0)');
   const shot=await c.send('Page.captureScreenshot',{format:'png',captureBeyondViewport:false});
   fs.writeFileSync(path.join(OUT,page.kind+'-'+width+'-'+theme+'-'+state+'.png'),Buffer.from(shot.data,'base64'));
  }
 }
 try{
  for(const page of selected)for(const [width,height] of [[390,844],[1440,900]])for(const theme of ['dark','system-light','explicit-light']){
   await c.navigate(page.route,{width,height,theme});await c.evaluate(functions);
   const policy=await c.evaluate('themeState('+JSON.stringify(theme)+')');assert.equal(policy.failures.length,0,'theme policy: '+JSON.stringify(policy));
   await measure(page,width,height,theme,'initial');
   if(page.kind==='slides'){
    const count=await c.evaluate('document.querySelectorAll(".slide").length');assert.equal(count,16);
    for(let i=1;i<count;i++){
     await c.send('Input.dispatchKeyEvent',{type:'keyDown',key:'ArrowRight',code:'ArrowRight',windowsVirtualKeyCode:39});
     await c.send('Input.dispatchKeyEvent',{type:'keyUp',key:'ArrowRight',code:'ArrowRight',windowsVirtualKeyCode:39});
     assert.equal(await c.evaluate('[...document.querySelectorAll(".slide")].findIndex(e=>e.classList.contains("active"))'),i,'slide interaction must change active slide');
     await measure(page,width,height,theme,'slide-'+(i+1));
    }
   }
   if(page.kind==='supplemental'){
    const count=await c.evaluate('document.querySelectorAll(".seg button").length');assert(count>=2,'non-vacuous active/inactive states');
    for(let i=0;i<count;i++){
     await c.evaluate(`document.querySelectorAll('.seg button')[${i}].click()`);
     assert(await c.evaluate(`document.querySelectorAll('.seg button')[${i}].classList.contains('active')`),'segment interaction active state');
     await measure(page,width,height,theme,'segment-'+i);
    }
    await c.evaluate("document.querySelectorAll('.q').forEach(q=>q.querySelectorAll('.choice')[(Number(q.dataset.a)+1)%q.querySelectorAll('.choice').length].click())");
    assert(await c.evaluate("document.querySelectorAll('.choice.correct').length>0&&document.querySelectorAll('.choice.wrong').length>0"),'both quiz feedback states');
    await measure(page,width,height,theme,'active-states');
   }
   assert.equal(c.events.exceptions.length+c.events.blocked.length,0,'runtime and network errors');
  }
 }finally{await c.close();await new Promise(r=>server.close(r));}
 const summary={pages:selected.length,families:[...new Set(selected.map(p=>p.kind))],observations:rows.length,samples:rows.reduce((n,r)=>n+r.rows.length,0),failures:rows.reduce((n,r)=>n+r.failures.length,0)};
 fs.writeFileSync(path.join(OUT,'summary.json'),JSON.stringify(summary,null,2)+'\n');console.log(JSON.stringify(summary));assert.equal(summary.failures,0,'rendered text contrast thresholds');
}
main().catch(e=>{console.error(e.stack);server.close();process.exitCode=1});
