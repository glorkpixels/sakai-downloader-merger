from bs4 import BeautifulSoup

text=""
with open("Recording Playback.html", "r", encoding='utf-8') as f:
    text= f.read()



pagelink = "https://scalelite.deu.edu.tr"

soup = BeautifulSoup(text, 'html.parser')
info = soup.find_all("video", {"id": "deskshare-video"})

xd = str(info)
lol = xd.split("source src=")
videolinewoparse= lol[2]
vlparsed = videolinewoparse.split(" ",1)
vl = vlparsed[0]
vl = vl.replace('"','')
print(vl)


link = pagelink + vl
print(link)


info1 = soup.find_all("video", {"class": "webcam"})

xd1 = str(info1)
lol1 = xd1.split("<source src=")
videolinewoparse1 = lol1[2]
vlparsed1 = videolinewoparse1.split(" ",1)
vl1 = vlparsed1[0]
vl1 = vl1.replace('"','')
link1 = pagelink + vl1
print(link1)


name = "video.mp4"
name2 = "sound.mp4"
f = open("link.txt", "a")
f.write(link +"\n")
f.write(link1)
f.close()

"""

try:
        print("sound Downloading starts...\n")
        urllib.request.urlretrieve(link1, name2)
        print("sound Download completed..!!")
except Exception as e:
        print(e)


try:
    print("video Downloading starts...\n")
    urllib.request.urlretrieve(link, name)
    print("video Download completed..!!")
except Exception as e:
    print(e)



try:
        print("sound Downloading starts...\n")
        urllib.request.urlretrieve(link1, name2)
        resp = urllib2.urlopen(link1)
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
"""