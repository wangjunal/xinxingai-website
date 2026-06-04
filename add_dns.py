from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    print("OK - 已连接到 Edge")
    
    page = browser.contexts[0].pages[0] if browser.contexts and browser.contexts[0].pages else browser.new_page()
    print(f"页面: {page.url}")
    
    # 看看页面上有什么
    html = page.content()
    with open("D:\\xuexi\\ubuntu\\.openclaw\\workspace\\xinxingai-website\\aliyun_html2.txt", "w", encoding="utf-8") as f:
        f.write(html[:20000])
    
    # 找"添加记录"按钮
    add_btns = page.locator("button:has-text('添加记录'), a:has-text('添加记录'), span:has-text('添加记录'), [class*='add']:has-text('记录')")
    print(f"添加记录按钮数: {add_btns.count()}")
    
    if add_btns.count() > 0:
        add_btns.first.click()
        print("点击了添加记录")
        time.sleep(3)
        
        # 在弹窗中填写
        # 找类型下拉
        type_select = page.locator("select, [class*='select'], [class*='dropdown']").first
        if type_select.count() > 0:
            type_select.select_option("CNAME")
            print("选择了CNAME")
        
        # 找主机记录输入框
        host_input = page.locator("input[placeholder*='记录'], input[placeholder*='主机'], input[placeholder*='www']").first
        if host_input.count() > 0:
            host_input.fill("www")
            print("填了www")
        
        # 找记录值输入框
        val_input = page.locator("input[placeholder*='值'], input[placeholder*='目标'], input[placeholder*='github']").first
        if val_input.count() > 0:
            val_input.fill("wangjunal.github.io")
            print("填了记录值")
        
        # 点确定
        confirm = page.locator("button:has-text('确定'), button:has-text('确认'), button:has-text('保存')").first
        if confirm.count() > 0:
            confirm.click()
            print("点击了确定")
            time.sleep(2)
        
        page.screenshot(path="D:\\xuexi\\ubuntu\\.openclaw\\workspace\\xinxingai-website\\dns_result.png")
        print("已截图保存结果")
    
    print("完成！")
    time.sleep(600)
