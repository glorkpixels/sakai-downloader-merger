# SAKAIDEN VIDEO IZLERKEN KENDINIZI MI KESMEK İSTİYORSUNUZ SİZE BİR ÇÖZÜM
## SAKAI PARSER - DOWNLOADER - MERGER.

İlk olarak kayıt sayfasına girin ve bir klasöre ctrl-s yaparak html dosyasını kaydedin ve py dosyalarıyla aynı klasöre atın.

ikincil olarak parselinks.py yada .exe çalıştırın
oluşan links içindeki urllere giderek kaydedin yada
downloader.py yada .exe çalıştırarak kaydetmesini sağlayın
son olarak mergethedownloads.py yada .exe çalıştırarak iki dosyayı birleştirin.


## Notes
Birleştirme için videoların ismi

```
video.mp4
```
ve
```
sound.mp4
```
olmalı


Dependencies:
notları okumadan
bot gibi dependencies kurmadan çalıştırdınız mı?
boşuna mı okuyorsunuz?


işte size listemiz:

for parselinks.py :
```
pip install beautifulsoup4
```
for downloader.py :
```
pip install urllib3
pip install requests
pip install moviepy
```
for mergethedownloads.py:

birleştirme için ilk
```
https://www.wikihow.com/Install-FFmpeg-on-Windows ----> bu adımları uygulayın bir reboot alalım sonra

pip install ffmpeg-python
```
ffmpeg normal şekilde kurulu olmazsa kütüphane çalışmıyor :)))))


## Sorun mu var?
Evet downloader yavaş indiriyor.
Bu sebeple link.txt girip kaydederseniz daha hızlı olur :))))
Ekran paylaşımı şeklinde yapılmış derslerde denendi.

### bug var? açın öğrenin kendiniz tamir edin.
