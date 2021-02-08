import requests
import urllib.request
import moviepy.editor as mpe
import os
lines = []
with open("link.txt") as file_in:
    
    for line in file_in:
        lines.append(line)
link = lines[0]
link1 = lines[1]

os.remove("link.txt")
name = "video.mp4"
name2 = "sound.mp4"

try:
    print("sound Downloading starts...\n")
    urllib.request.urlretrieve(link1, name2)
    resp = urllib.urlopen(link1)
    respHtml = resp.read()
    binfile = open(name2, "wb")
    binfile.write(respHtml)
    binfile.close()
    print("sound Download completed..!!")
except Exception as e:
        print(e)


try:
    print("video Downloading starts...\n")
    urllib.request.urlretrieve(link, name)
    print("video Download completed..!!")
except Exception as e:
    print(e)
