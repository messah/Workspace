def dizi_anahtari(dizi):
	yeni_dizi = []
	gecici = ''
	for i in dizi:
		if i != '-':
			gecici += i
		else :
			yeni_dizi.append(gecici)
			gecici = ''
	yeni_dizi.append(gecici)
	top = 0
	uzunluk = len(yeni_dizi) 
	for j in range (uzunluk):
		yeni_dizi[j] = int (yeni_dizi[j])
	for k in yeni_dizi:
		top += int(k)
	ort = top / len(yeni_dizi)
	yeni_dizi.sort()
	if  uzunluk% 2 == 0:
		b = (yeni_dizi[uzunluk / 2] + yeni_dizi[uzunluk/2 - 1]) / 2
	else:
		b = int (yeni_dizi[uzunluk / 2])
	print ort * b 
