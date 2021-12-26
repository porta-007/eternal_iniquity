
#   YoutubeVideoDownloader
#  takes abt 5-10 sec( net. speed dependent ) , max reslution is about 480p,  why u ask ?
#  due to some dumb shit video compression thing of YT.

import pytube  
from pytube import YouTube  
video_url = 'https://www.youtube.com/watch?v=rtOvBOTyX00&list=RDG1ajxH07b7w&index=4'   #link paste kr 
youtube = pytube.YouTube(video_url)  
video = youtube.streams.get_highest_resolution()  
video.download('D:\youtube songs') # location where you want to download videos
print("completed !!")  