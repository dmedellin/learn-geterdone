'use strict';
const fs=require('node:fs'),{lex,htmlParts}=require('../scripts/canvas_sources');
function templateLiterals(source){
 const tokens=lex(source),result=[];
 for(const token of tokens)if(token.kind==='template-start'){
  const end=tokens[token.templateEnd];if(!end||end.kind!=='template-end')throw Error('incomplete JavaScript template boundary');
  result.push({offset:token.offset,raw:source.slice(token.charOffset,end.charEnd)});
 }
 return result;
}
function documentTemplates(html){return htmlParts(html).scripts.filter(s=>s.executable).flatMap(s=>templateLiterals(s.source).map(t=>({script:s.ordinal,...t,text:t.raw.slice(1,-1)})));}
module.exports={templateLiterals,documentTemplates};
if(require.main===module)process.stdout.write(JSON.stringify(documentTemplates(fs.readFileSync(0,'utf8')))+'\n');
