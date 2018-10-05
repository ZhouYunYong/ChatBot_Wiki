#  1-2-2  機器人的耳朵函式
import speech_recognition as sr

def chatBot_Listen():
    recong = sr.Recognizer()                                                    # 建立辨識物件
    with sr.Microphone() as source:                                             # 打開麥克風取得聲音
        audioData = recong.listen(source)                                       # 讓辨識物件聽到的聲音
    try:
        text = recong.recognize_google(audioData, language='zh-tw')             # 將聲音資料翻成文字
        return text
    except:
        return '聽不懂'

# 1-4-3 機器人的說話函式

from gtts import gTTS
from pygame import mixer
import tempfile

mixer.init()   # 初始化 mixer 物件
def chatBot_Speak(text, lang):
	try:
		with tempfile.NamedTemporaryFile() as ntf:    
			tts = gTTS(text=text, lang=lang)
			tts.save(f'{ntf.name}.mp3')
			mixer.music.load(f'{ntf.name}.mp3')
			mixer.music.play()
			while(mixer.music.get_busy()):
				pass
	except:
		print('播放音效失敗')

# 	1-6-3  抓取維基百科愛因斯坦網頁內的文章第一段

from bs4 import BeautifulSoup
import requests

def chatBot_GET_Wiki(keyword):
    response = requests.get('https://zh.wikipedia.org/zh-tw/' + keyword)
    bs = BeautifulSoup(response.text, 'lxml')
    p_list = bs.find_all('p')
    for p in p_list:
        if keyword in p.text[0:10]:
            return p.text

# 1-7-3 唸出常規表達式處理後的字串
import re

def chatBot_Speak_Re(sentence):
	s1 = re.sub(r'\[[^\]]*\]', '', sentence)
	print(s1)
	en_list = re.findall(r'[a-zA-Z ]+',s1)
	s2 = re.sub(r'[a-zA-Z \-]+', '@English@', s1)
	all_list = s2.split('@')
	index = 0
	for text in all_list:
		if text != 'English':    
			chatBot_Speak(text, 'zh-tw')
		else:
			chatBot_Speak(en_list[index], 'en')
			index += 1

# 1-8-3 對 Google 搜尋結果進行網路爬蟲
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





