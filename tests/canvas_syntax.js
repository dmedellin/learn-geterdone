'use strict';
// Supplemental compiled-function reflection uses the parser already shipped
// inside Node. The independent source-inventory lexer remains dependency-free.
const vm=require('node:vm'),crypto=require('node:crypto');
const key='internal/deps/acorn/acorn/dist/acorn',source=process.binding('natives')[key];
if(typeof source!=='string')throw Error('source reflection setup failure: installed Node parser unavailable');
const output={};vm.runInNewContext(source,{exports:output,module:{exports:output}},{filename:'node-bundled-canvas-parser.js',timeout:5000});
const parserIdentity=Object.freeze({node:process.version,parser:output.version,sha256:crypto.createHash('sha256').update(source).digest('hex'),origin:'Parser bundled into the installed Node runtime; no vendored or downloaded parser.'});
function coverageSyntax(source){
 const ast=output.parse(source,{ecmaVersion:2024,sourceType:'script'}),owners=[{start:0,end:source.length,kind:'program'}];
 function walk(node,parent=null){
  if(['FunctionDeclaration','FunctionExpression','ArrowFunctionExpression'].includes(node.type))owners.push({start:parent?.type==='Property'&&parent.method?parent.start:node.start,end:node.end,kind:'function'});
  for(const value of Object.values(node))if(Array.isArray(value)){for(const child of value)if(child&&typeof child.type==='string')walk(child,node);}else if(value&&typeof value.type==='string')walk(value,node);
 }
 walk(ast);return owners;
}
module.exports={coverageSyntax,parserIdentity};
