#!/usr/bin/env node
/* A section's content must fill the column it sits in.
 *
 * The standardization pass capped `.prose` at 72ch for readability. `.prose` is
 * the lesson body CARD, not the text inside it, so every generated Algebra and
 * Discrete Mathematics lesson rendered its card 659px wide in a 1160px column
 * and left half the row empty next to a visible card edge. Contrast passed,
 * markup contracts passed, 386 smoke checks passed, and 185 unit tests passed:
 * nothing asserted that a block fills its row, so a reader saw it instantly and
 * the suite could not.
 *
 * Narrow text is not the defect: a bare paragraph capped to a readable measure
 * looks deliberate. What looks broken is a PANEL -- something that paints a
 * border or a background -- ending short of its row, because its edge draws a
 * line across the middle of the page with nothing beside it. So this flags only
 * elements that paint a box, are alone on their row, and do not fill it.
 * Two-column layouts are legitimate and pass: their children tile the row.
 *
 *   BROWSER_EVIDENCE=/tmp/ev node tests/browser_layout.js [--all]
 *
 * Without --all it checks one page of every page-kind family plus one lesson
 * from each of the 25 Courses. */
'use strict';
const fs=require('node:fs'),path=require('node:path'),http=require('node:http');
const ROOT=path.resolve(process.env.SOURCE_ROOT||path.join(__dirname,'..')),SITE=path.join(ROOT,'site');
const {launch}=require('./browser_cdp');
const OUT=process.env.BROWSER_EVIDENCE;
if(!OUT){console.error('set BROWSER_EVIDENCE to a directory outside the repository');process.exit(2);}
fs.mkdirSync(OUT,{recursive:true});
const TOLERANCE=40;   // px of slack for padding and sub-pixel rounding
const corpus=[];
(function walk(d){for(const e of fs.readdirSync(d,{withFileTypes:true})){const f=path.join(d,e.name);
 if(e.isDirectory())walk(f);else if(e.name==='index.html'){
  const src=fs.readFileSync(f,'utf8');
  corpus.push({route:'/'+path.relative(SITE,f).replace(/index\.html$/,''),
               kind:src.match(/<body data-page-kind="([^"]+)"/)?.[1]||'fallback'});}}})(SITE);
const seenKind=new Set(),seenCourse=new Set();
const selected=process.argv.includes('--all')?corpus:corpus.sort((a,b)=>a.route.localeCompare(b.route)).filter(p=>{
 if(p.kind!=='lesson'){if(seenKind.has(p.kind))return false;seenKind.add(p.kind);return true;}
 const course=p.route.split('/')[1];if(seenCourse.has(course))return false;seenCourse.add(course);return true;});
const PROBE=`(()=>{
 const rows=[];
 for(const sec of document.querySelectorAll('section')){
  const sr=sec.getBoundingClientRect();
  if(sr.width<5)continue;
  const kids=[...sec.children].map(k=>({el:k,r:k.getBoundingClientRect()})).filter(k=>k.r.width>5&&k.r.height>5);
  for(const k of kids){
   if(k.r.width>=sr.width-${TOLERANCE})continue;
   // A sibling beside it on the same row makes this a real column, not dead space.
   const beside=kids.some(o=>o.el!==k.el&&o.r.top<k.r.bottom-4&&o.r.bottom>k.r.top+4);
   if(beside)continue;
   // Only a painted panel shows the gap; bare text simply wraps short.
   const cs=getComputedStyle(k.el);
   // An inline box sizes to its content by definition -- a chip or pill is
   // supposed to be narrow. Only block-level panels are expected to fill.
   if(cs.display.startsWith('inline'))continue;
   const bg=(cs.backgroundColor.match(/[\d.]+/g)||[]);
   const paints=(bg.length===4?parseFloat(bg[3])>0.01:bg.length===3)
     ||['Top','Right','Bottom','Left'].some(s=>parseFloat(cs['border'+s+'Width'])>0);
   if(!paints)continue;
   rows.push({section:sec.id||sec.className||'(anonymous)',tag:k.el.tagName,
              cls:(k.el.className||'').slice(0,40),width:Math.round(k.r.width),
              column:Math.round(sr.width),shortBy:Math.round(sr.width-k.r.width)});
  }
 }
 return rows;})()`;
(async()=>{
 const server=http.createServer((q,r)=>{try{let f=path.join(SITE,decodeURIComponent(q.url.split('?')[0]));
  if(!f.startsWith(SITE))throw 0;if(fs.statSync(f).isDirectory())f=path.join(f,'index.html');
  r.setHeader('Content-Type','text/html; charset=utf-8');r.end(fs.readFileSync(f));}catch{r.writeHead(404);r.end();}});
 await new Promise(r=>server.listen(0,'127.0.0.1',r));
 const c=await launch({dir:OUT,name:'layout',base:'http://127.0.0.1:'+server.address().port});
 const failures=[];
 try{
  for(const page of selected)for(const width of [1400,1100]){
   await c.navigate(page.route,{width,height:900,theme:'dark'});
   await c.evaluate('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');
   for(const row of await c.evaluate(PROBE))failures.push({route:page.route,width,...row});
  }
 }finally{await c.close();server.close();}
 fs.writeFileSync(path.join(OUT,'layout.json'),JSON.stringify({pages:selected.length,failures},null,1));
 console.log(JSON.stringify({pages:selected.length,widths:2,failures:failures.length}));
 for(const f of failures.slice(0,10))console.log('ORPHAN ROW '+JSON.stringify(f));
 process.exit(failures.length?1:0);
})();
