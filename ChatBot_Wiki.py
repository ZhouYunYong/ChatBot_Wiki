# -*- coding: utf8 -*-
# STT 語音轉文字
# 安裝套件 : pip install SpeechRecognition
# 執行後會有問題，還需安裝 PyAudio
import speech_recognition
import sys
from hanziconv import HanziConv

question = ''
answer = ''
QA = {'你好嗎': '我很好', '你是誰': '我是小美'}
stt_language = 'zh-tw'
wikiWord = '灌籃高手'

google_request = 'https://www.google.com.tw/search?q='
relaWord = '+維基百科'


def compareSim(word1, word2):
    counter = 0
    for i, j in zip(word1, word2):
        if i == j:
            counter += 1
    try:    
        return counter / len(word1)
    except:
        return 0

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
            while(mixer.music.get_busy()):
                pass
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


pat_English = re.compile('[a-zA-Z ]+')   # 英文的正則表達式

#match_English = pat_English.findall(ori)
#
#ori_Chinese = re.sub(pat_English, 'XXX', ori)
#
#ori_Chinese
#
#match_English

#print(match_English)

question = stt()
print(question)
search_url = google_request + question + relaWord
response = requests.get(search_url)
if response.status_code == 200:                             # google 搜尋成功
    bs = BeautifulSoup(response.text, 'html.parser')        # 搜尋頁面內容轉為文字, 再用 BS4 轉成可解析物件
    wiki_url = bs.find('cite')                              # 找出存放網址的 <cite>  (要第一個)
    print(wiki_url.text)                                    # wiki 網址
    response = requests.get(wiki_url.text)                  # 前往關鍵字維基百科網站
    wikiWord = wiki_url.text.split('/')[-1]
    print(wikiWord)
    wikiWord_simp = HanziConv.toSimplified(wikiWord)        # 轉簡體
    wikiWord_trad = HanziConv.toTraditional(wikiWord)       # 轉繁體
    if response.status_code == 200:                         # 前往維基百科成功
#        print(response.text)                               # 發出請求取得網頁文字內容
        bs = BeautifulSoup(response.text, 'html.parser')    # 用 BeautifulSoup 解析原始內容
        content = bs.select('.mw-parser-output p')          # 回傳 list
        
        for i in range(len(content)):                       # 在 list 中尋找 wikiWord 開頭的段落
            firstWord = content[i].text[0 : len(wikiWord)]  # 文章前關鍵字 
            firstWord_2 = content[i].text[1 : len(wikiWord)+1]  # 文章前 <關鍵字>
            simVal1 = compareSim(firstWord, wikiWord_simp)  # 改以相似性比較, 因為例如人工智慧會變成人工智能
            simVal2 = compareSim(firstWord, wikiWord_trad)
            simVal3 = compareSim(firstWord_2, wikiWord_simp)
            simVal4 = compareSim(firstWord_2, wikiWord_trad)
            
            
                        
            
            if simVal1 >= 0.5 or simVal2 >= 0.5 or simVal3 >= 0.5 or simVal4 >= 0.5:
    #            print(content[i].text)
                re_text = re.sub(r'\[[0-9+]\]', '', content[i].text)   # 去除 [1] [2]...
                print(re_text)
                
                
                match_English = pat_English.findall(re_text)  # 找出句子中所有英文
                
                print(match_English)
                
                text_onlyChinese = re.sub(pat_English, 'XXX', re_text)
                
                text_onlyChinese_mark = re.sub(pat_English, '#XXX#', re_text)
                
                finalList = text_onlyChinese_mark.split('#')
                
                index = 0
                for sentance in finalList:
                    if sentance != 'XXX':
                        speak(sentance, 'zh-tw')
                    else:
                        speak(match_English[index], 'en')
                        index += 1
                
                
                
                
#                speak(content[i].text, 'zh-tw')
                break
        
    #    speak(content, 'zh-tw')
    else:
        print("查無資料")
        
mixer.music.stop()


    
    
    
    
    





