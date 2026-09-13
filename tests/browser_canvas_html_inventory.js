'use strict';
const fs=require('fs'),path=require('path'),crypto=require('crypto'),http=require('http'),protocol=require((process.env.SOURCE_ROOT||path.resolve(__dirname,'..'))+'/tests/mutation_protocol');
const {inventory}=require((process.env.SOURCE_ROOT||path.resolve(__dirname,'..'))+'/scripts/canvas_sources');
const {launch}=require((process.env.SOURCE_ROOT||path.resolve(__dirname,'..'))+'/tests/browser_cdp'),{interceptCanvasText}=require((process.env.SOURCE_ROOT||path.resolve(__dirname,'..'))+'/tests/canvas_runtime_contract');
const R=(process.env.SOURCE_ROOT||path.resolve(__dirname,'..')),OUT=process.env.BROWSER_EVIDENCE,Q=path.join(path.dirname(OUT),'owned-html-inventory');const fail=assertion=>{throw Object.assign(Error(assertion),{assertion,code:'LEARN_CANVAS_SEMANTIC'})};
(async()=>{fs.mkdirSync(OUT,{recursive:true});fs.mkdirSync(Q);fs.cpSync(R+'/site',Q+'/site',{recursive:true});fs.mkdirSync(Q+'/scripts');fs.copyFileSync(R+'/scripts/canvas_contract.js',Q+'/scripts/canvas_contract.js');
try{
 const baseline=inventory(Q);if(baseline.errors.length)throw Error('HTML inventory integration baseline invalid');
 const page=baseline.pages.find(p=>p.canvases.length),original=fs.readFileSync(page.file),source=original.toString().replace(/^<body(?=[\s>])/m,'<body onclick="this.querySelector(\'canvas\').getContext(\'2d\').fillText(\'Raw\',10,20)"');if(source===original.toString())throw Error('HTML body fixture anchor missing');
 let red,browser;try{fs.writeFileSync(page.file,source);red=inventory(Q);
  const server=http.createServer((req,res)=>{res.setHeader('Content-Type','text/html; charset=utf-8');res.end(source)});await new Promise(r=>server.listen(0,'127.0.0.1',r));const c=await launch({dir:OUT,name:'body-owner',base:'http://127.0.0.1:'+server.address().port});
  try{await c.send('Page.addScriptToEvaluateOnNewDocument',{source:'('+interceptCanvasText.toString()+')()'});await c.navigate('/',{width:390,height:844,theme:'dark'});browser=await c.evaluate('(()=>{const attribute=document.body.getAttribute("onclick"),before=__learnCanvasNative.snapshot();let error=null;try{document.body.onclick.call(document.body)}catch(e){error={code:e.code,assertion:e.assertion,message:e.message}}return {attribute,before,error,after:__learnCanvasNative.snapshot()}})()');fs.writeFileSync(OUT+'/body-browser.json',JSON.stringify(browser));if(!browser.attribute?.includes('fillText')||browser.before.failures.length||browser.after.failures.length||browser.error?.code!=='LEARN_CANVAS_SEMANTIC'||browser.error?.assertion!=='uncontracted native text')fail('real body attribute mutation must execute');if(c.events.exceptions.length||c.events.blocked.length||c.events.responses.some(r=>r.status>=400))throw Error('body owner fixture runtime/network setup failure');}
  finally{fs.writeFileSync(OUT+'/events.json',JSON.stringify(c.events));await c.close();await new Promise(r=>server.close(r));}
 }finally{fs.writeFileSync(page.file,original);}
 if(!fs.readFileSync(page.file).equals(original))throw Error('HTML inventory restore mismatch');
 const restored=inventory(Q);fs.writeFileSync(OUT+'/observations.json',JSON.stringify({route:page.route,sourceHash:crypto.createHash('sha256').update(original).digest('hex'),baseline:{bound:baseline.contractOccurrences,unbound:baseline.unbound,errors:baseline.errors},mutant:{bound:red.contractOccurrences,unbound:red.unbound,errors:red.errors},restored:{bound:restored.contractOccurrences,unbound:restored.unbound,errors:restored.errors},byteExactRestore:true},null,2));
 if(!red.errors.some(e=>e.route===page.route&&e.ownerKind==='event-handler'&&e.attribute==='onclick'&&e.assertion==='uncontracted native canvas text source')||red.unbound!==baseline.unbound+1)fail('executable HTML attributes must enter canvas source inventory');
 if(restored.errors.length)fail('restored executable HTML source inventory');console.log('1/1 complete HTML inventory mutation sequence passed');
}catch(e){if(e.code==='LEARN_CANVAS_SEMANTIC')protocol.semantic(e.assertion);else protocol.setup(e);process.exitCode=1;}
finally{const st=fs.lstatSync(Q);fs.writeFileSync(OUT+'/owned-before-teardown.json',JSON.stringify({path:Q,inode:st.ino,exists:true}));fs.rmSync(Q,{recursive:true});fs.writeFileSync(OUT+'/owned-after-teardown.json',JSON.stringify({path:Q,exists:fs.existsSync(Q)}));}

})().catch(e=>{protocol.setup(e);process.exitCode=1});
