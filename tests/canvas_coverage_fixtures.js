'use strict';
const fs=require('fs'),assert=require('assert/strict'),{coverageReflection}=require('./canvas_coverage'),protocol=require('./mutation_protocol');
const input=JSON.parse(fs.readFileSync(__dirname+'/canvas_coverage_fixture.json','utf8'));
const {source}=input,original=input.reflection,rows=[];
const clone=()=>structuredClone(original),low=source.indexOf('CanvasText.text',source.indexOf('}else{')),high=source.indexOf('CanvasText.text');
const cases=[
 ['missing active function',r=>r.functions.splice(1,1),'missing active source function coverage',low],
 ['missing source owner',r=>r.functions.splice(0,1),'missing source function coverage',source.length-1],
 ['missing block classification',r=>{r.functions[1].isBlockCoverage=null;r.functions[1].ranges[0].count=0;},'incomplete Chromium block coverage'],
 ['wrong source identity',r=>r.sha256='0'.repeat(64),'wrong Chromium coverage source identity'],
 ['wrong source length',r=>r.charLength++,'wrong Chromium coverage source identity'],
 ['empty function inventory',r=>r.functions=[],'empty Chromium source coverage'],
 ['missing function ranges',r=>r.functions[0].ranges=[],'missing Chromium function ranges'],
 ['duplicate function',r=>r.functions.push(structuredClone(r.functions[0])),'duplicate Chromium function coverage'],
 ['unbound function',r=>r.functions[0].ranges[0].endOffset--,'unbound Chromium function coverage'],
 ['warm function-only metadata',r=>r.functions[0].isBlockCoverage=false,'incomplete Chromium block coverage'],
 ['negative block count',r=>r.functions[1].ranges[1].count=-1,'invalid Chromium coverage range'],
 ['fractional range offset',r=>r.functions[1].ranges[1].startOffset+=.5,'invalid Chromium coverage range'],
 ['range outside function',r=>r.functions[1].ranges[1].startOffset=0,'invalid Chromium coverage range'],
 ['duplicate block',r=>r.functions[1].ranges.push(structuredClone(r.functions[1].ranges[1])),'duplicate Chromium block coverage'],
 ['crossing blocks',r=>{const b=r.functions[1].ranges[1];r.functions[1].ranges.push({startOffset:b.startOffset+1,endOffset:b.endOffset+1,count:0});},'crossing Chromium coverage ranges']
];
try{
 const baseline=coverageReflection(source,original);assert.equal(baseline.at(low).count,1,'active fixture site is witnessed');assert.equal(baseline.at(high).count,0,'inactive fixture site has zero coverage');rows.push({name:'actual cold Chromium conditional coverage',observed:'PASS',low:baseline.at(low),high:baseline.at(high)});
 for(const [name,mutate,expected,query] of cases){const changed=clone();mutate(changed);let error;try{const model=coverageReflection(source,changed);if(query!==undefined)model.at(query)}catch(e){error=e}assert.equal(error?.code,'LEARN_CANVAS_SEMANTIC',name+' rejects semantically');assert.equal(error?.assertion,expected,name+' rejects the intended metadata assertion');rows.push({name,expected,observed:error.assertion});}
 for(const offset of [-1,source.length,.5,undefined]){let error;try{baseline.at(offset)}catch(e){error=e}assert.equal(error?.assertion,'invalid source coverage occurrence','invalid occurrence is rejected');rows.push({name:'invalid occurrence '+String(offset),observed:error.assertion});}
 console.log(rows.length+'/'+rows.length+' source coverage reflection fixtures passed; application finite closure remains separate');
}catch(e){if(e.code==='ERR_ASSERTION')protocol.semantic(e.message.split('\n')[0]);else if(e.code==='LEARN_CANVAS_SEMANTIC')protocol.semantic(e.assertion);else protocol.setup(e);process.exitCode=1;}finally{if(process.env.BROWSER_EVIDENCE){fs.mkdirSync(process.env.BROWSER_EVIDENCE,{recursive:true});fs.writeFileSync(process.env.BROWSER_EVIDENCE+'/observations.json',JSON.stringify(rows,null,2));}}
