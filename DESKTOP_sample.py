import datetime
import time
import requests
import json
from selenium import webdriver

TOKEN = '1310687288:AAG0Yu1ITm_foSifcJeiL8oDfZOfYML7hP0'

data = {
    '1': {'name': '박주현', 'birth': '020125', 'pw': '0125'},
    '2': {'name': '이상웅', 'birth': '020215', 'pw': '1234'},
    '3': {'name': '최성훈', 'birth': '020405', 'pw': '1234'},
    '4': {'name': '이시아', 'birth': '021119', 'pw': '1234'},
    '5': {'name': '정원희', 'birth': '021021', 'pw': '7653'},
    '6': {'name': '박태민', 'birth': '021214', 'pw': '1214'},
    '7': {'name': '조성운', 'birth': '020713', 'pw': '3309'},
    '8': {'name': '신윤수', 'birth': '020322', 'pw': '1234'},

}


def autotest(name, birth, pw):

    #driver = webdriver.PhantomJS('phantomjs-2.1.1-windows/bin/phantomjs.exe')
    driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
    Url = 'https://hcs.eduro.go.kr/'

    # login
    driver.get(Url)
    driver.find_element_by_xpath('//*[@id="btnConfirm2"]').click()
    driver.find_element_by_xpath(
        '//*[@id="WriteInfoForm"]/table/tbody/tr[2]/td/input').click()
    driver.find_element_by_css_selector(
        '#WriteInfoForm > table > tbody > tr:nth-child(1) > td > button').click()
    driver.find_element_by_xpath(
        '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[1]/td/select/option[12]').click()
    driver.find_element_by_xpath(
        '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[2]/td/select/option[5]').click()
    driver.find_element_by_xpath(
        '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[1]/input').send_keys('충북과학고\n')
    time.sleep(0.5)
    driver.find_element_by_xpath(
        '//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a/p/a').click()
    driver.find_element_by_xpath(
        '//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()
    # driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()

    time.sleep(0.5)
    # driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/p').click()
    # driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()

    driver.find_element_by_xpath('//*[@id="user_name_input"]').send_keys(name)
    driver.find_element_by_xpath('//*[@id="birthday_input"]').send_keys(birth)
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
    time.sleep(0.5)
    driver.find_element_by_xpath(
        '//*[@id="WriteInfoForm"]/table/tbody/tr/td/input').send_keys(pw)
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
    time.sleep(2)

    # test
    driver.find_element_by_xpath(
        '//*[@id="container"]/div/section[2]/div[2]/ul/li[1]/a/span[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="container"]/div/div/div[2]/div[2]/dl[1]/dd/ul/li[1]/label').click()
    driver.find_element_by_xpath(
        '//*[@id="container"]/div/div/div[2]/div[2]/dl[2]/dd/ul/li[1]/label').click()
    driver.find_element_by_xpath(
        '//*[@id="container"]/div/div/div[2]/div[2]/dl[3]/dd/ul/li[1]/label').click()
    # driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[2]/dl[4]/dd/ul/li[1]/label').click()
    # driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[2]/dl[5]/dd/ul/li[1]/label').click()
    driver.find_element_by_id("btnConfirm").click()
    time.sleep(1)
    name = driver.find_element_by_xpath(
        '//*[@id="container"]/div/div/div[1]/p[1]/span').text
    success = driver.find_element_by_xpath(
        '//*[@id="container"]/div/div/div[1]/p[2]').text
    time.sleep(0.5)
    telegramtalk(name, success)

    driver.quit()


def telegramtalk(name, success):
    getUpdates = 'https://api.telegram.org/bot{}/getUpdates'.format(TOKEN)
    sendMessage = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN)

    # sendMessage or check updates
    with requests.Session() as sess:
        response = json.loads(sess.get(getUpdates).text)
        print(response)

        # update_id = response["result"][-1]["update_id"]         # check update id
        # check chat id
        chat_id = response["result"][-1]["message"]["from"]["id"]
        msg = response["result"][-1]["message"]["text"]  # check last chats

        sess.get(sendMessage, params={
                 "chat_id": chat_id, "text": name + " " + success})
        #sess.get(getUpdates, params = {'offset': update_id + 1 })


for i in range(8, 9):
    print(datetime.datetime.now())
    autotest(str(data[str(i)]['name']), str(
        data[str(i)]['birth']), str(data[str(i)]['pw']))

'''i = 0
while i != 8:
    try:
        print(datetime.datetime.now())
        autotest(str(data[str(i)]['name']),str(data[str(i)]['birth']),str(data[str(i)]['pw']))
        i+=1
    except EnvironmentError:
        print(datetime.datetime.now())
        autotest(str(data[str(i)]['name']),str(data[str(i)]['birth']),str(data[str(i)]['pw']))'''
