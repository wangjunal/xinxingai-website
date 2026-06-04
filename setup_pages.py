from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    
    # 找到 GitHub Pages 页面
    target_page = None
    for ctx in browser.contexts:
        for pg in ctx.pages:
            if "settings/pages" in pg.url:
                target_page = pg
                break
    
    if not target_page:
        print("没找到 Pages 页面，新建一个")
        target_page = browser.new_page()
        target_page.goto("https://github.com/wangjunal/xinxingai-website/settings/pages")
        time.sleep(5)
    
    print(f"当前页面: {target_page.url}")
    
    # 看看页面完整内容
    html = target_page.content()
    with open("D:\\xuexi\\ubuntu\\.openclaw\\workspace\\xinxingai-website\\pages_html.txt", "w", encoding="utf-8") as f:
        f.write(html)
    
    # 找 Custom domain 输入框
    # GitHub Pages 的 Custom domain 输入框特征
    selectors = [
        "input[type='text']",
        "input[aria-label*='domain' i]",
        "input[aria-label*='Domain' i]",
        "input[placeholder*='domain' i]",
        "input[placeholder*='Domain' i]",
        "#custom-domain-input",
        "[data-testid='custom-domain-input']",
        "input[name='domain']",
        "form input[type='text']"
    ]
    
    for sel in selectors:
        try:
            els = target_page.locator(sel)
            count = els.count()
            if count > 0:
                for i in range(count):
                    try:
                        placeholder = els.nth(i).get_attribute("placeholder") or ""
                        aria_label = els.nth(i).get_attribute("aria-label") or ""
                        name = els.nth(i).get_attribute("name") or ""
                        print(f"  输入框{i}: placeholder=[{placeholder}] aria=[{aria_label}] name=[{name}]")
                    except:
                        pass
        except:
            pass
    
    # 也找找所有 label
    labels = target_page.locator("label")
    for i in range(labels.count()):
        try:
            text = labels.nth(i).inner_text()
            if text.strip():
                print(f"Label{i}: [{text.strip()}]")
        except:
            pass
    
    # 截图
    target_page.screenshot(path="D:\\xuexi\\ubuntu\\.openclaw\\workspace\\xinxingai-website\\pages_full.png", full_page=True)
    print("\n已截图保存到 pages_full.png")
    
    # 保持浏览器打开
    while True:
        time.sleep(60)
