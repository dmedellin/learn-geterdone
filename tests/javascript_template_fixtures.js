'use strict';
const assert=require('node:assert/strict'),{templateLiterals,documentTemplates}=require('./javascript_templates'),protocol=require('./mutation_protocol');
try{
 const template='`Before ${flag ? `Nested ${value}` : "fallback"} After`',source='const draw=()=>{output.innerHTML='+template+'}; next();';
 const literals=templateLiterals(source);assert.equal(literals.length,2,'outer and nested templates are both inventoried');assert.equal(literals[0].raw,template,'nested expression does not truncate template ownership');assert.equal(literals[1].raw,'`Nested ${value}`','nested template remains separately owned');
 const wrapped=source.replace('()=>{','()=>{return CanvasText.frame(()=>{').replace('}; next();','});}; next();');assert.equal(templateLiterals(wrapped)[0].raw,template,'frame wrapper is outside template ownership');
 assert.equal(templateLiterals('// `comment`\nconst r=/[`]/; const q="`quoted`"; '+source).length,2,'comments regex and quoted backticks are not templates');
 assert.equal(documentTemplates('<script type="application/json">{"text":"`JSON`"}</script><script type="text/plain">Unexecuted `plain`</script><script>'+source+'</script>').length,2,'non-executable scripts are not template source');
 assert.notEqual(templateLiterals(source.replace(' After`',' Changed`'))[0].raw,template,'trailing semantic text remains protected');
 assert.notEqual(templateLiterals(source.replace('${value}','${otherValue}'))[0].raw,template,'interpolation expression remains protected');
 console.log('8/8 complete JavaScript template ownership fixtures passed');
}catch(e){if(e.code==='ERR_ASSERTION')protocol.semantic(e.message.split('\n')[0]);else protocol.setup(e);process.exitCode=1;}
