import re, os

os.chdir(r'D:\xuexi\ubuntu\.openclaw\workspace\xinxingai-website')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 删除红娘团队区块
start = c.find('<!-- ====== 红娘团队 ====== -->')
end = c.find('<!-- ====== 服务概览 ====== -->')
if start >= 0 and end >= 0:
    c = c[:start] + c[end:]
    print('红娘团队区块已删除')

# 删除成功案例区块
start2 = c.find('<!-- ====== 成功案例 ====== -->')
end2 = c.find('<!-- ====== CTA 行动号召 ====== -->')
if start2 >= 0 and end2 >= 0:
    c = c[:start2] + c[end2:]
    print('成功案例区块已删除')

# 补全导航
old_nav = '<li><a href="index.html" class="active">首页</a></li>\n\n\n\n      <li><a href="about.html">公司介绍</a></li>\n\n\n\n      <li><a href="services.html">服务项目</a></li>\n\n\n\n      <li><a href="cases.html">成功案例</a></li>\n\n\n\n      <li><a href="events.html">活动中心</a></li>\n\n\n\n      <li><a href="contact.html">联系我们</a></li>\n\n\n\n      <li><a href="message.html" class="nav-cta">在线留言</a></li>'

new_nav = '<li><a href="index.html" class="active">首页</a></li>\n      <li><a href="about.html">公司介绍</a></li>\n      <li><a href="services.html">服务项目</a></li>\n      <li><a href="hongniang.html">红娘团队</a></li>\n      <li><a href="process.html">入驻流程</a></li>\n      <li><a href="cases.html">成功案例</a></li>\n      <li><a href="events.html">活动中心</a></li>\n      <li><a href="contact.html">联系我们</a></li>\n      <li><a href="message.html" class="nav-cta">在线留言</a></li>'

c = c.replace(old_nav, new_nav)

# 清理多余空行
c = re.sub(r'\n{4,}', '\n\n', c)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

# 验证
print('\n首页检查:')
print('  红娘团队:', '红娘团队' in c)
print('  成功案例:', '成功案例' in c)
nav_items = re.findall(r'<li><a href="([^"]+)"[^>]*>([^<]+)</a></li>', c)
print('  导航项数:', len(nav_items))
for href, text in nav_items:
    print('    ' + text + ' -> ' + href)
