import urllib.request as ub

imgUrl = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EB%93%9C%EB%9F%BC#"
htmlUrl = "http://google.com"

savePath1 = "/Users/Cedric1/Pictures/Drum.jpg"
savePath2 = "/Users/Cedric1/Pictures/index.html"

f = ub.urlopen(imgUrl).read()
f2 = ub.urlopen(htmlUrl).read()

saveFile1 = open(savePath1, 'wb')
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료")
