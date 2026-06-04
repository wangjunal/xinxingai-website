from playwright.sync_api import sync_playwright
import time

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        executable_path=EDGE_PATH,
        args=["--start-maximized"]
    )
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    
    # 打开阿里云 DNS
    page.goto("https://dns.console.aliyun.com/")
    print("=== Edge 浏览器已打开 ===")
    print("请登录阿里云，然后告诉我「已登录」")
    print()
    
    # 等待用户说已登录
    input("登录后按回车继续...")
    
    # 截图看看当前页面
    page.screenshot(path="D:\\xuexi\\ubuntu\\.openclaw\\workspace\\xinxingai-website\\aliyun_step1.png")
    print("已截图，正在分析页面...")
    time.sleep(2)
    
    # 尝试找到域名并点击
    try:
        # 看看页面上有什么
        title = page.title()
        print(f"页面标题: {title}")
        
        # 尝试点击域名 xshlxx.com
        link = page.locator("text=xshlxx.com")
        if link.count() > 0:
            link.first.click()
            print("点击了 xshlxx.com")
            time.sleep(3)
        else:
            print("没找到 xshlxx.com 链接，看看页面内容")
            page.screenshot(path="D:\\xuexi\\ubuntu\\.openclaw\\workspace\\xinxingai-website\\aliyun_step2.png")
    except Exception as e:
        print(f"点击出错: {e}")
        page.screenshot(path="D:\\xuexi\\ubuntu\\.openclaw\\workspace\\xinxingai-website\\aliyun_error.png")
    
    input("\n按回车关闭浏览器...")
    browser.close()
