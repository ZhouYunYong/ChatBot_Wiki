import speech_recognition as sp

recog = sp.Recognizer()
with sp.Microphone() as source:
    audioData = recog.listen(source) # 使用 listen() 方法將聲源存起來
try:
    question = recog.recognize_google(audioData, language = 'zh-tw')   
    print(question)     
except:
    print("聽不懂...")








