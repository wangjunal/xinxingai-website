import re, os

os.chdir(r'D:\xuexi\ubuntu\.openclaw\workspace\xinxingai-website')

files = ['index.html', 'about.html', 'services.html', 'cases.html', 'events.html', 'contact.html', 'message.html', 'hongniang.html', 'process.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    # 修复 << 双写问题
    c = c.replace('<<', '<')
    
    # 修复 >> 双写问题
    c = c.replace('>>', '>')
    
    # 修复 /h3> /h2> /p> 等乱码（没有 < 前缀的）
    c = re.sub(r'(?<!<)/(h[234]|p|li|ul|div|section|span|a|title|head|body|html|nav|form|footer)>', r'</\1>', c)
    
    # 修复 alt 引号被吃掉
    c = c.replace('alt="心幸爱·喜柿婚恋 class="logo-img"', 'alt="心幸爱·喜柿婚恋" class="logo-img"')
    c = c.replace('alt="心幸爱·喜柿婚恋 class="footer-logo"', 'alt="心幸爱·喜柿婚恋" class="footer-logo"')
    
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(c)
    
    print(f + ' fixed')

# ===== 首页：删除红娘团队和成功案例区块，补全导航 =====
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 删除红娘团队区块
c = re.sub(r'<!-- ====== 红娘团队 ====== -->.*?<!-- ====== 服务概览 ====== -->', '<!-- ====== 服务概览 ====== -->', c, flags=re.DOTALL)

# 删除成功案例区块
c = re.sub(r'<!-- ====== 成功案例 ====== -->.*?<!-- ====== CTA 行动号召 ====== -->', '<!-- ====== CTA 行动号召 ====== -->', c, flags=re.DOTALL)

# 补全导航
old_nav = '<li><a href="index.html" class="active">首页</a></li>\n      <li><a href="about.html">公司介绍</a></li>\n      <li><a href="services.html">服务项目</a></li>\n      <li><a href="cases.html">成功案例</a></li>\n      <li><a href="events.html">活动中心</a></li>\n      <li><a href="contact.html">联系我们</a></li>\n      <li><a href="message.html" class="nav-cta">在线留言</a></li>'

new_nav = '<li><a href="index.html" class="active">首页</a></li>\n      <li><a href="about.html">公司介绍</a></li>\n      <li><a href="services.html">服务项目</a></li>\n      <li><a href="hongniang.html">红娘团队</a></li>\n      <li><a href="process.html">入驻流程</a></li>\n      <li><a href="cases.html">成功案例</a></li>\n      <li><a href="events.html">活动中心</a></li>\n      <li><a href="contact.html">联系我们</a></li>\n      <li><a href="message.html" class="nav-cta">在线留言</a></li>'

c = c.replace(old_nav, new_nav)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('index.html: 删除红娘团队+成功案例+补全导航')

# ===== 验证 =====
print('\n=== 验证 ===')
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    bad_tags = bool(re.search(r'(?<!<)/(h[234]|p|li|ul|div|section|span|a|title|head|body|html|nav|form|footer)>', c))
    has_double = '<<' in c or '>>' in c
    has_bad = '\ufffd' in c
    
    print(f + ': 乱码=' + str(bad_tags) + ' 双写=' + str(has_double) + ' 坏字符=' + str(has_bad))

# 首页专项
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()
print('\n首页:')
print('  红娘团队区块:', '红娘团队' in c)
print('  成功案例区块:', '成功案例' in c)
nav_items = re.findall(r'<li><a href="([^"]+)"[^>]*>([^<]+)</a></li>', c)
print('  导航项数:', len(nav_items))
for href, text in nav_items:
    print('    ' + text + ' -> ' + href)
