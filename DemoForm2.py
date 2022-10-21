# DemoForm2.py
# DemoForm2.ui(화면) + DemoForm2.py(로직 구현)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
#웹서버와 통신
import urllib.request
#웹크롤링
from bs4 import BeautifulSoup

#화면을 로딩(DemoForm2.ui)
form_class = uic.loadUiType("DemoForm2.ui")[0]

#폼 클래스 정의(QMainWindow로 변경)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #슬롯메서드 추가 
    def firstClick(self):
        f = open("c:\\work2\\webtoon.txt", "wt", encoding="utf-8")
        for i in range(1,6):
            url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
            print( url )
            data = urllib.request.urlopen(url)
            #검색이 용이한 객체
            soup = BeautifulSoup(data, "html.parser")
            #필터링: <td class="title">
            cartoons = soup.find_all("td", class_="title")
            for item in cartoons:
                title = item.find("a").text 
                print(title)
                f.write(title + "\n")
        f.close() 
        self.label.setText("네이버 웹툰 크롤링 완료")
    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭~~")

#진입점 체크(직접 실행한 경우 윈도우 생성)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm() 
    demoWindow.show()
    app.exec_() 