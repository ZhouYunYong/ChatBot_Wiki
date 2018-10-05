from chatBot_modules import *

question = ''
answer = ''
QA = {'你是誰' : '我是萱萱', '聽不懂' : '請再說一次問題'}

question = chatBot_Listen()         # 打開耳朵聽問題
print(question)
if question in QA.keys():           # 如果問題存於 QA 字典中
    answer = QA[question]
    chatBot_Speak(answer, 'zh-tw')
    print(answer)
else:                               # 問題不存於 QA 字典中, 進行網路爬蟲
    keyword = chatBot_GET_Google(question)
    content = chatBot_GET_Wiki(keyword)
    if content != None:  
        chatBot_Speak_Re(content)
    else:
        print('找不到相關的維基百科資料')




