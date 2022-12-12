from __future__ import unicode_literals
import youtube_dl
print("Insert the link: ")
link = input ("")

ydl_opts = {
    'format': 'bestvideo/best',
    'postprocessors': [{
        'key': 'FFmpegExtractVideo',
        'preferredcodec': 'mp4',
        'preferredquality': '320',
    }],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
print("DONE BISH")