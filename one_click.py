import requests, json, time
import datetime

def selfstudy(command,name,period):
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month) if datetime.datetime.now().month > 9 else str(0)+str(datetime.datetime.now().month) 
    date = str(datetime.datetime.now().day) if datetime.datetime.now().day > 9 else  str(0)+str(datetime.datetime.now().day)
    now = year + month + date

    login = 'http://academic.petapop.com/sign/actionLogin.do'
    period = 1
    reserv = 'http://academic.petapop.com/self/requestSelfLrn.do?sgnId={}&lrnPd={}'.format(now,period)
    delet = 'http://academic.petapop.com/self/deleteSelfLrn.do'

    User = {
        '박주현': { 'id' : 'jacop0125', 'password':'12345678'}    
    }

    Tch = {
        '이상명' : 'USRCNFRM_00000000174',
        '임혜섭' : 'USRCNFRM_00000000185',
        '최승재': 'USRCNFRM_00000000013'

    }
    
    Cls = {
        '3-3교실' : "CLSSRM_0000000000007",
        '수창실' : 'CLSSRM_0000000000033',
        '코딩랩' : 'CLSSRM_0000000000075'
    }

    formdata = {
        'clssrmId': 'CLSSRM_0000000000007',     # 3-3교실
        'roomTcherId': 'USRCNFRM_00000000174',      #이상명 쌤  담임교사
        'cchTcherId': 'USRCNFRM_00000000174'            #지도교사
    }

    if '신청' in command:
        with requests.Session() as sess:    
            response = sess.post(login, data = User[name])
            resposne2 = sess.post(reserv,data=formdata)
            cook = json.loads(resposne2.text)["slrnNo"]
            print(cook)
    

    if '취소' in command:
        with requests.Session() as sess:    
            response = sess.post(login, data = User[name])
            resposne2 = sess.post(reserv,data=formdata)
            cook = json.loads(resposne2.text)["slrnNo"]
    
            deld = {
                "slrnNo": cook 
            }
            print('now')
            time.sleep(10)
            response3 = sess.post(delet,data=deld)

selfstudy("신청","박주현","1")     # command, name, period


#import modules

#telegram api token
TOKEN = '1310687288:AAG0Yu1ITm_foSifcJeiL8oDfZOfYML7hP0'

#Url
getUpdates = 'https://api.telegram.org/bot{}/getUpdates'.format(TOKEN)
sendMessage = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN)

# sendMessage or check updates 
with requests.Session() as sess:
    response = json.loads(sess.get(getUpdates).text)
    print(response)

    update_id = response["result"][-1]["update_id"]         # check update id
    chat_id = response["result"][-1]["message"]["from"]["id"]       # check chat id
    msg = response["result"][-1]["message"]["text"]         #check last chats
    print(type(chat_id))

    if msg == '자습신청해줘':
        selfstudy("신청","박주현","1")     # command, name, period
        sess.get(sendMessage, params = {"chat_id": chat_id, "text":"자습신청했습니다."})
        #sess.get(getUpdates, params = {'offset': update_id + 1 })