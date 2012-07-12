def Liste_anaLizi(liste):
	sayac1,sayac2,sayac3,sayac4,sayac5 = 0,0,0,0,0 
	for i in range(len(liste)):
                if type(liste[i])==int:
			sayac1 += 1
		elif type(liste[i]) == str:
			sayac2 += 1
		elif type(liste[i]) == float:
			sayac3 += 1
		elif type(liste[i]) == list:
			sayac4 += 1
		else:
                        sayac5 += 1
	print "Karakter dizisi sayisi\t:\t",sayac2
	print "Tamsayi sayisi\t\t:\t" ,sayac1
	print "Ondaliksayi sayisi\t:\t",sayac3
	print "Boolean sayisi\t\t:\t",sayac5
	print "Liste sayisi\t\t:\t",sayac4
