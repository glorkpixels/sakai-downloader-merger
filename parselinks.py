from bs4 import BeautifulSoup

text=""
with open("Recording Playback.html", "r", encoding='utf-8') as f:
    text= f.read()



pagelink = "https://scalelitey.deu.edu.tr"

soup = BeautifulSoup(text, 'html.parser')
info = soup.find_all("video", {"id": "deskshare-video"})

xd = str(info)
lol = xd.split("source src=")
videolinewoparse= lol[1]
vlparsed = videolinewoparse.split(" ",1)
vl = vlparsed[0]
vl = vl.replace('"','')
print(vl)


link = pagelink + vl
print(link)

info1 = soup.find_all("video", {"class": "webcam"})

xd1 = str(info1)
lol1 = xd1.split("<source src=")
videolinewoparse1 = lol1[1]
vlparsed1 = videolinewoparse1.split(" ",1)
vl1 = vlparsed1[0]
vl1 = vl1.replace('"','')
link1 = pagelink + vl1
print(link1)
f = open("link.txt", "a")
f.write(link +"\n")
f.write(link1)
f.close()


