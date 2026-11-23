/* Exercise a future JSON-only language in actual source/bundle/any/wheel HTML. */
'use strict';
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const {chromium}=require(process.env.ORCA_PLAYWRIGHT_MODULE || 'playwright');
const fixtures=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const report={ok:false,cases:[],errors:[],scope:'Synthetic language data only; four real distribution formats, page/dock. No native OrcaSlicer.'};
(async()=>{
  const browser=await chromium.launch({headless:true,args:["--use-angle=swiftshader","--enable-webgl","--ignore-gpu-blocklist","--enable-unsafe-swiftshader"],...(process.env.ORCA_BROWSER_EXECUTABLE?{executablePath:process.env.ORCA_BROWSER_EXECUTABLE}:{})});
  try{
    for(const fixture of fixtures){
      const page=await browser.newPage({viewport:{width:fixture.mode==='dock'?380:1600,height:960}});
      page.on('pageerror',error=>report.errors.push(String(error)));
      page.on('console',message=>{if(message.type()==='error')report.errors.push(message.text());});
      await page.setContent(fixture.html);
      assert.equal(await page.locator('html').getAttribute('lang'),fixture.lang);
      assert.equal(await page.locator('html').getAttribute('dir'),'ltr');
      assert.equal(await page.locator('#language option').count(),fixture.options);
      assert.equal(await page.locator('[data-i18n="sec_presets"]').textContent(),'Modellengalerij');
      assert.equal(await page.locator('[data-slider="height"] .ctrl-label').textContent(),'Container height','missing key must use English');
      await page.locator('#language').selectOption('it');
      assert.equal(await page.locator('html').getAttribute('lang'),'it');
      await page.locator('#language').selectOption(fixture.lang);
      assert.equal(await page.locator('[data-i18n="sec_presets"]').textContent(),'Modellengalerij');
      report.cases.push({format:fixture.format,mode:fixture.mode,code:fixture.lang,discovered:true,fallback:true});
      await page.close();
    }
    assert.deepEqual(report.errors,[]);report.ok=true;
  }finally{
    await browser.close();
    const output=process.env.ORCA_LANGUAGE_EXTENSION_OUTPUT || path.join(__dirname,'../test-output/language-extension');
    fs.mkdirSync(output,{recursive:true});fs.writeFileSync(path.join(output,'report.json'),JSON.stringify(report,null,2)+'\n');
  }
  console.log(JSON.stringify({ok:report.ok,cases:report.cases.length,errors:report.errors}));
})().catch(error=>{console.error(error);process.exitCode=1});
