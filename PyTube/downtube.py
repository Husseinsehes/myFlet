

















import yt_dlp

print ("welcome to app to download any video from YouTube")

url = input("Enter the URL of the video: ")

ydl_opts = {
    'format': 'best',
    'outtmpl': '/workspaces/myFlet/PyTube/%(title)s.%(ext)s'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

