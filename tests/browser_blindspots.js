#!/usr/bin/env node
/* The constructs renderedContrast() does not cover, measured directly.
 *
 * The rendered-contrast oracle reads the semantic text inventory and rasters
 * it. Eight independent canaries showed it misses five classes: SVG text under
 * fill-opacity, -webkit-text-fill-color, text clipped away by a clip-path, text
 * occluded by a shape painted later, and the value a native form control draws
 * itself. Rather than teach the raster oracle five new tricks, this asks the
 * narrower question the corpus actually needs answered: does any of those
 * constructs carry text here, and is that text legible?
 *
 * Backgrounds are composited through the ancestor stack. Reading only the first
 * fully opaque ancestor and ignoring the translucent panels above it reports a
 * dark-on-dark 1.32 where the screen shows dark-on-white -- that mistake is the
 * reason this file spells the compositing out.
 *
 *   BROWSER_EVIDENCE=/tmp/ev node tests/browser_blindspots.js
 *
 * Exits nonzero on any control below 4.5:1 or any clipped <text> rendered away
 * to nothing. */
'use strict';
const fs=require('node:fs'),path=require('node:path'),http=require('node:http');
const ROOT=path.resolve(process.env.SOURCE_ROOT||path.join(__dirname,'..'));
const SITE=path.join(ROOT,'site');
const {launch}=require('./browser_cdp');
const OUT=process.env.BROWSER_EVIDENCE;
if(!OUT){console.error('set BROWSER_EVIDENCE to a directory outside the repository');process.exit(2);}
fs.mkdirSync(OUT,{recursive:true});
const corpus=[];
(function walk(d){for(const e of fs.readdirSync(d,{withFileTypes:true})){const f=path.join(d,e.name);
 if(e.isDirectory())walk(f);else if(e.name==='index.html')corpus.push('/'+path.relative(SITE,f).replace(/index\.html$/,''));}})(SITE);
// one lesson per course + every non-lesson family
const seen=new Set(),sel=corpus.sort().filter(r=>{const p=r.split('/').filter(Boolean);
 if(p.length<2)return true;const c=p[0];if(seen.has(c))return false;seen.add(c);return true;});
const PROBE=`(()=>{
 const L=c=>{c=c.map(v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)});return .2126*c[0]+.7152*c[1]+.0722*c[2]};
 const rgb=s=>{const m=s.match(/[\\d.]+/g)||[0,0,0];return [+m[0],+m[1],+m[2],m[3]===undefined?1:+m[3]]};
 const over=(f,b)=>[0,1,2].map(i=>f[i]*f[3]+b[i]*(1-f[3])).concat([1]);
 const back=el=>{const stack=[];let n=el;
   while(n){const b=rgb(getComputedStyle(n).backgroundColor);if(b[3]>0)stack.push(b);
     if(b[3]>0.999)break;n=n.parentElement;}
   let acc=[255,255,255,1];
   for(let i=stack.length-1;i>=0;i--)acc=over(stack[i],acc);
   return acc};
 const ratio=(a,b)=>{const x=L(a)+.05,y=L(b)+.05;return x>y?x/y:y/x};
 const out={controls:[],clippedText:[]};
 for(const el of document.querySelectorAll('input,textarea,select')){
  const cs=getComputedStyle(el);const t=el.type||'';
  if(['range','checkbox','radio','hidden','file'].includes(t))continue;
  const r=el.getBoundingClientRect();if(!r.width||!r.height)continue;
  const has=(el.value??'').trim().length>0;if(!has)continue;
  const fg0=rgb(cs.color),bg=back(el),fg=fg0[3]>0.999?fg0:over(fg0,bg);
  out.controls.push({tag:el.tagName,id:el.id||null,type:t,value:(el.value||'').slice(0,30),
   color:cs.color,background:'rgb('+bg.slice(0,3).map(Math.round).join(',')+')',ratio:+ratio(fg,bg).toFixed(2)});
 }
 for(const t of document.querySelectorAll('text')){
  if(!(t.textContent||'').trim())continue;
  const r=t.getBoundingClientRect();
  const clipped=t.closest('[clip-path]')!==null||!!getComputedStyle(t).clipPath&&getComputedStyle(t).clipPath!=='none';
  if(!clipped)continue;
  out.clippedText.push({text:(t.textContent||'').trim().slice(0,40),w:Math.round(r.width),h:Math.round(r.height)});
 }
 return out;})()`;
(async()=>{
 const server=http.createServer((q,s)=>{try{let f=path.join(SITE,decodeURIComponent(q.url.split('?')[0]));
  if(!f.startsWith(SITE))throw 0;if(fs.statSync(f).isDirectory())f=path.join(f,'index.html');
  s.setHeader('Content-Type','text/html; charset=utf-8');s.end(fs.readFileSync(f));}catch{s.writeHead(404);s.end();}});
 await new Promise(r=>server.listen(0,'127.0.0.1',r));
 const c=await launch({dir:OUT,name:'blindspots',base:'http://127.0.0.1:'+server.address().port});
 let controls=0,clipped=0,fails=[];
 try{
  for(const route of sel)for(const theme of ['dark','explicit-light']){
   await c.navigate(route,{width:1440,height:900,theme});
   await c.evaluate('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');
   const res=await c.evaluate(PROBE);
   controls+=res.controls.length;clipped+=res.clippedText.length;
   for(const r of res.controls)if(r.ratio<4.5)fails.push({route,theme,kind:'control',...r});
   for(const r of res.clippedText)if(r.w<2||r.h<2)fails.push({route,theme,kind:'clipped-text',...r});
  }
 }finally{await c.close();server.close();}
 fs.writeFileSync(path.join(OUT,'blindspots.json'),JSON.stringify({pages:sel.length,controls,clipped,fails},null,1));
 console.log(JSON.stringify({pages:sel.length,controlSamples:controls,clippedTextSamples:clipped,failures:fails.length},null,1));
 for(const f of fails.slice(0,8))console.log('FAIL',JSON.stringify(f));
 process.exit(fails.length?1:0);
})();
