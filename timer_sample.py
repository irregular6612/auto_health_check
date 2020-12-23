import datetime, time

while True:  
    now = datetime.datetime.now()    
    if now.hour == 20 and now.minute == 51:
        print(now)
        print('now')
        break
    else:
        print(now)
        print('no')
        time.sleep(10)
    
