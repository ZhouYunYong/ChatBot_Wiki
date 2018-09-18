# STT 語音轉文字
# 安裝套件 : pip install SpeechRecognition
# 執行後會有問題，還需安裝 PyAudio
import speech_recognition
import sys

question = ''
answer = ''
QA = {'你好嗎': '我很好', '你是誰': '我是小美'}

def stt():
    global question, answer
    try:
        recong = speech_recognition.Recognizer()                        # 建立辨識物件
        with speech_recognition.Microphone(chunk_size = 2048) as voice: # 打開麥克風取得聲音
            audio = recong.listen(voice)                                # 讓辨識物件聽到的聲音
        question = recong.recognize_google(audio, language='zh-TW')     # 將聲音資料翻成文字
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
        
if '__name__' == 'main':   
    stt()
    speak(answer, 'zh-tw')

# 翻譯蒟蒻

# Wiki 爬蟲 







