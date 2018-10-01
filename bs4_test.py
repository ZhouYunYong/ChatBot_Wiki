from bs4 import BeautifulSoup
import requests
from gtts import gTTS
from pygame import mixer


def speak(text, lang):
    try:
        with tempfile.NamedTemporaryFile() as tf:    # 打開暫存檔
            tts = gTTS(text=text, lang=lang)                    # 要用 zh-tw 不能用 zh
            tts.save(f'{tf.name}.mp3')                          # 存成暫存檔
            print(f'{tf.name}')
            mixer.music.load(f'{tf.name}.mp3')                  # 讀取音檔
            mixer.music.play()                                  # 播放音檔
            while(mixer.music.get_busy()):
                pass
    except:
        print('發生錯誤: 無法以語音說出')                       # 空白或無內容無法以語音說出


mixer.init()
keyWord = '愛因斯坦'
response = requests.get('https://zh.wikipedia.org/zh-tw/' + keyWord)
bs = BeautifulSoup(response.text, 'lxml')
p_list = bs.find_all('p')
for p in p_list:
    if keyWord in p.text[0:10]:
        print(p.text)
        speak(p.text, 'zh-tw')
        break




