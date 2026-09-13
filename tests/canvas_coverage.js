'use strict';
const {coverageSyntax}=require('./canvas_syntax'),crypto=require('crypto');
const fail=(assertion,detail)=>{throw Object.assign(Error(assertion+': '+detail),{code:'LEARN_CANVAS_SEMANTIC',assertion,detail})};
function coverageReflection(source,reflection){
 const hash=crypto.createHash('sha256').update(source).digest('hex');if(reflection.sha256!==hash||reflection.charLength!==source.length)fail('wrong Chromium coverage source identity','source bytes/length differ');if(!Array.isArray(reflection.functions)||!reflection.functions.length)fail('empty Chromium source coverage','no functions');
 const owners=coverageSyntax(source);
 const seen=new Set(),rows=[];
 for(const f of reflection.functions){if(!Array.isArray(f.ranges)||!f.ranges.length)fail('missing Chromium function ranges','function lacks ranges');const top=f.ranges[0],key=top.startOffset+':'+top.endOffset;if(seen.has(key))fail('duplicate Chromium function coverage',key);seen.add(key);const match=owners.filter(o=>o.start===top.startOffset&&o.end===top.endOffset);if(match.length!==1)fail('unbound Chromium function coverage',key+' '+f.functionName);if(typeof f.isBlockCoverage!=='boolean'||top.count>0&&!f.isBlockCoverage)fail('incomplete Chromium block coverage',key);
  const rangeKeys=new Set();for(const range of f.ranges){if(![range.startOffset,range.endOffset,range.count].every(Number.isSafeInteger)||range.count<0||range.startOffset<top.startOffset||range.endOffset>top.endOffset||range.startOffset>=range.endOffset)fail('invalid Chromium coverage range',key);const identity=range.startOffset+':'+range.endOffset;if(rangeKeys.has(identity))fail('duplicate Chromium block coverage',identity);rangeKeys.add(identity);}
  for(const [i,left]of f.ranges.entries())for(const right of f.ranges.slice(i+1)){const overlap=left.startOffset<right.endOffset&&right.startOffset<left.endOffset,contains=left.startOffset<=right.startOffset&&left.endOffset>=right.endOffset||right.startOffset<=left.startOffset&&right.endOffset>=left.endOffset;if(overlap&&!contains)fail('crossing Chromium coverage ranges',key);}
  rows.push({owner:match[0],function:f});
 }
 function at(offset){if(!Number.isSafeInteger(offset)||offset<0||offset>=source.length)fail('invalid source coverage occurrence','outside executable source');const owner=owners.filter(o=>o.start<=offset&&offset<o.end).sort((a,b)=>(a.end-a.start)-(b.end-b.start))[0],row=rows.find(r=>r.owner===owner);if(!row){const ancestor=rows.filter(r=>r.owner.start<=owner.start&&r.owner.end>=owner.end).sort((a,b)=>(a.owner.end-a.owner.start)-(b.owner.end-b.owner.start))[0];if(!ancestor)fail('missing source function coverage',owner.start+':'+owner.end);const enclosing=ancestor.function.ranges.filter(r=>r.startOffset<=owner.start&&r.endOffset>=owner.end).sort((a,b)=>(a.endOffset-a.startOffset)-(b.endOffset-b.startOffset))[0];if(enclosing?.count===0)return {count:0,reason:'unexecuted enclosing source region',functionStart:owner.start,functionEnd:owner.end,range:enclosing};fail('missing active source function coverage',owner.start+':'+owner.end);}
  const range=row.function.ranges.filter(r=>r.startOffset<=offset&&offset<r.endOffset).sort((a,b)=>(a.endOffset-a.startOffset)-(b.endOffset-b.startOffset))[0];/* The validated complete function root contains every in-owner offset. */return {count:range.count,reason:'exact Chromium function/block source region',functionStart:owner.start,functionEnd:owner.end,range};
 }
 return {hash,functions:rows.length,at};
}
module.exports={coverageReflection};
