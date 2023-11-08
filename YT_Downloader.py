from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("Number of views: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download("/Users/root1/Desktop/")

print("Download completed!!")