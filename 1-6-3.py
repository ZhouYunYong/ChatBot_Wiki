from bs4 import BeautifulSoup
import requests

def chatBot_GET_Wiki(keyword):
    response = requests.get('https://zh.wikipedia.org/zh-tw/' + keyword)
    bs = BeautifulSoup(response.text, 'lxml')
    p_list = bs.find_all('p')
    for p in p_list:
        if keyword in p.text[0:10]:
            return p.text
        
content = chatBot_GET_Wiki('愛因斯坦')

print(content)






