'use strict';
const fs=require('fs'),path=require('path'),http=require('http');
const R=process.env.SOURCE_ROOT||path.resolve(__dirname,'..'),OUT=process.env.BROWSER_EVIDENCE;
const assert=require('node:assert/strict'),protocol=require(R+'/tests/mutation_protocol');
const SITE=process.env.SITE_ROOT||path.join(R,'site');
const {launch,sleep}=require(R+'/tests/browser_cdp');const contracts=require(R+'/tests/browser_contracts');
const source=Object.values(contracts).map(f=>f.toString()).join('\n');
(async()=>{
 fs.mkdirSync(OUT,{recursive:true});
 const server=http.createServer((req,res)=>{const p=path.join(SITE,decodeURI(req.url),'index.html');try{res.setHeader('Content-Type','text/html');res.end(fs.readFileSync(p))}catch{res.writeHead(404);res.end()}});await new Promise(r=>server.listen(0,'127.0.0.1',r));
 let c;const rows=[];
 try{
 c=await launch({dir:OUT,name:'deck',base:'http://127.0.0.1:'+server.address().port});
 const key=async (k,modifiers=0)=>{const codes={ArrowRight:39,ArrowLeft:37,ArrowDown:40,ArrowUp:38,PageDown:34,PageUp:33,Home:36,End:35,' ':32,Tab:9};await c.send('Input.dispatchKeyEvent',{type:'keyDown',modifiers,key:k,code:k===' '?'Space':k,windowsVirtualKeyCode:codes[k],nativeVirtualKeyCode:codes[k]});await c.send('Input.dispatchKeyEvent',{type:'keyUp',modifiers,key:k,code:k===' '?'Space':k,windowsVirtualKeyCode:codes[k],nativeVirtualKeyCode:codes[k]});await sleep(180)};
 const state=()=>c.evaluate(`(()=>{${source};const a=document.querySelector('.slide.active'),s=getComputedStyle(a),b=a.getBoundingClientRect(),foot=a.querySelector('.slide-stamp')?.getBoundingClientRect();return {heading:a.querySelector('h1,h2').textContent.replace(/\\s+/g,' ').trim(),verticalOwners:[a,...a.querySelectorAll('*')].filter(e=>['auto','scroll'].includes(getComputedStyle(e).overflowY)&&e.scrollHeight>e.clientHeight+1).map(e=>({tag:e.tagName,cls:e.className,tabIndex:e.tabIndex,name:e.getAttribute('aria-label')})),active:[...document.querySelectorAll('.slide')].indexOf(a),count:document.querySelectorAll('.slide.active').length,focus:document.activeElement===a,focused:document.activeElement.outerHTML.slice(0,200),tabIndex:a.tabIndex,name:a.getAttribute('aria-label')||(a.getAttribute('aria-labelledby')||'').split(/\\s+/).map(id=>document.getElementById(id)?.textContent||'').join(' ').trim(),overflow:s.overflowY,scrollTop:a.scrollTop,maxScroll:a.scrollHeight-a.clientHeight,foot:foot&&{top:foot.top,bottom:foot.bottom,ownerTop:b.top,ownerBottom:b.bottom},layout:rootLayout().failures}})()`);
 for(const [width,height] of [[320,800],[390,844]]){
 await c.navigate('/paths/trading/iren-analysis-2026-08-16/slides/',{width,height});const initial=await state();assert(!initial.focus,'initial slide must not autofocus');await key('Tab');const firstTab=await c.evaluate('document.activeElement.className');
 assert.equal(firstTab,'skip-link','masthead skip link remains first keyboard stop');
 await key('ArrowRight');await key('ArrowLeft');
 for(let i=0;i<16;i++){
 const before=await state(),keys=[];
 assert.equal(before.active,i,'left/right slide navigation');assert.equal(before.count,1,'exactly one active slide');assert.equal(before.tabIndex,0,'active slide focusability');assert.equal(before.name,'Slide '+(i+1)+' of 16: '+before.heading,'active slide accessible heading and position');assert(before.focus,'navigation focuses active slide');assert.equal(before.scrollTop,0,'navigation resets slide scroll');assert(['auto','scroll'].includes(before.overflow),'active slide scroll owner');assert.deepEqual(before.layout,[],'deck content layout');assert.equal(before.verticalOwners.length,1,'exactly one vertical slide scroll owner');
 const ax=(await c.send('Accessibility.getFullAXTree')).nodes.filter(n=>!n.ignored&&n.role?.value==='region'&&n.name?.value===before.name);assert.equal(ax.length,1,'active slide exposed with its name in accessibility tree');assert(ax[0].properties.some(p=>p.name==='focused'&&p.value.value),'active slide accessibility focus');before.accessibilityOwner=ax[0];
 for(const k of ['PageDown',' ','ArrowDown','End','ArrowUp','PageUp','Home']){await key(k);const after=await state();keys.push({key:k,...after});assert.equal(after.active,i,'native vertical key must not navigate slides: '+k);assert(after.focus,'native vertical key retains slide focus');assert.deepEqual(after.layout,[],'scrolled deck content layout');}
 await key('End');const end=await state();assert(end.foot.bottom<=end.foot.ownerBottom+1&&end.foot.top>=end.foot.ownerTop,'final meaningful slide footer keyboard reachable');assert(Math.abs(end.scrollTop-end.maxScroll)<=1,'End reaches slide scroll bottom');
 rows.push({width,height,initial:i===0?initial:undefined,firstTab:i===0?firstTab:undefined,before,keys,end});
 const chart=await c.evaluate("document.querySelector('.slide.active .chart')!==null");
 if(chart){
  await key('Home');
  for(let t=0;t<30&&!await c.evaluate("document.activeElement.matches('.slide.active .chart')");t++)await key('Tab');
  assert(await c.evaluate("document.activeElement.matches('.slide.active .chart')"),'chart is keyboard reachable');
  const chartBefore=await c.evaluate("(()=>{const e=document.activeElement;return {tabIndex:e.tabIndex,name:e.getAttribute('aria-label'),left:e.scrollLeft,max:e.scrollWidth-e.clientWidth}})()");
  assert(chartBefore.name&&chartBefore.tabIndex===0&&chartBefore.max>0,'named focusable horizontal chart scroller');
  await key('ArrowRight');await key('ArrowRight');
  assert(await c.evaluate('document.activeElement.scrollLeft')>chartBefore.left,'native horizontal chart scroll');
  assert.equal((await state()).active,i,'chart scrolling preserves slide');
  for(let t=0;t<30&&!await c.evaluate("document.activeElement.matches('.slide.active')");t++)await key('Tab',8);
  assert(await c.evaluate("document.activeElement.matches('.slide.active')"),'slide keyboard return from chart');
 }
 assert.equal(c.events.exceptions.length+c.events.blocked.length,0,'deck runtime/network errors');
 if(i<15)await key('ArrowRight');
 }
 }
 fs.writeFileSync(path.join(OUT,'matrix.json'),JSON.stringify({rows,events:c.events},null,2));
 assert.equal(rows.length,32,'all sixteen slides at both mobile widths');console.log('32/32 deck keyboard contracts pass');
 }finally{if(c)await c.close();await new Promise(r=>server.close(r));}
})().catch(e=>{if(e.code==='ERR_ASSERTION')protocol.semantic(e.message.split('\n')[0]);else protocol.setup(e);process.exitCode=1});
