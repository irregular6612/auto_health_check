
#import modules
import requests, json

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

    sess.get(sendMessage, params = {"chat_id": chat_id, "text":"자습신청했습니다."})
    #sess.get(getUpdates, params = {'offset': update_id + 1 })
