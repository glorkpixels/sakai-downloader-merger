# SAKAIDEN VIDEO IZLERKEN KENDINIZI MI KESMEK İSTİYORSUNUZ NEREDE BU 2X DÜĞMESİ NE KADAR YAVAŞ KONUŞMUŞ MU DİYORSUNUZ SİZE BİR ÇÖZÜM


## SAKAI VIDEO TOOL v0.2

YENİ GÜNCELLEME SAYESİNDE İKİ ŞEKİLDE YAPILMIŞ DERSLERİ INDIRIP İZLEYEBİLECEKSİNİZ

```
YENİLİKLER
----------
Sunum pdf vb. paylaşılarak yapılmış derslerin indirilmesi için ikincil bir script eklendi.

Değiştirilen static url düzenlendi.

BÖLÜMDE SINIFI AÇMASINI BEKLEME SİMÜLASYONU BAŞLATILDI

Hoca derse girişimi onaylamayı unuttu büyüsü eklendi.

3 gün sonra gelmeyen kayıtlar boş arazide usbde bulundu.

```

İlk olarak kayıt sayfasına girin ve bir klasöre ctrl-s yaparak html dosyasını kaydedin ve py dosyalarıyla aynı klasöre atın.


> Ekran paylaşımı şeklinde yapılmış dersler için

ikincil olarak parselinks.py yada .exe çalıştırın

oluşan links içindeki urllere giderek kaydedin yada

downloader.py yada .exe çalıştırarak kaydetmesini sağlayın

son olarak mergethedownloads.py yada .exe çalıştırarak iki dosyayı birleştirin.

> Not/slayt/pdf/word paylaşımı şeklinde yapılmış dersler için

ikincil olarak PresentationStyledClassesDownloads.py dosyasını çalıştırın. Bitmesini bekleyin (ses ve oluşturulan video dosyası birleştirmesi 10 dakika sürebiliyor 2 saatlik bir ders için)


> son olarak

Keyifini sürün

## Notes
Birleştirme için videoların ismi

```
video.mp4
```
ve
```
sound.mp4
```
olmalı kendisi öyle kaydediyor. Yani değiştirmezseniz bir problem olmaz


## Dependencies:
notları okumadan bot gibi dependencies kurmadan çalıştırdınız mı?
```
v0.2 YENİLİKLER
----------
Yeni dependenciesi çıkarmaya üşendim hata verdikçe kurun işte.
```

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



### Sorunları mı var?
Evet downloader yavaş indiriyor.

Bu sebeple link.txt girip kaydederseniz daha hızlı olur

~~Ekran paylaşımı şeklinde yapılmış derslerde denendi.~~ Her derste çalışır. Yani. Büyük ihtimalle.

### bug var?
e düzeltin valla o kadar yaptık pull requests orada.
