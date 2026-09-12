'use strict';
const assert=require('node:assert/strict'),{reconcileImplementations}=require('./canvas_implementation_evidence'),protocol=require('./mutation_protocol');
const digest='a'.repeat(64),other='b'.repeat(64),descriptor={id:'fixture.text',role:'value'};
const occurrence=route=>({route,script:0,offset:20,siteID:descriptor.id,descriptor,implementationOwner:'draw',implementationHash:digest,closure:{sha256:digest}});
const source={pages:['/a/','/b/'].map(route=>({route,sha256:digest,occurrences:[occurrence(route)]}))};
const rows=source.pages.map((page,i)=>({route:page.route,sourceHash:digest,error:null,exceptions:[],blocked:[],value:{native:{history:i?[]:[{site:descriptor.id,descriptor,diagnostic:false}]}}}));
const cases=[
 ['normal',()=>{},null],
 ['omitted-route',(s,r)=>r.pop(),'missing canvas route implementation evidence'],
 ['added-route',(s,r)=>r.push({...r[0],route:'/extra/'}),'canvas route evidence identity differs'],
 ['duplicate-route',(s,r)=>r.push(structuredClone(r[0])),'canvas route evidence identity differs'],
 ['wrong-route-source-bytes',(s,r)=>r[0].sourceHash=other,'canvas route evidence identity differs'],
 ['missing-implementation-hash',s=>delete s.pages[0].occurrences[0].implementationHash,'missing canvas implementation identity'],
 ['missing-closure-hash',s=>delete s.pages[0].occurrences[0].closure.sha256,'missing canvas implementation identity'],
 ['wrong-native-descriptor',(s,r)=>r[0].value.native.history[0].descriptor.role='guide','wrong canvas implementation witness identity'],
 ['empty-runtime-witnesses',(s,r)=>r[0].value.native.history=[],'empty canvas implementation evidence'],
 ['failed-route-witness',(s,r)=>r[0].error='bad frame','failed canvas route used as implementation witness'],
 ['runtime-error-witness',(s,r)=>r[0].exceptions.push({error:'runtime'}),'failed canvas route used as implementation witness'],
 ['network-error-witness',(s,r)=>r[0].blocked.push({url:'fixture'}),'failed canvas route used as implementation witness'],
 ['changed-dormant-implementation',s=>s.pages[1].occurrences[0].implementationHash=other,'canvas source occurrence has no implementation witness'],
 ['changed-dormant-closure',s=>s.pages[1].occurrences[0].closure.sha256=other,'canvas source occurrence has no implementation witness'],
 ['conditional-site-without-witness',s=>{const v=structuredClone(s.pages[1].occurrences[0]);v.siteID=v.descriptor.id='fixture.conditional';v.offset=90;s.pages[1].occurrences.push(v)},'canvas source occurrence has no implementation witness'],
 ['duplicate-source-occurrence',s=>s.pages[1].occurrences.push(structuredClone(s.pages[1].occurrences[0])),'duplicate canvas source occurrence identity']
];
try{
 for(const [name,mutate,expected]of cases){const s=structuredClone(source),r=structuredClone(rows);mutate(s,r);let observed=null,result=null;try{result=reconcileImplementations(s,r)}catch(e){if(e.code!=='LEARN_CANVAS_SEMANTIC')throw e;observed=e.assertion}assert.equal(observed,expected,'canvas implementation witness: '+name);if(result){assert.equal(result.sourceOccurrences,2);assert.equal(result.sameRoute,1);assert.equal(result.identicalImplementationWitnesses,2);}}
 console.log(cases.length+'/'+cases.length+' canvas implementation witness fixtures passed');
}catch(e){if(e.code==='ERR_ASSERTION'||e.code==='LEARN_CANVAS_SEMANTIC')protocol.semantic(e.assertion||e.message.split('\n')[0]);else protocol.setup(e);process.exitCode=1;}
