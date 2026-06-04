import re, os

os.chdir(r'D:\xuexi\ubuntu\.openclaw\workspace\xinxingai-website')

# 1. 先处理首页：删除红娘团队和成功案例区块，补全导航
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 删除红娘团队区块
c = re.sub(r'<!-- ====== 红娘团队 ====== -->.*?(?=<!-- ====== 服务概览 ====== -->)', '', c, flags=re.DOTALL)

# 删除成功案例区块
c = re.sub(r'<!-- ====== 成功案例 ====== -->.*?(?=<!-- ====== CTA 行动号召 ====== -->)', '', c, flags=re.DOTALL)

# 补全导航：加上红娘团队和入驻流程
nav_old = '<li><a href="index.html" class="active">首页</a></li>\n      <li><a href="about.html">公司介绍</a></li>\n      <li><a href="services.html">服务项目</a></li>\n      <li><a href="cases.html">成功案例</a></li>\n      <li><a href="events.html">活动中心</a></li>\n      <li><a href="contact.html">联系我们</a></li>\n      <li><a href="message.html" class="nav-cta">在线留言</a></li>'

nav_new = '<li><a href="index.html" class="active">首页</a></li>\n      <li><a href="about.html">公司介绍</a></li>\n      <li><a href="services.html">服务项目</a></li>\n      <li><a href="hongniang.html">红娘团队</a></li>\n      <li><a href="process.html">入驻流程</a></li>\n      <li><a href="cases.html">成功案例</a></li>\n      <li><a href="events.html">活动中心</a></li>\n      <li><a href="contact.html">联系我们</a></li>\n      <li><a href="message.html" class="nav-cta">在线留言</a></li>'

c = c.replace(nav_old, nav_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('index.html: 删除红娘团队+成功案例+补全导航')

# 2. 修复所有文件的乱码标签
files = ['index.html', 'about.html', 'services.html', 'cases.html', 'events.html', 'contact.html', 'message.html', 'hongniang.html', 'process.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    # 修复所有 /h3> /h2> /h4> /p> /li> /ul> /div> /section> /span> /a> 等
    c = re.sub(r'/(h[234]|p|li|ul|div|section|span|a)>', r'</\1>', c)
    
    # 修复其他标签
    c = c.replace('/title>', '</title>')
    c = c.replace('/head>', '</head>')
    c = c.replace('/body>', '</body>')
    c = c.replace('/html>', '</html>')
    c = c.replace('/nav>', '</nav>')
    c = c.replace('/form>', '</form>')
    c = c.replace('/footer>', '</footer>')
    
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(c)
    
    print(f + ': 乱码修复')

# 3. 验证
print('\n=== 验证 ===')
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    # 检查乱码
    bad_tags = re.findall(r'/(h[234]|p|li|ul|div|section|span|a)>', c)
    bad_other = '/title>' in c or '/head>' in c or '/body>' in c or '/html>' in c
    
    # 检查关键标签
    has_doctype = '<!DOCTYPE html>' in c
    has_title_open = '<title>' in c
    has_title_close = '</title>' in c
    
    # 检查导航
    nav_items = re.findall(r'<li><a href="([^"]+)"[^>]*>([^<]+)</a></li>', c)
    
    print(f + ': bad_tags=' + str(len(bad_tags)) + ' bad_other=' + str(bad_other) + ' title_ok=' + str(has_title_open and has_title_close))
    
    if f == 'index.html':
        has_hongniang = '专业红娘团队' in c
        has_case = '成功案例' in c
        print('  首页红娘团队=' + str(has_hongniang) + ' 成功案例=' + str(has_case))
        print('  导航项数=' + str(len(nav_items)))
        for href, text in nav_items:
            print('    ' + text + ' -> ' + href)
