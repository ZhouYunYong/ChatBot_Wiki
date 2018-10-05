import requests
from bs4 import BeautifulSoup
from hanziconv import HanziConv


def chatBot_GET_Google(question):
    url = 'https://www.google.com.tw/search?q=' + question + '+維基百科'
    response = requests.get(url)
    if response.status_code == 200:    
        bs = BeautifulSoup(response.text, 'lxml')
        wiki_url = bs.find('cite')
        kwd = wiki_url.text.split('/')[-1]
        keyword_trad = HanziConv.toTraditional(kwd)
        return keyword_trad
    else:
        print('請求失敗')

keyword = chatBot_GET_Google('誰是愛因斯坦')
print(keyword)