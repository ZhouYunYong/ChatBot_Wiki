# -*- coding: utf8 -*-
# STT 語音轉文字
# 安裝套件 : pip install SpeechRecognition
# 執行後會有問題，還需安裝 PyAudio
# 安裝套件 pip install gTTS 文字轉語音
# 安裝套件 pip install pygame 播放音檔
# 套件 tempfile , 為了要使用暫存檔
from gtts import gTTS 
from pygame import mixer
import tempfile   
import speech_recognition
from hanziconv import HanziConv
import requests 
from bs4 import BeautifulSoup 
import re

question = ''
answer = ''
QA = {'你好嗎': '我很好', '你是誰': '我是小美', '哈囉': '你好', '你可以幫助我什麼': '我可以回答妳很多問題'}               # 使用者自訂的 QA 字典
stt_language = 'zh-tw'                                      # 語音轉文字的語言
google_request = 'https://www.google.com.tw/search?q='      # google 搜尋的請求路徑
relaWord = '+維基百科'          # question 中 加上 維基百科在一起 gooogle 搜尋, 把維基百科的網站強制擺到第一個搜尋結果
mixer.init()                    # 初始化播放物件

# 比較兩個字的相似性
def compareSim(word1, word2):
    counter = 0
    for i, j in zip(word1, word2):
        if i == j:
            counter += 1
    try:    
        return counter / len(word1)
    except:
        return 0

#speeech to text 語音轉文字
def stt():
    global question, answer
    try:
        recong = speech_recognition.Recognizer()                                # 建立辨識物件
        with speech_recognition.Microphone() as voice:                          # 打開麥克風取得聲音
            audio = recong.listen(voice)                                        # 讓辨識物件聽到的聲音
        question = recong.recognize_google(audio, language=stt_language)        # 將聲音資料翻成文字
#        print(question)
        if question in QA.keys():
           answer = QA[question] 
        else:
            answer = '我不知道你說什麼'
    except:
#        print('error:# 聲音中找不到可翻譯的內容')                 # 聲音中找不到可翻譯的內容
        pass
    return question

# 執行說話(要說的文字, 要說的語言)
def speak(t, lang):
    try:
        with tempfile.NamedTemporaryFile(delete=True) as ntf:    # 打開暫存檔
            tts = gTTS(text=t, lang=lang)                       # 要用 zh-tw 不能用 zh
            tts.save(f"{ntf.name}.mp3")                          # 存成暫存檔
            mixer.music.load(f"{ntf.name}.mp3")                  # 讀取音檔
            mixer.music.play()                                  # 播放音檔
            while(mixer.music.get_busy()):
                pass
    except:
#        print("error: 文字無法以語音說出")                       # 有些符號無法以語音說出
        pass
    




    
question = stt()                                                # 等待語音輸入, 問一句話

if question in QA.keys():
    speak(QA[question], 'zh-tw')
    print(QA[question])

else:
    
    print(question)
    #-----Google 搜尋階段-----#
    search_url = google_request + question + relaWord               # 建構 google 請求路徑 (base+問題+維基百科)
    response = requests.get(search_url)                             # 執行 GET 請求
    if response.status_code == 200:                                 # 請求成功返回 200 HTTP 狀態碼
        bs = BeautifulSoup(response.text, 'html.parser')            # 將搜尋頁面內容轉為文字, 再用 BS4 轉成可解析物件
        wiki_url = bs.find('cite')                                  # 找出存放網址的 <cite>  (我們要第一個)
        print(wiki_url.text)                                        # wiki 網址
        #-----維基百科階段-----#
        wikiWord = wiki_url.text.split('/')[-1]                     # 切出網址後面的關鍵字 -> /關鍵字
        print(wikiWord)
        wikiWord_simp = HanziConv.toSimplified(wikiWord)            # 關鍵字轉簡體 (因為有時維基百科內文以簡體紀錄或者得到的網址以簡體表示)
        wikiWord_trad = HanziConv.toTraditional(wikiWord)           # 關鍵字轉繁體 (因為有時維基百科內文以繁體紀錄或者得到的網址以繁體表示)
        response = requests.get(wiki_url.text)                      # GET 取得維基百科
        if response.status_code == 200:                             # 前往維基百科成功
    
            bs = BeautifulSoup(response.text, 'lxml')        # 用 BeautifulSoup 解析原始內容
            content = bs.select('.mw-parser-output p')              # 找到 class = 'mw-parser-output' 下的 <p>, 回傳 list  結果
            
            for i in range(len(content)):                           # 在 list 結果中一個一個尋找有 關鍵字 開頭的段落
                firstWord = content[i].text[0 : len(wikiWord)]      # 取得文章開頭的文字 (以關鍵字為長度)
                firstWord_2 = content[i].text[1 : len(wikiWord)+1]  # 文章前 <關鍵字>
                simVal1 = compareSim(firstWord, wikiWord_simp)      # 對比文章開頭與關鍵字的相似性, 因為例如人工智慧會變成人工智能
                simVal2 = compareSim(firstWord, wikiWord_trad)
                simVal3 = compareSim(firstWord_2, wikiWord_simp)
                simVal4 = compareSim(firstWord_2, wikiWord_trad)
                
                
                if simVal1 >= 0.5 or simVal2 >= 0.5 or simVal3 >= 0.5 or simVal4 >= 0.5:    # 若相似性超過 50 %
                    
                    
                    
                    re_text = re.sub(r'[\[][0-9a-zA-Z]+[\]]', '', content[i].text)              # 去除 [1] [2]...
                    
                    print(re_text)
                    
                    pat_English = re.compile('[a-zA-Z \-]+')                                # 英文的正則表達式
                    match_English = pat_English.findall(re_text)                            # 找出句子中所有英文
                    print(match_English)
                    text_onlyChinese_mark = re.sub(pat_English, '#XXX#', re_text)           # 將英文用 #XXX# 取代
                    finalList = text_onlyChinese_mark.split('#')                            # 將文章以 # 切分片段
                                                            
#                    rmNum_Text = rmNum(content[i].text)             
                    
#                    get
                                                            
                    
                    index = 0                                                               # 紀錄英文出現的次數, 才可以搭配索引取出對應的英文字
                    for sentance in finalList:                                              # 切出來的文字片段一個一個唸出來
                        if sentance != 'XXX':                                               # 如果遇到 XXX 唸英文, 其他就念中文
                            speak(sentance, 'zh-tw')
                        else:
                            speak(match_English[index], 'en')
                            index += 1
                    break
    
            if not (simVal1 >= 0.5 or simVal2 >= 0.5 or simVal3 >= 0.5 or simVal4 >= 0.5) : speak('我也不知道', 'zh-tw')  # 全部搜尋完皆無 超過 50 % 的相似性開頭
    
        else:
            print('前往維基百科失敗')
    #        speak('前往維基百科失敗', 'zh-tw')
    else:
        print('Google 搜尋失敗')
    #    speak('Google 搜尋失敗', 'zh-tw')
        

    mixer.music.stop()
    
    
    
    
    
    





