import datetime, time
from selenium import webdriver

TOKEN = '1310687288:AAG0Yu1ITm_foSifcJeiL8oDfZOfYML7hP0'

data = {
    '1':{'name': '박주현', 'birth':'020125', 'pw':'0125'},
    '2':{'name': '이상웅', 'birth':'020215', 'pw':'1234'},
    '3':{'name': '최성훈', 'birth':'020405', 'pw':'1234'},
    '4':{'name': '이시아', 'birth':'021119', 'pw':'1234'}
}

def autotest(name,birth,pw):

    #driver = webdriver.PhantomJS('phantomjs-2.1.1-windows/bin/phantomjs.exe')
    driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
    Url = 'https://hcs.eduro.go.kr/'

    # login
    driver.get(Url)
    driver.find_element_by_xpath('//*[@id="btnConfirm2"]').click()
    driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[2]/td/input').click()
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[1]/td/select/option[12]').click()
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[2]/td/select/option[5]').click()
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[1]/input').send_keys('충북과학고')
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/p').click()
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()

    driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[3]/td/input').send_keys(name)
    driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[4]/td/input').send_keys(birth)
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr/td/input').send_keys(pw)
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
    time.sleep(2)

    # test 
    driver.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul/li[1]/a/span[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[2]/dl[1]/dd/ul/li[1]/label').click()
    driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[2]/dl[2]/dd/ul/li[1]/label').click()
    driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[2]/dl[3]/dd/ul/li[1]/label').click()
    driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[2]/dl[4]/dd/ul/li[1]/label').click()
    driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[2]/dl[5]/dd/ul/li[1]/label').click()
    driver.find_element_by_id("btnConfirm").click()
    time.sleep(1)
    name = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[1]/p[1]/span').text
    success = driver.find_element_by_xpath('//*[@id="container"]/div/div/div[1]/p[2]').text 
    print(name, success)

    driver.quit()

# timer
while True:  
    now = datetime.datetime.now()    
    if now.hour == 8 and now.minute == 9:             # set time which you want (rec : 07:12)
        try: 
            print('Current Time: ', now)
            for i in range(1,5):
                print(datetime.datetime.now())
                autotest(str(data[str(i)]['name']),str(data[str(i)]['birth']),str(data[str(i)]['pw']))
            break
        except:
            time.sleep(200)
            print('Current Time: ', now)
            for i in range(1,5):
                print(datetime.datetime.now())
                autotest(str(data[str(i)]['name']),str(data[str(i)]['birth']),str(data[str(i)]['pw']))
            break
    else:
        print("WAIT ! Don't turn off this program! ",now )
        time.sleep(30)
    
