import urllib.request as req
from urllib.parse import urlparse

url = "https://www.youtube.com/?gl=KR&hl=ko"

mem = req.urlopen(url)

print("read", mem.read(50).decode("utf-8"))
print(urlparse(url))
