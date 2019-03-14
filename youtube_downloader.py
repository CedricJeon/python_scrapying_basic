import pytube

#다운 받을 동영상 URL
yt = pytube.YouTube("https://www.youtube.com/watch?v=uQ3fiIixTdQ")
videos = yt.streams.all()
#print("videos", videos)

for i in range(len(videos)):
    print(i, " , ", videos[i])

down_dir = "/Users/Cedric1/youtube"

videos[0].download(down_dir)
