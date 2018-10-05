from gtts import gTTS
from pygame import mixer
import tempfile
import re

def chatBot_Speak(t, lang):
   try:
       with tempfile.NamedTemporaryFile(delete=True) as ntf:    
           tts = gTTS(text=t, lang=lang)			# 要用 zh-tw 不能用 zh
           tts.save(f"{ntf.name}.mp3")			# 存成暫存檔
           mixer.music.load(f"{ntf.name}.mp3")	# 讀取音檔
           mixer.music.play()					# 播放音檔
           while(mixer.music.get_busy()):		
               pass
   except:
       print('播放音效失敗')


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

mixer.init()
sentence = 	'阿爾伯特·愛因斯坦，或譯亞伯特·愛因斯坦（德語：Albert Einstein，1879年3月14日－1955年4月18日），猶太裔理論物理學家，創立了現代物理學的兩大支柱之一的相對論[註 2][2]:274[1]，也是質能等價公式（E = mc2）的發現者[3]。'
chatBot_Speak_Re(sentence)




