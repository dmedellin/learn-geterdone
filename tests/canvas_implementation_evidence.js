'use strict';
// Repeated inlined definitions can share an execution witness only when the
// site ID, lexical implementation bytes and complete recorded binding closure
// agree. This is source ownership closure, not parameter-domain equivalence.
function reconcileImplementations(source,rows){
 const fail=assertion=>{throw Object.assign(Error(assertion),{assertion,code:'LEARN_CANVAS_SEMANTIC'})};
 const hash=value=>typeof value==='string'&&/^[a-f0-9]{64}$/.test(value);
 if(!Array.isArray(source?.pages)||!source.pages.length||!Array.isArray(rows)||!rows.length)fail('empty canvas implementation evidence');
 const pages=new Map(),observed=new Map(),occurrences=[],identities=new Set(),witnesses=new Map();
 for(const page of source.pages){
  if(typeof page.route!=='string'||pages.has(page.route)||!hash(page.sha256)||!Array.isArray(page.occurrences))fail('invalid canvas source page identity');pages.set(page.route,page);
  for(const site of page.occurrences){
   if(site.route!==page.route||!Number.isInteger(site.script)||site.script<0||!Number.isInteger(site.offset)||site.offset<0||typeof site.siteID!=='string'||!site.siteID||!hash(site.implementationHash)||!hash(site.closure?.sha256)||typeof site.implementationOwner!=='string'||!site.implementationOwner)fail('missing canvas implementation identity');
   const identity=JSON.stringify([site.route,site.script,site.offset,site.siteID]);if(identities.has(identity))fail('duplicate canvas source occurrence identity');identities.add(identity);occurrences.push(site);
  }
 }
 for(const row of rows){
  const page=pages.get(row.route);if(!page||observed.has(row.route)||row.sourceHash!==page.sha256||!Array.isArray(row.value?.native?.history))fail('canvas route evidence identity differs');observed.set(row.route,row);
  if(row.error||!Array.isArray(row.exceptions)||row.exceptions.length||!Array.isArray(row.blocked)||row.blocked.length)fail('failed canvas route used as implementation witness');
  for(const call of row.value.native.history.filter(c=>!c.diagnostic)){
   const candidates=page.occurrences.filter(s=>s.siteID===call.site&&JSON.stringify(s.descriptor)===JSON.stringify(call.descriptor));if(candidates.length!==1)fail('wrong canvas implementation witness identity');
   const site=candidates[0],key=JSON.stringify([site.siteID,site.implementationHash,site.closure.sha256]);if(!witnesses.has(key))witnesses.set(key,new Set());witnesses.get(key).add(page.route);
  }
 }
 if(observed.size!==pages.size)fail('missing canvas route implementation evidence');
 if(!occurrences.length||!witnesses.size)fail('empty canvas implementation evidence');
 const records=occurrences.map(site=>{
  const routes=[...(witnesses.get(JSON.stringify([site.siteID,site.implementationHash,site.closure.sha256]))||[])].sort();if(!routes.length)fail('canvas source occurrence has no implementation witness');
  return {route:site.route,script:site.script,offset:site.offset,siteID:site.siteID,implementationOwner:site.implementationOwner,implementationHash:site.implementationHash,closureHash:site.closure.sha256,witnessRoutes:routes,sameRoute:routes.includes(site.route)};
 });
 return {sourceOccurrences:records.length,sameRoute:records.filter(r=>r.sameRoute).length,identicalImplementationWitnesses:records.length,unwitnessed:0,records,scope:'Exact repeated lexical implementation and recorded binding closure identity. Argument/state domains and conditional branch completeness require the separate finite-state proof.'};
}
module.exports={reconcileImplementations};
