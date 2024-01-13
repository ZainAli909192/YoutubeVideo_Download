
from pytube import YouTube
from time import time

link=input("Paste your url: ")
try:
    youtube_1=YouTube(link)

    print("Title of video is: "+youtube_1.title)
# print(youtube_1.views)
# print(youtube_1.thumbnail_url)

    videos=youtube_1.streams.all()

    vid=list(enumerate(videos))

    for i in vid:
        print(i)

    print()
    strm=int(input("Enter streaming index: "))
    # for downloading time calculate
    # startTime=time.time();

    print("Working on your Download")
    videos[strm].download()

    # endtime=time.time();
    print("Downloaded your video")
    # print("Total time taken is: "+endtime-startTime)
except:
    print("Internet Connectivity issue")
