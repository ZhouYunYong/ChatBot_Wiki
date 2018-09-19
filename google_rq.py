import requests
from bs4 import BeautifulSoup


google_request = 'https://www.google.com.tw/search?q='


response = requests.get(google_request + '台灣在哪裡+維基')

#print(response.text)

if response.status_code == 200:
    bs = BeautifulSoup(response.text, 'html.parser')   # 將回傳內容轉為文字, 再用 BS4 轉成可解析物件
#    t = bs.find_all("a")
#    
#    
#    for a in t:
#        if "皮卡丘" in a.text:
#            print(a)
#            print("------")
#    
#    content = bs.select('.bkWMgd h3') # 解析出 class 為 rc 中的 <a>, 回傳 list 結果
    content = bs.find('cite')
    print(content.text)
#    for s in content:
#        print(s.text)
    
#    print(content)


