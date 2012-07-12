from gasp import *
import time
ogrenci_sayi = input("Lutfen ogrenci sayisini giriniz	:")
isim = []
no_t = []
for m in range(ogrenci_sayi):
	ad = raw_input("Ogrenci ismini giriniz	:")
	puan = input("Bu ogrencinin notunu giriniz (0-100)	:")
	while ((puan<0) | (puan>100)):
		print "deger araliginda girmediniz"
		puan = input("Bu ogrencinin notunu giriniz (0-100)	:")
		
	while (puan<round(puan)) | (puan>round(puan)):
		print "belirtilen aralikta tamsayi giriniz"
		puan = input("Bu ogrencinin notunu giriniz (0-100)	:")
	isim.append(ad)
	no_t.append(puan)
begin_graphics(background = (0,0,0))

i = 360
Text("ISIMLER", (50,i+60), color = (255,0,0),size=50)
Text("PUANLAR", (360,i+60), color = (255,0,0),size=50)
Line((0,i+35),(750,i+35),color = (0,0,255))
Line((300,0),(300,750),color = (0,0,255))
for m in range(ogrenci_sayi):
	Text(isim[m], (50,i), color = (255,255,255),size=25)
	Box((300,i), no_t[m] , 25, filled = True, color = (255,255,0))
	i = i - 50
sleep(4)
end_graphics()
