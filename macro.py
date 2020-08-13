import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert



#창 안뜨고 실행하게 하는 옵션
options =webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--disable-gpu')
options.add_argument('lang=ko_KR')


#크롬 드라이버 열기
driver = webdriver.Chrome('chromedriver')
#driver = webdriver.Chrome('./chromedriver', chrome_options=options)
driver.get('http://www.gbgs.go.kr/swimmingpool/login/courseLogin.do')


#정보입력
# id 입력
elem = driver.find_element_by_id("user_id")
elem.send_keys('ajpuop')
#pwd 입력
elem = driver.find_element_by_id("user_pw")
elem.send_keys('tjwogus*1019')
# 로그인 버튼 클릭
elem = driver.find_element_by_class_name("log_btn")
elem.click()

time.sleep(1)

#알림 처리
alert_text = driver.switch_to.alert.text
print(alert_text)
alert = driver.switch_to.alert
alert.accept()

#time.sleep(1)
driver.find_element_by_link_text("일일 자유수영 신청").click()

#time.sleep(1)

table = driver.find_element_by_xpath("//*[@id='spage']/table/tbody")

for tr in table.find_elements_by_tag_name("tr"):
    td = tr.find_elements_by_tag_name("td")
    s = "{} , {}\n".format(td[1].text , td[2].text)
    print (s)


#창 닫기
driver.close()