from bs4 import BeautifulSoup
import os
import os.path
import urllib.request
import requests
import urllib
from time import sleep
import math
import subprocess
from typing import Final
import ffmpeg
class slidesxd:
    def __init__(self,pnglink,ins,out):
        self.pnglink = pnglink
        self.ins = ins
        self.out = out




text=""
with open("Recording Playback.html", "r", encoding='utf-8') as f:
    text= f.read()


pagelink = "https://scalelitey.deu.edu.tr"

soup = BeautifulSoup(text, 'html.parser')

imagesxs = soup.find_all("image", {"class": "slide"})

slidesList = []
print(type(imagesxs))
slides = str(imagesxs).split(",")
for image in slides:
    
    lol=image.split(" ")
    '''   
    print(len(lol))
    print("\n")
    '''
    inx = lol[5].split('"')
    inx = inx[1]
    out = lol[6].split('"')
    out = out[1]
    link = lol[len(lol)-2].split('"')
    link = pagelink +link[1]
   # print(inx + " " + out + " " +link)
    invsld = slidesxd(link, inx,out)
    slidesList.append(invsld)

lo2 = slidesList[0].ins

slidesList[0].ins = 0
lo = slidesList[0].out =lo2

path = os.getcwd()
if not os.path.isdir(path):
    os.mkdir(path)
try:
        count = 0 
        print("Slides Downloading starts...\n")
        for  i in slidesList:
            link =  i.pnglink
            print("slide {count} downloaded")
            name = str(count) + ".png"
            sleep(1)
            resp = urllib.request.urlopen(link)
            respHtml = resp.read()
            binfile = open(name, "wb")
            binfile.write(respHtml)
            
            count = count +1
        binfile.close()
        print("Slides Download completed..!!")
except Exception as e:
    print(e)

info1 = soup.find_all("video", {"class": "webcam"})

xd1 = str(info1)
lol1 = xd1.split("<source src=")
videolinewoparse1 = lol1[1]
vlparsed1 = videolinewoparse1.split(" ",1)
vl1 = vlparsed1[0]
vl1 = vl1.replace('"','')
link1 = pagelink + vl1
print(link1)
namesound = "speech.mp4"

try:
    print("sound Downloading starts...\n")
    sleep(1)
    resp = urllib.request.urlopen(link1)
    respHtml = resp.read()
    binfile = open(namesound, "wb")
    binfile.write(respHtml)
    binfile.close()
    print("sound Download completed..!!")
except Exception as e:
    print(e)



current_dir = os.getcwd()
print(current_dir)

print('Creating mp4 pieces from slides')
for index, slide in enumerate(slidesList):
    sure = float(slide.out) - float(slide.ins)
    subprocess.run(f"ffmpeg -loop 1 -f image2 -r 1 -i {index}.png -c:v libx264 -vf fps=24  -t {sure} -pix_fmt yuv420p {index}.mp4", shell=True)



list_file: Final[str] = f"videos.txt"
print('Creating list file to bind files')
with open(list_file, 'w') as file:
    for i in range(len(slides)):
        file.write(f"file {i}.mp4\n")

merged_file: Final[str] = f"merged.mp4"
print('Merging mp4 pieces')
subprocess.call("ffmpeg -f concat -safe 0 -i videos.txt -c copy output.mp4", shell=True)


input_video = ffmpeg.input('output.mp4')

input_audio = ffmpeg.input('speech.mp4')

print('Creating merged sound and slide video')
try:
    
    ffmpeg.concat(input_video, input_audio, v=1, a=1).output('finished_video.mp4').run()
except Exception as e:
    print(e)
print('Done!')