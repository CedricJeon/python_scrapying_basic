import urllib.request as ub

imgUrl = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EB%93%9C%EB%9F%BC#"
htmlUrl = "http://google.com"

savePath1 = "/Users/Cedric1/Pictures/Drum.jpg"
savePath2 = "/Users/Cedric1/Pictures/index.html"

ub.urlretrieve(imgUrl, savePath1)
ub.urlretrieve(htmlUrl, savePath2)



print("다운로드 완료")
