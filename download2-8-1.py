from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import os

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("아이폰")
url = base + quote

res = req.urlopen(url)
savePath = "/Users/Cedric1/imagedown/"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("다운로드 실패!")
        raise

soup = BeautifulSoup(res, "html.parser")

img_list = soup.select("div.img_area > a.thumb._thumb > img")

for i, img_list in enumerate(img_list, 1):
      #print(img_list["data-source"])
      fullFileName = os.path.join(savePath, savePath + str(i) + ".jpg")
      req.urlretrieve(img_list["data-source"], fullFileName)

print("다운로드 완료")
