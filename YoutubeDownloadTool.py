#   {things to take note of :}
# (pip install pytube) in cmd to download pytube library, google it if you dont get what i mean ,
#  have python installed , duhh  

#   YoutubeVideoDownloader
#  takes abt 1-5 sec( net. speed dependent ) , max resolution is about 480p,  why u ask ?
#  due to some dumb shit video compression thing of YT.

import pytube  
from pytube import YouTube  
video_url = 'https://www.youtube.com/watch?v=rtOvBOTyX00&list=RDG1ajxH07b7w&index=4'   #link , paste it here.
youtube = pytube.YouTube(video_url)  
video = youtube.streams.get_highest_resolution()  
video.download('D:\youtube songs') # location where you want to download videos
print("completed !!")  
