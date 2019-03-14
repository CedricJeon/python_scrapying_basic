from bs4 import BeautifulSoup
import urllib.parse as rep
import urllib.request as req
import os

base = "https://www.inflearn.com/"
quote = rep.quote_plus("추천-강좌")
url = base + quote

res = req.urlopen(url)
savePath = "/Users/Cedric1/inflearn_recommand/"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Fail to make file")
        raise

soup = BeautifulSoup(res, "html.parser") #html 통채로 소스코드 따오기

img_list = soup.select("ul.slides")[0] #html 내에 있는 첫번째 ul.slides를 img_list함수에 저장 (세분화 작업)

for i, e in enumerate(img_list, 1):
    '''with open(savePath+"text_"+str(i)+".txt","wt") as f:
        f.write(e.select_one("h4.block_title > a").string)''' #이미지 이름을 따로 txt로 저장
    y = e.select_one("h4.block_title > a").string
    fullFileName = os.path.join(savePath, savePath+y+'.png')
    req.urlretrieve(e.select_one("div.block_media > a > img")["src"],fullFileName)

print("다운로드 완료")
