import os, re

os.chdir(r'D:\xuexi\ubuntu\.openclaw\workspace\xinxingai-website')

files = ['index.html', 'about.html', 'services.html', 'process.html']

for f in files:
    with open(f, 'rb') as fh:
        raw = fh.read()
    
    # 去掉 BOM
    if raw[:3] == b'\xef\xbb\xbf':
        raw = raw[3:]
    
    # 修复 \r\r\n -> \n (去掉多余空行)
    text = raw.decode('utf-8', errors='replace')
    
    # 把多个空行合并成一个
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    
    # 修复 description 里的乱码
    text = text.replace('恋?>', '。">')
    text = text.replace('恋?', '。')
    
    # 修复 keywords 缺少闭合引号
    text = text.replace('黔西南相亲>', '黔西南相亲">')
    
    # 修复 meta description 缺少闭合引号
    text = re.sub(r'content="([^"]*?)>', r'content="\1">', text)
    
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(text)
    
    print(f + ' fixed')

# 验证
print('\n=== 验证 ===')
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    # 检查有没有连续3个以上空行
    has_multi_blank = bool(re.search(r'\n\s*\n\s*\n', c))
    has_bad = '\ufffd' in c or '恋?' in c
    print(f + ': multi_blank=' + str(has_multi_blank) + ' bad_chars=' + str(has_bad))
