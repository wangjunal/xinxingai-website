import os, re

os.chdir(r'D:\xuexi\ubuntu\.openclaw\workspace\xinxingai-website')

files = ['index.html', 'about.html', 'services.html', 'process.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    print('=== ' + f + ' ===')
    
    # 检查 title
    m = re.search(r'<title>(.*?)</title>', c)
    print('Title: ' + (m.group(1) if m else 'NOT FOUND'))
    
    # 检查所有 href
    for m in re.finditer(r'href=["\']([^"\']+)["\']', c):
        href = m.group(1)
        if '\ufffd' in href or '?' in href:
            print('  BAD href: ' + href)
    
    # 检查所有 src
    for m in re.finditer(r'src=["\']([^"\']+)["\']', c):
        src = m.group(1)
        if '\ufffd' in src or '?' in src:
            print('  BAD src: ' + src)
    
    # 检查所有 img alt
    for m in re.finditer(r'alt=["\']([^"\']*)["\']', c):
        alt = m.group(1)
        if '\ufffd' in alt or '?' in alt:
            print('  BAD alt: ' + alt)
    
    print('')
