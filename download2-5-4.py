from bs4 import BeautifulSoup

html = """
<html><body>
<div id="main">
  <h1>강의목록</h1>
  <ul class="lecs">
    <li>Java 초고수 되기</li>
    <li>파이썬 기초 프로그래밍</li>
    <li>파이썬 머신러닝 프로그래밍</li>
    <li>안드로이드 블루투스 프로그래밍</li>
  </ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
h1 = soup.select_one("div#main > h1")   #select_one의 경우 괄호 안 조건에 해당되는 태그 하나만을 지정!
print("h1", h1.string)

list_li = soup.select("div#main > ul.lecs > li") #일반적인 select 메소드의 경우 괄호 안 조건에 해당되는 태그 전부
for li in list_li:                               # --> list 임으로 for문으로 묶어줘야함
    print("li >>>", li.string)
