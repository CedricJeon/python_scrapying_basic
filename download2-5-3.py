from bs4 import BeautifulSoup

html = """
<html><body>
  <ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a")
a = soup.find_all("a", string="daum") # a태그 + "daum" 스트링을 가진 태그
b = soup.find_all("a", limit=2) # a태그 + limit이하 갯수의 스트링 태그
c = soup.find_all(string=["naver", "daum"]) #스트링이 naver, daum인 태그 **스트링만 변수에 저장
print('a', a)
print('b', b)
print('c', c)


for a in links:
    href = a.attrs["href"]
    txt = a.string
    print("txt >> ", txt, ',', "href >> ", href)
