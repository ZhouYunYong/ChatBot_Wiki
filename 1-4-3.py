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

chatBot_Speak('我是萱萱', 'zh-tw')	# 呼叫 chatBot_Speak() 函式
