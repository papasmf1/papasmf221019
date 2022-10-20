# web2.py
#웹서버와 통신
import urllib.request
#웹크롤링
from bs4 import BeautifulSoup

data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
#검색이 용이한 객체
soup = BeautifulSoup(data, "html.parser")
#필터링: <td class="title">
cartoons = soup.find_all("td", class_="title")
print("갯수:{0}".format( len(cartoons) ))
title = cartoons[0].find("a").text 
link = cartoons[0].find("a")["href"]
print( title )
print( link )
#<td class="title">
# 	<a href="/webtoon/detail?">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>

for item in cartoons:
    title = item.fine("a").text 
    print(title)