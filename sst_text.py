import speech_recognition

recog = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
	audio = recog.listen(source) # 使用 listen() 方法將聲源存起來
    

try:
    question = recog.recognize_google(audio, language = 'zh-tw')       
except:
    print("聽不懂...")

print(question) 






