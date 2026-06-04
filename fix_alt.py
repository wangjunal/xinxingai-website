import os, re

os.chdir(r'D:\xuexi\ubuntu\.openclaw\workspace\xinxingai-website')

files = ['index.html', 'about.html', 'services.html', 'cases.html', 'events.html', 'contact.html', 'message.html', 'hongniang.html', 'process.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    # 修复 alt 属性被破坏的问题
    # 把 alt="xxx? class= 修复为 alt="xxx" class=
    c = re.sub(r'alt="([^"]*?)[?]\s+class=', r'alt="\1" class=', c)
    
    # 修复 alt="xxx? 结尾没引号
    c = re.sub(r'alt="([^"]*?)[?](\s|>)', r'alt="\1"\2', c)
    
    # 修复任何残留的 ? 在属性值里
    c = c.replace('\ufffd', '')
    
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(c)
    
    print(f + ' fixed')

# 验证
print('\n=== 验证 ===')
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    bad_alt = bool(re.search(r'alt="[^"]*[?]', c))
    bad_char = '\ufffd' in c
    print(f + ': bad_alt=' + str(bad_alt) + ' bad_char=' + str(bad_char))
