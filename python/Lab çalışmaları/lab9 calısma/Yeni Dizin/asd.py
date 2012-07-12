import csv
okunacak_dosya = 'firmalar.csv'
dosya_tutacagi = open(okunacak_dosya)
okuyucu = csv.reader("firmalar.txt")
sira = 1
for satir in okuyucu:
    print "Firma No :", sira
    print " Firma Adi :", satir[0]
    print " Firma Turu :", satir[1]
    print " Ulke        :", satir[2]
    sira = sira + 1
dosya_tutacagi.close()
