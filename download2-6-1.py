from bs4 import BeautifulSoup
import re

html = """
<html><body>
  <ul>
    <li><a id="naver" href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
print(soup.find(id="naver").string)
li = soup.find_all(href=re.compile(r"da")) #정규표현식을 이용

for e in li:
    print(e.attrs["href"])
