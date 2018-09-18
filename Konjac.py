import ChatBot_Wiki

# 安裝套件 pip install googletrans
from googletrans import Translator

trans_lang = 'ja'   # zh-tw, ja

translator = Translator() # 建立翻譯物件

#result = translator.translate('你好嗎', dest='en').text
#print(result)

speech = ChatBot_Wiki.stt()
print(speech)
result = translator.translate(speech, dest=trans_lang).text
print(result)
ChatBot_Wiki.speak(result, trans_lang)   

