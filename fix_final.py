import re, os

os.chdir(r'D:\xuexi\ubuntu\.openclaw\workspace\xinxingai-website')

# ===== 1. 首页：删除红娘团队和成功案例区块，补全导航 =====
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 删除红娘团队区块（从注释到下一个注释）
c = re.sub(r'<!-- ====== 红娘团队 ====== -->.*?<!-- ====== 服务概览 ====== -->', '<!-- ====== 服务概览 ====== -->', c, flags=re.DOTALL)

# 删除成功案例区块（从注释到下一个注释）
c = re.sub(r'<!-- ====== 成功案例 ====== -->.*?<!-- ====== CTA 行动号召 ====== -->', '<!-- ====== CTA 行动号召 ====== -->', c, flags=re.DOTALL)

# 补全导航：加红娘团队和入驻流程
old_nav = '<li><a href="index.html" class="active">首页</a></li>\n      <li><a href="about.html">公司介绍</a></li>\n      <li><a href="services.html">服务项目</a></li>\n      <li><a href="cases.html">成功案例</a></li>\n      <li><a href="events.html">活动中心</a></li>\n      <li><a href="contact.html">联系我们</a></li>\n      <li><a href="message.html" class="nav-cta">在线留言</a></li>'

new_nav = '<li><a href="index.html" class="active">首页</a></li>\n      <li><a href="about.html">公司介绍</a></li>\n      <li><a href="services.html">服务项目</a></li>\n      <li><a href="hongniang.html">红娘团队</a></li>\n      <li><a href="process.html">入驻流程</a></li>\n      <li><a href="cases.html">成功案例</a></li>\n      <li><a href="events.html">活动中心</a></li>\n      <li><a href="contact.html">联系我们</a></li>\n      <li><a href="message.html" class="nav-cta">在线留言</a></li>'

c = c.replace(old_nav, new_nav)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('index.html: 删除红娘团队+成功案例+补全导航')

# ===== 2. 修复所有文件的乱码 =====
files = ['index.html', 'about.html', 'services.html', 'cases.html', 'events.html', 'contact.html', 'message.html', 'hongniang.html', 'process.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    # 只修复真正的乱码：/h3> /h2> /p> 等（没有<前缀的）
    # 注意：</h3> 是正常的，/h3> 才是乱码
    c = re.sub(r'(?<!<)/(h[234]|p|li|ul|div|section|span|a|title|head|body|html|nav|form|footer)>', r'</\1>', c)
    
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(c)
    
    print(f + ': 乱码修复')

# ===== 3. 验证 =====
print('\n=== 验证 ===')
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    # 检查乱码（真正的乱码，不是正常标签）
    bad = bool(re.search(r'(?<!<)/(h[234]|p|li|ul|div|section|span|a|title|head|body|html|nav|form|footer)>', c))
    has_garbage = '<<' in c
    has_bad_char = '\ufffd' in c
    
    print(f + ': 乱码=' + str(bad) + ' <<垃圾=' + str(has_garbage) + ' 坏字符=' + str(has_bad_char))

# 首页专项检查
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()
print('\n首页检查:')
print('  红娘团队区块:', '红娘团队' in c)
print('  成功案例区块:', '成功案例' in c)
# 检查导航
nav_items = re.findall(r'<li><a href="([^"]+)"[^>]*>([^<]+)</a></li>', c)
print('  导航项数:', len(nav_items))
for href, text in nav_items:
    print('    ' + text + ' -> ' + href)
