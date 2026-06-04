import re, os

os.chdir(r'D:\xuexi\ubuntu\.openclaw\workspace\xinxingai-website')

files = ['index.html', 'about.html', 'services.html', 'cases.html', 'events.html', 'contact.html', 'message.html', 'hongniang.html', 'process.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    # 1. 修复所有 /h3> /h2> /h4> /p> 等乱码
    c = re.sub(r'/(h[234]|p|li|ul|div|section|span|a)>', r'</\1>', c)
    
    # 2. 修复其他被破坏的闭合标签
    c = c.replace('/title>', '</title>')
    c = c.replace('/head>', '</head>')
    c = c.replace('/body>', '</body>')
    c = c.replace('/html>', '</html>')
    c = c.replace('/nav>', '</nav>')
    c = c.replace('/form>', '</form>')
    
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(c)
    
    print(f + ' fixed')

print('\n=== 验证 ===')
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    bad = bool(re.search(r'/(h[234]|p|li|ul|div|section|span|a)>', c))
    print(f + ': ' + ('OK' if not bad else '仍有乱码'))
