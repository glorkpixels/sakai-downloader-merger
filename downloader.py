import requests
import urllib.request
import moviepy.editor as mpe
import os
from time import sleep
lines = []
try:
        
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
        sleep(1)
        resp = urllib.request.urlopen(link1)
        respHtml = resp.read()
        binfile = open(name2, "wb")
        binfile.write(respHtml)
        binfile.close()
        print("sound Download completed..!!")
    except Exception as e:
        print(e)


    try:
        sleep(1)
        print("video Downloading starts...\n")
        urllib.request.urlretrieve(link, name)
        print("video Download completed..!!")
    except Exception as e:
        print(e)
except Exception as e:
        print(e)


