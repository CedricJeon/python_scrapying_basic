from bs4 import BeautifulSoup

html = """
<html>
<body>
<h1>파이썬 BeautifulSoup 공부</h1>
<p>html선택자</p>
<p>css선택자</p>
</body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify()) <--들여쓰기

h1 = soup.html.body.h1
print('h1', h1)
p1 = soup.html.body.p
print('p1', p1)
p2 = p1.next_sibling.next_sibling
print('p2', p2)
p3 = p1.previous_sibling.previous_sibling
print('p3', p3)

print("h1 >>", h1.string)
print("p1 >>", p1.string)
print("p2 >>", p2.string)
print("p3 >>", p3.string)
