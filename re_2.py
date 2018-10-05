from gtts import gTTS
from pygame import mixer
import re
import tempfile  

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
        print('播放音效失敗')


def speak_re(sentence):
    
#    t1 = re.sub(r'\[.+?\]', '', content)           # 去除 [1] [2]...
    s1 = re.sub(r'\[[^\]]*\]', '', sentence)                      # 去除 [1] [2]...   
    print(s1)
    en_list = re.findall(r'[a-zA-Z ]+',s1)                     # 找出句子中所有英文
    s2 = re.sub(r'[a-zA-Z \-]+', '@English@', s1)           # 將英文用 #Englist# 取代
    all_list = s2.split('@')                            # 將文章以 # 切割
    
    index = 0                                                               # 紀錄英文出現的次數, 才可以搭配索引取出對應的英文字
    for text in all_list:                                              # 切出來的文字片段一個一個唸出來
        if text != 'English':                       # 如果遇到 XXX 唸英文, 其他就念中文
            speak(text, 'zh-tw')
        else:
            speak(en_list[index], 'en')
            index += 1


mixer.init()
sentence = '阿爾伯特·愛因斯坦，或譯亞伯特·愛因斯坦（德語：Albert Einstein，1879年3月14日－1955年4月18日），猶太裔理論物理學家，創立了現代物理學的兩大支柱之一的相對論[註 2][2]:274[1]，也是質能等價公式（E = mc2）的發現者[3]。他在科學哲學領域頗具影響力[4][5]。'

speak_re(sentence)




