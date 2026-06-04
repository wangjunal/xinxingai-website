import re, os

os.chdir(r'D:\xuexi\ubuntu\.openclaw\workspace\xinxingai-website')

files = ['index.html', 'about.html', 'services.html', 'cases.html', 'events.html', 'contact.html', 'message.html', 'hongniang.html', 'process.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    # 修复 alt 缺少闭合引号
    c = c.replace('alt="心幸爱·喜柿婚恋 class="logo-img"', 'alt="心幸爱·喜柿婚恋" class="logo-img"')
    c = c.replace('alt="心幸爱·喜柿婚恋 class="footer-logo"', 'alt="心幸爱·喜柿婚恋" class="footer-logo"')
    
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(c)
    
    print(f + ' fixed')

print('\n=== 验证 ===')
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    bad = 'alt="心幸爱·喜柿婚恋 class=' in c
    print(f + ': ' + ('OK' if not bad else 'STILL BAD'))
