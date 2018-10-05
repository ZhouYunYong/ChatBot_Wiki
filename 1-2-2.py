import speech_recognition as sr

#speeech to text 語音轉文字



def chatBot_Listen():
    recong = sr.Recognizer()                                # 建立辨識物件
    with sr.Microphone() as source:                         # 打開麥克風取得聲音
        audioData = recong.listen(source)                                        # 讓辨識物件聽到的聲音
    try:
        text = recong.recognize_google(audioData, language='zh-tw')        # 將聲音資料翻成文字
        return text
    except:
        return '聽不懂'

question = chatBot_Listen()
print(question)








