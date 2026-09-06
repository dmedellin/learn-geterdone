// First-party CDP transport retained from the exact-commit verifier.
'use strict';
const fs=require('node:fs'),path=require('node:path'),http=require('node:http'),{spawn}=require('node:child_process');
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const json=url=>new Promise((resolve,reject)=>http.get(url,r=>{let b='';r.on('data',x=>b+=x);r.on('end',()=>{try{if(r.statusCode!==200)throw Error('HTTP '+r.statusCode);resolve(JSON.parse(b));}catch(e){reject(e)}})}).on('error',reject));
async function launch({dir,name,base}){
 fs.mkdirSync(dir,{recursive:true});const profile=fs.mkdtempSync(path.join(dir,name+'-profile-')),fd=fs.openSync(path.join(dir,name+'-chrome.log'),'w');
 const args=['--headless=new','--no-sandbox','--disable-gpu','--disable-background-networking','--disable-default-apps','--disable-extensions','--no-first-run','--no-default-browser-check','--disable-component-update','--disable-sync','--disable-features=MediaRouter,OptimizationHints','--remote-debugging-port=0','--remote-debugging-address=127.0.0.1','--host-resolver-rules=MAP * ~NOTFOUND, EXCLUDE 127.0.0.1, EXCLUDE localhost','--user-data-dir='+profile,'about:blank'];
 const chrome=spawn('/usr/bin/google-chrome',args,{stdio:['ignore',fd,fd],detached:true});const processRecord={pid:chrome.pid,profile,args,created:new Date().toISOString()};fs.writeFileSync(path.join(dir,name+'-process.json'),JSON.stringify(processRecord,null,2)+'\n');
 let ws,seq=0,closed=false;const pending=new Map(),events={exceptions:[],console:[],logs:[],requests:[],responses:[],blocked:[]};let allowedDocument=null;
 async function close(){if(closed)return;closed=true;try{if(ws&&ws.readyState===1)await send('Browser.close');}catch{}for(let i=0;i<50&&chrome.exitCode===null&&chrome.signalCode===null;i++)await sleep(100);try{process.kill(-chrome.pid,'SIGTERM')}catch{}await sleep(150);try{process.kill(-chrome.pid,'SIGKILL')}catch{}try{ws?.close()}catch{}fs.closeSync(fd);fs.rmSync(profile,{recursive:true,force:true});let alive;try{process.kill(chrome.pid,0);alive=true}catch{alive=false}const proof={...processRecord,closed:new Date().toISOString(),pidAlive:alive,profileExists:fs.existsSync(profile),exitCode:chrome.exitCode,signalCode:chrome.signalCode};fs.writeFileSync(path.join(dir,name+'-cleanup.json'),JSON.stringify(proof,null,2)+'\n');if(alive||proof.profileExists)throw Error('Chrome cleanup failed');}
 const send=(method,params={})=>new Promise((resolve,reject)=>{const id=++seq;const timer=setTimeout(()=>{pending.delete(id);reject(Error('CDP timeout '+method));},60000);pending.set(id,{resolve:v=>{clearTimeout(timer);resolve(v)},reject:e=>{clearTimeout(timer);reject(e)}});ws.send(JSON.stringify({id,method,params}));});
 try{
  let active;for(let i=0;i<150;i++){try{active=fs.readFileSync(path.join(profile,'DevToolsActivePort'),'utf8');break}catch{}await sleep(100)}if(!active)throw Error('Chrome launch timeout');const port=+active.split('\n')[0],target=(await json('http://127.0.0.1:'+port+'/json/list')).find(t=>t.type==='page');
  ws=new WebSocket(target.webSocketDebuggerUrl);await new Promise((resolve,reject)=>{ws.addEventListener('open',resolve,{once:true});ws.addEventListener('error',reject,{once:true})});
  ws.addEventListener('message',e=>{const m=JSON.parse(e.data);if(m.id){const p=pending.get(m.id);if(p){pending.delete(m.id);m.error?p.reject(Error(JSON.stringify(m.error))):p.resolve(m.result)}return}const p=m.params;
   if(m.method==='Fetch.requestPaused'){const allowed=p.request.url.startsWith('data:')||(p.resourceType==='Document'&&p.request.url===allowedDocument);if(!allowed)events.blocked.push({url:p.request.url,type:p.resourceType});send(allowed?'Fetch.continueRequest':'Fetch.failRequest',allowed?{requestId:p.requestId}:{requestId:p.requestId,errorReason:'BlockedByClient'}).catch(()=>{});}
   if(m.method==='Runtime.exceptionThrown')events.exceptions.push(p);
   if(m.method==='Runtime.consoleAPICalled'&&['error','warning','warn'].includes(p.type))events.console.push(p);
   if(m.method==='Log.entryAdded'&&['error','warning'].includes(p.entry.level))events.logs.push(p.entry);
   if(m.method==='Network.requestWillBeSent')events.requests.push({url:p.request.url,type:p.type,method:p.request.method});
   if(m.method==='Network.responseReceived')events.responses.push({url:p.response.url,type:p.type,status:p.response.status,headers:p.response.headers});
  });
  for(const m of ['Page.enable','Runtime.enable','Log.enable','Network.enable','Accessibility.enable'])await send(m);
  await send('Network.setCacheDisabled',{cacheDisabled:true});await send('Fetch.enable',{patterns:[{urlPattern:'*'}]});
  const browserVersion=await send('Browser.getVersion');fs.writeFileSync(path.join(dir,name+'-browser-version.json'),JSON.stringify(browserVersion,null,2)+'\n');
  const evaluate=async expression=>{const r=await send('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(r.exceptionDetails)throw Error(JSON.stringify(r.exceptionDetails));return r.result.value};
  async function navigate(route,{width,height,theme='dark'}={}){
   for(const k of Object.keys(events))events[k]=[];allowedDocument=base+route;
   await send('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:1,mobile:width<=390});await send('Emulation.setTouchEmulationEnabled',{enabled:width<=390,maxTouchPoints:5});await send('Emulation.setEmulatedMedia',{features:[{name:'prefers-color-scheme',value:theme==='system-light'?'light':'dark'},{name:'prefers-reduced-motion',value:'reduce'}]});
   const script=await send('Page.addScriptToEvaluateOnNewDocument',{source:"try{localStorage.clear();sessionStorage.clear();"+(theme==='system-light'?'':"localStorage.setItem('learn-theme','dark');")+"}catch(e){}"});
   const nav=await send('Page.navigate',{url:allowedDocument});if(nav.errorText)throw Error(nav.errorText);
   let ready=false;for(let i=0;i<200;i++){if(await evaluate('document.readyState==="complete"&&location.href==='+JSON.stringify(allowedDocument))){ready=true;break}await sleep(25)}if(!ready)throw Error('Document never completed '+route);
   await send('Page.removeScriptToEvaluateOnNewDocument',{identifier:script.identifier});
   // Even a reduced-motion duration creates a transition. Measure its final
   // rendered colors without changing the page's animation or theme policy.
   if(theme==='explicit-light')await evaluate("document.getElementById('themeToggle').click(); Promise.allSettled(document.getAnimations().filter(a=>a instanceof CSSTransition).map(a=>a.finished))");
   await evaluate('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');return nav;
  }
  return {send,evaluate,navigate,close,events,browserVersion,processRecord,base};
 }catch(e){await close();throw e}
}
module.exports={launch,sleep};
