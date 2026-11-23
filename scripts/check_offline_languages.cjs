/* Real offline controller, meshes and exports. Native Orca transport disabled. */
'use strict';
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const {spawn}=require('node:child_process');
const {chromium}=require(process.env.ORCA_PLAYWRIGHT_MODULE||'playwright');
const root=path.resolve(__dirname,'..');
const output=process.env.ORCA_LANGUAGE_OUTPUT||path.join(root,'test-output','languages');
const codes=['pt','en','es','it','fr','de','ja'];
const expectedOptions=fs.readdirSync(path.join(root,'src/thread_studio/locales')).filter(name=>name.endsWith('.json')).length;
const catalogs=Object.fromEntries(codes.map(code=>[code,JSON.parse(fs.readFileSync(path.join(root,'src/thread_studio/locales',code+'.json'),'utf8')).translations]));
const report={ok:false,cases:[],exports:[],errors:[],nativeApplicationTest:false};
const server=spawn(process.env.ORCA_TEST_PYTHON||'python',['-B','-W','error',path.join(__dirname,'ui_test_server.py')],{cwd:root,stdio:['ignore','pipe','pipe']});
let browser,logs='';server.stderr.on('data',data=>logs+=data.toString());
const ready=new Promise((resolve,reject)=>{
 const timeout=setTimeout(()=>reject(Error('Backend startup timed out: '+logs)),30000);let pending='';
 server.stdout.on('data',data=>{pending+=data;const lines=pending.split(/\r?\n/);pending=lines.pop();for(const line of lines){try{const row=JSON.parse(line);if(row.url){clearTimeout(timeout);resolve(row.url);}}catch{}}});
 server.once('exit',code=>{clearTimeout(timeout);reject(Error('Backend exited '+code+': '+logs));});server.once('error',reject);
});
const count=page=>page.evaluate(()=>window.__sentMessages.filter(m=>['update','ready','analyze'].includes(m.type)).length);
const geometry=page=>page.waitForFunction(()=>window.__hostMessages.some(m=>m.type==='geometry'&&m.meshes>0),null,{timeout:120000});
async function changeLanguage(page,code){
 const before=await page.evaluate(()=>window.__hostMessages.length);
 await page.locator('#language').selectOption(code);
 try {
  await page.waitForFunction(({code,before})=>document.documentElement.lang===code&&window.__hostMessages.slice(before).some(m=>m.type==='preferences_updated'&&m.lang===code),{code,before});
 } catch(error) {
  fs.writeFileSync(path.join(output,'language-failure.json'),JSON.stringify({code,before,state:await page.evaluate(()=>({lang:document.documentElement.lang,selected:document.querySelector('#language').value,sent:window.__sentMessages.slice(-8),received:window.__hostMessages.slice(-12),status:document.querySelector('#status').textContent}))},null,2));
  throw error;
 }
}
(async()=>{
 fs.mkdirSync(output,{recursive:true});const url=await ready;
 try{
  browser=await chromium.launch({headless:true,args:['--use-angle=swiftshader','--enable-webgl','--ignore-gpu-blocklist','--enable-unsafe-swiftshader'],...(process.env.ORCA_CHROMIUM_PATH?{executablePath:process.env.ORCA_CHROMIUM_PATH}:{})});
  for(const mode of ['page','dock']){
   const page=await browser.newPage({viewport:{width:mode==='page'?1600:400,height:960}});
   page.on('pageerror',error=>report.errors.push(String(error)));
   page.on('console',message=>{if(message.type()==='error')report.errors.push(message.text());});
   await page.goto(url+'/?lang=pt&theme=dark'+(mode==='dock'?'&dock':''));await geometry(page);
   const requests=await count(page);
   for(const theme of ['dark','light']){
    if(await page.locator('html').getAttribute('data-theme')!==theme){await page.locator('#theme').click();await page.waitForFunction(theme=>document.documentElement.dataset.theme===theme,theme);await page.waitForFunction(theme=>window.__hostMessages.some(m=>m.type==='geometry'&&m.params?.theme===theme),theme);}
    const baseline=await count(page);
    for(const code of codes){
     await changeLanguage(page,code);const vocabulary=catalogs[code];
     assert.equal(await page.locator('[data-i18n="sec_presets"]').textContent(),vocabulary['Model Gallery']);
     assert.equal(await page.locator('[data-slider="height"] .ctrl-label').textContent(),vocabulary['Container height']);
     assert.equal(await page.locator('.preset-name').first().textContent(),vocabulary['EDC jar 40']);
     assert.equal(await page.locator('#language option').count(),expectedOptions);
     assert.equal(await count(page),baseline,'Changing language requested geometry');
     assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false,'Horizontal overflow');
     assert.equal(await page.locator('#status').textContent(),vocabulary['Mesh updated.']);
     if(mode==='dock')for(const section of ['shape','textures','print','presets']){await page.locator(`.dock-tab-btn[data-tab="${section}"]`).click();assert(await page.locator('.dock-global-footer').isVisible());}
     await page.screenshot({path:path.join(output,`${mode}-${code}-${theme}.png`)});
     report.cases.push({mode,theme,code,geometryUnchanged:true});
    }
   }
   // Preserve user text even when it equals a source phrase.
   await page.locator('#inp-design-name').fill('Model Gallery');await page.locator('#inp-design-name').press('Tab');
   await page.waitForFunction(()=>window.__hostMessages.some(m=>m.type==='geometry'&&m.params?.name==='Model Gallery'));
   await changeLanguage(page,'it');assert.equal(await page.locator('#inp-design-name').inputValue(),'Model Gallery');
   if(mode==='page'){
    await page.locator('#printer-pill').click();await page.waitForFunction(()=>window.__hostMessages.some(m=>m.type==='host_state'));
   }
   assert.equal(await page.locator('#language').inputValue(),'it');
   // A blocked real preset must keep the translated warning while switching.
   if(mode==='dock')await page.locator('.dock-tab-btn[data-tab="presets"]').click();
   await page.locator('.preset-card[data-preset-id="mason86"]').click();
   await page.waitForFunction(()=>window.__hostMessages.some(m=>m.type==='geometry'&&m.params?.standard==='mason_86'&&m.meshes===0));
   const blockedCount=await count(page),warning='Mason 86 experimental: confirm measured dimensions before generation';
   for(const code of codes){await changeLanguage(page,code);assert.equal(await page.locator('#warning').textContent(),catalogs[code][warning]);assert.equal(await page.locator('#hud-warnings').textContent(),catalogs[code][warning]);assert.equal(await count(page),blockedCount);}
   await page.locator('.preset-card[data-preset-id="edc"]').click();
   await page.waitForFunction(()=>window.__hostMessages.filter(m=>m.type==='geometry').at(-1)?.params?.standard==='fdm_trapezoid_45'&&window.__hostMessages.filter(m=>m.type==='geometry').at(-1)?.meshes>0);
   for(const code of codes){
    await changeLanguage(page,code);
    for(const [format,action] of [['stl','export_stl'],['3mf','export_3mf']]){
     const before=await page.evaluate(()=>window.__hostMessages.length);
     const buttons=page.locator(`[data-action="${action}"]`);for(let i=0;i<await buttons.count();i++)if(await buttons.nth(i).isVisible()){await buttons.nth(i).click();break;}
     await page.waitForFunction(before=>window.__hostMessages.slice(before).some(m=>m.type==='action_result'&&m.ok!==null),before,{timeout:120000});
     const result=await page.evaluate(before=>window.__hostMessages.slice(before).find(m=>m.type==='action_result'&&m.ok!==null),before);
     assert.equal(result.ok,true,JSON.stringify(result));assert.equal(await page.locator('#language').inputValue(),code);
     assert((await page.locator('#status').textContent()).startsWith(catalogs[code]['Files exported.']));
     report.exports.push({mode,code,format,files:result.paths.length,ok:true});
    }
   }
   await changeLanguage(page,'it');await page.goto(url+'/?theme=dark'+(mode==='dock'?'&dock':''));await geometry(page);assert.equal(await page.locator('#language').inputValue(),'it');
   await page.close();
  }
  // Real page/dock receivers synchronize without requesting another mesh.
  const first=await browser.newPage(),second=await browser.newPage();
  for(const page of [first,second]){await page.goto(url+'/?theme=dark');await geometry(page);}
  await changeLanguage(first,'fr');await second.waitForFunction(()=>document.documentElement.lang==='fr');
  report.crossViewSync=true;
  assert.deepEqual(report.errors,[]);report.ok=true;
 }finally{
  if(browser)await browser.close();server.kill();fs.writeFileSync(path.join(output,'report.json'),JSON.stringify(report,null,2)+'\n');
 }
 console.log(JSON.stringify({ok:report.ok,cases:report.cases.length,exports:report.exports.length,output}));
})().catch(error=>{console.error(error);process.exitCode=1;server.kill();});
