from gtts import gTTS

tts = gTTS(text = '生日快樂', lang = 'zh-tw')

tts.save('D://生日快樂.mp3')