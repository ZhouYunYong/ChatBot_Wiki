# -*- coding: utf-8 -*-


from gtts import gTTS
from pygame import mixer

tts = gTTS(text='新年快樂', lang='zh-tw')

tts.save('happy.mp3')

tts.save()



