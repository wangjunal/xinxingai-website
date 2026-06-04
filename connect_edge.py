from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    print("OK - 已连接到 Edge")
    
    page = browser.contexts[0].pages[0] if browser.contexts and browser.contexts[0].pages else browser.new_page()
    print(f"页面: {page.url}")
    
    # 导航到阿里云DNS
    page.goto("https://dns.console.aliyun.com/")
    time.sleep(5)
    print(f"当前: {page.url}")
    
    # 看看页面有什么
    html = page.content()
    # 保存HTML分析
    with open("D:\\xuexi\\ubuntu\\.openclaw\\workspace\\xinxingai-website\\aliyun_html.txt", "w", encoding="utf-8") as f:
        f.write(html[:10000])
    print("已保存页面HTML")
    
    # 尝试各种方式找到域名
    selectors = [
        "text=xshlxx",
        "a:has-text('xshlxx')",
        "span:has-text('xshlxx')",
        "td:has-text('xshlxx')",
        "[class*='domain']:has-text('xshlxx')",
        "//*[contains(text(), 'xshlxx')]"
    ]
    
    for sel in selectors:
        try:
            el = page.locator(sel)
            if el.count() > 0:
                print(f"找到元素: {sel}, 数量: {el.count()}")
                el.first.click()
                print("已点击")
                time.sleep(3)
                page.screenshot(path="D:\\xuexi\\ubuntu\\.openclaw\\workspace\\xinxingai-website\\after_click.png")
                break
        except:
            pass
    
    # 如果还没找到，尝试查找"解析设置"按钮
    try:
        btn = page.locator("button:has-text('解析设置'), a:has-text('解析设置'), span:has-text('解析设置')")
        if btn.count() > 0:
            print(f"找到解析设置按钮")
            btn.first.click()
            time.sleep(3)
    except:
        pass
    
    input("按回车退出...")
    browser.close()
