# STT 語音轉文字
# 安裝套件 : pip install SpeechRecognition
# 執行後會有問題，還需安裝 PyAudio
import speech_recognition
import sys

question = ''
answer = ''
QA = {'你好嗎': '我很好', '你是誰': '我是小美'}
stt_language = 'zh-tw'
wikiWord = '灌籃高手'
# 特定名字與標題 《櫻桃小丸子》 《灌籃高手》 《道路交通法》 會有問題

def stt():
    global question, answer
    try:
        recong = speech_recognition.Recognizer()                        # 建立辨識物件
        with speech_recognition.Microphone(chunk_size = 2048) as voice: # 打開麥克風取得聲音
            audio = recong.listen(voice)                                # 讓辨識物件聽到的聲音
        question = recong.recognize_google(audio, language=stt_language)     # 將聲音資料翻成文字
#        print(question)
        if question in QA.keys():
           answer = QA[question] 
        else:
            answer = '我不知道你說什麼'
    except:
        print('Unexpected error:', sys.exc_info()[0])                   # 聲音中找不到可翻譯的內容
    return question


# TTS 文字轉語音
# 安裝套件 pip install gTTS 文字轉語音
# 安裝套件 pip install pygame 播放音檔
from gtts import gTTS
from pygame import mixer
import tempfile

mixer.init()                                                # 建立 mixer 物件並初始化

def speak(t, lang):
    try:
        with tempfile.NamedTemporaryFile(delete=True) as tf:    # 打開暫存檔
            tts = gTTS(text=t, lang=lang)                    # 要用 zh-tw 不能用 zh
            tts.save("{}.mp3".format(tf.name))                  # 存成暫存檔
            mixer.music.load("{}.mp3".format(tf.name))          # 讀取音檔
            mixer.music.play()                                  # 播放音檔
    except:
        print("Unexpected error:", sys.exc_info()[0])           # 無文字可以說
        
        
 

if __name__ == '__main__':   
#    print(stt())
#    speak(answer, 'zh-tw')
    pass


# Wiki 爬蟲 

import requests 
from bs4 import BeautifulSoup 
import re

wikiWord = stt()
print(wikiWord)
response = requests.get('https://zh.wikipedia.org/wiki/{}'.format(wikiWord))

if response.status_code == 200:
#    print(response.text)                                       # 發出請求取得網頁文字內容
    bs = BeautifulSoup(response.text, 'html.parser')            # 用 BeautifulSoup 解析原始內容
    content = bs.select('.mw-parser-output p')                  # 回傳 list

    for i in range(len(content)):                               # 在 list 中尋找 wikiWord 開頭的段落
        if content[i].text[0 : len(wikiWord)] == wikiWord or content[i].text[1 : len(wikiWord)+1] == wikiWord :
#            print(content[i].text)
            re_text = re.sub(r'\[[0-9+]\]', '', content[i].text)
            print(re_text)
            speak(content[i].text, 'zh-tw')
            break
    
#    speak(content, 'zh-tw')
else:
    print("查無資料")
        



#mixer.music.stop()
    
    

    
    
    
    
    





