# -*- coding: utf8 -*-
import re

patten = re.compile('[\u0800-\u4e00]+')   # 日文的正則表達式

s1 = "今天天氣不錯喔今日の天気は良いです哈哈哈哈哈私はあなたが好きです哈哈哈哈哈"
s = '今日の天気は良いです'
s_s = 'は'
match = patten.findall(s1)

print(match)



# 看看 unicode

str3 = u'0800'
print(str3)


sss = s_s.encode('utf-8')  # .py 儲存為 uft-8
print(sss)

re_s = sss.decode('utf-8')  # 還原

print(re_s)

# python 3 每個字串都是 Unicode

word = u'0800'
print(word)

word_big5 = word.encode('big5')
print(word_big5)

word_uft8 = word.encode('utf-8')
print(word_uft8)


