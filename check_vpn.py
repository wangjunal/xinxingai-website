from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    
    # 检查ikuuu - 常见端口
    import subprocess
    result = subprocess.run(["netstat", "-ano"], capture_output=True, text=True)
    lines = result.stdout.split("\n")
    
    # 找ikuuu/clash相关端口
    keywords = ["7890", "7891", "7892", "1080", "1081", "10809"]
    for line in lines:
        for kw in keywords:
            if kw in line and ("LISTENING" in line or "ESTABLISHED" in line):
                print(f"  端口: {line.strip()}")
    
    # 检查进程
    result2 = subprocess.run(["tasklist"], capture_output=True, text=True)
    for proc in ["clash", "ikuuu", "v2ray", "trojan", "ss-local", "shadowsocks"]:
        if proc in result2.stdout.lower():
            print(f"  进程: {proc} 运行中")
    
    # 检查系统代理设置
    import winreg
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Internet Settings")
        proxy_enable, _ = winreg.QueryValueEx(key, "ProxyEnable")
        proxy_server, _ = winreg.QueryValueEx(key, "ProxyServer")
        print(f"  系统代理: {'开启' if proxy_enable else '关闭'}, 服务器: {proxy_server}")
        winreg.CloseKey(key)
    except:
        pass
    
    print("\n检查完成，浏览器保持打开")
    while True:
        time.sleep(60)
