import re, os

os.chdir(r'D:\xuexi\ubuntu\.openclaw\workspace\xinxingai-website')

# 1. 修复 about.html 的 ?
with open('about.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('效率。?">', '效率。">')
c = c.replace('连接。?</p>', '连接。</p>')
c = c.replace('效率。?</p>', '效率。</p>')
c = c.replace('有限公司?&copy;', '有限公司 &copy;')

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('about.html: 修复?')

# 2. 修改 events.html 活动内容
with open('events.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 万峰林活动 -> 3月14日清水河孩子野炊
c = c.replace('万峰林活动', '清水河孩子野炊')
c = c.replace('40位单身青年在万峰林踏青徒步，在大自然中放松交流。', '3月14日，组织亲子野炊活动，家长和孩子们在清水河畔度过愉快的周末。')

# 红娘培训活动 -> 5月6日
c = c.replace('红娘培训活动', '红娘培训')
c = c.replace('红娘团队专业培训，提升服务品质，更好地服务会员。', '5月6日，红娘团队参加专业婚恋服务培训，提升服务品质。')

# 单身沙龙活动 -> 4月25日招商会
c = c.replace('单身沙龙活动', '招商会')
c = c.replace('主题交友沙龙，以兴趣为媒，让相遇自然发生。', '4月25日，举办招商合作交流会，诚邀合作伙伴共谋发展。')

with open('events.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('events.html: 更新活动内容')

# 3. 验证
print('\n=== 验证 ===')
with open('about.html', 'r', encoding='utf-8') as f:
    c = f.read()
print('about.html 还有?:', '?' in c)

with open('events.html', 'r', encoding='utf-8') as f:
    c = f.read()
print('events.html 万峰林:', '万峰林' in c)
print('events.html 清水河:', '清水河' in c)
print('events.html 红娘培训:', '红娘培训' in c)
print('events.html 5月6日:', '5月6日' in c)
print('events.html 招商会:', '招商会' in c)
print('events.html 4月25日:', '4月25日' in c)
