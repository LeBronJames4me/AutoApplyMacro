import csv
from threading import Timer

import selenium
from PyQt5 import QtCore, QtGui, QtWidgets
import time
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

# 창 안뜨고 실행하게 하는 옵션
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--disable-gpu')
options.add_argument('lang=ko_KR')


# 크롬 드라이버 열기
driver = webdriver.Chrome('./chromedriver')
# driver = webdriver.Chrome('./chromedriver', options=options)

driver.get('http://www.gbgs.go.kr/swimmingpool/login/courseLogin.do')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Swimming Macro")
        MainWindow.resize(900, 950)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 제목라인
        self.desc = QtWidgets.QTextBrowser(self.centralwidget)
        self.desc.setGeometry(QtCore.QRect(130, 50, 671, 121))
        self.desc.insertPlainText("여기에 메세지가 출력 됩니다.\n")
        self.desc.insertPlainText("수영 재밌게 하고 오세요!!! \n -아들 재현-\n")
        self.desc.setObjectName("Title")

        # Label
        self.label_ID = QtWidgets.QLabel(self.centralwidget)
        self.label_ID.setGeometry(QtCore.QRect(140, 210, 171, 141))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.label_ID.setFont(font)
        self.label_ID.setObjectName("label_ID")

        # Label
        self.label_pw = QtWidgets.QLabel(self.centralwidget)
        self.label_pw.setGeometry(QtCore.QRect(140, 350, 171, 141))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.label_pw.setFont(font)
        self.label_pw.setObjectName("label_pw")

        # 타임 라벨
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(130, 650, 171, 141))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label_time.setFont(font)
        self.label_time.setObjectName("label_time")

        # ID 입력
        self.input_id = QtWidgets.QLineEdit(self.centralwidget)
        self.input_id.setGeometry(QtCore.QRect(320, 260, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.input_id.setFont(font)
        # self.input_id.setText("")
        self.input_id.setObjectName("input_id")

        # PW입력
        self.input_pw = QtWidgets.QLineEdit(self.centralwidget)
        self.input_pw.setGeometry(QtCore.QRect(320, 390, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.input_pw.setFont(font)
        self.input_pw.setText("")
        self.input_pw.setObjectName("input_pw")

        # 로그인 버튼
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(320, 510, 271, 131))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(36)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")

        self.btn_login.clicked.connect(self.login)

        # 분리선
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 640, 961, 16))
        self.line.setLineWidth(9)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        # 시간 콤보 박스
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(330, 700, 441, 51))
        self.comboBox.setObjectName("comboBox")

        self.groupbox = QtWidgets.QGroupBox(self.centralwidget)
        """
        # self.groupbox.setFlat(True)
        font.setPointSize(18)
        self.groupbox.setFont(font)
        self.time0 = QtWidgets.QCheckBox('06:00-07:30')
        self.time1 = QtWidgets.QCheckBox('08:00-09:30')
        self.time2 = QtWidgets.QCheckBox('10:00-11:30')
        self.time3 = QtWidgets.QCheckBox('12:00-13:30')
        self.time4 = QtWidgets.QCheckBox('14:00-15:30')
        self.time5 = QtWidgets.QCheckBox('16:00-17:30')

        vbox = QtWidgets.QVBoxLayout()

        vbox.addWidget(self.time0)
        vbox.addWidget(self.time1)
        vbox.addWidget(self.time2)
        vbox.addWidget(self.time3)
        vbox.addWidget(self.time4)
        vbox.addWidget(self.time5)
        vbox.addStretch(1)
        self.groupbox.setLayout(vbox)
        # self.groupbox.setGeometry(QtCore.QRect(370, 800, 300, 300))
        self.groupbox.setGeometry(QtCore.QRect(450, 900, 300, 300))
        """


        # 실행 버튼
        self.btn_apply = QtWidgets.QPushButton(self.centralwidget)
        self.btn_apply.setGeometry(QtCore.QRect(320, 780, 311, 101))
        font = QtGui.QFont()
        font.setFamily("Haettenschweiler")
        font.setPointSize(36)
        self.btn_apply.setFont(font)
        self.btn_apply.setObjectName("btn_apply")
        self.btn_apply.clicked.connect(self.run)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 932, 38))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        self.label_ID.setText("I D")
        self.label_pw.setText("PW")
        self.btn_login.setText("Log In")
        self.label_time.setText("Time")
        self.btn_apply.setText("Run")
        #self.autoload()

        # self.comboBox.addItem('1'+':'+'aaa')

    def login(self):
        # 정보입력
        # id 입력
        myid = driver.find_element_by_id("user_id")
        myid.send_keys(self.input_id.text())
        #myid.send_keys('ajpuop')

        # pwd 입력
        mypw = driver.find_element_by_id("user_pw")
        mypw.send_keys(self.input_pw.text())
        #mypw.send_keys('tjwogus*1019')

        # 로그인 버튼 클릭
        elem = driver.find_element_by_class_name("log_btn")
        elem.click()



        # 알림 처리
        try:
            WebDriverWait(driver, 10).until(EC.alert_is_present(),
                                           'Timed out waiting for PA creation ' +
                                           'confirmation popup to appear.')

            alert = driver.switch_to.alert
            self.desc.insertPlainText(alert.text)

            """
            #아이디csv에 저장
            f = open('settings.csv', 'w', encoding='utf-8', newline='')
            wr = csv.writer(f)

            wr.writerow([self.input_id.text(),self.input_pw.text()])

            f.close()
            """
            print(alert.text)
            alert.accept()

        except TimeoutException:
            print("no alert")

        driver.find_element_by_link_text("일일 자유수영 신청").click()

        table = driver.find_element_by_xpath("//*[@id='spage']/table/tbody")

        for tr in table.find_elements_by_tag_name("tr"):
            td = tr.find_elements_by_tag_name("td")
            # s = "{},{},{}\n".format(td[1].text, td[2].text, td[8].text)
            k = "{}".format(td[1].text)
            self.comboBox.addItem(k)
            print(k)

        # 창 닫기
        # driver.close()

    def run(self):
        cnt = 0

        while True:

            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='spage']/table/tbody"))
            )
            selected_time = self.comboBox.currentText()


            table = driver.find_element_by_xpath("//*[@id='spage']/table/tbody")
            for tr in table.find_elements_by_tag_name("tr"):
                td = tr.find_elements_by_tag_name("td")
                if (selected_time == td[1].text):
                    break

            if (td[8].text == '접수마감'):
                # self.desc.append(td[1].text + td[8].text)
                print(td[1].text + td[8].text)
                print(cnt)
                cnt += 1
                # continue
            else:
                td[8].click()

                try:
                    WebDriverWait(driver, 1).until(EC.alert_is_present(),
                                                   'Timed out waiting for PA creation ' +
                                                   'confirmation popup to appear.')

                    alert = driver.switch_to.alert
                    alert.accept()


                    WebDriverWait(driver, 1).until(EC.alert_is_present(),
                                                   'Timed out waiting for PA creation ' +
                                                   'confirmation popup to appear.')
                    alert = driver.switch_to.alert
                    self.desc.insertPlainText(alert.text)
                    alert.accept()

                    break

                except TimeoutException:
                    print("no alert")

            driver.refresh()



    def autoload(self):
        # 1970년 1월 1일 0시 0분 0초 부터 현재까지 경과시간 (초단위)
        t = time.time()
        # 한국 시간 얻기
        kor = time.localtime(t)
        time_now = str(kor.tm_hour) + ':' + str(kor.tm_min) + ':' + str(kor.tm_sec)
        print(time_now)

        # 타이머 설정  (1초마다, 콜백함수)
        timer = Timer(1, self.autoload)
        timer.start()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
