# -*- coding: utf-8 -*-

from datetime import datetime
from gtts import gTTS
from pygame import mixer
import tempfile   
import os
mixer.init()                        # 初始化播放物件

type(gTTS)

tts = gTTS(text='新年快樂', lang='zh-tw')

type(gTTS)
type(tts)


type(tts)

#?gTTS

tts.save('新年快樂.mp3')


mixer.music.load('生日快樂.mp3')                    # 讀取音檔
mixer.music.play()                                  # 播放音檔


#from pygame import mixer
#import tempfile
#mixer.init()                        # 初始化播放物件




# 執行說話(要說的文字, 要說的語言)
def speak1(text, lang):
    try:
        with tempfile.NamedTemporaryFile() as tf:    # 打開暫存檔
            tts = gTTS(text=text, lang=lang)                    # 要用 zh-tw 不能用 zh
            tts.save(f'{tf.name}.mp3')                          # 存成暫存檔
            print(f'{tf.name}')
            mixer.music.load(f'{tf.name}.mp3')                  # 讀取音檔
            mixer.music.play()                                  # 播放音檔
#            while(mixer.music.get_busy()):
#                pass
    except:
        print('發生錯誤: 無法以語音說出')                       # 空白或無內容無法以語音說出
    

#speak('', 'en')


speak1('測試', 'zh-tw')
# C:\Users\Admin\AppData\Local\Temp


def speak2(text, lang):
    try:
        
        tts = gTTS(text=text, lang=lang)                    # 要用 zh-tw 不能用 zh
        now = datetime.now()
        timeStamp = int(now.timestamp() * 1000000)
        tts.save('temp\{}.mp3'.format(timeStamp))                  # 存成暫存檔
        mixer.music.load('temp\{}.mp3'.format(timeStamp))          # 讀取音檔
        mixer.music.play()                                  # 播放音檔
        while(mixer.music.get_busy()):
            pass
    except:
        print('發生錯誤: 無法以語音說出')                       # 空白或無內容無法以語音說出
   
    


#t = datetime.now().timestamp()
#print(type(datetime))





#speak2('測試2', 'zh-tw')
#print(datetime.now().timestamp() - t)
#
#
#
#
#t = datetime.now().timestamp()
#speak1('測試', 'zh-tw')
#print(datetime.now().timestamp() - t)




        
#tts = gTTS(text='測試', lang='zh-tw')                    # 要用 zh-tw 不能用 zh
#tts.save('測試.mp3')                  # 存成暫存檔
#mixer.music.load('測試.mp3')          # 讀取音檔
#mixer.music.play()                                  # 播放音檔      
#os.remove('C:\\Users\\Admin\\AppData\\Local\\Temp\\tmpr6gz01xj.mp3')
#os.remove('測試.mp3')


#mixer.music.load('test1.mp3')
#mixer.music.play()


#mixer.music.stop()

        
        
        
        
        
        
        



