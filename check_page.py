from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    page = browser.contexts[0].pages[0]
    print(f"当前页面: {page.url}")
    
    # 看看有没有"添加记录"按钮
    btns = page.locator("button")
    for i in range(btns.count()):
        try:
            text = btns.nth(i).inner_text()
            if text.strip():
                print(f"按钮{i}: [{text.strip()}]")
        except:
            pass
    
    # 看看有没有输入框
    inputs = page.locator("input")
    for i in range(inputs.count()):
        try:
            placeholder = inputs.nth(i).get_attribute("placeholder") or ""
            print(f"输入框{i}: placeholder=[{placeholder}]")
        except:
            pass
    
    # 看看有没有下拉框
    selects = page.locator("select")
    for i in range(selects.count()):
        try:
            print(f"下拉框{i}: 存在")
        except:
            pass
    
    print("\n页面分析完成，浏览器保持打开")
    while True:
        time.sleep(60)
