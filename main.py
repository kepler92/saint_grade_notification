from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time

import setting
import notice

try:
    import __secret_key as secret_key
except:
    import secret_key

driver_root = setting.driver()
driver = webdriver.PhantomJS(driver_root + 'phantomjs')

driver.get(secret_key.urlm)

driver.find_element_by_xpath('//*[@id="userid"]').send_keys(secret_key.receiver_id)
driver.find_element_by_xpath('//*[@id="passwd"]').send_keys(secret_key.receiver_pw)
driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()

beforeTable = ''
beforeSubject = set()

idx = 1
while idx:
    print (str(idx) + ' Times', end='')
    driver.get(secret_key.urlg)

    select = Select(driver.find_element_by_xpath('//*[@id="semesteridx"]'))

    try:
        select.select_by_value(setting.semester())
    except:
        select.select_by_index(1)

    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    gradeSection = soup.find_all('div', id='divDetailView')
    gradeTable = gradeSection[0].find_all('table')

    if gradeTable != beforeTable:
        gradeTableRow = gradeTable[0].find_all('tr')

        nowSubject = set()
        for i in range(1, len(gradeTableRow)):
            nowSubject.add(gradeTableRow[i])
        newSubject = nowSubject - beforeSubject

        if idx is not 1:
            subjectList = list()

            for i in range(len(newSubject)):
                tableRow = str(newSubject.pop())
                subjectList.append(tableRow)
            subjectList.sort()

            gradeTableHeader = str(gradeTableRow[0])
            subjectList.insert(0, gradeTableHeader)

            notice.sendMessage(secret_key.receiver_email, setting.message_format(subjectList))
            print (" > 변경점 발견, 메일이 발송되었습니다.", end='')

        beforeSubject = nowSubject

    beforeTable = gradeTable

    idx += 1
    print()

    time.sleep(setting.refresh_time)
