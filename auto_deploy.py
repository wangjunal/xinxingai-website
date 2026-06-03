from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # 第1步：GitHub 创建仓库
    page.goto("https://github.com/new")
    print("=== 浏览器已打开 ===")
    print("【第1步】请在浏览器中：")
    print("  1. 登录 GitHub")
    print("  2. 仓库名填: xinxingai-website")
    print("  3. 选 Public")
    print("  4. 勾选 Add a README")
    print("  5. 点 Create repository")
    print()
    
    # 等待跳转到仓库页面
    while "xinxingai-website" not in page.url:
        time.sleep(2)
    
    print("✓ 仓库创建成功！")
    time.sleep(2)
    
    # 获取用户名
    username = page.evaluate("() => document.querySelector('meta[name=\"user-login\"]')?.content || ''")
    repo_url = f"https://github.com/{username}/xinxingai-website.git"
    print(f"仓库地址: {repo_url}")
    
    # 保存仓库地址
    with open("D:\\xuexi\\ubuntu\\.openclaw\\workspace\\xinxingai-website\\repo_url.txt", "w") as f:
        f.write(repo_url)
    
    # 第2步：阿里云 DNS
    page.goto("https://dns.console.aliyun.com/")
    print("\n=== 浏览器已跳转到阿里云DNS ===")
    print("【第2步】请在浏览器中：")
    print("  1. 登录阿里云")
    print("  2. 找到域名 xshlxx.com")
    print("  3. 添加两条CNAME记录：")
    print(f"     记录1: www → {username}.github.io")
    print(f"     记录2: @ → {username}.github.io")
    print()
    print("添加完成后，回到这里告诉我，我来继续后面的操作")
    
    # 保持浏览器打开
    time.sleep(600)
    browser.close()
