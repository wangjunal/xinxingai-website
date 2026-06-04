import os

files = ['index.html', 'about.html', 'services.html', 'cases.html', 'events.html', 'contact.html', 'message.html', 'hongniang.html', 'process.html']

for f in files:
    with open(f, 'rb') as fh:
        raw = fh.read()
    
    # 去掉 BOM
    if raw[:3] == b'\xef\xbb\xbf':
        raw = raw[3:]
    
    # 修复 \r\r\n -> \r\n
    raw = raw.replace(b'\r\r\n', b'\r\n')
    
    text = raw.decode('utf-8', errors='replace')
    
    # 修复所有被破坏的 title 标签
    text = text.replace('/title>', '</title>')
    
    # 修复其他乱码
    text = text.replace('\ufffd', '')
    
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(text)
    
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    has_close_title = '</title>' in c
    has_bad = '\ufffd' in c
    print(f + ': title_ok=' + str(has_close_title) + ' 乱码=' + str(has_bad))
