import pytube
import op
import subprocess

#다운 받을 동영상 URL
yt = pytube.YouTube("https://www.youtube.com/watch?v=uQ3fiIixTdQ")
videos = yt.streams.all()
#print("videos", videos)

for i in range(len(videos)):
    print(i, " , ", videos[i])

cNum = int(input("다운 받을 화질을 입력하세요.(0-17 중 선택)"))

down_dir = "/Users/Cedric1/youtube"

videos[cNum].download(down_dir)

newFileName = input("변환할 파일 mp3 이름을 입력하세요(.mp3를 입력)")
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg','-i',
    os.path.join(down_dir,oriFileName),
    os.path.join(down_dir,newFileName)
])


print("동영상 다운로드 및 mp3 변환 완료")
